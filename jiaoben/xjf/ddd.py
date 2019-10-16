import json
# a=json.loads('{"result":{"data":12}}')
# # print(type(a))
# # print(a['result']['data'])


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


# head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}

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




#把txt的内容写入到表格中
# i=0
# import xlwt
# file=xlwt.Workbook('utf8')
# sheet=file.add_sheet('nihao')
# with open('e:\\jiaoben\\xjf\\hang.txt',mode='r',encoding='utf-8')as e:
#  a=e.readlines()
#  b=len(a)
#  c = e.readline(b)
#  for i in range(b):
#
#     sheet.write(i,0,c)
#
#     print(sheet)
#
# file.save('qq.xls')




#
# a='https://movie.douban.com/chart'
# b=requests.get(a)
# qin=b.content.decode('utf-8')
# # geshi=json.loads(qin)
# tuqu=re.compile(' <img src=(.*?).jpg',re.I)
# w=tuqu.findall(qin)
# for i in w:
#     i=i+'.jpg'
#     s=i.strip('"')
#     print(s)
#     a1 = requests.get(s)
#     b1 = a1.content
#     print(b1)
#
# with open(r'C:\Users\xjf\Desktop\333',mode='w',encoding='utf-8') as e :
#  for j in range(1,len(i)+1):
#   with open('{}'+'.jpg'.format(i),'')as p :
#    p.write(b1)
#    e.write(b1)
# print(b1)


#
# x=[]
# a='http://www.quanshuwang.com/book_9055.html?tdsourcetag=s_pcqq_aiomsg'
# header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
# b=requests.get(a)
# geshi=b.content.decode('gbk')
# guolv=re.compile(r'<li><a href="http://www.quanshuwang.com/book_.*?title=.*?><img onerror=.*?src="(.*?)" width="111px;',re.S)
# s=guolv.findall(geshi)
# z=x.extend(x)
# for i,j in enumerate(s):
#    new_url = j
#    new_b = requests.get(new_url)
#    with open(r'C:\Users\xjf\Desktop\333\{}.jpg'.format(i),'wb')as f:
#        for l in new_b:
#          f.write(l)

#r'<li><a href="http://www.quanshuwang.com/book_.*?title=(.*?)><img onerror=.*?src="(.*?)"width="111px;',re.S
#r'<li><a href="http://www.quanshuwang.com/book_.*?title="(.*?)"><img onerror=.*?src="(.*?)" width="111px;',re.S

#加个休眠时间，不然会被封  请求加个休眠时间
import json
import  requests
import  re
# # url='https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=530&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&=0&at=c8403515320f488dbf133e51db833eeb&rt=2848e76c570848e3b97cfe15c8b5bbeb&_v=0.56427094&userCode=1050815528&x-zp-page-request-id=abf592cbd3e34824886333e76ec70f7d-1569206084730-952313&x-zp-client-id=16776917-1567-4d20-810f-203d3885338d'
# # header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
# # huoqu=requests.get(url=url,headers=header)
# # geshi=huoqu.text
# # jieguo=json.loads(geshi)
# # i=0
# # f=xlwt.Workbook('utf8')
# # sheet=f.add_sheet('nihao')
# # while True:
# #      try:
# #                tiqu=jieguo['data']['results'][i]['jobName']
# #                tiqu2=jieguo['data']['results'][i]['salary']
# #                sheet.write(i,0,tiqu)
# #                sheet.write(i,1,tiqu2)
# #                i=i+1
# #
# #
# #
# #      except:
# #        break
# #
# # f.save('2.xls')



