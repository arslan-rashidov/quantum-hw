import numpy as np

def shor_classical(n, Q, a, y):
    if np.isclose(y * r / Q, round(y * r / Q)):

        p = np.gcd(int(np.power(a, r // 2) + 1), n)
        q = np.gcd(int(np.power(a, r // 2) - 1), n)

        if 1 < p < n and 1 < q < n and p * q == n:
            return p, q
        else:
            return "Перейдите к следующему a"
    else:
        return "Перейдите к следующему a"

n = 15
Q = 2
a = 7
y = 1
r = 4

result = shor_classical(n, Q, a, y)
print(result)