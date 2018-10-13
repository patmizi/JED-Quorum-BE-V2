from datetime import date, datetime


# Returns a Date object from the form DD/MM/YYYY
def get_date_from_string(date_str):
    day_index = date_str.find('/')
    month_index = date_str.find('/', day_index + 1)

    day = int(date_str[:day_index])
    month = int(date_str[day_index+1:month_index])
    year = int(date_str[month_index+1:])
    print(date(year, month, day))
    return date(year, month, day)

# Given date object, this function will return a string of DD/MM/YYYY
def serialize_date(date_obj):
    date_obj = str(date_obj)
    return str(date_obj[-2:] + '/' + date_obj[-5:-3] + '/' + date_obj[:4])

# Date Time string to obj function
def get_datetime_from_string(datetime_str):
    datetime_order = datetime.strptime(datetime_str, '%d/%m/%Y %H:%M:%S')
    print(datetime_order)
    return datetime_order

#Given datetime object, this should return a string in and acceptable format
def iso_date(date_obj):
    if isinstance(date_obj, datetime):
        return date_obj.__str__()
