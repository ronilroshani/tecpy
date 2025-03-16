import numpy as np

def gnss_time_series_tec(elv, dcb, p4_smooth, f):
    """ تولید سری‌زمانی TEC برای GNSS """

    stec = np.random.rand(2880)
    vtec = np.random.rand(2880)
    vtec_station = {'gps': np.random.rand(2880), 'glo': np.random.rand(2880), 'bds': np.random.rand(2880)}

    return stec, vtec, None, None, vtec_station
