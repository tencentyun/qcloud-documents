## 加解密任务

- 任务类型：加密，解密。
- 字段类型：字符串类型，不支持二进制类型。

## Proxy

### 版本

代理支持的 Mongo 版本类型。

| Mongo 版本 | 分片实例 | 副本实例 |
|---------|------|------|
| 3.6 | 是    | 否    |
| 4.0 | 是    | 是    |
|4.2 | 是    | 是    |
|4.4 | 是    | 是    |
|5.0 | 否    | 否    |

### 认证

- 支持：SCRAM-SHA-1，SCRAM-SHA-256。
- 不支持：SSL。

### 对字段类型的支持

- string，字符串类型。
- binData，二进制数据类型。

### 命令

1. insert，insertOne，insertMany，bulkWrite。
2. find，findOne，findOneAndUpdate，findOneAndDelete，findOneAndReplace，findAndModify。
3. update，updateOne，updateMany，replaceOne。
4. remove，deleteMany，deleteOne。
5. aggregate [match, group]。

### JsonPath 类型支持

| JsonPath                     | Proxy支持   | 加密任务支持   | 说明                 |
|:-----------------------------|:----------|:----------|:--------------------|
| $.name                       | 支持        | 支持        | 字段                  |
| $.addr.name                  | 支持        | 支持        | 结构体内字段              |
| $.books[*]                   | 支持        | 支持        | 数组内所有元素             |
| $.books[-1:]                 | 不支持       | 不支持       | 数组内部分元素             |
| $.friends[?(@.name)].phone   | 不支持       | 不支持       | 具有 name 属性的，取 phone 的值  |
