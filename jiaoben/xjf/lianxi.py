# class Lei():     #class + 类名： 类名首字母必须大写
#     pass
# Lei()

#猫类
# class Cat:
#     #属性
#     #行为
#     self.fff='nihao'
#     def __init__(self):
#         pass
#     def  eat(self):
#         print('----吃-----')
#     def  drink(self):
#         print('-----喝-----')
#     def  shuijiao(self):
#         print('----睡觉-----')
    # def prinfo(self):
    #     print(self.color)
    # def prinfo(self):
    #     print(self.weiba)
    # def prinfo(self):
    #     print(self.tui)


# big_flower_cat=Cat()
# big_flower_cat.eat()
# big_flower_cat.drink()
# big_flower_cat.shuijiao()
# big_flower_cat.color='花色'
# # print(big_flower_cat.color)
# big_flower_cat.weiba='有'
# # print(big_flower_cat.weiba)
# big_flower_cat.tui='四条'
# big_flower_cat.prinfo()

# print(big_flower_cat.tui)

# #语言
# class Yuyan:
#     def  english(self):
#         print('----英文------')
#     def   chian(self):
#         print('-----中文-------')
#     def   deyu(self):
#         print('-----德语------')
# zhong_guo_ren=Yuyan()
# zhong_guo_ren.chian()
# zhong_guo_ren.daxiao='14亿'
# ying_guo=Yuyan()
# ying_guo.english()

# class People:
#
#     def __init__(self,n,a,w):
#         self.name=n
#         self.age=a
#         self.__weight=w
#     def __str__(self):
#       # return  str('年龄多少：')+str(self.age)
#       nl='年纪多少：'+str(self.age)
#       return  nl
#     # def prinfo(self):
#     #     print(self.name)
#     #     print(self.age)
#     #     print(self.__weight)
#     # def  speak(self):
#     #     print(("my name is %s,i age is %s")%(self.name,self.age))
# china=People('xjf',23,55)
# # china.prinfo()
# # china.speak()
# print(china)


# 烤地瓜
# class Sweetpotato:
#     def __init__(self):
#         self.cookedLevel=0
#         self.cookedString='生的'
#         self.condiments=[]
#     def __str__(self):
#         msg='地瓜的生熟程度: '+str(self.cookedString)
#         msg+='\n地瓜等级：'+str(self.cookedLevel)
#         msg+='\n添加佐料：'
#         if len(self.condiments)>0:
#          for i in self.condiments:
#             msg+=i+ ','
#          msg=msg.strip(',')
#         else:
#           msg+='当前没有佐料'
#         return msg
#     def cook(self,times):
#         self.cookedLevel+=times
#         if self.cookedLevel>8:
#             self.cookedString='烤成木炭'
#         elif self.cookedLevel>5:
#             self.cookedString='已经烤好'
#         elif self.cookedLevel>3:
#             self.cookedString='半生不熟'
#         else:
#             self.cookedString='生的'
#     def addcondiments(self,temp):
#         self.condiments.append(temp)
#
# digua=Sweetpotato()
# print(digua)
# digua.cook(4)
# digua.addcondiments('沙拉')
# print(digua)
# digua.cook(2)
# digua.addcondiments('番茄')
# print(digua)
# digua.cook(4)
# digua.addcondiments('玉米粒')
# print(digua)
#
# 继承
# class Stuend:
#     def __init__(self,name):
#         self.name='hello'
#     def haoshu(self):
#         print(120)
#     def hanshu1(self):
#         print(110)
# class  KdStuend(Stuend):
#     pass
# laowang=KdStuend()
# laowang.haoshu()
# laowang.hanshu1()
#
#
# 多态
# class Animal():  # 统一形态  动物
#     def talk(self):
#         pass
# class People(Animal): #动物第一个形态：人
#     def talk(self):
#         print('say hello')
# class Pig(Animal):  #动物第二个形态：猪
#     def talk(self):
#         print('hengheng')
# class  Dog(Animal):  #动物第三个形态：狗
#     def talk(self):
#         print('wangwang')
#
# People().talk()
# Pig().talk()
# Dog().talk()
#
# 方法重写
# class Student:
#     def hanshu(self):
#         print('nihao')
# class KdStudent(Student,):
#     def hanshu(self):
#         print('slhjoghjg')
# laowang=KdStudent()
# laowang.hanshu()

#存放家具
# #定义一个家的类
# class  Home:
#     def __init__(self,newarea): #area面积  containsIiems 家具
#         self.area=newarea
#         self.containsIiems=[]
#     def __str__(self):
#         msg='家当前可用面积为：'+str(self.area)+'平方米'
#         msg+='\n家里目前的家具有：'
#         if len(self.containsIiems)>0:
#             for i in self.containsIiems:
#                 msg+=i.name+','
#             msg=msg.strip(',')
#         else:
#             msg+='当前还没有家具'
#         return  msg
#     def additems(self,item):
#        if self.area>item.area:
#         self.containsIiems.append(item)
#         self.area-=item.area
# class Bed():# 床类
#     def __init__(self,newname,newarea):
#         self.name=newname
#         self.area=newarea
#     def __str__(self):
#         msg='床的名字：'+self.name
#         msg+='\n床的面积为：'+str(self.area)+'平方米'
#         return  msg
#
# bed=Bed('席梦思',35)
# home=Home(110)
# print(home)
# print(bed)
# home.additems(bed)
# print(home)



# class Deng():

# import  xlwt # 导入xlwt模块，只有写入的模块
# f=xlwt.Workbook(encoding='utf8') #设置excel文件的格式
# sheet1=f.add_sheet('nihao')  #给sheet文件改名字(添加标签页）
# for i in range(1,10):
#     for j in  range(1,i+1):
#      sheet1.write(i-1,j-1,'{}*{}={}'.format(i,j,i*j))  #'给一个表格添加内容，括号内是（行的位置，列位置，内容）
#
# f.save('a.xls')  #保存文件

