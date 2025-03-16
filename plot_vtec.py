import matplotlib.pyplot as plt
import matplotlib
import matplotlib.font_manager as fm
import numpy as np
import os
import arabic_reshaper
from bidi.algorithm import get_display

# تنظیم مسیر فونت فارسی
font_farsi_path = os.path.join(os.getcwd(), "B-NAZANIN.ttf")

if os.path.exists(font_farsi_path):
    font_farsi = fm.FontProperties(fname=font_farsi_path, size=12)
else:
    print(f"❌ فایل فونت فارسی پیدا نشد! مسیر: {font_farsi_path}")
    font_farsi = fm.FontProperties(family="Arial", size=12)  # جایگزینی با Arial

# تابع برای اصلاح و راست‌چین کردن متن فارسی
def fix_text(text):
    reshaped_text = arabic_reshaper.reshape(text)  # اصلاح اتصال حروف فارسی
    return get_display(reshaped_text)  # نمایش از راست به چپ

def plot_vtec(year, month, day, vtec_station, doy, sys):
    """ نمایش نمودار VTEC برای GNSS با متن فارسی-انگلیسی صحیح """

    time_tec = np.linspace(0, 24, len(vtec_station['gps']))

    plt.figure(figsize=(10, 5))
    plt.plot(time_tec, vtec_station['gps'], '-', linewidth=1, color='b', label="GPS - " + fix_text("GPS"))
    plt.plot(time_tec, vtec_station['glo'], '-', linewidth=1, color='r', label="GLONASS - " + fix_text("GLONAS"))
    plt.plot(time_tec, vtec_station['bds'], '-', linewidth=1, color='g', label="BDS - " + fix_text("BIDO"))

    plt.xlabel(fix_text("TIME (Hourse)"), fontproperties=font_farsi)
    plt.ylabel(fix_text("VTEC (TECU)"), fontproperties=font_farsi)
    plt.title(fix_text(f"Chart VTEC - Date: {year}/{month}/{day} ({sys})"), fontproperties=font_farsi)
    plt.legend(prop=font_farsi)
    plt.grid()
    plt.show()

