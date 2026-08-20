import matplotlib.pyplot as plt
import numpy as np
from constants import EARTH_RADIUS

def plot_trajectories(state):
    x, y, z, vx, vy, vz = state
    R = EARTH_RADIUS
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    earth_texture = plt.imread("data/bluemarble-2048.png")

    u, v = np.mgrid[0:2*np.pi:300j, 0:np.pi:150j]

    sphere_x = R * np.cos(u) * np.sin(v)
    sphere_y = R * np.sin(u) * np.sin(v)
    sphere_z = R * np.cos(v)

    texture_u = u / (2 * np.pi)
    texture_v = v / np.pi

    img_h, img_w = earth_texture.shape[:2]

    pixel_x = (texture_u * (img_w - 1)).astype(int)
    pixel_y = (texture_v * (img_h - 1)).astype(int)

    facecolors = earth_texture[pixel_y, pixel_x]

    ax.plot_surface(
        sphere_x,
        sphere_y,
        sphere_z,
        facecolors=facecolors,
        edgecolor='none',
        alpha=.5
    )
    ax.plot(x, y, z)
    ax.set_box_aspect([1, 1, 1])

    ax.set_title('Orbit around Earth')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    dimensions = [x, y, z]
    furthest = np.max(dimensions)
    ax.set_xlim([-furthest, furthest])
    ax.set_ylim([-furthest, furthest])
    ax.set_zlim([-furthest, furthest])
    ax.view_init(elev=25, azim=30)

    plt.tight_layout()
    plt.show()

