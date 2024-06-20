n = int(input())

i = 0
total =0

while i<n:
    i+=1

    l,c = map(int,input().split())

    if l>c:
        total = total +c

print(total)