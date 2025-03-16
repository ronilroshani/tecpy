import numpy as np

def get_sat_pos_bds(nav_data):
    """ محاسبه موقعیت ماهواره‌های BDS با استفاده از داده‌های ناوبری """

    if nav_data is None:
        return None

    # شبیه‌سازی موقعیت‌های ماهواره‌ای BDS
    positions = np.random.rand(10, 3) * 21500000  # مقدار تصادفی برای شبیه‌سازی مدار BDS
    return positions

# مثال استفاده
positions = get_sat_pos_bds(None)
print("موقعیت ماهواره‌های BDS:", positions)
