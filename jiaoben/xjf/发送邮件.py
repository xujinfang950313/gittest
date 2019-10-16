 #发送邮件
#发送邮件 （发送邮件协议：smtp）   针对smtp进行封装的模块  smtplib (python自带的模块)
import  smtplib   #smtplib封装smtp协议
import  email.mime.text                         #处理正文的数据
import email.mime.multipart                     #封装邮件的格式
sender='13750895650@163.com'                    #发送者邮箱
reser=['15039008093@163.com','l13812929932@163.com']  #接收者邮箱
server='smtp.163.com'
passwd='zxcvbnm0313'                            #授权码（允许登陆）
mssage=email.mime.multipart.MIMEMultipart()     #创建空邮件
#添加发件人、收件人、主题
mssage['From']=sender                          #来自：发送者
mssage['To']=','.join(reser)                    #到哪里：接收者
mssage['Subject']='123'                         #主题
aa='''4444'''                                   #内容
cc=email.mime.text.MIMEText(aa)                 #处理正文的内容
mssage.attach((cc))                           #将处理完的正文内容添加到邮箱

#添加附件

#定义发送的附件的文件名，文件可以是任何格式的文件
att1=email.mime.text.MIMEText(open('qq.txt','rb').read(),'base64','utf-8')
#附件携带的字段和值
att1["Content-Type"]='application/octet-stream'
#附件携带的字段和值  这里的filename可以任意写，写什么名字,邮件中显示什么名字
att1["Content-Disposition"]='attachment;filename="1.txt"'  #接收到的文件名，内容是qq.txt的内容
#将附件添加到邮件里
mssage.attach(att1)

#服务器发送邮件
smtp123=smtplib.SMTP_SSL(server,465)           #定义发送邮件的服务器和端口号
#登陆服务器,  发送者邮箱和密码
smtp123.login(sender,passwd)
#发送邮件
smtp123.sendmail(sender,reser,mssage.as_string())
#断开连接
smtp123.close()




#发送邮件 （发送邮件协议：smtp）   针对smtp进行封装的模块  smtplib (python自带的模块)
# import  smtplib   #smtplib封装smtp协议
# import  email.mime.text
# import email.mime.multipart
# sender='13750895650@163.com'
# reser=['1169197820@qq.com','l13812929932@163.com']
# server='smtp.163.com'
# passwd='zxcvbnm0313'
# mssage=email.mime.multipart.MIMEMultipart()
# #添加发件人、收件人、主题
# mssage['From']=sender
# mssage['To']=','.join(reser)
# mssage['Subject']='123'
# aa='''4444'''
# cc=email.mime.text.MIMEText(aa)
# mssage.attach((cc))
# b = ['qq.txt', 'hang.txt']
#
# for j in range(len(b)):
#     att1 = email.mime.text.MIMEText(open('{}', 'rb').read(), 'base64', 'utf-8'.format(b[j]))
#     att1["Content-Type"] = 'application/octet-stream'
#     for i in range(3):
#         att1["Content-Disposition"]='attachment;filename="{}.txt"'.format(i)
#         mssage.attach(att1)
#
# smtp123=smtplib.SMTP_SSL(server,465)
# smtp123.login(sender,passwd)
# smtp123.sendmail(sender,reser,mssage.as_string())
# smtp123.close()
