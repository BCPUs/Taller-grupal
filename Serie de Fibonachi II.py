numero = int(input("Ingresa un numero entero positivo: "))
if numero== 0 or numero == 1:
    print(f"El numero {numero} pertenece a la serie de fibonacchi. ")
else:
    a, b = 0 , 1
    while b<numero:
        a, b = b, a + b

if b == numero:
    print(f"el numero {numero} pertenece a la serie de fibonacchi.")
else:
    print(f"el numero {numero} no pertenece a la serie de fibonacchi.")