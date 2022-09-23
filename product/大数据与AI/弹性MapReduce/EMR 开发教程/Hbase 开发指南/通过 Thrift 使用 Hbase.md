Apache Thrift 是一个跨平台、跨语言的开发框架，提供多语言的编译功能，并提供多种服务器工作模式。用户通过 Thrift 的 IDL（接口描述语言）来描述接口函数及数据类型，然后通过 Thrift 的编译环境生成各种语言类型的接口文件，用来进行可扩展且跨语言的服务的开发。

它结合了功能强大的软件堆栈和代码生成引擎，以构建在 C++、Java、Go、Python、PHP、Ruby、Erlang、Perl、Haskell、C#、Cocoa、JavaScript、Node.js、Smalltalk 和 OCaml 编程语言间无缝结合的、高效的服务。

Thrift server 是 HBase 中的一种服务，主要用于对多语言 API 的支持。基于 Apache Thrift 开发。Thrift API 依赖于客户端和服务器进程。本节将以 Python 为例子，说明如何通过 Thrift 利用 Python 编程来使用 Hbase。

## 1. 开发准备
确认您已开通腾讯云，并且创建了一个 EMR 集群。创建 EMR 集群时需要在软件配置界面选择 Hbase 组件。

## 2. 通过 Python API 使用 Hbase
EMR 集群中 Hbase 默认集成了 Thrift，并在 Master1（外网 IP 节点）节点上启动了 Thrift Server。

