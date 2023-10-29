import numpy as np
import itertools

vector1 = np.array([1 / 3, 2 / 3, 2 / 3])
vector2 = np.array([2 / 3, 1 / 3, -2 / 3])
vector3 = np.array([2 / 3, -2 / 3, 1 / 3])

Q = np.array([vector1, vector2, vector3])

possibleLambdas = [0, 1, -1]
permutations = list(itertools.permutations(possibleLambdas))

for perm in permutations:
    lambda1, lambda2, lambda3 = perm

    D = np.array([[lambda1, 0, 0], [0, lambda2, 0], [0, 0, lambda3]])

    product = np.dot(np.dot(Q, D), Q)

    Av1 = np.dot(product, vector1)
    Av2 = np.dot(product, vector2)
    Av3 = np.dot(product, vector3)

    L1v1 = lambda1 * vector1
    L2v2 = lambda2 * vector2
    L3v3 = lambda3 * vector3

    print(np.array_equal(Av1, L1v1))
    print(np.array_equal(Av2, L2v2))
    print(np.array_equal(Av3, L3v3))
    print("========================")
