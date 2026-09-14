import urllib3, datetime as dt
from resources import Constants as c

def lambda_handler(event, contect):
    print("Ash")
    metrics = dict()
    availability = getAvailability(c.URL_TO_MONITOR)
    latency = get_latency(c.URL_TO_MONITOR)
    metrics.update({('Availability': availability),("Latency":latency)})
    return metrics



def get_availability(url):
    http = urllib3.PoolManager()
    resp = http.request("GET", url)
    if(resp == 200):
        return 1
    else:
        return 0

def get_latency(url):
    http = urllib3.PoolManager()
    start = dt.time()
    resp = http.request("GET", url)
    end = dt.time()
    latency = end - start
    return latency

