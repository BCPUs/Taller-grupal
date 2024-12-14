numero=int(input("Ingrese el numero decimal que desea convertir a octal\n"))
Octal=""
while numero > 0:
    Octal=str(numero % 8)+Octal
    numero= numero//8
print ("El numero octal correspondiente al numero decimal ingresado es :", Octal) 

