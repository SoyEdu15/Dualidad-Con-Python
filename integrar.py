import numpy as np
from scipy.optimize import linprog

# Definir la matriz de coeficientes de la función objetivo
c = np.array([-1, -2, -3])  # Coeficientes negativos para maximizar

# Definir la matriz de coeficientes de las restricciones
A = np.array([
    [1, 2, 1],
    [2, 3, 1],
    [1, 1, 2]
])

# Definir los términos independientes de las restricciones
b = np.array([6, 15, 4])

# Calcular las dualidades con el método 'revised simplex'
res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None), method='revised simplex')

# Imprimir los resultados
Soluciondeprimal=( res.x)
Valoroptimo=(-res.fun)  # Tomamos el negativo del valor óptimo para obtener el valor real
Valoresdelasvariablesduales=(res.x)