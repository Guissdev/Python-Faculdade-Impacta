#Treinamento 3

#Números ímpares

count_impar = 0

n = int(input())

for i in range (n):
    count_impar += 1

    if count_impar%2 != 0:
        print(count_impar)


#Soma de Impares Consecutivos I
x = int(input())
y = int(input())
impar = y

for y in range(x):
    impar += 1

    print(impar)