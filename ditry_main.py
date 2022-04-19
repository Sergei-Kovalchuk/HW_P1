import datetime as dt
from application import *

def now():
    return str(dt.datetime.today())

if __name__ == '__main__':
    print(calculate_salary(), now())
    print(get_employees(), now())