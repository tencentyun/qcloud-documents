## 介绍
MySQL 数据目的表负责装载清洗转换后的数据。

## 示例
创建 ETL 作业后，进入【开发调试】页面。在数据目的表处单击【添加】。
![](https://main.qcloudimg.com/raw/78286815cc3b3113b6bba5a164eac2ec.png)

根据示例正确填写 MySQL 目的表相应信息。
![](https://main.qcloudimg.com/raw/6deb026e64eae644a7f840c7a572a4bd.png)

如信息填写无误，ETL 作业会自动获取数据目的表中所有字段的名称和类型（前提为数据源表已正确录入）。
![](https://main.qcloudimg.com/raw/23de48ec5209af05292b0889213ed40f.png)

## 注意事项
#### 主键说明
- 对于 Append（Tuple）数据，MySQL 数据库的表不需要定义主键，也不建议定义主键（否则可能因为重复数据而造成写入失败）。
- 对于 Upsert 数据，MySQL 数据库的表**必须**定义主键。

