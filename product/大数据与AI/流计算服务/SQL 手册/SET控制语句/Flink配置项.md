## 简介
SET 语句可以调整作业的关键运行参数。目前大多数参数都可以通过 [作业高级参数](https://cloud.tencent.com/document/product/849/53391) 功能来配置，只有极少数参数需要使用 SET 语句。
> !
> - SET 命令属于高级用法，请谨慎使用，避免参数配置不当而引起的运行时异常。
> - SET 命令不支持注释，请不要在其后增加 `--` 注释信息。
> - SET 语句行尾需加上分号。

## 语法
SET 语句中字符串类型的参数值必须用半角单引号括起来，布尔值和数值型的可以不加单引号。
```sql
SET 配置项 = '参数值';
```

## 示例
### 配置 SQL 作业状态保留时间
针对 GROUP BY 和 JOIN 等大状态的语句，Flink 提供了 [Idle State Retention Time 机制](https://cloud.tencent.com/developer/article/1452854)，用户可以通过设置状态的最短保留时间和最长保留时间，避免状态的无限制增长造成作业崩溃（OOM）。例如，下面的语句指定了状态的最短保留时间是5小时，最长保留时间是6小时，Flink 会在这两个时间点之间自行选择状态的清理时机。
> ! 
>- 状态的最短保留时间和最长保留时间之间的差值必须大于5分钟，否则 Flink 会报错并忽略该设置。
>- 时间单位的写法遵循 Flink 配置的规范，例如可以写10min、也可以写3h、3hour、7day、7d等。数值和单位之间的空格为可选项。

```sql
SET execution.min-idle-state-retention = '5 h';
SET execution.max-idle-state-retention = '6 h';
```

### 配置 SQL 作业快照超时时间
对于 SQL 作业，默认情况下，快照超时时间最短为10分钟，最长为2倍的快照周期。例如，对于快照周期为60秒的作业，其快照超时时间是10分钟；而对于快照周期为10分钟的作业，其快照超时时间是20分钟。

如果您需要自定义快照的超时时间，可以使用如下的 SET 语句。
```sql
SET CHECKPOINT_TIMEOUT = '300 s';
```
> ! Flink 配置项（高级参数）`execution.checkpointing.timeout` 对 SQL 作业可能不生效，请使用本文中的 SET 语句设置 SQL 作业的快照超时时间。

