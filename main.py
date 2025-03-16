import os
import tkinter as tk
from tkinter import filedialog
from load_rinex_obs import load_rinex_obs
from load_rinex_navigation import load_rinex_navigation
from get_sat_pos_gps import get_sat_pos_gps
from get_sat_pos_glo import get_sat_pos_glo
from get_sat_pos_bds import get_sat_pos_bds
from main_cal_tec import main_cal_tec
from run_vtec_estimate import run_vtec_estimate_stations
import matplotlib
matplotlib.use("TkAgg")  # تغییر بک‌اند برای نمایش نمودار


def main():
    """ اجرای پروژه و دریافت فایل ورودی از کاربر به صورت گرافیکی """

    # نمایش پنجره انتخاب فایل
    root = tk.Tk()
    root.withdraw()  # مخفی کردن پنجره اصلی
    file_path = filedialog.askopenfilename(title="انتخاب فایل RINEX", filetypes=[("RINEX Files", "*.txt *.rnx *.obs")])

    if not file_path:
        print("❌ هیچ فایلی انتخاب نشد!")
        return

    print(f"✅ فایل انتخاب‌شده: {file_path}")

    # بارگذاری داده‌های RINEX
    obs_data = load_rinex_obs(file_path)
    nav_data = load_rinex_navigation(file_path.replace(".txt", ".nav"))  # تغییر نام فایل برای فایل ناوبری

    if obs_data is None or nav_data is None:
        print("❌ خطا در پردازش داده‌های RINEX!")
        return

    # محاسبه موقعیت ماهواره‌ها
    gps_positions = get_sat_pos_gps(nav_data)
    glo_positions = get_sat_pos_glo(nav_data)
    bds_positions = get_sat_pos_bds(nav_data)

    # اجرای محاسبات TEC
    vtec_results = main_cal_tec(gps_positions, obs_data, {}, {}, {}, {}, {})

    # اجرای پردازش کلی VTEC
    run_vtec_estimate_stations()

    print("✅ پردازش با موفقیت انجام شد!")


if __name__ == "__main__":
    main()
