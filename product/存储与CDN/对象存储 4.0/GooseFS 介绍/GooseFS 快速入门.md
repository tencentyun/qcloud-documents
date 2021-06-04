
本文档主要提供 GooseFS 快速部署、调试的相关指引，提供在本地机器上部署 GooseFS ，并将对象存储 COS 作为远端存储的步骤指引，具体步骤请见下。


## 前提条件

在使用 GooseFS 之前，您还需要准备以下工作：

1. 在对象存储 COS 服务上创建一个存储桶以作为远端存储，操作指引请参见 [对象存储快速入门](https://cloud.tencent.com/document/product/436/38484)。
2. 安装 [JAVA 8 或者更高的版本](https://www.oracle.com/java/technologies/javase/javase-jdk8-downloads.html)。
3. 安装 [SSH](https://www.ssh.com/ssh/)，确保能通过 SSH 连接到 LocalHost，并远程登录。

## 下载并配置 GooseFS

1. 从官方 Github 下载 GooseFS 安装包到本地。
2. 按照如下命令对安装包进行解压。
```plaintext
tar-xzf goosefs-1.0.0-bin.tar.gz
cd goosefs-1.0.0
```
3. 解压后，GooseFS 安装包的源文件和 JAVA 二进制文件均会存储在 goosefs-1.0.0 的文件夹下，本指南中通过`${GOOSEFS_HOME}`引用。
4. 在`${GOOSEFS_HOME}/conf`的目录下创建`conf/goosefs-site.properties`的配置文件，可以使用内置的配置模板：
```plaintext
$ cp conf/goosefs-site.properties.template conf/goosefs-site.properties
```
5. 在配置文件`conf/goosefs-site.properties`中，将 goosefs.master.hostname 设置为`localhost`：
```plaintext
$ echo"goosefs.master.hostname=localhost">> conf/goosefs-site.properties
```

## 启用 GooseFS 

1. 启用 GooseFS 之前建议先进行系统环境检查，确保 GooseFS 可以在本地环境中正确运行：
```plaintext
$ goosefs validateEnv local
```
 >?使用该命令可以查看 GooseFS 的运行情况。
2. 启用 GooseFS 之前对 GooseFS 进行格式化，该命令将清除 GooseFS 的日志和 `worker`存储目录下的内容：
```plaintext
$ goosefs format
```
3. 使用如下指令可以启用 GooseFS，在系统默认配置下，GooseFS 会启动一个  Master  和一个  Worker ：
```plaintext
$ ./bin/goosefs-start.sh local SudoMount
```
该命令执行完毕后，可以访问 http://localhost:19999 和 http://localhost:30000 ，分别查看  Master 和 Worker 的运行状态。

## 使用 GooseFS 挂载对象存储 COS
1. 创建一个命名空间 Namespace 并挂载对象存储 COS ：

```plaintext
$ goosefs ns create myNamespace cosn://bucketName-125xxxxxx/ 3TB
--option fs.cosn.userinfo.secretId=AKIDxxxxxxxxxxxxxx \
--option fs.cosn.userinfo.secretKey=xxxxxxxxxxxxxxxxx \
--option fs.cosn.bucket.region=ap-guangzhou \
```

>!在创建 Namespace 的时候必须指定 –-option 参数，并且指定 Hadoop-COS（COSN）所有必选参数，具体的必选参数可参考 [Hadoop 工具](https://cloud.tencent.com/document/product/436/6884)。创建 Namespace 的时候，如果没有指定读写策略（rPolicy/wPolicy），默认会使用配置文件中指定的 read/write type，或使用默认值（CACHE/CACHE_THROUGH）。

2. 挂载成功后，可以通过 ls 指令列出集群中创建的所有 namespace，如下指令所示：

```plaintext
$ goosefs ns list
myNamespace    /myNamespace   cosn://bucketName-125xxxxxx/3TB  CACHE_THROUGH      CACHE        -1      DELETE
```

3. 如果只需要了解指定 namespace 的详细信息，可以通过如下指令实现：

```plaintext
$ goosefs ns stat myNamespace
 
NamespaceStatus{name=myNamespace, path=/myNamespace, ttlTime=-1, ttlAction=DELETE, ufsPath=cosn://bucketName-125xxxxxx/3TB, creationTimeMs=1615434186076, lastModificationTimeMs=1615436308143, lastAccessTimeMs=1615436308143, persistenceState=PERSISTED, mountPoint=true, mountId=4948824396519771065, acl=user::rwx,group::rwx,other::rwx, defaultAcl=, owner=user1, group=user1, mode=511, writePolicy=CACHE_THROUGH, readPolicy=CACHE}
```

元数据中记录的信息包括如下内容：

| 序号 | 参数                   |
| ---- | ---------------------- |
| 1    | name                   |
| 2    | path                   |
| 3    | ttlTime                |
| 4    | ttlAction              |
| 5    | ufsPath                |
| 6    | creationTimeMs         |
| 7    | lastModificationTimeMs |
| 8    | persistenceState       |
| 9    | mountPoint             |
| 10   | mountId                |
| 11   | acl                    |
| 12   | defaultAcl             |
| 13   | owner                  |
| 14   | group                  |
| 15   | mode                   |
| 16   | writePolicy            |
| 17   | readPolicy             |


## 使用 GooseFS 预热 Table 中的数据

1. GooseFS 支持将 Hive Table 中的数据预热dao  GooseFS中，在预热之前需要先将相关的 DB 关联到 GooseFS 上，相关指令如下：
```plaintext
$ goosefs table attachdb --db test_db hive thrift://
172.16.16.22:7004 test_for_demo
```

>!指令中的 thrift 需要填写实际的 Hive Metastore 的地址。

2. 添加完 DB 后，可以通过 ls 指令查看当前关联的 DB 和 Table 的信息：

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
   gfs://172.16.16.22:19998/myNamespace/3000/web_page
)
PARTITION LIST (
   {
   partitionName: web_page
   location: gfs://172.16.16.22:19998/myNamespace/3000/web_page
   }
)
```

3. 通过 load 指令预热 Table 中的数据：
```plaintext
$ goosefs table load test_db web_page
Asynchronous job submitted successfully, jobId: 1615966078836
```

预热 Table 中的数据是一个异步任务，因此会返回一个任务 ID。可以通过 goosefs job stat <Job Id> 指令查看预热作业的执行进度。当状态为"COMPLETED"后，则整个预热过程完成。

## 使用 GooseFS 进行文件上传和下载操作

1. GooseFS 支持绝大部分文件系统操作指令，可以通过以下命令来查询当前支持的命令列表：
```plaintext
$ goosefs fs
```
2. 可以通过`ls`指令列出 GooseFS 中的文件，以下示例展示如何列出根目录下的所有文件：
```plaintext
$ goosefs fs ls /
```
3. 可以通过`copyFromLocal`指令将数据从本地拷贝到 GooseFS 中：
```plaintext
$ goosefs fs copyFromLocal LICENSE /LICENSE
Copied LICENSE to /LICENSE
$ goosefs fs ls /LICENSE
-rw-r--r--  hadoop         supergroup               20798       NOT_PERSISTED 03-26-2021 16:49:37:215   0% /LICENSE
```
4. 可以通过`cat`命令查看文件内容：
```plaintext
$ goosefs fs cat /LICENSE                                                                         
Apache License
Version 2.0, January 2004
http://www.apache.org/licenses/
TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION
...
```
5. GooseFS 默认使用本地磁盘作为底层文件系统，默认文件系统路径为`./underFSStorage`，可以通过`persist`指令将文件持久化存储到本地文件系统中：
```plaintext
$ goosefs fs persist /LICENSE
persisted file /LICENSE with size 26847
```

## 使用 GooseFS 加速文件上传和下载操作

1. 检查文件存储状态，确认文件是否已被缓存。文件状态`PERSISTED`代表文件已在内存中，文件状态`NOT_PERSISTED`则代表文件不在内存中：
```plaintext
$ goosefs fs ls /data/cos/sample_tweets_150m.csv
-r-x------ staff  staff 157046046 NOT_PERSISTED 01-09-2018 16:35:01:002   0% /data/cos/sample_tweets_150m.csv
```
2. 统计文件中有多少单词“tencent”，并计算操作耗时：
```plaintext
$ time goosefs fs cat /data/s3/sample_tweets_150m.csv | grep-c kitten
889
real	0m22.857s
user	0m7.557s
sys	0m1.181s
```
3. 将该数据缓存到内存中可以有效提升查询速度，详细示例如下：
```plaintext
$ goosefs fs ls /data/cos/sample_tweets_150m.csv
-r-x------ staff  staff 157046046 PERSISTED 01-09-2018 16:35:01:002   0% /data/cos/sample_tweets_150m.csv
$ time goosefs fs cat /data/s3/sample_tweets_150m.csv | grep-c kitten
889
real	0m1.917s
user	0m2.306s
sys	    0m0.243s
```

可见，系统处理延迟从1.181s减少到了0.243s，得到了10倍的提升。

## 关闭 GooseFS

通过如下指令可以关闭 GooseFS：
```plaintext
$ ./bin/goosefs-stop.sh local
```

