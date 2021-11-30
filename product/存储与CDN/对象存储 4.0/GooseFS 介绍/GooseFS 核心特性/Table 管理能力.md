## Table 管理能力概述

GooseFS Table 管理能力用于管理结构化数据，为 SparkSQL、Hive、Presto 等上层计算应用提供数据库表管理能力，目前底层支持对接 Hive MetaStore。Table 管理能力能够帮助各类 SQL 引擎读取指定的数据内容，能够有效提升大数据场景下对数据的访问效率。

![](https://main.qcloudimg.com/raw/e35a2c0320da700c3af72deefece71f5.png)          

GooseFS Table 管理能力目前主要支持了以下特性：

- 元数据层面的描述能力。GooseFS Catalog 提供源自远程元数据服务（Hive MetaStore）的元数据缓存服务，针对 SparkSQL，Hive，SQL Presto 等 SQL 引擎做查询时，可以根据 GooseFS Catalog 中的元数据缓存服务来确定读取数据大小、目标数据位置以及数据结构，具备与 Hive MetaStore 相同的能力表现。
- 表级数据预缓存能力。GooseFS Catalog 能够感知数据表和数据存储路径的对应关系，进而可以提供 Table 级别以及 Table Partition 级别的缓存预热能力，帮助用户提前按照表结构缓存数据，极大提高访问性能。
- 跨存储服务的统一元数据服务。通过 GooseFS Catalog 运行上层计算应用，可以同时对不同的底层存储系统提供访问加速能力。同时 GooseFS Catalog 可以提供跨越存储服务的统一元数据查询能力，只需要一个 GooseFS 客户端开启 Catalog 功能，即可查询不同存储系统，例如 HDFS、COS、CHDFS 中的数据。

## 使用 GooseFS Table 管理能力

GooseFS Table 管理能力通过 goosefs table 指令集实现，提供了 DB 的绑定和解绑、查询 DB 信息、查询表信息、数据加载、数据淘汰等能力。GooseFS Table 管理指令集如下所示：

```plaintext
$ goosefs table
Usage: goosefs table [generic options]
	 [attachdb [-o|--option <key=value>] [--db <goosefs db name>] [--ignore-sync-errors] <udb type> <udb connection uri> <udb db name>]
	 [detachdb <db name>]                                      
	 [free <dbName> <tableName> [-p|--partition <partitionSpec>]]
	 [load <dbName> <tableName> [-g|--greedy] [--replication <num>] [-p|--partition <partitionSpec>]]
	 [ls [<db name> [<table name>]]]                           
	 [stat <dbName> <tableName>]                               
	 [sync <db name>]                                          
```

上述指令集中各项指令的能力简述如下：

- attachdb：挂载数据库，将一个远端数据库绑定到 GooseFS 上，目前仅支持 Hive MetaStore。
- detachdb：卸载数据库，将 GooseFS 上绑定的数据库解绑。
- free：清除指定 DB.Table 的数据缓存，可支持 Partition 粒度。
- load：缓存指定 DB.Table 的数据，可支持 partition 粒度，支持通过 replication 设置缓存的副本数。
- ls：列出指定 DB 或 DB.Table 的元数据信息。
- stat：查询指定 DB.Table 的文件数目、总大小、以及缓存百分比。
- sync：同步指定 DB 的内容。
- transform：将指定 DB 关联的 Table 转换为新的 Table。
- transformStatus：Table 转换的进度情况。

### 1. 挂载 DB

预热指定 Table 数据到 GooseFS 之前，需要将对应的 DB 挂载到 GooseFS 上。如下指令展示了将指定地址 metastore_host:port 中的数据库 goosefs_db_demo 挂载到 GooseFS 中，并将该 DB 在 GooseFS 中命名为 test_db：

```plaintext
$ goosefs table attachdb --db test_db hive thrift://metastore_host:port goosefs_db_demo

response of attachdb
```

>! metastore_host:port 可以替换为任意合法可连接的 Hive MetaStore 地址。
>

### 2. 查看 Table 信息

绑定完数据库后，可以通过 ls 指令查看已挂载的 DB 和 Table 信息，如下指令展示了如何查询 test_db 中的 web_page 表信息：

```plaintext
$ goosefs table ls test_db web_page
 
OWNER: hadoop
DBNAME.TABLENAME: testdb.web_page (
   wp_web_page_sk bigint,
   wp_web_page_id string,
   wp_rec_start_date string,
   wp_rec_end_date string,
   wp_creation_date_sk bigint,
   wp_access_date_sk bigint,
   wp_autogen_flag string,
   wp_customer_sk bigint,
   wp_url string,
   wp_type string,
   wp_char_count int,
   wp_link_count int,
   wp_image_count int,
   wp_max_ad_count int,
)
PARTITIONED BY (
)
LOCATION (
   gfs://metastore_host:port/myiNamespace/3000/web_page
)
PARTITION LIST (
   {
   partitionName: web_page
   location: gfs://metastore_host:port/myNamespace/3000/web_page
   }
)
```


### 3. 预热 Table 中的数据

预热 Table 的指令下发后会在后台发起一个异步作业，GooseFS 会在启动作业后返回一个作业 ID，可以通过 `job stat <ID>` 指令查询任务的运行状态，同时可以通过 `table stat` 指令查看预热百分比。预热指令如下：

```plaintext
$ goosefs table load test_db web_page
Asynchronous job submitted successfully, jobId: 1615966078836
```


### 4. 查看 Table 预热情况

通过 `job stat` 指令可以查看预热 Table 作业的执行进度。当状态为 COMPLETED 时，整个预热过程完成，如果状态为 FAILED，可以在 master.log 文件中查看日志记录，排查预热错误的原因：

```plaintext
$ goosefs job stat 1615966078836
COMPLETED
```

当 Table 完成预热后，可以通过 stat 指令查看指定 Table 的概况。

```plaintext
$ goosefs table stat test_db web_page
detail
```


### 5. 释放 Table

通过以下指令可以从 GooseFS 中释放指定 Table 数据缓存：

```plaintext
$ goosefs table free test_db web_page
detail
```


### 6. 卸载 DB

通过以下指令可以从 GooseFS 中卸载指定 DB:

```plaintext
$ goosefs table detachdb test_db
detail
```
