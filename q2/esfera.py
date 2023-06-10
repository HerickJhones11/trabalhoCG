import numpy as np

def plot_esfera(ax, translacao, escala, angulos_rotacao):
    radius = 1.5  # Raio da esfera
    u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
    x = radius * np.cos(u) * np.sin(v) 
    y = radius * np.sin(u) * np.sin(v) 
    z = radius * np.cos(v) 


    escala_x = escala[0]
    escala_y = escala[1]
    escala_z = escala[2]

    x = x * escala_x
    y = y * escala_y
    z = z * escala_z

    angulos_rotacao = [45, 30, 60]  
    pontos_rotacionados = np.array([rotacionar_ponto(np.array([x[i, j], y[i, j], z[i, j]]), angulos_rotacao) for i in range(x.shape[0]) for j in range(x.shape[1])])
    x_rotacionado = pontos_rotacionados[:, 0].reshape(x.shape) + translacao[0]
    y_rotacionado = pontos_rotacionados[:, 1].reshape(x.shape) + translacao[1]  
    z_rotacionado = pontos_rotacionados[:, 2].reshape(x.shape) + translacao[2] 

    
    ax.plot_surface(x_rotacionado, y_rotacionado, z_rotacionado, color="r", edgecolor="r")


def rotacionar_ponto(ponto, angulos):
    # Conversão dos ângulos para radianos
    angulos_rad = np.radians(angulos)
    # Matriz de rotação em torno dos eixos x, y, z
    matriz_rot_x = np.array([[1, 0, 0], [0, np.cos(angulos_rad[0]), -np.sin(angulos_rad[0])], [0, np.sin(angulos_rad[0]), np.cos(angulos_rad[0])]])
    matriz_rot_y = np.array([[np.cos(angulos_rad[1]), 0, np.sin(angulos_rad[1])], [0, 1, 0], [-np.sin(angulos_rad[1]), 0, np.cos(angulos_rad[1])]])
    matriz_rot_z = np.array([[np.cos(angulos_rad[2]), -np.sin(angulos_rad[2]), 0], [np.sin(angulos_rad[2]), np.cos(angulos_rad[2]), 0], [0, 0, 1]])
    # Aplicação das rotações nos pontos
    ponto_rot = np.dot(matriz_rot_z, np.dot(matriz_rot_y, np.dot(matriz_rot_x, ponto)))


    return ponto_rot

def esfera(ax):
    translacao = [-3, -3, -7]
    escala = [0.75, 0.75, 0.75]
    angulos_rotacao = [45, 30, 60] # Ângulos de rotação em graus
    plot_esfera(ax, translacao, escala, angulos_rotacao)