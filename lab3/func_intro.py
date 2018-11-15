# def add():      #def la dinh nghia 1 ham khai bao ham , add la ham tong 
#     a=5                       # 4 dong nay la than ham , function body
#     b=10
#     r= a+b
#     print(r)

# def add(a,b):      
    
#     r= a+b
#     # print(r)
#     return r



# #call func , goi ham
# s = add(4,10)
# print(s)



# viet 1 ham , ten cua ham la eval , ham nay nhan 3 tham so dau vao la a,b,op . Tu 3 tham so tinh ket qua va return kq in ra va dung kq

def  eval(a,b,op) :
    if op == "+" :
       r= a+b
    elif op == "-" :
       r= a-b
    elif op == "*" :
       r= a*b
    elif op == "/" :
       r= a/b
    else :
        print("may bi dien a")
    return r

# s = eval(9,10,"-")
# print(s)