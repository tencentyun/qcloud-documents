## 介绍
Elasticsearch 数据目的表支持将数据写入到 Elasticsearch 中。
>!Elasticsearch 数据目的表暂时只支持 Elasticsearch 6 或 Elasticsearch 7 版本。

## 常见数据类型映射
关于 Elasticsearch 支持的数据类型定义及其使用，可参考 [Elasticsearch data-types](https://www.elastic.co/guide/en/elasticsearch/reference/7.x/mapping-types.html#_core_datatypes)，这里列举了常用的数据类型，及其与 Flink 类型的对应关系。

| Flink 数据类型     | Elasticsearch 对应数据类型 |
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

#### 版本差异
Elasticsearch 6 版本与 Elasticsearch 7 版本在配置上有一些不同，Elasticsearch 6 版本需要配置 document-type 而 Elasticsearch 7 版本不需要。

## WITH 参数
Elasticsearch 数据目的表基于数据分析引擎 Elasticsearch 开发，两者具有相同的 WITH 参数，具体参数含义用法参见 [数据分析引擎 Elasticsearch](https://cloud.tencent.com/document/product/849/48313)。

