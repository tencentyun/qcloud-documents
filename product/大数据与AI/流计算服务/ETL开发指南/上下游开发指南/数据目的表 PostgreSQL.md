## 介绍

PostgreSQL 数据目的表支持将数据写入到 PostgreSQL 数据库中。

## 示例

创建 ETL 作业后，进入**开发调试**页面。在数据目的表处单击**添加**。
![](https://main.qcloudimg.com/raw/78286815cc3b3113b6bba5a164eac2ec.png)

根据示例正确填写 PostgreSQL 目的表相应信息。
![](https://main.qcloudimg.com/raw/efe7122fc74e08496977eb52103b10fa.png)
如信息填写无误，ETL 作业会自动获取数据目的表中所有字段的名称和类型（前提为数据源表已正确录入）。
![](https://main.qcloudimg.com/raw/23de48ec5209af05292b0889213ed40f.png)

## 注意事项

#### 主键说明

- 由于 ETL 数据源表产生的数据都为 Upsert 数据，因此PostgreSQL 数据目的表**必须**定义主键。
- 数据目的表定义的主键**必须**为物理表中定义的主键，否则任务启动后会出错。

## WITH 参数

PostgreSQL 数据目的表基于 [JDBC](https://cloud.tencent.com/document/product/849/48312) 开发，可以使用其中用于目的表的相关配置项：

| 参数值                     | 必填 | 默认值 | 描述                                                         |
| :------------------------- | :--- | :----- | :----------------------------------------------------------- |
| sink.buffer-flush.max-rows | 否   | 100    | 批量输出时，缓存中最多缓存多少数据。如果设置为0，表示禁止输出缓存。 |
| sink.buffer-flush.interval | 否   | 1s     | 批量输出时，每批次最大的间隔（毫秒）。**如果 `'sink.buffer-flush.max-rows'` 设为 `'0'`，而这个选项不为零，则说明启用纯异步输出功能，即数据输出到算子、从算子最终写入数据库这两部分线程完全解耦。** |
| sink.max-retries           | 否   | 3      | 数据库写入失败时，最多重试的次数。                           |

