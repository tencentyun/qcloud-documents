## Hudi 表类型说明
Hudi 支持如下两种表类型：
- Copy On Write
写时复制，简称 cow。使用 Parquet 格式存储数据。Copy On Write 表的更新操作需要通过重写实现。
- Merge On Read
读时合并，简称 mor。使用列式文件格式（Parquet）和行式文件格式（Avro）混合的方式来存储数据。Merge On Read 使用列式格式存放Base数据，同时使用行式格式存放增量数据。最新写入的增量数据存放至行式文件中，根据可配置的策略执行 COMPACTION 操作合并增量数据至列式文件中。

两种表类型的差异点如下表所示。

| 权衡     | Copy On Write             | Merge On Read        |
| -------- | ------------------------- | -------------------- |
| 数据延迟 | 高                        | 低                   |
| 查询延迟 | 低                        | 高                   |
| 更新成本 | 高（重写整个 Parquet 文件） | 低（追加到增量日志） |
| 写放大   | 高                        | 低                   |
| 适用场景 | 写少读多                  | 写多读少，实时 upsert |

## Spark SQL 创建 Hudi 表
### 语法格式与参数说明
支持在 DLC Spark 引擎使用 SQL 直接创建 Hudi 表，详细请参考语法格式和示例。
- 语法格式
```SQL
CREATE TABLE [ IF NOT EXISTS ] table_identifier
    ( col_name[:] col_type [ COMMENT col_comment ], ... )
USING data_source
    [ COMMENT table_comment ]
    [ PARTITIONED BY ( col_name1, transform(col_name2), ... ) ]
    [ LOCATION path ]
    [ TBLPROPERTIES ( property_name=property_value, ... ) ]
	

CREATE TABLE [IF NOT EXISTS] [db_name.]table_name 
    [(col_name1 col_type1 [COMMENT col_comment1], ...)]
    USING hudi 
    [ COMMENT table_comment ]
    [ PARTITIONED BY ( col_name1, col_name2, ... ) ]
    [ LOCATION path ]
    [ TBLPROPERTIES ( property_name=property_value, ... ) ]
```

- TBLPROPERTIES 参数说明
<table>
<thead>
<tr>
<th>参数</th>
<th>默认值</th>
<th>描述</th>
</tr>
</thead>
<tbody><tr>
<td>primaryKey</td>
<td>uuid</td>
<td>指定主键列，多个主键时使用逗号<code>,</code>隔开。</td>
</tr>
<tr>
<td>type</td>
<td>cow</td>
<td>表类型，支持以下两种类型：<br>cow：表示 Copy-On-Write 类型表。<br>mor：表示Merge-On-Read 类型表。</td>
</tr>
<tr>
<td>preCombineField</td>
<td>-</td>
<td>该值用于在写之前对具有相同的key的行进行合并去重。<br>对应 Hudi 的 DataSourceWriteOptions.PRECOMBINE_FIELD_OPT_KEY 字段。</td>
</tr>
</tbody></table>

### 示例
- 创建非分区表
```SQL
create table hudi_mor_tbl (
    id int,
    name string,
    price double,
    ts bigint
) using hudi
comment 'hudi demo'
location 'cosn://<cos_bucket>/spark_hudi/hudi_mor_tbl'
tblproperties (
    'type' = 'mor',
    'primaryKey' = 'id',
    'preCombineField' = 'ts'
);
```
- 创建分区表
```SQL
create table hudi_cow_pt_tbl (
    id bigint,
    name string,
    ts bigint,
    dt string,
    hh string
) using hudi
comment 'hudi partition demo'
partitioned by (dt, hh)
location 'cosn://<cos_bucket>/spark_hudi/hudi_cow_pt_tbl'
tblproperties (
    'type' = 'cow',
    'primaryKey' = 'id',
    'preCombineField' = 'ts'
)
```
