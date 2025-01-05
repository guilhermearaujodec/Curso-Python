import os

restaurantes = [{'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False},
                {'nome': 'Pizza Suprema', 'categoria': 'Pizza', 'ativo': True},
                {'nome': 'Cantina', 'categoria': 'Italiana', 'ativo': False}]

def exibir_nome_do_programa():
    """
    Exibe o nome do programa no console em um formato estilizado.
    
    Inputs: Nenhum
    Outputs: Nenhum
    """
    print("""
      
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")

def exibir_opcoes():
    """
    Exibe as opções do menu principal para o usuário.

    Inputs: Nenhum
    Outputs: Nenhum
    """
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Alternar o Estado do Restaurante')
    print('4. Sair\n')

def finalizar_app():
    """
    Finaliza o aplicativo exibindo uma mensagem de encerramento.

    Inputs: Nenhum
    Outputs: Nenhum
    """
    exibir_subtitulo('Finalizando o app')
    
def voltar_ao_menu_principal():
    """
    Solicita ao usuário pressionar ENTER para voltar ao menu principal.

    Inputs: Nenhum
    Outputs: Nenhum
    """
    input('\nDigite ENTER para voltar ao menu principal!')
    main()

def opcao_invalida():
    """
    Informa o usuário que uma opção inválida foi escolhida e retorna ao menu principal.

    Inputs: Nenhum
    Outputs: Nenhum
    """
    print('Opção Inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    """
    Exibe um texto no formato de subtítulo.

    Inputs:
        texto (str): O texto a ser exibido como subtítulo.

    Outputs: Nenhum
    """
    os.system('cls')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    """
    Cadastra um novo restaurante na lista global de restaurantes.

    Inputs:
        nome_do_restaurante (str): Nome do restaurante fornecido pelo usuário.
        categoria (str): Categoria do restaurante fornecida pelo usuário.

    Outputs: Nenhum
    """
    exibir_subtitulo('Cadastro de novos restaurantes...')
    nome_do_restaurante = str(input('Insira o nome do restaurante que deseja cadastrar: '))
    categoria = str(input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: '))
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    """
    Lista todos os restaurantes da lista global no console.

    Inputs: Nenhum
    Outputs: Nenhum
    """
    exibir_subtitulo('Listando os restaurantes...')
    print(f'{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | Status\n')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    """
    Altera o estado (ativo/desativado) de um restaurante específico.

    Inputs:
        nome_restaurante (str): Nome do restaurante fornecido pelo usuário.

    Outputs: Nenhum
    """
    exibir_subtitulo('Alterando estado do restaurante...')
    nome_restaurante = str(input('Digite o nome do restaurante que deseja alterar o estado: '))
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = (f'O restaurante {nome_restaurante} foi ativado com sucesso' 
                        if restaurante['ativo'] else 
                        f'O restaurante {nome_restaurante} foi desativado com sucesso')
            print(mensagem)
    if not restaurante_encontrado:
        print(f'O restaurante {nome_restaurante} não foi encontrado.')
    
    voltar_ao_menu_principal()

def escolher_opcao():
    """
    Solicita ao usuário uma opção no menu e executa a função correspondente.

    Inputs:
        opcao_escolhida (int): Opção numérica fornecida pelo usuário.

    Outputs: Nenhum
    """
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alternar_estado_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except ValueError:
        opcao_invalida()

def main():
    """
    Inicializa o aplicativo exibindo o nome do programa e as opções do menu principal.

    Inputs: Nenhum
    Outputs: Nenhum
    """
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()