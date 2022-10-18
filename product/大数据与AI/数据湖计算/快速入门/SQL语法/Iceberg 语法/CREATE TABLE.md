## 语法
```
CREATE TABLE [ IF NOT EXISTS ] table_identifier
    ( col_name[:] col_type [ COMMENT col_comment ], ... )
USING iceberg
    [ COMMENT table_comment ]
    [ PARTITIONED BY ( col_name1, transform(col_name2), ... ) ]
    [ LOCATION path ]
    [ TBLPROPERTIES ( property_name=property_value, ... ) ]

```

## 参数说明
`table_identifier`：支持三段式，`catalog.db.name`。
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
  
transform
  : identity，支持任意类型, DLC不支持该转换
  | bucket[N]，hash mod N分桶，支持col_type: int,long, decimal, date, timestamp, string, binary
  | truncate[L]，L截取分桶，支持col_type: int,long,decimal,string
  | years，年份，支持col_type: date,timestamp
  | months，月份，支持col_type: date,timestamp
  | days/date，日期，支持col_type: date,timestamp
  | hours/date_hour，小时，支持col_type: timestamp
```


TBLPROPERTIES，常用配置：

| Property | Default | Description |
|---------|---------|---------|
| write.format.default	| parquet	| file format for the table; parquet, avro, or orc| 
| write.parquet.compression-codec	| gzip	| Parquet compression codec: zstd, brotli, lz4, gzip, snappy, uncompressed| 
| write.avro.compression-codec	| gzip	| Avro compression codec: gzip(deflate with 9 level), gzip, snappy, uncompressed| 
| write.metadata.compression-codec	| none| 	Metadata compression codec; none or gzip| 
| write.spark.fanout.enabled	| false| 	Enables Partitioned-Fanout-Writer writes in Spark| 

## 示例
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


