## 功能描述

Create Vault 请求实现创建一个 Vault，每个用户支持创建1000个 Vault。成功后返回201 Created。

支持跨账户创建。当创建本账户下 valut 时，UID值为"-"。
## 请求

#### 请求语法

```HTTP
PUT /<UID>/vaults/<VaultName> HTTP 1.1
Host:cas.<Region>.myqcloud.com
Date:date
Authorization: Auth
```

#### 请求参数

无特殊请求参数。

#### 请求头部

无特殊请求头部，其他头部请参见公共请求头部。

#### 请求内容

无请求内容

## 返回值

#### 返回头部

| 名称       | 描述              | 类型     |
| -------- | --------------- | ------ |
| Location | 创建成功以后，Vault的路径 | String |

#### 返回内容

无返回内容。