#1到5页的内容的职位和工资显示i出来
# from  time import sleep
# header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
# j=0
# for i in range(1,6):
#     i=90*i
#     url = 'https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=90&cityId=530&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&=0&at=c8403515320f488dbf133e51db833eeb&rt=2848e76c570848e3b97cfe15c8b5bbeb&_v=0.56427094&userCode=1050815528&x-zp-page-request-id=abf592cbd3e34824886333e76ec70f7d-1569206084730-952313&x-zp-client-id=16776917-1567-4d20-810f-203d3885338d'.format(i)
#     huoqu=requests.get(url=url,headers=header)
#     geshi=huoqu.text
#     neirong=json.loads(geshi)
#     while True:
#         try:
#             shuju=neirong['data']['results'][j]['jobName']
#             shuju1=neirong['data']['results'][j]['salary']
#             sleep(0.5)
#             print(shuju+'工资：'+shuju1)
#             j=j+1
#
#         except:
#             break


#从小说网找到图片和名字，下载到文件夹里


# url='http://www.quanshuwang.com//'
# header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
# huoqu=requests.get(url=url,headers=header)
# a=huoqu.content.decode('gbk')
#
# guolv=re.compile(r'target="_blank" href="http://www.quanshuwang.com/book_.*?" title="(.*?)" class="msgBorder"><img src="(.*?)" width="120"',re.S)
# b=guolv.findall(a)
#
# for i in range(len(b)):
#     new_url=b[i][1]
#     bt=b[i][0]
#
#     ww = requests.get(url=new_url, headers=header)
#     with open(r'C:\Users\xjf\Desktop\333\{}.jpg'.format(bt), 'wb')as e:
#
#         for j in ww:
#          e.write(j)










# url='http://www.quanshuwang.com/book/9/9055/9674264.html'
# header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
# huoqu=requests.get(url=url,headers=header)
# s=huoqu.content.decode('gbk')
# guolv=re.compile('&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />\r\n<br />\r\n&nbsp;&nbsp;&nbsp;&nbsp;',re.S)
# gl=guolv.findall(s)
# for i in gl:
#     print(i+'\n')
#     with open('e:\\jiaoben\\xjf\\xiaoshuo.txt', mode='a', encoding='utf-8')as e:
#      e.write(i+'\n')

# url='http://www.quanshuwang.com/list/11_1.html'
# header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
# huoqu=requests.get(url=url,headers=header)
# geshi=huoqu.content.decode('gbk')
# guolv=re.compile('src="http(.*?)" alt="(.*?)"',re.S)
# gl=guolv.findall(geshi)
# print(gl)
#
# for j in range(len(gl)):
#     new_url='http'+gl[j][0]
#     mz=gl[j][1]
#     print(new_url)
#     huoqu1=requests.get(url=new_url,headers=header)
#
#     with open(r'C:\Users\xjf\Desktop\333\{}.jpg'.format(mz),'wb')as e :
#         for i in huoqu1: 将请求的图片，一个一个的写入到文件夹中
#             e.write(i)

# url='http://www.quanshuwang.com/list/5_1.html'
# header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
# huoqu=requests.get(url=url,headers=header)
# geshi=huoqu.content.decode('gbk')
# guolv=re.compile('src="http(.*?)" alt="(.*?)"',re.S )
# gl=guolv.findall(geshi)
#
# for i in range(len(gl)):
#     new_url='http'+gl[i][0]
#     mz=gl[i][1]
#     huoqu1=requests.get(url=new_url,headers=header)
#     with open(r'C:\Users\xjf\Desktop\333\{}.jpg'.format(mz),'wb')as e :
#         for i in huoqu1:
#             e.write(i)

# #把表格的内容写入到txt
# file=xlrd.open_workbook('1.xls')
# sheet=file.sheet_by_name('nihao')
# c=sheet.nrows
#
# with open('e:\\jiaoben\\xjf\\hh.txt',mode='w',encoding='utf-8')as e :
#     for i in range(c):
#         c = sheet.row_values(i)
#
#         for j in c:
#           j=str(j)
#           e.write(j)


#第一步分析网址的变化
#第二步分析网络源代码，通过正则表达式过滤出想要的内容
#第三步根据过滤出来的内容，保存
# class Douban(object):
#
#     def qing_qiu(self,page):
#
#        url=''
#        header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
#        #发送请求，并将请求结果赋值给res
#        res=requests.get(url=url,headers=header)
#        #读取结果
#        h=res.content.decode('utf-8')
#         return h
#     def   guo_lv(self,html):
#       patt=re.compile()



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

