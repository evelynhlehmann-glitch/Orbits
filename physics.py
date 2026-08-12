import numpy as np
from constants import EARTH_MU

def orbital_derivatives(t, state):
    x, y, z, vx, vy, vz = state
    r_vec = np.array([x, y, z])
    r_mag = np.linalg.norm(r_vec)
    a_vec = -EARTH_MU * r_vec/(r_mag**3)
    return (vx, vy, vz, a_vec[0], a_vec[1], a_vec[2])

# import numpy as np
# from constants import *

# def orbital_derivatives(t, state, mass, area, Cd):
#     x, y, z, vx, vy, vz = state
#     r_vec = np.array([x, y, z])
#     v_vec = np.array([vx, vy, vz])

#     r_mag = np.linalg.norm(r_vec)
#     v_mag = np.linalg.norm(v_vec)

#     a_gravity = -EARTH_MU * r_vec/(r_mag**3)

#     altitude = r_mag - EARTH_RADIUS

#     a_drag = -0.5 * rho * CD * A / mass * v_mag * v_vec

#     a_vec = a_gravity + a_drag

#     return (vx, vy, vz, a_vec[0], a_vec[1], a_vec[2])

