meses = [
    "Janeiro",
    "Fevereiro",
    "Março",
    "Abril",
    "Maio",
    "Junho",
    "Julho",
    "Agosto",
    "Setembro",
    "Outubro",
    "Novembro",
    "Dezembro",
]

# iterate indexes at meses list.
# for index in range(len(meses)):
#     mes = meses[index]
#     print(f'{mes} é o {index + 1}° mês do ano.')

# enumerate meses, unpacking index and item turn de code more readble
for index, mes in enumerate(meses, start=1):
    print(f'{mes} é o {index}° mes do ano.')
