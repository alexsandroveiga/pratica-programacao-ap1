import locale

locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')

while True:
  try:
    salary = input('Digite seu salário: ')
    salary = float(salary.replace(',', '.'))
    break
  except ValueError:
    print('Digite o valor de seu salário corretamente, lembre-se de usar ponto ou vírgula somente para centavos')
    continue

percent = 0
if salary < 280:
  percent = 20
if salary >= 280 and salary < 700:
  percent = 15
if salary >= 700 and salary < 1500:
  percent = 10
if salary >= 1500:
  percent = 5

increase = (salary * percent) / 100

print('Salário antes do reajuste:', locale.currency(salary))
print(F'Porcentagem do aumento aplicado: {percent}%')
print('Valor do aumento:', locale.currency(increase))
print('Novo salário:', locale.currency(salary + increase))