# import  pymysql   #用来连接与操作数据库
# conn=pymysql.connect(host='192.168.2.99',port=3306,user='root',passwd='123456') #数据库的账号，密码  connect:连接
# cursor=conn.cursor()#创建游标：得到东西保存下来(获取)    cursor:光标
# #执行sql语句
# # cursor.execute('create database  pachong;')  #创建一个数据库pa     execute:执行  括号内是执行的内容
# # cursor.execute('show databases;')
# # conn.commit()   #提交操作  (提交数据)
# # conn.close()     #关闭     （断开连接）


# import  pymysql   #用来连接与操作数据库
# conn=pymysql.connect(host='192.168.2.99',port=3306,user='root',passwd='123456',db='pachong')
# a=conn.cursor()
# # cursor.execute('create table xjf(name char(20));')
# a.execute('show databases;')
# print(a.fetchmany(3))   #括号里不填数字，默认只显示结果的第一个，3是显示结果的前面3个
# # print(a.fetchall())   #fetchall执行上一句语句的结果
#
# # # a.execute('show tables;')
# conn.commit()
# conn.close()


# f=xlrd.open_workbook('3.xls')
# sheet=f.sheet_by_name('nihao')
# a=sheet.nrows
# with open('e:\\jiaoben\\xjf\\hh.txt',mode='w',encoding='utf8')as e :
#     for i in range(a):
#         b=sheet.row_values(i)
#         print(b)
#         for j in b:
#
#          e.write(j +'\n')



# a=int(input("输入数字："))
# if a%2==0:
#     if a%3==0:
#      print('hello word')
#     else:
#         print('hello')
# elif a%3==0:
#     print('word')
# else:
#     print(123)






#判断回文

# a=(input('输入：'))
# b=a[::-1]
# c=len(a)
# for  i in range(c):
#
#       if a[i]==b[i] :
#
#         if a == b :
#          print('是回文字符串')
#          break
#       else:
#           break


# a=[99,99,1,33,2]
# c=len(a)
# b=[]
# x=[]
# # for i, j in enumerate (a):
# #
# for i in range(0,c):
#     for j in range(i+1,c):
#         if a[i]<a[j]:
#             a[i],a[j]=a[j],a[i]
# x.append(a)
# for j in range(len(x)):
#  if  x[j] not in b:
#     b.append(x[j])
# print()
#         # if a[i]==a[j] and a[i]<a[0] and a[i]<a[1]:
#         #
#         #     print(a[0],a[1])







# a='I love this Game'
# c=a.split(' ')
# b=c[::-1]
# x=' '.join(b)
# print(x)

#12不用int
#13任意4个数,组成3位数
#15十六进制转十进制
#14将列表中的元素向左挪一位

# a='123456'
# b=a[::-1]
# c=len(a)
# sum=0
# for i in range(c):
#     for j in range(0,10):
#         if str(j)==b[i]:
#             j=j*10**i
#             sum=sum+j
# print(sum)


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

#
# a=[22,1,34,88,6]
# c=len(a)
# for i in range(0,c):
#         if a[0] >a[i]:
#             a[0],a[i]=a[i],a[0]
#         elif a[i]>a[c-1]:
#             a[i],a[c-1]=a[c-1],a[i]
# print(a)

# a=list(input('输入：').split(','))
# c=max(a)
# d=min(a)
# xb=a.index(c)
# xb1=a.index(d)
# c=len(a)
# a[0],a[xb]=a[xb],a[0]
# a[xb1],a[c-1]=a[c-1],a[xb1]
# print(a)


# b=(input('输入数值'))
# c=len(b)
# for i  in range(c):
#  for j in range(c):
#      for a in range(c):
#          if b[i]!=b[j]!=b[a]:
#              print(b[i],b[j],b[a])




