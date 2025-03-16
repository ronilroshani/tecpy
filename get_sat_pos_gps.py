import numpy as np


def get_sat_pos_gps(nav_data):
    """ محاسبه موقعیت ماهواره‌های GPS """

    if nav_data is None:
        return None

    # شبیه‌سازی موقعیت‌های ماهواره‌ای
    positions = np.random.rand(10, 3) * 20200000  # مقدار تصادفی برای شبیه‌سازی مدار
    return positions


# مثال استفاده
positions = get_sat_pos_gps(None)
print("GPS Satellite Positions:", positions)
