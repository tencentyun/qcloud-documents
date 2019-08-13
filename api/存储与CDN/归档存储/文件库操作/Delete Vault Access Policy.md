## 功能描述

Delete Vault Access Policy 请求删除 Vault 的权限。

只支持所有者操作，对应 UID 值为"-"。成功后返回204 No Content。

## 请求

#### 请求语法

```HTTP
DELETE /<UID>/vaults/<VaultName>/access-policy HTTP 1.1
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
