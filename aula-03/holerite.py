salario = float(input('Entre com o seu salário: R$'))
inss = salario * 0.09
vale_transporte = salario * 0.03
plano_saude = 347 * 0.15
salario_liquido = salario - inss - vale_transporte - plano_saude
print(f'''Salário bruto: R${salario}
INSS: R${inss}
Vale transporte: R${vale_transporte}
Plano de saúde: R${plano_saude}
''', 50 * '-', f'''
Salário líquido: R${salario_liquido}''')
