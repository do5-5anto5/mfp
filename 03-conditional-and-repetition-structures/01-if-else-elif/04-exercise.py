escala = float(input('Digite a escala: '))

if escala < 2:
    print('Micro')
elif escala < 3:
    print('Muito Pequeno')
elif escala < 4:
    print('Pequeno')
elif escala < 5:
    print('Leve')
elif escala < 6:
    print('Moderado')
elif escala < 7:
    print('Forte')
elif escala < 8:
    print('Grande')
elif escala < 10:
    print('Enorme')
else:
    print('Muito Grande')