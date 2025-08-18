"""
TRABAJO PRACTICO N°1. Estructuras Secuenciales.
Realizado por: Alarcón Esteban Manuel
"""

# Ejercicio 1. --------------------------------------------------------
# Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

"""print("Hola Mundo!")"""

# Ejercicio 2. -----------------------------------------------------------------------------------------------
# Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado.

"""print("Ingrese su nombre:")
nombre = input()
print("Hola " + nombre)"""

# Ejercicio 3. -------------------------------------------------------------------------------------------------------------------------------------
# Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados.

"""nombre = input("Ingrese su nombre:")
apellido = input("Ingrese su apellido:")
edad = input("Ingrese su edad:")
lugar_residencia = input("Ingrese su lugar de residencia:")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_residencia}.")"""

# Ejercicio 4. ----------------------------------------------------------------------------------------------
# Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.

"""radio = float(input("Ingrese el radio del círculo: "))
area = 3.14159 * radio**2
print(f"El área es {area} y el perímetro es {2 * 3.14159 * radio}.")"""

# Ejercicio 5. --------------------------------------------------------------------------------------------------
# Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.

"""segundos = input("Ingrese el número de segundos: ")
print("La cantidad de horas es:", int(segundos) / 3600)"""

# Ejercicio 6. ---------------------------------------------------------------------------------------------------
#  Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.

"""numero = int(input("Ingrese un número: "))
print("La tabla de multiplicar de", numero, "es:")
print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")"""

# Ejercicio 7. ------------------------------------------------------------------------------------------------------------------------------------------------------
#  Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

"""num1 = int(input("Ingrese el primer número (distinto de 0): "))
num2 = int(input("Ingrese el segundo número (distinto de 0): "))

print(f"La suma es: {num1 + num2}")
print(f"La resta es: {num1 - num2}")
print(f"La multiplicación es: {num1 * num2}")
print(f"La división es: {num1 / num2}")"""

# Ejercicio 8
# Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal.

"""altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kilogramos: "))
imc = peso / (altura ** 2)
print(f"Su índice de masa corporal es: {imc}")"""

# Ejercicio 9. ----------------------------------------------------------------------------------------------------------------------
# Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.

"""celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"El equivalente en grados Fahrenheit es: {fahrenheit}")"""

# Ejercicio 10. ----------------------------------------------------------------------------------------------------------------------
# Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.

"""num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio de los tres números es: {promedio}")"""