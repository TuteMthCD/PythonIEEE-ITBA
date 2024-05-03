import numpy as np
    
notas = np.array([])

for _ in range(3):
    notas = np.append(notas, int( input()))

print(notas.mean())
