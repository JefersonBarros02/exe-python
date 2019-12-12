celular = str(input('Digite seu número de celular (sem código de país, separação ou DDD): ')).strip()
if celular[0] not in '9' or len(celular) != 9:
    while celular[0] not in '9' or len(celular) != 9:
        celular = str(input('Número incorreto, tente novamente: ')).strip()
print('Número cadastrado com sucesso!')
