## 概述
对象存储 COS 使用临时密钥服务时，不同的 COS API 操作需要不同的操作权限，而且可以同时指定一个操作或一序列操作。

COS API 授权策略（policy）是一种 json 字符串。例如，授予 APPID 为1253653367，地域为`ap-beijing`，存储桶为`example-1253653367` ，路径前缀为`tes`的上传操作权限，路径前缀为`tes2`的下载操作权限的策略内容如下所示：

```shell
{
  "version": "2.0",
  "statement": [
    {
      "action": [
        "name/cos:PutObject",
        "name/cos:InitiateMultipartUpload",
        "name/cos:ListParts",
        "name/cos:UploadPart",
        "name/cos:CompleteMultipartUpload",
        "name/cos:AbortMultipartUpload"
      ],
      "effect": "allow",
      "resource": [
        "qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/test/*"
      ]
    },
    {
      "action": [
        "name/cos:GetObject"
      ],
      "effect": "allow",
      "resource": [
        "qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/test2/*"
      ]
    }
  ]
}
```

<a id="policy"></a>
#### 授权策略（policy）元素说明

| 名称     | 描述                                                         |
| -------- | ------------------------------------------------------------ |
| version  | 策略语法版本，默认为2.0                                      |
| effect   | 有 allow （允许）和 deny （显式拒绝）两种情况                |
| resource | 授权操作的具体数据，可以是任意资源、指定路径前缀的资源、指定绝对路径的资源或它们的组合 |
| action   | 此处是指 COS API，根据需求指定一个或者一序列操作的组合或所有操作(*)       |
|condition|约束条件，可以不填，具体说明请参考 [condition](https://cloud.tencent.com/document/product/598/10603#6..E7.94.9F.E6.95.88.E6.9D.A1.E4.BB.B6(condition)) 说明  |

以下根据 COS API 详细介绍授权策略。

## Service API 

### 获取存储桶列表

获取存储桶列表：Get Service，若授予其操作权限，则策略的`action` 为 `name/cos:GetService`，`resource`为`*` 。

#### 示例 

授予获取存储桶列表操作权限的策略详细内容如下：

```shell
{
  "version": "2.0",
  "statement": [
    {
      "action": [
        "name/cos:GetService"
      ],
      "effect": "allow",
      "resource": [
        "*"
      ]
    }
  ]
}
```

## Bucket API

Bucket API 策略的`resource`可以归纳为以下几种情况：

- 可操作任意地域的存储桶，策略的`resource`为`*`。
- 只可操作指定地域的存储桶，如只可操作 APPID 为1253653367 ，地域为`ap-beijing`的存储桶，则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/*`。
- 只可操作指定地域且指定名称的存储桶，如只可操作 APPID 为1253653367 ，地域为`ap-beijing`且名称为`example-1253653367`的存储桶， 则策略的`resource`为`qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/`。



Bucket API 策略的`action`则因操作不同而取值不同，以下列举所有 Bucket API 授权策略。

### 创建存储桶 

创建存储桶：Put Bucket，若授予其操作权限，则策略的`action`为`name/cos:PutBucket`。

#### 示例 

授予可在 APPID 为1253653367 ，地域为`ap-beijing`中创建任意名称的存储桶的操作权限， 其策略详细内容如下：

```shell
{
  "version": "2.0",
  "statement": [
    {
      "action": [
        "name/cos:PutBucket"
      ],
      "effect": "allow",
      "resource": [
        "qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/*"
      ]
    }
  ]
}
```

### 检索存储桶  

检索存储桶：Head Bucket，若授予其操作权限，则策略的`action`为`name/cos:HeadBucket`。

#### 示例 

授予只能检索 APPID 为1253653367 ，地域为`ap-beijing` ，存储桶为`example-1253653367`的操作权限，其策略详细内容如下：

```shell
{
  "version": "2.0",
  "statement": [
    {
      "action": [
        "name/cos:HeadBucket"
      ],
      "effect": "allow",
      "resource": [
        "qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/"
      ]
    }
  ]
}
```

### 查询存储桶地域信息

查询存储桶地域信息：Get Bucket Location，若授予其操作权限，则策略的`action`为`name/cos:GetBucketLocation`。

#### 示例 

授予只能查询 APPID 为1253653367 ，地域为`ap-beijing`，存储桶为`example-1253653367`的存储桶地域信息的操作权限， 其策略详细内容如下：

```shell
{
  "version": "2.0",
  "statement": [
    {
      "action": [
        "name/cos:GetBucketLocation"
      ],
      "effect": "allow",
      "resource": [
        "qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/"
      ]
    }
  ]
}
```

### 获取存储桶的对象列表

获取存储桶的对象列表：Get Bucket，若授予其操作权限，则策略的`action`为`name/cos:GetBucket`。

#### 示例 

授予只能获取 APPID 为1253653367 ，地域为`ap-beijing`，存储桶为`example-1253653367`的对象列表的操作权限，其策略详细内容如下：

```shell
{
  "version": "2.0",
  "statement": [
    {
      "action": [
        "name/cos:GetBucket"
      ],
      "effect": "allow",
      "resource": [
        "qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/*"
      ]
    }
  ]
}
```

### 删除存储桶

删除存储桶：Delete Bucket，若授予其操作权限，则策略的`action`为`name/cos:DeleteBucket`。

#### 示例 

授予只能删除 APPID 为1253653367 ，地域为`ap-beijing` ，存储桶为`example-1253653367`的存储桶的操作权限，其策略详细内容如下：

```shell
{
  "version": "2.0",
  "statement": [
    {
      "action": [
        "name/cos:DeleteBucket"
      ],
      "effect": "allow",
      "resource": [
        "qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/"
      ]
    }
  ]
}
```

### 设置存储桶 ACL 

设置存储桶 ACL：Put Bucket ACL，若授予其操作权限，则策略的`action`为`name/cos:PutBucketACL`。

#### 示例 

授予只能设置 APPID 为1253653367 ，地域为`ap-beijing` ，存储桶为`example-1253653367`的 ACL 的操作权限，其策略详细内容如下：

```shell
{
  "version": "2.0",
  "statement": [
    {
      "action": [
        "name/cos:PutBucketACL"
      ],
      "effect": "allow",
      "resource": [
        "qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/"
      ]
    }
  ]
}
```

### 获取存储桶 ACL

获取存储桶 ACL：Get Bucket ACL，若授予其操作权限，则策略的`action`为`name/cos:GetBucketACL`。

#### 示例 

授予只能获取 APPID 为1253653367 ，地域为`ap-beijing` ，存储桶为`example-1253653367`的 ACL 的操作权限，其策略详细内容如下：

```shell
{
  "version": "2.0",
  "statement": [
    {
      "action": [
        "name/cos:GetBucketACL"
      ],
      "effect": "allow",
      "resource": [
        "qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/"
      ]
    }
  ]
}
```

### 设置存储桶跨域配置

设置存储桶跨域配置：Put Bucket CORS，若授予其操作权限，则策略的`action`为`name/cos:PutBucketCORS`。

#### 示例 

授予只能设置 APPID 为1253653367 ，地域为`ap-beijing` ，存储桶为`example-1253653367`的跨域配置的操作权限，其策略详细内容如下：

```shell
{
  "version": "2.0",
  "statement": [
    {
      "action": [
        "name/cos:PutBucketCORS"
      ],
      "effect": "allow",
      "resource": [
        "qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/"
      ]
    }
  ]
}
```

### 获取存储桶跨域配置

获取存储桶跨域配置：Get Bucket CORS，若授予其权限，则策略的`action`为`name/cos:GetBucketCORS`。

#### 示例 

授予只能获取 APPID 为1253653367 ，地域为`ap-beijing` ，存储桶为`example-1253653367`的跨域配置的操作权限，其策略详细内容如下：

```shell
{
  "version": "2.0",
  "statement": [
    {
      "action": [
        "name/cos:GetBucketCORS"
      ],
      "effect": "allow",
      "resource": [
        "qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/"
      ]
    }
  ]
}
```

### 删除存储桶跨域配置

删除存储桶跨域配置 Delete Bucket CORS，若授予其操作权限，则策略的 `action` 为`name/cos:DeleteBucketCORS`。

#### 示例 

授予只能删除 APPID 为1253653367 ，地域为`ap-beijing` ，存储桶为`example-1253653367`的跨域配置的操作权限，其策略详细内容如下：

```shell
{
  "version": "2.0",
  "statement": [
    {
      "action": [
        "name/cos:DeleteBucketCORS"
      ],
      "effect": "allow",
      "resource": [
        "qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/"
      ]
    }
  ]
}
```

### 设置存储桶生命周期

设置存储桶生命周期：Put Bucket Lifecycle，若授予其操作权限，则策略的`action`为 `name/cos:PutBucketLifecycle` 。

#### 示例 

授予只能设置 APPID 为1253653367 ，地域为`ap-beijing` ，存储桶为`example-1253653367`的生命周期配置的操作权限，其策略详细内容如下：

```shell
{
  "version": "2.0",
  "statement": [
    {
      "action": [
        "name/cos:PutBucketLifecycle"
      ],
      "effect": "allow",
      "resource": [
        "qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/"
      ]
    }
  ]
}
```

### 获取存储桶生命周期

获取存储桶生命周期：Get Bucket Lifecycle，若授予其操作权限，则策略的`action`为`name/cos:GetBucketLifecycle`。

#### 示例 

授予只能获取 APPID 为1253653367 ，地域为`ap-beijing` ，存储桶为`example-1253653367`的生命周期配置的操作权限，其策略详细内容如下：

```shell
{
  "version": "2.0",
  "statement": [
    {
      "action": [
        "name/cos:GetBucketLifecycle"
      ],
      "effect": "allow",
      "resource": [
        "qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/"
      ]
    }
  ]
}
```

### 删除存储桶生命周期

删除存储桶生命周期：Delete Bucket Lifecycle，若授予其操作权限，则策略的`action`为`name/cos:DeleteBucketLifecycle`。

#### 示例 

授予只能删除 APPID 为1253653367 ，地域为`ap-beijing`，存储桶为`example-1253653367`的生命周期配置的操作权限，其策略详细内容如下：

```shell
{
  "version": "2.0",
  "statement": [
    {
      "action": [
        "name/cos:DeleteBucketLifecycle"
      ],
      "effect": "allow",
      "resource": [
        "qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/"
      ]
    }
  ]
}
```

### 获取存储桶中正在分片上传信息

获取存储桶中正在分片上传信息：List Multipart Uploads，若授予其操作权限，则策略的`action`为 `name/cos:ListMultipartUploads`。

#### 示例 

授予只能获取 APPID 为1253653367 ，地域为`ap-beijing` ，存储桶为`example-1253653367`中的正在分片上传信息的操作权限，其策略详细内容如下：

```shell
{
  "version": "2.0",
  "statement": [
    {
      "action": [
        "name/cos:ListMultipartUploads"
      ],
      "effect": "allow",
      "resource": [
        "qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/"
      ]
    }
  ]
}
```



## Object API

Object API 策略的`resource`可以归纳为以下几种情况：<br>

- 可操作任意对象，策略的`resource`为`*`。
- 只可操作指定存储桶中的任意对象，如只可操作 APPID 为1253653367 ， 地域为`ap-beijing`，且名称为`example-1253653367`的存储桶中的任意对象，则策略的`resource`为`qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/*`。
- 只可操作指定存储桶 且 指定路径前缀下的任意对象，如只可操作 APPID 为1253653367 ， 地域为`ap-beijing`，存储桶为`example-1253653367`，路径前缀为`test`下的任意对象，则策略的`resource`为`qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/test/*`。
- 只可操作指定绝对路径的对象，如只可操作 APPID 为1253653367 ， 地域为`ap-beijing`，存储桶为`example-1253653367`，绝对路径为`test/audio.mp3`的对象，则策略的`resource`为`qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/test/audio.mp3`。



Object API 策略的`action`则因操作不同而取值不同，以下列举所有 Object API 授权策略。

### 简单上传

简单上传：Put Object，若授予其操作权限，则策略的`action`为`name/cos:PutObject`。

#### 示例 

授予只能在 APPID 为1253653367 ，地域为`ap-beijing`，存储桶为`example-1253653367`，路径前缀为`test`下进行简单上传的操作权限，其策略详细内容如下：

```shell
 {
  "version": "2.0",
  "statement": [
    {
      "action": [
        "name/cos:PutObject"
      ],
      "effect": "allow",
      "resource": [
        "qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/test/*"
      ]
    }
  ]
}
```

### 分片上传 

分片上传包含：Initiate Multipar tUpload，List Parts，Upload Part，Complete Multipart Upload，Abort Multipart Upload。若授予其操作权限，则策略的`action`为 `"name/cos:InitiateMultipartUpload","name/cos:ListParts","name/cos:UploadPart","name/cos:CompleteMultipartUpload","name/cos:AbortMultipartUpload"`的集合。

#### 示例 

授予只能在 APPID 为1253653367 ，地域为`ap-beijing` ，存储桶为`example-1253653367`，路径前缀为`test`下进行分片上传的操作权限，其策略详细内容如下：

```shell
{
  "version": "2.0",
  "statement": [
    {
      "action": [
        "name/cos:InitiateMultipartUpload",
        "name/cos:ListParts",
        "name/cos:UploadPart",
        "name/cos:CompleteMultipartUpload",
        "name/cos:AbortMultipartUpload"
      ],
      "effect": "allow",
      "resource": [
        "qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/test/*"
      ]
    }
  ]
}
```

### Post 上传

Post 上传：Post Object，若授予其操作权限，则策略的`action`为`name/cos:PostObject`。

#### 示例 

授予只能在 APPID 为1253653367 ，地域为`ap-beijing` ，存储桶为`example-1253653367`，路径前缀为`test`下进行Post上传的操作权限，其策略详细内容如下：

```shell
{
  "version": "2.0",
  "statement": [
    {
      "action": [
        "name/cos:PostObject"
      ],
      "effect": "allow",
      "resource": [
        "qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/test/*"
      ]
    }
  ]
}
```

### 检索对象

检索对象：Head Object，若授予其操作权限，则策略的`action`为`name/cos:HeadObject`。

#### 示例 

授予只能检索 APPID 为1253653367 ，地域为`ap-beijing` ，存储桶为`example-1253653367`，路径前缀为`test`中的对象的操作权限，其策略详细内容如下：

```shell
{
  "version": "2.0",
  "statement": [
    {
      "action": [
        "name/cos:HeadObject"
      ],
      "effect": "allow",
      "resource": [
        "qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/test/*"
      ]
    }
  ]
}
```

### 下载对象

下载对象：Get Object，若授予其操作权限，则策略的`action`为`name/cos:GetObject`。

#### 示例 

授予只能下载 APPID 为1253653367 ，地域为`ap-beijing`，存储桶为`example-1253653367`，路径前缀为`test`中的对象的操作权限，其策略详细内容如下：

```shell
{
  "version": "2.0",
  "statement": [
    {
      "action": [
        "name/cos:GetObject"
      ],
      "effect": "allow",
      "resource": [
        "qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/test/*"
      ]
    }
  ]
}
```

### 简单复制

简单复制：Put Object Copy，若授予其操作权限，则策略的目标对象的`action`为`name/cos:PutObject`， 和 源对象的`action`为`name/cos:GetObject`。

#### 示例 

授予在APPID 为1253653367 ，地域为`ap-beijing`，存储桶为`example-1253653367`的路径前缀为`test`和路径前缀为`test2`间进行分片复制的操作权限，其策略详细内容如下：

```shell
{
  "version": "2.0",
  "statement": [
    {
      "action": [
        "name/cos:PutObject"
      ],
      "effect": "allow",
      "resource": [
        "qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/test/*"
      ]
    },
    {
      "action": [
        "name/cos:GetObject"
      ],
      "effect": "allow",
      "resource": [
        "qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/test2/*"
      ]
    }
  ]
}
```

其中`"qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/test2/*"`为源对象。

### 分片复制

分片复制：Upload Part Copy，若授予其操作权限，则策略的目标对象的`action`为`action`为`"name/cos:InitiateMultipartUpload","name/cos:ListParts","name/cos:PutObject","name/cos:CompleteMultipartUpload","name/cos:AbortMultipartUpload"`集合， 和源对象的`action`为`name/cos:GetObject`。

#### 示例 

授予在 APPID 为1253653367 ，地域为`ap-beijing`，存储桶为`example-1253653367`的路径前缀为`test`和路径前缀为`test2`间进行分片复制的操作权限，其策略详细内容如下：

```shell
{
  "version": "2.0",
  "statement": [
    {
      "action": [
        "name/cos:InitiateMultipartUpload",
        "name/cos:ListParts",
        "name/cos:PutObject",
        "name/cos:CompleteMultipartUpload",
        "name/cos:AbortMultipartUpload"
      ],
      "effect": "allow",
      "resource": [
        "qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/test/*"
      ]
    },
    {
      "action": [
        "name/cos:GetObject"
      ],
      "effect": "allow",
      "resource": [
        "qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/test2/*" 
      ]
    }
  ]
}
```

其中`"qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/test2/*"`为源对象。

### 设置对象 ACL

设置对象 ACL：Put Object ACL，若授予其操作权限，则策略的 `action` 为 `name/cos:PutObjectACL` 。

#### 示例 

授予只能设置 APPID 为1253653367 ，地域为`ap-beijing` ，存储桶为`example-1253653367`，路径前缀为`test`中的对象 ACL 操作权限，其策略详细内容如下：

```shell
{
  "version": "2.0",
  "statement": [
    {
      "action": [
        "name/cos:PutObjectACL"
      ],
      "effect": "allow",
      "resource": [
        "qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/test/*"
      ]
    }
  ]
}
```

### 获取对象 ACL

获取对象 ACL：Get Object ACL，若授予其操作权限，则策略的`action`为 `name/cos:GetObjectACL`。

#### 示例 

授予只能获取 APPID 为1253653367 ，地域为`ap-beijing`，存储桶为`example-1253653367`，路径前缀为`test`中的对象 ACL 操作权限，其策略详细内容如下：

```shell
{
  "version": "2.0",
  "statement": [
    {
      "action": [
        "name/cos:GetObjectACL"
      ],
      "effect": "allow",
      "resource": [
        "qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/test/*"
      ]
    }
  ]
}
```

### Options 请求

Options 请求：Options Object，若授予其操作权限，则策略的 `action` 为 `name/cos:OptionsObject`。

#### 示例 

授予只能在 APPID 为1253653367 ，地域为`ap-beijing`，存储桶为`example-1253653367`，路径前缀为`test`下进行 Options 请求 的操作权限，其策略详细内容如下：

```shell
{
  "version": "2.0",
  "statement": [
    {
      "action": [
        "name/cos:OptionsObject"
      ],
      "effect": "allow",
      "resource": [
        "qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/test/*"
      ]
    }
  ]
}
```

### 恢复归档

恢复归档：Post Object Restore，若其作权限，则策略的`action`为`name/cos:PostObjectRestore`。

#### 示例 

授予只能在 APPID 为1253653367 ，地域为`ap-beijing`，存储桶为`example-1253653367`，路径前缀为`test`下进行恢复归档的操作权限，其策略详细内容如下：

```shell
{
  "version": "2.0",
  "statement": [
    {
      "action": [
        "name/cos:PostObjectRestore"
      ],
      "effect": "allow",
      "resource": [
        "qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/test/*"
      ]
    }
  ]
}
```

### 删除对象

删除对象：Delete Object，若授予其操作权限，则策略的`action`为`name/cos:DeleteObject`。

#### 示例 

授予只能删除 APPID 为1253653367 ，地域为`ap-beijing` ，存储桶为`example-1253653367`中的`audio.mp3`这个对象的操作权限，其策略详细内容如下：

```shell
{
  "version": "2.0",
  "statement": [
    {
      "action": [
        "name/cos:DeleteObject"
      ],
      "effect": "allow",
      "resource": [
        "qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/audio.mp3"
      ]
    }
  ]
}
```

### 批量删除对象

批量删除对象：Delete Multiple Objects，若授予其操作权限，则策略的`action`为`name/cos:DeleteObject`。

#### 示例 

授予只能批量删除 APPID 为1253653367 ，地域为`ap-beijing`，存储桶为`example-1253653367`中的`audio.mp3`和`video.mp4`两个对象的操作权限，其策略详细内容如下：

```shell
{
  "version": "2.0",
  "statement": [
    {
      "action": [
        "name/cos:DeleteObject"
      ],
      "effect": "allow",
      "resource": [
        "qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/audio.mp3",
        "qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/video.mp4"
      ]
    }
  ]
}
```

## 常见场景授权策略

### 授予所有资源完全读写权限
授予所有资源完全读写权限，其策略详细内容如下：
```shell
{
  "version": "2.0",
  "statement": [
    {
      "action": [
        "*"
      ],
      "effect": "allow",
      "resource": [
        "*"
      ]
    }
  ]
}
```

### 授予所有资源只读权限
授予所有资源只读权限，其策略详细内容如下：
```shell
{
  "version": "2.0",
  "statement": [
    {
      "action": [
        "name/cos:Head*",
        "name/cos:Get*",
        "name/cos:List*",
        "name/cos:OptionsObject"
      ],
      "effect": "allow",
      "resource": [
        "*"
      ]
    }
  ]
}
```

### 授予指定路径前缀的读写操作
授予用户只能访问存储桶 example-1253653367 中路径前缀为 userID123456 下的文件，且无法操作其它路径文件的操作权限，该策略详细内容如下：
```shell
{
  "version": "2.0",
  "statement": [
    {
      "action": [
        "*"
      ],
      "effect": "allow",
      "resource": [
        "qcs::cos:ap-shanghai:uid/1253653367:prefix//1253653367/example/userID123456/*"
      ]
    }
  ]
}
```

