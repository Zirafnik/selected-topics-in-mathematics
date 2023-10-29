import sympy as sp

# Ex 1
# a = sp.symbols("a")

# v1 = sp.Matrix([4 * a, 5 * a])

# Ex 2
matrix = sp.Matrix([[-1, 1, 0, 2], [2, 3, -1, 4], [3, 2, -1, 2]])

At = matrix.transpose().rref()
image = sp.Matrix(At[0]).columnspace()
print(image)
