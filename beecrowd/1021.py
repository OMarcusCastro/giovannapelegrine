

# ##não deu certo, não consegui terminar com resultado correto

# valor=float(input())

# notaG= valor //100
# valor= valor - notaG*100

# notaF= valor //50
# valor= valor - notaF*50

# notaE= valor //20
# valor= valor - notaE*20

# notaD= valor //10
# valor= valor - notaD*10
 
# notaC= valor //5
# valor= valor - notaC*5

# notaB= valor //2
# valor= valor - notaB*2

# moedaA= valor//1
# valor= valor - moedaA*1
# moedaA=float('%.2f'%moedaA)
# valor=float('%.2f'%valor)

# moedaB= valor//0.50
# valor= valor - moedaB*0.50
# moedaB=float('%.2f'%moedaB)
# valor=float('%.2f'%valor)

# moedaC= valor//0.25
# valor= valor - moedaC*0.25
# moedaC=float('%.2f'%moedaC)
# valor=float('%.2f'%valor)

# moedaD= valor//0.10
# valor= valor - moedaD*0.10
# moedaD=float('%.2f'%moedaD)
# valor=float('%.2f'%valor)

# moedaE= valor//0.05
# valor= valor - moedaE*0.05
# moedaE=float('%.2f'%moedaE)
# valor=float('%.2f'%valor)

# moedaF= valor//0.01
# valor= valor - moedaF*0.01
# moedaF=float('%.2f'%moedaF)
# valor=float('%.2f'%valor)

# print("NOTAS:")
# print('{} nota(s) de R$ 100.00'.format(int(notaG)))
# print('{} nota(s) de R$ 50.00'.format(int(notaF)))
# print('{} nota(s) de R$ 20.00'.format(int(notaE)))
# print('{} nota(s) de R$ 10.00'.format(int(notaD)))
# print('{} nota(s) de R$ 5.00'.format(int(notaC)))
# print('{} nota(s) de R$ 2.00'.format(int(notaB)))

# print('MOEDAS:')
# print('{} moeda(s) de R$ 1.00'.format(int(moedaA)))
# print('{} moeda(s) de R$ 0.50'.format(int(moedaB)))
# print('{} moeda(s) de R$ 0.25'.format(int(moedaC)))
# print('{} moeda(s) de R$ 0.10'.format(int(moedaD)))
# print('{} moeda(s) de R$ 0.05'.format(int(moedaE)))
# print('{} moeda(s) de R$ 0.01'.format(int(moedaF)))



# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
n = float(input())
#100

nota100 = n//100
n -= (int(nota100))*100
n = float(f'{n:.2f}')

#50

nota050 = n//50
n -= (nota050)*50
n = float(f'{n:.2f}')
#20
nota020 = n//20
n -= (nota020)*20
n = float(f'{n:.2f}')
#10
nota010 = n//10
n -= (nota010)*10
n = float(f'{n:.2f}')
#5
nota005 = n//5
n -= (nota005)*5
n = float(f'{n:.2f}')
#2
nota002 = n//2
n -= (nota002)*2
n = float(f'{n:.2f}')
#1
moeda100 = n//1
n -= (moeda100)*1
n = float(f'{n:.2f}')
#0.50
moeda050 = n//0.50
n -= (moeda050)*0.50
n = float(f'{n:.2f}')
#0.25
moeda025 = n//0.25
n -= (moeda025)*0.25
n = float(f'{n:.2f}')
#0.10
moeda010 = n//0.10
n -= (moeda010)*0.10
n = float(f'{n:.2f}')
#0.05
#print(n)
moeda005 = n//0.05
n -= (moeda005)*0.05
n = float(f'{n:.2f}')
#0.01
#print('n',n)
moeda001 = n/0.01
#print(moeda001)
n -= (moeda001)*0.01
n = float(f'{n:.2f}')

print('NOTAS:')
print(f'{int(nota100)} nota(s) de R$ 100.00')
print(f'{int(nota050)} nota(s) de R$ 50.00')
print(f'{int(nota020)} nota(s) de R$ 20.00')
print(f'{int(nota010)} nota(s) de R$ 10.00')
print(f'{int(nota005)} nota(s) de R$ 5.00')
print(f'{int(nota002)} nota(s) de R$ 2.00')
print('MOEDAS:')
print(f'{int(moeda100)} moeda(s) de R$ 1.00')
print(f'{int(moeda050)} moeda(s) de R$ 0.50')
print(f'{int(moeda025)} moeda(s) de R$ 0.25')
print(f'{int(moeda010)} moeda(s) de R$ 0.10')
print(f'{int(moeda005)} moeda(s) de R$ 0.05')
print(f'{int(moeda001)} moeda(s) de R$ 0.01')