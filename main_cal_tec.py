import numpy as np
import os
from get_p4grc import get_p4grc
from get_dcb_grc import get_dcb_grc
from get_nonsh_gcr import get_nonsh_gcr
from gnss_time_series_tec import gnss_time_series_tec
from plot_vtec import plot_vtec
from plot_timeseries_tec import plot_timeseries_tec


def main_cal_tec(position, obs_gnss, sites_info, sdcb_ref, f, date_rm, doy):
    """ محاسبه STEC و VTEC برای داده‌های GNSS """

    year = str(date_rm[0])
    month = f"{date_rm[1]:02d}"
    day = f"{date_rm[2]:02d}"

    sys = 'GPS_GLO_BDS'

    # دریافت مشاهدات P4 برای GPS، GLONASS و BDS
    gps_p4, glo_p4, bds_p4 = get_p4grc(position, obs_gnss, sites_info, cutoff=10)

    # محاسبه تصحیحات DCB و موقعیت‌های IPP
    dcb, az, elv, lat_ipp, lon_ipp, lat_lon_sta, ippz = get_dcb_grc(str(sdcb_ref['doy']), sites_info, position,
                                                                    sdcb_ref, order=3)

    # محاسبه مدل غیرکروی برای GNSS
    g_r, c_r, r_r = get_nonsh_gcr(str(sdcb_ref['doy']), sites_info, position, sdcb_ref, order=3)

    # تخصیص داده‌های DCB به سیستم‌های مختلف
    dcb['gps_dcb_r'] = g_r
    dcb['bds_dcb_r'] = c_r
    dcb['glo_dcb_r'] = r_r

    p4_smooth = {'gps': gps_p4, 'glo': glo_p4, 'bds': bds_p4}

    # محاسبه سری‌زمانی TEC
    stec, vtec, _, _, vtec_station = gnss_time_series_tec(elv, dcb, p4_smooth, f)

    # میانگین‌گیری از VTEC محاسبه‌شده برای تمام سیستم‌های GNSS
    vtec_gnss = np.nanmean([vtec_station['gps'], vtec_station['glo'], vtec_station['bds']], axis=0)

    # ذخیره نتایج
    results_path = os.path.join("Results", "TimeSeries_text", f"{year}_{str(sites_info['doy'])[2:5]}")
    os.makedirs(results_path, exist_ok=True)

    time = np.arange(len(vtec_gnss)) * 30 / 3600  # تبدیل به ساعت

    result_file = os.path.join(results_path, f"{sites_info['name']}{year}{str(sites_info['doy'])[2:5]}_{sys}.txt")
    np.savetxt(result_file, np.column_stack((time, vtec_gnss)), delimiter='\t', header="Time\tTEC")

    # رسم نمودارها
    plot_vtec(year, month, day, vtec_station, sites_info['doy'], sys)
    plot_timeseries_tec(year, month, day, vtec_gnss, sites_info['doy'], sys)

    return vtec_gnss
