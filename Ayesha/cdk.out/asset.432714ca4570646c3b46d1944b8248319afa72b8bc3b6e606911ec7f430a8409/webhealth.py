import CW
import constants

def lambda_handler(event, context):
    print(event)
        
    # you are expected to obtain the metrics for all URLS. 
    # Following values are being used only for code demonstration
    availability = 0
    latency = 0.23


    response = CW.putMetric(constants.namespace,constants.metricAvailability,constants.URL,availability)
    response = CW.putMetric(constants.namespace,constants.metricLatency,constants.URL,latency)

    return response

    