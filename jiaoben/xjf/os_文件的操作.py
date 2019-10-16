#os模块的使用
import os
dd=os.popen('ping 192.168.2.99')       # popen()执行cmd命令
print(dd.read())                       #显示ping的结果
print(os.getcwd())                     # getcwd:获取当前所在的目录
os.chdir('..')                         # chdir 切换目录  ：切换到上级目录
print(os.getcwd())                     #获取当前所有的目录
os.mkdir('aaa')                        # mkdir创建目录
os.makedirs('ee/qq/ww')                # makedirs 创建递归目录
os.removedirs('ee/qq/ww')              # 删除递归目录
os.rmdir('aaa')                        # 删除空目录
os.remove('jj.html')                   # remove:删除文件
os.rename('qq.txt','q.txt')            # 文件重命名 rename
#获取目录下面的所有文件 listdir
print(os.listdir()) #括号内不写入，默认当前目录下的所有文件
print(os.listdir('C:'))#括号内写入其他目录的绝对路径时，显示改路径下目录的所有文件

#将文件名和路径分隔开
aa=os.path.split(r'‪C:\Users\xjf\Desktop\搜索 Everything.lnk')
print(aa)

#将文件的后缀名和路径隔开
aa=os.path.splitext(r'E:\jiaoben\hang.txt')
print(aa)

#isdir判断是否是目录
aa=os.path.isdir(r'E:/jiaoben')
print(aa)

#isfile判断是否是文件
aa=os.path.isfile(r'hang.txt')
print(aa)



#将当前目录下的所有.py过滤到列表中

c=[]
a=(os.listdir())
for i in a:
 aa=os.path.splitext(r'E:\jiaoben\xjf\{}'.format(i))
 if aa[1]=='.py':
     bb=os.path.split(r'E:\jiaoben\xjf\{}'.format(i))
     c.append(bb[1])
print(c)



#统计某个目录下有多少个目录文件，有多少个普通文件
a=(os.listdir())
b=0
c=0
for i in a:
   if os.path.isfile(i):
      c=c+1
   else:
       b=b+1
print(c)
print(b)
