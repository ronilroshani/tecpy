import os
import numpy as np
import tkinter as tk
from tkinter import simpledialog
from georgd2yearday import georgd2yearday
from tec import TEC
from modelling_vtec_bspline import modelling_vtec_bspline


def run_vtec_estimate_stations():
    """ اجرای محاسبه VTEC برای ایستگاه‌های مختلف با دریافت ورودی از کاربر. """

    root = tk.Tk()
    root.withdraw()

    year = simpledialog.askinteger("ورود اطلاعات", "سال:", initialvalue=2022)
    month = simpledialog.askinteger("ورود اطلاعات", "ماه:", initialvalue=6)
    day_start = simpledialog.askinteger("ورود اطلاعات", "روز شروع:", initialvalue=1)
    day_end = simpledialog.askinteger("ورود اطلاعات", "روز پایان:", initialvalue=1)

    days = np.arange(day_start, day_end + 1)
    doy = [georgd2yearday(year, month, day) for day in days]

    for d in doy:
        doy_str = f"{d:03d}"
        folder = os.path.join("RINEX", str(year), doy_str)

        if not os.path.exists(folder):
            print(f"پوشه {folder} یافت نشد!")
            continue

        files = [f for f in os.listdir(folder) if f.endswith(".rnx")]

        for j, rinex_file in enumerate(files):
            rinex_path = os.path.join(folder, rinex_file)
            TEC(rinex_path, year, doy_str)
            print(f"{j + 1}: ایستگاه {rinex_file} پردازش شد.")

        modelling_vtec_bspline("Results")

    print("🔹 محاسبات VTEC برای تمام ایستگاه‌ها به پایان رسید.")


if __name__ == "__main__":
    run_vtec_estimate_stations()
