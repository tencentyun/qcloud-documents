## 背景
数据库作为数据存放、处理、加⼯的核⼼组件，随着业务的发展，其数据量会越来越⼤；由于时间或业务设计逻辑的原因，会存在部分历史数据、归档数据。而业务对此类数据的访问并不频繁，但又不能删除，因为在某些场景下会使⽤到这些数据。为了提升数据库的处理性能，需要将此类数据进⾏落冷处理。

对于数据库而言，如何最⼤化地存储数据以及更好的提供统⼀数据处理接⼝尤为重要，腾讯云数据库 PostgreSQL 针对此类用户需求，提供数据分级存储方案。其核心原理是⽀持多种成本的存储介质，供⽤户选择使⽤。如，可使冷数据存放于性能略低，但成本低的存储中，将热数据存放于成本较⾼，但性能更强的高性能 SSD 中。更好的服务⽤户，保证业务的正常运行，并且兼顾⽤户成本，是⼀种极具性价⽐的存储⽅案。

## 方案简介
腾讯云 COS 是腾讯云提供的对象存储服务。分级存储当前实现的能力主要是基于 cos_fdw 插件连接和解析 COS 上的⽂件数据。
通过 cos_fdw 插件可以将 COS 中的数据加载到 PostgreSQL 数据库表中，像访问普通表⼀样访问 COS 中的数据，实现冷热存储分离。⽤户无需关心不同存储介质的访问形式，仅需要将 COS 存储中的数据文件配置到 PostgreSQL 数据库中即可。

## 方案优势
- **统⼀引擎**：多种存储介质，⽆需业务层改动代码，直接使用 PostgreSQL 数据协议均可实现统⼀访问。
- **成本更低**：相对⾼性能 SSD 存储，整体成本降低 86.25%。
- **使用简单**：用户仅需要将源端数据导出 CSV 格式存放于 COS 中，在云数据库 PostgreSQL 基于插件进⾏外表创建，即可像原表⼀样直接使用。
- **无限存储**：COS 存储容量不设上限，⽤户可以根据实际情况进行动态存储，不再担心容量问题。
- **⽀持联合查询表**：多种存储的表⽀持联合查询，跨区 join 等，这在其他混合引擎上是⽆法直接实现的，均需要⼀个统一的数据融合节点才能⽀持。

## 支持版本
目前分级存储⽀持以下版本的云数据库 PostgreSQL：
- PostgreSQL 10
- PostgreSQL 11
- PostgreSQL 12
- PostgreSQL 13
- PostgreSQL 14

## 使用 cos_fdw 的方法
需要按照以下顺序使⽤ cos_fdw ：
1. 导出数据。
2. 上传⾄ COS。
3. 创建 cos_fdw 插件。
4. 创建 Foreign Server。
5. 创建 Foreign Table。
6. 查询外部表。

