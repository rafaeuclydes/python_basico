# Você e sua equipe de programadores foram contratados por pequena
# empresa para desenvolver o software de gerencialme de pessoas. Este
# software deve ter o seguinte menu e opções:
#
# 1)	Cadastrar Colaborador
# 2)	Consultar Colaborador
#   1.	Consultar Todos
#   2.	Consultar por Id;
#   3.	Consultar por Setor;
#   4.	Retornar ao menu;
# 3)	Remover Colaborador
# 4)	Encerrar Programa

#--------------------Início das Variáveis Globais#--------------------#
lista_colaboradores = []
id_global = 0
#--------------------Fim das Variáveis Globais#--------------------#

# Inicio função cadastrar_colaborador(id) #
def cadastrar_colaborador(id): # função que cadastro um colaborador
    print('Menu de cadastramento de colaboradores')
    print('ID do colaborador: {}' .format(id))
    nome = input('Digite o nome do colaborador (a): ')
    setor = input('Digite o setor do colaborador (a): ')
    salario = float(input('Digite o valor do salário: R$ '))
    dados_dicionario = {'id'      : id, # formato chave - valor de dicionários
                        'nome'    : nome,
                        'setor'   : setor,
                        'salario' : salario}
    lista_colaboradores.append(dados_dicionario.copy()) # o append coloca o dicionario dentro da lista e o copy copia os dados do dicionario criado acima na lista
# Fim da função cadastrar_colaborador(id) #

# Inicio função consultar_colaborador() #
def consultar_colaborador(): # função para consultar outras opções detro de consultar colaborador
    print('Menu de consulta de colaboradores')
    while True:
        menu_consulta = input('1 - Consultar Todos \n' +
                              '2 - Consultar por Id\n' +
                              '3 - Consultar por Setor\n' +
                              '4 - Retornar ao menu\n' +
                              '>> ')
        if menu_consulta == '1':
            print('Você selecionou a opção Colsultar Todos')
            for colaborador in lista_colaboradores: # criei a variável colaborador p/ varrer a lista lista_colaborador
                print('----------------------------------------')
                for key, value in colaborador.items(): # como dicionarios são formados por chave: valor, coloquei em inglês key e value assim o for vai varrer cada item do dicionário
                    print('{}: {}' .format(key, value)) # vai printar cada conjunto chave: valor de cada colaborador
                print('----------------------------------------')
        elif menu_consulta == '2':
            print('Você selecionou a opção Colsultar por Id')
            consulta_id = int(input('Digite o Id do colaborador (a): '))
            for colaborador in lista_colaboradores:
                if colaborador ['id'] == consulta_id: #o valor do campo id do dicionário é igual ao valor do id desejado
                    print('----------------------------------------') # o if selecionou o que quero procurar, nesse cado o ID
                    for key, value in colaborador.items():  # como dicionarios são formados por chave: valor, coloquei em inglês key e value assim o for vai varrer cada item do dicionário
                        print('{}: {}'.format(key, value))  # vai printar cada conjunto chave: valor de cada colaborador
                print('----------------------------------------')
        elif menu_consulta == '3':
            print('Você selecionou a Consultar por Setor')
            consulta_setor = input('Digite o setor do colaborador (a): ')
            for colaborador in lista_colaboradores: # varre toda a lista de colaboradores
                if colaborador['setor'] == consulta_setor:  # o valor do campo id do dicionário é igual ao valor do id desejado
                    print('----------------------------------------')  # o if selecionou o que quero procurar, nesse cado o ID
                    for key, value in colaborador.items():  # como dicionarios são formados por chave: valor, coloquei em inglês key e value assim o for vai varrer cada item do dicionário
                        print('{}: {}'.format(key, value))  # vai printar cada conjunto chave: valor de cada colaborador
                print('----------------------------------------')
        elif menu_consulta == '4':
            return # aqui sai da função consultar colaborador e cai no laço global do menu principal
        else:
            print('Opção inválida. Tente novamente')
            continue  # volta para o inicio do laço
# Fim da função consultar_colaborador() #

# Inicio função remover_colaborador() #
def remover_colaborador(): # função para remover item/colaborador de uma lista
    print('Menu de remoção de colaboradores')
    remover = int(input('Digite o Id do colaborador que deseja remover: '))
    for deletar in lista_colaboradores: # varre toda a lista de colaboradores e remove a opção seleionada
        if deletar['id'] == remover:
            lista_colaboradores.remove(deletar) # vai remover da lista o id selecionado
            print('Colaborador (a) removido')
# Fim da função remover_colaborador() #

# Programa principal #
print('Bem vindo ao software de gerenciamento de pessoas de Rafael Euclydes dos Santos')
while True: # laço 'infinito para o usuário usar ou errar quantas vezes quiser
    menu_principal = input('\nEscolha a opção desejada:\n' +
                           '1 - Cadastrar Colaborador\n' +
                           '2 - Consultar Colaborador\n' +
                           '3 - Remover Colaborador\n' +
                           '4 - Encerrar Programa\n' +
                           '>> ')
    if menu_principal == '1':
        id_global = id_global + 1 # variável acumuladora
        cadastrar_colaborador(id_global)
    elif menu_principal == '2':
        consultar_colaborador()
    elif menu_principal == "3":
        remover_colaborador()
    elif menu_principal == '4': # encerra o programa
        break # encerra o laço
    else:
        print('Opção inválida. Tente novamente')
        continue # volta para o inicio do laço
print('Encerrando o programa...')


