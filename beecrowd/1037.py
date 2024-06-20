# n =4

# if n>20: 
#     print('n m 20')
# elif n>10: 
#     print('n m 10')
# elif n > 5: 
#     print('n m 5')
# else:
#     print('menor q 5')

n=float(input())
if n>=0 and n<=25:
    print('Intervalo [0,25]')
elif n>25 and n<=50:
    print('Intervalo (25,50]')
elif n>50 and n<=75:
    print('Intervalo (50,75]')
elif n>75 and n<=100:
    print ('Intervalo (75,100]')
else:
    print('Fora de intervalo')