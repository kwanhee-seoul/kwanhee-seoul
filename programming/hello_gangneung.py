#Day 9

days = ("Mon", "Tue", "Wed",'Thu','Fri')

for day in days:
    if day is "Thu":
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
print(fsum([1,3,5.5,7,9]))   #꿀팁: 여러개는 무조건 []로 리스트화 시켜야함

#그렇다면 tuple로도 가능할까?

print(fsum((1,2,4.5)))
#놀랍게도 가능하다. 하나하나의 값을 빼는건 어려울듯..?