#
'''
import xlrd
xr=xlrd.open_workbook('a.xls') #打开文件 ，其他路径需要加绝对路径
#1.通过索引来进入要操作的标签页
'''
'''
b=xr.nsheets#获取总共有多少个标签页
print(b)
sheet=xr.sheets()[0]#通过索引进入第一页,0代表第一页
hangshu=sheet.nrows#获取标签页有多少行
print(hangshu)
'''
#2通过名称来进入要操作的标签页
'''
name=xr.sheet_names()#获取所有标签页的名称
print(name)
sheet=xr.sheet_by_name('nihao')#进入nihao的标签页
b=xr.nsheets
print(b)
hangshu=sheet.nrows  #一共有多少行，n是统计行
print(hangshu)
hang3=sheet.row_values(2)#查找第三行的内容 ，row是行，2是第三行
print(hang3)
lie=sheet.ncols  #获取一共有多少列，n是统计列
print(lie)
lie3=sheet.col_values(2)  #查找第三列的内容，col是列，2是第三列
print(lie3)

hezi=sheet.cell(0,0).value#查找第一行第一列的内容(单元格的内容)
print(hezi)
'''

#复制文件并操作
# from  xlutils.copy import  copy
# import  xlrd
# yuan_file=xlrd.open_workbook('a.xls')#源文件打开 ，file:文件
# new_file=copy(yuan_file)#新文件复制源文件，只有写入功能，没有读取功能
# sheet=new_file.get_sheet(0)#新文件获取第一个标签页，（0）：下标位置；0是第一个标签页
# sheet.write(0,0,1111)
# new_file.save('a.xls')
# print(sheet)

#操作一 把文件的内容复制到表格中
#操作二 把表格的内容复制到文件中

#时间戳 （秒） 从公元1970年1月1日8点到现在所经过的时间秒
# import  time
# a=time.time()
# print(a)

#本地时间（现在的时间）
#
# import time
# a=time.localtime()#括号内可填数字
# print(a)



#本地时间
# import  time
# b=time.time()
# a=time.localtime(b)
# print(a)

# import  time
# a=time.gmtime()#utc时间  世界时间
# b=time.localtime()#本地时区的时间
# print(a)
# print(b)
# print(time.strftime('%Y-%m-%d %X',a))#%X = %H:%M:%S ：结果都是时分秒  a是世界时间
# print(time.strftime('%x %X',a))#%x =%Y-%m-%d   ：结果都是月/日/年
# print(time.strftime('%Y-%m-%d %H:%M:%S'))
# print(time.strftime('%Y-%m-%d',time.localtime()))#将本地时间的结构化时间转换成格式化时间
# print(time.strptime('2019/09/08 10:05:28','%Y/%m/%d %X'))#将格式化时间转化为结构化时间


# import time
# a=time.strftime('%Y-%m-%d %H:%M:%S:%W',time.localtime((2000)))
# print(a)

#元祖时间
# import time
# c=time.localtime()
# a=(2019,9,18,10,24,29,2,261,0)
# b=time.mktime(a)
# print(b)

#元祖时间
# import time
# a=time.localtime()
# b=time.mktime(a)
# print(b)


#休眠第一种方法
# from time import sleep
# for i in range(3):
#     sleep(1)   #休眠1秒再打印
#     print(i)
#休眠的第二种方法
# import time
# for i in range(3):
#    time.sleep(1)   #休眠1秒再打印
#    print(i)


#休眠开始时间-结束时间
# import time
# start=time.time() #开始时间
# for i in range(3):
#      time.sleep(3) #休眠3秒再打印
#      print(i)
# end=time.time()#结束时间
# print(end-start)






#冒泡排序
# a=[33,11,22,55,2]
# c=len(a)
# for i in range(0,c):    #拿i的位置和i后一位的位置做比较
#     for j in  range(i+1,c):
#       if a[i]>a[j]:
#         a[i],a[j]=a[j],a[i]
# print(a)

#冒泡排序
# a=[33,11,22,55,2]
# c=len(a)
# for i in range (c):     #将i与i的前一位做比较
#     for j in range(c-1):
#         if a[i]>a[j]:
#             a[j],a[i]=a[i],a[j]
# # print(a)

#输入十进制，转成十六进制
# a =[i for i in range(10)]+[chr(i)for i in range(97,103)]
# b = int(input('>>>'))
# f =[]
# while True:
#     d=b%16
#     b=b//16
#     f.append(a[d])
#     if b==0:
#         break
# f.reverse()
# print(f)

#连接内容
# a=['a','b']
# print(a)
# print(''.join(a))


#不用int 将字符串转换为整数（十进制）   赋值给新的变量
# b=0
# a='12344'
# a=a[::-1] #将数值反转（倒转）显示
#
# c=len(a)
# for i in range(c): #下标值
#     for j in range(10):#每位数值的范围（0，9）（个，十，白，千，万）
#      if str(j)==a[i]: #定义字符串j，把字符串a的内容赋值到f
#          b+=j*10**i  #字符串与数值无法做加减乘除运算
# print(b)
# print(type(b))

#反转
# a=[1,2,4,5]
# a=a[::-1]
# print(a)

#在b列表中添加 a的值，a的值来自于c的取值范围
# b=[]
# c=[i for i in range(10)]
# a=1
# b.append(c[a])
# print(b)


#输入三个数，求列数之和
# while True:
#
#     i =int(input("输入第一项"))
#     j =int(input("输入最后一项"))
#     z =int(input("输入公差"))
#     a = [i]
#     for s in range(i,j-1):
#      s=s+z
#      if s%2!=0:
#       a.append(s)
#     print(a)
#     print(sum(a))


