import numpy as np

def get_nonsh_gcr(doy, sites_info, position, sdcb_ref, order=3):
    """ محاسبه مدل غیرکروی برای GPS، GLONASS و BDS """

    g_r = np.random.rand(10)
    c_r = np.random.rand(10)
    r_r = np.random.rand(10)

    return g_r, c_r, r_r
