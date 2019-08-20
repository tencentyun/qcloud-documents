## 功能描述

Upload Part请求实现上传档案的一段数据。支持乱序上传档案段，支持覆盖已上传的数据段。需在请求中标示该数据段在档案的字节范围。此外，支持并行上传数据段，最多可以上传10000段。

当 x-cas-sha256-tree-hash 或 x-cas-content-sha256 与请求体中的真实文件校验和不一致时，请求返回错误。

当 Content-Length 与请求体中的真实文件大小不一致时，请求返回错误。

当Content-Range为必须以初始化分块时对应的块大小严格一致。例如，指定4194304 字节（4MB）的段大小，则0到4194303字节（4MB-1） 以及4194304（4MB）到8388607（8MB-1）为有效的段范围。2097152（2MB） 到6291456（6MB-1）为非法段范围。

成功上传段后，将返回204 No Content。 

## 请求

#### 请求语法

```HTTP
PUT /<UID>/vaults/<VaultName>/multipart-uploads/<uploadID> HTTP/1.1
Host: cas.<Region>.myqcloud.com
Date: Date
Authorization: Auth
Content-Range: ContentRange
Content-Length: PayloadSize
Content-Type: application/octet-stream
x-cas-sha256-tree-hash: Checksum of the part
x-cas-content-sha256: Checksum of the entire payload
```

#### 请求参数

无特殊请求参数。

#### 请求头部

#### 必选头部

| 名称                     | 描述                                       | 类型     | 必选   |
| ---------------------- | ---------------------------------------- | ------ | ---- |
| Content-Range          | 标识将在此段中上传的档案文件的字节范围，范围不能大于您在启动分段上传时指定的段大小。例如，Content-Range:bytes 0-4194303/* | String | 是    |
| x-cas-content-sha256   | 上传的数据段的 SHA256 校验和（线性哈希）                 | String | 是    |
| x-cas-sha256-tree-hash | 上传的数据段的 SHA256 树形哈希                      | String | 是    |

#### 推荐使用头部

| 名称             | 描述            | 类型     | 必选   |
| -------------- | ------------- | ------ | ---- |
| Content-Length | 数据段的长度（以字节为单位） | String | 否    |

#### 请求内容

数据段。

## 返回值

#### 返回头部

| 名称                     | 描述               | 类型     |
| ---------------------- | ---------------- | ------ |
| x-cas-sha256-tree-hash | 数据段的 SHA256 树形哈希 | String |

#### 返回内容

无返回内容。
