
## 简介
用户可以通过调用 getttl 命令，获取记录的生存时间（Time To Live，TTL），在为记录设置了生存时间之后，用户可以使用 getttl 命令查看键的剩余生存时间（精度为毫秒），即键还有多久才会因为过期而被移除。getttl 命令只针对单条记录生效，不支持针对多条记录的操作。

## 语法
```
getttl from [table]  where key1 = 1 and key2 = "abc";
```

## 参数

| 参数             | 是否必填 | 限制条件                     | 说明                            |
| ---------------- | -------- | ---------------------------- | ------------------------------- |
| table            | 是       | 无                           | 表名                            |
| where 条件中的 key | 是       | 对于 TDR 表，必须填入所有 key 值 | 声明 key 的值，多个 key 值用 and 连接 |

## 错误
请参考 [错误码列表](https://cloud.tencent.com/document/product/596/49767)。

## 返回信息

| 情况描述                                 | 返回信息                                                     |
| ---------------------------------------- | ------------------------------------------------------------ |
| keys 不存在或者已过期                     | Record does not exist or has expired\.                       |
| keys 存在并且没有设置过期时间（永久有效） | Record exists and no expiration time is set \(permanent\)\.  |
| 获取失败                                 | Failed to get time to live\. The error code is \[error code\] and the error message is \[Error message\]\. |
| 获取成功                                 | The time to live is \[TTL\] milliseconds\.                   |


## 示例
获取某条记录已经设置的生存时间：
```
tcaplus> getttl from mails where key1 = 1 and key2 = "abc";
The time to live is 2000 milliseconds.
```