登录 EMR 集群中的任意机器，最好是登录到 Master 节点。登录 EMR 的方式请参考 [登录 Linux 实例](https://cloud.tencent.com/document/product/213/5436)。这里我们可以选择使用 WebShell 登录。单击对应云服务器右侧的登录，进入登录界面，用户名默认为 root，密码为创建 EMR 时用户自己输入的密码。输入正确后，即可进入命令行界面。

在 EMR 命令行先使用以下指令切换到 Hadoop 用户并进入 Hbase 文件夹：
```
[root@172 ~]# su hadoop
[hadoop@172 root]$ cd /usr/local/service/hbase/
[hadoop@172 hbase]$
```
在 Hbase 的配置文件中查看 thrift 的 IP 地址和端口号：
```
[hadoop@172 hbase]$ vim conf/hbase-site.xml

<property>
        <name>hbase.master.hostname</name>
        <value>$thriftIP</value>
</property>
<property>
        <name>hbase.regionserver.thrift.port</name>
        <value>$port</value>
</property>
```
其中 $port 为 ThriftServer 的端口号。

因为 EMR 集群的 Hbase 默认集成了 Thrift，所以不需要再进行安装配置，使用以下命令查看 Thrift Server 是否已经启动：
```
[hadoop@172 hbase]$ jps

4711 ThriftServer
```
可见 Thrift Server 已经在后台运行。我们可以直接使用 Python 编程来操作 Hbase。

### 负载均衡
HA 集群有两个 master 节点，两个节点默认都启动了 Thrift Server。若需要实现负载均衡，客户端代码需要自定义策略将请求分散到两台 Thrift Server 上，这两台 Thrift Server 是完全独立的，之间没通信。

### 准备数据
使用 Hbase Shell 在 Hbase 中新建一个表，如果您使用过 EMR 的 Hbase 并且创建过自己的表，那么该步骤可以略过：
```
[hadoop@172 hbase]$ hbase shell 

hbase(main):001:0> create 'thrift_test', 'cf'
hbase(main):005:0> list
thrift_test                                                                                     
1 row(s) in 0.2270 seconds

hbase(main):001:0> quit
```

### 使用 Python 查看 Hbase 中的表
首先需要安装 Python 依赖包，切换到 root 用户下，密码即为创建 EMR 集群时您设置的密码，先安装 python-pip 工具再安装依赖包：
```
[hadoop@172 hbase]$ su
Password: ********
[root@172 hbase]# yum install python-pip
[root@172 hbase]# pip install hbase-thrift
```
然后切换回 Hadoop 用户并新建一个 Python 文件 Hbase_client.py，在其中加入以下代码：
```
#! /usr/bin/env python
#coding=utf-8

from thrift.transport import TSocket,TTransport
from thrift.protocol import TBinaryProtocol
from hbase import Hbase

socket = TSocket.TSocket('$thriftIP ', $port)
socket.setTimeout(5000)

transport = TTransport.TBufferedTransport(socket)
protocol = TBinaryProtocol.TBinaryProtocol(transport)

client = Hbase.Client(protocol)
transport.open()

print client.getTableNames()
```
>!其中 $thriftIP 为 Master 节点在内网的 IP 地址，$port 为 ThriftService 的端口号，下同。

保存后直接运行程序，会直接在控制台输出 Hbase 中的存在的表：
```
[hadoop@172 hbase]$ python Hbase_client.py
['thrift_test']
```

### 使用 Python 创建一个 Hbase 表
新建一个 Python 文件 Create_table.py，把以下代码加入其中：
```
#! /usr/bin/env python
#coding=utf-8

from thrift import Thrift
from thrift.transport import TSocket,TTransport
from thrift.protocol import TBinaryProtocol
from hbase import Hbase
from hbase.ttypes import ColumnDescriptor,Mutation,BatchMutation,TRegionInfo
from hbase.ttypes import IOError,AlreadyExists

socket = TSocket.TSocket('$thriftIP ',$port)
socket.setTimeout(5000)

transport = TTransport.TBufferedTransport(socket)
protocol = TBinaryProtocol.TBinaryProtocol(transport)

client = Hbase.Client(protocol)
transport.open()

new_table = ColumnDescriptor(name = 'cf:',maxVersions = 1)
client.createTable('thrift_test_1',[new_table])

tables = client.getTableNames()
socket.close()

print tables
```
该程序会在 Hbase 中添加一个名为 thrift_test_1 的新表，并且输出所有存在的表，运行效果如下：
```
[hadoop@172 hbase]$ python Create_table.py
['thrift_test', 'thrift_test_1']
```

### 使用 Python 在 Hbase 表中插入数据
新建一个 Python 文件 Insert.py，把以下代码加入其中：
```
#! /usr/bin/env python
#coding=utf-8

from thrift import Thrift
from thrift.transport import TSocket,TTransport
from thrift.protocol import TBinaryProtocol
from hbase import Hbase
from hbase.ttypes import ColumnDescriptor,Mutation,BatchMutation,TRegionInfo
from hbase.ttypes import IOError,AlreadyExists

socket = TSocket.TSocket('$thriftIP ', $port)
socket.setTimeout(5000)

transport = TTransport.TBufferedTransport(socket)
protocol = TBinaryProtocol.TBinaryProtocol(transport)

client = Hbase.Client(protocol)
transport.open()

mutation1 = [Mutation(column = "cf:a",value = "value1")]
client.mutateRow('thrift_test_1',"row1",mutation1)

mutation2 = [Mutation(column = "cf:b",value = "value2")]
client.mutateRow('thrift_test_1',"row1",mutation2)

mutation1 = [Mutation(column = "cf:a",value = "value3")]
client.mutateRow('thrift_test_1',"row2",mutation1)

mutation2 = [Mutation(column = "cf:b",value = "value4")]
client.mutateRow('thrift_test_1',"row2",mutation2)

socket.close()
```
该程序会在 Hbase 的 thrift_test_1 表中添加两行数据，每行分别有两个数据，可以在 Hbase Shell 中查看插入的数据：
```
hbase(main):005:0> scan 'thrift_test_1'
ROW       COLUMN+CELL                                                             
row1       column=cf:a, timestamp=1530697238581, value=value1                      
row1       column=cf:b, timestamp=1530697238587, value=value2                      
row2       column=cf:a, timestamp=1530704886969, value=value3                      
row2       column=cf:b, timestamp=1530704886975, value=value4                      
2 row(s) in 0.0190 seconds
```

### 使用 Python 查看 Hbase 表中的数据
有两种查看方式，一种是查看一行，一种是使用 Scan 来查看全部数据，新建一个 Python 文件 Scan_table.py，加入以下代码：
```
#! /usr/bin/env python
#coding=utf-8

from thrift import Thrift
from thrift.transport import TSocket,TTransport
from thrift.protocol import TBinaryProtocol
from hbase import Hbase
from hbase.ttypes import ColumnDescriptor,Mutation,BatchMutation,TRegionInfo
from hbase.ttypes import IOError,AlreadyExists

socket = TSocket.TSocket('$thriftIP ', $port)
socket.setTimeout(5000)

transport = TTransport.TBufferedTransport(socket)
protocol = TBinaryProtocol.TBinaryProtocol(transport)

client = Hbase.Client(protocol)
transport.open()

result1 = client.getRow("thrift_test_1","row1")
print result1
for r in result1:
        print 'the rowname is ',r.row
        print 'the frist value is ',r.columns.get('cf:a').value
        print 'the second value is ',r.columns.get('cf:b').value

scanId = client.scannerOpen('thrift_test_1',"",["cf"])
result2 = client.scannerGetList(scanId,10)
print result2

client.scannerClose(scanId)
socket.close()
```
其中使用 GetRow 来取得一行的数据，使用 scannerGetList 来得到整个表格中的数据，运行该程序后输出如下：
```
[hadoop@172 hbase]$ python Scan_table.py
[TRowResult(columns={'cf:a': TCell(timestamp=1530697238581, value='value1'), 'cf:b': TCell(timestamp=1530697238587, value='value2')}, row='row1')]
the rowname is  row1
the frist value is  value1
the second value is  value2

[TRowResult(columns={'cf:a': TCell(timestamp=1530697238581, value='value1'), 'cf:b': TCell(timestamp=1530697238587, value='value2')}, row='row1'), TRowResult(columns={'cf:a': TCell(timestamp=1530704886969, value='value3'), 'cf:b': TCell(timestamp=1530704886975, value='value4')}, row='row2')]
```
分别输出了第一行的数据和整个表中的数据。

### 使用 Python 删除 Hbase 中的数据
新建一个 Python 文件 Delete_row.py，把以下代码加入其中：
```
#! /usr/bin/env python
#coding=utf-8

from thrift import Thrift
from thrift.transport import TSocket,TTransport
from thrift.protocol import TBinaryProtocol
from hbase import Hbase
from hbase.ttypes import *

socket = TSocket.TSocket('$thriftIP ',$port)
socket.setTimeout(5000)

transport = TTransport.TBufferedTransport(socket)
protocol = TBinaryProtocol.TBinaryProtocol(transport)

client = Hbase.Client(protocol)
transport.open()

client.deleteAllRow("thrift_test_1","row2")

socket.close()
```
该程序会删除测试表中的第二行数据，运行后可以在 Hbase Shell 中查看该表中的内容：
```
[hadoop@172 hbase]$ python Delete_row.py
[hadoop@172 hbase]$ hbase shell

hbase(main):004:0> scan 'thrift_test_1'
ROW     COLUMN+CELL                                                                             
 row1     column=cf:a, timestamp=1530697238581, value=value1                                     
 row1     column=cf:b, timestamp=1530697238587, value=value2                                     
1 row(s) in 0.2050 seconds
```
此时表中只剩第一行中的数据。

更多关于 Thrift 的操作详见 [如何使用 Thrift](http://blog.cloudera.com/blog/2013/09/how-to-use-the-hbase-thrift-interface-part-1/?spm=5176.doc53887.2.4.6Nfd1X)。
