from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
from q2.cilindro import cilindro
from q2.cone import cone
from q2.cubo import cubo

from q2.esfera import esfera
from q2.tronco import tronco
from q3.plot import plot_projecao_from_points
from q4.plot import plot_perspectiva_from_points


def get_rectangle_faces(Z):
    return [
        [Z[0], Z[1], Z[2], Z[3]],
        [Z[4], Z[5], Z[6], Z[7]],
        [Z[0], Z[1], Z[5], Z[4]],
        [Z[2], Z[3], Z[7], Z[6]],
        [Z[1], Z[2], Z[6], Z[5]],
        [Z[4], Z[7], Z[3], Z[0]],
        [Z[2], Z[3], Z[7], Z[6]],
    ]

def plot_cone_from_points(points, num_points, ax):


    # Traçar as arestas do cone
    pontos_horizontais = np.array(points[0])
    pontos_verticais = np.array(points[1])
    
    x = pontos_horizontais[:, 0]
    y = pontos_horizontais[:, 1]
    z = pontos_horizontais[:, 2]
    for i in range(len(x) - 1):
        ax.plot([x[i], x[i + 1]], [y[i], y[i + 1]], [z[i], z[i + 1]], color="blue")

    for aresta in pontos_verticais:
      ax.plot(aresta[0], aresta[1], aresta[2], color="blue")
        


        


def draw_camera_and_vectors_in_world(
        ponto_camera, 
        vetor_up, 
        vetor_n, 
        vetor_u, 
        vetor_v, 
        cilindro, 
        cone, 
        num_points_cilindro, 
        num_points_cone
    ):
    camera = np.array(
        [
            [ponto_camera[0] - 0.5, ponto_camera[1] - 0.5, ponto_camera[2] - 0.5],
            [ponto_camera[0] + 0.5, ponto_camera[1] - 0.5, ponto_camera[2] - 0.5],
            [ponto_camera[0] + 0.5, ponto_camera[1] + 0.5, ponto_camera[2] - 0.5],
            [ponto_camera[0] - 0.5, ponto_camera[1] + 0.5, ponto_camera[2] - 0.5],
            [ponto_camera[0] - 0.5, ponto_camera[1] - 0.5, ponto_camera[2] + 0.5],
            [ponto_camera[0] + 0.5, ponto_camera[1] - 0.5, ponto_camera[2] + 0.5],
            [ponto_camera[0] + 0.5, ponto_camera[1] + 0.5, ponto_camera[2] + 0.5],
            [ponto_camera[0] - 0.5, ponto_camera[1] + 0.5, ponto_camera[2] + 0.5],
        ]
    )

    all_points = []
    all_points.extend(camera.tolist())
    all_points.extend([
        [0, 10, 10], [0, -10, 10], [0, -10, -10], [0, 10, -10],
        [10, 0, 10], [-10, 0, 10], [-10, 0, -10], [10, 0, -10],
        [10, 10, 0], [-10, 10, 0], [-10, -10, 0], [10, -10, 0]
    ])

    points = np.array(all_points)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.text(*[ponto_camera[0] + 1, ponto_camera[1] - 2, ponto_camera[2] - 1], "Câmera", c="Black")

    ax.text(*[ponto_camera[0] + 1, ponto_camera[1] - 2, ponto_camera[2] - 1], "Câmera", c="Black")

    # plot vertices
    ax.scatter3D(points[:, 0], points[:, 1], points[:, 2])

    ax.add_collection3d(
        Poly3DCollection(
            get_rectangle_faces(camera),
            facecolors="blue",
            linewidths=1,
            edgecolors="b",
            alpha=0.25,
        )
    )
    esfera(ax)
    cubo(ax)
    tronco(ax)
    plot_cone_from_points(cilindro,num_points_cilindro, ax)
    plot_cone_from_points(cone,num_points_cone, ax)

    # pontos_cilindro = cilindro(ax)
    # pontos_cone = cone(ax)
    # octantes
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

    # setas
    soa = np.array([
        [ponto_camera[0], ponto_camera[1], ponto_camera[2], vetor_up[0] * 5, vetor_up[1] * 5, vetor_up[2] * 5],
        [ponto_camera[0], ponto_camera[1], ponto_camera[2], vetor_n[0] * -5, vetor_n[1] * -5, vetor_n[2] * -5],
        [ponto_camera[0], ponto_camera[1], ponto_camera[2], vetor_u[0] * 5, vetor_u[1] * 5, vetor_u[2] * 5],
        [ponto_camera[0], ponto_camera[1], ponto_camera[2], vetor_v[0] * 5, vetor_v[1] * 5, vetor_v[2] * 5]
    ])

    X, Y, Z, U, V, W = zip(*soa)
    ax.quiver(X, Y, Z, U, V, W)
    plt.show()


    
