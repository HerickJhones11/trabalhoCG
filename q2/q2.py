from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
from q2.cilindro import cilindro
from q2.cone import cone
from q2.cubo import cubo
from q2.esfera import esfera
from q2.tronco import tronco



def mundo(ax):
    all_points = []
    all_points.extend([
        [0, 10, 10], [0, -10, 10], [0, -10, -10], [0, 10, -10],
        [10, 0, 10], [-10, 0, 10], [-10, 0, -10], [10, 0, -10],
        [10, 10, 0], [-10, 10, 0], [-10, -10, 0], [10, -10, 0]
    ])
    
    points = np.array(all_points)

    ax.scatter3D(points[:, 0], points[:, 1], points[:, 2])
    
    ax.add_collection3d(Poly3DCollection([
        [
            [0, 10, 10], [0, -10, 10], [0, -10, -10], [0, 10, -10]
        ],
        [
            [10, 0, 10], [-10, 0, 10], [-10, 0, -10], [10, 0, -10]
        ],
        [
            [10, 10, 0], [-10, 10, 0], [-10, -10, 0], [10, -10, 0]
        ]
    ],
    facecolors="purple", linewidths=1, edgecolors="w", alpha=.25))

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")



def q2():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    mundo(ax)
    esfera(ax)
    cubo(ax)
    tronco(ax)
    pontos_cilindro = cilindro(ax)
    pontos_cone = cone(ax)
    plt.show()
    return pontos_cilindro, pontos_cone 