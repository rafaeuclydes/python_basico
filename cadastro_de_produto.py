
#Início da função cadastrar produto
def cadastrar_produto():
    print('Menu de cadastro de produtos')
    nome = input('Digite o nome do produto: ')
    descricao = input('Qal a descrição do produto: ')
    valor = float(input('Valor do produto: R$ '))
    disponibilidade = input('Disponível para venda (S/N): ')

#Final da função cadastrar produto

#Programa principal
while True:
    menu_principal = input('\nEscolha a opção desejada:\n' +
                           '1 - Cadastrar produto\n'+
                           '2 - Sair\n'+
                           '>> ')

    if menu_principal == '1':
        cadastrar_produto()
    else:
        print('Encerrando o programa...')
        break
