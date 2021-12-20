## 1 引言
### 1.1 背景
在“秒杀”和“限时抢购”等这样的场景下，大量用户在极短时间内请求大量商品。而体现在 MySQL 数据库中，同一商品在数据库里肯定是一行存储，所以会有大量的线程来竞争 InnoDB 行锁，当并发度越高时等待的线程也会越多，TPS 会下降 RT 会上升，数据库的吞吐量会严重受到影响。本文档描述 MariaDB 解决“秒杀”和“限时抢购”所做的特殊优化——热点更新技术。

### 1.2 使用简介
热点更新：采用如下示例语句对某个数据对象频繁进行更新。
目前仅支持 Percona 5.7.17 版本，可在 [MariaDB 购买页](https://console.cloud.tencent.com/mariadb/buy) 购买。
```
UPDATE COMMIT_ON_SUCCESS ROLLBACK_ON_FAIL QUEUE_ON_PK 88 TARGET_AFFECT_ROW 1 table_name  SET k=k+1 WHERE id=88
```

## 2 UPDATE 和 INSERT 语法变化
UPDATE 和 INSERT 的 SQL 语句可以增加新关键字，以表达热点更新的功能，红色为新增内容。

### 2.1 UPDATE 语法
```
UPDATE [LOW_PRIORITY]

       [COMMIT_ON_SUCCESS] [ROLLBACK_ON_FAIL] [QUEUE_ON_PK expr1] [TARGET_AFFECT_ROW expr2]

       [IGNORE] table_reference

SET col_name1={expr1|DEFAULT} [, col_name2={expr2|DEFAULT}] ...

[WHERE where_condition]

[ORDER BY ...]

[LIMIT row_count]
```

### 2.2 INSERT 语法
```
INSERT [LOW_PRIORITY | DELAYED | HIGH_PRIORITY]

       [COMMIT_ON_SUCCESS] [ROLLBACK_ON_FAIL] [QUEUE_ON_PK expr]

       [IGNORE]

[INTO] tbl_name

[PARTITION (partition_name,...)]

[(col_name,...)]

{VALUES | VALUE} ({expr | DEFAULT},...),(...),...

[ ON DUPLICATE KEY UPDATE

col_name=expr

[, col_name=expr] ... ]
```

### 2.3 说明
1. UPDATE 只支持单对象更新，即支持 &quot;single-table-syntax&quot;，不支持 &quot;multiple-table-syntax&quot;。
2. 只支持单机场景，XA 场景之后的迭代版本由 proxy 实现。
3. INSERT 的三种语法都支持，这里只列举一种。
4. 标准语法参考官方标准：[UPDATE Syntax](https://dev.mysql.com/doc/refman/5.7/en/update.html)、[INSERT Syntax](https://dev.mysql.com/doc/refman/5.7/en/insert.html)。
1. 对`QUEUE_ON_PK`指定的 expr 的值的对象，实施热点更新功能，通常 expr 的值是一个正整数值。
2. 参数含义：
   * `COMMIT_ON_SUCCESS`：更新操作成功后，立即提交。适合单语句作为一个事务。
   * `ROLLBACK_ON_FAIL`：更新操作失败后吗，立即回滚。适合单语句作为一个事务。
   * `QUEUE_ON_PK expr`：指定热点更新对象，对被更新的对象封锁和解锁。被更新的对象总数不超过`hot_commodity_query_size`，即，具有不同值的 expr 的个数不超过`hot_commodity_query_size`。expr 取值自由，但建议与主键保持一致，也可以不一致。
   * `TARGET_AFFECT_ROW expr`：指定热点更新影响的数据行。expr 是一个正整数（[1, MAX], MAX 是 8 位正数的最大值）。通常 expr 为 1，表示只有一行受到影响。

### 2.4 建议
使用时，只在单语句事务中增加全部新增的参数使用，并且建议蓝色字体值匹配（可以不匹配）。
```
UPDATE COMMIT_ON_SUCCESS ROLLBACK_ON_FAIL QUEUE_ON_PK 88 TARGET_AFFECT_ROW 1 table_name  SET k=k+1 WHERE id=88
```

### 2.5 示例
```
CREATE DATABASE hc_db;

CREATE TABLE hc_tbl(a INT PRIMARY KEY, b INT, c INT);

CREATE TABLE hc_tbl_2(a INT PRIMARY KEY, b INT, c INT);
```

#### 2.5.1 INSERT 示例
```

INSERT COMMIT_ON_SUCCESS ROLLBACK_ON_FAIL QUEUE_ON_PK 1 INTO hc_tbl VALUES(1, 1, 1);

INSERT COMMIT_ON_SUCCESS ROLLBACK_ON_FAIL QUEUE_ON_PK 1 INTO hc_tbl SET a= 2;

INSERT COMMIT_ON_SUCCESS ROLLBACK_ON_FAIL QUEUE_ON_PK 1 INTO hc_tbl_2 SELECT * FROM hc_tbl;
```

#### 2.5.2 UPDATE 示例
```
UPDATE COMMIT_ON_SUCCESS ROLLBACK_ON_FAIL QUEUE_ON_PK 1 TARGET_AFFECT_ROW 1 hc_tbl SET b= b+1 WHERE a = 1;

QUEUE_ON_PK expr 中 expr 不一定和 WHERE clause 中的值一致

UPDATE COMMIT_ON_SUCCESS ROLLBACK_ON_FAIL QUEUE_ON_PK 2 TARGET_AFFECT_ROW 1 hc_tbl SET b= b+1 WHERE a = 1;
```

## 3 新增参数说明
| 参数名 | 功能 | 类型 | 默认值 | 其他 |
| --- | --- | --- | --- | --- |
|` hot_commodity`<br/>`_enable `| 控制热点更新功能的开闭 | 布尔型 | true 打开热点更新功能 | 运行中关闭此参数，新的事务不再使用热点更新。最好是系统启动前就设置好，而不是运行时改变 |
|` hot_commodity`<br/>`_trace` | 控制跟踪功能的开闭 | 布尔型 | false 关闭跟踪功能 | 打开时，跟踪信息会输出到标准输出 |
| `hot_commodity`<br/>`_query_size` | 控制允许对多少个热点更新对象进行更新/插入操作 | 数值型 | 10000 | 起到限流的作用 |
|` hot_commodity`<br/>`_query_size_modify_enable` | 控制能否修改<br/>`hot_commodity_query_size `| 布尔型 | false 不允许修改<br/>`hot_commodity`<br/>`_query_size `| 方便在单元测试中改<br/>`hot_commodity_query_size `|

注意：如果 MyQL server 启动的时候，参数`hot_commodity_enable`是关闭的，则需要设置其为打开，重新启动 server，才能初始化全局的数据对象表。但如果`hot_commodity_query_size`值为 0，即使打开了`hot_commodity_enable`，也不能使用热点更新。所以热点更新功能需要同时设置：

- `hot_commodity_enable`=ON
- `hot_commodity_query_size`=10000  为一个大于 0 的数值，建议控制在 10000、20000 左右，需要根据硬件环境和应用压力等实际情况测试确定其适合的值。
- 启动 server。

