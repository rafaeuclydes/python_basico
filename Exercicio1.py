# Enunciado: Imagina-se que você é um dos programadores responsáveis pela
# construção de app de vendas para uma determinada empresa X que vende em
# atacado. Uma das estratégias de vendas dessa empresa X é dar desconto
# maiores por unidade as informações abaixo:
# •	Se quantidade for menor que 200 o desconto será de 0%;
# •	Se quantidade for igual ou maior que 200 e menor que 1000 o desconto será de 5%;
# •	Se quantidade for igual ou maior que 1000 e menor que 2000 o desconto será de 10%;
# •	Se quantidade for igual ou maior que 2000 o desconto será de 15%;

print('Bom dia Rafael Euclydes, seja bem vindo.') # print de identificação
valor_unid = float(input('Qual o valor unitário da do produto: ')) # entrada dos valores do produto
# tipo float, porque os valores podem não ser inteiros
quantidade = int(input('Quantidade de produtos adquiridos: ')) # input de entrada da quantidade
# em formato int (inteiro)
if quantidade < 200: # essa quantidade não é aplicado desconto
    desconto = 0.00
elif quantidade >= 200 and quantidade < 1000: # aplicação de 5% de desconto
    desconto = 0.05
elif quantidade >= 1000 and quantidade < 2000: # aplicação de 10% de desconto
    desconto = 0.10
else: # aplicação de 15% de desconto
    desconto = 0.15

total_sem_desconto = valor_unid * quantidade # valores sem desconto
print('Valor a pagar SEM desconto: R$ {:.2f}' .format(total_sem_desconto))
total_com_desconto = total_sem_desconto - total_sem_desconto * desconto # valores com desconto
print('Valor a pagar COM desconto: R$ {:.2f}' .format(total_com_desconto))