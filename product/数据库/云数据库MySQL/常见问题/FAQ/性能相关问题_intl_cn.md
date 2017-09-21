### 1. 为什么 MyISAM 引擎不能使用？
CDB for MySQL 不支持 MyISAM 引擎的主要原因有如下几个：
- MyISAM 不支持事务。
- MyISAM 是表锁机制，并发支持不如 InnoDB。
- 现在 InnoDB 已经完全可以替代 MyISAM，官方最新版本已经放弃了 MyISAM，不在使用。

### 2. 云数据库 MySQL 执行任务时，为什么会卡死？
是并发操作导致的锁等待，属于正常现象。

### 3. 高 IO 版，内存 1000MB，硬盘 45GB，1000 次/秒 MySQL5.5 这里的 1000 次每秒指的是什么？
1000 次/秒是每秒执行操作数，是增删改查的总数。 

### 4. 为什么查看云数据库中的中文数据时出现乱码？
开发者将数据存储到云数据库中时，请先到 [云数据库的管理控制台](https://console.qcloud.com/cdb) 进入相应实例的【管理视图】页面查看该实例的默认字符集。在编写程序时，将 `character_set_client`、`character_set_results`、`character_set_connection` 设置为和云数据库实例相同的字符集。否则，如果存储的数据中有中文，会出现中文数据乱码的现象。
例如：云数据库实例的默认字符集为 utf8，在编写程序连接数据库时，需要先执行以下语句，再将中文数据存储到云数据库。
```
SET NAMES 'utf8';
```
### 5. 如何查看云数据库慢查询日志？
可在云数据库控制台导出并查看并慢查询日志。
云数据库的慢查询时间（long\_query\_time）的默认值是 10 秒，用户可以自行修改。
登录腾讯云 [管理控制台](https://console.qcloud.com/) ，进入管理中心后，在【云产品】模块单击【云数据库】，进入关系型数据库页面。
![总览](//mc.qcloudimg.com/static/img/d274cc926a10f2b4741d114264f927d5/image.png)
在关系型数据库页面，单击【MySQL】下的【实例列表】，找到目标地域（此例中以广州为例）中待重置密码的 MySQL 数据库实例，单击【管理】按钮，进入 MySQL 数据库管理页面。
![管理](//mc.qcloudimg.com/static/img/8216d33e2c5063b13c92e6010a7219d9/image.png)
在 MySQL 数据库管理页面，单击管理列表下的参数设置，修改的变量如下：
![参数设置](//mc.qcloudimg.com/static/img/a9836f3b39acfdf0f200df22e612d2bd/image.png)
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
### 6. 单击后台的登录，不能直接进入 phpadmin 创建数据库了，请问如何登录 phpadmin？
在控制台单击登录后选择返回 pma 即可 。
![图片描述](http://tss.sng.com/ticket/upload/displayImage?filename=598d51e955f76.png)
### 7. CDB 支持改成不同可用区吗？
目前支持不同可用户的地域只支持深圳金融，其他地区暂时还未发布 ，还请您知晓 。
### 8. phpMyAdmin 有上传文件的限制吗？
云数据库目前可以通过 phpMyAdmin 导入/导出 sql 数据文件。在导入上传的文件时，文件必须是 sql 文件或者压缩（tar、bz2、zip）后的 sql 文件，而且文件的大小不能超过 2M。