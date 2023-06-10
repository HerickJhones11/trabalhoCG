from matplotlib import pyplot as plt
import numpy as np

from q1.plot import plot_cone, plot_cubo, plot_esfera, plot_tronco


def cilindro():
    centro = (0, 0, 0)  # Coordenadas do centro do cone
    raio_base = 6  # Raio da base do cone
    altura = 2*raio_base  # Altura do cone
    tamanho_tampa_superior = 1  # Tamanho da tampa superior em relação à base (valor entre 0 e 1)
    raio_superior = raio_base * tamanho_tampa_superior  # Raio da tampa superior
    numero_fatias = 20  # Número de fatias do cone
    plot_cone(centro, raio_base, altura, top_radius_ratio=tamanho_tampa_superior, num_slices=numero_fatias)

def cone():
    # Exemplo de uso
    centro = (0, 0, 0)  # Coordenadas do centro do cone
    raio_base = 6  # Raio da base do cone
    altura = 2*raio_base  # Altura do cone
    tamanho_tampa_superior = 0  # Tamanho da tampa superior em relação à base (valor entre 0 e 1)
    raio_superior = raio_base * tamanho_tampa_superior  # Raio da tampa superior
    numero_fatias = 20  # Número de fatias do cone
    plot_cone(centro, raio_base, altura, top_radius_ratio=tamanho_tampa_superior, num_slices=numero_fatias)

def esfera():
    radius = 2.0  # Raio da esfera
    plot_esfera(radius)
    plt.show()

def cubo():
    edge_length = 4.0
    plot_cubo(edge_length)

def tronco():
    base = 2.0  # Comprimento da base inferior do tronco de pirâmide
    topo = 1.0     # Comprimento da base superior do tronco de pirâmide
    height = 3.0              # Altura do tronco de pirâmide

    plot_tronco(base, topo, height)


def q1():
    # cilindro()
    # cone()
    # esfera()
    # cubo()
    tronco()
    return