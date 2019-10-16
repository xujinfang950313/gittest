#下载图片
#下载视频
#爬虫小说1到10页
#查找公司，职位，工资等内容写入到表格中
#查找公司，职位，工资等内容写入到表格中
#取小说网第一页的所有小说名字，写入到txt文件
#将百度地图获取的某个内容显示出来
#将百度地图获取的某个内容写入到txt文件中
#将百度地图获取的某个内容写入到表格中
#获取小说网页第一章的文本内容
#将小说的图片和名字下载到文件夹





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


#将小说的图片和名字下载到文件夹
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