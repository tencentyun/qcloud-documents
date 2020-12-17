连接保护用于 proxy 与后端数据库连接断开时（如后端数据库发生了异常，但异常未影响 proxy），保持客户端和 proxy 之间的连接不断开。

proxy 正在执行 SQL 时，如果与数据库的连接断开，则 proxy 断开与该 SQL 相关的所有连接（除 proxy 与客户端之间的连接），并告知用户错误：
```c++
ER_PROXY_TRANSACTION_ERROR // 在事务中
ER_PROXY_CONN_BROKEN_ERROR // 非事务中
```

#### 处理方式
- 如果 proxy 与后端数据库连接断开时，用户 session 处于`普通事务`中，处理如下（图中错误码均为 ER_PROXY_TRANSACTION_ERROR）：
![](https://main.qcloudimg.com/raw/a758c8c5d73ab6a54c62bb86d971131b.png)

- 如果 proxy 与后端数据库连接断开时，用户正处于`XA 事务`中，处理如下（图中错误码均为 ER_PROXY_TRANSACTION_ERROR）：
![](https://main.qcloudimg.com/raw/e15b45ae460c0ddfc7a60fa3c21cf3c4.png)

#### 超时配置
>?用户在事务中 proxy 与后端数据库发生连接断开事件，如果用户在超时之前还没有回滚事务，则 proxy 断开与用户的连接。
>
超时参数在 proxy 配置文件中为：
```json
<server_close timeout="60"/>
```
