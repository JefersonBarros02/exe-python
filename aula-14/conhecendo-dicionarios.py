pessoa = {
    "nome": 'Matheus Alefe',
    "e-mail":'matheus.orvati@hotmail.com'
}
print(f'Olá {pessoa["nome"]}, esse é o seu e-mail: {pessoa["e-mail"]}')

pessoa.update({"Está trabalhando?": True})
print(pessoa)
