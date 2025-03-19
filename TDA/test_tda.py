# Creación de números complejos
from TDA.complejo import complejo
from TDA.fraccion import Fraccion

c1 = complejo(3, 4)
c2 = complejo(1, -2)

# Operaciones con números complejos
suma_c = c1.sumar(c2)
resta_c = c1.restar(c2)
multiplicacion_c = c1.multiplicar(c2)

# Resultados
print(f"Número Complejo 1: {c1}")
print(f"Número Complejo 2: {c2}")
print(f"Suma: {suma_c}")
print(f"Resta: {resta_c}")
print(f"Multiplicación: {multiplicacion_c}")

# Creación de fracciones
f1 = Fraccion(3, 4)
f2 = Fraccion(2, 5)

# Operaciones con fracciones
suma = f1.sumar(f2)
resta = f1.restar(f2)
multiplicacion = f1.multiplicar(f2)
comparacion = f1.comparar(f2)  # Positivo si f1 > f2, 0 si iguales, negativo si f1 < f2

# Resultados
print(f"Fracción 1: {f1}")
print(f"Fracción 2: {f2}")
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"Comparación (positivo si f1 > f2, negativo si f1 < f2, 0 si iguales): {comparacion}")
