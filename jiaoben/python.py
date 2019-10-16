#!/usr/bin/python3
# -*- coding: utf-8 -*-
#while True：


# b=[11,12,13,[1,2,3,4],12,14]
# a=b.copy()
# a.append('nihao')
# a[3].append('hello')
# print(id(a[3]))
# print(id(b[3]))
# import copy
# a=[1,2,3,4,[22,33,44],556]
# b=copy.deepcopy(a)
# b[4].append('nihao' )
# print(id(a))
# print(id(b))
# while True:
#   i=int(input("请输入："))
#   if i % 2==0 and i %3 ==0:
#     print("helloworld")
#   elif i %2==0:
#         print("hello")
#   elif i %3 ==0:
#         print("word")
#         break


# i=str(input("请输入："))
# if i.startswith('Ac')or i.startswith('ac'):
#     print(110)
# elif i.startswith('a'):
#     print(120)
# elif i.startswith('c'):
#     print(130)
# else:
#     print(250)

# i =int(input("请输入:"))
# j=int(input("请输入个数："))
#
#
# for i in range(1,10):
#     for j in range(1,9):
#      for n in range(j):
#
#       print(i)

# sum =0
#
# for i in range(1,101):
#     if i%2==0:
#         sum=sum+i
# print(sum)
# for i in range(1,101):
#     if i%2!=0:
#         sum=sum+i
# print(sum)

# sum =0
# sum1=0
# for i in range(1,101):
#     if i%2==0:
#         sum=sum+i
#     elif i%2!=0:
#         sum1=sum1+i
# print(sum,sum1)
# sum=0
# for i in range(1,101,1):
#     sum=sum+i
#     print(sum)
# a=[1,2,3,4,555]
# for i,j in enumerate(a):
#     print(i,j)

# a=[34,55,66,193]
# for i in a :
#     if i ==34:
#      break
#     else:
#      print('no')


# a=[12,34,546]
# for i in a :
#     continue
# else:
#     print(00)

# while True:
#   import  random
#   a=random.randrange(10)


# c=3
# for i in range(1,10):
#  a=int(input("请输入："))
#  c=c-1
#  if a==i :
#      print('ok')
#      break
#  else:
#      print("还剩下",c,"次")
#      if c==0:
#          break



#while True:

# import  random
# a=random.randrange(10)
# for j in range(1,4):
#  i=int(input("请输入："))
#  j=3-j
#  if i==a:
#     print('ok')
#     break
#  elif i>a:
#      print('猜大了','还剩下',j,'次')
#  else:
#      if i<a:
#        print('猜小了','还剩下',j,'次')
#
#






#九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(('{}*{}={}'.format(i,j,i*j)),end='\t')
#     print()

# for i in range(1,10):
#   for j in range(1,i+1):
#
#    print(j,'*',i,'=',i*j,end='\t')
#   print()


# i=0
# a=0
# while i <5:
#  i = i+1
#  while a<3:
#    a = a+1
#    print('ok')
#  else:
#    print('9')
# else:
#  print('no')



# i=0
# while i <4:
#
#   j=0
#   while a<i+1:
#
#     print('*',end="\t")
#     a = a + 1
#   print()
#     i=i+1


#水仙花
def sxh ():
    for i in range(0,9):
        for j in range(1,9):
            for a in range(1,9):
                if i**3+j**3+a**3==i*100+j*10+a:
                    print(i,j,a)
sxh()
#阶乘之和
# sum=1
# b=0
# for j in range(1,4):
#    for i in range(1,j+1):
#     sum =sum*1
#    b=b+sum
# print(b)


# #因数之和 :所有能被数整除的数
def ys():
    sum=0
    for i in range(1,10):
        for j in range (1,i+1):
            if i%j==0:
                sum =sum+j

    print(sum)
ys()

#质数之和
def zsh():

    sum=0
    for i in range(1,10):
        for j in range (1,i+1):
            if i%j==0:
                break
            else:
             sum =sum+j
    print(sum)
zsh()

