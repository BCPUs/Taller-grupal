#Serie de Fibonacci

limite = int(input("Ingrese el número limite: "))

num1 = 0
num2 = 1
num3 = 0
sumatoria = 0

while (num1 <= limite):

    print(num1)
    num3 = num1
    num1 = num2
    num2 = num3 + num2
    sumatoria += num3

print("La sumatoria de la serie de fibonacci es: ", sumatoria)  