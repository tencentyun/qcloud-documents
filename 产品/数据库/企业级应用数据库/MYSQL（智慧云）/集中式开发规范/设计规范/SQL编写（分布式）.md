## DML语句
- 【不建议】SELECT 语句必须指定具体字段名称，禁止写成select *，因为select * 会造成不必要的IO和网络开销，无法使用覆盖索引，表结构变更业务会受影响
- 【不建议】insert 语句指定具体字段名称，不要写成 insert into t1 values(…)，因为后期如果表字段做了变更，但应用层没有及时更新的话，系统会报错
- 【建议】事务涉及的表必须全部是 innodb 表。否则一旦失败不会全部回滚，且易造成主从库同步中断
- 【不建议】事务中，不要使用SELECT … FOR UPDATE 语法，它会扩大意向锁范围，较大程度影响数据库的并发事务效率
- 【建议】单个事务操作的行数不超过5000行
- 【建议】除静态表或小表（XXX行以内），DML 语句必须有 where 条件，且使用索引查找
- 【建议】生产环境禁止使用 hint，如 sql_no_cache，force index，ignore key，straightjoin 等。因为 hint 是用来强制 SQL 按照某个执行计划来执行，但随着数据量变化我们无法保证自己当初的预判是正确的
- 【建议】where 条件里等号左右字段类型必须一致 ，否则无法利用索引
- 【建议】WHERE 子句中禁止只使用全模糊的 LIKE 条件进行查找，必须有其他等值或范围查询条件，否则无法利用索引
- 【建议】事务里批量更新数据需要控制数量，进行必要的 sleep，做到少量多次
-	【建议】SELECT|UPDATE|DELETE|REPLACE 要有 WHERE 子句，且 WHERE 子句的条件必需使用索引查找
- 【不建议】 索 引 列 不 要 使 用 函 数 或 表 达 式 ， 否 则 无 法 利 用 索 引 
- 【建议】减少使用 or 语句，可将 or 语句优化为 union，然后在各个 where 条件上建立索引。如 where a=1 or b=2 优化为 where a=1… union …where b=2, key(a),key(b)
- 【建议】要返回 MySQL 自增序列的 ID 值，可以考虑使用函数 LAST_INSERT_ID()，此函数只能返回同一个 SESSION 最近一次对有 AUTO_INCREMENT 属性表 INSERT 的 ID 值
- 【建议】使用 covering index 提高性能（index key 包含所要查询的数据）
- 【建议】分页查询，当 limit 起点较高时，可先用过滤条件进行过滤，比如： 
 	select a,b,c from t1 limit 10000,20;
 ==> select a,b,c from t1 where id>10000 limit 20;
	具体条件需要根据 sql调整

##  多表连接
- 【不建议】不建议在业务的更新类 SQL 语句中使用 join，比如 update t1 join t2…
- 【建议】建议将子查询 SQL 拆开结合程序多次查询，或使用 join来代替子查询
- 【建议】线上环境，多表 join 不要超过 3个表
- 【建议】在多表 join 中，尽量选取结果集较小的表作为驱动表，来 join 其他表
- 【建议】Join 操作，确保第二个表（探针表的关联列存在 index）
- 【建议】Join 操作，尽量确保 group by 或 order by 子句中列只参考一个表中的列

##  事务
- 【建议】单个事务中 INSERT|UPDATE|DELETE|REPLACE 语句操作的行数控制在 5000行 以内
- 【建议】事务里包含 SQL 不超过 5 个（支付业务除外）。因为过长的事务会导致锁数据较久，MySQL 内部缓存、连接消耗过多等问题
- 【建议】事务里更新语句尽量基于主键或 unique key，如 update … where id=XX; 否则会产生间隙锁，内部扩大锁定范围，导致系统性能下降，产生死锁
- 【建议】尽量把一些典型外部调用移出事务，如调用 webservice，访问文件存储等，从而避免事务过长
- 【建议】对于 MySQL 主从延迟严格敏感的 select 语句，请开启事务强制访问主库
- 【建议】事务中，不要使用 SELECT … FOR UPDATE 语法，它会扩大意向锁范围，较大程度影响数据库的并发事务效率
 
## 分布式事务说明
由于事务操作的数据通常跨多个物理节点，在分布式数据库中，类似方案即称为分布式事务。TDSQL支持普通分布式事务协议和XA分布式事务协议。TDSQL默认支持分布式事务，且对客户端透明，使用户像使用单机事务一样方便。
TDSQL 分布式事务采用两阶段提交算法（2PC）保证事务的原子性（Atomicity）和一致性（Consistency），隔离级别配置为 Read committed, Repeatable read，或 Serializable。
分布式事务使用方法：
```
begin; 	# 开启事务
... 	# 跨set的增、删、改、查等非DDL操作
commit; # 提交事务
```
【建议】分布式事务的性能不如单机事务，性能会有一定的损耗。如需使用，需要进行实际测试结果来决定是否使用。
## 排序和分组
- 【建议】减少使用 order by，和业务沟通能不排序就不排序，或将排序放到程序端去做。order by、group by、distinct 这些语句较为耗费 CPU，数据库的 CPU 资源是极其宝贵的
- 【建议】order by、group by、distinct 这些 SQL 尽量利用索引直接检索出排序好的数据。如 where a=1 order by 可以利用 key(a,b)
- 【建议】包含了 order by、group by、distinct 这些查询的语句，where 条件过滤出来的结果集请保持在 1000 行以内，否则导致 IO/CPU 过高
