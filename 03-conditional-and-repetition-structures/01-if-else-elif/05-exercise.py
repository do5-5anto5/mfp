plan = 100.00
planMessages = 50
planMinutes = 50

extraMinutePrice = 0.25
extraMessagePrice = 0.15

emergencyTax = 2.00
fee = 0.05

usedMinutes = int(input("Quantos minutos foram usados? "))
usedMessages = int(input("Quantos SMS foram enviados? "))

totalBill = plan
print(f"Valor base: R$ {plan:.2f}")


if usedMessages > planMessages:
    totalPerExtraMessages = (usedMessages - planMessages) * extraMessagePrice
    totalBill += totalPerExtraMessages
    print(f"Valor por minutos adicionais: R$ {totalPerExtraMessages:.2f}")

if usedMinutes > planMinutes:
    totalPerExtraMinutes = (usedMinutes - planMinutes) * extraMinutePrice
    totalBill += totalPerExtraMinutes
    print(f"Valor por minutos adicionais: R$ {totalPerExtraMinutes:.2f}")

totalFee = (totalBill + emergencyTax) * fee

totalBill += emergencyTax + totalFee  # ((totalBill + emergencyTax) * fee)

print(
    f"""Taxa de emergência: R$ {emergencyTax:.2f}
Valor do imposto: R$ {totalFee:.2f}
Total: R$ {totalBill:.2f}"""
)