#输入3个整数，用空格隔开，第一个数是首项，第二个数是末项，第三个数是公差，求该列数之和
# s=0
# i =list(input("输入三个数").split(' '))
# a=[int(i[0])]
# for s in range(int(i[1])-1):
#    s=s+(int(i[2]))
#    if s%2!=0:
#     a.append(s)
# print(a)
# print(sum(a))


# a=1  #首项数
# b=9   #末项数
# c=2   #公差
# s=0
# d=[1]
# for i in range(a,b-1):
#     s=i+c
#     if s%2!=0:
#       d.append(s)
# print(d)
# print(sum(d))
#水仙花数

# for i in range(100,1000):
#     a=i//100  #百位数   整除的数
#     b=i//10%10 #十位数   余数
#     c=i%10   #个位数     余数
#     if a**3+b**3+c**3==i:
#         print(i)







#阶乘之和
# 阶乘：1*2*3*4*5*.......
#阶乘之和：1*1+1*2+2*3+6*4+24*5+.....
# a=1
# sum=0
# for i in range(1,6):
#     a=a*i
#     sum=sum+a
# print(a)
# print(sum)





#去重
# a=[55,13,13,24,36]  #a列表中取其中一个数跟b列表所有的数，做对比，如果没有重复，添加到b列表
# b=[]
# c=len(a)
# for i in range(0,c):
#     if a[i] not in b :
#         b.append(a[i])
# print(b)




#猜大小
# c=3
#
# for j in range(1,10):
#     i = int(input("请输入数字："))
#     c = c - 1
#     if i ==j:
#         print('真棒猜对了')
#     elif c==0:
#         break
#     elif i>j:
#
#         print('猜大了','还剩下',c)
#     elif i < j:
#         print('猜小了','还剩下',c)





#查看文件
#桌面的hello.txt文件
# a=open(r'C:\Users\xjf\Desktop\hello.txt',mode='r',encoding='UTF-8')
# print(a.read())
#查看包中的文件
# b=open('e:\\jiaoben\\xjf\\today.py',mode='r',encoding='UTF-8')
# print(b.read())
#桌面新建一个2.txt文件
# a=open(r'C:\Users\xjf\Desktop\2.txt',mode='w',encoding='UTF-8')
# print(a)
#往桌面2.txt文件写入内容
# a=open(r'C:\Users\xjf\Desktop\2.txt',mode='w',encoding='UTF-8')
# print(a.write('111'))
# print(a.write('222'))
# a.close()
#往桌面2.txt文件写入九九乘法表
# a=open(r'C:\Users\xjf\Desktop\2.txt',mode='w',encoding='UTF-8')
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(a.write(('{}*{}={}'.format(i,j,i*j))))
#     a.write('\n')
# a.close()
#追加内容，不覆盖之前的内容
# a=open(r'C:\Users\xjf\Desktop\2.txt',mode='a',encoding='UTF-8')
# print(a.write('我爱你'))
# a.close()

#读取2.txt内容的一行的内容
# a=open(r'C:\Users\xjf\Desktop\2.txt',mode='r',encoding='UTF-8')
# print(a.readline())

#判断2.txt内容的开头
# a=open(r'C:\Users\xjf\Desktop\2.txt',mode='r',encoding='UTF-8')
# print(a.read().startswith('*'))


#with
# with open(r'C:\Users\xjf\Desktop\2.txt',mode='r',encoding='UTF-8')as e:
#  print(e.read())




#excl
#创建
# import xlwt
# file=xlwt.Workbook(encoding='utf8')
# sheet=file.add_sheet('nihao')
# for i in range(1,10):
#     for j in range(1,i+1):
#         sheet.write(i-1,j-1,'{}*{}={}'.format(i,j,i*j))
# file.save('aa.xls')

#查询
# import xlrd
# file=xlrd.open_workbook('aa.xls')
# sheet=file.nsheets
# print(sheet)
# name=file.sheet_names()
# print(name)
# sheet1=file.sheet_by_name('nihao')
# hang=sheet1.nrows
# print(hang)
# hang3=sheet1.row_values(2)
# print(hang3)
# lie=sheet1.ncols
# print(lie)
# lie3=sheet1.col_values(2)
# print(lie3)
# danyuange=sheet1.cell(0,0).value
# print(danyuange)

#追加复制
# from xlutils.copy import copy
# import xlrd
# yuan=xlrd.open_workbook('aa.xls')
# new=copy(yuan)
# sheet=new.get_sheet(0)
# sheet.write(0,0,'ok')
# new.save('aaa.xls')


#爬虫

# import requests
# import  re
# a='http://www.quanshuwang.com/book_9055.html' #定义网址变量
# b=requests.get(a)     #请求网址                 get: 请求方法的一种类型
# print( b)
# #接收响应内容第一种  text
# # c=b.text
# # print(c)   #查看的是网址的源代码（html代码）  是以文本的格式接收  缺点：中文是乱码
#
# #接收响应内容第二种   content  :以字节的方式接收
# c=b.content.decode('gbk')   #content 响应实体  gbk:网页的编码方式  decode:解码
# print(c)

import requests
import re
# a='https://5g.ifeng.com/'
# b=requests.get(a)
# print(b)
# c=b.content.decode('utf-8')
# print(c)

# #下载视频
# b="https://video.pearvideo.com/head/20190920/cont-1604362-14405643.mp4"
# a=requests.get(b)
# print(a)
# c=a.content
# print(c)
# with open('a.mp4','wb') as e :  #下载视频命名   wb:以字节方式写入  rd:以自己方式查看
#     e.write(c)
#
# #下载图片
# a='https://ss0.baidu.com/73t1bjeh1BF3odCf/it/u=1933589750,3172332897&fm=85&s=55A8BB5745424741062835700300C032'
# b=requests.get(a)
# print(b)
# c=b.content
# print(c)
# with open('tupian.jpg','wb')as e:
#     e.write(c)
# #


