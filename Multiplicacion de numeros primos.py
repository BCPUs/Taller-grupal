##Numeros primos 
# Como primer paso solicitamos al usuario que nos de un numero inicial y un numero final para empezar el contador
rango_inicial = int(input("Ingresa el número inicial del rango: \n"))
rango_final = int(input("Ingresa el número final del rango: \n"))

# Verificamos si el rango inicial es mayor que el final, ya que caso contrario no podria realizarse la operacion 
if rango_inicial > rango_final:
    print("El número inicial no puede ser mayor que el número final.")
else:
    ## En este paso verificamos cual es el numero inicial y cual es el numero final para empezar el bucle , en donde el programa mostrara todos los numeros 
    #primos dentro de este rango 
    print(f"\nLos números primos entre {rango_inicial} y {rango_final} son:")
    for numero in range(rango_inicial, rango_final + 1): # Recorremos cada número en el rango
        if numero > 1: # Los números menores o iguales a 1 no son primos
            es_primo = True # En este caso si el numero es primo lo colocamos como verdadero, es decir que continua el recorrido del programa 
            for i in range(2, int(numero**0.5) + 1): # En este caso sabemos que un numero primo es divisible por 1 y por si mismo
                if numero % i == 0:
                    es_primo = False ##Si tiene un divisor ademas de si mismo no es un numero primo, por lo tanto esta secuencia lógica es falsa
                                     #porlo que el programa no puede continuar su ejecucion
                    break
            if es_primo:
                print(numero, end=" ") ##En caso de ser divisible para uno y para si mismo le decimos al programa que muestre el siguiente mensaje,
                                       #donde enseña el mensaje"Los numeros primos entre 10 y 20 son %%%%%")
