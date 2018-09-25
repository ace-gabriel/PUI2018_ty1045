# PUI_HW2 Part III
# Gabriel Yin - ty1045 - N10088627

import pandas as pd
import numpy as np
import requests
import json
import sys, os


URL = "http://bustime.mta.info/api/siri/vehicle-monitoring.json"

def get_params():
    # a dictionary that contains all the necessary needed for the request
    if len(sys.argv) != 3:
        print("Invalid arguments. Please run as python3 show_bus_locations_ty1045.py <MTA_KEY> <BUS_LINE>")
        sys.exit()
    # return the formatted output as a dictionary
    return {"key": sys.argv[1], "LineRef": sys.argv[2], "VehicleMonitoringDetailLevel": "calls"}

def request_results(params):
    # make request and retrieve the results
    resp = requests.get(URL, params=params).json()
    # handle garbage value
    if 'VehicleActivity' not in resp['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0].keys():
        return None, None
    # handle regular situations
    info = resp['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
    locations = list(info[i]['MonitoredVehicleJourney']['VehicleLocation'] for i in range(0, len(info)))
    num_bus, locations = len(locations), locations
    return num_bus, locations

def formatted_result(line, num_bus, locations,):
    # simply print the well formated result
    """
    Bus Line : B52
    Number of Active Buses : 5
    Bus 0 is at latitude 40.687241 and longitude -73.941661
    Bus 1 is at latitude 40.690822 and longitude -73.920759
    Bus 2 is at latitude 40.688363 and longitude -73.979563
    Bus 3 is at latitude 40.688282 and longitude -73.979356
    Bus 4 is at latitude 40.686839 and longitude -73.964694
    """
    print("Bus Line : %s" % line)
    print("Number of Active Buses : %d" % num_bus)
    for i in np.arange(0, num_bus):
        print("Bus %d is at latitude %f and longitude %f" %(i, locations[i]['Latitude'], locations[i]['Longitude']))
    return locations

if __name__ == '__main__':

    params = get_params()
    num_bus, locations = request_results(params)
    if num_bus == None and locations == None:
        print("The line number you entered doesn't return any results. ")
    else:
        result = formatted_result(params['LineRef'], num_bus, locations)
