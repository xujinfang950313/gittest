import  socket
#tcp协议 通信
#服务器端
#创建一个套接字（创建一个有接收能力和发送能力的对象）
# s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# #绑定IP地址和端口号,以元祖的形式
# s.bind(('192.168.1.10',50))
# #监听,启用服务器以接收连接
# s.listen(3)#数字代表最大的等待数
# while True:
#     #接收请求
#     client,addr=s.accept()   #addr:接收   accept:接收
#     #client变量：建立客户端连接的信息
#     #addr变量：客户端的ip地址和端口号
#     recive=client.recv(1024)
#     #recive变量：接收客户端发送的请求最大1024个字节    recv:接收数据
#     print(recive.decode('utf8'))  #将接收过来的信息解码打印
#     reponse=input('请响应：')   #将输入的响应内容
#     client.send(reponse.encode('utf8'))#将输入的内容响应内容发送   send:发送  encode:编码



# s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.bind('192.168.1.10',33)
# s.listen(3)
# while True:
#     client,addr=s.accept()
#     jieshou=client.recv(1024)
#     print(jieshou.decode('utf8'))
#     fasong=input('输入响应：')
#     s.send(fasong.encode('utf8'))











import  socket
# tcp协议 通信
# 服务器端
# # 创建一个套接字（创建一个有接收能力和发送能力的对象）
# s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# #绑定IP地址和端口号,以元祖的形式
# s.bind(('192.168.1.10',50))
# #监听,启用服务器以接收连接
# s.listen(3)#数字代表最大的等待数
# while True:
#     #接收请求
#     client,addr=s.accept()   #addr:接收   accept:接收
#     #client变量：建立客户端连接的信息
#     #addr变量：客户端的ip地址和端口号
#     recive=client.recv(1024)
#     #recive变量：接收客户端发送的请求最大1024个字节    recv:接收数据
#     print(recive.decode('utf8'))  #将接收过来的信息解码打印
#     reponse=input('请响应：')   #将输入的响应内容
#     client.send(reponse.encode('utf8'))#将输入的内容响应内容发送   send:发送












