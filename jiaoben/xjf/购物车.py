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


yue = i - sum
while True:
    if gm == 'Y':
        j = int(input("请选择想要购买的商品序号"))
        print('商品：', b[j - 1], '\n价格：', a[j - 1])
        gm = (input('是否还购买其他商品，输入Y/N:'))

    elif yue<=0:
        print('购买失败！\n您的余额不足，请充值！！')
        cz=(input('是否需要充值，输入yes/no'))
        if cz == 'yes':
          je=int(input('输入充值金额'))
          i=i+je
          print('您成功充值了',je,'元','当前余额：',i)

          if i-sum>0:
              yue=i-sum
              print('购买成功！\n已扣除商品价，您的当前余额为',yue)
          elif i-sum<0:
              print('购买失败！\n您的余额不足，请继续充值！！')
          break
        elif cz == 'no':

            break
    elif gm =='N':
        sum = sum + a[j - 1]
    print('购买成功！\n已扣除商品价，您的当前余额为',yue)
    cz=(input('是否继续购买，输入yes/no'))


    break






