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


#