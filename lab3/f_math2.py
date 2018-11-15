from random import randint,choice #hoac import * cho nhanh
from func_intro import eval # duoc rut ngan tu import func_intro

def generate_quiz(): # khong can den ng dung nhap vao du lieu gi nen k can tham so dau vao , ben trong () k co gi

    option = ["+","-","*","/"]
    op = choice(option)
    # print(op)

    x = randint(0,10)
    y = randint(0,10)

    error = [-1,0,0,1,2]
    err = choice(error)

    # s = eval(a,b,op) # duoc rut ngan tu s = func_intro.eval(a,b,op) khi da xai import eval
    # r = a + b + err
    # print(a,op,b,"=",r)
    #bien thanh : 
    r = eval(x,y,op)+err

    return x,y,op,r,err
a,b,op,r,err = generate_quiz() # a ,b , op ,r,err la noi dung de luu tru 5 cai return duoc goi ra

print(a,op,b,"=",r)

answer = input("lua chon cua ban : ").upper()
if answer == "Y":
    if err == 0 :  # or if r = func_intro.eval(a,b,op)
        print("yay")
    else :
        print("wrong")
elif answer == "N":
    if err ==0: # or if r = func_intro.eval(a,b,op)
        print('wrong')
    else : 
        print("yay")
