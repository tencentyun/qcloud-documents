Hive 中集成了 Thrift 服务。Thrift 是 Facebook 开发的一个软件框架，它用来进行可扩展且跨语言的服务的开发。Hive 的 HiveServer2 就是基于 Thrift 的，所以能让不同的语言如 Java、Python 来调用 Hive 的接口。

本节将演示如何使用 Python 代码来连接 HiveServer2。

## 1. 开发准备 
- 确认您已经开通了腾讯云，并且创建了一个 EMR 集群。在创建 EMR 集群的时候需要在软件配置界面选择 Hive 组件。 
- Hive 等相关软件安装在路径 EMR 云服务器的`/usr/local/service/`路径下。

## 2. 查看参数
首先需要登录 EMR 集群中的任意机器，最好是登录到 Master 节点。登录 EMR 的方式请参考 [登录 Linux 实例](https://cloud.tencent.com/document/product/213/5436)，这里我们可以选择使用 WebShell 登录。单击对应云服务器右侧的登录，进入登录界面，用户名默认为 root，密码为创建 EMR 时用户自己输入的密码。输入正确后，即可进入命令行界面。

在 EMR 命令行先使用以下指令切换到 Hadoop 用户，并进入 Hive 安装文件夹：
```
[root@172 ~]# su hadoop
[hadoop@172 root]$ cd /usr/local/service/hive/
[hadoop@172 hive]$
```
查看在程序中需要使用的参数：
```
[hadoop@172 hive]$ vim conf/hive-site.xml

<property>
	<name>hive.server2.thrift.bind.host</name>
	<value>$hs2host</value>
</property>
<property>
	<name>hive.server2.thrift.port</name>
	<value>$hs2port</value>
</property>
```
其中 $hs2host 为您的 HiveServer2 的 hostID，$hs2port 为您的 HiveServer2 的端口号。

## 3. 使用 Python 进行 Hive 操作
使用 Python 程序操作 Hive 需要安装 pip：
```
[hadoop@172 hive]$ su
[root@172 hive]# pip install pyhs2
```
安装完成后切换回 Hadoop 用户。然后在 `/usr/local/service/hive/` 目录下新建一个 Python 文件 hivetest.py，并且添加以下代码：
```
#!/usr/bin/env python

import pyhs2
import sys

default_encoding = 'utf-8'

conn = pyhs2.connect(host='$hs2host',
                                  port=$hs2port,
                                  authMechanism='PLAIN',
                                  user='hadoop',
                                  password='',
                                  database='default',)

tablename = 'HiveByPython'
cur = conn.cursor()
print 'show the databases: '
print cur.getDatabases()

print "\n"
print 'show the tables in default: '
cur.execute('show tables')
for i in cur.fetch():
        print i

cur.execute('drop table if exists ' + tablename)
cur.execute('create table ' + tablename + ' (key int,value string)')

print "\n"
print 'show the new table: '
cur.execute('show tables ' +"'" +tablename+"'")
for i in cur.fetch():
        print i

print "\n"
print "contents from " + tablename + ":";
cur.execute('insert into ' + tablename + ' values (42,"hello"),(48,"world")')
cur.execute('select * from ' + tablename)
for i in cur.fetch():
        print i
```
>!将程序中的参数 $hs2host 和 $hs2port 分别修改为您查到的 HiveServer2 的 hostID 和端口号的值。

该程序连接 HiveServer2 后，首先输出所有的数据库，然后显示“default”数据库中的表。创建一个名为“hivebypython”的表，在表中插入两个数据并输出。运行该程序：
```
[hadoop@172 hive]$ python hivetest.py
show the databases: 
[['default', ''], ['hue_test', ''], ['test', '']]

show the tables in default: 
['dd']
['ext_table']
['hive_test']
['hivebypython']

show the new table: 
['hivebypython']

contents from HiveByPython:
[42, 'hello']
[48, 'world']
```
