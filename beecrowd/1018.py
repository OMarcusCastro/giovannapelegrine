

valor=int(input())
print(valor)

notaG= valor //100
valor= valor - notaG*100

notaF= valor //50
valor= valor - notaF*50

notaE= valor //20
valor= valor - notaE*20

notaD= valor //10
valor= valor - notaD*10
 
notaC= valor //5
valor= valor - notaC*5

notaB= valor //2
valor= valor - notaB*2

notaA= valor//1
valor= valor - notaA*1


print('{} nota(s) de R$ 100,00'.format(notaG))
print('{} nota(s) de R$ 50,00'.format(notaF))
print('{} nota(s) de R$ 20,00'.format(notaE))
print('{} nota(s) de R$ 10,00'.format(notaD))
print('{} nota(s) de R$ 5,00'.format(notaC))
print('{} nota(s) de R$ 2,00'.format(notaB))
print('{} nota(s) de R$ 1,00'.format(notaA))

