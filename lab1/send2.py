from gmail import GMail, Message 
from random import choice


sickness_list = ['1','2','3']
gmail = GMail("yolovl.cf@gmail.com","yolovl.123")
template = '''
<p>pussy</p>
<p>bố m&agrave;y thề bố m&agrave; thấy m&agrave;y th&igrave; t&ocirc;n lo&agrave;ng<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-kiss.gif" alt="kiss" /></p>
'''
sickness = " kiet ly"
pussy = " vl "
content= template.replace("{{sick}}",choice(sickness_list)).replace("{{push}}", pussy)
msg = Message("don to cao",to = "dungphamanh45@gmail.com",html = content)
gmail.send(msg) 