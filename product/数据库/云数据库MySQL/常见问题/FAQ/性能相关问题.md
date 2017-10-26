### 1. 为什么 MyISAM 引擎不能使用？
CDB for MySQL 不支持 MyISAM 引擎的主要原因有如下几个：
- MyISAM 不支持事务。
- MyISAM 是表锁机制，并发支持不如 InnoDB。
- 现在 InnoDB 已经完全可以替代 MyISAM，官方最新版本已经放弃了 MyISAM，不再使用。

### 2. 云数据库 MySQL 执行任务时，为什么会卡死？
是并发操作导致的锁等待，属于正常现象。

### 3. 高 IO 版，内存 1000MB，硬盘 45GB，1000 次/秒 MySQL5.5 这里的 1000 次每秒指的是什么？
1000 次/秒是每秒执行操作数，是增删改查的总数。 

### 4. 为什么查看云数据库中的中文数据时出现乱码？
开发者将数据存储到云数据库中时，请先到 [云数据库的管理控制台](https://console.cloud.tencent.com/cdb) 进入相应实例的【管理视图】页面查看该实例的默认字符集。在编写程序时，将 `character_set_client`、`character_set_results`、`character_set_connection` 设置为和云数据库实例相同的字符集。否则，如果存储的数据中有中文，会出现中文数据乱码的现象。
例如：云数据库实例的默认字符集为 utf8，在编写程序连接数据库时，需要先执行以下语句，再将中文数据存储到云数据库。
```
SET NAMES 'utf8';
```
### 5. MySQL 连接数占用满了的常见原因和解决方法？
- sleep 线程数很多，建议在控制台调低 wait_timeout和interactive_timeout 参数值；
- 慢查询堆积，long_query_time 参数值默认 10s，建议调成 1~2s，观察慢查询日志；
- sleep 线程数很少，也没有慢查询堆积，建议在控制台调大 max_connections 参数值。

### 6. MySQL CPU 占比过高的常见原因和解决方法？
- 慢查询堆积，请查看实例监控上的慢查询和全表扫描，结合慢查询日志（控制台可下载）进行分析优化，若监控上没有慢查询只有全表扫描，建议在控制台将 long_query_time 调小至 1~2s，使用一段时间后再分析慢查询；
- 没有慢查询堆积，请查看实例监控上的内存占用，若超出实例规格很多，并且磁盘读写量明显增大，表明内存遇到瓶颈，建议升级内存。

### 7. 如何查看 MySQL 慢查询日志？
MySQL 慢查询时间（long_query_time）的默认值是 10s，在遇到性能问题时，若没发现有慢查询，建议调成 1~2s 再查看 。
登录腾讯云 [管理控制台](https://console.cloud.tencent.com/) ，进入管理中心后，在【云产品】模块单击【云数据库】，进入关系型数据库页面。
![总览](//mc.qcloudimg.com/static/img/d274cc926a10f2b4741d114264f927d5/image.png)
在关系型数据库页面，单击【MySQL】下的【实例列表】，找到目标地域（此例中以广州为例）中的 MySQL 数据库实例，单击【管理】按钮，进入 MySQL 数据库管理页面。
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
在【操作日志】查看并导出慢查询日志。
![操作日志](//mc.qcloudimg.com/static/img/101fd6b1360e3e77e3ba2bd5522fd8e6/image.png)
