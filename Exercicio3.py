# Você foi contratado para desenvolver um sistema de cobrança de
# banho para um petshop. Você ficou com a parte de desenvolver a
# interface com o funcionário.
# O petshop opera da seguinte maneira:
# •	Para cães com peso menor que 3 kg o valor base é de 40 reais;
# •	Para cães com peso igual ou maior que 3 kg e menor que 10 kg o valor base é de 50 reais;
# •	Para cães com peso igual ou maior que 10 kg e menor que 30kg o valor base é de 60 reais;
# •	Para cães com peso igual ou maior que 30 kg e menor que 50kg o valor base é de 70 reais;
#
# 	Para cães com pelo curto (c) o multiplicador é 1;
# 	Para cães com pelo médio (m) o multiplicador é 1.5;
# 	Para cães com pelo longo (l) o multiplicador é 2;
#
# ♦	Para o adicional de cortar unhas (1) do cachorro é cobrado um valor extra de 10 reais;
# ♦	Para o adicional de escovar os dentes (2) do cachorro é cobrado um valor extra de 12 reais;
# ♦	Para o adicional de limpar as orelhas (3) do cachorro é cobrado um valor extra de 15 reais;
# ♦	Para o adicional de não querer mais nada (0) é cobrado um valor extra de 0 reais;
#
# O valor final da conta é calculado da seguinte maneira:
#
# total = base * multiplicador + extra

# Início da função cachorro_peso(): pergunta o peso do cachorro
def cachorro_peso(): #pergunta o peso do cachorro
    print('---------------------Menu 1 de 3---------------------')
    while True: # laço infinito o usuário pode errar infinitamente
        try: # tenta os if's e elif's abaixo e continua se estiver tudo verdadeiro com relação as condições de cada
            peso = int(input('Digite o peso do cachorro (kg): '))
            if peso < 3 and peso > 0:
                return 40.00 # Retorna o valor base com base no peso
            elif (peso >= 3) and (peso < 10): # Caso seja maior ou igual ao valor do intervalo vai indo de elif em elif pra atender ao intervalo
                return 50.00
            elif (peso >= 10) and (peso < 30):
                return 60.00
            elif (peso >= 30) and (peso < 50):
                return 70.00
            else: # caso o usuário digite outro valor fora do intervalo dos peso da tabela
                print('Favor digitar uma valor válido')
                continue
        except ValueError:  # caso o usuário digite uma letra ou número não inteiro
            print('Favor digitar um valor numérico')
# Final da função cachorro_peso

# Inicio da função cachorro_pelo(): pergunta o comprimento do pelo do cachorro
def cachorro_pelo(): # pergunta o tipo do pelo do cachorro
    print('---------------------Menu 2 de 3---------------------')
    while True: # laço infinito
        pelo = input('Como é o pelo do cachorro:\n' + # \n para quebra de linha e o mais é para deixa as strings uma embaixo da outra
                     'Curto(c)\n' +
                     'Médio (m)\n' +
                     'Longo (l)\n' +
                     '>> ') # o usuário irá digitar a opção aqui
        pelo = pelo.lower() # lower transforma as letras em minúscula caso o usuário digite 'c' ou 'C' por exemplo
        pelo = pelo.strip() # remove possíveis espaços que possa ter na resposta do usuário
        if pelo == 'c':
            return 1.00 # retorna o multiplicador de cada condição
        elif pelo == 'm':
            return 1.50
        elif pelo == 'l':
            return 2.00
        else: # casoo usuário digite algo diferentes das opções corretas
            print('Digite uma opção válida c, m ou l')
            continue # retorna para o início do laço
# Final da função cachorro_pelo()

# Início da função cachorro_extra(): pergunta se deseja adicionar algum serviço extra
def cachorro_extra(): # pergunta se deseja produto/serviço adicional
    print('---------------------Menu 3 de 3---------------------')
    acumulador = 0 # pra ter a opção de adicionar mais de um serviço e acumular os valores de cada serviço escolhido
    while True:
        extra = input('Adição de serviço extra:\n' +
                      '(0) Sem adicional \n' +
                      '(1) Cortar as unhas - 10,00 \n' +
                      '(2) Escovar os dentes - 12,00 \n' +
                      '(3) Limpar as orelhas - 15,00 \n' +
                      '>> ')
        if extra == '0':
            return acumulador # retorna o valor acumulado das escolhas
        elif extra == '1':
            acumulador = acumulador + 10
        elif extra == '2':
            acumulador = acumulador + 12
        elif extra == '3':
            acumulador = acumulador + 15
        else:
            print('Digite uma opção válida 0, 1, 2 ou 3')
#Final da função cachorro_extra()

# Programa principal
print("Sistema de cobrança de Rafael Euclydes dos Santos - Petshop fofinho. Seja bem vindo!")
base = cachorro_peso()
pelo = cachorro_pelo()
extra = cachorro_extra()
print('Total a ser pago: {:.2f}. \n' .format(base * pelo + extra) +
      'Peso: {:.2f} x Pelo {} + Extra {:.2f}'.format(base, pelo, extra)) # fórmula para calcular o total do peso/base, multiplicados e extra

