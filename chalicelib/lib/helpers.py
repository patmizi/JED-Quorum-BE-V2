from datetime import date


# Returns a Date object from the form DD/MM/YYYY
def get_date_from_string(date_str):
    day_index = date_str.find('/')
    month_index = date_str.find('/', day_index + 1)

    day = int(date_str[:day_index])
    month = int(date_str[day_index+1:month_index])
    year = int(date_str[month_index+1:])

    return date(year, month, day)

# Given date object, this function will return a string of DD/MM/YYYY
def serialize_date(date_obj):
    date_obj = str(date_obj)
    return str(date_obj[-2:] + '/' + date_obj[-5:-3] + '/' + date_obj[:4])