## 初始化环境
⾸先申请⼀个在数据库与 COS 同地域，同可⽤区的规格较小的中转服务器如 CVM。
操作系统建议为：Centos 7。
1. 安装 PostgreSQL 客户端，可参考 [PostgreSQL 官网下载安装方案](https://www.postgresql.org/download/linux/redhat/)。
```
sudo yum install -y 
https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-
x86_64/pgdg-redhat-repo-latest.noarch.rpm
sudo yum install -y postgresql13
```
2. 安装完成后，可使⽤ psql 命令访问⼀下数据库，查看是否安装完成，命令如下：
```
psql -Uroot -p 5432 -h 10.x.x.8 -d postgres
Password for user root: 
psql (13.6, server 13.3)
Type "help" for help.

postgres=>
```
3. PostgerSQL 客户端⼯具安装完成后，进⾏ COS 挂载。这里我们通过 COSFS 挂载到服务器上的形式来进行，可避免需要更⼤容量的 CVM 进⾏转储上传。请参见 [通过 COSFS 挂载](https://cloud.tencent.com/document/product/436/6883)。
4. 针对当前环境，可执⾏以下命令安装依赖包。
```
sudo yum install libxml2-devel libcurl-devel -y
```
5. 访问 COSFS 的 [github 下载地址](https://github.com/tencentyun/cosfs/releases/download/v1.0.19/cosfs-1.0.19-centos7.0.x86_64.rpm)，下载 COSFS 的安装包。
6. 下载完成后将此安装包上传⾄此服务器中。再执⾏下列命令将 COSFS 安装成功。
```
rpm -ivh cosfs-1.0.19-centos7.0.x86_64.rpm
```
>!如确定依赖包安装完成，但是依然⽆法安装成功 COSFS 的，可以在上⾯命令中加⼊ --force 参数强制安装。
7. 安装完成 COSFS 后，执⾏以下命令，将 COS 桶挂载到中转服务器中。
```
echo <BucketName-APPID>:<SecretId>:<SecretKey> > /etc/passwd-cosfs
chmod 640 /etc/passwd-cosfs
cosfs <BucketName-APPID> <MountPoint> -ourl=http://cos.<Region>.myqcloud.c
om -odbglevel=info -oallow_other
```
 - BucketName-APPID 为存储桶名称格式。
 - SecretId 和 SecretKey 为密钥信息。
8. 挂载完成后，可进入到挂载目录中，拷贝⼀个⽂件进⾏测试。查看是否挂载成功。亦可执行 df -h 查看挂载情况：
```
[root@VM-4-17-centos ~]# df -h
Filesystem Size Used Avail Use% Mounted on
devtmpfs 1.9G 0 1.9G 0% /dev
tmpfs 1.9G 0 1.9G 0% /dev/shm
tmpfs 1.9G 472K 1.9G 1% /run
tmpfs 1.9G 0 1.9G 0% /sys/fs/cgroup
/dev/vda1 50G 3.0G 44G 7% /
tmpfs 379M 0 379M 0% /run/user/0
cosfs 256T 0 256T 0% /mnt/pgstorage
```

## 导出数据
挂载完成后，即可进⾏数据导出。
如果存在⼀张表 sensor_log，表结构如下：
```
CREATE TABLE sensor_log (
 sensor_log_id SERIAL PRIMARY KEY,
 location VARCHAR NOT NULL,
 reading BIGINT NOT NULL,
 reading_date TIMESTAMP NOT NULL
);
CREATE INDEX idx_sensor_log_location ON sensor_log (location);
CREATE INDEX idx_sensor_log_date ON sensor_log (reading_date);
insert into sensor_log(location,reading,reading_date) values('38c-
1401',293857,current_timestamp);
insert into sensor_log(location,reading,reading_date) values('38c-
1402',293858,current_timestamp);
insert into sensor_log(location,reading,reading_date) values('34c-
1401',293859,current_timestamp);
insert into sensor_log(location,reading,reading_date) values('18c-
1401',2938510,current_timestamp);
```

如果使用 psql 客户端进行数据导出，可按照以下流程进行操作，注意导出不要带 header。
**导出整张表**：
```
psql -U root -p 5432 -h 10.0.4.8 -d hehe -c \COPY sensor_log 
(sensor_log_id,location, reading,reading_date) TO '/mnt/xxx/sensor_log.csv' WITH 
csv;
```

**指定数据导出（支持数据筛选，过滤，多表联合，视图等场景）**：
```
psql -U root -p 5432 -h 10.0.4.8 -d hehe -c '\COPY (select * from sensor_log 
where location='18c-1401') TO '/mnt/pgstorage/sensor_log.csv' WITH csv;'
```
上面的语句执⾏完成后，就可以在 COS 桶对应⽬录中找到导出的⽂件。
导入到 COS 的 csv 文件不需要带列名。

## 创建插件
cos_fdw 插件会对 COS 的 secret id 和 secret key 进⾏加密处理，加密算法依赖于 pgcrypto 插件，因此我们在使⽤时需要先安装 pgcrypto 插件。
```
CREATE EXTENSION pgcrypto;
CREATE EXTENSION cos_fdw;
```

## 创建 Foreign Server
```
CREATE SERVER cos_server FOREIGN DATA WRAPPER cos_fdw OPTIONS(
 host 'xxxxxx.cos.ap-nanjing.myqcloud.com',
 bucket 'xxxxxxxx',
 id 'xxxxxxxx',
 key 'xxxxxxxxxx'
);
```

>!
>- host 中配置的域名为 COS 桶的访问地址，地址前缀协议不需要带 http 或 https。
>- Foreign Server 中的 id 和 key 属于敏感信息，cos_fdw 会对其进⾏加密存储。不同的实例将会使⽤不同的密钥，最⼤限度保护用户信息。我们可以⽤ `SELECT * FROM pg_foreign_server；`看到。

## 创建 COS 外部表
```
CREATE FOREIGN TABLE test_csv (
 word1 text OPTIONS (force_not_null 'true'),
 word2 text OPTIONS (force_not_null 'off') ) SERVER cos_server OPTIONS (
 filepath '/test.csv',
 format 'csv',
 null 'NULL'
);
```
cos_fdw ⽀持将多个 COS ⽂件可以映射到同⼀个 FOREIGN TABLE 中，在 filepath 参数中填写多个⽂件名，每个⽂件用 `,` 分隔即可（不允许出现多余空格）。

```
CREATE FOREIGN TABLE multi_csv (
 word1 text OPTIONS (force_not_null 'true'),
 word2 text OPTIONS (force_not_null 'off') ) SERVER cos_server OPTIONS (
 filepath '/a.csv,/b.csv,/c.csv.2',
 format 'csv',
 null 'NULL'
);
```

## 查询外部表
### 规划查询计划
cos_fdw 能够预估外部文件的大小，为查询计划做规划。对于映射了多个 COS 文件的外部表，将会把它们每⼀个的文件大小打印出来，并计算出来所有文件的总大小。
```
-- 单⼀⽂件
postgres=# EXPLAIN SELECT * FROM test_csv;
 QUERY PLAN 
-----------------------------------------------------------------
--------------
Foreign Scan on test_csv (cost=0.00..1.10 rows=1 width=128)
 Foreign COS Url: https://xxxxxxx.cos.ap-nanjing.myqcloud.com
 Foreign COS File Path: /test_csv.csv
 Foreign each COS File Size(Bytes): 86
 Foreign total COS File Size(Bytes): 86
(5 rows)
-- 多个⽂件
postgres=# EXPLAIN SELECT * FROM multi_csv;
 QUERY PLAN 
-----------------------------------------------------------------
---------------
Foreign Scan on multi_csv (cost=0.00..1.20 rows=2 width=128)
 Foreign COS Url: https://xxxxxxxxxx.cos.ap-nanjing.myqcloud.com
 Foreign COS File Path: /a.csv,/b.csv,/c.csv.2
 Foreign each COS File Size(Bytes): 15,172,86
 Foreign total COS File Size(Bytes): 273
(5 rows)
```

### 查询数据
```
postgres=# SELECT * FROM test_csv;
word1 | word2 | word3 | word4 
-------+-------+-------+-------
AAA | aaa | 123 |
XYZ | xyz | | 321
NULL | | |
NULL | | |
ABC | abc | | (5 rows)
```

### 将外部表数据导入本地表
可以使⽤ `insert into ... select * from ...;` 类似的语句将外部表的数据导入本地表中。
```
postgres=# CREATE TABLE local_test_csv (
postgres(# a text,
postgres(# b text,
postgres(# c text,
postgres(# d text
postgres(# );
CREATE TABLE
postgres=# INSERT INTO local_test_csv SELECT * FROM test_csv;
INSERT 0 5
postgres=# SELECT * FROM local_test_csv;
 a | b | c | d 
------+-----+-----+-----
AAA | aaa | 123 |
XYZ | xyz | | 321
NULL | | |
NULL | | |
ABC | abc | | (5 rows)
```

### 分区表查询
```
postgres=# CREATE TABLE pt (a int, b text) partition by list (a);
CREATE TABLE
postgres=# CREATE FOREIGN TABLE p1 partition of pt for values in (1) SERVER
cos_server
postgres-# OPTIONS (format 'csv', filepath '/list1.csv', delimiter ',');
CREATE FOREIGN TABLE
postgres=# CREATE TABLE p2 partition of pt for values in (2);
CREATE TABLE
-- 分区表⽀持查询
postgres=# SELECT tableoid::regclass, * FROM pt;
tableoid | a | b 
----------+---+-----
p1 | 1 | foo
p1 | 1 | bar
(2 rows)
postgres=# SELECT tableoid::regclass, * FROM p1;
tableoid | a | b 
----------+---+-----
p1 | 1 | foo
p1 | 1 | bar
(2 rows)
postgres=# SELECT tableoid::regclass, * FROM p2;
tableoid | a | b 
----------+---+---
(0 rows)
-- ⽬前不⽀持往外部表中写⼊数据
postgres=# INSERT INTO pt VALUES (1, 'xyzzy'); -- ERROR
ERROR: cannot route inserted tuples to a foreign table
-- 本地表不受影响，可以正常往分区表中写⼊
postgres=# INSERT INTO pt VALUES (2, 'xyzzy');
INSERT 0 1
postgres=# SELECT tableoid::regclass, * FROM pt;
tableoid | a | b 
----------+---+-------
p1 | 1 | foo
p1 | 1 | bar
p2 | 2 | xyzzy
(3 rows)
postgres=# SELECT tableoid::regclass, * FROM p1;
tableoid | a | b 
----------+---+-----
p1 | 1 | foo
p1 | 1 | bar
(2 rows)
postgres=# SELECT tableoid::regclass, * FROM p2;
tableoid | a | b 
----------+---+-------
p2 | 2 | xyzzy
(1 row)
```

## 删除插件
```
DROP EXTENSION cos_fdw;
```

## 参数说明
**CERATE SERVER 参数**

| 参数 | 说明 | 
|---------|---------|
| host | 内网访问 COS 的地址，注意 host 不包含 http/https 前缀 | 
| bucket | 存储桶名称，存储桶的命名格式为 BucketName-APPID，此处填写的存储桶名称必须为此格式 | 
| id | 账号的 secret id | 
| key | 账号的 secret key | 

**CREATE FOREIGN TABLE 参数**

| 参数 | 说明 | 
|---------|---------|
| filepath | Sample | 
| format | 指定数据的格式，⽬前仅⽀持 csv | 
| delimiter | 指定数据的分隔符 | 
| quote | 指定数据的引⽤字符 | 
| escape | 指定数据的转义字符 | 
| encoding | 指定数据的编码 | 
| null | 指定匹配对应字符串的列为 null，例如 null ‘NULL’，即列值为 ’NULL’ 的字符串为 null  | 
| force_not_null | 指定该列的值不应该与空字符串匹配。例如，force_not_null ‘id’ 表示：如果 id 列的值为空，则该值为空字符串，而不是 null  | 
| force_null | 指定该列的值与空字符串匹配。例如，force_null ‘id’ 表示：如果 id 列的值为空，则该值为 null | 

## 错误处理
当使用 cos_fdw 向 COS 请求数据超时，会显示以下内容：
- code：出错请求的 HTTP 状态码。
- 错误请求的 HTTP header：显示错误的信息。其格式参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729)。其中 `x-cos-request-id` 可以⽤于寻求 [在线支持](https://cloud.tencent.com/online-service) 排查问题。如果该项为空，表示未成功向 COS 发送请求。

```
• postgres=# SELECT * FROM test_csv; • ERROR: COS api return error. • DETAIL: COS api http status:403
• HTTP/1.1 403 Forbidden
• Content-Type: application/xml
• Content-Length: 0 • Connection: keep-alive
• Date: Thu, 07 Apr 2022 09:00:22 GMT
• Server: tencent-cos
• x-cos-request-id: NjI0ZWE4MjZfNDc1NGU0MDlfMjI3ZTJfMTI3YTJjMWM= 
• x-cos-trace-id:
OGVmYzZiMmQzYjA2OWNhODk0NTRkMTBiOWVmMDAxODc0OWRkZjk0ZDM1NmI1M2E2MTRlY2MzZDhmNmI5MWI1OTBjYzE2MjAxN2M1MzJiOTdkZjMxMDVlYTZjN2FiMmI0MWMyZGYxMDAyZmVmMjNkZDQ5NGViMDhiZWJkOTE2YzI=
```

