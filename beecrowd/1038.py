codigo , qtd = map(int,input().split())

if codigo ==1:
    preco = 4
if codigo ==2:
    preco = 4.50
if codigo ==3:
    preco = 5
if codigo ==4:
    preco = 2
if codigo ==5:
    preco =1.50

preco_total= qtd*preco

print(f"Total: R$ {preco_total:.2f}")