from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    RemovalPolicy,
    aws_lambda as lambda_,
    aws_events as events_,
    aws_events_targets as targets_,
    Duration,
    aws_iam as iam_,
    aws_cloudwatch as cw,
    aws_sns as sns_,
    aws_cloudwatch_actions as cwaction_,
    aws_sns as sns_,
    aws_sns_subscriptions as subscriptions_,
)
from constructs import Construct
from resources import constants as C

class AyeshaStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_iam/Role.html
        user_role = iam_.Role(self, 
            "CWMetricPublishRole",
            assumed_by=iam_.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies = [iam_.ManagedPolicy.from_aws_managed_policy_name("CloudWatchFullAccess")]
        )
        user_role.apply_removal_policy(RemovalPolicy.DESTROY)

        #  https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_lambda/Function.html
        fn = lambda_.Function(
            self, 
            "WebhealthApplication",
             code=lambda_.Code.from_asset("./resources"),
             handler="webhealth.lambda_handler",
             runtime=lambda_.Runtime.PYTHON_3_12,
             role = user_role
        )
        fn.apply_removal_policy(RemovalPolicy.DESTROY)

        # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_events/Schedule.html
        Schedule = events_.Schedule.rate(Duration.minutes(5)) 

        # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_events_targets/LambdaFunction.html
        Target = [targets_.LambdaFunction(fn)]

        # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_events/Rule.html
        Rule = rule = events_.Rule(self, 
            "LambdaSchedule",
            schedule=Schedule,
            targets = Target
        )
        Rule.apply_removal_policy(RemovalPolicy.DESTROY)

        # # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_cloudwatch/Metric.html
        # dimensions_map={"URL": C.URL}
        # latencyMetric = cw.Metric(
        #     namespace=C.namespace,
        #     metric_name=C.metricLatency,
        #     dimensions_map=dimensions_map     
        # )        

        # # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_cloudwatch/Metric.html
        # availabilityMetric = cw.Metric(
        #     namespace=C.namespace,
        #     metric_name=C.metricAvailability,
        #     dimensions_map=dimensions_map     
        # )
        # # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_cloudwatch/Alarm.html
        # availabilityAlarm = cw.Alarm(self, "availAlarm",
        #     metric=availabilityMetric,
        #     threshold=1,
        #     comparison_operator = cw.ComparisonOperator.LESS_THAN_THRESHOLD
        # )
        # availabilityAlarm.apply_removal_policy(RemovalPolicy.DESTROY)
        # availabilityAlarm.add_alarm_action(topic)

        # # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_cloudwatch/Alarm.html
        # latencyAlarm = cw.Alarm(self, "latencyAlarm",
        #     metric=latencyMetric,
        #     threshold=0.2,
        #     comparison_operator = cw.ComparisonOperator.GREATER_THAN_THRESHOLD
        # )
        # latencyAlarm.apply_removal_policy(RemovalPolicy.DESTROY)
        # latencyAlarm.add_alarm_action(topic)
        
        # # should have created your cloudwatch dashboard as well

        # # Notification service to notify ourselves of any significant change in our metric
        # topic = sns_.Topic(self, "AlarmNotifications")
        # topic.add_subscription(subscriptions_.EmailSubscription(a.ashfaq@westernsydney.edu.au))
        # topic.add_subscription(subscriptions_.LambdaSubscription(fn_Database))
        
        # # logging alarm information in a DynamoDB databse
         
        