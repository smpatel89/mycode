#!/usr/bin/env python

import requests
import pprint
import pyexcel

#35.8, 78.8
def main():
    api_url = 'http://api.open-notify.org/iss-pass.json?lat={}&lon={}'
    lat = 35.8
    lon = 78.8

    r = requests.get(api_url.format(lat, lon))
    req = r.json().get('request')
    res = r.json().get('response')

    excel_data = []

    for time in res:
        duration_int = int(time['duration'])
        duration_m = int((duration_int  - (duration_int % 60))/60)
        duration_s = duration_int % 60
        print(f'Time: {time["risetime"]}, Duration: {duration_m}m{duration_s}s')
        excel_data.append(
                {
                    'time': time['risetime'],
                    'duration_m': duration_m,
                    'duration_s': duration_s
                    })

    pyexcel.save_as(records=excel_data, dest_file_name="time_list.xls")

main()
