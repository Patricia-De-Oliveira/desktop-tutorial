velocidade = float(input('Qual é a velocidade do carro? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Você foi multado! O valor da multa é R${multa:.2f}.')
print('Tenha um bom dia! Continue dirigindo com segurança!')
