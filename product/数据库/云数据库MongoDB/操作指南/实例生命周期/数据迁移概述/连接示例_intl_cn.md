实例初始化后，可以通过MongoDB shell 或者各语言驱动进行访问数据库，进行各种管理操作。需要使用CVM通过内网进行访问，暂不支持外网访问方式。

## 详细说明
### 客户端版本
连接腾讯云MongoDB服务最低驱动版本需要3.2，请尽量使用**最新版**的客户端驱动以保证最好的兼容性，包括shell套件、java jar包、php扩展、nodejs模块等等，具体请参见[MongoDB官网驱动介绍](https://docs.mongodb.com/ecosystem/drivers/)。
### MongoDB shell方式
mongo shell是MongoDB自带的一种交互式JavaScript shell。可在shell中使用命令行与MongoDB实例交互。您可以使用mongo shell查询和更新数据或执行管理操作。mongo shell是MongoDB发行版的一部分，您需要先下载或者安装MongoDB，然后再使用mongo shell 连接至您的MongoDB实例。MongoDB发行版下载地址请点击[连接](https://www.mongodb.com/download-center#community)具体连接步骤如下<br>

    cd <mongodb installation dir>
	./bin/mongo -umongouser -plxh2081* 172.16.0.56:27017/admin
> 上例中，-u参数指定用户名，-p参数指定密码,172.16.0.56和27017分别指定MongoDB实例的IP和端口。
### URI方式
MongoDB服务可以用传统的传参的方式进行连接，同时大部分的驱动程序也支持URI形式进行连接。MongoDB官方推荐使用URI的方式连接MongoDB服务。典型的URI如下：

例1
```
mongodb://username:password@IP:27017/admin
```
例2
```
mongodb://username:password@IP:27017/somedb?authSource=admin
```
例3
```
mongodb://username:password@IP:27017/somedb?authSource=admin&readPreference=secondaryPreferred
```

URI组成的各个部分解释如下：

| 组成部分 | 含义 | 是否必须 |
|---------|---------|---------|
| mongodb:// | 一个特定的字符串，表示MognoDB协议 | 必须|
| username |用于登录MongoDB服务的用户名 |必须，参见本页“[默认用户名](#.E9.BB.98.E8.AE.A4.E7.94.A8.E6.88.B7.E5.90.8D)”|
| password | 用于登录MongoDB服务的用户密码 |必须|
| IP:27017 | MongoDB服务IP和端口 |必须|
| /admin | 要认证的数据库，腾讯云MongoDB固定为admin |必须，参见本页“[认证数据库](#.E8.AE.A4.E8.AF.81.E6.95.B0.E6.8D.AE.E5.BA.93)”|
| authMechanism=MONGODB-CR | 认证机制 |参见本页“[认证机制](#.E8.AE.A4.E8.AF.81.E6.9C.BA.E5.88.B6)”|
| authSource=admin | 身份认证所用库，腾讯云MongoDB固定为admin |必须，参见本页“[认证数据库](#.E8.AE.A4.E8.AF.81.E6.95.B0.E6.8D.AE.E5.BA.93)”|
| readPreference=secondaryPreferred | 可以设置优先读从库 |非必须，参见本页“[读操作的主从优先级](#.E8.AF.BB.E6.93.8D.E4.BD.9C.E7.9A.84.E4.B8.BB.E4.BB.8E.E4.BC.98.E5.85.88.E7.BA.A7)”|
这里只是列举了一部分MongoDB连接URI的参数，更多内容请参考[MongoDB官网文档](https://docs.mongodb.com/manual/reference/connection-string/)。

### 默认用户

根据腾讯云MongoDB发布版本而异，对于最新生产的实例，我们內建了“rwuser”和“mongouser”两个默认用户。较老实例只有rwuser（对于这批实例我们会进行升级，升级之前会联系您）。您也可以使用腾讯云MongoDB控制台进行账号和权限管理以满足您的业务需要。

#### rwuser（MONGODB-CR认证）URI示例
**rwuser是唯一使用MONGODB-CR认证的用户**
```
mongodb://rwuser:password@10.66.100.186:27017/admin?authMechanism=MONGODB-CR
或者
mongodb://rwuser:password@10.66.100.186:27017/somedb?authMechanism=MONGODB-CR&authSource=admin
```

#### mongouser（SCRAM-SHA-1认证）URI示例
**mongouser以及在云控制台创建的用户都使用SCRAM-SHA-1认证**
```
mongodb://mongouser:password@10.66.100.186:27017/admin
或者
mongodb://mongouser:password@10.66.100.186:27017/somedb?authSource=admin
```

### 认证数据库
腾讯云MongoDB统一使用“admin”库作为登录鉴权的认证数据库，所以在URI中端口后面必须加上“**/admin**”以指定认证库，通过认证以后再切换到具体业务数据库进行读写操作，URI示例：

```
mongodb://username:password@IP:27017/admin
```

当然，也可通过直接指定读写目标数据库和额外的认证库参数（authSource=admin）来直达目标数据库，URI示例：

```
mongodb://username:password@IP:27017/somedb?authSource=admin
```

综上，您必须选择一种方式将admin作为认证库代入URI中。

### 认证机制
MongoDB支持多种认证机制，目前官方推荐的是“SCRAM-SHA-1”。
腾讯云MongoDB支持“MONGODB-CR”和“SCRAM-SHA-1”两种认证方式。
前文说道，腾讯云MongoDB内建了两个默认用户“rwuser”和“mongouser”，同时还可以在腾讯云MongoDB控制台创建额外的用户，这些用户被分成了两类，分别采用不同的认证机制，分类如下：

| 用户名 | 认证机制 | URI处理 |
|---------|---------|---------|
| rwuser | MONGODB-CR | 必须加上参数“authMechanism=MONGODB-CR”|
| mongouser 以及在云控制台创建的用户 |SCRAM-SHA-1（推荐）|不用加任何参数|

###  读操作的主从优先级
腾讯云MongoDB提供了一个负载均衡IP用于访问整个副本集，如果需要指定访问从库读请在URI里设置“readPreference”参数，具体取值含义如下：

| 取值 | 含义 | 是否默认|
|---------|---------|---------|
| primary |只读主节点 | 默认方式|
| primaryPreferred |主节点优先，如主节点不可用，则读从节点 |　|
| secondary | 只读从节点，如从节点不可用会报错|　|
| secondaryPreferred |  从节点优先，如从节点不可用，则读主节点|　|

设置优先读取从节点可以按示例拼接URI：

```
mongodb://username:password@IP:27017/admin?readPreference=secondaryPreferred
```

## 各语言示例

### Shell
[Shell连接示例](https://cloud.tencent.com/doc/product/240/Shell%E8%BF%9E%E6%8E%A5%E7%A4%BA%E4%BE%8B)
### PHP
[PHP连接示例](https://cloud.tencent.com/doc/product/240/PHP%E8%BF%9E%E6%8E%A5%E7%A4%BA%E4%BE%8B)
### Node.js
[Node.js连接示例](https://cloud.tencent.com/doc/product/240/Node.js%E8%BF%9E%E6%8E%A5%E7%A4%BA%E4%BE%8B) 
 [mongoose示例](https://cloud.tencent.com/doc/product/240/Node.js%E8%BF%9E%E6%8E%A5%E7%A4%BA%E4%BE%8B#node.js-mongoose-.E8.BF.9E.E6.8E.A5.E7.A4.BA.E4.BE.8B)
### Java
[Java连接示例](https://cloud.tencent.com/doc/product/240/Java%E8%BF%9E%E6%8E%A5%E7%A4%BA%E4%BE%8B)
### Python
[Python连接示例](https://cloud.tencent.com/doc/product/240/Python%E8%BF%9E%E6%8E%A5%E7%A4%BA%E4%BE%8B)
### 重连机制
[重连机制](https://cloud.tencent.com/doc/product/240/4980)
