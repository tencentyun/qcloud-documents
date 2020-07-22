## INSERT INTO
INSERT INTO 语句必须和 SELECT 子查询联用。
#### 语法
```
INSERT INTO 数据目的
SELECT 子句
```
#### 示例
将 SELECT 查询的结果插入名为 KafkaSink1 的数据目的（Sink）。
```
INSERT INTO KafkaSink1
SELECT s1.time_, s1.client_ip, s1.uri, s1.protocol_version, s2.status_code, s2.date_
FROM KafkaSource1 AS s1, KafkaSource2 AS s2
WHERE s1.time_ = s2.time_ AND s1.client_ip = s2.client_ip;
```

## SELECT FROM
#### 语法
```
SELECT 以逗号分隔的需要选中的字段
FROM 数据源或视图
WHERE 过滤条件
其他子查询
```
#### 示例
```
SELECT s1.time_, s1.client_ip, s1.uri, s1.protocol_version, s2.status_code, s2.date_
FROM KafkaSource1 AS s1, KafkaSource2 AS s2
WHERE s1.time_ = s2.time_ AND s1.client_ip = s2.client_ip;
```
SELECT 不能单独使用，必须配合 CREATE VIEW … AS 或 INSERT INTO 使用，否则系统会提示没有合适的 Operator。

## WHERE
WHERE 用来过滤查询条件（谓词），多个并列的条件可以用 AND、OR 来连接。

在与外部数据库 TencentDB 的表 JOIN 时，条件的连接只支持 AND。如需使用 OR 的功能，请参见 UNION ALL。

## HAVING
HAVING 用于过滤 GROUP BY 之后的结果。**WHERE 在 GROUP BY 之前过滤，而 HAVING 在 GROUP BY 分组之后过滤。**
#### 示例
```
SELECT SUM(amount)
FROM Orders
WHERE price > 10
GROUP BY users
HAVING SUM(amount) > 50
```

## GROUP BY
在流计算 Oceanus 中，GROUP BY 用于对结果进行分组聚合。目前有含时间窗口（Window）类型的  GROUP BY 和不含窗口的 GROUP BY（即持续查询）。
- 含时间窗口（Window）类型的  GROUP BY 不会更新之前的结果，因而会产生 Append 类型的数据流，只允许写入不带主键的 MySQL、PostgreSQL 表，以及 CKafka。
- 不含窗口的 GROUP BY 会更新之前发出的记录，因而会产生 Upsert 类型的数据流，只允许写入含主键的云数据库 MySQL、PostgreSQL 数据目的表（Sink），且主键必须与 GROUP BY 语句里 Upsert 字段一致。

#### 含时间窗口的 GROUP BY
本示例定义了一个包含时间窗口的 GROUP BY 查询语句。关于时间窗口函数的使用方法，请参见 [时间窗口函数](/document/product/849/18077)。
```
SELECT user, SUM(amount)
FROM Orders
GROUP BY TUMBLE(rowtime, INTERVAL '1' DAY), user
```
- 在 Event Time 时间模式下，使用 WATERMARK FOR BOUNDED 定义时间戳字段，那么 TUMBLE 窗口函数的第一个参数必须为该字段。HOP 和 SESSION 同理。
- 在 Processing Time 时间模式下，TUMBLE 窗口函数的第一个参数必须为 PROCTIME（大写）。HOP 和 SESSION 同理。

#### 不含时间窗口的 GROUP BY（持续查询）
本示例定义了一个不包含时间窗口的 GROUP BY 查询语句，这种查询叫做持续查询，因为它会根据每条新到的数据来计算并决定是否更新之前发出的结果，因而会产生一个 Upsert 流。
```
SELECT a, SUM(b) as d
FROM Orders
GROUP BY a
```
> !这种方式可能会因为 key 的数量过大或数据过多而发生内存溢出。因而请谨慎设置对象超时时间，不要过长。

## JOIN

目前流计算 Oceanus 系统只支持等值连接 Equi-JOIN，即 JOIN 条件内包含至少一条令左右表某字段相等的过滤条件，且只支持 Inner JOIN。对于 Outer JOIN 的支持将在后续的版本添加。 

### 流和流的 Inner Equi-JOIN
目前流和流的连接也分为两种：含时间范围的和不含时间范围的。前者会生成 Append 类型的流，而后者会生成 Upsert 类型的流。

#### 含时间范围的流-流 JOIN
含时间范围的 JOIN 的 WHERE 条件中需要至少一个等值连接的 JOIN 条件和一个指定的时间范围。这个时间范围可以用 <、<=、>=、> 或 BETWEEN … AND 等来表示。

**时间范围的示例：**
```
ltime = rtime
ltime >= rtime AND ltime < rtime + INTERVAL '10' MINUTE
ltime BETWEEN rtime - INTERVAL '10' SECOND AND rtime + INTERVAL '5' SECOND
```
**示例：**
```
SELECT *
FROM Orders o, Shipments s
WHERE o.id = s.orderId AND
o.ordertime BETWEEN s.shiptime - INTERVAL '4' HOUR AND s.shiptime
```

