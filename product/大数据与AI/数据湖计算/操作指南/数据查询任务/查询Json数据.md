## 查询步骤
1. 创建数据表，指定 Json 解析格式。
```
CREATE EXTERNAL TABLE `order_demo`(
  `docid` string COMMENT 'from deserializer',
  `user` struct < id :int,
  username :string,
  name :string,
  shippingaddress :struct < address1 :string,
  address2 :string,
  city :string,
  state :string > > COMMENT 'from deserializer',
  `children` array < string >
) ROW FORMAT SERDE 'org.apache.hive.hcatalog.data.JsonSerDe' LOCATION 'cosn://dlc-bucket/order'
```
2. 执行查询语句查询 Json 数据。DLC 支持 Json 解析函数`json_parse()`，`json_extract_scalar()`，`json_extract()`等。详情请参见 [SQL 语法](https://cloud.tencent.com/document/product/1342/61734)。
```sql
SELECT `user`.`shippingaddress`.`address1` FROM `order_demo` limit 10;
```

## 系统约束
- 必须是完整的 JSON 格式，否则 DLC 无法正常解析。
- 同一行数据不能有换行符，不能对 Json 进行可视化格式优化。例如：
```json
{"name":"Michael"}
{"name":"Andy", "age":30}
{"name":"Justin", "age":19}
```
- DLC 会自动将 Json 的一层级识别为数据表的属性列，其余嵌套结构识别为对应的属性值。
