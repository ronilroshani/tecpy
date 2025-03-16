import numpy as np


def get_p4grc(position, observation, sites_info, cutoff=10):
    """ پردازش مشاهدات P4 برای GPS، GLONASS و BDS """

    gps_p4 = observation.get('GPSP1', np.zeros((2880, 10))) - observation.get('GPSP2', np.zeros((2880, 10)))
    glo_p4 = observation.get('GLOP1', np.zeros((2880, 10))) - observation.get('GLOP2', np.zeros((2880, 10)))
    bds_p4 = observation.get('BDSP1', np.zeros((2880, 10))) - observation.get('BDSP2', np.zeros((2880, 10)))

    return gps_p4, glo_p4, bds_p4
