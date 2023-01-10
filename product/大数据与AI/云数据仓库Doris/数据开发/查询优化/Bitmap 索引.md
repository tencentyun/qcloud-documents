用户可以通过创建 bitmap index 加速查询。
本文档主要介绍如何创建 bitmap 索引，以及创建 bitmap 索引的一些注意事项和常见问题。

## 名词解释
bitmap 索引：用位图表示的索引，对索引列的每个键值建立一个位图。是一种快速数据结构，能够加快查询速。
索引原理示意：
![](https://qcloudimg.tencent-cloud.cn/raw/7ab7ff735623cb59299b077ecbe5585c.jpg)

## 原理介绍
主要针对大量相同值的列而创建（例如：类别，操作员，部门 ID，库房 ID 等），索引块的一个索引行中存储键值和起止 Rowid，以及这些键值的位置编码，位置编码中的每一位表示键值对应的数据行的有无。一个块可能指向的是几十甚至成百上千行数据的位置。
- 当根据键值查询时，可以根据起始 Rowid 和位图状态，快速定位数据。
- 当根据键值做 and，or 或 in(x,y,..)查询时，直接用索引的位图进行位运算，快速得出结果行数据。
- 当执行 select count(xx) 时，可以直接访问索引就快速得出统计数据。

## 语法
创建和删除本质上是一个 schema change 的作业，具体细节可以参照 [Schema Change](https://doris.apache.org/zh-CN/docs/dev/advanced/alter-table/schema-change)。

### 创建索引
在 table1 上为 siteid 创建 bitmap 索引：
```sql
CREATE INDEX [IF NOT EXISTS] index_name ON table1 (siteid) USING BITMAP COMMENT 'balabala';
```

### 查看索引
展示指定 table_name 的下索引：
```sql
SHOW INDEX FROM example_db.table_name;
```

### 删除索引
删除指定 table_name 的下索引：
```sql
DROP INDEX [IF EXISTS] index_name ON [db_name.]table_name;
```
![](https://qcloudimg.tencent-cloud.cn/raw/949ba8c1385fcf910073ff1ef4ea43b2.png)

## 注意事项
- 目前索引命令（[show | create | drop] index）仅支持 bitmap 类型的索引。
- bitmap 索引仅在单列上创建。
- bitmap 索引能够应用在 `Duplicate`、`Uniq`  数据模型的所有列和 `Aggregate`模型的key列上。
- bitmap 索引支持的数据类型如下:
  - `TINYINT`
  - `SMALLINT`
  - `INT`
  - `BIGINT`
  - `CHAR`
  - `VARCHAR`
  - `DATE`
  - `DATETIME`
  - `LARGEINT`
  - `DECIMAL`
  - `BOOL`
- bitmap 索引仅在 Segment V2 下生效。当创建 index 时，表的存储格式将默认转换为 V2 格式（查看表的存储格式可通过 show create table table_name 命令）。

## bitmap 索引适用场景
- 适用于低基数的列上，建议在100到100,000之间，如：职业、地市等。重复度过高则对比其他类型索引没有明显优势；重复度过低，则空间效率和性能会大大降低。
- 特定类型的查询例如 count、or、and 等逻辑操作因为只需要进行位运算。如：通过多个条件组合查询，`select count(*) from table where job = '医生' and phonetype = 'iphone' and gender ='男';`类似这种场景，如果在每个查询条件列上都建立了 bitmap 索引，则数据库可以进行高效的位运算，精确定位到需要的数据，减少磁盘 IO。并且筛选出的结果集越小，bitmap 索引的优势越明显。
- 适用于即席查询、多维分析等 OLAP 场景。如果有一张表有100列，用户会使用其中的20个列作为查询条件（任意使用这20个列上的N的列），几乎没有办法创建合适的 b-tree 索引。但是在这些列上创建20个 bitmap 索引，那么所有的查询都可以应用到索引。

## bitmap 索引不适用场景
- 值重复度低的列，如：身份证号、手机号码等。
- 重复度过高的列，如：性别，可以建立 bitmap 索引，但不建议单独作为查询条件使用，建议与其他条件共同过滤。
- 经常需要更新修改的列。
