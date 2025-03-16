import numpy as np


def get_state_derivation(const, state_vector, acc):
    """ محاسبه مشتق عددی بردار وضعیت """

    r2 = np.sum(state_vector[:3] ** 2)
    r = np.sqrt(r2)
    mur = const['GM'] / r2
    rho = const['a'] / r
    xr = state_vector[0] / r
    yr = state_vector[1] / r
    zr = state_vector[2] / r

    state_der = np.array([
        state_vector[3],
        state_vector[4],
        state_vector[5],
        -mur * xr + (3 / 2) * const['C20'] * mur * xr * (rho ** 2) * (1 - 5 * zr ** 2) + acc[0],
        -mur * yr + (3 / 2) * const['C20'] * mur * yr * (rho ** 2) * (1 - 5 * zr ** 2) + acc[1],
        -mur * zr + (3 / 2) * const['C20'] * mur * zr * (rho ** 2) * (3 - 5 * zr ** 2) + acc[2]
    ])

    return state_der


# مثال استفاده
constants = {'GM': 3.986004418e14, 'a': 6378137.0, 'C20': -1.08263e-3}
state_vector = np.array([7000e3, 0, 0, 0, 7.5e3, 0])
acceleration = np.array([0, 0, 0])

state_derivative = get_state_derivation(constants, state_vector, acceleration)
print("State Derivative:", state_derivative)
