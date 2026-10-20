#Ejercicio 4.6.1. Escribir dos funciones que resuelvan los siguientes problemas:
#a) Dado un número entero 𝑛, indicar si es par o no.
my_number = int(input("Ingrese un número entero: "))
remainder = my_number % 2
if remainder == 0:
    result = True
else:
    result = False
print(f"El número {my_number} es {'par' if result else 'impar'}.")

#b) Dado un número entero 𝑛, indicar si es primo o no.
my_number = int(input("Ingrese un número entero: "))
if my_number <= 1:
    is_prime = False
elif my_number == 2:
    is_prime = True
elif my_number % 2 == 0:
    is_prime = False
else:
    is_prime = True
    i = 3
    while i*i <= my_number and is_prime:
        if my_number % i == 0:
            is_prime = False
        i+=2
print(f"El número {my_number} es {'primo' if is_prime else 'no primo'}.")

# Ejercicio 4.6.2. Escribir una implementación propia de la función abs, que devuelva el valor
# absoluto de cualquier valor que reciba.
input_number = float(input("Ingrese un número: "))
def mi_abs(x):
    if x < 0:
        return -x
    else:
        return x
print(f"El valor absoluto de {input_number} es {mi_abs(input_number)}")

# Ejercicio 4.6.3. Escribir una función que reciba por parámetro una dimensión 𝑛, e imprima la
# matriz identidad correspondiente a esa dimensión.
def imprimir_matriz_identidad(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                print(1, end=" ")
            else:
                print(0, end=" ")
        print()

n = int(input("Ingrese la dimensión de la matriz identidad: "))
imprimir_matriz_identidad(n)

# Ejercicio 4.6.4. Escribir funciones que permitan encontrar:
# a) El máximo o mínimo de un polinomio de segundo grado (dados los coeficientes a, b y
# c), indicando si es un máximo o un mínimo.

a = float(input("Ingrese el coeficiente a: "))
b = float(input("Ingrese el coeficiente b: "))
c = float(input("Ingrese el coeficiente c: "))
x = -b/(2*a)
y = a*pow(x, 2) + b*x + c
coords = (x, y)
if a<0:
    print(f"El polinomio tiene un máximo en el punto {coords}.")
else:
    print(f"El polinomio tiene un mínimo en el punto {coords}.")
# b) Las raíces (reales o complejas) de un polinomio de segundo grado.
# Nota: validar que las operaciones puedan efectuarse antes de realizarlas (no dividir por
# cero, ni calcular la raíz de un número negativo).
def validar_coeficientes(a, b, c):
    for nombre, valor in (("a", a), ("b", b), ("c", c)):
        if not isinstance(valor, (int, float)):
            raise TypeError(f"'{nombre}' debe ser un número.")
    if a == 0:
        raise ValueError("'a' no puede ser 0.")
    
def discriminante(a, b, c):
    return b ** 2 - 4 * a * c

import math

def raices_segundo_grado(a, b, c):
    validar_coeficientes(a, b, c)
    d = discriminante(a, b, c)
    den = 2 * a                      # seguro: a != 0

    if d >= 0:                       # sqrt es válida
        raiz = math.sqrt(d)
        return (-b + raiz) / den, (-b - raiz) / den
    else:                            # d < 0: pasamos a complejos
        real = -b / den
        imag = math.sqrt(-d) / den   # -d es positivo, sqrt válida
        return complex(real, imag), complex(real, -imag)

casos = [(1, -3, 2), (1, 2, 1), (1, 2, 5), (0, 2, 1)]

for a, b, c in casos:
    try:
        print((a, b, c), "->", raices_segundo_grado(a, b, c))
    except (TypeError, ValueError) as e:
        print((a, b, c), "-> Error:", e)

# c) La intersección de dos rectas (dadas las pendientes y ordenada al origen de cada recta).
# Nota: validar que no sean dos rectas con la misma pendiente, antes de efectuar la operación.
m1 = float(input("Ingrese la pendiente de la primera recta: "))
b1 = float(input("Ingrese la ordenada al origen de la primera recta: "))
m2 = float(input("Ingrese la pendiente de la segunda recta: "))
b2 = float(input("Ingrese la ordenada al origen de la segunda recta: "))
def interseccion_rectas(m1, b1, m2, b2):
    if m1 == m2:
        raise ValueError("Las rectas son paralelas y no se intersectan.")
    x = (b2 - b1) / (m1 - m2)
    y = m1 * x + b1
    return (x, y)
try:
    print("La intersección de las rectas es:", interseccion_rectas(m1, b1, m2, b2))
except ValueError as e:
    print("Error:", e)
