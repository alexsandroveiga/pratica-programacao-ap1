print('Digite qualquer número, digite -1 para finalizar:')

numbers = []

while True:
  try:    
    number = int(input())
    if number == -1:
      break
    numbers.append(number)
  except ValueError:
    print('Digite um número inteiro:')
    continue

print(F'''
Quantidade de valores lidos: {len(numbers)}
Valores informados: {numbers}
Lista de valores informados em ordem inversa:''')

for x in list(reversed(numbers)):
  print(x)

average = sum(numbers) / len(numbers) 
aboveAverage = sorted(i for i in numbers if i >= average)
belowSeven = sorted(i for i in numbers if i < 7)

print(F'''Soma dos valores: {sum(numbers)}
Média dos valores: {average}
Quantidade de valores acima da média: {len(aboveAverage)}
Quantidade de valores abaixo de sete: {len(belowSeven)}

Trabalho feito com muito estudo e disciplina.
Alexsandro Veiga © 2022''')