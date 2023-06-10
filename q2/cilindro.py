from matplotlib import pyplot as plt
import numpy as np

def rotation_matrix_3d(axis, angle):
    x, y, z = axis
    c = np.cos(angle)
    s = np.sin(angle)
    C = 1 - c

    rotation_matrix = np.array([
        [x*x*C + c, x*y*C - z*s, x*z*C + y*s],
        [y*x*C + z*s, y*y*C + c, y*z*C - x*s],
        [x*z*C - y*s, y*z*C + x*s, z*z*C + c]
    ])

    return rotation_matrix

def plot_cone(
        center,
        radius,
        height,
        top_radius_ratio,
        num_slices,
        num_points,
        ax,
        translation,
        scale,
        rotation_angle,
        rotation_axis
    ):

    center = (center[0] + translation[0], center[1] + translation[1], center[2] + translation[2])
    z = np.linspace(center[2], center[2] + height, num_slices)

    rotation_matrix = rotation_matrix_3d(rotation_axis, rotation_angle)
    points_list = []
    for i in range(num_slices):
        theta = np.linspace(0, 2 * np.pi, num_points) # de 0 até 2pi
        r = radius * (1 - (i/num_slices) * (1 - top_radius_ratio))  # Reduz o raio para formar o cone com a tampa superior

        x = center[0] + r * np.cos(theta) * scale[0]
        y = center[1] + r * np.sin(theta) * scale[1]
        z_val = np.full_like(theta, z[i]) * scale[2]

        points = np.column_stack((x, y, z_val))
        rotated_points = np.dot(points, rotation_matrix)

        points_list.extend(rotated_points.tolist())


        ax.plot(rotated_points[:, 0], rotated_points[:, 1], rotated_points[:, 2], color="blue")


        if i == 0:
            x_start = rotated_points[:, 0]
            y_start = rotated_points[:, 1]
            z_start = rotated_points[:, 2]
        if i == (num_slices - 1):
            x_end = rotated_points[:, 0]
            y_end = rotated_points[:, 1]
            z_end = rotated_points[:, 2]

    arestas_verticais = []
    for j in range(len(x_start)):
      aresta = ([x_start[j], x_end[j]], [y_start[j], y_end[j]], [z_start[j], z_end[j]])
      arestas_verticais.append(aresta)

    for aresta in arestas_verticais:
      ax.plot(aresta[0], aresta[1], aresta[2], color="blue")


    return points_list, arestas_verticais


def cilindro(ax):
    centro = (0, 0, 0)  # Coordenadas do centro do cone
    raio_base = 1.5  # Raio da base do cone
    altura = 2*raio_base  # Altura do cone
    tamanho_tampa_superior = 1  # Tamanho da tampa superior em relação à base (valor entre 0 e 1)
    raio_superior = raio_base * tamanho_tampa_superior  # Raio da tampa superior
    numero_fatias = 20  # Número de fatias do cone
    num_points = 10
    translacao = [6, 4, 2]
    scale = [1, 1, 1]
    angulo_rotacao = np.pi/4  # Ângulo de rotação (45 graus)
    eixo_rotacao = (0, 0, 0)  
    arestar_horizontais, arestas_verticais = plot_cone(centro, raio_base, altura, tamanho_tampa_superior, numero_fatias, num_points, ax, translacao, scale, angulo_rotacao, eixo_rotacao)
    return arestar_horizontais, arestas_verticais