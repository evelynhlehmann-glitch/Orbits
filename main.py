import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from physics import orbital_derivatives
from constants import EARTH_MU, EARTH_RADIUS
from plotting import plot_trajectories
from conversions import keplarian_to_cartesian

def main():
    t_span = (0, 5400)
    ISS_altitude = 400 # km
    ISS_y = 50
    ISS_z = 0
    ISS_x = ISS_altitude + EARTH_RADIUS
    v_mag = np.sqrt(EARTH_MU/ISS_x)
    ISS_vy = v_mag
    ISS_vx = 2
    ISS_vz = 1
    y0 = (ISS_x, ISS_y, ISS_z, ISS_vx, ISS_vy, ISS_vz)
    sol = solve_ivp(orbital_derivatives, t_span, y0, max_step = 20)
    # plot_trajectories(sol.y)

    ISSkeplarian = [6771, 0.0001, np.deg2rad(51.6), 0, 0, 0]
    ISS_orbit = keplarian_to_cartesian(3600, ISSkeplarian)
    sol2 = solve_ivp(orbital_derivatives, t_span, ISS_orbit, max_step = 20)
    plot_trajectories(sol2.y)

    # moon_time = 2358720
    # moon_span = (0, moon_time)
    # moon_keplarian = [384400, 0.055, np.deg2rad(5.145), 0, 0, 0]
    # moon_orbit = keplarian_to_cartesian(moon_time, moon_keplarian)
    # sol_moon = solve_ivp(orbital_derivatives, moon_span, moon_orbit, max_step = 20)
    # plot_trajectories(sol_moon.y)



if __name__ == "__main__":
    main() 