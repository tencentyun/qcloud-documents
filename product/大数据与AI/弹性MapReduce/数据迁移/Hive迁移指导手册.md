Hive 迁移涉及两部分，数据迁移和元数据迁移。Hive 表数据主要存储在 HDFS 上，故数据的迁移主要在 HDFS 层。Hive 的元数据主要存储在关系型数据库，可平滑迁移到云上 TencentDB，并可保障高可用。

### Hive 元数据迁移

1. Dump 源 Hive 元数据库。
```
mysqldump -hX.X.X.X -uroot -pXXXX --single-transaction --set-gtid-purged=OFF hivemetastore > hivemetastore-src.sql  
# 如果 mysql 数据没有开启 GTID，请删除命令行中的 --set-gtid-purged=OFF  
# X.X.X.X为数据库服务器地址  
# XXXX为数据库密码  
# 如果数据库用户不是 root，请用正确的用户名  
# hivemetastor 是 Hive 元数据库名 
```
2. 确认目标 Hive 表数据在 HDFS 中的缺省路径。
Hive 表数据在 HDFS中 的缺省路径由`hive-site.xml`中的`hive.metastore.warehouse.dir`指定。如果 Hive 表在 HDFS 的存储位置依然保持与源 Hive 一致，那么需要修改为与源 Hive 数据库中的值一致。

 例如：源`hive-site.xml`中`hive.metastore.warehouse.dir`为下面的值。
```
<property>  
    <name>hive.metastore.warehouse.dir</name>  
    <value>/apps/hive/warehouse</value>  
</property>  
```

 目标`hive-site.xml`中`hive.metastore.warehouse.dir`为下面的值。
```
<property>  
    <name>hive.metastore.warehouse.dir</name>  
    <value>/usr/hive/warehouse</value>  
</property>  
```
如果 Hive 表在 HDFS 的存储位置依然保持与源 Hive 一致，那么修改目标`hive-site.xml`中的`hive.metastore.warehouse.dir`，即为：
```
<property>  
    <name>hive.metastore.warehouse.dir</name>  
    <value>/apps/hive/warehouse</value>  
</property>  
```
3. 确认目标 Hive 元数据 SDS.LOCATION 和 DBS.DB_LOCATION_URI 字段。
通过下面的查询获取当前 SDS.LOCATION 和 DBS.DB_LOCATION_URI 字段。
```
SELECT DB_LOCATION_URI from DBS;  
SELECT LOCATION from SDS; 
```
查询出的结果类似如下：
```
mysql> SELECT LOCATION from SDS;  
+--------------------------------------------------+  
| LOCATION |  
+--------------------------------------------------+  
| hdfs://HDFS2648/usr/hive/warehouse/hitest.db/t1 |  
| hdfs://HDFS2648/usr/hive/warehouse/wyp |  
+--------------------------------------------------+  
mysql> SELECT DB_LOCATION_URI from DBS;  
+-----------------------------------------------+  
| DB_LOCATION_URI |  
+-----------------------------------------------+  
| hdfs://HDFS2648/usr/hive/warehouse |  
| hdfs://HDFS2648/usr/hive/warehouse/hitest.db |  
+-----------------------------------------------+ 
```

 其中`hdfs://HDFS2648`是 HDFS 默认文件系统名，由`core-site.xml`中的`fs.defaultFS`指定。
```
<property>  
    <name>fs.defaultFS</name>  
    <value>hdfs://HDFS2648</value>  
</property> 
```
`/usr/hive/warehouse`为 Hive 表在 HDFS 中的默认存储路径，也是`hive-site.xml`中`hive.metastore.warehouse.dir`指定的值。

 所以我们需要修改源 hive 元数据 sql 文件中的 SDS.LOCATION 和 DBS.DB_LOCATION_URI 两个字段。确保被导入的 Hive 元数据库中的这两个字段使用的是正确的路径。

 可以使用下面 sed 命令批量修改 sql 文件。
