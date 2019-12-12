funcionario = {
    'Nome': input('Nome do funcionário: '),
    'Hora de trabalho': float(input('Valor da hora de trabalho: R$')),
    'Horas Trabalhadas': float(input('Horas trabalhadas: '))
}
print(f"Salário de {funcionario['Nome']}: R${funcionario['Hora de trabalho'] * funcionario['Horas Trabalhadas']:.2f}")
