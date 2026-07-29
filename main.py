import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from physics import orbital_derivatives
from constants import EARTH_MU, EARTH_RADIUS

def main():
    t_span = (0, 5400)
    ISS_altitude = 400 # km
    ISS_y = 0
    ISS_z = 0
    ISS_x = ISS_altitude + EARTH_RADIUS
    v_mag = np.sqrt(EARTH_MU/ISS_x)
    ISS_vy = v_mag
    ISS_vx = 0
    ISS_vz = 0
    y0 = (ISS_x, ISS_y, ISS_z, ISS_vx, ISS_vy, ISS_vz)
    sol = solve_ivp(orbital_derivatives, t_span, y0, max_step = 20)
    print(sol.t)


if __name__ == "__main__":
    main() 