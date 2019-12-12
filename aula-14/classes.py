class Carro:
    # Define-se a classe - modelo para os objetos pertencentes
    def __init__(self, proprietario, modelo, marca, preco, placa):
        # Inicia-se o metodo construtor "__init__", a referência "self" e os argumentos do metodo
        self.proprietario = proprietario
        self.modelo = modelo
        self.marca = marca
        self.preco = preco
        self.placa = placa

    def __str__(self):
        # Define o método __str__() que retornará uma string formatada de acordo com os dados do usuário
        return f'Olá {self.proprietario}, seu carro é um {self.modelo} - {self.marca} de placa {self.placa} avaliado' \
               f' em R${self.preco:.2f}'


meu_carro = Carro(
    proprietario='Matheus Alefe',
    modelo='Corsa',
    marca='Chevrolet',
    preco=9000,
    placa='CVR-3486'
)

print(meu_carro)
