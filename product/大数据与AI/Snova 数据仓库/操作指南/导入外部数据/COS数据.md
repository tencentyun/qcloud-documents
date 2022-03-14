## 使用 COS_EXT 查询 COS 数据
COS_EXT 是访问 COS 文件的外部数据访问插件，通过 DDL 定义外部表，可以按照普通的数据表执行 DML，实现对 COS 数据的操作。目前支持：
- 作为外表，读取 COS 数据。
- 作为外表，将结果导出到 COS。
- 作为外表，执行简单分析功能，分析 COS 数据。

### 注意事项
1. 支持 CSV 等文本格式文件，以及 GZIP 压缩格式文件。
2. 只能读取本地域的 COS 数据，例如，广州四区的集群只能读取广州地域的 COS 数据。
3. 只能读取用户自己的 COS 数据（这里用户是指创建集群的用户）。
4. 只写外表只能用于 INSERT 语句，不能用于 UPDATE/DELETE 语句，不能用于 SELECT 查询语句。
5. 删除外表，不会删除 COS 上的数据。

### 使用步骤
1. 定义 cos_ext 插件。
>!COS 外表插件的作用域为库。
>
 - 创建命令如下：
```
CREATE EXTENSION IF NOT EXISTS cos_ext SCHEMA public;
```
 - 删除命令如下：
```
DROP EXTENSION IF EXISTS cos_ext;
```
2. 定义 COS 外表，语法参考 [语法说明](#codeintro)。
3. 操作 COS 外表数据。

[](id:codeintro)
### 语法说明
- 只读输入表定义
```
   CREATE [READABLE] EXTERNAL TABLE tablename
   ( columnname datatype [, ...] | LIKE othertable )
   LOCATION (cos_ext_params)
   FORMAT 'TEXT'
		 [( [HEADER]
				[DELIMITER [AS] 'delimiter' | 'OFF']
				[NULL [AS] 'null string']
				[ESCAPE [AS] 'escape' | 'OFF']
				[NEWLINE [ AS ] 'LF' | 'CR' | 'CRLF']
				[FILL MISSING FIELDS] )]
		| 'CSV'
		 [( [HEADER]
				[QUOTE [AS] 'quote']
				[DELIMITER [AS] 'delimiter']
				[NULL [AS] 'null string']
				[FORCE NOT NULL column [, ...]]
				[ESCAPE [AS] 'escape']
				[NEWLINE [ AS ] 'LF' | 'CR' | 'CRLF']
				[FILL MISSING FIELDS] )]
   [ ENCODING 'encoding' ]
   [ [LOG ERRORS [INTO error_table]] SEGMENT REJECT LIMIT count
          [ROWS | PERCENT] ]
```
- 只写输出表定义
```
   CREATE WRITABLE EXTERNAL TABLE table_name
   ( column_name data_type [, ...] | LIKE other_table )
   LOCATION (cos_ext_params)
   FORMAT 'TEXT'
			[( [DELIMITER [AS] 'delimiter']
			[NULL [AS] 'null string']
			[ESCAPE [AS] 'escape' | 'OFF'] )]
		| 'CSV'
			[([QUOTE [AS] 'quote']
			[DELIMITER [AS] 'delimiter']
			[NULL [AS] 'null string']
			[FORCE QUOTE column [, ...] ]
			[ESCAPE [AS] 'escape'] )]
   [ ENCODING 'encoding' ]
   [ DISTRIBUTED BY (column, [ ... ] ) | DISTRIBUTED RANDOMLY ]
```
3. cos_ext_params 说明
```
cos://cos_endpoint/bucket/prefix secretId=id secretKey=key compressType=[none|gzip] https=[true|false]
```


### 参数说明

| 参数         | 格式              | 必填 | 说明                            |
| ------------ | ------------------------------------ | ---- | --------------------------------------- |
| URL          | <li/>COS V4：`cos://cos.{REGION}.myqcloud.com/{BUCKET}/{PREFIX}`<li/>COS V5：`cos:// {BUCKET}-{APPID}.cos.{REGION}.myqcloud.com/{PREFIX}`  | 是   | 参见 [URL 参数说明](#url)                |
| secretId     | 无         | 是   | 访问 API 使用的密钥 ID，参见 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) |
| secretKey    | 无     | 是   | 访问 API 使用的密钥 ID，参见 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) |
| HTTPS        | true &Iota; false       | 否   | 是否使用 HTTPS 访问 COS，默认为 true        |
| compressType | gzip            | 否   | COS 文件是否压缩，默认为空，不压缩            |

