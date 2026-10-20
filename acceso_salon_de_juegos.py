# Planteo mis variables
from datetime import date

fechaNacimiento = input("Ingrese su fecha de nacimiento (YYYY-MM-DD): ")
fechaNacimiento = date.fromisoformat(fechaNacimiento)

hoy = date.today()

#  Calculo la edad de la persona

edad = hoy.year - fechaNacimiento.year

edad = edad - ((hoy.month, hoy.day) < (fechaNacimiento.month, fechaNacimiento.day))

# Creo un algoritmo booleano para entrar o no a un salon de juegos

if (edad >= 18):
    print("Puedes pasar")

else:
    print ("No puedes pasar")

