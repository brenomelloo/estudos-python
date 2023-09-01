
#Faça um programa que peça dois números inteiros. Imprima a soma desses dois números na tela.

def restart_program():
    pass

n1 = input('Digite seu primeiro número: ')
n2 = input('Digite seu segundo número: ')

if n1.isnumeric() and n2.isnumeric():
    n1 = int(n1)
    n2 = int(n2)
    soma = n1 + n2
    print(f'A soma de seus números é {soma}')
else:
    print('Só são aceitos números!')
    restart_program()
