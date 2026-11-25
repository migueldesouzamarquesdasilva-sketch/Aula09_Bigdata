produto1 = {} # Dicionário vazio

produto = {
    'nome': 'Notebook',
    'preco': 3500.80,
    'marca': 'Lenovo'
}
# type(produto)
print(produto) # todas as chaves e valores

print(produto['nome']) # chave nome
print(produto['preco']) # chave preco

# Alterando o valor
produto['marca'] = 'Positivo'
print(produto['marca']) 

# Adcionando Chaves
produto['tela'] = '18"'
#print(produto)

# Deletando uma chave

del produto['marca']
print(produto)

print(produto.keys()) # Chaves
print(produto.values()) # Valores
print(produto.items())
