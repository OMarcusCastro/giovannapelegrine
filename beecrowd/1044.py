#resto ==0

A,B=map(int,input().split())

if (B%A==0):
    print('Sao Multiplos')
elif (A%B==0):
    print('Sao Multiplos')      
else:
    print('Nao sao Multiplos')