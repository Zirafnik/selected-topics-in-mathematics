import sympy as sp
from sympy.abc import x, y, z

# October 10, 2023

# Problem 1.1
seatsTotal = 50
cargoTotal = 150

seatsEq = sp.Eq(1 * x + 2 * y + 4 * z, seatsTotal)
cargoEq = sp.Eq(4 * x + 7 * y + 10 * z, cargoTotal)

solution = sp.solve((seatsEq, cargoEq), (x, y, z))

print(solution)

solution2 = sp.solve((solution[x], solution[y]), (z))

print(solution2)