# with open('e:\\jiaoben\\xjf\\hh.txt', mode='r', encoding='utf-8')as e:
#   c=e.readlines()
#   b = len(c)
#
# for i in range(b):
#     if c[i]=='\n':
#       b=b-1
#     elif c[i].startswith('#'):
#        b=b-1
# print(b)
#
# sum=0
# i=0
# while i <100:
#      i=i+1
#      sum=sum+i
# print(sum)

# a=1
# def hanshu():
#     global a
#     print(a)
#     a=0
#
# hanshu()
# print(a)

#参数个数无限制
# def hanshu(*arys,**kwargs):#必须参数，参数有x,y两个
#     print(arys)
#     print(kwargs)
# hanshu(1,2,3,name=4,age=3)#参数有多少个，值对应写入多少个


# def hanshu(x):
#     print(x)
# hanshu(sum(range(101)))
#
#
# def hanshu(x):
#     a=sum(range(x))
#     return a,100,101 # a是函数的值，100，101，是return调用的值
#     #return可返回多个值，（可赋值多个值）
# print(hanshu(10))#结果（45,100,101）
#
# def hanshu(x,y):
#     return x,y,100#return 可赋多个值
# print(hanshu(101,102)) #函数里面的值对应的是参数的值


# a = '123456'
# a = a[::-1]
# c = len(a)
# sum = 0
# def hanshu(sum):
#     for i in range(c):
#         for j in range(10):
#             if str(j)==a[i]:
#                 j=j*10**i
#                 sum=sum+j
#     print(sum)
# hanshu(sum)

#
# for i in range(101):#gong数量
#     for j in range(101):
#         for a in range(101):
#           if 2*i+1*j+0.5*a==100 and i+j+a==100  :
#                print(i,j,a)
# sum=0
# a=(input("输入：").split(','))
# c=len(a)
# for i in range(c):
#    sum=sum+a[i]
#    print(sum)


#
# for i in range(1,1001):
#     sum = 0
#     for j in range(1,i):
#         if i%j==0 :
#            sum=sum+j
#     if i==sum:
#          print(i)

# for i in range(1,1001):
#     s = 0
#     for j in range(1,i):
#         if i % j == 0:
#             s = s + j
#     if i == s:
#         print(i)

# def hanshu(x):
#     for i in range(1,x):
#         sum = 0
#         for j in range(1,i):
#             if i%j==0 :
#                sum=sum+j
#         if i==sum:
#              print(i)
# hanshu(1001)
#弄不出来
# def hanshu(b)
#
#     for i  in b:
#      for j in b:
#          for a in b:
#              if i!=j!=a:
#                return i,j,a
#
# print(hanshu(1234))


# b=int(input('请输入：'))
# def hanshu(b):
#     a=[1,3,5,7,9]
#     a.append(b)
#     c=len(a)
#     for i in range(0,c):
#         for j in range(i+1,c):
#
#             if a[j]<a[i]:
#                a[j],a[i]=a[i],a[j]
#     print(a)
# hanshu(b)


# a=lambda :print('hello')
# a()

#列表推导式
#变量名=[结果的变量 控制语句]
# a=[x for x in range(20) if x>7]
# print(a)



# a=['{}*{}={}'.format(i,j,i*j)    for i in range(10) for j in range(1,i+1)]
# print(a)

# a=[j for i in range(100) for j in range(1,i)  if i%j==0 ]
# if sum(a)==i:
#    print()


# f=open('hh.txt','rb')
# bb=f.read()
# print(bb)
# f=open('hh.txt','wb')
# f.write(b'\xe4\xb8\xad\xe5\x9b\xbd')


# f=open('tupian.jpg','rb')
# bb=f.read()
# print(bb)
#
# ff=open('qwe.jpg','wb')
# ff.write(bb)

