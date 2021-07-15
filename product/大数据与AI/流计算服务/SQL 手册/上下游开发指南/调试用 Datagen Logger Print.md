## 调试 Source 和 Sink 介绍
当需要检验作业是否可以正常运行、逻辑是否正确时，为了减少外部系统的部署开销，以及避免干扰因素，我们可以使用一些调试专用的  Connector。

## Datagen Source
Datagen 是 Flink 自带的随机数据生成器，它可以作为数据源直接引用。详细的使用方式可参考 [Flink 官方文档](https://ci.apache.org/projects/flink/flink-docs-release-1.13/zh/docs/connectors/table/datagen/)。

下面是 Datagen 数据源的一个示例，它生成的数据含有三个字段：第一个字段 `f_sequence` 是一个递增的有界序列，第二个字段 `f_random` 是一个随机数，第三个字段 `f_random_str` 是一个随机字符串。

```sql
CREATE TABLE random_source ( 
			f_sequence INT, 
			f_random INT, 
			f_random_str VARCHAR 
  ) WITH ( 
			'connector' = 'datagen', 
			'rows-per-second'='1',  -- 每秒产生的数据条数
			'fields.f_sequence.kind'='sequence',   -- 有界序列（结束后自动停止输出）
			'fields.f_sequence.start'='1',         -- 序列的起始值
			'fields.f_sequence.end'='10000',       -- 序列的终止值
			'fields.f_random.kind'='random',       -- 无界的随机数
			'fields.f_random.min'='1',             -- 随机数的最小值
			'fields.f_random.max'='1000',          -- 随机数的最大值
			'fields.f_random_str.length'='10'      -- 随机字符串的长度
);
```

## Logger Sink
Logger Sink 是腾讯云 Oceanus 提供的一个自定义 Logger 示例，它可以将最终的结果数据写入 TaskManager 的日志文件中，后续可以通过 Flink UI 或者控制台的日志面板查看这些日志的输出。

使用 Logger Sink 前，需要先 [下载 JAR 包](https://github.com/tencentyun/flink-hello-world/releases)，**如果您希望自定义输出逻辑，也可以自行修改并编译构建程序包**。将下载的 JAR 包上传到程序包（具体操作可参考 [程序包管理](https://cloud.tencent.com/document/product/849/48295)），然后在 SQL 作业中引用该程序包（具体操作可参考 [开发 SQL 作业](https://cloud.tencent.com/document/product/849/48287)）。

下面是 Logger Sink 的一个示例：

```sql
CREATE TABLE CustomSink ( 
			f_sequence INT, 
			f_random INT, 
			f_random_str VARCHAR 
) WITH ( 
			'connector' = 'logger',
			'print-identifier' = 'DebugData'
);
```

## Print Sink（不建议使用）
Flink 内置了输出到 STDOUT（标准输出）的 Print Sink，但是由于打印的格式不符合 Oceanus 日志采集器的规则，目前不能很好地展示在界面上。我们建议使用上述 Logger Sink 来代替 Print Sink。
