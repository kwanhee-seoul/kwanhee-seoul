c=""

'''c="" 와 while 의 역할이 뭔지 모르겠다. 
일단 Q는 quit의 역할을 한다. 연산자 입력에서
Q를 누르면 끝난다.'''

while c.upper() != "Q" :
    a = int(input("첫번째숫자입력 : "))
    b = int(input("두번째숫자입력 : "))
    c = input("연산자 입력 예> +,-,*,/,// ,**,Q(quit) : ")

if c == "+" :
    print(a + b)
elif c == "-" :
    print(a - b)
elif c == "*" :   #elifs는 아마도 else if 인듯.
    print(a * b)
elif c == "/" :
    print(a / b)
elif c == "//" :
    print(a // b)
elif c == "**" :
    print(a ** b)
#계속 숫자 입력해도 계산이 안되는건 왜그런지 모르겠음

