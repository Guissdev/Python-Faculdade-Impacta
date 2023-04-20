#Atividade contínua 2
#Data de realização 29/03/2023

#Jogo do par ou ímpar
while True:
    num = int(input('Entre com um numero maior ou igual a dois: '))
    
    if num >= 2:
    
        if num % 2 == 0:
            impar_anterior = num - 1
            par_posterior = num + 2

            print(f'{impar_anterior} {par_posterior}')
            break
        else:
            impar_anterior = num - 2
            par_posterior = num + 1

            print(f'{impar_anterior} {par_posterior}')
            break
    else:
        print('O numero digitado não é maior ou igual a dois')


#Professor, mas é só 0.5
while True:
    trabalhos = float(input('Entre com a nota dos trabalhos de 0 a 10: '))
    prova = float(input('Entre com a nota da prova de 0 a 10: '))

    if 0 <= trabalhos <= 10 and 0 <= prova <= 10:
        media = (trabalhos + prova) / 2
        if media >= 6:
            print('aprovado')
            break
        else:
            if 2 > trabalhos:
                print('reprovado')
                break
            else:
                print('talvez com a sub')
                break
    else:
        print('Valor inválido')


#Dia da entrega
dia_da_semana = {'domingo': 0, 'segunda': 1, 'terca': 2, 'quarta': 3, 'quinta': 4, 'sexta': 5, 'sabado': 6}
dia_compra = input('Digite o dia da semana em que a compra foi realizada: ').lower()
dias_entrega = int(input('Digite a quantidade de dias para a entrega: '))

if dias_entrega == 0:
    print('chega hoje!')
else:
    numero_dia_compra = dia_da_semana[dia_compra]
    numero_dia_entrega = (numero_dia_compra + dias_entrega) % 7

    dia_entrega = list(dia_da_semana.keys())[list(dia_da_semana.values()).index(numero_dia_entrega)]

    print('sera entregue', dia_entrega)
