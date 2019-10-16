#paramiko ,封装了ssh协议，主要用于远程控制
import  paramiko
# #创建ssh客户端
# ssh123=paramiko.SSHClient()
# # #将第一次连接的主机跳过验证，并添加到know_host文件中   know_host文件存放了可以远程的主机IP地址
# ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy())  #跳过进入host文件查看,如果没有这句，会报错。
#missing :遗漏   policy:系统，信息  autaddpolicy :自动添加系统
# ssh123.connect(hostname='192.168.2.99',port=22,username='xjf',password='123456')  #连接到linux系统
# stuin ,stuout,stuerr =ssh123.exec_command('pwd')#输入在liunx上的命令,定义3个变量 ,产生3个结果 括号里的命令必须是能够直接有结果的
# #stuin:输入命令（但是打印不出来，因为加密了）  command:命令 exec:执行
# #stuout:命令运行后的结果
# #stuerr:命令的报错
# aa=stuout.read().decode('utf-8')
# print(aa)
# ssh123.close()#断开连接


#paramiko ,封装了ssh协议，主要用于远程控制
import  paramiko
ssh1=paramiko.SSHClient()
ssh1.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh1.connect(hostname='192.168.2.99',port=22,username='xjf',password='123456')
a,b,c=ssh1.exec_command('pwd')
aa=b.read().decode('utf-8')
print(aa)
ssh1.close()



#下载
#使用paramiko模块中的stfpclient组件传输文件
#建立一个传输通道，填入IP地址和端口号（是一个元祖）
#将liunx的文件下载到windows
import paramiko
client=paramiko.Transport(('192.168.2.99',22))
#连接主机，输入用户名和密码
client.connect(username='xjf', password='123456')
#创建一个sftp的客户端
sftp_client=paramiko.SFTPClient.from_transport(client)
#从liunx下载传文件到windows
sftp_client.get('/home/xjf/桌面/ert.txt',r'E:\jiaoben\xjf\ll.txt')
               # 第一个是虚拟机打开“在终端打开”的界面的路径
               #第二个是包的路径




#下载：get (将服务器下载到本地文件) 上传put（将本地文件上传到服务器）


#上传
#从windows上传文件到linux
client=paramiko.Transport(('192.168.2.99',22))
#连接主机，输入用户名和密码
client.connect(username='xjf', password='123456')
#创建一个sftp的客户端
sftp_client=paramiko.SFTPClient.from_transport(client)
sftp_client.put(r'E:\jiaoben\xjf\hh.txt','/home/xjf/桌面/hhh.txt')


#重命名
sftp_client.rename('/home/xjf/桌面/jj','/home/xjf/桌面/xx')
#新建目录
sftp_client.mkdir('/home/xjf/桌面/jj')
#查看文件状态
print(sftp_client.stat('/home/xjf/桌面/1.html'))
#列出服务器目录下的文件
print(sftp_client.listdir('/home/xjf/桌面'))
