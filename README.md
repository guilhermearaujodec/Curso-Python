

Restaurant Manager Readme
Gerenciador de Restaurantes ✨
Bem-vindo ao Gerenciador de Restaurantes! Este é um programa interativo feito em Python que permite cadastrar, listar e gerenciar o estado de restaurantes em uma lista.

Funcionalidades 🌟
Cadastrar Restaurante

Adicione novos restaurantes com nome e categoria. Os restaurantes são automaticamente desativados ao serem adicionados.

Listar Restaurantes

Visualize todos os restaurantes cadastrados, incluindo nome, categoria e status (Ativado ou Desativado).

Alternar Estado do Restaurante

Ative ou desative restaurantes já cadastrados.

Sair

Encerre o programa com uma mensagem estilizada.

Tecnologias Utilizadas 🛠️
Linguagem: Python 3.x

Módulo: os para limpar a tela e melhorar a experiência do usuário.

Como usar 🔧
Clone ou baixe o projeto.

Execute o arquivo Python:

python nome_do_arquivo.py
Navegue pelas opções do menu interativo digitando o número correspondente. 🔊

Estrutura do Programa 🔄
exibir_nome_do_programa()

Exibe o nome estilizado do programa no console.

exibir_opcoes()

Exibe o menu principal com as opções disponíveis.

cadastrar_novo_restaurante()

Solicita ao usuário o nome e a categoria de um restaurante e o adiciona à lista global restaurantes.

listar_restaurantes()

Mostra todos os restaurantes cadastrados, com suas informações alinhadas em colunas.

alternar_estado_restaurante()

Permite ao usuário alterar o estado (ativo/desativado) de um restaurante pelo nome.

escolher_opcao()

Solicita ao usuário uma opção do menu e executa a função correspondente usando match-case.

voltar_ao_menu_principal()

Aguarda o pressionamento da tecla ENTER para retornar ao menu principal.

finalizar_app()

Exibe uma mensagem ao encerrar o programa.

Exemplos de Uso 🔍
1. Cadastro de Restaurante
Insira o nome do restaurante que deseja cadastrar: Sushi Place
Digite o nome da categoria do restaurante Sushi Place: Japonesa
O restaurante Sushi Place foi cadastrado com sucesso!
2. Listar Restaurantes
Listando os restaurantes...
Nome do restaurante      | Categoria            | Status
- Pizza Suprema          | Pizza                | Ativado
- Sushi Place            | Japonesa            | Desativado
3. Alternar Estado
Digite o nome do restaurante que deseja alterar o estado: Sushi Place
O restaurante Sushi Place foi ativado com sucesso.
Personalização 🎨
Para alterar o conjunto inicial de restaurantes, edite a lista restaurantes:

restaurantes = [
    {'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False},
    {'nome': 'Pizza Suprema', 'categoria': 'Pizza', 'ativo': True},
    {'nome': 'Cantina', 'categoria': 'Italiana', 'ativo': False}
]
Requisitos 🚀
Python 3.6 ou superior

Terminal ou prompt de comando

Melhorias Futuras 🔄
Adicionar persistência de dados em um arquivo.

Implementar buscas por categoria.

Criar uma interface gráfica.

Contribuições ✨
Sinta-se à vontade para enviar melhorias ou sugerir funções adicionais. Basta realizar um fork do repositório e abrir um pull request. 🔁

Criado com ❤️ e Python!

# Site para strings estilizadas
https://fsymbols.com/
