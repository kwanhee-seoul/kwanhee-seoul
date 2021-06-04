def plus(a,b):
    return(int(a) + int(b))

def minus(a,b):
    return(int(a) - int(b))

def times(a,b):
    return(int(a) * int(b)) #곱하기

def division(a,b):
    return(int(a) / int(b))  #나누기. 소숫점 표시된다.

def negation(a):
    return(-int(a)) #음수화

def power(a,b):
    return(int(a) ** int(b)) #제곱

def remainder(a,b):
    return(int(a) % int(b)) #나머지계산

def what(a,b):
    return(int(a) // int(b))

# 60만들기
print(plus(52,8))

print(minus(78,"18"))

print(times("10",6))

print(division("120","2"))

print(negation("-60"))

print(power(60,2))

print(remainder(180,120))

print(what(729,9))
