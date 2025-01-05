def exercicio1():
    """
    1 - Crie uma lista para cada informação a seguir:

    Lista de números de 1 a 10;
    Lista com quatro nomes;
    Lista com o ano que você nasceu e o ano atual.
    """
    
    lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    lista_nomes = ['João', 'Maria', 'Ricardo', 'Jonas']
    lista_nascimento = [2024, 2025]

    print(lista_numeros)
    print(lista_nomes)
    print(lista_nascimento)
    
# exercicio1()

def exercicio2():
    """ 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista. """
    
    lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    for n in lista_numeros:
        print(n)

# exercicio2()

def exercicio3():
    """ 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10. """
    
    soma = 0
    
    for n in range(11):
        if n % 2 != 0:
            print(n)
            soma += n
    print(soma)
    
# exercicio3()

def exercicio4():
    """ 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente. """
    
    for n in range(10, 0, -1):
        print(n)
        
# exercicio4()

def exercicio5():
    """ 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10. """
    
    tabuada = []
    
    numero = int(input('Insira um número: '))
    
    for n in range (1, 11):
        tabuada.append(f'{numero} x {n} = {numero * n}')
        
    for i in tabuada:
        print(i)

# exercicio5()

def exercicio6():
    """ 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções. """
    
    lista_numeros = [10, 5, 8, 3, 7]
    soma = 0
    
    try:
        for numero in lista_numeros:
            soma += numero
        print(f'Soma dos elementos: {soma}')
        
    except Exception as e:
        print('Ocorreu um erro: {e}')

# exercicio6()

def exercicio7():
    """ 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia. """
    
    lista_valores = [10, 15, 16, 17, 19, 45]
    soma = 0
    
    try:
        for valor in lista_valores:
            soma += valor
        media = soma / len(lista_valores)
        print(f'A média dos valores foi de: {media}')
        
    except ZeroDivisionError:
        print('A lista está vazia, não é possível calcular a média.')
        
    except Exception as e:
        print(f'Ocorreu um erro: {e}')