# file=xlrd.open_workbook('3.xls')
# sheet=file.sheet_by_name('nihao')
# c=sheet.nrows
# with open('e:\\jiaoben\\xjf\\hh.txt',mode='w',encoding='utf-8')as e:
#     for i in range(c):
#         neirong=sheet.row_values(i)
#         for j in neirong:
#            j=str(j)
#            e.write(j)
#            e.write('\n')

# with open('e:\\jiaoben\\xjf\\hh.txt',mode='r',encoding='utf-8')as e:
#    c=e.readliens()
#    d=len(c)
#    for i in range(d):
#     if c[i].startswith=='abc':
#        print(c[i])


#
# from hhhh import hanshu
# hanshu()
# from xjf.hhhh import hanshu
# hanshu()
#如果 在源文件里面有if __name__=='__main__'，结果只会显示一遍
#如果没有判断语句，源文件有调用函数结果会显示2遍
#如果没有判读语句，源文件没有调用函数结果只显示1遍
#被调用的源文件内容如下


# 一次写入
# # 13到18行的内容
# # 开头有abc的行
#
# with open('e:\\jiaoben\\xjf\\hh.txt',mode='r',encoding='utf-8')as e:
#      c=e.readlines()
#      for i ,j in enumerate (c):
#         while 19> i >12:
#             print(i,j)
#             break

# with open('e:\\jiaoben\\xjf\\hh.txt',mode='r',encoding='utf-8')as e:
#    c=e.readlines()
#    for i ,j in enumerate(c):
#      if j.startswith('abc'):
#          print(j)



# with open('e:\\jiaoben\\xjf\\hh.txt', mode='w', encoding='utf-8')as e:
#  for i in range(10):
#      e.write('重生之贼行天下'+'\n')

#未解决
# a=(input('输入成绩：').split(','))
# c=len(a)
# sum=0
# for i in range(c):
#    sum=sum+int(a[i])
#    yu=sum//c
#    s = int(a[i])
#    if s<yu:
#        print(s)



# def hanshu(a,b):
#    for i in a:
#        for j in a:
#            if i+j==b:
#                print(i,j)
# hanshu([1,2,3,4,5],7)



# a=[4,55,55,62,62,62,1]
# b=[]
# da=max(a)
# c=a.count(da)
# z=0
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]<a[j]:
#             a[i],a[j]=a[j],a[i]
#             if a[i] == da:
#                b.append(a[i])
# while z < c:
#      a.remove(da)
#      z=z+1
# da1=max(a)
# for i in range(len(a)):
#     if a[i]==da1:
#        b.append(a[i])
# print(b)

# a = input('>>>').split(',')
# b = len(a)
# for i in range(0,b-1):
#     a[i],a[i+1] = a[i+1],a[i]
# print(a)
#
# file=xlrd.open_workbook('2.xls')
# sheet=file.sheets()[0]
# hang=sheet.nrows
# with open('e:\\jiaoben\\xjf\\hh.txt',mode='w',encoding='utf-8')as e:
#     for i in range(hang):
#         hang1=sheet.row_values(i)
#         for j in hang1:
#             j=str(j)+'\n'
#             j=j.split('\n')
#             j='\t\t\t\t'.join(j)
#             e.write(j)
#         e.write('\n')

# while True:
#     a=(input('输入成绩：').split(','))
#     c=len(a)
#     he=0
#     for i in range(c):
#         he = he+int(a[i])
#         yu = he / c
#     print('总成绩为{},平均成绩为{}'.format(he, yu))
#     for j in a :
#         if int(j) < yu:
#             print(int(j))
#         elif j.startswith('-'):
#             break

#显示文本中13行到18行的内容
#文本中开头带有abc的行
#写入十行的内容
#将表格的内容写入到txt
#将txt写入到表格
#下载图片到文件夹
#下载网页中的某个内容到表格
#下载网页中的某个内容到txt
#函数
#把基础那块内容再练习一遍

