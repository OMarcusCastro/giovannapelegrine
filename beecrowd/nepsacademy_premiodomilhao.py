n = int(input())

i = 0
acessos = 0
dia = 1

while i<n:
    i+=1

    acesso_dia = int(input())

    if acessos<10**6:
        acessos+=acesso_dia
        if acessos>=10**6:
            dia = i

print(dia)

   