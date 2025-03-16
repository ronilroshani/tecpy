from datetime import datetime, timedelta
import numpy as np


def cal2gpstime(year, month, day, hour, minute, second):
    """ تبدیل تاریخ میلادی به هفته و ثانیه‌ی GPS """

    SECONDS_PER_WEEK = 604800

    if 80 <= year <= 99:
        year += 1900
    elif 0 <= year <= 79:
        year += 2000

    if month <= 2:
        y = year - 1
        m = month + 12
    else:
        y = year
        m = month

    JD = int(365.25 * y) + int(30.6001 * (m + 1)) + day + ((hour + minute / 60 + second / 3600) / 24) + 1720981.5

    gps_week = int((JD - 2444244.5) / 7)
    gps_seconds = round(((((JD - 2444244.5) / 7) - gps_week) * SECONDS_PER_WEEK) / 0.5) * 0.5

    return gps_week, gps_seconds


# مثال استفاده
gps_week, gps_seconds = cal2gpstime(2024, 3, 10, 12, 30, 15)
print(f"GPS Week: {gps_week}, GPS Seconds: {gps_seconds}")
