from random import randint

a = randint(0,10)
b= randint(0,10)
error = randint(0,1)
r = a + b + error
# or dung ham choice

print(a,"+",b,"=",r)

# c= a+b
# d = input("y/n: ").upper()
# if c ==r and d =="y" :
#     print("ban gioi qua , ahihihi")
# elif c==r and d =="n": 
#     print("ban dot vai loz")
# elif c !=r and d =="n":
#     print("eu oi , gioi qua , hihihi")
# elif c !=r and d =="y":
#     print("ngu nhat he mat troi la day roi , hihihi :3")
# else :
#     print("may bi dien a`")


#or
answer = input("lua chon cua ban : ").upper()
if answer == "Y":
    if error == 0 :
        print("yay")
    else :
        print("wrong")
elif answer == "N":
    if error ==0:
        print('wrong')
    else :
        print('Yay')

