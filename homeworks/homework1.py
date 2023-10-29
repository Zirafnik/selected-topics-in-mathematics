import numpy as np
import sympy as sp
from sympy.abc import x, y, z

# October 16, 2023

# Problem 1
sol11 = complex(2, -3) * complex(5, 2)
print(f"Ex1.1: {sol11}")

# Problem 4
eq1 = sp.Eq(4 * x + 2 * y + z, 6)
eq2 = sp.Eq(x - 3 * y + 2 * z, 4)
eq3 = sp.Eq(3 * x + 5 * y - z, 1)

solution = sp.solve((eq1, eq2), (x, y, z))

print(f"Ex4: {solution}")

# Problem 5
a = sp.symbols("a")
a = -3
A = sp.Matrix([[a + 4, a + 1, 3], [-1, 2, 1], [a + 6, 1, 3]])

rankA = A.rank()
rrefA = A.echelon_form()

checkedSolutions = []
for row in rrefA.tolist():
    commonEq = 0
    for index in row:
        commonEq += index

    equation = sp.Eq(commonEq, 0)
    solutionsEq = sp.solve(equation, a)

    # check that solutions make all indeces in row 0
    for sol in solutionsEq:
        allZero = True
        for index in row:
            iEq = sp.Eq(index, 0)

            if iEq.subs({a: sol}) != True:
                allZero = False
                break

        if allZero:
            checkedSolutions.append(sol)


print(f"Ex5: {rankA}, {rrefA}, {checkedSolutions}")

# Problem 7
from scipy import linalg

A = np.array([[1, 0, 0, -1], [3, 3, 4, 6], [-3, 2, 5, 9], [-4, -5, 6, 1]])
# detA = np.linalg.det(A)
detA = linalg.det(A)


print(f"Ex7: {detA}")

# Problem 8
A = np.array([[1, 2, -1], [2, 3, -1], [4, 1, 4]])

inverseA = np.linalg.inv(A)

print(f"Ex8: {inverseA}")
