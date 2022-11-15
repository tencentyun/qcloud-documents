## 新增功能
- 添加开关，控制是否直接将update ... limit ...下推给DB执行，而无需先计算出被更新行的主键。
```
<mode>
    ...
     <compatible update_limit="0"/>
 </mode>
```
- 支持一致性读。网关配置新增 <xa> <basic enable_consistent_read="1" />配置，0：关闭，1：打开，动态生效。配置是OSS接口修改，用户不需要修改
- 网关上报网关id到zk，并在赤兔前台展示
- 网关通过过滤握手包连接属性（connection attributes）中以“TDSQL_”为前缀的属性，来识别应用sql的交易渠道，并打印日志便于用户事后分析。
```
MYSQL con;
mysql_init(&con);
mysql_option4(&con, 
                        MYSQL_OPT_CONNECT_ATTR_ADD,
                       "TDSQL_trade_channel"/*TDSQL_前缀属性名*/,
                       "000124120122"/*属性值*/);
```
- 支持新的数据分布方式：create table (...) tdsql_distributed by list/range(...) (......)：
```
create table t1(a int key, b int) local_table_options tdsql_distributed by range(a) (s1 values less than(100), s2 values less than(200));
create table t2(a int key, b int) local_table_options tdsql_distributed by list(a) (s1 values in(1,2), s2 values in (3,4));
例如：
 CREATE TABLE `t1` (
  `a` int(11) NOT NULL,
  `b` int(11) DEFAULT NULL,
  PRIMARY KEY (`a`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
/*!50100 PARTITION BY LIST (a)
(PARTITION p1 VALUES IN (1,2) ENGINE = InnoDB,
 PARTITION p2 VALUES IN (3,4) ENGINE = InnoDB) */ TDSQL_DISTRIBUTED BY LIST(b) (s1 values in ('100'),s2 values in ('200'));  
```
- 网关慢查询上报到监控库
- 提供针对新的数据分布方式的rebalance工具
- proxy通过对发送给db的sql中携带/*proxy:qid*/，将业务sql与proxy拆分过后的sql关联起来
- 新增log.slow_log.report参数，默认为1，开启慢查询日志的上报。
- 新增optimiz distinct_to_group_by标志，将distinct 转成group by。
- 新增查看各种类型表的语法：
```
查看分片表： /*proxy*/show tables with shardkey      
查看全局表：/*proxy*/show tables with noshardkey_allset  
查看单表：/*proxy*/show tables without shardkey   
``` 

## 功能优化
- 对没有指定分区键值的SQL，在接口日志中添加标志：noshardkey=1。
- 支持一致性读，并优化了一致性读的性能。
- 网关上报最近一分钟内的SQL平均时耗，中位数时耗，p95, p99等时耗指标（网关配置statistics.time_cost.stat_percentile="1"）。
- 变量enable_column_cutoff 默认值为0，listen的地址修改为0.0.0.0。

## BUG修复
- 修复后台元数据缓存，在合并后台set不一致的元数据时，没有及时释放内存导致的内存泄漏问题。触发条件：跨节点JOIN访问的表，在不同的SET上不一致（例如注释、列定义、字符集等）
- 修复执行INSERT ... SELECT ... 过程中，由于客户端突然异常退出，导致proxy core的bug
- 修复对二级分区DDL语句进行改写时，由于SQL中的注释或者‘;’等，造成SQL改写之后不符合预期的BUG
- 修复mysql_real_connect()由于未传入用户名时，触发CORE的BUG
- 修复客户端握手包传入不存在的库时，无任何报错的BUG（与mysql行为不一致）
- 修复LEFT/RIGHT JOIN下推结果不对的BUG
- 修复group/order by时，proxy进行排序的collation与db不一致的bug
- 修复处理跨节点查询时，下推ORDER  BY ... LIMIT时导致的CORE
- 修复网关启动的时候，没有监听到zookeeper的节点，会导致所有跟zookeeper的交互的操作都会失败，类似自增，grant之类的操作
- 修复客户端执行sql其间异常退出时，导致proxy异常重启的bug
- 修复select distinct 执行速度变慢的问题，引入版本为 1.16.00-M-V2.0R700D001B103308 
- 修复autocommit=0时，偶发的建表失败问题
- 修复group by别名添加collation，不能执行问题
- 修复sql过长，导致bison的爆栈问题
- 修复/dev/shm无权访问时，网关不断coredump的BUG：start.sh脚本在无权访问/dev/shm时，直接退出
- 修复同版本扩容时，目标set上不存在网关配置文件中指定的嵌入式数据库目录而导致的启动失败：不存在则尝试创建目录
- 修复gateway.mode.sub_partition.auto_create失效的BUG
- 修复网关处理order/group by时，添加collation(列)时，列明错乱的bug
- 修复网关上报sql耗时一直为0的BUG
- 修复添加sql前缀/*proxy_id: qid*/导致性能下降的BUG
- 修复join.basic.max)pushdown_index_values不生效的BUG
- 修复慢查询上报功能导致日志清理功能被阻塞的BUG。
- 新增log.slow_log.report参数，默认为1，开启慢查询日志的上报。修复dd进程的占用CPU和io的问题
- 修复noshard 上报proxy id到/rootdir/session，造成新建noshard失败的问题。引入版本，迭代15的版本
- 修复noshard的，查询某个字段大于16M的内存泄漏问题

