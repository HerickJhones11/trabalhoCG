import numpy as np
from q1.q1 import q1
from q2.q2 import q2
from q3.q3 import q3

if __name__ == "__main__":
    # q1()
    pontos_cilindro, pontos_cone = q2()
    q3(pontos_cilindro, pontos_cone, np.array([-5, 5, 5]), True)