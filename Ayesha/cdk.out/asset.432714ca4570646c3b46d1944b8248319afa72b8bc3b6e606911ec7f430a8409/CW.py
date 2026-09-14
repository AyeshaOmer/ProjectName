import boto3


def putMetric(namespace, metric, url, value):
    client = boto3.client('cloudwatch')
    return client.put_metric_data(
                Namespace=namespace,
                MetricData=[
                    {
                        'MetricName': metric,
                        'Dimensions': [
                            {
                                'Name': 'url',
                                'Value': url
                            },
                        ],
                        
                        'Value': value,     
                    }
                ]
            )