def q3(
        pontos_cilindro, 
        pontos_cone, 
        ponto_camera=np.array([-5, 5, 5]),
        show=False,
        num_points_cilindro = 10,
        num_points_cone = 10
        ):
    cilindro = np.array(pontos_cilindro[0])
    cone = np.array(pontos_cone[0])

    centro_cilindro = [(max(cilindro[:, i]) + min(cilindro[:, i])) / 2 for i in range(3)]
    centro_cone = [(max(cone[:, i]) + min(cone[:, i])) / 2 for i in range(3)]

    ponto_medio = np.add(centro_cilindro, centro_cone) / 2

    if show:
        print("Centro cilindro", centro_cilindro)
        print("Centro cone", centro_cone)
        print("Ponto médio", ponto_medio)


    vetor_n = np.subtract(ponto_camera, ponto_medio)

    vetor_up = [0, 0, 1]

    vetor_u = np.cross(vetor_up, vetor_n)
    vetor_v = np.cross(vetor_n, vetor_u)

    if show:
        print("Vetor n, u e v:", vetor_n, vetor_u, vetor_v)


    vetor_n = np.divide(vetor_n, np.linalg.norm(vetor_n))
    vetor_u = np.divide(vetor_u, np.linalg.norm(vetor_u))
    vetor_v = np.divide(vetor_v, np.linalg.norm(vetor_v))

    if show:
        print("Vetor n, u e v:", vetor_n, vetor_u, vetor_v)

    V = np.matrix([
        [vetor_u[0], vetor_u[1], vetor_u[2],
         - ponto_camera[0] * vetor_u[0] - ponto_camera[1] * vetor_u[1] - ponto_camera[2] * vetor_u[2]],
        [vetor_v[0], vetor_v[1], vetor_v[2],
         - ponto_camera[0] * vetor_v[0] - ponto_camera[1] * vetor_v[1] - ponto_camera[2] * vetor_v[2]],
        [vetor_n[0], vetor_n[1], vetor_n[2],
         - ponto_camera[0] * vetor_n[0] - ponto_camera[1] * vetor_n[1] - ponto_camera[2] * vetor_n[2]],
        [0, 0, 0, 1]
    ])

    def transform_camera_arestas_verticais(object_points):
        #trazer pra camera os pontos da base inferior
        p1 = np.ones((len(object_points) + 1, 4))
        for i in range(len(object_points)):
            p1[i][0] = object_points[i][0][0]
            p1[i][1] = object_points[i][1][0]
            p1[i][2] = object_points[i][2][0]

        p1 = (V * p1.transpose()).transpose()[0:10]
        aresta_base = np.array([[point[0], point[1], point[2]] for point in p1.A])
        #trazer os pontos da base superior 
        p2 = np.ones((len(object_points) + 1, 4))
        for i in range(len(object_points)):
            p2[i][0] = object_points[i][0][1]
            p2[i][1] = object_points[i][1][1]
            p2[i][2] = object_points[i][2][1]

        p2 = (V * p2.transpose()).transpose()[0:10]
        aresta_topo = np.array([[point[0], point[1], point[2]] for point in p2.A])
        return aresta_topo, aresta_base
    

    def transform_camera(object_points):
        p = np.ones((len(object_points) + 1, 4))
        for i in range(len(object_points)):
            p[i][0] = object_points[i][0]
            p[i][1] = object_points[i][1]
            p[i][2] = object_points[i][2]

        p = (V * p.transpose()).transpose()[0:200]
        return np.array([[point[0], point[1], point[2]] for point in p.A])
    
    if show:
        print("Transformação V", V)
    
    cilindro_projetado = transform_camera(cilindro)
    arestas_verticais_cilindro = np.array(pontos_cilindro[1])
    arestas_verticais_cilindro_projetada = transform_camera_arestas_verticais(arestas_verticais_cilindro)

    cone_projetado = transform_camera(cone)
    arestas_verticais_cone = np.array(pontos_cone[1])
    arestas_verticais_cone_projetada = transform_camera_arestas_verticais(arestas_verticais_cone)

    if show:
        draw_camera_and_vectors_in_world(
            ponto_camera,
            vetor_up,
            vetor_n,
            vetor_u,
            vetor_v,
            pontos_cilindro,
            pontos_cone,
            pontos_cilindro,
            pontos_cone
        )
        #projeção
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
        all_points = []
        all_points.extend(cilindro_projetado.tolist())
        all_points.extend(cone_projetado.tolist())
        points = np.array(all_points)

        # ax.scatter3D(points[:, 0], points[:, 1], points[:, 2])
        # plot_cone_from_points([cilindro_projetado, []], num_points_cilindro, ax)
        plot_projecao_from_points([cilindro_projetado, arestas_verticais_cilindro_projetada], num_points_cilindro, ax)
        plot_projecao_from_points([cone_projetado, arestas_verticais_cone_projetada], num_points_cilindro, ax)
        

        

        # Plotar os pontos

        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")

        plt.show()
        
        return [cilindro_projetado, arestas_verticais_cilindro_projetada], [cone_projetado, arestas_verticais_cone_projetada]

        



    print("camera")