import numpy as np
import os
def load_rinex_navigation(file_path):
    """ پردازش فایل ناوبری RINEX و استخراج پارامترهای مداری ماهواره‌ها """
    if not os.path.exists(file_path):
        print(f"❌ فایل {file_path} پیدا نشد!")
        return None
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # حذف هدر RINEX
        while lines and "END OF HEADER" not in lines[0]:
            lines.pop(0)
        lines.pop(0)

        # استخراج داده‌های ناوبری
        nav_data = []
        for line in lines:
            values = line.strip().split()
            nav_data.append([float(v.replace("D", "E")) for v in values if "D" in v or v.replace('.', '', 1).isdigit()])

        return np.array(nav_data)

    except Exception as e:
        print(f"❌ خطا در پردازش فایل ناوبری RINEX: {e}")
        return None

# مثال استفاده
nav = load_rinex_navigation("BAGH2840.txt")
print("داده‌های ناوبری RINEX:", nav)
