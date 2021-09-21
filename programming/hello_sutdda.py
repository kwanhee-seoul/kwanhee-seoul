import random




start=int(input("섯다에 오신것을 환영합니다. 시작하시려면 비밀번호 입력."))
if start == 5400:
    print("시작하겠습니다.")
    playeropen=random.randrange(1,12)
    playerclose=random.randrange(1,12)
    print(playeropen,playerclose)