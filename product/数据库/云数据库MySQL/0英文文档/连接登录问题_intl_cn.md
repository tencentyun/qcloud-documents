### 1. 云服务器与云数据库部署在相同区域上，如何连接 MySQL？
云服务器与云数据库部署在相同区域上时，请使用内网访问，连接方式请参考 [访问MySQL数据库](https://cloud.tencent.com/document/product/236/3130)。

### 2. 云服务器与云数据库部署在不同区域上，如何连接 MySQL？
云服务器与云数据库部署在不同区域上时，请使用外网访问，连接方式请参考 [外网访问](https://cloud.tencent.com/document/product/236/9038)。

### 3. 同一账号 CDB 数据库在上海一区，云服务器也在上海一区内网无法 PING 通？
CDB 是默认禁 ping 的，可以使用 telnet 来检测连通性。

### 4. 如何使用外网访问数据库 CDB for MySQL？
外网访问请参考 [外网访问](https://cloud.tencent.com/document/product/236/9038)。

### 5. 如何使用内网访问数据库 CDB for MySQL？
内网访问请参考 [访问 MySQL 数据库](https://cloud.tencent.com/document/product/236/3130)。

### 6. 云数据库连接故障诊断及解决方案
当使用云数据库出现连接登录问题时，首先 telnet 验证云数据库的网络端口连通性，然后在您的云服务器上通过命令行登录云数据库（云数据库的帐号默认为 root，密码为之前在初始化选项中配置的帐号密码）：
```
mysql -h [云数据库IP] -P[云数据库端口号] -uroot -p[云数据库密码]
```
下面是常见的问题类型及解决方案：
1. 当出现 “ERROR 1045(28000):Access denied for user...” 的提示语时，请确认您输入的云数据库帐号、密码是否正确，忘记密码请参考 [密码重置](https://cloud.tencent.com/document/product/236/10305)，如果重复输入正确信息后仍然报该错误，请查看您的实例是否有对访问 IP 做限制，在 【[MySQL控制台](https://console.cloud.tencent.com/)】>【对应实例】>【帐号管理】。
2.  当出现 “ERROR 1040(00000):Too many connections” 的提示语时，表明云数据库实例当前最大连接数超过了限制。常见原因及解决方案：
i. sleep 线程数很多，建议在控制台调低 wait_timeout和interactive_timeout 参数值； 
ii. 慢查询堆积，long_query_time参数值默认 10s，建议调成 1~2s，观察慢查询日志；
iii. sleep 线程数很少，也没有慢查询堆积，建议在控制台调大 max_connections 参数值；
3. 当出现 “ERROR 2003 (HY000): Can't connect to MySQL server...” 的提示语时，请确认您输入的云数据库的 IP、端口信息是否正确。如果重复输入正确信息后仍然报该错，可以查看该实例控制台的“安全组”策略，确认该 CVM 是否有访问该 CDB 的权限。详见 [云数据库安全组操作指引 ](https://cloud.tencent.com/document/product/236/10636)。