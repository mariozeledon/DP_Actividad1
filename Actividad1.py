import math
print("1. Calcular el promedio de 5 valores numéricos ingresados por el usuario.")
print("Ingrese 5 valores numéricos:")
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())
promedio = (num1+num2+num3+num4+num5)/5 
print("El promedio de los 5 valore ingresados es ",promedio)
print("")
print("2. Calcular la hipotenusa de un triángulo rectángulo")
ladoA = int(input("Ingrese el lado A "))
ladoB = int(input("Ingrese el lado B "))
ladoC = math.sqrt(pow(ladoA,2)+pow(ladoB,2))
print("La hipotenusa del tríángulo es igual a ",ladoC)
print("")
print("3. Indicar cual de 2 valores es el mayor y cual el menor.")
num1_3 = int(input("Ingrese un número "))
num2_3 = int(input("Ingrese otro número "))
if num1_3 > num2_3:
    print("El número mayor es ",num1_3)
    print("El número menor es ",num2_3)
elif num2_3 > num1_3:
    print("El número mayor es ",num2_3)
    print("El número menor es ",num1_3)
print("")
print("4. Indicar cual de 3 valores es el mayor.")
num1_4 = int(input("Ingrese el 1er. número "))
num2_4 = int(input("Ingrese el 2do. número "))
num3_4 = int(input("Ingrese el 3er. número "))
if num1_4 > num2_4 and num1_4 > num3_4:
    print("El número mayor es ",num1_4)
elif num2_4 > num1_4 and num2_4 > num3_4:
    print("El número mayor es ",num2_4)
elif num3_4 > num1_4 and num3_4 > num2_4:
    print("El número mayor es ",num3_4)
print("")
print("5. Mostrar los números continuos del 1 hasta el 20.")
for continuos in range(1,21):
    print(continuos)
print("")
print("6. Mostrar la tabla de multiplicación de un valor ingresado por el usuario.")
num1_6 = int(input("Ingrese un número "))
print("Tabla de multiplicar del ",num1_6)
for multiplicar in range(1,11):
    print(multiplicar, " x ", num1_6, " = ",multiplicar*num1_6)
print("")
num1_7 = int(0)
print("7. Mostrar cuantas veces se repite la letra S en un texto ingresado por el usuario.")
texto = input("Ingrese un texto ")
for letra in texto:
    if letra == "s" or letra == "S":
        num1_7 = num1_7+1
print("La cantidad de letras S encontradas en el texto es de ",num1_7)
print("")
num1_8 = int(0)
print("8. Indicar cuantas vocales hay en un texto.")
texto1 = input("Ingrese un texto ")
for vocal in texto1:
    if vocal == "a" or vocal == "e" or vocal == "i" or vocal == "o" or vocal == "u" or vocal == "A" or vocal == "E" or vocal == "I" or vocal == "O" or vocal == "U":
        num1_8 = num1_8 + 1
print("La cantidad de vocales encontradas en el texto es de ",num1_8)
