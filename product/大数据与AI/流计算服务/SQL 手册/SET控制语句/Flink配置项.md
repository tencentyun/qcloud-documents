## 简介
SET 语句用来设置作业的 [运行时参数](https://ci.apache.org/projects/flink/flink-docs-release-1.11/zh/ops/config.html)。可以用 SET 语句来实现作业行为的微调，例如设置作业的重启策略、调整 SQL 的 Mini-Batch 配置、关闭异步快照、设置快照最小间隔、调整 RocksDB StateBackend 的缓存大小等。

> !
> - SET 命令属于高级用法，请谨慎使用，避免参数配置不当而引起的运行时异常。
> - 不是所有 Flink 运行时参数都支持设置。具体支持情况可以自行验证或通过工单咨询。

### 语法
```sql
SET 配置项 = '参数值';
```
其中字符串类型的参数值必须用半角单引号括起来，布尔值和数值型的可以不加引号。同时，语句行尾需加上分号。

## 示例
### 配置 At Least Once 快照策略
默认情况下，流计算 Oceanus 使用 Exactly-Once 作为默认的快照策略，该策略可以确保作业崩溃恢复后，有最精确的状态一致性，但是少数情况下可能会造成较大延迟。

如果允许作业崩溃恢复时，一部分重复数据再次参与计算（造成短期的结果不精确），可以通过调整 Flink 的快照策略为 At Least Once，这样会取得更好的快照性能，尤其是对于状态超大且多个流之间的速度不一致时效果明显。
```sql
SET execution.checkpointing.mode='AT_LEAST_ONCE';
```

### 关闭 Operator Chaining 功能
默认情况下，Flink 会将运行图中相同并行度的算子尽可能的绑在一起，避免数据上下游传输的序列化、反序列化额外开销。

如果出于定位问题的角度，希望看到每个算子的数据流入流出情况，则可以关闭这个 Operator Chaining 功能。
>!关闭此功能后，作业的运行效率可能会大幅下降，请谨慎使用。
>
```sql
SET pipeline.operator-chaining=false;
```


### 启用 Table 的 Mini-Batch 支持
Flink SQL 对聚合提供了 Mini-Batch 支持，可以显著提升吞吐量。默认没有开启，因为会增加处理时延。如果希望使用 Mini-Batch，可以通过的下面的设置项启用此功能（批次大小和延迟参数可以自行设置，但不可省略）：
```sql
SET table.exec.mini-batch.enabled=true;
SET table.exec.mini-batch.size=5000;
SET table.exec.mini-batch.allow-latency='200 ms';
```