```
替换ip：sed -i 's/oldcluster-ip:4007/newcluster-ip:4007/g' hivemetastore-src.sql  
替换defaultFS：sed -i 's/old-defaultFS/new-defaultFS/g' hivemetastore-src.sql  
```
4. 停止目标 Hive 服务 MetaStore、HiveServer2、WebHcataLog。
5. 备份目标 Hive 元数据库。
```
mysqldump -hX.X.X.X -uroot -pXXXX --single-transaction --set-gtid-purged=OFF hivemetastore > hivemetastore-target.sql  
# 如果 mysql 数据没有开启 GTID，请删除命令行中的 --set-gtid-purged=OFF  
# X.X.X.X为数据库服务器地址  
# XXXX为数据库密码  
# 如果数据库用户不是 root，请用正确的用户名  
# hivemetastor 是 Hive 元数据库名 
```
6. Drop/Create 目标 Hive 元数据。
```
mysql> drop database hivemetastore;  
mysql> create database hivemetastore; 
```
7. 导入源 Hive 元数据库到目标数据库。
```
mysql -hX.X.X.X -uroot -pXXXX hivemetastore < hivemetastore-src.sql  
# X.X.X.X为数据库服务器地址  
# XXXX为数据库密码  
# 如果数据库用户不是 root，请用正确的用户名  
# hivemetastor 是 Hive 元数据库名 
```
8. Hive 元数据升级。
如果目标和源 Hive 版本一致，则可直接跳过该步骤；否则，分别在源集群和目标集群查询 Hive 版本。
```
hive --service version 
```
hive 的升级脚本存放在`/usr/local/service/hive/scripts/metastore/upgrade/mysql/`目录下。

 hive 不支持跨版本升级，例如 hive 从1.2升级到2.3.0需要依次执行：
```
upgrade-1.2.0-to-2.0.0.mysql.sql -> upgrade-2.0.0-to-2.1.0.mysql.sql -> upgrade-2.1.0-to-2.2.0.mysql.sql -> upgrade-2.2.0-to-2.3.0.mysql.sql
```
升级脚本主要操作为建表、加字段、改内容。如果表或字段已经存在，则升级过程中字段已存在的异常可以忽略。例如 hive 从2.3.3升级至3.1.1。
```
mysql> source upgrade-2.3.0-to-3.0.0.mysql.sql;  
mysql> source upgrade-3.0.0-to-3.1.0.mysql.sql;  
```
9. 修改目标 Hive 元数据中 phoneix 表的 zookeeper 地址。
如果源 Hive 中有 phoneix 表，通过下面的查询获取 phoenix 表的`phoenix.zookeeper.quorum`配置。
```
mysql> SELECT PARAM_VALUE from TABLE_PARAMS where PARAM_KEY = 'phoenix.zookeeper.quorum';  
+--------------------------------------------------+    
| PARAM_VALUE |    
+--------------------------------------------------+    
| 172.17.64.57,172.17.64.78,172.17.64.54 |     
+--------------------------------------------------+  
```
查看目标集群的 zookeeper 地址，即`hive-site.xml`配置文件中`hbase.zookeeper.quorum`指定的值。
```
<property>  
    <name>hbase.zookeeper.quorum</name>  
    <value>172.17.64.98:2181,172.17.64.112:2181,172.17.64.223:2181</value>  
</property>  
```
将目标 Hive 元数据中的 phoenix 表的 zookeeper 地址改为目标集群的 zookeeper 地址。
```
mysql> UPDATE TABLE_PARAMS set PARAM_VALUE  = '172.17.64.98,172.17.64.112,172.17.64.223' where PARAM_KEY = 'phoenix.zookeeper.quorum';    
```
10. 启动目标 Hive 服务 MetaStore、HiveServer2、WebHcataLog。
11. 最后可通过简单的 Hive sql 查询进行验证。

 
