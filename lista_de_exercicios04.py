def exercicio1():
    """1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade."""
    
    cadastro = {'nome':'Jonathan', 'idade':47, 'cidade':'Caraguatatuba'}
    print(cadastro)

# exercicio1()

def exercicio2():
    """
    2 - Utilizando o dicionário criado no item 1:

    Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
    Adicione um campo de profissão para essa pessoa;
    Remova um item do dicionário.
    """
    
    cadastro = {'nome':'Jonathan', 'idade':47, 'cidade':'Caraguatatuba'}
    print(cadastro)
    novo_nome = str(input('Insira um nome: '))
    cadastro['nome'] = novo_nome
    print(f'{'Nome atualizado para ' + novo_nome if cadastro['nome'] == novo_nome else 'Nenhuma atualização realizada'}')
    
    cadastro['profissão'] = 'Engenheiro de Software'
    del cadastro['cidade']
    print(cadastro)
    
# exercicio2()

def exercicio3():
    """3 - Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5."""
    
    numeros_quadrados = {x:x**2 for x in range(1,6)}
    print(numeros_quadrados)

exercicio3()

def exercicio4():
    """4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário."""
    
    cadastro = {'nome':'Jonathan', 'idade':47, 'cidade':'Caraguatatuba'}
    if 'nome' in cadastro:
        print("A chave 'nome' existe no dicionário.")
    else:
        print("'A chave 'nome' não existe no dicionário.")

# exercicio4()

def exercicio5():
    """5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário."""
    
    frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
    contagem_palavras = {}
    palavras = frase.split()
    print(palavras)
    for palavra in palavras:
        contagem_palavras[palavra] = contagem_palavras.get(palavra,0) + 1 
    print(contagem_palavras)

# exercicio5()