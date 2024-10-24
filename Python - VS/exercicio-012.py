
dias = int(input('Quantos dias foi alugado o veículo :'))
kmrodados = float(input('Quantos km rodados :'))

""" aluguel : 25R$ por dia """
""" km 1R$"""

somadiaria = dias * 60
kmresult = kmrodados * 0.15

print('{} dias alugados e {}Km rodados, total de {:.2f}R$'.format(dias,kmrodados,somadiaria+kmresult))