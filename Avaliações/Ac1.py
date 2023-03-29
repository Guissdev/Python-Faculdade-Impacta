valor_unitario = float(input('Entre com o valor unitário do produto: '))
quantidade = int(input('Entre com a quantidade: '))

if quantidade > 40:
    print("Desculpe, não é possível comprar mais de 40 unidades.")
else:
    valor_total = valor_unitario * quantidade
    porcentagem_adicional = 0.10 + (0.01 * quantidade)
    desconto = valor_total * porcentagem_adicional
    valor_final = valor_total - desconto
    
print (f'O valor total é de: {valor_total:.2f}')
print (f'O valor com desconto é de: {valor_final:.2f}')