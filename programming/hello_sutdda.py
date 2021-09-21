import random




start=int(input("섯다에 오신것을 환영합니다. 시작하시려면 비밀번호 입력."))
if start == 5400:
    print("시작하겠습니다.")
   
    hand = int()
    comhand = int()
    defaultmoney = 10000
    defaultcommoney = 10000



    while defaultmoney>0 and defaultcommoney>0:
        print("\n\n\n시작하겠습니다. \n")
        print("당신의 손패입니다.")
        playeropen=random.randrange(1,10)
        playerclose=random.randrange(1,10)
        playerkwang=random.randrange(1,100)
        playercatcher=random.randrange(1,20)  #땡잡이는 끗한테서 망통#
        print(playeropen,playerclose)
        if playerkwang == 38:
            print("3 8 광땡")
        elif playercatcher == 37:
            print("3 7 땡잡이")
        elif playerclose > playeropen:
            print(playerclose,"끝")
            hand = playerclose
        elif playeropen == playerclose:
            print(playerclose,"땡")
            hand = playerclose+100
        elif playerclose < playeropen:
            print(playeropen,"끝")
            hand = playeropen


        #print(" \n테스트용으로 출력되는 컴퓨터의 손패입니다. 릴리즈 전에 삭제하시오")
        comopen=random.randrange(1,10)
        comclose=random.randrange(1,10)
        comkwang=random.randrange(1,100)
        comcatcher=random.randrange(1,20)  #땡잡이는 끗한테서 망통#
        '''print(comopen,comclose)
        if comkwang == 38:
            print("3 8 광땡")  
        elif comcatcher == 37:
            print("3 7 땡잡이")
        elif comclose > comopen:
            print(comclose,"끝")
            comhand = comclose
        elif comopen == comclose:
            print(comclose,"땡")
            comhand = comclose+100
        elif comclose < comopen:
            print(comopen,"끝")
            comhand = comopen'''

        print("\n당신의 오픈 카드는", playeropen)
        print("\n컴퓨터의 오픈 카드는",comopen)


        #print("\n테스트용 각 패 출력",hand, comhand)
        
        print("\n당신의 현재 칩은",defaultmoney,"입니다.\n컴퓨터의 현재 칩은",defaultcommoney,"입니다.")
        batmoney=int(input("배팅할 칩을 적어주세요"))
                
        
            
        defaultmoney-=batmoney
        #print("테스트용 디폴트머니 출력",defaultmoney)
        defaultcommoney-=batmoney
        #print("테스트용 컴디폴트머니 출력",defaultcommoney)




        print("\n결과 오픈하겠습니다.\n")
        
        print("컴퓨터의 패는",comopen,comclose)
        if comkwang == 38:
            print("3 8 광땡")  
        elif comcatcher == 37:
            print("3 7 땡잡이")
        elif comclose > comopen:
            print(comclose,"끝")
            comhand = comclose
        elif comopen == comclose:
            print(comclose,"땡")
            comhand = comclose+100
        elif comclose < comopen:
            print(comopen,"끝")
            comhand = comopen

        print("\n\n\n")
        if comkwang == 38 and playerkwang == 38:
            print("당신은 10000분의 1의 확률을 뚫고\n광땡을 들고 광땡을 만났습니다.") 
            defaultcommoney += batmoney
            defaultmoney += batmoney
        elif comkwang == 38:
            print("컴퓨터가 광땡으로 승리.")
            defaultcommoney += batmoney
        elif playerkwang == 38:
            print("당신이 광땡으로 승리.") 
            defaultmoney += batmoney
            defaultmoney += batmoney    #여기까지 광의 경우

        elif hand >= 100 and comhand >= 100:
            if hand > comhand:
                print("당신이",hand-100,"땡으로",comhand-100,"땡에게 승리.")
                defaultmoney += batmoney
                defaultmoney += batmoney
            elif hand == comhand:
                print("당신이",hand-100,"땡으로",comhand-100,"땡에게 비김.")
                defaultcommoney += batmoney
                defaultmoney += batmoney
            elif hand < comhand:
                print("당신이",hand-100,"땡으로",comhand-100,"땡에게 패배.")
                defaultcommoney += batmoney
                defaultcommoney += batmoney   #여기까지 땡의 경우#

        elif hand>=100:
            print("당신이",hand-100,"땡으로",comhand,"끝에게 승리.")
            defaultmoney += batmoney
            defaultmoney += batmoney
        elif comhand>=100:
            print("당신이",hand,"끝으로",comhand-100,"땡에게 패배.")
            defaultcommoney += batmoney
            defaultcommoney += batmoney    #여기까지 떙과 끝이 만날경우#



        elif hand > comhand:
                print("당신이",hand,"끝으로",comhand,"끝에게 승리.")
                defaultmoney += batmoney
                defaultmoney += batmoney
        elif hand == comhand:
                print("당신이",hand,"끝으로",comhand,"끝에게 비김.")
                defaultcommoney += batmoney
                defaultmoney += batmoney
        elif hand < comhand:
                print("당신이",hand,"끝으로",comhand,"끝에게 패배.")
                defaultcommoney += batmoney
                defaultcommoney += batmoney  #여기까지 끝의 경우#
        print("당신의 칩은",defaultmoney,"컴퓨터의 칩은",defaultcommoney)      
                
        qwerty=int(input("다시 하시겠습니까? 1/0"))
        if qwerty == 1:
            pass
        else:
            defaultmoney = -1000000

    if defaultcommoney > 0:
        print("당신의 파산으로 게임이 끝났습니다. 안녕히 가십시오")

    else:
        print("컴퓨터의 파산으로 게임이 끝났습니다. 안녕히 가십시오.")