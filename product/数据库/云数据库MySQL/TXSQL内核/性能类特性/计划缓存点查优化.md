## 功能介绍
MySQL 数据的 SQL 执行步骤主要包括解析、准备、优化和执行四个阶段。执行计划缓存能力在 prepare statement 模式起作用，prepare statement 模式在 execute 时省略了解析和准备两个阶段，执行计划还会省略优化阶段，将性能进一步提升。

MySQL 8.0 20210830 版本只对（UK&PK）点查起作用，我们将会在后面的版本中开放更大的功能范围。

## 支持版本
内核版本 MySQL 8.0 20210830 及以上

## 适用场景
对云线上短小点查询较多，且使用 prepare statement 模式时，应用有性能上的提升。具体性能提升的幅度根据线上业务而定。

## 性能影响
- 对于点查（UK&PK）的 SQL，延迟性能提升20% - 30%，吞吐性能提升20% - 30%（sysbench 中的 point_select.lua 测试）。
- 对于内存开销，打开计划缓存开关的情况下，内存使用较不打开将有所提升。

## 使用说明
新增 cdb_plan_cache 开关控制是否打开计划缓存，新增 cdb_plan_cache_stats 开关控制观察缓存命中状态，以上参数为 tencentroot 级别。

| 参数名         | 状态 | 类型 | 默认  | 参数值范围 | 说明                              |
| -------------- | ---- | ---- | ----- | ---------- | --------------------------------- |
| cdb_plan_cache | yes  | bool | false | true/false | tencentroot 开关，是否打开计划缓存 |

新增 `show cdb_plan_cache` 命令查看计划缓存命中状态，字段意思如下：

| 字段名 | 说明                                                         |
| ------ | ------------------------------------------------------------ |
| sql    | SQL 语句，这里是带有?的 SQL 语句，代表此条 SQL 的执行计划已经被缓存 |
| mode   | SQL 缓存的模式，现只支持 prepare 模式                           |
| hit    | 本 THD 中命中的次数                                            |

当 cdb_plan_cache_stats 开关打开时，相当于信息记录，将会对性能产生影响。

## 相关状态说明
在通过 show profile 查看 SQL 执行各阶段状态时，当执行 SQL 命中计划缓存，optimizing、statistics 和 preparing 状态将被省略。

