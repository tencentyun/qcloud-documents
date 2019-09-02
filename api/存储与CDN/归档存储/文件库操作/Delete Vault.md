## 功能描述

Delete Vault 请求实现删除一个 Vault，删除前要求 Vault 下无 Archive 同时无 Archive 写入。删除 Vault 时同时删除其权限信息。请求成功后返回204 NoContent。

支持跨账户删除。当删除本账户下 Valut 时，UID值为"-"

## 请求

#### 请求语法

```HTTP
DELETE /<UID>/vaults/<VaultName> HTTP 1.1
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
