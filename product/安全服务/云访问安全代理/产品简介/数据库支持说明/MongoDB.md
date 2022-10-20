## 加解密任务
- 任务类型：加密，解密。
- 段类型：字符串类型，不支持二进制类型。

## Proxy
### 版本
支持现网所有公有云版本，3.6，4.0，4.2，4.4。

### 部署方式
支持分片实例，不支持副本实例。

   
### 认证
- 支持：SCRAM-SHA-1, SCRAM-SHA-256。
- 不支持：SSL。

### 对字段类型的支持
-  string， 字符串类型。
-  binData，二进制数据类型。
 
### 命令
1. insert, insertOne, insertMany, bulkWrite。
2. find, findOne, findOneAndUpdate，findOneAndDelete, findOneAndReplace, findAndModify。
3. update，updateOne, updateMany, replaceOne。
4. remove, deleteMany, deleteOne。
5. aggregate [match, group]。
