import boto3
import constants

def lambda_handler(event, context):
    print(event)
    client = boto3.client("CloudWatch")
    
    # you are expected to obtain the metrics for all URLS. 
    # Following values are being used only for code demonstration
    availability = 0
    latency = 0.23



    response = client.put_metric_data(
        Namespace=constants.ASH_NAMESPACE,
        MetricData=[
            {
                'MetricName': constants.AVAILABILITY_METRIC,
                'Dimensions': [
                    {
                        'Name': 'url',
                        'Value': client.URL
                    },
                ],
                
                'Value': availability,     
            }
        ]
    )

    response = client.put_metric_data(
        Namespace=constants.ASH_NAMESPACE,
        MetricData=[
            {
                'MetricName': constants.LATENCY_METRIC,
                'Dimensions': [
                    {
                        'Name': 'url',
                        'Value': client.URL
                    },
                ],
                
                'Value': latency,     
            }
        ]
    )

    