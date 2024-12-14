##EJERCICIO 4
    
x= int(input("Ingrese un numero entero positivo"))
suma = 0
if x > 0:
    for i in range(1, x):
            if x % i == 0:
                suma += i
if suma == x:
        print(f"El numero {x}, es perfecto")
else:
    print(f"El numero {x}, no es perfecto")




 