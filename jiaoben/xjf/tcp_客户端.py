#客户端
#客户端不需要绑定IP和监听
import  socket
import socket
# while True:  #必须一直处于运行的状态
#     #创建一个套件
#     sock=socket.socket()
#     #客户端不需要绑定IP地址，但是连接服务器
#     sock.connect(('192.168.1.10',50))
#     #发送请求
#     #输入请求的内容
#     message=input('请输入请求内容：')
#     #发送请求的内容
#     sock.send(message.encode('utf8'))
#     #接收服务器的响应
#     recive=sock.recv(1024)
#     print(recive.decode('utf8'))
#     #断开连接
#     sock.close()




while True:
    s=socket.socket()
    s.connect(('192.168.1.7',33))
    a=input('输入请求：')
    s.send(a.encode('utf8'))
    xy=s.recv(2014)
    print(xy.decode('utf8'))
    s.close()










