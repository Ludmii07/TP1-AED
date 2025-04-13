destinatario = str(input("Ingrese el nombre y apellido del beneficiario: "))
iso = str(input("Ingrese el código de identificación de la orden de pago, en formato 'AAA': "))
montoNom = int(input("Ingrese el monto nominal: "))

moneda = ""
montoBase = 0
montoFinal= ""

if "ARS" in iso:
    moneda = "ARS"
    montoBase = montoNom * 0.05

elif "EUR" in iso:
    moneda = "EUR"
    montoBase = montoNom * 0.07
elif "USD" in iso:
    moneda = "USD"
    montoBase = montoNom * 0.07
elif "GBP" in iso:
    moneda = "GBP"
    montoBase = montoNom * 0.09
elif "JPY" in iso:
    moneda = "JPY"
    montoBase = montoNom * 0.09
else:
    print("Moneda no autorizada")

if montoBase > 50000:
    montoFinal = montoBase * 0.21
else:
    montoFinal = montoBase

print("Beneficiario:", destinatario)
print("Moneda:", moneda)
print("Monto base:", montoBase)
print("Monto final: ", montoFinal)