## 数据导入
### INSERT 直接写入数据
通过 INSERT 语句直接向 TDSQL-A PostgreSQL版 的表中写入数据，使用 psql 客户端工具连接数据库后，INSERT INTO … VALUES 或者 INSERT INTO…SELECT 写入数据，TDSQL-A PostgreSQL版 也支持 JDBC、ODBC、Python、CAPI、ADO.net 等接口方式连接数据库，来执行 INSERT 语句向 TDSQL-A PostgreSQL 版 表中写入数据。

### COPY FROM 导入数据
除 INSERT 外，TDSQL-A PostgreSQL版 支持通过 COPY 命令，在文件和表之间复制数据，其语法格式如下：
```
COPY table_name [ ( column_name [, ...] ) ]
  FROM { 'filename' | PROGRAM 'command' | STDIN }
  [ [ WITH ] ( option [, ...] ) ]
COPY { table_name [ ( column_name [, ...] ) ] | ( query ) }
  TO { 'filename' | PROGRAM 'command' | STDOUT }
  [ [ WITH ] ( option [, ...] ) ]
```
其中 option 可以是下列之一：
```
FORMAT format_name
OIDS [ boolean ]
FREEZE [ boolean ]
DELIMITER 'delimiter_character'
NULL 'null_string'
HEADER [ boolean ]
QUOTE 'quote_character'
ESCAPE 'escape_character'
FORCE_QUOTE { ( column_name [, ...] ) | * }
FORCE_NOT_NULL ( column_name [, ...] )
FORCE_NULL ( column_name [, ...] )
ENCODING 'encoding_name'
```
带一个文件名的 COPY 指示 TDSQL-A PostgreSQL版 服务器直接从一个文件读取或者写入到一个文件。该文件必须是运行TDSQL-A PostgreSQL版 服务器的用户可访问的并且应该以服务器的视角来指定其名称。
当指定了 PROGRAM 时，服务器执行给定的命令，并且从该程序的标准输出读取或者写入到该程序的标准输入。该程序必须以服务器的视角指定，并且必须是 tdapg 用户可执行的。
在指定 STDIN 或者 STDOUT 时，数据会通过客户端和服务器之间的连接传输。
另外，\COPY FROM/TO，用于将本地文件复制到数据表中或将数据表中数据复制到本地文件中。

#### 多种数据源加载
- STDIN 标准输入：
```
postgres=# COPY tdapg (id, mc) FROM stdin;
Enter data to be copied followed by a newline.
End with a backslash and a period on a line by itself.
>> 1  tdapg
>> 2  \N
>> 3  pgxc
>> \.
postgres=# select * from tdapg;
 id | mc  
----+-------
 1 | tdapg
 2 | 
 3 | pgxc
(3 rows)
```
- SFTP 数据源：
准备环境：安装 sftp 服务，将数据文件上传进 sftp 服务器。
```
postgres=# COPY copy_hdfs FROM PROGRAM 'hadoop fs -cat hdfs://10.183.208.190:9000/lineitem' DELIMITER '|';
COPY 797000000
```
- HTTP 数据源：
准备环境：安装 httpd 服务，并将数据文件上传到 HTTP 服务器。
```
postgres =# \COPY copy_http FROM PROGRAM 'curl -s http://10.183.208.191:8081/lineitem.csv' WITH csv DELIMITER ',';
COPY 797000000
```
- HDFS 数据源：
准备环境：安装 hadoop 服务并配置，将数据文件上传到 hadoop 服务上。
```
postgres =# COPY copy_hdfs FROM PROGRAM 'hadoop fs -cat hdfs://10.183.208.190:9000/lineitem' DELIMITER '|';
COPY 797000000
```

#### 多种数据格式加载
COPY 支持 CSV，TXT，GZIP，SNAPPY 等多种数据文件格式导入。

- CSV 文件导入：
```
postgres =# \COPY copy_csv FROM '/data12/copy_test_data/lineitem.csv' WITH csv DELIMITER ',';
COPY 797000000
```
- TXT 文件导入：
```
postgres =# \COPY copy_csv FROM '/data12/copy_test_data/lineitem.txt' WITH (FORMAT 'text', DELIMITER '|');
COPY 797000000
```
- SNAPPY 文件导入：
```
postgres=# \COPY copy_snappy FROM PROGRAM 'snzip -dc /data12/copy_test_data/lineitem.snappy' DELIMITER '|';
COPY 797000000
```
- GZIP 文件导入：
```
postgrs=# \COPY copy_gzip FROM PROGRAM 'tar -zxvf /data12/copy_test_data/lineitem.tar.gz | xargs cat' DELIMITER '|';
COPY 797000000
```
- LZO 文件导入：
```
postgres=# \COPY copy_lzop FROM PROGRAM 'lzop -cd /data12/copy_test_data/lineitem.lzo | more' DELIMITER '|'; 
COPY 797000000
```

## 数据导出
使用 COPY TO 或者 \COPY TO 将表数据复制到文件：
```
COPY copyperf_txt TO '/data12/copy_test_data/cpto/cpto1.dat' WITH(FORMAT csv, DELIMITER ',');
```

将表中数据导入到多个数据文件：
```
COPY copyperf_txt TO PROGRAM 'cd /data12/copy_test_data/cpto && split -l 39850000 -d -a 4 && ls | grep ^x | xargs -n1 -i{} mv {} perfcopyto_{}.csv' WITH csv DELIMITER ',';
```
