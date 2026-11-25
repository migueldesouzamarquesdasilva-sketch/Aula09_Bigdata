def dobro(x):
    r = x * 2
    return r

def triplo(y):
    t = y * 3
    return t

def quadrado(p):
    q = p **2
    return q

valor = float(input('Digite um valor: '))
resultado = dobro(valor)
resultado02 = triplo(valor)
resultado03 = quadrado(valor)


print(f'O dobro desse número é: {resultado} ')
print(f'O triplo desse número é: {resultado02} ')
print(f'O quadrado desse número é: {resultado03}')