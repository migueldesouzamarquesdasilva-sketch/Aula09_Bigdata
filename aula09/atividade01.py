lista_contato = []

for i in range(3):
    print(f'\ncontato {i+1}')

    contato = {}

    contato['nome'] = input('Informe o nome completo: ')
    contato['telefone'] = int(input('Informe seu telefone (apenas números): '))
    contato['e-mail'] = input('Informe o seu e-mail: ')

    lista_contato.append(contato)

#print(lista_contato)

for elemento in lista_contato:  
    print(f'Nome: \n{elemento['nome']}')
    print(f'Telefone: {elemento['telefone']}')
    print(f'E-mail: {elemento['e-mail']}')




