## 调试 Source 和 Sink 介绍

当需要检验作业是否可以正常运行、逻辑是否正确时，为了减少外部系统的部署开销，以及避免干扰因素，我们可以使用一些调试专用的 Connector。

## 版本说明

| Flink 版本 | 说明 |
| :-------- | :--- |
| 1.11      | 支持 |
| 1.13      | 支持 |

## Datagen Source

Datagen 是 Flink 自带的随机数据生成器，它可以作为数据源直接引用。详细的使用方式可参考 [Flink 官方文档](https://ci.apache.org/projects/flink/flink-docs-release-1.13/zh/docs/connectors/table/datagen/)。

下面是 Datagen 数据源的一个示例，它生成的数据含有两个字段：第一个字段 `id` 是一个随机数，第二个字段 `name` 是一个随机字符串。

### DDL 定义

```sql
CREATE TABLE datagen_source_table ( 
	id INT, 
	name STRING 
) WITH ( 
  'connector' = 'datagen',
  'rows-per-second'='1'  -- 每秒产生的数据条数
);
```

### WITH 参数

<table class="table table-bordered">
    <thead>
      <tr>
        <th class="text-left" style="width: 25%">参数</th>
        <th class="text-center" style="width: 8%">是否必选</th>
        <th class="text-center" style="width: 7%">默认参数</th>
        <th class="text-center" style="width: 10%">数据类型</th>
        <th class="text-center" style="width: 50%">描述</th>
      </tr>
    </thead>
    <tbody>
    <tr>
      <td><h5>connector</h5></td>
      <td>必须</td>
      <td style="word-wrap: break-word;">(none)</td>
      <td>String</td>
      <td>指定要使用的连接器，这里是 'datagen'。</td>
    </tr>
    <tr>
      <td><h5>rows-per-second</h5></td>
      <td>可选	</td>
      <td style="word-wrap: break-word;">10000</td>
      <td>Long</td>
      <td>每秒生成的行数，用以控制数据发出速率。</td>
    </tr>
    <tr>
      <td><h5>fields.#.kind</h5></td>
      <td>可选</td>
      <td style="word-wrap: break-word;">random</td>
      <td>String</td>
      <td>指定 '#' 字段的生成器。可以是 'sequence' 或 'random'。</td>
    </tr>
    <tr>
      <td><h5>fields.#.min</h5></td>
      <td>可选</td>
      <td style="word-wrap: break-word;">(Minimum value of type)</td>
      <td>(Type of field)</td>
      <td>随机生成器的最小值，适用于数字类型。</td>
    </tr>
    <tr>
      <td><h5>fields.#.max</h5></td>
      <td>可选</td>
      <td style="word-wrap: break-word;">(Maximum value of type)</td>
      <td>(Type of field)</td>
      <td>随机生成器的最大值，适用于数字类型。</td>
    </tr>
    <tr>
      <td><h5>fields.#.length</h5></td>
      <td>可选</td>
      <td style="word-wrap: break-word;">100</td>
      <td>Integer</td>
      <td>随机生成器生成字符的长度，适用于 char、varchar、string。</td>
    </tr>
    <tr>
      <td><h5>fields.#.start</h5></td>
      <td>可选	</td>
      <td style="word-wrap: break-word;">(none)</td>
      <td>(Type of field)</td>
      <td>序列生成器的起始值。</td>
    </tr>
    <tr>
      <td><h5>fields.#.end</h5></td>
      <td>可选	</td>
      <td style="word-wrap: break-word;">(none)</td>
      <td>(Type of field)</td>
      <td>序列生成器的结束值。</td>
    </tr>
    </tbody>
</table>



## Logger Sink
Logger Sink 是腾讯云 Oceanus 提供的一个自定义 Logger 示例，它可以将最终的结果数据写入 TaskManager 的日志文件中，后续可以通过 Flink UI 或者控制台的日志面板查看这些日志的输出。
1. 使用 Logger Sink 前，需要先 [下载 JAR 包](https://github.com/tencentyun/flink-hello-world/releases)，**如果您希望自定义输出逻辑，也可以自行修改并编译构建程序包**。
2. 将下载的 JAR 包上传到程序包，具体可参考 [依赖管理](https://cloud.tencent.com/document/product/849/48295)。
3. 在 SQL 作业中引用该程序包，具体可参考 [开发 SQL 作业](https://cloud.tencent.com/document/product/849/48287)。

### DDL 定义
```sql
CREATE TABLE logger_sink_table ( 
	id INT,  
	name STRING 
) WITH ( 
	'connector' = 'logger',
	'print-identifier' = 'DebugData'
);
```

### WITH 参数
<table class="table table-bordered">
    <thead>
      <tr>
        <th class="text-left" style="width: 25%">参数</th>
        <th class="text-center" style="width: 8%">是否必选</th>
        <th class="text-center" style="width: 7%">默认参数</th>
        <th class="text-center" style="width: 10%">数据类型</th>
        <th class="text-center" style="width: 50%">描述</th>
      </tr>
    </thead>
    <tbody>
    <tr>
      <td><h5>connector</h5></td>
      <td>必须</td>
      <td style="word-wrap: break-word;">(none)</td>
      <td>String</td>
      <td>指定要使用的连接器，这里是 'logger'。</td>
    </tr>
    <tr>
      <td><h5>print-identifier</h5></td>
      <td>可选</td>
      <td style="word-wrap: break-word;">(none)</td>
      <td>String</td>
      <td>日志打印的前缀信息。</td>
    </tr>
    </tbody>
</table>       

## Print Sink（不建议使用）
Flink 内置了输出到 STDOUT（标准输出）的 Print Sink，但是由于打印的格式不符合 Oceanus 日志采集器的规则，目前不能很好地展示在界面上。我们建议使用上述 Logger Sink 来代替 Print Sink。

### DDL 定义
```sql
CREATE TABLE `print_table` (
  `id` INT,
  `name` STRING
) WITH (
 'connector' = 'print'
);
```

### WITH 参数
<table class="table table-bordered">
    <thead>
      <tr>
        <th class="text-left" style="width: 25%">参数</th>
        <th class="text-center" style="width: 10%">是否必选</th>
        <th class="text-center" style="width: 10%">默认值</th>
        <th class="text-center" style="width: 10%">数据类型</th>
        <th class="text-center" style="width: 45%">描述</th>
      </tr>
    </thead>
    <tbody>
    <tr>
      <td><h5>connector</h5></td>
      <td>必选</td>
      <td style="word-wrap: break-word;">(none)</td>
      <td>String</td>
      <td>指定要使用的连接器，此处应为 'print'。</td>
    </tr>
    <tr>
      <td><h5>print-identifier</h5></td>
      <td>可选</td>
      <td style="word-wrap: break-word;">(none)</td>
      <td>String</td>
      <td>配置一个标识符作为输出数据的前缀。</td>
    </tr>
    <tr>
      <td><h5>standard-error</h5></td>
      <td>可选</td>
      <td style="word-wrap: break-word;">false</td>
      <td>Boolean</td>
      <td>如果 format 需要打印为标准错误而不是标准输出，则为 True。</td>
    </tr>
    </tbody>
</table>