# import re
# a='wqe\nQfwq123qfQwqw'
# b=re.compile('q(.*?)q')         #结果只有数字     #括号内是过滤表达式
# # b=re.compile('q(.*?)q',re.S)  #结果没有数字
# c=b.findall(a)
# print(c)


#过滤4到4之间的内容
# a='4wqe\nQfwq123qfQwqw4'
# b=re.compile('q(.*?)q',re.S)  #不加？也可以 re.I 不区分大小写   \n换行符  ，S不排除换行符，I 排除换行符
# #贪婪模式，不排除换行符，非贪婪排除换行符
#
# # s=re.findall(b,a)      #表达式和字符串也可以直接写入括号内
# s=b.findall(a)
# print(s)
#获取小说网页第一章的文本内容
# import requests
# import re
# a='http://www.quanshuwang.com/book/0/269/78854.html'
# b=requests.get(a)
# c=b.content.decode('gbk')
# guolv=re.compile('&nbsp;&nbsp;&nbsp;&nbsp;(.*?)&nbsp;&nbsp;&nbsp;&nbsp;',re.S)
# ww=guolv.findall(c)
# for i in ww:
#    print(i.strip('(《》)<br />\r\n<br />\r\n'+'\n'))



# import requests
# import re
# import xlwt
# # for x in range(2):
# j=0
# for i in range(78861,78878):
#       j=j+1
#       i=i+j
#
#       a='http://www.quanshuwang.com/book/0/269/{}.html'.format(i)
#       b=requests.get(a)
#       hxcc=b.content.decode('gbk')
#
# with open('e:\\jiaoben\\xjf\\hang.txt',mode='w',encoding='utf-8')as e :
#  e.write(c)
# guolv = re.compile('&nbsp;&nbsp;&nbsp;&nbsp;(.*?)&nbsp;&nbsp;&nbsp;&nbsp;', re.S)
# ww = guolv.findall(c)
#
# for y in ww:
#         print(y.strip('(《》)<br />\r\n<br />\r\n') + '\n')


#JSON
#loads:反序列化（将JSON格式转换为python的字典格式）
import json



#（将JSON格式转换为python的字典格式）
# a=json.loads('{"result":{"data":12}}')
# # print(type(a))
# # print(a['result']['data'])

#将百度地图获取的某个内容写入到表格中
# import xlwt
# a = 'https://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=direct&pcevaname=pc4.1&qt=spot&from=webmap&c=333&wd=%E7%BE%8E%E9%A3%9F&wd2=&pn=0&nn=0&db=0&sug=0&addr=0&pl_data_type=cater&pl_sub_type=%E9%A4%90%E9%A6%86&pl_price_section=0%2C%2B&pl_sort_type=data_type&pl_sort_rule=0&pl_discount2_section=0%2C%2B&pl_groupon_section=0%2C%2B&pl_cater_book_pc_section=0%2C%2B&pl_hotel_book_pc_section=0%2C%2B&pl_ticket_book_flag_section=0%2C%2B&pl_movie_book_section=0%2C%2B&pl_business_type=cater&pl_business_id=&da_src=pcmappg.poi.page&on_gel=1&src=7&gr=3&l=13&rn=50&tn=B_NORMAL_MAP&auth=GTNwIA8CC4OBdzNRxDSBe2JzAIJZe7bFuxHLTVBEEVLtykiOxAXXwcvY1SGpuztFHhxQ7E%40Z5Z3%40wWv1cv3uVtGccZcuVtPWv3Guxt58Jv7uUvhgMZSguxzBEHLNRTVtcEWe1GD8zv7u%40ZPuVteuVtegvcguxHLTVBEEVEthl44yYxrZZWuV&u_loc=12725748,4113272&ie=utf-8&b=(13361384.693561113,3374406.30645;13405096.693561113,3378182.30645)&t=1569034406704'
# h=requests.get(a)
# neirong=h.text
# geshi=json.loads(neirong)
# f = xlwt.Workbook(encoding='utf8')
# sheet1 = f.add_sheet('nihao')
# i=0
# while True:
#
#     try:
#         tuqu = geshi['content'][i]['addr']
#
#         sheet1.write(i, 0, tuqu)
#         i = i + 1
#     except:
#      break
# f.save('1.xls')


#将百度地图获取的某个内容写入到txt文件中
import xlrd
import xlwt
# a='https://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=direct&pcevaname=pc4.1&qt=spot&from=webmap&c=333&wd=%E7%BE%8E%E9%A3%9F&wd2=&pn=0&nn=0&db=0&sug=0&addr=0&pl_data_type=cater&pl_sub_type=%E9%A4%90%E9%A6%86&pl_price_section=0%2C%2B&pl_sort_type=data_type&pl_sort_rule=0&pl_discount2_section=0%2C%2B&pl_groupon_section=0%2C%2B&pl_cater_book_pc_section=0%2C%2B&pl_hotel_book_pc_section=0%2C%2B&pl_ticket_book_flag_section=0%2C%2B&pl_movie_book_section=0%2C%2B&pl_business_type=cater&pl_business_id=&da_src=pcmappg.poi.page&on_gel=1&src=7&gr=3&l=13&rn=50&tn=B_NORMAL_MAP&auth=GTNwIA8CC4OBdzNRxDSBe2JzAIJZe7bFuxHLTVBEEVLtykiOxAXXwcvY1SGpuztFHhxQ7E%40Z5Z3%40wWv1cv3uVtGccZcuVtPWv3Guxt58Jv7uUvhgMZSguxzBEHLNRTVtcEWe1GD8zv7u%40ZPuVteuVtegvcguxHLTVBEEVEthl44yYxrZZWuV&u_loc=12725748,4113272&ie=utf-8&b=(13361384.693561113,3374406.30645;13405096.693561113,3378182.30645)&t=1569034406704'
# h=requests.get(a)
# neirong=h.text
# geshi=json.loads(neirong)
# i=0
# while True:
#     try:
#
#          with open('e:\\jiaoben\\xjf\\hang.txt', mode='a', encoding='utf-8')as e:
#              tuqu = geshi['content'][i]['addr']
#              e.write(tuqu+'\n')
#              i = i + 1
#
#
#     except:
#           break


