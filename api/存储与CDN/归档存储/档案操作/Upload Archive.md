## 功能描述

Upload Archive 请求实现上传一个 Archive 到指定 Vault。请求成功以后会返回 x-cas-archive-id 用来表示唯一的 Archive 文件。请求成功返回201 Created。

上传文件时，可以指定 x-cas-archive-description 用来做文件内容备注。

支持跨账户操作。当操作本账户时，UID为"-"。

## 请求

#### 请求语法

```http
POST /<UID>/vaults/<VaultName>/archives HTTP/1.1
Host: cas.<Region>.myqcloud.com
Date: date
Authorization: Auth
Content-Length: length
x-cas-content-sha256: sha256
x-cas-sha256-tree-hash: sha256
x-cas-archive-description: description

[Archive]
```

#### 请求参数

无特殊请求参数。

#### 请求头部

#### 必选头部

| 名称                     | 描述                             | 类型     | 必选   |
| ---------------------- | ------------------------------ | ------ | ---- |
| x-cas-content-sha256   | 档案的 SHA256 校验和（线性哈希）            | String | 是    |
| Content-Length         | RFC 2616 中定义的 HTTP 请求内容长度（字节）。 | String | 是    |
| x-cas-sha256-tree-hash | 档案的树形哈希校验和。                    | String | 是    |

#### 推荐使用头部

| 名称                        | 描述                           | 类型     | 必选   |
| ------------------------- | ---------------------------- | ------ | ---- |
| x-cas-archive-description | Archive的描述，会在读取Archive的时候返回。 | String | 否    |

#### 请求内容

Archive。

## 返回值

#### 返回头部

| 名称                     | 描述                  | 类型     |
| ---------------------- | ------------------- | ------ |
| Location               | 创建成功以后，Archive 的路径 。 | String |
| x-cas-archive-id       | Archive的表示 ID。    | String |
| x-cas-content-sha256   | 档案的SHA256校验和（线性哈希） | String |
| x-cas-sha256-tree-hash | 档案的树形哈希校验和。       | String |

#### 返回内容

无返回内容。