# import requests
# # import re
# # url='http://www.quanshuwang.com/book/0/567/7347707.html'
# # header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
# # huoqu=requests.get(url=url,headers=header)
# # geshi=huoqu.content.decode('gbk')
# # guolv=re.compile('&nbsp;&nbsp;&nbsp;&nbsp;(.*?)&nbsp;&nbsp;&nbsp;&nbsp;',re.S)
# # gl=guolv.findall(geshi)
# # gl.strip('<br />\r\n<br />\r\n')
# # print(gl)
# # # j=gl.split('<br />\r\n<br />\r\n')
# # # c='\n'+join(j)
# # # print(c)'


import  pymysql
# class Mysql_learn(object):
#     def __init__(self):#连接数据库
#       self.conn=pymysql.connect(host='192.168.2.99',port=3306,user='root',passwd='123456')#host:数据库所在的主机I
#       self.su=self.conn.cursor()#设置游标:执行动作，操作，能操控对象。所在位置。（类似光标，光标在哪里就在哪里操作）
#     def cao_zuo(self): #执行sql语句,只能是字符串
#        self.su.execute('show databases;')
#        self.su.execute('use yyy;')
#        for i in range(10):
#         # self.su.execute(('insert into  jj values ({},{},{},{},{},{});').format(i,i,i,i,i,i))
#         self.su.execute('select * from jj;')
#         print(self.su.fetchall())
#         # self.conn.commit() #提交数据，只有在对某个表的数据进行添加（insert）、删除（delete）、修改(alter)，等操作时使用
#            # print(self.su.fetchall())#读取上一个执行语句的结果，读取所有结果
#            # print(self.su.fetchmany(3))#读取多条内容，默认是一条内容
#            # print(self.su.fetchone())#每次只读取一条内容
#            # self.conn.close()#断开连接
# d=Mysql_learn()
# d.cao_zuo()



#
#
# import  pymysql
# class Mysql_learn(object):
#     def __init__(self):
#       self.conn=pymysql.connect(host='192.168.2.99',port=3306,user='root',passwd='123456')
#       self.su=self.conn.cursor()
#     def cao_zuo(self):
#        self.su.execute('use yyy;')
#        with open('qq.txt',mode='r',encoding='utf-8')as e:
#            c=e.readlines()
#            for i in range(10):
#              print(c[i])
#              self.su.execute(('insert into `我` values ({});').format(i))
#
#        self.conn.commit()
# d=Mysql_learn()
# d.cao_zuo()


# file =xlrd.open_workbook('3.xls')
# sheet=file.sheet_by_name('nihao')
# hang=sheet.nrows
# with open('qq.txt',mode='w',encoding='utf-8')as e :
#     for i in range(hang):
#         hang1=sheet.row_values(i)
#         for j in hang1:
#             j=str(j)
#             e.write(j)
#             e.write('\n')


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


#手动输入
#把表格中的内容写到数据库
#把数据库的内容写到表格
#把txt内容写到数据库
#把数据库内容写到txt
#更改数据库的编码
#
# class Shuju(object):
#     def __init__(self):
#         self.conn=pymysql.connect(host='192.168.2.99',port=3306,user='root',passwd='123456')
#         self.you=self.conn.cursor()
#     def zhi_xing(self):
#
#         s=[]
#         self.you.execute('use yyy;')
#         self.you.execute(('select * from xu;'))
#         b=list(self.you.fetchall())
#
#         # c=len(b)
#         # for i in range(c):
#         #     s.append(b[i][0])
#         #
#         # with open('qq.txt',mode='w',encoding='utf-8')as e:
#
#
#
#
# b=Shuju()
# b.zhi_xing()

import os
#popen()执行cmd命令
# dd=os.popen('ping 192.168.2.99')
# print(dd.read())
#getcwd:获取当前所在的目录
# print(os.getcwd())
#chdir 切换目录
# os.chdir('..')
# print(os.getcwd())
#mkdir创建目录
# os.mkdir('aaa')
#makedirs 创建递归目录
# os.makedirs('ee/qq/ww')
#删除递归目录
# os.removedirs('ee/qq/ww')
#删除空目录
# os.rmdir('aaa')
#remove:删除文件
# os.remove('jj.html')
#文件重命名 rename
# os.rename('qq.txt','q.txt')
#获取目录下面的所有文件 listdir
# print(os.listdir('C:')) #括号内不写入，默认当前目录下的所有文件
                        #括号内可以写其他目录的绝对路径

