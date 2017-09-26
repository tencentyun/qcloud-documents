### 1. 云服务器与云数据库部署在相同区域上，如何连接 MySQL？
云服务器与云数据库部署在相同区域上时，请使用内网访问，连接方式请参考 [访问MySQL数据库](https://cloud.tencent.com/document/product/236/3130)。

### 2. 云服务器与云数据库部署在不同区域上，如何连接 MySQL？
云服务器与云数据库部署在不同区域上时，请使用外网访问，连接方式请参考 [外网访问](https://cloud.tencent.com/document/product/236/9038)。

### 3. 同一账号 CDB 数据库在上海一区，云服务器也在上海一区内网无法 PING 通？
CDB 是默认禁 ping 的，可以使用 telnet 来检测连通性。

### 4. 设置普通用户，MySQL 登录不了。提示：ERROR 1045 (28000): Access denied for user xxx (using password: YES)？
1045 密码不对。查看下设置的用户是否可以所有的 IP 用户进行登录，在 [MySQL控制台](https://console.cloud.tencent.com/) --对应实例--用户管理 。

### 5. 如何使用外网访问数据库 CDB for MySQL？
外网访问请参考 [外网访问](https://cloud.tencent.com/document/product/236/9038)。

### 6. 如何使用内网访问数据库 CDB for MySQL？
内网访问请参考 [访问 MySQL 数据库](https://cloud.tencent.com/document/product/236/3130)。

### 7. 如何使用命令行方式登录 MySQL的实例？
命令行访问请参考 [访问 MySQL 数据库](https://cloud.tencent.com/document/product/236/3130)。

### 8. 云数据库连接故障诊断及解决方案
当使用云数据库出现连接故障时，首先您需要确认您的云数据库实例的 IP、端口、用户、密码，然后在您的应用机器上通过命令行登录云数据库：
```
mysql -h IP -P 端口号 -u root -p 云数据库密码
```
下面是出现的问题类型及解决方案：
```
ERROR 1045(28000)：Access denied for user...
```
当出现 `Access denied for user ‘xxx’@‘x.x.x.x’(using password:YES)` 的提示语时，表明密码不正确。请确认您输入的云数据库密码是否正确，如果重复输入正确密码后仍然报该错，则请通过 [提交工单](https://console.qcloud.com/workorder) 联系技术支持。 
```
ERROR 1040(00000):Too many connections
```
当出现 `ERROR 1040(00000):Too many connections` 的提示语时，表明云数据库实例当前最大连接数超过了限制。
请检查程序，适当减少数据库的连接数。如果减少连接数后仍然报该错，则请通过 [提交工单](https://console.qcloud.com/workorder) 联系技术支持。 
```
ERROR 2003 (HY000): Can't connect to MySQL server...
```
当出现 `ERROR 2003 (HY000): Can't connect to MySQL server on 'x.x.x.x' (111)` 的提示语时，表明云数据库地址不能连通，请确认您输入的云数据库的 IP、端口信息是否正确。如果重复输入正确信息后仍然报该错，则请通过 [提交工单](https://console.qcloud.com/workorder) 联系技术支持。