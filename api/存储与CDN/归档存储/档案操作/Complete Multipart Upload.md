## 功能描述

Complete Multipart Upload请求实现结束分段上传，形成文件。发起该请求时必须携带全文件的树形哈希值，服务端将比较用户上传的全文树形哈希和利用已上传分块得到的树形哈希，一致则请求成功，不一致则返回失败。

## 请求

#### 请求语法

```HTTP
POST /<UID>/vaults/<VaultName>/multipart-uploads/<uploadID> HTTP/1.1
Host: cas.<Region>.myqcloud.com
Date: date
Authorization: Auth
x-cas-sha256-tree-hash: SHA256 tree hash of the archive
x-cas-archive-size: ArchiveSize in bytes
```

#### 请求参数

无特殊请求参数。

#### 请求头部

#### 必选头部

| 名称                     | 描述                                       | 类型     | 必选   |
| ---------------------- | ---------------------------------------- | ------ | ---- |
| x-cas-archive-size     | 整个档案的总大小（以字节为单位）。此值应为上传的各段的所有大小之和。       | String | 是    |
| x-cas-sha256-tree-hash | 整个档案的 SHA256 树形哈希，服务端将比较用户上传的全文树形哈希和利用已上传分块得到的树形哈希，一致则请求成功，不一致则返回失败 | String | 是    |

#### 请求内容

无请求内容。

## 返回值

#### 返回头部

| 名称               | 描述              | 类型     |
| ---------------- | --------------- | ------ |
| Location         | 新创建档案的相对 URI 路径 | String |
| x-cas-archive-id | 档案的 ID          | String |

#### 返回内容

无返回内容。
