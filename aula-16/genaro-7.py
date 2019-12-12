notas = []
soma = 0
contador = 0
numero_notas = int(input('Diga o número de notas: '))
while contador < numero_notas:
	contador += 1
	notas += [float(input(f'Insira a {contador}ª nota: '))]
len_notas = len(notas) - 1
print(f'A maior nota foi {max(notas)}')
