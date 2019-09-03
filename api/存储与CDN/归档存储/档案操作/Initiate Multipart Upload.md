## 功能描述

Initiate Multipart Upload 请求实现初始化分段上传，此请求将返回一个 Upload Id 用以后续分段上传，此 Upload Id 有效期24小时。

每次分段上传的段大小要求一致（除了最后一个段），且必须为1MB乘以2的幂次

## 请求

#### 请求语法

```HTTP
POST /<UID>/vaults/<VaultName>/multipart-uploads HTTP/1.1
Host: cas.<Region>.myqcloud.com
Date: Date
Authorization: Auth
x-cas-archive-description: ArchiveDescription
x-cas-part-size: PartSize
```

#### 请求参数

无特殊请求参数

#### 请求头部

#### 必选头部

| 名称              | 描述                     | 类型     | 必选   |
| --------------- | ---------------------- | ------ | ---- |
| x-cas-part-size | 分段上传的段大小，必须为1MB乘以2的幂次，例如，1048576（1MB）、2097152（2MB） | String | 是    |

#### 推荐使用头部

| 名称                        | 描述                    | 类型     | 必选   |
| ------------------------- | --------------------- | ------ | ---- |
| x-cas-archive-description | 正在分段上传的档案描述，限制为1024B | String | 否    |

#### 请求内容

无请求内容。

## 返回值

#### 返回头部

| 名称                        | 描述                                       | 类型     |
| ------------------------- | ---------------------------------------- | ------ |
| Location                  | 创建的分段上传 ID 的相对 URI 路径，格式为`/<UID>/vaults/<VaultName>/multipart-uploads/<UploadId>` | String |
| x-cas-multipart-upload-id | 分段上传的 ID                                 | String |

#### 返回内容

无返回内容。
