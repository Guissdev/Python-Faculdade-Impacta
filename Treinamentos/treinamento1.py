#Treinamento 1 

#salário com bônus
nome = input()
salario = float(input())
vendas = float(input())

comissao = vendas * 0.15

total = comissao + salario

print(f'TOTAL = R$ {total:.2f}')


#Área
a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

triangulo = (a*c) / 2
circulo = (c*c) * 3.14159
trapezio = (a+b) * c/2
quadrado = b*b
retangulo = a*b

print(f'TRIANGULO: {triangulo:.3f}')
print(f'CIRCULO: {circulo:.3f}')
print(f'TRAPEZIO: {trapezio:.3f}')
print(f'QUADRADO: {quadrado:.3f}')
print(f'RETANGULO: {retangulo:.3f}')


#Distancia entre dois pontos
x1, y1 = input().split()
x1 = float(x1)
y1 = float(y1)

x2, y2 = input().split()
x2 = float(x2)
y2 = float(y2)

distancia = (((x2 - x1) ** 2) + (y2 -y1) ** 2) **0.5
print (f'{distancia:.4f}')