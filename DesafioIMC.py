#calculadora de imc

for imc in range(10000000):
  
    altura = float(input('Digite sua altura: '))
    peso = float(input('Digite seu pesso: '))

    calculo = peso / (altura * altura)
  
    if calculo < 18.5:
      print(f'Voce está com IMC de {calculo} que é considerado magreza')
      
    elif calculo >= 18.5 and calculo < 25.0:
      print(f'O seu IMC é de {calculo} que é considerado normal')

    elif calculo >= 25.0 and calculo < 30.0:
      print(f'O seu IMC é de {calculo} que é considerado sobrepeso')

    elif calculo >= 30.0 and calculo < 35.0:
      print(f'O seu IMC é de {calculo} que é considerado Obesidade nivel 1')

    elif calculo >= 35.0 and calculo < 38.0:
      print(f'O seu IMC é de {calculo} que é considerado obesiade nivel 2')

    elif calculo >= 38.0 and calculo < 100.0:
      print(f'O seu IMC é de {calculo} que é considerado Obesidade nivel 3')

    else:
      print('digite o valor corretamente: ')
    break