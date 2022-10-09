## 特性描述
#### 优化前
原生 ClickHouse 实时 update 和 delete 性能较弱。针对 TDSQL-H LibraDB 同步的数据表，会自动映射成分布式表和本地表，业务层实际是通过分布式表来进行数据读写。本地表和分布式表中字段除原表字段外，额外为每个表新增字段 `_sign` 和 `_version`，使用 insert 代替 update 和 delete，查询获取一致性的数据需要使用 FINAL，查询性能差。 

- 查询时，需带上条件 `_sign=1`。
- 具体转换逻辑如下：
  - 新增字段含义
    - `_version` 是单调递增的版本数据。下文以初始值1为例。
    - `_sign=1` 代表有效数据，`_sign=-1` 为删除的数据。
  - INSERT
    - 插入新的一行数据。
    - 其他数据不变，`_sign=1`，`_version=1`。
  - DELETE
    - 插入新的一行数据。 
    - 其他数据不变，`_sign=-1`，`_version`=`_version+1`。
  - UPDATE
    - 对于修改的列中，不包含排序键的情况：
      - 插入新的一行数据。
      - 使用后镜像，`_sign=1`，`_version`=`_version+1`。
    - 对于修改的列中，包含了排序键的情况：
      - 插入两行数据。
      - 第一行，使用前镜像，`_sign=-1`，`_version`=`_version+1`。
      - 第二行，使用新镜像，`_sign=1`，`_version`=`_version+1`。

#### 优化后
TDSQL-H LibraDB 提供 MVCC 版本，对于 CDC 同步场景，将 update/delete 转换为 insert+delete 模式，无需 FINAL 即可保证目标端的数据与源端完全一致，且几乎没有查询性能的损失。同时在本地表原有字段基础上增加 `_dversion` 隐藏字段，用于删除操作标记。

基于 MVCC 版本，update/delete 转换与上述内置字段值变化关系如下：
- **update：**转换成 delete+insert 模式，delete 操作会对原数据打删除标记并更新 `_dversion` 的值，对于删除标记的主键记录会单独进行缓存，以便于异步聚合删除，insert 会新插入一条数据，并更新 `_version` 值， `_dversion` 取值为0。
- **delete：**转换成 delete 模式，对原数据打删除标记，更新 `_dversion` 值，并记录到缓存中，包括删除的主键和删除的时间戳，`_version` 值不变。

## 使用限制
仅 TDSQL-H LibraDB 的 MVCC 版本支持。

## 前提条件
- 已创建上线 MVCC 版本的 TDSQL-H LibraDB 实例。
- 已创建 CDC 任务，同步类型为表结构 + 全量数据 + 增量数据。

## 使用说明
下文以一个示例来演示数据一致性查询，源端 OLTP 库表为 migrate.t1。

在源端更新 id=8 的数据。
```sql
update t1 set birth=now() where id=8
```

在 CDC 任务目标端（即 TDSQL-H LibraDB）查看优化前和优化后的 MVCC 版本同步的数据。

### 优化前：非 MVCC 版本
```sql
#查询数据时，与原生 ClickHouse 的 VersionedCollapsingMergeTree 引擎相同, 数据出现三条
  
select * from t1 where id=8;
  
SELECT *
FROM t1
WHERE id = 8
  
Query id: d8b66e67-ba54-4b0e-850b-b2b54ceb1ec6
  
┌─id─┬─name─┬───────────────birth─┬─_sign─┬─_version─┐
│  8 │ tt   │ 2022-05-29 12:32:26 │     1 │      194 │
└────┴──────┴─────────────────────┴───────┴──────────┘
┌─id─┬─name─┬───────────────birth─┬─_sign─┬─_version─┐
│  8 │ tt   │ 2022-05-29 12:28:20 │     1 │       66 │
└────┴──────┴─────────────────────┴───────┴──────────┘
┌─id─┬─name─┬───────────────birth─┬─_sign─┬─_version─┐
│  8 │ tt   │ 2022-05-29 12:28:20 │    -1 │      194 │
└────┴──────┴─────────────────────┴───────┴──────────┘
  
3 rows in set. Elapsed: 0.004 sec.
  
#如果要获取正确的数据效果, 通过用 final 实现，达到数据最终一致目标
  
select * from t1 final where id=8;
  
SELECT *
FROM t1
FINAL
WHERE id = 8
  
Query id: 72e7fe14-0b1e-456f-bcbc-4bc91db4fd12
  
┌─id─┬─name─┬───────────────birth─┬─_sign─┬─_version─
│  8 │ tt  │ 2022-05-29 12:32:26 │     1 │     194   │
└────┴──────┴─────────────────────┴───────┴──────────┴
  
1 rows in set. Elapsed: 0.003 sec.
```
  
### 优化后：MVCC 版本
```sql
# 基于 MVCC 版本的内核, 直接显示最新数据，保证数据一致
  
select * from t1 where id=8;
  
SELECT *
FROM t1
WHERE id = 8
  
Query id: 9f6107b5-f45b-47d1-93ea-5f139a943bbe
  
┌─id─┬─name─┬───────────────birth─┬─_sign─┬─_version─┐
│  8 │ tt   │ 2022-05-29 12:32:26 │     1 │      370 │
└────┴──────┴─────────────────────┴───────┴──────────┘
  
1 rows in set. Elapsed: 0.007 sec.
```



