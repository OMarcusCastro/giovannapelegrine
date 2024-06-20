total_days = int(input())

years = total_days//365

months = (total_days%365)//30

days =(total_days%365)%30

print(f'{years} ano(s)')
print(f'{months} mes(es)')
print(f'{days} dia(s)')