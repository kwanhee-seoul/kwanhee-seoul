#Day 9

days = ("Mon", "Tue", "Wed",'Thu','Fri')

for day in days:
    if day is "Wed":
        break 
    else:
        print(day)



alphabet = ('A', 'B', 'C', 'D', "E", 'F')

for pick in alphabet:
    if pick is "D":
        break
    else:
        print(pick)

from math import ceil, fsum

print(ceil(1.34352)) #반올림 ceil
                           #꿀팁: 같은 함수 선택 단축키는 커맨드 쉬프트 L
print(fsum([1,3,5,7,9]))   #꿀팁: 여러개는 무조건 []로 리스트화 시켜야함

