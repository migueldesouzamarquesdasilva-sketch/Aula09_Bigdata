lista_catalogo = []


for i in range(3):
    print(f'\nLivro {i+1}')
    
    livro = {}

    livro['titulo'] = input('Informe o nome do livro: ')
    livro['autor'] = input('Informe o nome do autor: ')
    livro['ano'] = int(input('Informe o ano de lançamento: '))
    livro['genero'] = input('Informe o gênero: ')
    livro['paginas'] = int(input('Informe o número de páginas: '))

    lista_catalogo.append(livro)

#print(lista_catalogo)

for elemento in lista_catalogo:  # 3 vezes
    #print(elemento)
    if elemento['ano'] >= 2020:
        print(f'Nome: {elemento['titulo']}')
        print(f'Ano: {elemento['ano']}')





