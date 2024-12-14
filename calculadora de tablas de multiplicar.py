#tabla de multiplicar
print("Biernvenido a este programa")
numero= int(input("Ingrese un numero para empezar: ")) 
rango_inicial= int(input("Ingrese el rango inicial: ")) 
rango_final= int(input("Ingrese el rango final: ")) 

if rango_final>=rango_inicial:
    print ("el rango inicial no puede ser mayor al rango final")
else:
    print(f"tabla de multiplicar del {numero} desde {rango_inicial} hasta {rango_final}")
    for i in range(rango_inicial,rango_final +1):
        print(f"{numero}x{i}={numero*i}")


