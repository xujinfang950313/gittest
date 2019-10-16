# def xx():
#     a = sum(range(101))
#     print(a)
# if __name__=='__main__':#判断当前被执行的文件是不是本文件 ，如果是本文件，显示结果，反之不显示结果
# xx()
import paramiko
# client=paramiko.Transport(('192.168.2.99',22))
# #连接主机，输入用户名和密码
# client.connect(username='xjf', password='123456')
# #创建一个sftp的客户端
# sftp_client=paramiko.SFTPClient.from_transport(client)
# #从liunx下载传文件到windows
# sftp_client.get('/home/xjf/桌面/ert.txt',r'E:\jiaoben\xjf\ll.txt')




#从windows上传文件到linux
client=paramiko.Transport(('192.168.2.99',22))
#连接主机，输入用户名和密码
client.connect(username='xjf', password='123456')
#创建一个sftp的客户端
sftp_client=paramiko.SFTPClient.from_transport(client)
#从liunx下载传文件到windows
# sftp_client.rename('/home/xjf/桌面/jj','/home/xjf/桌面/xx')
# print(sftp_client.stat('/home/xjf/桌面/1.html'))
print(sftp_client.listdir('/home/xjf/桌面'))