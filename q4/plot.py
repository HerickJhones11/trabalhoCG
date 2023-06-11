import numpy as np


def plot_perspectiva_from_points(cilindro_projetado, arestas_verticais_cilindro_projetada, ax, color):
    width = 800
    height = 600
    ratio = width/height
    alfa = np.pi/4 
    far = 4 
    near = 8
    matriz_projecao_perspectiva = np.array([
            [1/(ratio*np.tan(alfa/2)), 0, 0, 0],
            [0, 1/np.tan(alfa/2), 0, 0 ],
            [0, 0, far/(far - near), 1],
            [0, 0, (-near*far)/(far - near), 0]
        ])
    
    points_list = []
    for ponto in cilindro_projetado:
        vertice_2d = np.dot([ponto[0], ponto[1], ponto[2], 1], [matriz_projecao_perspectiva])
        x = vertice_2d[0][0]
        y = vertice_2d[0][1]
        points_list.append([x, y])

    points_array = np.array(points_list)
    px = points_array[:, 0]
    py = points_array[:, 1]
    for i in range(len(px) - 1):
        ax.plot([px[i], px[i + 1]], [py[i], py[i + 1]], color=color)


    arestas_verticais_cilindro_perspectiva = [[],[]]
    for i in range(0, len(arestas_verticais_cilindro_projetada[0])) :
        x_start = arestas_verticais_cilindro_projetada[0][i][0]
        y_start = arestas_verticais_cilindro_projetada[0][i][1]
        z_start = arestas_verticais_cilindro_projetada[0][i][2]

        x_end = arestas_verticais_cilindro_projetada[1][i][0]
        y_end = arestas_verticais_cilindro_projetada[1][i][1]
        z_end = arestas_verticais_cilindro_projetada[1][i][2]

        vertice_2d_inicio = np.dot([x_start, y_start, z_start, 1], [matriz_projecao_perspectiva])
        x = vertice_2d_inicio[0][0]
        y = vertice_2d_inicio[0][1]
        arestas_verticais_cilindro_perspectiva[0].append([x, y])

        vertice_2d_fim = np.dot([x_end, y_end, z_end, 1], [matriz_projecao_perspectiva])
        x = vertice_2d_fim[0][0]
        y = vertice_2d_fim[0][1]
        arestas_verticais_cilindro_perspectiva[1].append([x, y])

    for i in range(0, len(arestas_verticais_cilindro_perspectiva[0])) :
        x_start = arestas_verticais_cilindro_perspectiva[0][i][0]
        x_end = arestas_verticais_cilindro_perspectiva[1][i][0]

        y_start = arestas_verticais_cilindro_perspectiva[0][i][1]
        y_end = arestas_verticais_cilindro_perspectiva[1][i][1]

        ax.plot([x_start, x_end], [y_start, y_end], color=color)