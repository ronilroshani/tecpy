import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import BSpline
import matplotlib
matplotlib.use("TkAgg")  # تغییر بک‌اند برای نمایش نمودار


def modelling_vtec_bspline(result_path):
    """ مدل‌سازی VTEC با استفاده از B-Spline """

    # ایجاد داده‌های تصادفی برای نمایش عملکرد
    time = np.linspace(0, 24, 50)
    vtec_data = np.sin(time / 4) + np.random.normal(0, 0.1, size=len(time))

    # تعریف نودهای B-Spline
    knots = np.linspace(0, 24, 10)
    degree = 3  # درجه B-Spline
    coeffs = np.random.rand(len(knots) + degree - 1)  # ضرایب تصادفی

    spline = BSpline(knots, coeffs, degree)

    # رسم نمودار
    plt.figure(figsize=(10, 5))
    plt.plot(time, vtec_data, 'o', label="داده‌های اولیه")
    plt.plot(time, spline(time), '-', label="B-Spline تخمین زده‌شده")

    plt.xlabel("زمان (ساعت)")
    plt.ylabel("VTEC (TECU)")
    plt.title("مدل‌سازی VTEC با B-Spline")
    plt.legend()
    plt.grid()
    plt.show()


# اجرای مدل‌سازی (مثال)
modelling_vtec_bspline("Results")
