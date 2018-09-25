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
    if len(sys.argv) != 4:
        print("Invalid arguments. Please run as python3 get_bus_info_ty1045.py <MTA_KEY> <BUS_LINE> <BUS_LINE>.csv")
        sys.exit()
    # return the formatted output as a dictionary and filename
    return {"key": sys.argv[1], "LineRef": sys.argv[2].upper(), "VehicleMonitoringDetailLevel": "calls"}, sys.argv[3]

def request_results(params):
    # make request and retrieve the results
    resp = requests.get(URL, params=params).json()
    # handle garbage value
    if 'VehicleActivity' not in resp['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0].keys():
        return None, None
    # handle regular situations
    info = resp['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
    locations = list(info[i]['MonitoredVehicleJourney']['VehicleLocation'] for i in range(0, len(info)))
    stops = list(info[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'] if len(info[i]['MonitoredVehicleJourney']['OnwardCalls']) > 0 else 'N/A' for i in range(0, len(info)))
    stop = list(item[0]['StopPointName'] if item != 'N/A' else 'N/A' for item in stops)
    status = list(item[0]['Extensions']['Distances']['PresentableDistance'] if item != 'N/A' else 'N/A' for item in stops)
    # return locations, stop, status
    return locations, stop, status


def formatted_result(locations, stops, status):

    """
    Latitude,Longitude,Stop Name,Stop Status
    40.755489,-73.987347,7 AV/W 41 ST,at stop
    40.775657,-73.982036,BROADWAY/W 69 ST,approaching
    40.808332,-73.944979,MALCOLM X BL/W 127 ST,approaching
    40.764998,-73.980416,N/A,N/A
    40.804702,-73.947620,MALCOLM X BL/W 122 ST,< 1 stop away
    40.776950,-73.981983,AMSTERDAM AV/W 72 ST,< 1 stop away
    40.737650,-73.996626,AV OF THE AMERICAS/W 18 ST,< 1 stop away
    """
    # dump data into a dataframe and then output to a csv file
    lat = list(item['Latitude'] for item in locations)
    long = list(item['Longitude'] for item in locations)
    df_dic = {'Latitude' : lat, 'Longitude' : long, 'Stop Name' : stops, 'Stop Status' : status}
    df = pd.DataFrame(data=df_dic)
    return df

if __name__ == '__main__':
    # main function of this program
    params, filename = get_params()
    locations, stops, status = request_results(params)
    dataframe = formatted_result(locations, stops, status)
    # output csv
    dataframe.to_csv(filename)
