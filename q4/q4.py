from matplotlib import pyplot as plt
from q4.plot import plot_perspectiva_from_points


def q4(cilindro, cone):
    fig = plt.figure()
    ax = fig.add_subplot(111)

    plot_perspectiva_from_points(cilindro[0], cilindro[1], ax, "blue")
    plot_perspectiva_from_points(cone[0], cone[1], ax, "red")

    plt.gca().set_aspect('equal')
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    plt.show()