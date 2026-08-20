import numpy as np
from constants import EARTH_MU, EARTH_RADIUS, ISS_AREA, ISS_CD, ISS_MASS
from pyatmos import read_sw_nrlmsise00
from pyatmos import nrlmsise00
from datetime import timedelta


def orbital_derivatives(t, state, epoch = None, mu = EARTH_MU, mass = ISS_MASS, A = ISS_AREA, CD = ISS_CD):
    x, y, z, vx, vy, vz = state
    r_vec = np.array([x, y, z])
    v_vec = np.array([vx, vy, vz])
    r_mag = np.linalg.norm(r_vec)
    a_gravity = -mu * r_vec / r_mag**3

    swdata = read_sw_nrlmsise00("data/SW-Last5Years.csv")
    utc = epoch + timedelta(seconds = t)
    t_str = utc.strftime("%Y-%m-%d %H:%M:%S")
    alt = r_mag - EARTH_RADIUS
    lat,lon = 25,102
    nrl00 = nrlmsise00(t_str,(lat,lon,alt),swdata)
    rho = nrl00.rho

    v_vec_m = v_vec * 1000
    v_mag_m = np.linalg.norm(v_vec_m)

    a_drag_m = (-0.5 * rho * CD * A / mass * v_mag_m * v_vec_m)
    a_drag = a_drag_m / 1000
    a_total = a_gravity + a_drag

    

    return (vx, vy, vz, a_total[0], a_total[1], a_total[2])