from csv import reader
import datetime as dt

def open_file(filename):
    opened_file = open(file=filename, mode="r")
    read_file = reader(opened_file)
    apps_data = list(read_file)

    return apps_data

potus = open_file('data/whitehouse_waves-2015_12.csv')
potus_header = potus[0]
potus = potus[1:]

print(potus_header)
print(potus[:5])
print("Amount of entries in potus dataset:", len(potus)-1)

# Format taken from https://strftime.org/
date_format = "%m/%d/%Y %H:%M"

for row in potus:
    appt_start_date = row[11]
    appt_end_date = row[12]
    try:
        row[11] = dt.datetime.strptime(appt_start_date, date_format)
    except ValueError:
        row[11] = appt_start_date  # If the format is incorrect, leave the value as string
    try:
        row[12] = dt.datetime.strptime(appt_end_date, date_format)
    except ValueError:
        row[12] = appt_end_date  # If the format is incorrect, leave the value as string


print(potus[:5])
print("Amount of entries in potus dataset after appointment start and end dates conversion:", len(potus)-1)

visitors_per_month = {}
incorrect_date_indicator = 'IncorrectDate'
appt_times = []
appt_lengths = {}

for row in potus:
    appt_start_date = row[11]
    appt_end_date = row[12]
    if isinstance(appt_start_date, dt.datetime) and isinstance(appt_end_date, dt.datetime):
        appt_start_date_formatted_month_year = appt_start_date.strftime("%B, %Y")
        if appt_start_date_formatted_month_year not in visitors_per_month:
            visitors_per_month[appt_start_date_formatted_month_year] = 1
        else:
            visitors_per_month[appt_start_date_formatted_month_year] += 1
        appt_start_time = appt_start_date.time()
        appt_times.append(appt_start_time)
        length = appt_end_date - appt_start_date
        if length not in appt_lengths:
            appt_lengths[length] = 1
        else:
            appt_lengths[length] += 1
    else:
        if incorrect_date_indicator not in visitors_per_month:
            visitors_per_month[incorrect_date_indicator] = 1
        else:
            visitors_per_month[incorrect_date_indicator] += 1

print(visitors_per_month)

min_time = min(appt_times)
max_time = max(appt_times)

print('The earlist time of appointment:', min_time)
print('The latest time of appointment:', max_time)

min_length = min(appt_lengths)
max_length = max(appt_lengths)

print('The minimum length of appointment:', min_length)
print('The maximum length of appointment:', max_length)
