'''#Números ímpares
count_impar = 0

n = int(input())

for i in range (n):
    count_impar += 1
    if count_impar%2 != 0:
        print(count_impar)


#Soma de Impares Consecutivos I
x = int(input())
y = int(input())

menor = x 
maior = y

if x > y:
    maior = x
    menor = y

menor += 1
soma = 0 

while menor < maior:
    if menor % 2 != 0:
        soma += menor
    menor += 1
print(soma)


#Quadrado de Pares
n = int(input())

for i in range(2, n + 1):
    if i % 2 == 0:
        resultado = i * i
        print(f'{i}^2 = {resultado}')


#Idades
count_media = 0
total = 0
while True:
    idade = int(input())
    if idade >= 0:
        total += idade
        count_media += 1
    else:
        break

media = total / count_media
print(f'{media:.2f}')


#Fatorial simples
num = int(input())
fatorial = 1

for i in range(1, num + 1):
    fatorial *= i

print(fatorial)'''


#Maior e posição
maior = 0
posi = 0

for i in range (1, 10):
    num = int(input())
    if num > maior:
        maior = num
        posi = i

print(maior)
print(posi)