#将百度地图获取的某个内容显示出来
import requests
import re
# url='https://map.baidu.com/?qt=subwayscity&t=1569031875980'
# a=requests.get(url)
# c=a.text
# result=json.loads(c)
# i=0
# while True:
#    try:
#         tiqu=result['subways_city']['cities'][i]['cn_name']
#         print(tiqu)
#         i+=1
#    except:
#        break



#智联网上获取职位和工资，写入excel表格中
import json
import  requests
import  re
url='https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=530&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&=0&at=c8403515320f488dbf133e51db833eeb&rt=2848e76c570848e3b97cfe15c8b5bbeb&_v=0.56427094&userCode=1050815528&x-zp-page-request-id=abf592cbd3e34824886333e76ec70f7d-1569206084730-952313&x-zp-client-id=16776917-1567-4d20-810f-203d3885338d'
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
huoqu=requests.get(url=url,headers=header)
geshi=huoqu.text
jieguo=json.loads(geshi)
i=0
f=xlwt.Workbook('utf8')
sheet=f.add_sheet('nihao')
while True:
     try:
               tiqu=jieguo['data']['results'][i]['jobName']
               tiqu2=jieguo['data']['results'][i]['salary']
               sheet.write(i,0,tiqu)
               sheet.write(i,1,tiqu2)
               i=i+1



     except:
       break

f.save('2.xls')


#将txt的内容写入到表格里

# with open('e:\\jiaoben\\xjf\\hang.txt',mode='r',encoding='utf-8')as  e:
#     c= e.readlines()
#     file=xlwt.Workbook(encoding='utf8')
#     sheet=file.add_sheet('nihao')
#
#     for i in range(len(c)):
#         sheet.write(i, 0, c[i])
# file.save('1.xls')
xc
#把表格的内容写入到txt
# file=xlrd.open_workbook('1.xls')
# sheet=file.sheet_by_name('nihao')
# c=sheet.nrows
#
# with open('e:\\jiaoben\\xjf\\hh.txt',mode='w',encoding='utf-8')as e :
#     for i in range(c):

#
#         for j in c:
#           j=str(j)
#           e.write(j)

#取小说网第一页的所有小说名字，写入到txt文件
# url='http://www.quanshuwang.com/'
# header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
# huoqu=requests.get(url=url,headers=header)
# geshi=huoqu.content.decode('gbk')
# guolv=re.compile('title="(.*?)" class="msgBorder"><img src="(.*?)" width="120" height="150">')
# gl=guolv.findall(geshi)
# c=[]
# for i in range(len(gl)):
#   a=gl[i][0]
#   c.append(a)
#   with open('e:\\jiaoben\\xjf\\3.txt',mode='w',encoding='utf-8')as e:
#
#       for j in range(len(c)):
#        e.write(c[j]+'\n')

#将小说网的的第一页的小说名字，写入到表格
# url='http://www.quanshuwang.com/'
# header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
# huoqu=requests.get(url=url,headers=header)
# geshi=huoqu.content.decode('gbk')
# guolv=re.compile('title="(.*?)" class="msgBorder"><img src="(.*?)" width="120" height="150">')
# gl=guolv.findall(geshi)
# c=[]
# f=xlwt.Workbook(encoding='utf-8')
# sheet=f.add_sheet('nihao')
# for i in range(len(gl)):
#   a=gl[i][0]
#   c.append(a)
# for j in range(len(c)):
#           sheet.write(j,0,c[j])
# f.save('3.xls')


#查找公司，职位，工资等内容写入到表格中
# url='https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=530&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%A1%8C%E6%94%BF%E4%BA%BA%E4%BA%8B&kt=3&=0&at=c8403515320f488dbf133e51db833eeb&rt=2848e76c570848e3b97cfe15c8b5bbeb&_v=0.03937636&userCode=1050815528&x-zp-page-request-id=ccee1853768a4ea0a3a3daf2f9b08209-1569243656813-816233&x-zp-client-id=16776917-1567-4d20-810f-203d3885338d'
# header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
# huoqu=requests.get(url=url,headers=header)
# geshi=huoqu.text
# neirong=json.loads(geshi)
# c=len(neirong)
# i=1
# f=xlwt.Workbook(encoding='utf8')
# sheet=f.add_sheet('nihao')
# sheet.write(0,0,'公司名称')
# sheet.write(0,1,'工资')
# sheet.write(0,2,'职位')
# while True:
#      try:
#
#         shuju=neirong['data']['results'][i]['jobName']
#         shuju1=neirong['data']['results'][i]['salary']
#         shuju2=neirong['data']['results'][i]['company']['name']
#
#         sheet.write(i,0,shuju2)
#         sheet.write(i,1,shuju1)
#         sheet.write(i,2,shuju)
#         # print('招聘公司：'+shuju2+'\n'+'职位：'+shuju+'\t'+'工资：'+shuju1)
#
#         i=i+1
#
#      except:
#       break
# f.save('2.xls')


