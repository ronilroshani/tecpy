from datetime import datetime


def georgd2yearday(year, month, day):
    """ تبدیل تاریخ میلادی به روز سال (DOY) """

    date = datetime(year, month, day)
    doy = date.timetuple().tm_yday  # محاسبه شماره روز در سال

    return doy


# مثال استفاده
doy = georgd2yearday(2024, 3, 10)
print(f"روز سال (DOY): {doy}")
