# Você e sua equipe de programadores foram contratados para desenvolver um app de
# vendas para uma sorveteria. Você ficou com a parte de desenvolver a interface do
# cliente para retirada do produto.
# A Sorveteria possui seguinte relação:
#
# •	1 bola de sorvete no sabor tradicional (tr) custa 6 reais, no sabor premium (pr)
# 7 reais e no especial (es) 8 reais;
# •	2 bolas de sorvete no sabor tradicional (tr) custam 11 reais, no sabor premium (pr)
# 13 reais e no especial (es) 15 reais;
# •	3 bolas de sorvete no sabor tradicional (tr) custam 15 reais, no sabor premium (pr)
# 18 reais e no especial (es) 21 reais;

print('                Sorveteria Rafael Euclydes dos Santos. Bem vindo!                ')
print('-------------------------------------Cardápio------------------------------------')
print('|Nº DE BOLAS | Sabor Tradicional (tr) | Sabor Premium (pr) | Sabor Especial (es)|')
print('|      1     |        R$ 6,00         |      R$ 7,00       |       R$ 8,00      |')
print('|      2     |        R$ 10,00        |      R$ 12,00      |      R$ 14,00      |')
print('|      3     |        R$ 14,00        |      R$ 17,00      |      R$ 20,00      |')
print('---------------------------------------------------------------------------------')
acumulador = 0 # variável acumulador p/ iniciar as somas a partir do zero
while True: # laço de repetição
    tipo = input('Escolha o tipo de sorvete (tr, pr ou es): ')
    if tipo != 'tr' and tipo != 'pr' and tipo != 'es':
        print('Sabor de Sorvete Inválido.')
        continue # caso seja digitado algum sabor de sorvete inválido volta ao início e pergunta novamente qual sabor
    bolas = int(input('Escolha quantas bolas deseja (1, 2 ou 3): '))
    if bolas != 1 and bolas != 2 and bolas != 3:
        print('Quantidade de Bolas de Sorvete Inválida.')
        continue # caso seja digitado algum valor inválido volta ao início e pergunta novamente qual sabor
    if tipo == 'tr' and bolas == 1: # o 'and' junta duas condições
        print('Você pediu 1 bola do sabor Tradicional R$: 6,00')
        acumulador = acumulador + 6 # pega o valor do acumulador inicial/atual e soma 6
    elif tipo == 'tr' and bolas == 2:
        print('Você pediu 2 bolas do sabor Tradicional R$: 10,00')
        acumulador = acumulador + 10 # pega o valor do acumulador inicial/atual e soma 10
    elif tipo == 'tr' and bolas == 3:
        print('Você pediu 3 bolas do sabor Tradicional R$: 14,00')
        acumulador = acumulador + 14 # pega o valor do acumulador inicial/atual e soma 14
    if tipo == 'pr' and bolas == 1:
        print('Você pediu 1 bola do sabor Tradicional R$: 7,00')
        acumulador = acumulador + 7 # pega o valor do acumulador inicial/atual e soma 7
    elif tipo == 'pr' and bolas == 2:
        print('Você pediu 2 bolas do sabor Tradicional R$: 12,00')
        acumulador = acumulador + 12 # pega o valor do acumulador inicial/atual e soma 12
    elif tipo == 'pr' and bolas == 3:
        print('Você pediu 3 bolas do sabor Tradicional R$: 17,00')
        acumulador = acumulador + 17 # pega o valor do acumulador inicial/atual e soma 17
    if tipo == 'es' and bolas == 1:
        print('Você pediu 1 bola do sabor Tradicional R$: 8,00')
        acumulador = acumulador + 8 # pega o valor do acumulador inicial/atual e soma 8
    elif tipo == 'es' and bolas == 2:
        print('Você pediu 2 bolas do sabor Tradicional R$: 14,00')
        acumulador = acumulador + 14 # pega o valor do acumulador inicial/atual e soma 14
    elif tipo == 'es' and bolas == 3:
        print('Você pediu 3 bolas do sabor Tradicional R$: 20,00')
        acumulador = acumulador + 20 # pega o valor do acumulador inicial/atual e soma 20

    pedir_mais = input('Deseja fazer mais algum pedido? (s / n): ')
    if pedir_mais == 's':
        continue # se for digitado 's' inicia o laço novamente (tipo = input('Escolha o tipo de sorvete (tr, pr ou es): ')
    else:
        print('Valor a ser pago: R$ {:.2f}' .format(acumulador)) # o :.2f deixa o somatório do valor a pagar com duas casa decimais
        break # se digitado 'n' encerra o laço, termina o programa printando o valor total a pagar e a mensagem de volte sempre
print('Obrigado. Volte sempre!')
