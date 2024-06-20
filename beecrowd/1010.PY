codigoA,pecasA,valorA = map(float,input().split())
codigoB,pecasB,valorB = map(float,input().split())

total = (pecasA*valorA + pecasB*valorB)

print(f"VALOR A PAGAR: R$ {total:.2f}")