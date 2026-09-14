
import constants
import CWPutData as cw

def lambda_handler(event, context):
    print(event)
    
    #  you compute the 3 metrics in this application
    # Following values are being used as an example. you are expected to compute these 
    availability = 1
    latency = 0.23


    response = cw.putDataFunc(constants.namespace, constants.metricAvailability, constants.URL, availability )
    response = cw.putDataFunc(constants.namespace, constants.metricLatency, constants.URL, latency )


    return response

    