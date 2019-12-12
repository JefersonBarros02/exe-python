def par_impar(valor):
    if valor % 2 == 0:
        return 'par'
    else:
        return 'impar'


valor =[par_impar(int(input('Digite um valor: '))), par_impar(int(input('Digite um valor: ')))]
print(valor)
