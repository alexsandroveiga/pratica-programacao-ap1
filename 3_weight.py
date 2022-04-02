while True:
  try:
    height = input('Digite a sua altura: ')
    height = float(height.replace(',', '.'))
    break
  except ValueError:
    print('Por favor, digite sua idade corretamente...')  
    continue

sex = input('Digite seu sexo (M ou F): ').upper()

while sex not in ('M','F','MASCULINO', 'FEMININO'):
  sex = input('Digite seu sexo corretamente: ').upper()

if sex == 'M' or sex == 'MASCULINO':
  weight = (72.7 * height) - 58
  print('Seu peso ideal é:', '{:.2f}kg'.format(weight))

if sex == 'F' or sex == 'FEMINIMO':
  weight = (62.1 * height) - 44.7
  print('Seu peso ideal é:', '{:.2f}kg'.format(weight))