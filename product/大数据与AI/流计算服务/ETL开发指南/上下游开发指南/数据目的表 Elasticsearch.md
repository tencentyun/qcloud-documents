## 介绍
Elasticsearch 数据目的表支持将数据写入到 Elasticsearch 中。
>!Elasticsearch 数据目的表暂时只支持 Elasticsearch 6 或 Elasticsearch 7 版本。

## 示例
创建 ETL 作业后，进入**开发调试**页面。在数据目的表处单击**添加**。
![](https://main.qcloudimg.com/raw/ed72b4cfa8ed243f6e7c0c8387d8ee8b.png)
根据示例正确填写 Elasticsearch 目的表相应信息。

>!Elasticsearch 6 版本与 Elasticsearch 7 版本在配置上有一些不同，Elasticsearch 6 版本需要配置 document-type 而 Elasticsearch 7 版本不需要。

![](https://main.qcloudimg.com/raw/42619970125f288ead44c2d05134e75f.png)
动态 index 功能支持用户将数据写入到按时间切分的不同 index 中去，其中 date_field 指目标表中的某个确定的时间类型字段（DATE 或是 TIMESTAMP）yyyy-MM-dd 表示时间格式化后的格式，具体语法可以参考 [相关 JDK 文档](https://docs.oracle.com/javase/8/docs/api/java/time/format/DateTimeFormatter.html)。

下方的下拉框会查询出 Elasticsearch 现存 index 中符合格式的 index 列表，选择一个确定的 index 会读取对应的字段名与字段类型，方便字段映射规则的填写。
![](https://main.qcloudimg.com/raw/7a81000fd1d5a06d6a5d65b9d913e19e.png)
如信息填写无误，ETL 作业会自动获取数据目的表中所有字段的名称和类型（前提为数据源表已正确录入）。

由于 Elasticsearch 具有动态生成字段能力，因此对于 Elasticsearch 数据目的表，我们同样也提供了能够自由定义数字字段与类型的能力，如下图的 capture_time 字段，注意自定义的字段类型必须要与数据源表的类型一致，否则启动任务时将会报错。
![](https://main.qcloudimg.com/raw/193774754f8e9511909b621324c7a49e.png)

## 常见数据类型映射
关于 Elasticsearch 支持的数据类型定义及其使用，可参考 [Elasticsearch data-types](https://www.elastic.co/guide/en/elasticsearch/reference/7.x/mapping-types.html#_core_datatypes)，这里列举了常用的数据类型，及其与 Flink 类型的对应关系。

| Flink 数据类型     | ClickHouse 对应数据类型 |
| :----------------- | :---------------------- |
| text               | STRING                  |
| match_only_text    | STRING                  |
| binary             | STRING                  |
| keyword            | STRING                  |
| wildcard           | STRING                  |
| search_as_you_type | STRING                  |
| ip                 | STRING                  |
| short              | SMALLINT                |
| integer            | INT                     |
| long               | BIGINT                  |
| unsigned_long      | BIGINT                  |
| float              | FLOAT                   |
| half_float         | FLOAT                   |
| double             | DOUBLE                  |
| boolean            | BOOLEAN                 |
| date               | TIMESTAMP(3)            |
| date_nanos         | TIMESTAMP(6)            |

> !暂时不支持上述表格没有提到的类型。

## 注意事项
#### 主键说明
Elasticsearch 必须设置主键，设置为主键的字段会被写入到 \_id 字段中，相同 ID 的数据会进行覆盖。

## WITH 参数
Elasticsearch 数据目的表基于数据分析引擎 Elasticsearch 开发，两者具有相同的 WITH 参数，具体参数含义用法参见 [数据分析引擎 Elasticsearch](https://cloud.tencent.com/document/product/849/48313)。

