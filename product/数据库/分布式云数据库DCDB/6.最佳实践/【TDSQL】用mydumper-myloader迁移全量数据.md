## 1. 准备工作
在导出导入数据前，需要梳理待迁移的库表，改造 shardkey，然后在目标实例创建需要迁移的表结构，可参考 [数据表迁移](https://cloud.tencent.com/document/product/557/8637) 中表结构迁移的部分。

下载 [mydumper-myloader工具包](https://tdsql-demo-1309409385.cos.ap-guangzhou.myqcloud.com/mydumper-myloader-for-tdsql.tar.gz) 并将其解压到有较大剩余空间的磁盘中。

## 2. 导出源实例数据
找一个剩余容量大于实例规格的磁盘，将工具拷贝进数据备份目录，执行数据导出操作：

```
cd [数据备份目录]
./mydumper_tdsql  -B [数据库名] -T [表名]  -o [备份目录] -F 20 -m -c -h [源实例IP] -u [源实例用户名] -p [源实例密码] -P [源实例端口] -t 15 -N -k --complete-insert --statement-size 2000000 --less-locking --long-query-guard 86400 -v 3 -L dump.log
```

参数说明：
```
若导出整个库，则去掉 -T [表名] 参数即可。

-F 20 指定将表数据拆为多个小文件，每个文件 20MB

-m 表示不导出表结构

-c 表示将导出数据压缩后存放，减少存储空间（副作用是可能会使导出时间变长，建议根据实例数据量和磁盘可用空间酌情考虑是否开启压缩）

-t 15 表示开启15个线程导出

-N 表示将插入语句改写为 INSERT IGNORE 语法，导入新建的表可以不加该参数

-k 表示不加读锁

--complete-insert 表示生成完整的插入语句（TDSQL 分布式实例要求插入语句指定列名）

--statement-size 2000000 指定生成的语句大小不超过2000000字节（约2MB）

--less-locking 表示尽量少的锁表

--long-query-guard 86400 指定单个查询的时长不超过 86400s（1天，相当于不限制查询时长）

-v 3 表示开启 info 日志级别

-L dump.log 表示将导出的日志写到 dump.log 中
```

> ?建议指定数据库进行导出。若导出整个实例，请删除所有系统库的数据，常见系统库有：sys，mysql，SysDB，test。

## 3. 导入目标实例
将数据拷贝到能访问分布式数据库实例的机器上，然后执行下面的命令进行导入。

```
cd [数据备份目录]
./myloader_tdsql -d [备份目录] -B [数据库名]-h [源实例IP] -u [源实例用户名] -p [源实例密码] -P [源实例端口] -t 20 -v 3 -e
```

参数说明：
```
-t 20 表示开启20个线程执行导入

-v 3 表示开启 info 日志级别

-e 表示导入时开启 binlog，否则导入的数据将不会同步到备机
```
 
> ? 导入到分布式实例时，请勿指定-o参数，否则可能导入一堆单表。
