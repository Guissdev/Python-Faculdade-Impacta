#Treinamento 2

# Múltiplos
a, b = input().split()
a = int(a)
b = int(b)

if a > b:
    if a % b == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')

if a < b:
    if b % a == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')
if a == b:
    print('Sao Multiplos')


#Mês
while True:
    mes = int(input('Entre com o numero de um mês de 1 a 12: '))

    if mes == 1:
        print('January')
        break
    elif mes == 2:
        print('February')
        break
    elif mes == 3:
        print('March')
        break
    elif mes == 4:
        print('April')
        break
    elif mes == 5:
        print('May')
        break
    elif mes == 6:
        print('June')
        break
    elif mes == 7:
        print('July')
        break
    elif mes == 8:
        print('August')
        break
    elif mes == 9:
        print('September')
        break
    elif mes == 10:
        print('October')
        break
    elif mes == 11:
        print('November')
        break
    elif mes == 12:
        print('December')
        break
    else:
        print('O numero digitado não corresponde a nenhum mês')


#Pares entre 5 números
cont_pares = 0  # variável para contar a quantidade de números pares

for i in range(5):
    num = int(input("Digite um número inteiro: "))
    if num % 2 == 0:
        cont_pares += 1

print(f"{cont_pares} valores pares.")


#Intervalo
numero = float(input())

if 0 <= numero <= 25:
    print('Intervalo [0,25]')
elif 25 < numero <= 50:
    print('Intervalo (25,50]')
elif 50 < numero <= 75:
    print('Intervalo (50,75]')
elif 75 < numero <= 100:
    print('Intervalo (75,100]')
else:
    print('Fora de intervalo')


#Animal teste1

animal = input('O animal é vertebrado ou invertebrado? ')

if animal == 'vertebrado':
    vertebrado = input('O animal é ave ou mamifero? ')
    if vertebrado == 'ave':
        ave = input('A ave é carnivoro ou onivoro? ')
        if ave == 'carnivoro':
            print('aguia')
        else:
            ave == 'onivoro'
            print('pomba')
    else:
        vertebrado == 'mamifero'
        mamifero = input('O mamifero é onivoro ou herbivoro? ')
        if mamifero == 'onivoro':
            print('homem')
        else:
            mamifero == 'herbivoro'
            print('vaca')
else:
    animal == 'invertebrado'
    invertebrado = input('O animal é inseto ou anelideo? ')
    if invertebrado == 'inseto':
        inseto = input('O inseto é hematofago ou herbivoro? ')
        if inseto == 'hematofago':
            print('pulga')
        else:
            inseto == 'herbivoro'
            print('lagarta')
    else:
        invertebrado == 'anelideo'
        anelidio = input('O anelideo é hematofago ou onivoro? ')
        if anelidio == 'hematofago':
            print('sanguessuga')
        else:
            anelidio == 'onivoro'
            print('minhoca')


#Animal teste2
tipo1 = input()
tipo2 = input()
tipo3 = input()

if tipo1 == 'vertebrado' and tipo2 == 'ave' and tipo3 == 'carnivoro':
    print('aguia')
elif tipo1 == 'vertebrado' and tipo2 == 'ave' and tipo3 == 'onivoro':
    print('pomba')
elif tipo1 == 'vertebrado' and tipo2 == 'mamifero' and tipo3 == 'onivoro':
    print('homem')
elif tipo1 == 'vertebrado' and tipo2 == 'mamifero' and tipo3 == 'herbivoro':
    print('vaca')
elif tipo1 == 'invertebrado' and tipo2 == 'inseto' and tipo3 == 'hematofago':
    print('pulga')
elif tipo1 == 'invertebrado' and tipo2 == 'inseto' and tipo3 == 'herbivoro':
    print('lagarta')
elif tipo1 == 'invertebrado' and tipo2 == 'anelideo' and tipo3 == 'hematofago':
    print('sanguessuga')
elif tipo1 == 'invertebrado' and tipo2 == 'anelideo' and tipo3 == 'onivoro':
    print('minhoca')


#Média 3
n1, n2, n3, n4 = map(float, input().split())

media = (n1*2 + n2*3 + n3*4 + n4*1) / 10

print(f"Media: {media:.1f}")

if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    nota_exame = float(input())
    media_final = (media + nota_exame) / 2
    print(f"Nota do exame: {nota_exame:.1f}")
    print("Aluno aprovado." if media_final >= 5.0 else "Aluno reprovado.")
    print(f"Media final: {media_final:.1f}")
