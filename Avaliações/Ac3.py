#Atividade contínua 3
#Data da realização 19/04/2023

# Tabuada

n = int(input())

for i in range(1, 11):
    tabuada = n * i
    print(f'{n} x {i} = {tabuada}')

#######

# Triangulo alfabético

n = int(input())

for i in range(n):
    letra = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[i]
    linha = letra * (i + 1)
    print(linha)

#######

# Doação

total_reais = 0
total_vic_coin = 0

while True:
    vic_coin = float(input())
    if vic_coin != -1.0:
        conversao = vic_coin * 2.5

        total_reais += conversao
        total_vic_coin += vic_coin

    else:
        print(f'VC$ {total_vic_coin:.2f}')
        print(f'R$ {total_reais:.2f}')
        break

#######

# Anos Bissextos

inicio = int(input())
fim = int(input())
bissexto = 0

for i in range(inicio, fim + 1):
        if i % 4 == 0 and (i % 100 != 0 or i % 400 == 0):
            print(i)
            bissexto += 1

print(f'bissextos: {bissexto}')