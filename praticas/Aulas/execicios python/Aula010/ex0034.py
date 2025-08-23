salário = float(input('Digite o salário do funcionário: R$ '))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print(f'O salário do funcionário com aumento será de R$ {novo:.2f}')
