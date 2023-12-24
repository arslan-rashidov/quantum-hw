import numpy as np


def shor_classical_factorization(n, Q, a, y, r):
    if np.isclose(y * r / Q, round(y * r / Q)):
        p = np.gcd(int(np.power(a, r // 2) + 1), n)
        q = np.gcd(int(np.power(a, r // 2) - 1), n)
        if 1 < p < n and 1 < q < n and p * q == n:
            return p, q
        else:
            return
    else:
        return


n_example = 15
Q_example = 2
a_example = 7
y_example = 1
r_example = 4
print(shor_classical_factorization(n_example, Q_example, a_example, y_example, r_example))
