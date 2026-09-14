import boto3
import constants


def lambda_handler(event, context):
    print(event)
    client = boto3.client('cloudwatch')
#    you compute the 3 metrics in this application
# Following values are being used as an example. you are expected to compute these 
availability = 1
latency = 0.23

response = client.put_metric_data(
    Namespace=constants.namespace,
    MetricData=[
        {
            'MetricName': constants.metricAvailability,
            'Dimensions': [
                {
                    'Name': 'URL',
                    'Value': constants.URL
                },
            ],
            
            'Value': availability,
        }   
    ],    
)

response = client.put_metric_data(
    Namespace=constants.namespace,
    MetricData=[
        {
            'MetricName': constants.metricLatency,
            'Dimensions': [
                {
                    'Name': 'URL',
                    'Value': constants.URL
                },
            ],
            
            'Value': latency,
        }   
    ],    
)
return response

    