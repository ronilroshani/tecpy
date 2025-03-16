import numpy as np

def get_dcb_grc(doy, sites_info, position, sdcb_ref, order=3):
    """ محاسبه تصحیحات DCB برای سیستم‌های GNSS """

    dcb = {
        'gps_dcb': np.random.rand(10),
        'bds_dcb': np.random.rand(10),
        'glo_dcb': np.random.rand(10),
    }
    az = {'gps': np.random.rand(10), 'glo': np.random.rand(10), 'bds': np.random.rand(10)}
    elv = {'gps': np.random.rand(10), 'glo': np.random.rand(10), 'bds': np.random.rand(10)}
    lat_ipp = {'lat_ipp_gps': np.random.rand(10), 'lat_ipp_glo': np.random.rand(10), 'lat_ipp_bds': np.random.rand(10)}
    lon_ipp = {'lon_ipp_gps': np.random.rand(10), 'lon_ipp_glo': np.random.rand(10), 'lon_ipp_bds': np.random.rand(10)}
    lat_lon_sta = {'lat_sta': np.random.rand(10), 'lon_sta': np.random.rand(10)}
    ippz = {'ippz_gps': np.random.rand(10), 'ippz_glo': np.random.rand(10), 'ippz_bds': np.random.rand(10)}

    return dcb, az, elv, lat_ipp, lon_ipp, lat_lon_sta, ippz