#判断三角型
# while True:
#     a=int(input("请输入a："))
#     b=int(input("请输入b:"))
#     c=int(input("请输入c:"))
#     if a**2+b**2>c**2:
#         print("是锐角三角型")
#     elif a**2+b**2==c**2:
#         print("是直角三角型")
#     elif a**2+b**2<c**2:
#         print("是钝角三角型")
#     else:
#         print("啥都不是")



for  i in range(1,101):
    for j in range(1,101):
        for a in range(1,101):
            if 2*i+j+0.5*a==100:
                print(i,j,a)

# i=int(input("请输入公鸡数"))
# j=int(input("请输入母鸡数"))
# a=int(input("请输入小鸡数"))
# if 2*i+j+0.5*a==100:
#     print('公鸡：',i,'母鸡：',j,'小鸡',a)
# else:
#     print("错的")



# a=[1,2,3,4]
# for i in a:
#  for j in a:
#      for c in a:
#          if i!=j and j !=c and i!=c:
#              print(i*100+j*10+c)


# a=[1,2,3,4]
# for i in a:
#  for j in a:
#      for c in a:
#          if i!=j and j !=c and i!=c:
#              print(i,j,c)

  #去重
# i=[99,34,25,25,56]
# if i.count(25)>1:
#    i.remove(25)
#    i.sort()
# print(i)
#





# while True:
#     i=input("请输入：")
#     if 100>=int(i)>=90:
#         print('youxiu')
#     elif 90>=int(i)>=80:
#         print('langhao')
#     elif  80>=int(i)>=70:
#         print('jige')
#     elif  int(i)<70:
#         print('no')
#     elif  i=="exit":
#         break


# i=list(input("请输入").split(" ,"))
# a=len(i)
# c =0
#*
#**
#***
# for i  in range(1,4):
#     for j in range (1,i+1):
#         print('*',end="\t")
#     print()

#嵌套判断
# i=int(input("请输入"))
# if i < 10 :
#   print('ok')
#   if i >1:
#    print('oktoto')
#   else:
#    print('nototo')
#
# else:
#   print('no')

# 排序
# a=[12,14,33,9]
# c=len(a)
# for i in range(0,c):
#   for j in range(i+1,c):
#    if a[i]>a[0]:
#     a[0],a[i]=a[i],a[0]
# print(a)


# for i in range(1,3):
#
#       print(a)
# else:
#     print('no')

#选择排序
# a=[12,14,33,9]
# c=len(a)
# for i in range(0,c):
#    if a[i]>a[0]:
#     a[0],a[i]=a[i],a[0]
# print(a)

# a=list(input("请输入").split(","))
# c=len(a)
# a=int(a)
# for i in range(0,c):
#     if a[i]>a[0]:
#      a[0],a[i]=a[i],a[0]
# print(a)

#while 九九乘法表
# i=1
# while i<10:
#     j = 1
#     while j <i+1:
#       print(('{}*{}={}'.format(j,i,i*j)),end="\t")
#       j=j+1
#     print()
#     i=i+1


#去重
# a=[12,14,33,9]
# c=len(a)
# for i in range(0,c):
#    if a[i]<a[i+1]:
#     a[i],a[i+1]=a[i+1],a[i]
# print(a)



#2，22，222
# i=int(input("输入"))
# # j=int(input("输入"))
# # for j in range (10,100,100):
# # print(i,i*10+i,i*100+i*10+i)

# a='qwrkwqd'
# # b=a.strip('qd')
# # print(b)

def jiuJiu():
    i=1
    while i<10:
        j = 1
        while j <i+1:
          print(('{}*{}={}'.format(j,i,i*j)),end="\t")
          j=j+1
        print()
        i=i+1
jiuJiu()

# a=1
# def hanshu():
#
#   global a
#   print(a)
#
# def hanshu1():
#     global a
#     print(a)
# hanshu()
# hanshu1()

# def hanshu(a,b,c,d=10,*args,**kwargs):
#     print(a)
#     print(b)
#     print(c)
#     print(d)
#     print(args)
#     print(kwargs)
#
# hanshu(12,143,14,99,00,22,key='values',key1=124)


