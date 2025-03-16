import numpy as np
import os

def load_rinex_obs(file_path):
    """ پردازش فایل مشاهده RINEX و استخراج داده‌های GPS/GLONASS """
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

        # استخراج داده‌ها
        obs_data = []
        for line in lines:
            values = line.strip().split()
            obs_data.append([float(v.replace("D", "E")) for v in values if "D" in v or v.replace('.', '', 1).isdigit()])

        return np.array(obs_data)

    except Exception as e:
        print(f"❌ خطا در خواندن فایل RINEX: {e}")
        return None


# مثال استفاده
obs = load_rinex_obs("BAGH2840.txt")
print("مشاهدات RINEX:", obs)
