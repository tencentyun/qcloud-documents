## 测试工具
数据库基准性能测试为 sysbench 0.5。
工具修改说明：
对 sysbench 自带的 otlp 脚本做了修改，读写比例修改为 1：1，并通过执行测试命令参数 oltp_point_selects 和 oltp_index_updates 来控制读写比例，本文测试用例的均采用 4 个 select 点，1 个 update 点，读写比例保持 4：1。

## 测试环境

|类型|说明|
|:--:|:--:|
|实例物理机器|高 IO 版-单机器最高可支撑 488 GB 内存 6 T 硬盘数据库|
|实例规格|当前售卖主流配置规格（详见下文测试用例）|
|客户端配置| 4 核 8 GB 内存|
|客户端数量|1~6 个(配置的提升，客户端数量也需要相应提升)|
|网络环境|万兆网络机房，网络延时 < 0.05 ms|
|环境负载|安装 mysql 机器负载 > 70% (针对非独占实例)|

* 客户端规格说明：机器采用了较高配置的客户机器，保证单客户端可以压测出数据库实例的性能，如果客户端配置规格较小，建议采用多个客户并行压测实例来求取数据总和。
* 网络延时说明：测试环境保证客户端机器与数据库实例在同一可用区，测试结果不受网络环境影响。

## 测试方法
### 1. 测试库表结构

```
CREATE TABLE `sbtest1` ( 
`id` int(10) unsigned NOT NULL AUTO_INCREMENT, 
`k` int(10) unsigned NOT NULL DEFAULT '0', 
`c` char(120) NOT NULL DEFAULT '', 
`pad` char(60) NOT NULL DEFAULT '',
 PRIMARY KEY (`id`), KEY `k_1` (`k`) 
) ENGINE=InnoDB DEFAULT CHARSET=utf8；
```

### 2. 测试数据行格式

```
id: 1
k: 20106885
c: 08566691963-88624912351-16662227201-46648573979-64646226163-77505759394-75470094713-41097360717-15161106334-50535565977
pad: 63188288836-92351140030-06390587585-66802097351-4928296184
```


### 3. 数据准备

```
/root//sysbench/sysbench --mysql-host=xxxx --mysql-port=xxxx --mysql-user=xxx --mysql-password=xxx --mysql-db=test --mysql-table-engine=innodb --test=tests/db/oltp.lua --oltp_tables_count=20 --oltp-table-size=10000000  --rand-init=on prepare
```

数据准备参数说明：
- `--test=tests/db/oltp.lua`，表示调用 tests/db/oltp.lua 脚本进行 oltp 模式测试。
- `--oltp_tables_count=20`，表示用于测试的表数量为 20 张。
- `--oltp-table-size=10000000`，表示每个测试表填充数据行数为 1000 W 行。
- `--rand-init=on`，表示每个测试表都是用随机数据来填充的。
   

### 4. 性能压测命令
```
/root//sysbench/sysbench --mysql-host=xxxx --mysql-port=xxx --mysql-user=xxx --mysql-password=xxx --mysql-db=test --test=/root/sysbench_for_z3/sysbench/tests/db/oltp.lua --oltp_tables_count=xx --oltp-table-size=xxxx --num-threads=xxx --oltp-read-only=off --rand-type=special --max-time=600 --max-requests=0 --percentile=99 --oltp-point-selects=4 run
```

 性能压测参数说明：
- `--test=/root/sysbench_for_z3/sysbench/tests/db/oltp.lua`，表示调用 /root/sysbench_for_z3/sysbench/tests/db/oltp.lua 脚本进行 oltp 模式测试。。
- `--oltp_tables_count=20`，表示本次用于测试的表数量为 20 张。
- `--oltp-table-size=10000000`，表示本次测试使用的表行数均为 1000 W 行。
- `--num-threads=128`，表示本次测试的客户端连接并发数为 128。
- `--oltp-read-only=off` ，off 表示测试关闭只读测试模型，采用读写混合模型。
- `--rand-type=special`，表示随机模型为特定的。
- `--max-time=1800`，表示本次测试的执行时间。
- `--max-requests=0`，0 表示不限制总请求数，而是按 max-time 来测试。
- `--percentile=99`，表示设定采样比例，默认是 95%，即丢弃 1% 的长请求，在剩余的 99% 里取最大值。
- `--oltp-point-selects=4`，表示 oltp 脚本中 sql 测试命令，select 操作次数为 4，默认值为 1。

### 5. 场景模型

本文用例均使用场景脚本 our_oltp.lua，修改为 4 个 select 点查询，1 个 update （索引列），读写比为 4：1。
针对最大配置类型，对数据场景增加了参数调优模型，测试结果见下文 [测试结果](#document_test_result)。

## 测试参数
|内存|存储空间|表数量|表行数|数据集大小|并发数|执行时间(m)|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|4 GB|200 GB|8|4000 W|76 GB|128|30|
|8 GB|200 GB|15|4000 W|142 GB|128|30|
|16 GB|400 GB|25|4000 W|238 GB|128|30|
|32 GB|700 GB|25|4000 W|238 GB|128|30|
|64 GB|1 T|40|4000 W|378 GB|256|30|
|96 GB|1.5 T|40|4000 W|378 GB|128|30|
|128 GB|2 T|40|4000 W|378 GB|128|30|
|244 GB|3 T|60|4000 W|567 GB|128|30|
|488 GB|6 T|60|4000 W|567 GB|128|30|
|488 GB(调优)|6 T|60|1000 W|140 GB|128|30|

<span id="document_test_result"></span>
## 测试结果
|内存|存储空间|数据集|客户端数|单客户端并发数|QPS|TPS|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|4 GB|200 GB|76 GB|1|128|4082|816|
|8 GB|200 GB|142 GB|1|128|6551|1310|
|16 GB|400 GB|238 GB|1|128|11098|2219|
|32 GB|700 GB|238 GB|2|128|20484|3768|
|64 GB|1 T|378 GB|2|128|36395|7279|
|96 GB|1.5 T|378 GB|3|128|56464|11292|
|128 GB|2 T|378 GB|3|128|81752|16350|
|244 GB|3 T|567 GB|4|128|98528|19705|
|488 GB|6 T|567 GB|6|128|142246|28449|
|488 GB(调优)|6 T|140 GB|6|128|245509|46304|
