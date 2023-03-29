#Avaliação 2 
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