#将文件名和路径分隔开
# aa=os.path.split(r'‪C:\Users\xjf\Desktop\搜索 Everything.lnk')
# print(aa)

#将文件的后缀名和路径隔开
# aa=os.path.splitext(r'E:\jiaoben\hang.txt')
# print(aa)
#isdir判断是否是目录
# aa=os.path.isdir(r'E:/jiaoben')
# print(aa)
#isfile判断是否是文件
# aa=os.path.isfile(r'hang.txt')
# print(aa)


#统计某个目录下有多少个目录文件，有多少个普通文件

# a=(os.listdir())
# b=[]
# for i in range(len(a)):
#    if os.path.isfile((r'{}').format(a[i]))==True:
#        print(a[i])
#        b.append(a[i])
# print(len(b))
#正确的方法如下：
# a=(os.listdir())
# b=0
# c=0
#
# for i in a:
#    if os.path.isfile(i):
#       c=c+1
#    else:
#        b=b+1
# print(c)
# print(b)
#将当前目录下的所有.py过滤到列表中

# c=[]
# a=(os.listdir())
# for i in a:
#  aa=os.path.splitext(r'E:\jiaoben\xjf\{}'.format(i))
#  if aa[1]=='.py':
#      bb=os.path.split(r'E:\jiaoben\xjf\{}'.format(i))
#      c.append(bb[1])
# print(c)

#用列表推导式的方法写




#输入一个日期，（例如 2019-09-08）判断是否是润年，今天是一年中的第几天，这一天是周几
import time
import datetime
#
# a=(input('输入日期：').split('-'))
# b=int(a[0])
# c=int(a[1])
# x=int(a[2])
# jj=[]
# sum=0
# if b%4==0 and b%100!=0:
#     print('是闰年')
# elif b%400==0:
#     print('是闰年')
# days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# for i in range(x):
#    sum=sum+days[i]
# anyday=datetime.datetime(b,c,x).strftime("%w")

# print('是一年中的第',sum,'天','一周中的星期',anyday)



# import time
# a =['星期一','星期二','星期三','星期四','星期五','星期六','星期日']
# b = input('输入日期：')
# c=time.strptime(b,'%Y-%m-%d')
# if c.tm_year%4==0 and c.tm_year%100!=0 or c.tm_year%400==0:
#     print(c.tm_year,'年是闰年')
# else:
#     print(c.tm_year,'年是平年')
# print(c.tm_year,'年',c.tm_mon,'月',c.tm_mday,'日','是一年的第',c.tm_yday,'天','是一周中的',a[c.tm_wday])







#paramiko ,封装了ssh协议，主要用于远程控制
import  paramiko
# #创建ssh客户端
# ssh123=paramiko.SSHClient()
# # #将第一次连接的主机跳过验证，并添加到know_host文件中   know_host文件存放了可以远程的主机IP地址
# ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy())  #跳过进入host文件查看,如果没有这句，会报错。
# ssh123.connect(hostname='192.168.2.99',port=22,username='xjf',password='123456')  #连接到linux系统
#
# stuin ,stuout,stuerr =ssh123.exec_command('pwd')#输入在liunx上的命令,定义3个变量 ,产生3个结果 括号里的命令必须是能够直接有结果的
# #stuin:输入命令（但是打印不出来，因为加密了）
# #stuout:命令运行后的结果
# #stuerr:命令的报错
# aa=stuout.read().decode('utf-8')
# print(aa)
# ssh123.close()#断开连接



