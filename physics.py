import numpy as np
from constants import EARTH_MU

def orbital_derivatives(t, state):
    x, y, z, vx, vy, vz = state
    r_vec = np.array([x, y, z])
    r_mag = np.linalg.norm(r_vec)
    a_vec = -EARTH_MU * r_vec/(r_mag**3)
    return (vx, vy, vz, a_vec[0], a_vec[1], a_vec[2])

