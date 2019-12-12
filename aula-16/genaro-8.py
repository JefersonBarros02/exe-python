from math import pi, pow
def calc_area(raio):
    return pow(raio, 2)*pi

raio = float(input('Insira o raio do cículo: '))
print(f'A área do c´iculo de raio {raio} vale {calc_area(raio):.2f}')
