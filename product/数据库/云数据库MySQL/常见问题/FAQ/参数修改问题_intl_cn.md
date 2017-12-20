### 1. 如何查看数据库 CDB for MySQL 的参数列表？
您可以通过离线迁移到本地来备份 MySQL 数据，请参考 [离线迁移数据](https://cloud.tencent.com/document/product/236/8464)。

### 2. 如何修改云数据库配置参数？

开发者可通过命令行和 phpMyAdmin 控制台，修改云数据库配置参数：

**1. 命令行方式**
步骤1：登录腾讯云 [管理控制台](https://console.cloud.tencent.com/) ，进入管理中心后，在【云产品】模块单击【云数据库】，进入关系型数据库页面。
![](//mc.qcloudimg.com/static/img/00ff8ac563c02a5f661a1b47284f92dc/image.png)

步骤2：在关系型数据库页面，单击【MySQL】下的【实例列表】，找到目标地域（此例中以广州为例）中待重置密码的 MySQL 数据库实例，单击【管理】按钮，进入 MySQL 数据库管理页面。

![](//mc.qcloudimg.com/static/img/62b1e4ab9953e54eab6c53da62ad6436/image.png)
步骤3：在 MySQL 数据库管理页面，单击管理列表下的参数设置，其中常见的 var\_name 包括如下变量：
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
**2. phpMyAdmin 控制台方式**
通过 phpMyAdmin 登录云数据库后，单击上面菜单中的【变量】，在下面的变量列表中，单击需要修改的变量对应的【编辑】按钮，对其进行修改后单击【保存】。
![](//mc.qcloudimg.com/static/img/dbe6b04b221424dc11fedd1507e03f09/image.png)
更多请参考 [云数据库可以修改的配置](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/doc/cdb_user_modify_var.xls)。

### 2. 数据库CDB for MySQL 怎么设置中文查询？
数据库 CDB 目前不支持中文字符。

### 3. 如何设置开启 MySQL 的定时器功能？
进入 [云数据库控制台](https://console.cloud.tencent.com/cdb)，找到需要修改的实例单击【管理】按钮，进入数据库管理页面，接着单击【参数设置】。在控制台参数设置中修改将 event 开启 。
![](//mc.qcloudimg.com/static/img/3843219af515499661c4335800253c6a/image.png)
   
### 4. MySQL 超时连接设置太短，如何增加时间？
进入 [云数据库控制台](https://console.cloud.tencent.com/cdb)，找到需要修改的实例单击【管理】按钮，进入数据库管理页面，接着单击【参数设置】。在控制台参数设置中修改 wait_timeout 参数 。
![](//mc.qcloudimg.com/static/img/e70e9a76b6651794552bd5253099c285/image.png)

### 5. 数据库CDB for MySQL 怎样调整 group_concat 参数？
进入 [云数据库控制台](https://console.cloud.tencent.com/cdb)，找到需要修改的实例单击【管理】按钮，进入数据库管理页面，接着单击【参数设置】。在控制台参数设置中修改参数 。
![](//mc.qcloudimg.com/static/img/67cfe78563599245bd12c07d55aad191/image.png)

### 6. MySQL 全表扫描的 SQL 语句有什么方法可以找到吗？
默认是不记录全表扫描的语句，可在云数据库控制台参数设置中开启 log_queries_not_using_indexes 参数。注意：不要开太久。

### 7. 云数据库的默认字符集编码如何修改？
云数据库与 MySQL 数据库一样，默认字符集编码格式是：latin1，即 ISO-8859-1 编码格式，开发者可以在云数据库的管理控制台修改 Server 端的数据库字符集，目前支持 latin1,gbk,utf8，utf8mb4 四种字符集设置。虽然云数据库支持默认字符集编码的设置，但我们还是建议您在创建表时，显式的指定表的编码，并在连接建立时指定连接的编码，这样，您的应用将会有更好的移植性，MySQL 默认字符集说明以及修改方法请参考<a href=https://cloud.tencent.com/document/product/236/7259#6-.E5.AD.97.E7.AC.A6.E9.9B.86.E8.AF.B4.E6.98.8E6"" target="_blank">云数据库使用限制</a>。可通过 CDB 管理控制台修改字符集。
