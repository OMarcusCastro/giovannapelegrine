# n =4

# if n>20: 
#     print('n m 20')
# elif n>10: 
#     print('n m 10')
# elif n > 5: 
#     print('n m 5')
# else:
#     print('menor q 5')

# v  = int(input())
# x=0
# while x<v:
#     print(x)
#     x = x+2

x = 0
qtd = 0
soma = 0
while x<10:
    x=x+1
    val = int(input())

    if val>0:
        qtd=qtd+1
        soma = soma + val

media = soma/qtd

print(f"media dos positivos: {media}")
    