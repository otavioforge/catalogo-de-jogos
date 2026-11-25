#Programa: Catálogo de Jogos
#Feito por: João Otávio R. Brandão
#Data: 23/11/26
import time
catalogo = [

{
    'nome': 'GTA San Andreas',
    'genero': 'Ação',
    'plataforma': 'Playstation 2',
    'ano': 2004,
    'nota': 9.5
},

{
    'nome': 'Minecraft',
    'genero': 'Sandbox',
    'plataforma': 'PC',
    'ano': 2011,
    'nota': 10
},

{
    'nome': 'The Witcher 3',
    'genero': 'RPG',
    'plataforma': 'Playstation 4',
    'ano': 2015,
    'nota': 9.5
},

{
    'nome': 'Terraria',
    'genero': 'Aventura',
    'plataforma': 'PC',
    'ano': 2011,
    'nota': 9
},

{
    'nome': 'Resident Evil 4',
    'genero': 'Terror',
    'plataforma': 'Playstation 2',
    'ano': 2005,
    'nota': 9
},
]

#Primeira Função: Cadastrar Jogo
def cadastrar_jogo():
    nome = input("Digite o nome do jogo: ")
    genero = input("Digite o nome do gênero desse jogo: ")
    plataforma = input("Digite (apenas uma) plataforma que suporta esse jogo: ")
    ano = int(input("Digite o ano em que esse jogo foi lançado: "))
    nota = float(input("Digite a nota desse jogo: "))

    jogo = {
        'nome': nome,
        'genero': genero,
        'plataforma': plataforma,
        'ano': ano,
        'nota': nota
    }

    catalogo.append(jogo)

    print("Jogo cadastrado com sucesso!")

#Segunda Função: Listar Jogos
def listar_jogos():
    for jogo in catalogo:
        print('\n-------------------------')
        print('Nome:', jogo['nome'])
        print('Gênero:', jogo['genero'])
        print('Plataforma:', jogo['plataforma'])
        print('Ano:', jogo['ano'])
        print('Nota:', jogo['nota'])
        print('-------------------------')

#Terceira Função: Remover Jogos
def remover_jogo():
    nome = input("Digite o nome do jogo que você deseja remover: ")

    for jogo in catalogo:
        if jogo['nome'].lower() == nome.lower():
            catalogo.remove(jogo)
            print("Jogo removido com sucesso!")
            return
    print("Jogo não encontrado.")

#Quarta Função: Menu
def menu():
    while True:
        print("\n===== CATÁLOGO DE JOGOS =====")
        print("1 - Listar Jogos")
        print("2 - Cadastrar Jogo")
        print("3 - Remover jogo")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            listar_jogos()
        elif opcao == '2':
            cadastrar_jogo()
        elif opcao == '3':
            remover_jogo()
        elif opcao == '4':
            print("Saindo do Programa", end="")

            for i in range(3):
                time.sleep(1)
                print(".", end="", flush=True)

            print("\nPrograma encerrado!")
            break

        else: print("Opção escolhida inválida. Tente Novamente.")

menu()