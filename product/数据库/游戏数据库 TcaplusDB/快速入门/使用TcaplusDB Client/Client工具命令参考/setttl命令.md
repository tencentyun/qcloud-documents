
## 简介
用户可以通过调用 setttl 命令，为记录设置一个生存时间（Time To Live，TTL），记录的生存时间（精度为毫秒）在设置之后就会随着时间的流逝而不断地减少，当一个记录的生存时间被消耗殆尽时，TcaplusDB 就会移除这个记录。setttl 命令只针对单条记录生效，不支持针对多条记录的操作。

## 语法
```
setttl [table] ttl=[TTL] where key1 = 1 and key2 = "abc";
```

## 参数

| 参数             | 是否必填 | 限制条件                                                   | 说明                            |
| ---------------- | -------- | ------------------------------------------------------------ |------------------------------- |
| table            | 是       | 无                                                       | 表名                            |
| TTL              | 是       | 最大不能超过 uint64\_t 最大值的一半，即 ttl 最大值为 ULONG\_MAX/2，超过该值接口会强制设置为该值    | 生存时间，以毫秒为单位          |
| where 条件中的 key | 是       | 对于 tdr 表，必须填入所有 key 值      | 声明 key 的值，多个 key 值用 and 连接 |

## 错误
请参考 [错误码列表](https://cloud.tencent.com/document/product/596/49767)。


## 返回信息

| 情况描述             | 返回信息                                                     |
| -------------------- | ------------------------------------------------------------ |
| 记录不存在或者已过期 | Record does not exist or has expired\.                       |
| 设置失败             | Failed to set time to live\. The error code is \[error code\] and the error message is \[Error message\]\. |
| 设置成功             | Set time to live successfully\.                              |


## 示例
设置2000毫秒的生存时间：
```
tcaplus> setttl mails ttl=2000 where key1 = 1 and key2 = "abc";
Set time to live successfully.
```