[](id:url)
#### URL 参数说明
- REGION：COS 支持的地域，需要和实例在相同地域，可选值参见 [地域和访问域名](https://cloud.tencent.com/document/product/436/6224)。
- BUCKET：COS 存储桶名称。可参见 [存储桶列表](https://console.cloud.tencent.com/cos5/bucket)，**此处名称为不包含 APPID 的名称**，如您在存储桶列表中看到存储桶名称为“test-123123123”，此处填写“test”即可。
- PREFIX：COS 对象名称前缀。prefix 可以为空，可以包括多个斜杠。
 - 在只读表场景下，prefix 指定需要读取的对象名前缀。
prefix 为空时，读取 bucket 下所有文件；prefix 以斜杠(/) 结尾时，则匹配该文件夹下面的所有文件及子文件夹中的文件；否则，读取前缀匹配的所有文件夹及子文件夹中的文件。例如，COS 对象包括：read-bucket/simple/a.csv、read-bucket/simple/b.csv、read-bucket/simple/dir/c.csv、read-bucket/simple_prefix/d.csv。
   - prefix 指定 simple 则读取所有文件，包括目录名称前缀匹配的 simple_prefix，对象列表：
    read-bucket/simple/a.csv
    read-bucket/simple/b.csv
    read-bucket/simple/dir/c.csv
    read-bucket/simple_prefix/d.csv
   - prefix 指定 simple/ 则读取包括 simple/ 的所有文件，包括：
    read-bucket/simple/a.csv
    read-bucket/simple/b.csv
    read-bucket/simple/dir/c.csv
 - 在只写表场景下，prefix 指定输出文件前缀。
不指定 prefix 时，文件写入到 bucket 下；prefix 以斜杠（/）结尾时，文件写入到 prefix 指定的目录下，否则以给定的 prefix 作为文件前缀。例如，需要创建的文件包括：a.csv、b.csv、c.csv。
   - 指定 prefix 为 simple/ 则生成的对象为：
    read-bucket/simple/a.csv
    read-bucket/simple/b.csv
    read-bucket/simple/b.csv
   - 指定 prefix 为 simple\_，则生成的对象为：
    read-bucket/simple_a.csv
    read-bucket/simple_b.csv
    read-bucket/simple_b.csv

## 使用示例
### 导入 COS 数据
1. 定义 COS 扩展。  
```
CREATE EXTENSION IF NOT EXISTS cos_ext SCHEMA public; 
```
2. 定义只读 COS 外表和本地表。
本地表：
```
CREATE TABLE cos_local_tbl (c1 int, c2 text, c3 int)
DISTRIBUTED BY (c1);
```
COS 外表：指定读取广州 simple-bucket 下的所有文件。
```
CREATE READABLE EXTERNAL TABLE cos_tbl (c1 int, c2 text, c3 int)
LOCATION('cos://cos.ap-guangzhou.myqcloud.com/simple-bucket/from_cos/ secretKey=xxx secretId=xxx')
FORMAT 'csv';
```
3. 准备本地表数据。
将文件上传到 simple-bucket 下 from_cos 目录下，文件内容：
```
1,simple line 1,1
2,simple line 1,1
3,simple line 1,1
4,simple line 1,1
5,simple line 1,1
6,simple line 2,1
7,simple line 2,1
8,simple line 2,1
9,simple line 2,1
```
>!导入数据不包含表头字段行。
4. 导入 COS 数据。
```
INSERT INTO cos_local_tbl SELECT * FROM cos_tbl;
```
5. 查看结果，对比数据是否一致。
```
SELECT count(1) FROM cos_local_tbl;
SELECT count(1) FROM cos_tbl;
```

### 数据导出到 COS
1. 定义 COS 扩展。
```
CREATE EXTENSION IF NOT EXISTS cos_ext SCHEMA public;
```
2. 定义只写 COS 外表。
本地表：
```
CREATE TABLE cos_local_tbl (c1 int, c2 text, c3 int)
DISTRIBUTED BY (c1);
```
COS 外表：指定读取广州 simple-bucket 下的所有文件。
```
CREATE WRITABLE EXTERNAL TABLE cos_tbl_wr (c1 int, c2 text, c3 int)
LOCATION('cos://cos.ap-guangzhou.myqcloud.com/simple-bucket/to-cos/ secretKey=xxx secretId=xxx')
FORMAT 'csv';
```
3. 构造测试数据。
```
insert into cos_local_tbl values
(1, 'simple line 1' , 1),
(2, 'simple line 2', 2), 
(3, 'simple line 3', 3) ,
(4, 'simple line 4', 4) , 
(5, 'simple line 5', 5) ,
(6, 'simple line 6', 6) , 
(7, 'simple line 7', 7) , 
(8, 'simple line 8', 8) , 
(9, 'simple line 9', 9);
```
4. 导出数据到 COS。
```
INSERT INTO cos_tbl_wr SELECT * FROM cos_local_tbl;
```
5. 查看结果。
![](https://main.qcloudimg.com/raw/28d8cd469b6c485b3d2067997771bede.png)


### 简单分析 COS 数据
>!使用 COS 外表做查询分析时，未进行查询优化，复杂查询建议先将数据导入到本地。 
>
1. 定义 COS 扩展。
```
CREATE EXTENSION IF NOT EXISTS cos_ext SCHEMA public;
```
2. 准备数据。
将文件上传到 simple-bucket 的 for-dml 目录下，文件内容：
```
1,simple line 1,1
2,simple line 1,1
3,simple line 1,1
4,simple line 1,1
5,simple line 1,1
6,simple line 2,1
7,simple line 2,1
8,simple line 2,1
9,simple line 2,1
```
3. 定义只读 COS 外表。
```
CREATE READABLE EXTERNAL TABLE cos_tbl_dml (c1 int, c2 text, c3 int)
LOCATION('cos://cos.ap-guangzhou.myqcloud.com/simple-bucket/for-dml/ secretKey=xxx secretId=xxx')
FORMAT ‘csv’;
```
4. 分析 COS 外表数据。
```
SELECT c2, sum(c1) FROM cos_tbl GROUP BY c2;
```

## 使用经验
对于 COS 外表的使用盲点，以及一些技巧可以参见云+社区文章 [云数据仓库 PostgreSQL COS 使用经验](https://cloud.tencent.com/developer/article/1359016)。
