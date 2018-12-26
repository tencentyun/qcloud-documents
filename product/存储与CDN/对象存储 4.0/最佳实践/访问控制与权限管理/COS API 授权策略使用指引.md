## COS API 授权策略使用指引
 COS 使用临时密钥服务时，不同的 COS API 操作需要不同的操作权限，而且可以同时指定一个操作或一序列操作操作权限.

## Service API 

### 获取存储桶列表 
若授予 获取存储桶列表 操作权限，则策略的 `action` 为 `name/cos:GetService` .
 对应的策略详细内容如下，其中 `resource` 为 `*`.：
```{
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

### 创建存储桶
若授予 创建存储桶 操作权限，则策略的 `action` 为 `name/cos:PutBucket` .
如在 APPID 为 1253653367 账号下创建一个`ap-beijing`地域的存储桶策略详细内容如下：
```
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
若授予 检索存储桶 操作权限，则策略的 `action` 为 `name/cos:HeadBucket` .
如查询 APPID 为 1253653367 账号下的`ap-beijing`地域的`example-1253653367` 存储桶策略详细内容如下：
```
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
若授予 查询存储桶地域信息 操作权限，则策略的 `action` 为 `name/cos:GetBucketLocation` .
如查询 APPID 为 1253653367 账号下的`ap-beijing`地域的`example-1253653367` 存储桶的地域信息策略详细内容如下：
```
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
若授予 获取存储桶的对象列表 操作权限，则策略的 `action` 为 `name/cos:GetBucket` .
如获取 APPID 为 1253653367 账号下的`ap-beijing`地域的`example-1253653367` 存储桶对象列表的策略详细内容如下：
```
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
若授予 删除存储桶 操作权限，则策略的 `action` 为 `name/cos:DeleteBucket` .
如删除 APPID 为 1253653367 账号下的`ap-beijing`地域的`example-1253653367` 存储桶的策略详细内容如下：
```
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
若授予 设置存储桶 ACL 操作权限，则策略的 `action` 为 `name/cos:PutBucketACL` .
如设置 APPID 为 1253653367 账号下的`ap-beijing`地域的`example-1253653367` 存储桶访问控制信息的策略详细内容如下：
```
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
若授予 获取存储桶 ACL 操作权限，则策略的 `action` 为 `name/cos:GetBucketACL` .
如获取 APPID 为 1253653367 账号下的`ap-beijing`地域的`example-1253653367` 存储桶访问控制信息的策略详细内容如下：
```
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
若授予 设置存储桶跨域配置 操作权限，则策略的 `action` 为 `name/cos:PutBucketCORS` .
如设置 APPID 为 1253653367 账号下的`ap-beijing`地域的`example-1253653367` 存储桶跨域配置信息的策略详细内容如下：
```
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
若授予 获取存储桶跨域配置 操作权限，则策略的 `action` 为 `name/cos:GetBucketCORS` .
如获取 APPID 为 1253653367 账号下的`ap-beijing`地域的`example-1253653367` 存储桶跨域配置信息的策略详细内容如下：
```{
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
若授予 删除存储桶跨域配置 操作权限，则策略的 `action` 为 `name/cos:DeleteBucketCORS` .
如删除 APPID 为 1253653367 账号下的`ap-beijing`地域的`example-1253653367` 存储桶跨域配置信息的策略详细内容如下：
```
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
若授予 设置存储桶生命周期 操作权限，则策略的 `action` 为 `name/cos:PutBucketLifecycle` .
如设置 APPID 为 1253653367 账号下的`ap-beijing`地域的`example-1253653367` 存储桶生命周期配置信息的策略详细内容如下：
```
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
若授予 获取存储桶生命周期 操作权限，则策略的 `action` 为 `name/cos:GetBucketLifecycle` .
如获取 APPID 为 1253653367 账号下的`ap-beijing`地域的`example-1253653367` 存储桶生命周期配置信息的策略详细内容如下：
```
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
若授予 删除存储桶生命周期 操作权限，则策略的 `action` 为 `name/cos:DeleteBucketLifecycle` .
如删除 APPID 为 1253653367 账号下的`ap-beijing`地域的`example-1253653367` 存储桶生命周期配置信息的策略详细内容如下：
```
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
若授予 获取存储桶中正在分片上传信息 操作权限，则策略的 `action` 为 `name/cos:ListMultipartUploads` .
如查询 APPID 为 1253653367 账号下的`ap-beijing`地域的`example-1253653367` 存储桶中正在分片上传信息的策略详细内容如下：
```
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

### 简单上传
若授予 简单上传 操作权限，则策略的 `action` 为 `name/cos:PutObject` .
如允许在 APPID 为 1253653367 账号下的`ap-beijing`地域的`example-1253653367` 存储桶中简单上传操作的策略详细内容如下：
```
 {
  "version": "2.0",
  "statement": [
    {
      "action": [
        "name/cos:PutObject"
      ],
      "effect": "allow",
      "resource": [
        "qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/*"
      ]
    }
  ]
}
```
### 分片上传
若授予 分片上传 操作权限，则策略的 `action` 为 `"name/cos:InitiateMultipartUpload","name/cos:ListParts","name/cos:UploadPart","name/cos:CompleteMultipartUpload","name/cos:AbortMultipartUpload"` 的集合.
如允许在 APPID 为 1253653367 账号下的`ap-beijing`地域的`example-1253653367` 存储桶中分片上传操作的策略详细内容如下：
```
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
        "qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/*"
      ]
    }
  ]
}
```

### Post 上传
若授予 Post上传 操作权限，则策略的 `action` 为 `name/cos:PostObject` .
如允许在 APPID 为 1253653367 账号下的`ap-beijing`地域的`example-1253653367` 存储桶中Post上传操作的策略详细内容如下：
```
{
  "version": "2.0",
  "statement": [
    {
      "action": [
        "name/cos:PostObject"
      ],
      "effect": "allow",
      "resource": [
        "qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/*"
      ]
    }
  ]
}
```
### 检索对象
若授予 检索对象 操作权限，则策略的 `action` 为 `name/cos:HeadObject` .
如允许检索 APPID 为 1253653367 账号下的`ap-beijing`地域的`example-1253653367` 存储桶中的对象操作的策略详细内容如下：
```
{
  "version": "2.0",
  "statement": [
    {
      "action": [
        "name/cos:HeadObject"
      ],
      "effect": "allow",
      "resource": [
        "qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/*"
      ]
    }
  ]
}
```
### 下载对象
若授予 下载对象 操作权限，则策略的 `action` 为 `name/cos:GetObject` .
如允许下载 APPID 为 1253653367 账号下的`ap-beijing`地域的`example-1253653367` 存储桶中的对象操作的策略详细内容如下：
```
{
  "version": "2.0",
  "statement": [
    {
      "action": [
        "name/cos:GetObject"
      ],
      "effect": "allow",
      "resource": [
        "qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/*"
      ]
    }
  ]
}
```
### 简单复制
若授予 简单复制 操作权限，则策略的目标对象的 `action` 为 `name/cos:PutObject` ， 和 源对象的`action` 为 `name/cos:GetObject` 
如将 APPID 为 1253653367 账号下的`ap-beijing`地域的`example-1253653367` 存储桶中的`audio.mp3`对象复制到 `copy_audio.mp3`对象中操作的策略详细内容如下：
```
{
  "version": "2.0",
  "statement": [
    {
      "action": [
        "name/cos:PutObject"
      ],
      "effect": "allow",
      "resource": [
        "qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/copy_audio.mp3"
      ]
    },
    {
      "action": [
        "name/cos:GetObject"
      ],
      "effect": "allow",
      "resource": [
        "qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/audio.mp3"    //这是源对象
      ]
    }
  ]
}
```
### 分片复制
若授予 分片复制 操作权限，则策略的目标对象的 `action` 为 `action` 为 `"name/cos:InitiateMultipartUpload","name/cos:ListParts","name/cos:PutObject","name/cos:CompleteMultipartUpload","name/cos:AbortMultipartUpload"` 集合， 和 源对象的`action` 为 `name/cos:GetObject` 
如将 APPID 为 1253653367 账号下的`ap-beijing`地域的`example-1253653367` 存储桶中的`audio.mp3`对象复制到 `copy_audio.mp3`对象中操作的策略详细内容如下：
```json
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
        "qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/copy_audio.mp3"
      ]
    },
    {
      "action": [
        "name/cos:GetObject"
      ],
      "effect": "allow",
      "resource": [
        "qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/audio.mp3"
      ]
    }
  ]
}
```
### 设置对象 ACL
若授予 设置对象 ACL 操作权限，则策略的 `action` 为 `name/cos:PutObjectACL` .
如允许设置 APPID 为 1253653367 账号下的`ap-beijing`地域的`example-1253653367` 存储桶中的对象ACL操作的策略详细内容如下：
```
{
  "version": "2.0",
  "statement": [
    {
      "action": [
        "name/cos:PutObjectACL"
      ],
      "effect": "allow",
      "resource": [
        "qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/*"
      ]
    }
  ]
}
```
### 获取对象 ACL
若授予 获取对象 ACL 操作权限，则策略的 `action` 为 `name/cos:GetObjectACL` .
如允许获取 APPID 为 1253653367 账号下的`ap-beijing`地域的`example-1253653367` 存储桶中的对象ACL操作的策略详细内容如下：
```

  "version": "2.0",
  "statement": [
    {
      "action": [
        "name/cos:GetObjectACL"
      ],
      "effect": "allow",
      "resource": [
        "qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/*"
      ]
    }
  ]
}
```
### Options 请求
若授予 Options 请求 操作权限，则策略的 `action` 为 `name/cos:OptionsObject` .
如允许在 APPID 为 1253653367 账号下的`ap-beijing`地域的`example-1253653367` 存储桶中的 options 请求操作的策略详细内容如下：
```json
{
  "version": "2.0",
  "statement": [
    {
      "action": [
        "name/cos:OptionsObject"
      ],
      "effect": "allow",
      "resource": [
        "qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/*"
      ]
    }
  ]
}
```
### 恢复归档
若授予 恢复归档 操作权限，则策略的 `action` 为 `name/cos:PostObjectRestore` .
如允许在 APPID 为 1253653367 账号下的`ap-beijing`地域的`example-1253653367` 存储桶中的 恢复归档 操作的策略详细内容如下：
```json
{
  "version": "2.0",
  "statement": [
    {
      "action": [
        "name/cos:PostObjectRestore"
      ],
      "effect": "allow",
      "resource": [
        "qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/*"
      ]
    }
  ]
}
```
### 删除对象
若授予 删除对象 操作权限，则策略的 `action` 为 `name/cos:DeleteObject` .
如允许删除 APPID 为 1253653367 账号下的`ap-beijing`地域的`example-1253653367` 存储桶中的 `audio.mp3`文件 操作的策略详细内容如下：
```
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
若授予 批量删除 操作权限，则策略的 `action` 为 `name/cos:DeleteObject` .
如允许删除 APPID 为 1253653367 账号下的`ap-beijing`地域的`example-1253653367` 存储桶中的 `audio.mp3`和 `video.mp4` 文件 操作的策略详细内容如下：
```
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
        "qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/video.mp4"
      ]
    }
  ]
}
```
