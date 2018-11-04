from gmail import GMail, Message 
from random import choice
from datetime import datetime

gmail = GMail("yolovl.cf@gmail.com","yolovl.123")
template = " hom nay toi bi om , toi bi {{sick}}, toi xin phep nghi "
sickness = (" ngo doc thuc pham","tieu chay","tao bon","an khong ngon ngu k yen")

content= template.replace("{{sick}}",choice(sickness))
msg = Message("don xin nghi",to = "daotrongc@gmail.com",text = content)


now = datetime.time(datetime.now())
now1 = now.strftime("%H:%M")
while True :
    if now1<"7:00" :
        gmail.send(msg)
        break