#Day 3
import time

kwanhee = {
    'name':'Kim kwanhee',
    'location':'seoul',
    'fav_game':'league of legend',
}
print(kwanhee["name"])

yongsun =  {
    'name':'Ryu yongsun',
    'location':'seoul',
    'do_for_fun':'Drawing',
    "Is_yongsun_cute?" : True,
}
print(yongsun["name"])
print("Is yongsun cute? kwanhee said yongsun is the cutest man in Yongsan High.")
print(yongsun["Is_yongsun_cute?"])
print("look_again")
yongsun["Is_yongsun_cute?"]=False
print(yongsun["Is_yongsun_cute?"])


sujin = {
    'name':'Kim sujin',
    'age' : 14,
    'fav_food': 'Kimchi_jumokbab',
    'cloth' : 'bangtan'
}
print (sujin["age"])
print ("hello Python")
print (sujin["cloth"])

#민호의 마지막 시험날까지 디데이를 구하려고 했으나
#왜인지 datetime에서 오류가 난다. 일단 봉인
'''
import time
from datetime import date
today = date.today()
today
datetime.date(2021, 5, 13)
today == date.fromtimestamp(time.time())
True
my_birthday = date(today.year, 5, 14)
if my_birthday < today:
    my_birthday= my_birthday.replace(year+today.year + 1)
my_birthday
datetime.date(2020, 5, 14)
time_to_birthday = abs(my_birthday - today)
'''


minho = {
    'age' :18 ,
    'do_for_fun' : 'twitch',
    #'end_of_midtumn_test' : time_to_birthday,

}

print(minho['age'])

ganzi = {
    "cafe" : "starbucks",
    "IDcard" : "Macbook",
    "my feel" : "fucking bad.. i didnt wanna this expensive shit",
}

print(ganzi["cafe"])
print(ganzi["IDcard"])
print(ganzi["my feel"])