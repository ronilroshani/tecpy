import numpy as np

def get_sat_pos_glo(nav_data):
    """ محاسبه موقعیت ماهواره‌های GLONASS با استفاده از داده‌های ناوبری """

    if nav_data is None:
        return None

    # شبیه‌سازی موقعیت‌های ماهواره‌ای GLONASS
    positions = np.random.rand(10, 3) * 25500000  # مقدار تصادفی برای شبیه‌سازی مدار
    return positions

# مثال استفاده
positions = get_sat_pos_glo(None)
print("موقعیت ماهواره‌های GLONASS:", positions)
