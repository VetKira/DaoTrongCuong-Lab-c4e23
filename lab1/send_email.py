from gmail import GMail, Message 
from random import choice


sickness_list = ['1','2','3']
gmail = GMail("yolovl.cf@gmail.com","yolovl.123")
template = " ia chay vl , {{sick}}, the cuon {{push}}"
sickness = " kiet ly"
pussy = " vl "
# content= template.replace("{{sick}}",sickness).replace("{{push}}", pussy) #thay the {{sick}} bang sickness

content= template.replace("{{sick}}",choice(sickness_list)).replace("{{push}}", pussy)
msg = Message("don to cao",to = "dungphamanh45@gmail.com",text = content)
gmail.send(msg) 