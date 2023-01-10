目前使用 Flink CDC Connector 做数据同步时，每个表都需要建立一个数据库连接，在多表、整库同步等场景下，对数据库实例的压力非常大，Oceanus 引入了多 Source 复用的优化来解决这种问题。
## 功能介绍
例如以下作业：
```sql
CREATE TABLE `source_1`
(
	`f_sequence`   INT,
    `f_random`     INT,
    `f_random_str` VARCHAR,
    PRIMARY KEY (`f_sequence`) NOT ENFORCED
) WITH (
      'connector' = 'mysql-cdc' ,
      'hostname' = 'ip1',
      'port' = '3306',
      'username' = 'xxx',
      'password' = 'xxx',
      'database-name' = 'db1',
      'table-name' = 'source_1'
);

CREATE TABLE `source_2`
(
	`f_sequence`   INT,
    `f_random`     INT,
    `f_random_1`     INT,
    `f_random_str` VARCHAR,
    `f_random_str_1` VARCHAR,
    PRIMARY KEY (`f_sequence`) NOT ENFORCED
) WITH (
      'connector' = 'mysql-cdc' ,
      'hostname' = 'ip1',
      'port' = '3306',
      'username' = 'xxx',
      'password' = 'xxx',
      'database-name' = 'db2',
      'table-name' = 'source_2'
);


CREATE TABLE `sink_1`
(
	`f_sequence`   INT,
    `f_random`     INT,
    `f_random_str` VARCHAR,
    PRIMARY KEY (`f_sequence`) NOT ENFORCED
) WITH (
      'connector' = 'logger'
);

CREATE TABLE `sink_2`
(
	`f_sequence`   INT,
    `f_random`     INT,
    `f_random_1`     INT,
    `f_random_str` VARCHAR,
    `f_random_str_1` VARCHAR,
    PRIMARY KEY (`f_sequence`) NOT ENFORCED
) WITH (
      'connector' = 'logger'
);

insert into sink_1 select * from source_1;
insert into sink_2 select * from source_2;
```
对于来自相同 db 实例的表同步，Flink 会生成两条 pipeline（如下图），每个 CDC 的 Source 都会跟 Mysql 建立一个数据库连接，在表的数量非常多的时候，作业与 Mysql 的连接会非常多，DB 端相应的压力也会非常大。
![](https://qcloudimg.tencent-cloud.cn/raw/1e4923e083f66afc48d0b3aa62dd6bfb.png)
我们可以看到在开启了 Source 复用功能之后，读相同 DB 实例的 Mysql CDC Source 会合并成一个 Source （如下图），可以有效的降低对 DB 的链接压力。并且在 Mysql 增量同步阶段，多个 Source 只需要读取一份 binlog 数据即可，避免了多个 Source 重复拉取 binlog 的问题。
![](https://qcloudimg.tencent-cloud.cn/raw/7ac17662c3c7df8428197823131ca09f.png)

## 如何开启 CDC Source 复用功能
在 sql 作业的开头，通过 set 命令指定开启 mysql cdc source 合并功能即可。
``` sql
SET table.optimizer.mysql-cdc-source.merge.enabled=true;
```
相关 set 参数说明

|                       参数                                      | 默认值 | 含义                                                         |
| ----------------------------------------------------------- | :----: | ------------------------------------------------------------ |
| table.optimizer.mysql-cdc-source.merge.enabled              | false  | 是否开启 mysql cdc source 复用功能，开启后会自动尝试 merge 同一作业内读相同 DB 的 mysql cdc source 为同一个 source。 |
| table.optimizer.mysql-cdc-source.merge.default-group.splits |   1    | 开启 mysql cdc source 合并功能后，相同 DB 实例 mysql cdc source 会合并成的 source 数量。对于表非常多的场景，当合并成一个 source 不能满足性能要求时，可以通过 set 命令调高这个值，oceanus 会自动将 cdc source 尽量均匀的划分成指定的 group splits 数量。 |

分组合并功能示例如下，假如 source_1 、source_2、source_3、source_4是来自同一个 DB 实例的 Mysql CDC Source 表（此处省略 source 和 sink 表定义），我们可以用如下的参数来配置 source 复用功能。
```sql
SET table.optimizer.mysql-cdc-source.merge.enabled=true;
SET table.optimizer.mysql-cdc-source.merge.default-group.splits=2;

insert into sink_1 select * from source_1;
insert into sink_2 select * from source_2;
insert into sink_3 select * from source_3;
insert into sink_4 select * from source_4;
```
最终的运行拓扑图如下，我们可以看到4个 cdc source 自动的划分成2个分组。
![](https://qcloudimg.tencent-cloud.cn/raw/bf804ad054d8f99e32e22ef202a748e1.png)

## 使用提醒
目前该功能不支持写入 kudu，开启该功能作业编译会报错。
