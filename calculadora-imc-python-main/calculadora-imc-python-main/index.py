a = float(input('Digite sua altura: '))
p = float(input('Digite seu peso: '))
imc = p / (a **2)
if imc < 18.5:
    print('IMC: {:.1f} ABAIXO DO PESO!'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('IMC: {:.1f}  PESO IDEAL!'.format(imc))
elif imc>= 25 and imc < 30:
    print('IMC: {:.1f} SOBREPESO'.format(imc))
elif imc >= 30 and imc < 40:
    print('IMC: {:.1f} OBESIDADE'.format(imc))
else:
    print('IMC: {:.1f} OBESIDADE MORBIDA'.format(imc))
