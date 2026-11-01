import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from physics import orbital_derivatives
from constants import EARTH_MU, EARTH_RADIUS, MOON_MU, MOON_RADIUS
from plotting import plot_trajectories
from conversions import keplarian_to_cartesian
from datetime import datetime
from pyatmos import read_sw_nrlmsise00


def main():
    epoch = datetime(2026, 8, 20, 0, 0, 0)
    swdata = read_sw_nrlmsise00("data/SW-Last5Years.csv")
    mu = EARTH_MU
    ISS_time = 864000
    ISS_span = (0, ISS_time)
    ISS_altitude = 420 # km
    ISS_y = 0
    ISS_z = 0
    ISS_x = ISS_altitude + EARTH_RADIUS
    v_mag = np.sqrt(EARTH_MU/ISS_x)
    ISS_vy = v_mag
    ISS_vx = 2
    ISS_vz = 1
    # y0 = (ISS_x, ISS_y, ISS_z, ISS_vx, ISS_vy, ISS_vz)
    # sol = solve_ivp(orbital_derivatives, ISS_span, y0, max_step = 20, args = (swdata, epoch, mu))
    # plot_trajectories(sol.y)


    # ISSkeplarian = [6771, 0.001, np.deg2rad(51.6), 0, 0, 0]
    # ISS_orbit = keplarian_to_cartesian(ISS_span[0], ISSkeplarian)
    # sol2 = solve_ivp(orbital_derivatives, ISS_span, ISS_orbit, max_step = 100, args = (swdata, epoch, mu))
    heo_keplerian = [15000, 0.5, np.deg2rad(63.4), 0, 0, 0]
    heo_orbit = keplarian_to_cartesian(ISS_span[0], heo_keplerian)
    sol_heo = solve_ivp(orbital_derivatives, ISS_span, heo_orbit, max_step=200, args=(swdata, epoch, mu))
    plot_trajectories(sol_heo.y)
    # v = np.linalg.norm(sol2.y[3:6], axis=0)
    # r = np.linalg.norm(sol2.y[:3], axis=0)

    # energy = 0.5 * v**2 - EARTH_MU / r

    # print("Initial energy:", energy[0])
    # print("Final energy:", energy[-1])
    # plot_trajectories(sol2.y)

    # moon_time = 2358720
    # moon_span = (0, moon_time)
    # moon_keplarian = [384400, 0.055, np.deg2rad(5.145), 0, 0, 0]
    # moon_orbit = keplarian_to_cartesian(moon_span[0], moon_keplarian)
    # sol_moon = solve_ivp(orbital_derivatives, moon_span, moon_orbit, max_step = 20)
    # plot_trajectories(sol_moon.y)





if __name__ == "__main__":
    main() 