import numpy as np
from constants import EARTH_MU

def keplarian_to_cartesian(t, keplarian_state, mu = EARTH_MU):
    a, e, i, ω, Ω, T = keplarian_state
    # a (semimajor axis) is in km
    n = np.sqrt(mu/(a**3))
    M = n * (t - T)
    M = np.mod(M, 2 * np.pi)
    E = M

    for _ in range(100):
        dE = (E - e * np.sin(E) - M) / (1 - e * np.cos(E))
        E -= dE

        if abs(dE) < 1e-10:
            break
    x_p = a * (np.cos(E) - e)
    y_p = a * np.sqrt(1 - e**2) * np.sin(E)

    x_dot_p = -a * n * np.sin(E) / (1 - e * np.cos(E))
    y_dot_p = a * n * np.sqrt(1 - e**2) * np.cos(E) / (1 - e * np.cos(E))

    cos_O = np.cos(Ω)
    sin_O = np.sin(Ω)
    cos_i = np.cos(i)
    sin_i = np.sin(i)
    cos_w = np.cos(ω)
    sin_w = np.sin(ω)

    R = np.array([
        [
            cos_O*cos_w - sin_O*sin_w*cos_i,
            -cos_O*sin_w - sin_O*cos_w*cos_i,
            sin_O*sin_i
        ],
        [
            sin_O*cos_w + cos_O*sin_w*cos_i,
            -sin_O*sin_w + cos_O*cos_w*cos_i,
            -cos_O*sin_i
        ],
        [
            sin_w*sin_i,
            cos_w*sin_i,
            cos_i
        ]
    ])
    r_pqw = np.array([x_p, y_p, 0])
    v_pqw = np.array([x_dot_p, y_dot_p, 0])

    r_eci = R @ r_pqw
    v_eci = R @ v_pqw
    return np.concatenate((r_eci, v_eci))