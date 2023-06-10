from matplotlib import pyplot as plt
import numpy as np

from q2.cilindro import plot_cone



def cone(ax):
    centro = (0, 0, 0)  # Coordenadas do centro do cone
    raio_base = 1.5  # Raio da base do cone
    altura = 2*raio_base  # Altura do cone
    tamanho_tampa_superior = 0  # Tamanho da tampa superior em relação à base (valor entre 0 e 1)
    raio_superior = raio_base * tamanho_tampa_superior  # Raio da tampa superior
    numero_fatias = 20  # Número de fatias do cone
    num_points = 10
    translacao = [7, 9, 2]
    scale = [1.5, 1.5, 1.5]
    angulo_rotacao = np.pi/4  # Ângulo de rotação (45 graus)
    eixo_rotacao = (0, 0, 0) 
    arestar_horizontais, arestas_verticais = plot_cone(centro, raio_base, altura, tamanho_tampa_superior, numero_fatias, num_points, ax, translacao, scale, angulo_rotacao, eixo_rotacao)
    return arestar_horizontais, arestas_verticais
 