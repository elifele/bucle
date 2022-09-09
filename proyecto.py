#Ejercicio bucle for con listas
from time import sleep

coundown = [4,3,2,1]

for numero in coundown:
    print(numero)
    sleep(1)#pausa 1 segondo
print("Despegar")



#ejercicio 2 bucle for
coundown = [4,3,2,1]

for numero in coundown:
    print(numero)
print("despegar")



#Ejercicio de bucle while.pedir al usuario numero entero positivo

n = int(input("Ingresa un numero entero positivo: "))

while n < 0:
    print("Error ingresó numero negativo")
    n = int(input("Ingrese de nuevo numero entero positivo: "))

print("Numero correcto")
