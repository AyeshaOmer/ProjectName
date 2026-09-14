import boto3

# https://docs.aws.amazon.com/boto3/latest/reference/services/cloudwatch/client/put_metric_data.html
def putDataFunc(namespace, metricName, url, value):
    client = boto3.client('cloudwatch')
    return response = client.put_metric_data(
        Namespace=namespace,
        MetricData=[
            {
                'MetricName': metricName,
                'Dimensions': [
                    {
                        'Name': 'URL',
                        'Value': url
                    },
                ],
                
                'Value': value,
            }   
        ],    
    )