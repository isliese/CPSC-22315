# Name : Chanran Kim
# Date : 15/10/2024
# 'weather' module which contains various functions to perform tasks

import json
from calendar import month_name

# read_data function
def read_data(*, filename):
    try: 
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# write_data function
def write_data(*, data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)

# max_temperature function
def max_temperature(*, data, date):
    temps = [readings['t'] for key, readings in data.items() if key.startswith(date)]
    return max(temps) if temps else None

# min_temperature function
def min_temperature(*, data, date):
    temps = [readings['t'] for key, readings in data.items() if key.startswith(date)]
    return min(temps) if temps else None

# max_humidity function
def max_humidity(*, data, date):
    humidities = [readings['h'] for key, readings in data.items() if key.startswith(date)]
    return max(humidities) if humidities else None

# min_humidity function
def min_humidity(*, data, date):
    humidities = [readings['h'] for key, readings in data.items() if key.startswith(date)]
    return min(humidities) if humidities else None

# tot_rain function
def tot_rain(*, data, date):
    rainfall = [readings['r'] for key, readings in data.items() if key.startswith(date)]
    return sum(rainfall) if rainfall else 0.0

# report_daily function
def report_daily(*, data, date):
    report = "========================= DAILY REPORT ========================\n"
    report += "Date                      Time  Temperature  Humidity  Rainfall\n"
    report += "====================  ========  ===========  ========  ========\n"
    for key, readings in data.items():
        if key.startswith(date):
            if key[4:6] == '01':
                month_txt = 'January'
            elif key[4:6] == '02':
                month_txt = 'February'
            elif key[4:6] == "03":
                month_txt = 'March'
            date_part = key[:8]
            time_part = key[8:]
            report += f"{month_txt}  {time_part[:4]}  {readings['t']:>10}  {readings['h']:>8}  {readings['r']:>8.2f}\n"
    return report

# report_historical function
def report_historical(*, data):
    report = "============================== HISTORICAL REPORT ===========================\n"
    report += "			  Minimum      Maximum   Minumum   Maximum     Total\n"
    report += "Date     Temperature  Temperature  Humidity  Humidity  Rainfall\n"
    report += "====================  ===========  ===========  ========  ========  ========\n"

    date_groups = {}
    for key, readings in data.items():
        date = key[:8]
        if date not in date_groups:
            date_groups[date] = {'t': [], 'h': [], 'r': []}
        date_groups[date]['t'].append(readings['t'])
        date_groups[date]['h'].append(readings['h'])
        date_groups[date]['r'].append(readings['r'])

    for date, readings in date_groups.items():
        max_temp = max(readings['t'])
        min_temp = min(readings['t'])
        max_hum = max(readings['h'])
        min_hum = min(readings['h'])
        total_rain = sum(readings['r'])
        report += f"{date}  {min_temp:>10}  {max_temp:>10}  {min_hum:>8}  {max_hum:>8}  {total_rain:>8.2f}\n"

    return report
