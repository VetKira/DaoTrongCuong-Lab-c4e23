content = "van ban khong quy duoc roi"
# #1 open file
# f = open("content.txt","w")#write # phai them mode , o day la w de co the ghi vao neu khong thi chi co the doc

# #2 write file
# f.write(content)

# #3 close file
# f.close()

with open("content.txt","w") as f:
    f.write(content)

with open("content.txt","r") as f: #doc 1 cuc
    c =f.read()
    print(c)