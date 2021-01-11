## 数据变大，Impala 启动失败
### 背景
当 Impala 中的元数据信息太多（例如几百个库、几万个表），Impala 在启动的时候，需要把这些元数据信息广播到所有节点上，默认这个动作的超时时间是10s。当元数据较大且较易触发时，可通过在 Impala 的启动配置文件`/data/Impala/conf/impalad.flgs`中设置`-statestore_subscriber_timeout_seconds=100`。

### 问题排查确定
通常出现这个问题，会在 Impala 的日志`/data/emr/impala/logs`中出现如下内容：
```
Connection with state-store lost
Trying to re-register with state-store
```

## 配置低导致，Impala 查询慢
虽然 Impala 不是内存数据库，但在处理大型表、大型数据时，还是应该为 Impala 分配更多的物理内存，一般建议是使用128G或者更多的内存，并分配80%给到 Impala 进程。

## SELECT 语句失败
可能原因如下：
1. 由于某个特定节点的性能，容量或网络问题而导致超时。查看 impala log，确定是什么节点，检查该节点机器网络是否有问题。
2. join 查询使用过多的内存，导致查询自动取消。检查 join 语句是否合理，或者加大机器内存。
3. 受节点上如何生成本机代码以处理查询中特定 WHERE 子句的影响。例如，可以生成特定节点的处理器不支持的机器指令。如果日志中的错误消息表明原因是非法指令，请考虑暂时关闭本机代码生成，然后再次尝试查询。
4. 格式错误的输入数据，例如具有超长行的文本数据文件，或者与 CREATE TABLE 语句的 FIELDS TERMINATED BY 子句中指定的字符不匹配的分隔符。检查是否有超长的数据。并检查建表语句，是否制定了正确的分隔符。

## 设置查询的使用内存限制
```
[localhost:27001] > set mem_limit=3000000000;
MEM_LIMIT set to 3000000000
[localhost:27001] > select 5;
Query: select 5
+---+ |5 | +---+ |5 | +---+
[localhost:27001] > set mem_limit=3g;
MEM_LIMIT set to 3g
[localhost:27001] > select 5;
Query: select 5
+---+ |5 | +---+ |5 | +---+
[localhost:27001] > set mem_limit=3gb;
MEM_LIMIT set to 3gb
[localhost:27001] > select 5;
+---+
|5 | +---+ |5 | +---+
[localhost:27001] > set mem_limit=3m;
MEM_LIMIT set to 3m
[localhost:27001] > select 5;
+---+
|5 |
+---+
|5 |
+---+
[localhost:27001] > set mem_limit=3mb; MEM_LIMIT set to 3mb [localhost:21000] > select 5;
+---+ |5 | +---+
```
