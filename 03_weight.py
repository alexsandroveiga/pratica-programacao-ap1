while True:
  try:
    height = input('Digite a sua altura: ')
    height = float(height.replace(',', '.'))
    break
  except ValueError:
    print('Por favor, digite sua altura corretamente...')  
    continue

mensIdealWeight = (72.7 * height) - 58
womensIdealWeight = (62.1 * height) - 44.7

print('Peso ideal')
print('Para homens:', '{:.2f}kg'.format(mensIdealWeight))
print('Para mulheres:', '{:.2f}kg'.format(womensIdealWeight))