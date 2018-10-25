## 1. phpMyAdmin上传文件的限制
云数据库目前可以通过 phpMyAdmin 导入/导出 sql 数据文件。在导入上传的文件时，文件必须是 sql 文件或者压缩（tar、bz2、zip）后的 sql 文件，而且文件的大小不能超过 2 M。

## 2. 如何获知磁盘空间不足
监控中心对云数据库的磁盘空间进行了监控，当云数据库的使用空间超过 90% 的时候就会触发短信和邮件告警，这里只需要在云监控中配置好对应的告警接收人（如何配置请参考[告警功能](https://cloud.tencent.com/document/product/236/8457)），当空间不足的时候就能收到告警。

## 3. 使用云数据库前要做什么准备
在使用云数据库前您需要考虑以下两个问题：
1. 您的应用是否适合使用 DB？比如数据量小、访问量高、key-value 存储的场景就应该考虑使用内存级持久化存储服务 [【云缓存Memcached】](https://cloud.tencent.com/product/cmem)。
2. 您的数据库设计是否合理？比如有明显访问热点或者数据量过大的表，则应该考虑拆分成多个表。 

## 4. 云数据库的binlog保存时间是多久
由于 MySQL binlog 会占用大量的存储空间，所以云数据库只保存最近 5 天的 binlog。另外，如果 binlog 数据量增加太快，服务器磁盘存储不下 5 天的 binlog，会人工删除 binlog，释放空间。

## 5. 云数据库连接故障诊断及解决方案
当使用云数据库出现连接故障时，首先您需要确认您的云数据库实例的 IP、端口、用户、密码，然后在您的应用机器上通过命令行登录云数据库：
```
mysql -h IP -P 端口号 -u root -p 云数据库密码
```
下面是出现的问题类型及解决方案：
```
ERROR 1045(28000)：Access denied for user...
```
当出现 `Access denied for user ‘xxx’@‘x.x.x.x’(using password:YES)` 的提示语时，表明密码不正确。请确认输入的云数据库密码是否正确，如果重复输入正确密码后仍然报该错，则请通过 [提交工单](https://console.cloud.tencent.com/workorder) 联系技术支持。 
```
ERROR 1040(00000):Too many connections
```
当出现 `ERROR 1040(00000):Too many connections` 的提示语时，表明云数据库实例当前最大连接数超过了限制。
请检查程序，适当减少数据库的连接数。如果减少连接数后仍然报该错，则请通过 [提交工单](https://console.cloud.tencent.com/workorder) 联系技术支持。 
```
ERROR 2003 (HY000): Can't connect to MySQL server...
```
当出现 `ERROR 2003 (HY000): Can't connect to MySQL server on 'x.x.x.x' (111)` 的提示语时，表明云数据库地址不能连通，请确认您输入的云数据库的 IP、端口信息是否正确。如果重复输入正确信息后仍然报该错，则请通过 [提交工单](https://console.cloud.tencent.com/workorder) 联系技术支持。

## 6. 云数据库适用于哪些业务场景
MySQL 数据库适用的地方都可以使用云数据库。相比于自行搭建 MySQL，使用云数据库更加方便和可靠。
云数据库完全兼容 MySQL 协议，同时提供 master-slave 热备和定时冷备服务，此外支持实例无缝升级，可最大程度减少开发者在部署、监控、扩容和故障恢复等方面的投入，使开发者可以集中精力进行产品开发和运营。

## 7. 云数据库占用空间与使用空间的区别
目前云数据库用户实际使用空间与 binlog 等日志数据已分开统计，开发者在云数据库控制台看到的占用空间即等于使用空间。

## 8. 云数据库执行任务是否有缓冲
**问题描述：**
在很短的时间，送入了 N 条 SQL 语句给云数据库执行，此时云数据库会逐条执行，还是卡死？如果会卡死，那么同时的连接并发数限制是多少？
**问题解答：**
云数据库提供的 MySQL 实例与平时我们自己安装的 MySQL 实例是一样的。并发执行的语句是否会卡死跟系统资源和 SQL 语句本身有关。
如果连接数 max_connections 到达极限值，那么该实例基本上已经无法正常提供服务，一般是由以下原因造成的：
- 业务程序 bug 导致的空连接过多；
- 前端过来的访问远远超出实例的处理能力；
- 某个连接执行了太久，独占了 MySQL 的资源，导致大量的访问请求被阻塞。

## 9. 云数据库对数据量有什么限制？

详见 <a href="https://cloud.tencent.com/document/product/236/7259#1-.E6.95.B0.E6.8D.AE.E9.87.8F.E9.99.90.E5.88.B61" target="_blank">云数据库数量限制</a>。

## 10. 使用云数据库的注意事项？
详见 <a href="https://cloud.tencent.com/document/product/236/7259#7-.E6.93.8D.E4.BD.9C.E9.99.90.E5.88.B67" target="_blank">云数据库操作限制</a>。

## 11. 如何登录云数据库？
开发人员通过 IP/Port 的方式就可以完全控制和管理 MySQL 实例，无需登录到服务器进行操作。可通过命令行或者云数据库管理台登录云数据库，详见 <a href="https://cloud.tencent.com/document/product/236/3130" target="_blank">访问MySQL数据库</a>。

## 12. 是否可以自助修改 MySQL 实例的配置？
MySQL 实例的配置由云数据库统一管理，并支持部分参数的自助修改，详细请参考下面的问题 [如何修改云数据库配置参数](#change_parameter_21)。

## 13. 云数据库如何对MySQL进行管理？
开发者不需要对 MySQL 进行日常管理，日常的维护和调整由云数据库运维系统完成。当 MySQL 出现异常时，运维系统会及时发现并通知运维人员处理，开发者不需要做任何变更操作。

## 14. 云数据库中运行的MySQL版本是多少？
云数据库中使用的 MySQL 版本为 5.5.45、5.6.28。

## 15. 云数据库后面是否是实体机？
云数据库后面是实体机。

## 16. 云数据库会帮我做分库分表吗？
因为分库分表的标准和业务逻辑相关，所以云数据库不会帮业务做分库分表。

## 17. 云数据库的默认字符集编码能修改么？
可以修改。
默认字符集说明以及修改方法详见 <a href=https://cloud.tencent.com/document/product/236/7259#6-.E5.AD.97.E7.AC.A6.E9.9B.86.E8.AF.B4.E6.98.8E6"" target="_blank">云数据库使用限制</a>。

## 18. 如何查看云数据库慢查询日志？
可通过云数据库数据导出工具获取慢查询日志，详见 <a href="https://cloud.tencent.com/document/product/236/7274" target="_blank">下载备份文件</a>。

## 19. 开发者自己如何备份数据？
云数据库实例每天会进行全量备份，开发者也可以采用云数据库提供的多线程快速导入导出工具进行备份，详见[手动备份与恢复云数据库](https://cloud.tencent.com/document/product/236/7275)，或者通过 mysqldump 工具自己备份数据。

## 20.<span id="change_parameter_21"></span> 如何修改云数据库配置参数？

开发者可通过命令行和 phpMyAdmin 控制台，修改云数据库配置参数：

1. 命令行方式
以下变量可以单击“进入管理中心”，进入[总览页面](https://console.cloud.tencent.com/)：
![总览](//mc.qcloudimg.com/static/img/e3b4a1474b5d47ded82b5f2c3b534caf/image.png)
在”使用中的云产品“下拉菜单下单击“云数据库”，进入[MySQL-实例列表](https://console.cloud.tencent.com/cdb)：
![管理](//mc.qcloudimg.com/static/img/ca4c7858bcf89a2d0fe97fdcd4754e42/image.png)
单击管理列表下的参数设置，其中常见的 var\_name 包括如下变量：
<table class="t">
<tbody><tr>
<th>  变量
</th><th>  说明
</th></tr>
<tr>
<td> character_set_server
</td><td> 服务器默认字符集
</td></tr>
<tr>
<td> connect_timeout
</td><td> 连接超时
</td></tr>
<tr>
<td> long_query_time
</td><td> 超过该时间的查询为慢查询
</td></tr>
<tr>
<td> max_allowed_packet
</td><td> 最大包长度
</td></tr>
<tr>
<td> max_connections
</td><td> 最大连接数
</td></tr>
<tr>
<td> sql_mode
</td><td> 当前的服务器 SQL 模式
</td></tr>
<tr>
<td> table_open_cache
</td><td> 所有线程打开表的个数，增大该值可以增加 mysqld 被请求打开的文件描述符个数
</td></tr>
<tr>
<td> wait_timeout
</td><td> 非交互连接超时时间
</td></tr></tbody></table>
2. phpMyAdmin 控制台方式
通过 phpMyAdmin 登录云数据库后，单击上面菜单中的【变量】，在下面的变量列表中，单击需要修改的变量对应的【编辑】按钮，对其进行修改后单击【保存】。
![](//mc.qcloudimg.com/static/img/dbe6b04b221424dc11fedd1507e03f09/image.png)
更多请参考 [云数据库可以修改的配置](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/doc/cdb_user_modify_var.xls)。

## 21. 云数据库的连接数有限制吗？
详见 <a href="https://cloud.tencent.com/document/product/236/7259#2-.E8.BF.9E.E6.8E.A5.E6.95.B0.E9.99.90.E5.88.B62" target="_blank">云数据库链接数限制</a>。

## 22. 云数据库的binlog保存时间是多久？
详见 <a href="https://cloud.tencent.com/document/product/236/7269#5-.E4.BA.91.E6.95.B0.E6.8D.AE.E5.BA.93.E7.9A.84binlog.E4.BF.9D.E5.AD.98.E6.97.B6.E9.97.B4.E8.AF.B4.E6.98.8E5" target="_blank">云数据库的binlog保存时间说明</a>。

## 23. 云数据库的慢查询时间是多久？
云数据库的慢查询时间（long\_query\_time）的默认值是 10 秒，用户可以自行修改，命令跟配置参数的命令行方式一样,详见[数据库MySQL](https://cloud.tencent.com/document/product/236)，在参数配置里可修改。
单击“进入管理中心”，进入[总览页面](https://console.cloud.tencent.com/)：

![总览](//mc.qcloudimg.com/static/img/33ad26ed6b2fde8caad10566c7e21206/image.png)
在”使用中的云产品“下拉菜单下单击“云数据库”，进入[MySQL-实例列表](https://console.cloud.tencent.com/cdb)：

![管理](//mc.qcloudimg.com/static/img/0513c3baad993254f80fbd0be0825f96/image.png)

单击管理列表下的参数设置，修改的变量如下：
<table>
<tbody><tr>
<th>  变量
</th><th>  说明
</th></tr>
<tr>
<td> long_query_time
</td><td> 超过该时间的查询为慢查询
</td></tr>
</tr></tbody></table>

## 24. 为什么查看云数据库中的中文数据时出现乱码？
开发者将数据存储到云数据库中时，请先到 [云数据库的管理控制台](https://console.cloud.tencent.com/cdb) 进入相应实例的【管理视图】页面查看该实例的默认字符集，在编写程序时，将 character\_set\_client、character\_set\_results、character\_set\_connection 设置为和云数据库实例相同的字符集。否则，如果存储的数据中有中文，会出现中文数据乱码的现象。
例如：云数据库实例的默认字符集为 utf8，在编写程序连接数据库时，需要先执行以下语句，再将中文数据存储到云数据库。
```
SET NAMES 'utf8';
```

## 25. 如何导出数据库数据？
1. 如果需要导出冷备数据，可在控制台实例【备份管理】下载。
2. 如果需要导出实时数据，可以购买只读实例，通过只读实例 mysqldump 获取。
