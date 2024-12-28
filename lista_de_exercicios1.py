"""
3 - Para imprimir a palavra ‘ALURA’ com cada letra em cada linha com a função print utilizando o parâmetro sep para especificar o separador entre os argumentos da seguinte forma:
"""

print('A','L','U','R','A',sep='\n')

"""
4 - Para imprimir o valor de pi arredondado, temos algumas possíveis abordagens:
"""

pi = 3.14159

# Abordagem de f-string
print(f'O valor arredondado de pi é: {pi:.2f}')

# Abordagem de .format()
print('O valor arredondado de pi é: {:.2f}'.format(pi))

# Utilizando a função round()
print('O valor arredondado de pi é:', round(pi, 2))