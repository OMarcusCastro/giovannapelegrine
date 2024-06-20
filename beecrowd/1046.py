h1,h2= map(int,input().split())

tempo=h2-h1
if h2<=h1:
    tempo =tempo+24

print(f"O JOGO DUROU {tempo} HORA(S)")