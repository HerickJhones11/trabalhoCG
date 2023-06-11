import numpy as np


def plot_projecao_from_points(points, num_points, ax):


    # Traçar as arestas do cone
    pontos_horizontais = np.array(points[0])
    pontos_verticais = np.array(points[1])
    
    x = pontos_horizontais[:, 0]
    y = pontos_horizontais[:, 1]
    z = pontos_horizontais[:, 2]
    for i in range(len(x) - 1):
        ax.plot([x[i], x[i + 1]], [y[i], y[i + 1]], [z[i], z[i + 1]], color="blue")

    for i in range(0, len(pontos_verticais[0])) :
      
      x_start = pontos_verticais[0][i][0]
      x_end = pontos_verticais[1][i][0]

      y_start = pontos_verticais[0][i][1]
      y_end = pontos_verticais[1][i][1
                                     ]
      z_start = pontos_verticais[0][i][2]
      z_end = pontos_verticais[1][i][2]


      ax.plot([x_start, x_end], [y_start, y_end], [z_start, z_end], color="blue")