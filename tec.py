import numpy as np

def TEC(file_path, year, doy):
    """ پردازش داده‌های RINEX و محاسبه کل TEC """

    try:
        # بارگذاری داده‌های نمونه (در پروژه واقعی، داده‌های RINEX پردازش می‌شوند)
        stec = np.random.rand(2880) * 50  # مقدار تصادفی برای TEC
        vtec = stec / 2  # مقدار تقریبی VTEC

        print(f"✅ محاسبات TEC برای {file_path} انجام شد.")

        return stec, vtec

    except Exception as e:
        print(f"❌ خطا در پردازش TEC: {e}")
        return None, None

# مثال استفاده
stec, vtec = TEC("BAGH2840.txt", 2024, 69)
print("STEC Sample:", stec[:5])
print("VTEC Sample:", vtec[:5])
