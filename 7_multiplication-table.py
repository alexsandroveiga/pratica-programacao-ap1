while True:
  try:
    number = int(input('Digite um número inteiro de 1 à 10: '))
    if number < 1 or number > 10:
      raise ValueError
    break
  except ValueError:  
    continue

print('Tabuada de', number)
for a in range(1, 10 + 1):
  multiplication = number * a
  print(number, 'X', a, '=', multiplication)