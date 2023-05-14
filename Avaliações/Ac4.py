#Pague o aluguel

divida = int(input())
pagamento = int(input())

count_pagamento = 0

while divida > 0:
    count_pagamento += 1
    divida_anterior = divida
    divida -= pagamento

    if divida < 0:
        divida = 0
    print(f'pagamento: {count_pagamento}')
    print(f'antes = {divida_anterior}')
    print(f'depois = {divida}')
    print(f'-----')


#Exibindo tabuadas

n1 = int(input())
n2 = int(input())

intervalo = n1

if n1 <= n2:
    while intervalo <= n2:

        for i in range (1, 11):
            tabuada = intervalo * i
            print(f'{intervalo} x {i} = {tabuada}')
        print('----------')
        intervalo += 1
else:
    print('Nenhuma tabuada no intervalo!')


#Intervalo de primos!

def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

inicio = int(input())
fim = int(input())

quantidade_primos = 0
primos = []

for num in range (inicio, fim + 1):
    if eh_primo(num):
        quantidade_primos += 1
        primos.append(num)

for primo in primos:
    print(primo)

print(f'primos: {quantidade_primos}')


#Corra forest!

tempos = []
while True:
    tempo = int(input())
    if tempo < 0:
        break
    tempos.append(tempo)

media = sum(tempos) / len(tempos)

print('MEDIA: {:.2f}'.format(media))

for tempo in tempos:
    if tempo < media:
        print(tempo)