#数据库
import  pymysql   #用来连接与操作数据库
conn=pymysql.connect(host='192.168.2.99',port=3306,user='root',passwd='123456') #数据库的账号，密码  connect:连接
cursor=conn.cursor()#创建游标：得到东西保存下来(获取)    cursor:光标
#执行sql语句
cursor.execute('create database  pachong;')  #创建一个数据库pa     execute:执行  括号内是执行的内容
cursor.execute('show databases;')
conn.commit()   #提交操作  (提交数据)
conn.close()     #关闭     （断开连接）


#fetchmany 与 fetchall 的用法
import  pymysql   #用来连接与操作数据库
conn=pymysql.connect(host='192.168.2.99',port=3306,user='root',passwd='123456',db='pachong')
a=conn.cursor()
a.execute('show databases;')
print(a.fetchmany(3))   #括号里不填数字，默认只显示结果的第一个，3是显示结果的前面3个   （查询前面3个数据库）
a.execute('show tables;')
print(a.fetchall())     #显示上一个语句的结果  (查询所有的表)


#嵌套函数
a=int(input("输入数字："))
if a%2==0:
    if a%3==0:
     print('hello word')
    else:
        print('hello')
elif a%3==0:
    print('word')
else:
    print(123)

#最大的放第一位，最小的放最后，中间的不变
    # a=list(input('输入：').split(','))
    # c=max(a)
    # d=min(a)
    # xb=a.index(c)
    # xb1=a.index(d)
    # c=len(a)
    # a[0],a[xb]=a[xb],a[0]
    # a[xb1],a[c-1]=a[c-1],a[xb1]
    # print(a)

#有一个顺序的列表，随意属于数字进入，放入正确的位置
# b=int(input('请输入：'))
# a=[1,3,5,7,9]
# a.append(b)
# c=len(a)
# for i in range(0,c):
#     for j in range(i+1,c):
#
#         if a[j]<a[i]:
#            a[j],a[i]=a[i],a[j]
# print(a)

#将4位数，写入不重复的3位数
# b=(input('输入数值'))
# c=len(b)
# for i  in range(c):
#  for j in range(c):
#      for a in range(c):
#          if b[i]!=b[j]!=b[a]:
#              print(b[i],b[j],b[a])


#21.	统计.Cpp文件有多少行，统计的时候将文件中的空行、单行注释的行去除
with open('e:\\jiaoben\\xjf\\hh.txt', mode='r', encoding='utf-8')as e:
    c = e.readlines()
    b = len(c)

for i in range(b):
    if c[i] == '\n':
        b = b - 1
    elif c[i].startswith('#'):
        b = b - 1
print(b)

#1到100的数相加
sum=0
i=0
while i <100:
     i=i+1
     sum=sum+i
print(sum)


# def hanshu(a=10,b=10):  #默认写入写a=0
#     print(a)
# hanshu(20)#调用函数写入值20
#         #调用函数最后的结果是写入的值20
#
# def  hanshu(**kwargs):#kwargs 是可变长参数 ，可以有多个值
#     print(kwargs)
# hanshu(name=123,age=456)#调用函数写入键值对
# #以字典的格式显示,结果是{'name':'123,'age':'456'}

#return
def hanshu(x):
    a=sum(range(x))
    return a,100,101 # a是函数的值，100，101，是return调用的值
    #return可返回多个值，（可赋值多个值）
print(hanshu(10))#结果（45,100,101）

#显示1到9的累加
def hanshu(x):
    a = sum(range(x))
    print(a)
hanshu(10)

#显示1到100的累加
def hanshu(x):
    a = sum(range(x))
    print(a)
hanshu(101)

#不用int 变成整形
a = '123456'
a = a[::-1]
c = len(a)
sum = 0
def hanshu(sum):
    for i in range(c):
        for j in range(10):
            if str(j)==a[i]:
                j=j*10**i
                sum=sum+j
    print(sum)
hanshu(sum)


#用函数的方法，输入一个数，放入正确的位置
b = int(input('请输入：'))
def hanshu(b):
    a=[1,3,5,7,9]
    a.append(b)
    c=len(a)
    for i in range(0,c):
        for j in range(i+1,c):

            if a[j]<a[i]:
               a[j],a[i]=a[i],a[j]
    print(a)
hanshu(b)

#一个因数之和等于他本身

for i in range(1,1001):
    sum = 0
    for j in range(1,i):
        if i%j==0 :
           sum=sum+j
    if i==sum:
         print(i)


def hanshu(x):
    for i in range(1,x):
        sum = 0
        for j in range(1,i):
            if i%j==0 :
               sum=sum+j
        if i==sum:
             print(i)
hanshu(1001)



#匿名函数
a=lambda x,y :x+y
print(a(2,3))


# a=lambda :print('hello')
# a()

#列表推导式
#变量名=[结果的变量 控制语句]
a=[x for x in range(20) if x>7]
print(a)
#九九乘法表
a=['{}*{}={}'.format(i,j,i*j)    for i in range(10) for j in range(1,i+1)]
print(a)


#所有的因数
a=[j for i in range(100) for j in range(1,i)  if i%j==0 ]

print(a)

#复制图片
f=open('tupian.jpg','rb')
bb=f.read()
print(bb)
ff=open('qwe.jpg','wb')
ff.write(bb)


#以二进制的方式写入到txt中
f=open('hh.txt','rb')  #第一步：打开文件 ，hh,txt文件有中国两个字
bb=f.read()
print(bb) #读取txt文件中国两个字的字节
#第二步：把文件中的中国删掉
f=open('hh.txt','wb') #打开文件
f.write(b'\xe4\xb8\xad\xe5\x9b\xbd')#写入中国的字节


#导入函数
from hhhh import hanshu  # from 文件名 import 函数名
hanshu()

from xjf.hhhh import hanshu   #from  包名.文件名 import 函数名
hanshu()
#如果 在源文件里面有if __name__=='__main__'，结果只会显示一遍
#如果没有判断语句，源文件有调用函数结果会显示2遍
#如果没有判读语句，源文件没有调用函数结果只显示1遍
#如下：源文件
def hanshu():
    a = sum(range(101))
    print(a)
