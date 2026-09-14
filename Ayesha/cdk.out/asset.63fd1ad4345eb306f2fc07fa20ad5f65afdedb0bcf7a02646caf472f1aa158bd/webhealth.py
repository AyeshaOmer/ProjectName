import boto3
import constants

def lambda_handler(event, context):
    print(event)
    client = boto3.client('cloudwatch')
    
    # you are expected to obtain the metrics for all URLS. 
    # Following values are being used only for code demonstration
    availability = 0
    latency = 0.23



    response = client.put_metric_data(
        Namespace=constants.namespace,
        MetricData=[
            {
                'MetricName': constants.metricAvailability,
                'Dimensions': [
                    {
                        'Name': 'url',
                        'Value': constants.URL
                    },
                ],
                
                'Value': availability,     
            }
        ]
    )

    response = client.put_metric_data(
        Namespace=constants.namespace,
        MetricData=[
            {
                'MetricName': constants.metricLatency,
                'Dimensions': [
                    {
                        'Name': 'url',
                        'Value': constants.URL
                    },
                ],
                
                'Value': latency,     
            }
        ]
    )

    