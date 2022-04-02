while True:
  try:
    firstGrade = input('Digite a primeira nota: ')
    secondGrade = input('Digite a segunda nota: ')
    firstGrade = float(firstGrade.replace(',', '.'))
    secondGrade = float(secondGrade.replace(',', '.'))
    break
  except ValueError:
    print('Por favor, digite as notas corretamente...')  
    continue

average = (firstGrade + secondGrade) / 2

if average >= 7:
  if (average == 10):
    print('Aprovado com Distinção')
  else:
    print('Aprovado')
else:
  print('Reprovado')