if __name__=='__main__':#判断当前被执行的文件是不是本文件 ，如果是本文件，显示结果，反之不显示结果
hanshu()


#显示文本中13行到18行的内容
with open('e:\\jiaoben\\xjf\\hh.txt',mode='r',encoding='utf-8')as e:
     c=e.readlines()
     for i ,j in enumerate (c):
        while 19> i >12:
            print(i,j)
            break

#文本中开头带有abc的行
with open('e:\\jiaoben\\xjf\\hh.txt',mode='r',encoding='utf-8')as e:
   c=e.readlines()
   for i ,j in enumerate(c):
     if j.startswith('abc'):
         print(j)

# 文本中带有abc的行
with open('e:\\jiaoben\\xjf\\hh.txt',mode='r',encoding='utf-8')as e:
   c=e.readlines()
   for i in range(len(c)):
       if 'abc' in c:
           print(c[i])

#写入十行的内容
with open('e:\\jiaoben\\xjf\\hh.txt', mode='w', encoding='utf-8')as e:
 for i in range(10):
     e.write('重生之贼行天下'+'\n')

#一个函数，传两个参数a,b，a是数组，b是一个数字，找出a数组中两数只和等于b，打印出来这两个数
def hanshu(a,b):
   for i in a:
       for j in a:
           if i+j==b:
               print(i,j)
hanshu([1,2,3,4,5],7)


#打印列表中所有第一大和第二大的数
a=[4,55,55,62,62,62,1]
b=[]
da=max(a)
c=a.count(da)
z=0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]<a[j]:
            a[i],a[j]=a[j],a[i]
            if a[i] == da:
               b.append(a[i])
while z < c:
     a.remove(da)
     z=z+1
da1=max(a)
for i in range(len(a)):
    if a[i]==da1:
       b.append(a[i])
print(b)


#向左移一位

a = input('>>>').split(',')
b = len(a)
for i in range(0,b-1):
    a[i],a[i+1] = a[i+1],a[i]
print(a)

#将表格中的内容写入到txt
file=xlrd.open_workbook('2.xls')
sheet=file.sheet_by_name('nihao')
with open('e:\\jiaoben\\xjf\\hh.txt',mode='w',encoding='utf-8')as e:
    hang = sheet.nrows
    for i in range(hang):
        hang1=sheet.row_values(i)
        for x in hang1:
            x=str(x)
            e.write(x)
        e.write('\n')


#把txt文本的内容放入表格中，以.作为分隔符，分段，写入表格，一段代表一列
xw = xlwt.Workbook(encoding='utf-8')
sheet = xw.add_sheet('nei')
with open('hh.txt','r',encoding='utf-8') as a:
    b = a.readlines()
    for i in range(len(b)):
        k = b[i].split('.')
        for j in range(len(k)):
            sheet.write(i,j,k[j])
xw.save('b.xls')


#将导入的内容，根据表格的形式显示，有几行几列的样子，展现出来
file=xlrd.open_workbook('2.xls')
sheet=file.sheets()[0]
hang=sheet.nrows
with open('e:\\jiaoben\\xjf\\hh.txt',mode='w',encoding='utf-8')as e:
    for i in range(hang):
        hang1=sheet.row_values(i)
        for j in hang1:
            j=str(j)+'\n'
            j=j.split('\n')
            j='\t\t\t\t'.join(j)
            e.write(j)
        e.write('\n')


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





#连接数据库
class Mysql_learn(object):
    def __init__(self):#连接数据库
      self.conn=pymysql.connect(host='192.168.2.99',port=3306,user='root',passwd='123456')#host:数据库所在的主机I
      self.su=self.conn.cursor()#设置游标:执行动作，操作，能操控对象。所在位置。（类似光标，光标在哪里就在哪里操作）
    def cao_zuo(self): #执行sql语句,只能是字符串
       self.su.execute('show databases;')
       self.su.execute('use yyy;')
       for i in range(10):
        # self.su.execute(('insert into  jj values ({},{},{},{},{},{});').format(i,i,i,i,i,i))
        self.su.execute('select * from jj;')
        print(self.su.fetchall())
        # self.conn.commit() #提交数据，只有在对某个表的数据进行添加（insert）、删除（delete）、修改(alter)，等操作时使用
           # print(self.su.fetchall())#读取上一个执行语句的结果，读取所有结果
           # print(self.su.fetchmany(3))#读取多条内容，默认是一条内容
           # print(self.su.fetchone())#每次只读取一条内容
           # self.conn.close()#断开连接
d=Mysql_learn()
d.cao_zuo()



#查询有多少个数据库
class Shuju(object):
    def __init__(self):
        self.conn=pymysql.connect(host='192.168.2.99',port=3306,user='root',passwd='123456')
        self.you=self.conn.cursor()
    def zhixing(self):
        self.you.execute('show databases;')
        print(self.you.fetchall())

b=Shuju()
b.zhixing()


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


#判断是否是回文字符串
a=(input('输入：'))
b=a[::-1]
c=len(a)
for  i in range(c):

      if a[i]==b[i] :

        if a == b :
         print('是回文字符串')
         break
      else:
          break


 #回文的第二种方法
while True:
    a = input('输入的字符串')
    c = list(a)
    b = list(reversed(c))
    if b==c:
        print('回文')
    else:
        print('不是回文')

 #如果一个数 只能被3整数的输入word
 #如果一个数，不能被2和3整除的输入123
 #如果一个数，能被2整除，又能被3整除，输入hello word
 #如果一个数，能被2整数，但是不能被3整除，输入hello
a=int(input("输入数字："))
if a%2==0:
    if a%3==0:
     print('hello word')
    else:
        print('hello')