#### 不含时间范围的流-流 JOIN
不含时间范围的流-流 JOIN 的特点是只要求有至少一个等值连接，而不要求指定时间范围。也就是说，它会将历史以来所有的活跃数据参与计算（可以通过指定超时时间来去除不活跃的元素）。
> !
> - 可能会导致非常大的内存占用，需要谨慎使用。通常需要设置合适的对象超时时间，以及时清除失活的对象。
> - 这种查询会产生一个 Upsert 流，只能使用含主键的 MySQL、PostgreSQL 数据目的（Sink）来接收数据。

**示例：**
```
SELECT *
FROM Orders INNER JOIN Product ON Orders.productId = Product.id
```

### 流与 TencentDB 表的 JOIN

流计算 Oceanus 也支持流与 TencentDB for MySQL 数据表的 JOIN，语法同上面介绍的完全一致，只是要求 TencentDB 表必须放在 JOIN 条件的右表。
>?目前要求 JOIN 查询条件需要包括表的所有定义的键，否则会因查询结果过多、内存占用过大等问题而导致任务失败。

**示例：**
```
SELECT d.client_agent AS time_, d.client_ip, d.numbers AS request_body_length
FROM StreamSource AS s, DimSource AS d
WHERE s.client_ip = d.client_ip AND d.`month` LIKE  '20180%' AND ABS(d.numbers) BETWEEN 0 AND 2000
```

### 与数组进行 JOIN
流计算 Oceanus 系统支持和一个已定义的数组对象（可通过 [值构造函数](https://cloud.tencent.com/document/product/849/18074#.E5.80.BC.E6.9E.84.E9.80.A0.E5.87.BD.E6.95.B0) 构造数组对象 ARRAY）做 JOIN 操作。

**示例：**假设 tags 是一个已定义的数组。
```
SELECT users, tag
FROM Orders CROSS JOIN UNNEST(tags) AS t (tag)
```

## UNION ALL
UNION ALL 用来合并两个查询的结果。在流和 TencentDB 表 JOIN 时由于不支持 OR 连接查询条件，可使用 UNION ALL 来实现同样的查询效果。

#### 示例
```
SELECT *
FROM (
    (SELECT user FROM Orders WHERE a % 2 = 0)
  UNION ALL
    (SELECT user FROM Orders WHERE b = 0)
)
```
目前流计算 Oceanus 只支持 UNION ALL 而暂不支持 UNION，即不会对相同的行进行去重操作。如果需要实现去重以达到 UNION 的效果，请配合 DISTINCT 使用。**DISTINCT 会让结果由 Append 流变为 Upsert 流，因而只能使用含主键的 MySQL、PostgreSQL 数据目的（Sink）来接收数据。**

## OVER Window 聚合
如果需要对数据流做基于滑动窗口的聚合（不使用 GROUP BY 的聚合），那么可以使用 OVER 来进行滑动窗口的聚合操作。在 OVER 中可以指定 PARTITION、ORDER、窗口范围等。

#### 示例
下面的示例定义了一个滑动窗口聚合查询，统计一个大小为3的滑动窗口的交易总额（amount）。其中对之前的行使用 PRECEDING，而目前还不支持 FOLLOWING。

另外 ORDER BY 后面只允许一个时间戳字段，本例使用 Processing Time 时间模式下系统自动添加的 PROCTIME 列。
```
SELECT SUM(amount) OVER (
  PARTITION BY user
  ORDER BY PROCTIME
  ROWS BETWEEN 2 PRECEDING AND CURRENT ROW)
FROM Orders
```

## ORDER BY
ORDER BY 用来对查询的结果做排序，默认是 ASC（升序排列），也可以显式指定 DESC（降序排列）。
> !要求第一个排序项必须是升序的时间列（Event Time 时间戳或 Processing Time 时间戳，即 PROCTIME），之后的排序项可以自由指定。

#### 示例
```
SELECT *
FROM Orders
ORDER BY `orderTime`, `username` DESC, `userId` ASC 
```

## DISTINCT
DISTINCT 用来对查询结果进行去重，它必须放在 SELECT 后面。

#### 示例
```
SELECT DISTINCT users FROM Orders
```
- DISTINCT 会产生一个 Upsert 流，因而只有 Upsert 类型的数据目的（Sink）才可以接收其结果。而且长时间查询可能会导致内存占用过大，请谨慎使用。
- 通过设置合适的对象过期时间，可以及时清除失活对象来节省内存。

## 暂未支持的语法结构
目前还未支持的 SQL 语法结构有：
GROUPING SETS/ROLLUP/CUBE/IN/UNION（可以使用 UNION ALL 和 DISTINCT 来实现）/LIMIT 等，在后续版本会逐步增加相应语法的支持，例如对 Top 的数据进行实时查询。

