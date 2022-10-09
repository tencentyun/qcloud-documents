## 说明
- 支持内核：Presto、SparkSQL。
- 适用表范围：原生 Iceberg 表、外部表。
- 用途：创建一个表同时带一些属性，支持使用 CREATE TABLE AS 语法。

## 外部表语法
### 语法
```
CREATE TABLE [ IF NOT EXISTS ] table_identifier
    ( col_name[:] col_type [ COMMENT col_comment ], ... )
USING data_source
    [ COMMENT table_comment ]
    [ PARTITIONED BY ( col_name1, transform(col_name2), ... ) ]
    [ LOCATION path ]
    [ TBLPROPERTIES ( property_name=property_value, ... ) ]
```

### 参数
`USING data_source`：建表时，数据的输入类型，目前有：CSV，ORC，PARQUET，ICEBERG 等。
`table_identifier`：指定表名，支持三段式，例如：catalog.database.table。
`COMMENT`：表的描述信息
`PARTITIONED BY`：基于指定的列创建分区。
`LOCATION path`：数据表存储路径。
`TBLPROPERTIES`：一组 k-v 值，用于指定表的参数。

### 示例
```
CREATE TABLE dempts(
    id bigint COMMENT 'id number',
    num int,
    eno float,
    dno double,
    cno decimal(9,3),
    flag  boolean,
    data string,
    ts_year timestamp,
    date_month date,
    bno binary,
    point struct<x: double, y: double>,
    points array<struct<x: double, y: double>>,
    pointmaps map<struct<x: int>, struct<a: int>> 
    )
USING iceberg
COMMENT 'table documentation' 
PARTITIONED BY (bucket(16,id), years(ts_year), months(date_month), identity(bno),  bucket(3,num),  truncate(10,data))
LOCATION '/warehouse/db_001/dempts'
TBLPROPERTIES ('write.format.default'='orc');
```

## 原生表 Iceberg 语法
>! 该语法仅支持创建原生表。

### 语法
```
CREATE TABLE [ IF NOT EXISTS ] table_identifier
    ( col_name[:] col_type [ COMMENT col_comment ], ... )
[ COMMENT table_comment ]
[ PARTITIONED BY ( col_name1, transform(col_name2), ... ) ]
```

### 参数
`table_identifier`：支持三段式，catalog.db.name
Schemas and Data Types
```
col_type
  : primitive_type
  | nested_type

primitive_type
  : boolean
  | int/integer
  | long/bigint
  | float
  | double
  | decimal(p,s)，p=最大位数，s=最大小数点位数, s<=p<=38
  | date
  | timestamp，timestamp with timezone，不支持time和without timezone
  | string，也可对应Iceberg uuid类型
  | binary，也可对应Iceberg fixed类型

nested_type
  : struct
  | list
  | map
```
Partition Transforms
```
transform
  : identity，支持任意类型, DLC不支持该转换
  | bucket[N]，hash mod N分桶，支持col_type: int,long, decimal, date, timestamp, string, binary
  | truncate[L]，L截取分桶，支持col_type: int,long,decimal,string
  | years，年份，支持col_type: date,timestamp
  | months，月份，支持col_type: date,timestamp
  | days/date，日期，支持col_type: date,timestamp
  | hours/date_hour，小时，支持col_type: timestamp
```


### 示例
```
CREATE TABLE dempts(
    id bigint COMMENT 'id number',
    num int,
    eno float,
    dno double,
    cno decimal(9,3),
    flag  boolean,
    data string,
    ts_year timestamp,
    date_month date,
    bno binary,
    point struct<x: double, y: double>,
    points array<struct<x: double, y: double>>,
    pointmaps map<struct<x: int>, struct<a: int>> 
    )
COMMENT 'table documentation' 
PARTITIONED BY (bucket(16,id), years(ts_year), months(date_month), identity(bno),  bucket(3,num),  truncate(10,data));
```