elif a%3==0:
    print('word')
else:
    print(123)


#输入一个日期，（例如 2019-09-08）判断是否是润年，今天是一年中的第几天，这一天是周几
import time
import datetime

a=(input('输入日期：').split('-'))
b=int(a[0])
c=int(a[1])
x=int(a[2])
jj=[]
sum=0
if b%4==0 and b%100!=0:
    print('是闰年')
elif b%400==0:
    print('是闰年')
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i in range(x):
   sum=sum+days[i]
anyday=datetime.datetime(b,c,x).strftime("%w")
print('是一年中的第',sum,'天','一周中的星期',anyday)


#第二种方法
a =['星期一','星期二','星期三','星期四','星期五','星期六','星期日']
b = input('输入日期：')
c=time.strptime(b,'%Y-%m-%d')
if c.tm_year%4==0 and c.tm_year%100!=0 or c.tm_year%400==0:
    print(c.tm_year,'年是闰年')
else:
    print(c.tm_year,'年是平年')
print(c.tm_year,'年',c.tm_mon,'月',c.tm_mday,'日','是一年的第',c.tm_yday,'天','是一周中的',a[c.tm_wday])




#将txt文本的内容写入到数据库的表里（子母和中文必须在文本加英文引号）  （只有一个字段的内容）
class Shuju(object):
    def __init__(self):
       self.conn=pymysql.connect(host='192.168.2.99',port=3306,user='root',passwd='123456')
       self.you=self.conn.cursor()
    def cao_zuo(self):
        self.you.execute('use yyy;')
        with open('q.txt',mode='r',encoding='utf-8')as e:
            c=e.readlines()
        for i in range(len(c)):
                self.you.execute(('insert into xu values({})').format(c[i]))
        self.conn.commit()
a=Shuju()
a.cao_zuo()

#爬虫小说1到10页
import requests
import re
j=9674263
for i in range(10):
    j=j+1
    url='http://www.quanshuwang.com/book/9/9055/{}.html'.format(j)
    header={'Use-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
    huoqu=requests.get(url=url,headers=header)
    geshi=huoqu.content.decode('gbk')
    guolv=re.compile('&nbsp;&nbsp;&nbsp;&nbsp;(.*?)&nbsp;&nbsp;&nbsp;&nbsp;',re.S)
    gl=guolv.findall(geshi)
    for i in gl:
       print(i.strip('<br />\r\n<br />\r\n')+'\n')

#paramiko ,封装了ssh协议，主要用于远程控制
import  paramiko
# #创建ssh客户端
# ssh123=paramiko.SSHClient()
# # #将第一次连接的主机跳过验证，并添加到know_host文件中   know_host文件存放了可以远程的主机IP地址
# ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy())  #跳过进入host文件查看,如果没有这句，会报错。
#missing :遗漏   policy:系统，信息  autaddpolicy :自动添加系统
# ssh123.connect(hostname='192.168.2.99',port=22,username='xjf',password='123456')  #连接到linux系统
#
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

#将数据库的内容传入表格
class Shuju(object):
    def __init__(self):
        self.conn=pymysql.connect(host='192.168.2.99',port=3306,user='root',passwd='123456')
        self.you=self.conn.cursor()
    def zhixing(self):
        c=[]
        self.you.execute('use yyy;')
        self.you.execute('select * from jj;')
        a=self.you.fetchall()
        h=len(a[0])
        for i in (a[0]):
         c.append(i)
         file=xlwt.Workbook(encoding='utf8')
         sheet=file.add_sheet('nihao')
         for j in range(len(c)):
          sheet.write(0,j,c[j])
        file.save('5.xls')
b=Shuju()
b.zhixing()


无限输入sql语句



import  socket
#tcp协议 通信
#服务器端
#创建一个套接字（创建一个有接收能力和发送能力的对象）
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#绑定IP地址和端口号,以元祖的形式
s.bind(('192.168.1.10',50))
#监听,启用服务器以接受连接
s.listen(3)#数字代表最大的等待数
while True:
    #接收请求
    client,addr=s.accept()   #addr:接收   accept:接收
    #client变量：建立客户端连接的信息
    #addr变量：客户端的ip地址和端口号
    recive=client.recv(1024)
    #recive变量：接收客户端发送的请求最大1024个字节    recv:接收数据
    print(recive.decode('utf8'))  #将接收过来的信息解码打印
    reponse=input('请响应：')   #将输入的响应内容
    client.send(reponse.encode('utf8'))#将输入的内容响应内容发送   send:发送
    client.close()



    # 客户端
    # 客户端不需要绑定IP和监听
import socket
import socket

while True:  # 必须一直处于运行的状态
        # 创建一个套件
        sock = socket.socket()
        # 客户端不需要绑定IP地址，但是连接服务器
        sock.connect(('192.168.1.10', 50))
        # 发送请求
        # 输入请求的内容
        message = input('请输入请求内容：')
        # 发送请求的内容
        sock.send(message.encode('utf8'))
        # 接收服务器的响应
        recive = sock.recv(1024)
        print(recive.decode('utf8'))
        # 断开连接
        sock.close()


#下载到文件夹
url='http://www.quanshuwang.com/list/5_1.html'
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
huoqu=requests.get(url=url,headers=header)
geshi=huoqu.content.decode('gbk')
guolv=re.compile('src="http(.*?)" alt="(.*?)"',re.S )
gl=guolv.findall(geshi)

for i in range(len(gl)):
    new_url='http'+gl[i][0]
    mz=gl[i][1]
    huoqu1=requests.get(url=new_url,headers=header)
    with open(r'C:\Users\xjf\Desktop\333\{}.jpg'.format(mz),'wb')as e :
        for i in huoqu1:
            e.write(i)