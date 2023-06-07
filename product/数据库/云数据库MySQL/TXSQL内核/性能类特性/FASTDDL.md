
## 功能介绍
该功能优化二级索引创建过程的耗时。开启该功能会使用多线程并发对二级索引数据进行外部排序，同时优化 flush bulk loading 阶段对 flush list 的加锁操作，有效降低 CREATE INDEX 的耗时和对并发 DML 的影响。

## 支持版本
- 内核版本 MySQL 8.0 20210330 及以上
- 内核版本 MySQL 5.7 20210331 及以上

## 适用场景
数据库经常会执行 DDL 操作，也经常会遇到 DDL 相关的问题，例如：
- 为什么加索引会造成实例的抖动，影响正常的业务读写？
- 为什么不到1GB的表执行 DDL 有时需要十几分钟？
- 为什么使用了临时表的连接退出时会造成实例抖动？

针对以上常见问题，TXSQL 内核团队经过多场景深入分析以及测试，优化 flush bulk loading 阶段对 flush list 的加锁操作，有效降低 CREATE INDEX 的耗时和对并发 DML 的影响，降低了 DDL 操作带来的影响。

## 性能数据
sysbench 测试导入20亿行数据，数据量约453GB，开启 FAST DDL 功能。
```
mysql> set global innodb_fast_ddl=ON;
Query OK, 0 rows affected (0.00 sec)
```
开启前耗时4395秒，开启后耗时2455秒。

## 使用说明
通过参数 innodb_fast_ddl 开启或关闭该功能。

| 参数名                        | 动态 | 类型    | 默认 | 参数值范围 | 说明                         |
| ----------------------------- | ---- | ------- | ---- | ---------- | ---------------------------- |
| innodb_fast_ddl               | Yes  | bool    | OFF  | {ON,OFF}   | 开启或关闭 FAST DDL           |

>?用户目前无法直接修改以上参数的参数值，如需修改可 [提交工单](https://console.cloud.tencent.com/workorder/category) 进行修改。
>
