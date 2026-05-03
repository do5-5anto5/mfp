employees = {
    "Alice": {"salário": 5000, "ferias_restantes": 15, "departamento": "TI"},
    "Bruno": {"salário": 4500, "ferias_restantes": 10, "departamento": "Financeiro"},
    "Carlos": {"salário": 6000, "ferias_restantes": 20, "departamento": "Marketing"},
    "Diana": {"salário": 7000, "ferias_restantes": 5, "departamento": "Vendas"},
    "Eduardo": {"salário": 5500, "ferias_restantes": 12, "departamento": "TI"},
}

# 1. access and print the salary of Bruno
print(employees.get("Bruno").get('salário'))
print (type(employees.get("Bruno").get('salário')))

# 2. access and print the 'ferias_restantes' of Diana
print(employees.get('Diana').get('ferias_restantes'))

# 3. Eduardo gets a salary raise of 5%. update it in the dictionary
raisedSalary = employees.get('Eduardo').get('salário') * 1.05
employees.get('Eduardo').update({'salário': raisedSalary})
print(employees.get('Eduardo').get('salário'))

# 4. A new worker comes to team. add her info:
# name: "Fernanda", salary: 6000, ferias_restantes: 30 (CLT), departamento: "RH"
employees.update({'Fernanda': {'salário': 6000, 'ferias_restantes': 30, 'departamento': 'RH'}})
print (employees)

# 5. Sum and print the total salary of all employees
totalSalary = 0
for employee in employees: 
    totalSalary += employees.get(employee).get('salário')
print(f'total salary is {totalSalary}')

# 6. Alice resigned. delete her from the dictionary
aliceResigned = employees.pop('Alice')
print('Alice resigned: ', aliceResigned)

# 7. Search an employee named Carlos in the dictionary
print(employees.get('Carlos', 'not found'))