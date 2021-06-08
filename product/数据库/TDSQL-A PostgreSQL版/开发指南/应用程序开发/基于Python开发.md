[Psycopg](https://psycopg.org/) 是常用于 [Python](https://www.python.org/) 编程语言的 [PostgreSQL](https://www.postgresql.org/) 数据库适配器，同样也可以用来连接TDSQL-A PostgreSQL版 进行数据库操作。

Psycopg2 需要提前进行部署，可使用 `pip install psycopg2` 命令进行部署。

示例使用的均是3.6的 Python 版本，若使用 python2.x 版本需进行代码兼容修改。

## 示例1：数据库连接
```
conn.py
#coding=utf-8
#!/usr/bin/python
import psycopg2
try:
  conn = psycopg2.connect(database="v3", user="dbadmin", password="tdapg@tdapg", host="100.1.1.1", port="11345")
  print ("连接数据库成功")
  conn.close()
except psycopg2.Error as msg:
  print ("连接数据库出错，错误详细信息： %s" %(msg.args[0])) 
```
![](https://main.qcloudimg.com/raw/b4683aeddc5afd2ad6b5193a2d2aa506.png)

## 示例2：表创建
```
#coding=utf-8
#!/usr/bin/python
import psycopg2
try:
  conn = psycopg2.connect(database="v3", user="dbadmin", password="tdapg@tdapg", host="100.1.1.1", port="11345")
  print ("连接数据库成功") 
  cur = conn.cursor()
  sql = """
     create table tdapg 
     (
       id int,
       nickname varchar(100)
     )     """
  cur.execute(sql)
  conn.commit()
  print ("建立数据表成功")
  conn.close()
except psycopg2.Error as msg:
  print ("Tdapg Error %s" %(msg.args[0]))
```
![](https://main.qcloudimg.com/raw/c49aee177be94f8c0a2db48c90f6c2bc.png)

## 示例3：数据插入
```
#coding=utf-8
#!/usr/bin/python
import psycopg2
try:
  conn = psycopg2.connect(database="v3", user="dbadmin", password="tdapg@Tdapg", host="100.1.1.1", port="11345")
  print ("连接数据库成功")  
  cur = conn.cursor()
  sql = "insert into tdapg values(1,'tdapg'),(2,'tdapg');"
  cur.execute(sql)
  sql = "insert into tdapg values(%s,%s)"  
  cur.execute(sql,(3,'pg'))
  conn.commit()
  print ("插入数据成功")  
  conn.close()
except psycopg2.Error as msg:
  print ("操作数据库出库 %s" %(msg.args[0]))
```
![](https://main.qcloudimg.com/raw/8b9e60239a988518b5efdb7781c60bae.png)

## 示例4：数据查询
```
#coding=utf-8
#!/usr/bin/python
import psycopg2
try:
  conn = psycopg2.connect(database="v3", user="dbadmin", password="tdapg@Tdapg", host="100.1.1.1", port="11345")
  print ("连接数据库成功") 
  cur = conn.cursor()
  sql = "select * from tdapg"
  cur.execute(sql)
  rows = cur.fetchall()
  for row in rows:
    print ("ID = %s NICKNAME = %s " %(row[0],row[1]))
  conn.close()
except psycopg2.Error as msg:
  print ("操作数据库出库 %s" %(msg.args[0]))
```
![](https://main.qcloudimg.com/raw/e0e6a4f79ee5380da53ccc2d05f84907.png)

## 示例5：copy 数据插入
```
#coding=utf-8
#!/usr/bin/python
import psycopg2
    try:
       conn = psycopg2.connect(database="postgres", user="dbadmin",
       password="", host="172.16.0.29", port="15432")
       print ("连接数据库成功")
       cur = conn.cursor()
       filename = "/data/tbase/tdapg.txt"
       cols = ('id','nickname')
       tablename="public.tdapg"
       cur.copy_from(file=open(filename),table=tablename,columns=cols,sep=',')
       conn.commit()
       print ("导入数据成功")
       conn.close()
    except psycopg2.Error as msg:
       print ("操作数据库出库 %s" %(msg.args[0]))
```
