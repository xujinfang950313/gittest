#!/usr/bin/python3
# -*- coding: utf-8 -*-
# a=[ i*i for i in range(1,11)]
# print(a)
# try:
#    print (abcd)
# except SyntaxError as e :
#    print(e)


# txt =open(r'C:\Users\xjf\Desktopy\pp.txt',mode='w',encoding='UTF-8')
# txt.write('我爱你'+'\n相信我')
# txt.close()
# print(txt.read())


# print('nihao')
# raise TypeError('程序出错！！')


# i = int(input("请输入"))
# if i >50:
#     raise  TypeError('数值必须小于50')
# elif i  <20:
#     raise  TypeError('数值必须大于20')
# print(i)

# try:
#     print(123)
#     raise TypeError (111)
# except NameError as e :
#     print(e)
#     print(124)
# 有疑问
# # try:
# #         print(123)
# #         raise TypeError(111)
# # except TypeError as e:
# #         print(e)
# #         print(124)


# txt =open(r'E:\jiaoben\xjf\3.py',mode='w',encoding='UTF-8')
# a=txt.write('nihaoahello')
# txt.read().startswith('ni')
# txt.close()
# print()



# txt=open(r'E:\jiaoben\xjf\3.py',mode='a',encoding='UTF-8')
# txt.write('ok'*2)
# txt.close()

# txt=open(r'E:\jiaoben\xjf\3.py',mode='rb',encoding='UTF-8')
# txt.write('hh')




# with open(r'E:\jiaoben\xjf\3.py',mode='w+',encoding='UTF-8') as e :
#  e.write('bbb')

i=int(input("请输入总资产"))
print('\n\t\t\t商品总列表\t\t\t\n')
s1='序号\t\t商品名\t\t费用'
s2='\n 1\t\t\t电脑\t\t4500'+'\n 2\t\t\t鼠标\t\t200'+'\n 3\t\t\t游艇\t\t10000'+'\n 4\t\t\t美女\t\t8000'
print(s1,s2)
j=int(input("请选择想要购买得商品序号"))
b=['电脑','鼠标','游艇','美女']
a=[4500,200,10000,8000]
print('商品：',b[j-1],'\n价格：',a[j-1])
gm=(input('是否还购买其他商品，输入Y/N:'))
sum=a[j-1]
yue=i-sum

if yue<=0:
     print('购买失败！\n您的余额不足，请充值！！')
elif gm =='N':
   print('购买成功！\n已扣除商品价，您的当前余额为',yue)

else:
 if gm=='Y':
      j = int(input("请选择想要购买得第二个商品序号"))
      print('商品：',b[j-1],'\n价格：',a[j-1])
      gm=(input('是否还购买其他商品，输入Y/N:'))

 sum=sum+a[j-1]
 yue=i-sum
 if yue<=0:

        print('购买失败！\n您的余额不足，请充值')
 elif gm =='N':


         print('扣除商品价，您的当前余额为',yue,'元')


 else:
  if gm=='Y':
              j = int(input("请选择想要购买得第三个商品序号"))
              print('商品：',b[j-1],'\n价格：',a[j-1])
              gm=(input('是否还购买其他商品，输入Y/N:'))



  if yue<=0:

                    print('购买失败！\n您的余额不足，请充值')

  elif gm =='N':
                 sum=sum+a[j-1]
                 yue=i-sum

                 print('扣除商品价，您的当前余额为',yue,'元')



  else:
   if gm=='Y':
                  j = int(input("请选择想要购买得第四个商品序号"))
                  print('商品：',b[j-1],'\n价格：',a[j-1])
                  gm=(input('是否还购买其他商品，输入Y/N:'))
   sum = sum + a[j - 1]
   yue = i - sum
   if yue <= 0:
       print('购买失败！\n您的余额不足，请充值')

   elif gm =='N':


        print('扣除商品价，您的当前余额为',yue,'元')



