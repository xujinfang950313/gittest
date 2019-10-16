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



#将txt文本的内容写入到数据库的表里  （txt只有一行的内容，对应写入每个字段）以行的实行写入
class Shuju(object):
    def __init__(self):
        self.conn=pymysql.connect(host='192.168.2.99',port=3306,user='root',passwd='123456')
        self.you=self.conn.cursor()
    def zhixing(self):
        self.you.execute('use ttt;')
        with open('e:\\jiaoben\\xjf\\q.txt',mode='r',encoding='utf8')as e:
            c=e.readlines()
            for i in c:
                i= i.split(',')
                for j in range(len(i)):

                       self.you.execute('insert into xu values("{}","{}")'.format(i[j],i[j]))
            self.conn.commit()

b=Shuju()
b.zhixing()




#将txt文本的内容传入数据库（txt 两列对应写入到数据表中的两列）以列的形式写入
class Shuju(object):
    def __init__(self):
        self.conn=pymysql.connect(host='192.168.2.99',port=3306,user='root',passwd='123456')
        self.you=self.conn.cursor()
    def zhixing(self):
        self.you.execute('use ttt;')
        with open('e:\\jiaoben\\xjf\\q.txt',mode='r',encoding='utf8')as e:
            c=e.readlines()
            for i in c:
                i= i.split(',')
                self.you.execute('insert into xu values("{}","{}")'.format(i[0],i[1].replace('\n','')))
            self.conn.commit()
b=Shuju()
b.zhixing()


#将数据库的内容写入到txt文本 以列的形式写入
class Shuju(object):
    def __init__(self):
        self.conn=pymysql.connect(host='192.168.2.99',port=3306,user='root',passwd='123456')
        self.you=self.conn.cursor()
    def zhixing(self):
        c=[]
        self.you.execute('use ttt;')
        self.you.execute('select * from xu;')
        aa=self.you.fetchall()
        for i in aa:
          c.append(i)
        with open('e:\\jiaoben\\xjf\\q.txt', mode='w', encoding='utf8')as e:
            c1 = len(c)
            for j in range(c1):
                    e.write(c[j][0]+','+c[j][1]+'\n')
b=Shuju()
b.zhixing()




#将数据库的内容写入到表格
class Shuju(object):
    def __init__(self):
        self.conn=pymysql.connect(host='192.168.2.99',port=3306,user='root',passwd='123456')
        self.you=self.conn.cursor()
    def zhixing(self):
        c=[]
        self.you.execute('use ttt;')
        self.you.execute('select * from xu;')
        aa=self.you.fetchall()
        for i in aa:
          c.append(i)
        file=xlwt.Workbook(encoding='utf8')
        sheet=file.add_sheet('nihao')
        c1 = len(c)
        for j in range(c1):
                    sheet.write(j,0,c[j][0])
                    sheet.write(j,1,c[j][1])
        file.save('66.xls')
b=Shuju()
b.zhixing()


#将表格的内容写入数据库
class Shuju(object):
    def __init__(self):
        self.conn=pymysql.connect(host='192.168.2.99',port=3306,user='root',passwd='123456')
        self.you=self.conn.cursor()
    def zhixing(self):
        self.you.execute('use ttt;')
        file=xlrd.open_workbook('2.xls')
        sheet=file.sheets()[0]
        hang=sheet.nrows
        for i in range(hang):
            hang1=sheet.row_values(i)
            self.you.execute('insert into xu values("{}","{}")'.format(hang1[0],hang1[1]))
b=Shuju()
b.zhixing()