#将txt文本的内容写入到数据库的表里（子母和中文必须在文本加英文引号）
# class Shuju(object):
#     def __init__(self):
#        self.conn=pymysql.connect(host='192.168.2.99',port=3306,user='root',passwd='123456')
#        self.you=self.conn.cursor()
#     def cao_zuo(self):
#         self.you.execute('use yyy;')
#         with open('q.txt',mode='r',encoding='utf-8')as e:
#             c=e.readlines()
#         for i in range(len(c)):
#                 self.you.execute(('insert into xu values({})').format(c[i]))
#         self.conn.commit()
# a=Shuju()
# a.cao_zuo()

#将表格中的内容添加到数据库中
# class Shuju(object):
#     def __init__(self):
#        self.conn=pymysql.connect(host='192.168.2.99',port=3306,user='root',passwd='123456')
#        self.you=self.conn.cursor()
#     def cao_zuo(self):
#         self.you.execute('use yyy;')
#         file = xlrd.open_workbook('3.xls')
#         sheet = file.sheets()[0]
#         hang = sheet.nrows
#         for i in range(1,hang):
#             hang1 = sheet.row_values(i)
#             self.you .execute(('insert into xu values({})').format(hang1))
#         self.conn.commit()
# a=Shuju()
# a.cao_zuo()

#
# class Shuju(object):
#     def __init__(self):
#        self.conn=pymysql.connect(host='192.168.2.99',port=3306,user='root',passwd='123456')
#        self.you=self.conn.cursor()
#     def cao_zuo(self):
#         self.you.execute('use yyy;')
#         a=self.you.execute('select * from c;')
#         # print(self.you.fetchall())
#         b=self.you.execute('select count(*) from c;')
#         # print(self.you.fetchall())
#         with open('q.txt',mode='w',encoding='utf-8')as e:
#            for i in range(b):
#                print(a[i])
#                # e.write(a[i])
#
# a=Shuju()
# a.cao_zuo()

#局部变量和全局变量
# class Lei:
#     def __init__(self,b):
#         self.a=b
#     def haoshu(self,a):
#         print(f'nihao{self.a,a}')
#     def hanshu1(self):
#         print(f'zhongguo{self.haoshu()}')
#
# # Lei(33).haoshu()
# c=Lei().haoshu(44)





# import requests
# import re
# j=9674263
# for i in range(10):
#     j=j+1
#     url='http://www.quanshuwang.com/book/9/9055/{}.html'.format(j)
#     header={'Use-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
#     huoqu=requests.get(url=url,headers=header)
#     geshi=huoqu.content.decode('gbk')
#     guolv=re.compile('&nbsp;&nbsp;&nbsp;&nbsp;(.*?)&nbsp;&nbsp;&nbsp;&nbsp;',re.S)
#     gl=guolv.findall(geshi)
#     for i in gl:
#        print(i.strip('<br />\r\n<br />\r\n')+'\n')






#使用paramiko模块中的stfpclient组件传输文件
#建立一个传输通道，填入IP地址和端口号（是一个元祖）
# client=paramiko.Transport(('192.168.2.99',22))
# #连接主机，输入用户名和密码
# client.connect(username='xjf', password='123456')
# #创建一个sftp的客户端
# sftp_client=paramiko.SFTPClient.from_transport(client)
# #从liunx下载传文件到windows
# sftp_client.get('/root/桌面/a.txt',r'E:\xjf\u.txt')

import os
#将当前目录下的所有.py过滤到列表中
#统计某个目录下有多少个目录文件，有多少个普通文件

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



import  os
# print(os.listdir('C:'))




s
import pymysql
import xlwt
import xlrd
conn=pymysql.connect(host='192.168.2.99',port=3306,user='root',passwd='123456')
you=conn.cursor()
you.execute('use ttt;')
file=xlrd.open_workbook('3.xls')
sheet = file.sheets()[0]
hang=sheet.nrows
for i in range(hang):
    hang1=sheet.row_values(i)
    you.execute('insert into xu values("{}","{}")'.format(hang1[0],hang1[1]))
conn.commit()








