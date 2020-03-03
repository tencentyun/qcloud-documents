## 功能描述

Delete Archive 请求实现删除一个 Archive。请求成功以后会返回 x-cas-archive-id 用来表示唯一的 Archive 文件。请求成功返回204 No Content。

在删除 Archive 后，您仍可能成功请求启动对已删除 Archive 的检索任务，但 Archive 检索任务会失败。

在您删除 Archive 时，对相应 Archive ID 正在进行的 Archive 检索可能成功，也可能不成功，具体取决于下面的场景：

- 收到删除 Archive 请求时，Archive 检索任务正在下载 Archive 到缓存池，则 Archive 检索操作可能会失败。
- 收到删除 Archive 请求时，Archive 检索任务已经下载 Archive 到缓存池，则您将能够下载输出。

支持跨账户操作。当操作本账户时，UID 为"-"。

## 请求

#### 请求语法

```HTTP
DELETE /<UID>/vaults/<VaultName>/archives/<ArchiveID> HTTP 1.1
Host:cas.<Region>.myqcloud.com
Date:date
Authorization: Auth
```

#### 请求参数

无特殊请求参数。

#### 请求头部

无特殊请求头部，其他头部请参见公共请求头部。

#### 请求内容

无请求内容。

## 返回值

#### 返回头部

无特殊返回头部，其他头部请参见公共返回头部。

#### 返回内容

无返回内容。
