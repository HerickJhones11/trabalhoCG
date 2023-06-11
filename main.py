import numpy as np
from q1.q1 import q1
from q2.q2 import q2
from q3.q3 import q3
from q4.q4 import q4

if __name__ == "__main__":
    # q1()
    pontos_cilindro, pontos_cone  = q2()

    cilindro, cone = q3(pontos_cilindro, pontos_cone, np.array([-5, 5, 5]), True)

    q4(cilindro, cone)