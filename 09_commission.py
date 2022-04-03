from random import randint

employees = randint(30,50)
employeeSalary = 200
employeePercentage = 9
commissions = []
salaries = []

for x in range(0, employees):
  commissions.append(randint(0,15000))

for y in commissions:
  salaries.append(((y * employeePercentage) / 100) + employeeSalary)

print(F'''Quantidade de vendedores: {employees}

R$ 200 - R$ 299: {len(sorted(i for i in salaries if i >= 200 and i <= 299))} vendedores
R$ 300 - R$ 399: {len(sorted(i for i in salaries if i >= 300 and i <= 399))} vendedores
R$ 400 - R$ 499: {len(sorted(i for i in salaries if i >= 400 and i <= 499))} vendedores
R$ 500 - R$ 599: {len(sorted(i for i in salaries if i >= 500 and i <= 599))} vendedores
R$ 600 - R$ 699: {len(sorted(i for i in salaries if i >= 600 and i <= 699))} vendedores
R$ 700 - R$ 799: {len(sorted(i for i in salaries if i >= 700 and i <= 799))} vendedores
R$ 800 - R$ 899: {len(sorted(i for i in salaries if i >= 800 and i <= 899))} vendedores
R$ 900 - R$ 999: {len(sorted(i for i in salaries if i >= 900 and i <= 999))} vendedores
R$ 1000 em diante: {len(sorted(i for i in salaries if i >= 1000))} vendedores''')