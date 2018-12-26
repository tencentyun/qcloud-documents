## COS API 授权策略使用指引
 COS 使用临时密钥服务时，不同的 COS API 操作需要不同的操作权限，而且可以同时指定一个操作或一序列操作操作权限.<br>
COS API 授权策略 (policy) 是一个 json 字符串,其包含的元素有` version , statement , action , effect , resource `.其中 `version` 默认为 2.0 , `effect` 有 `allow` (允许)和 `deny` (显式拒绝)两种情况. `resource`  可以是任意资源 或 指定路径前缀的
资源 或 指定绝对路径的资源 或 它们的组合. `action` 根据需求指定一个或者一序列操作的组合.<br>
如授予 APPID 为 1253653367 ，地域为 `ap-beijing` ，存储桶为 `example-1253653367` ，路径前缀为 `tes` 的上传操作权限，路径前缀为 `tes2` 的下载操作权限：
```
{
  "version": "2.0",
  "statement": [
    {
      "action": [
        "name/cos:PutObject"
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

以下根据 COS API 详细介绍授权策略.

## Service API 

### 获取存储桶列表 (Get Service) 
若授予 获取存储桶列表 操作权限，则策略的 `action` 为 `name/cos:GetService` .<br>
其策略的`resource` 为 `*` .
#### 示例 
授予 获取存储桶列表 操作权限 的策略详细内容如下：
```
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

### 创建存储桶 (Put Bucket) 
若授予 创建存储桶 操作权限，则策略的 `action` 为 `name/cos:PutBucket` .<br>
若 可创建任意地域的存储桶，则策略的 `resource` 为 `*` .<br>
若 只能创建指定地域的存储桶，如只能在 appid 为 1253653367 中创建 `ap-beijing` 地域的存储桶，则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/*` .<br>
若 只能创建指定地域 且 指定名称的存储桶，如只能在 appid 为 1253653367 中创建 `ap-beijing` 地域 且 名称为 `example-1253653367` 的存储桶， 则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/` .
#### 示例 
授予 可在 APPID 为 1253653367 ，地域为 `ap-beijing` 中创建任意名称的存储桶的操作权限， 其策略详细内容如下：
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
### 检索存储桶 (Head Bucket) 
若授予 检索存储桶 操作权限，则策略的 `action` 为 `name/cos:HeadBucket` .<br>
若 可检索任意地域的存储桶，则策略的 `resource` 为 `*` .<br>
若 只能检索指定地域的存储桶，如只能检索 appid 为 1253653367 中 `ap-beijing` 地域的存储桶，则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/*` .<br>
若 只能检索指定地域 且 指定名称的存储桶，如只能检索 appid 为 1253653367 中 `ap-beijing` 地域 且 名称为 `example-1253653367` 的存储桶， 则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/` .
#### 示例 
授予 只能检索 APPID 为 1253653367 ，地域为 `ap-beijing` ，存储桶为 `example-1253653367` 的操作权限，其策略详细内容如下：
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
### 查询存储桶地域信息 (Get Bucket Location) 
若授予 查询存储桶地域信息 操作权限，则策略的 `action` 为 `name/cos:GetBucketLocation` .<br>
若 可查询任意地域的存储桶地域信息，则策略的 `resource` 为 `*` .<br>
若 只能查询指定地域的存储桶地域信息，如只能查询 appid 为 1253653367 中 `ap-beijing` 地域的存储桶地域信息，则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/*` .<br>
若 只能查询指定地域 且 指定名称的存储桶地域信息，如只能查询 appid 为 1253653367 中 `ap-beijing` 地域 且 名称为 `example-1253653367` 的存储桶地域信息， 则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/` .
#### 示例 
授予 只能查询 APPID 为 1253653367 ，地域为 `ap-beijing` ，存储桶为 `example-1253653367` 的存储桶地域信息的操作权限， 其策略详细内容如下：
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
### 获取存储桶的对象列表 (Get Bucket) 
若授予 获取存储桶的对象列表 操作权限，则策略的 `action` 为 `name/cos:GetBucket` .<br>
若 可获取任意地域的存储桶的对象列表，则策略的 `resource` 为 `*` .<br>
若 只能获取指定地域的存储桶的对象列表，如只能获取 appid 为 1253653367 中 `ap-beijing` 地域的存储桶的对象列表，则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/*` .<br>
若 只能获取指定地域 且 指定名称的存储桶的对象列表，如只能获取 appid 为 1253653367 中 `ap-beijing` 地域 且 名称为 `example-1253653367` 的对象列表， 则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/` .
#### 示例 
授予 只能获取 APPID 为 1253653367 ，地域为 `ap-beijing` ，存储桶为 `example-1253653367` 的对象列表 的操作权限，其策略详细内容如下：
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
### 删除存储桶 (Delete Bucket) 
若授予 删除存储桶 操作权限，则策略的 `action` 为 `name/cos:DeleteBucket` .<br>
若 可删除任意地域的存储桶，则策略的 `resource` 为 `*` .<br>
若 只能删除指定地域的存储桶，如只能删除 appid 为 1253653367 中 `ap-beijing` 地域的存储桶，则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/*` .<br>
若 只能删除指定地域 且 指定名称的存储桶，如只能删除 appid 为 1253653367 中 `ap-beijing` 地域 且 名称为 `example-1253653367` 的存储桶， 则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/` .
#### 示例 
授予 只能删除 APPID 为 1253653367 ，地域为 `ap-beijing` ，存储桶为 `example-1253653367` 的存储桶 的操作权限，其策略详细内容如下：
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
### 设置存储桶 ACL (Put Bucket ACL) 
若授予 设置存储桶 ACL 操作权限，则策略的 `action` 为 `name/cos:PutBucketACL` .<br>
若 可设置任意地域的存储桶的 ACL ，则策略的 `resource` 为 `*` .<br>
若 只能设置指定地域的存储桶的 ACL ，如只能设置 appid 为 1253653367 中 `ap-beijing` 地域的存储桶的 ACL ，则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/*` .<br>
若 只能设置指定地域 且 指定名称的存储桶的 ACL ，如只能设置 appid 为 1253653367 中 `ap-beijing` 地域 且 名称为 `example-1253653367` 的存储桶的 ACL ， 则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/` .
#### 示例 
授予 只能设置 APPID 为 1253653367 ，地域为 `ap-beijing` ，存储桶为 `example-1253653367` 的 ACL 的操作权限，其策略详细内容如下：
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
### 获取存储桶 ACL (Get Bucket ACL) 
若授予 获取存储桶 ACL 操作权限，则策略的 `action` 为 `name/cos:GetBucketACL` .<br>
若 可获取任意地域的存储桶的 ACL ，则策略的 `resource` 为 `*` .<br>
若 只能获取指定地域的存储桶的 ACL ，如只能获取 appid 为 1253653367 中 `ap-beijing` 地域的存储桶的 ACL ，则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/*` .<br>
若 只能获取指定地域 且 指定名称的存储桶的 ACL ，如只能获取 appid 为 1253653367 中 `ap-beijing` 地域 且 名称为 `example-1253653367` 的存储桶的 ACL ， 则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/` .
#### 示例 
授予 只能获取 APPID 为 1253653367 ，地域为 `ap-beijing` ，存储桶为 `example-1253653367` 的 ACL 的操作权限，其策略详细内容如下：
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
### 设置存储桶跨域配置 (Put Bucket CORS) 
若授予 设置存储桶跨域配置 操作权限，则策略的 `action` 为 `name/cos:PutBucketCORS` .<br>
若 可设置任意地域的存储桶的跨域配置，则策略的 `resource` 为 `*` .<br>
若 只能设置指定地域的存储桶的跨域配置，如只能设置 appid 为 1253653367 中 `ap-beijing` 地域的存储桶的跨域配置，则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/*` .<br>
若 只能设置指定地域 且 指定名称的存储桶的跨域配置，如只能设置 appid 为 1253653367 中 `ap-beijing` 地域 且 名称为 `example-1253653367` 的存储桶的跨域配置， 则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/` .
#### 示例 
授予 只能设置 APPID 为 1253653367 ，地域为 `ap-beijing` ，存储桶为 `example-1253653367` 的跨域配置的操作权限，其策略详细内容如下：
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
### 获取存储桶跨域配置 (Get Bucket CORS) 
若授予 获取存储桶跨域配置 操作权限，则策略的 `action` 为 `name/cos:GetBucketCORS` .<br>
若 可获取任意地域的存储桶的跨域配置，则策略的 `resource` 为 `*` .<br>
若 只能获取指定地域的存储桶的跨域配置，如只能获取 appid 为 1253653367 中 `ap-beijing` 地域的存储桶的跨域配置，则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/*` .<br>
若 只能获取指定地域 且 指定名称的存储桶的跨域配置，如只能获取 appid 为 1253653367 中 `ap-beijing` 地域 且 名称为 `example-1253653367` 的存储桶的跨域配置， 则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/` .
#### 示例 
授予 只能获取 APPID 为 1253653367 ，地域为 `ap-beijing` ，存储桶为 `example-1253653367` 的跨域配置的操作权限，其策略详细内容如下：
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
### 删除存储桶跨域配置 (Delete Bucket CORS) 
若授予 删除存储桶跨域配置 操作权限，则策略的 `action` 为 `name/cos:DeleteBucketCORS` .<br>
若 可删除任意地域的存储桶的跨域配置，则策略的 `resource` 为 `*` .<br>
若 只能删除指定地域的存储桶的跨域配置，如只能删除 appid 为 1253653367 中 `ap-beijing` 地域的存储桶的跨域配置，则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/*` .<br>
若 只能删除指定地域 且 指定名称的存储桶的跨域配置，如只能删除 appid 为 1253653367 中 `ap-beijing` 地域 且 名称为 `example-1253653367` 的存储桶的跨域配置， 则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/` .
#### 示例 
授予 只能删除 APPID 为 1253653367 ，地域为 `ap-beijing` ，存储桶为 `example-1253653367` 的跨域配置的操作权限，其策略详细内容如下：
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
### 设置存储桶生命周期 (Put Bucket Lifecycle) 
若授予 设置存储桶生命周期 操作权限，则策略的 `action` 为 `name/cos:PutBucketLifecycle` .<br>
若 可设置任意地域的存储桶的生命周期配置，则策略的 `resource` 为 `*` .<br>
若 只能设置指定地域的存储桶的生命周期配置，如只能设置 appid 为 1253653367 中 `ap-beijing` 地域的存储桶的生命周期配置，则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/*` .<br>
若 只能设置指定地域 且 指定名称的存储桶的生命周期配置，如只能设置 appid 为 1253653367 中 `ap-beijing` 地域 且 名称为 `example-1253653367` 的存储桶的生命周期配置， 则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/` .
#### 示例 
授予 只能设置 APPID 为 1253653367 ，地域为 `ap-beijing` ，存储桶为 `example-1253653367` 的生命周期配置的操作权限，其策略详细内容如下：
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
### 获取存储桶生命周期 (Get Bucket Lifecycle) 
若授予 获取存储桶生命周期 操作权限，则策略的 `action` 为 `name/cos:GetBucketLifecycle` .<br>
若 可获取任意地域的存储桶的生命周期配置，则策略的 `resource` 为 `*` .<br>
若 只能获取指定地域的存储桶的生命周期配置，如只能获取 appid 为 1253653367 中 `ap-beijing` 地域的存储桶的生命周期配置，则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/*` .<br>
若 只能获取指定地域 且 指定名称的存储桶的生命周期配置，如只能获取 appid 为 1253653367 中 `ap-beijing` 地域 且 名称为 `example-1253653367` 的存储桶的生命周期配置， 则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/` .
#### 示例 
授予 只能获取 APPID 为 1253653367 ，地域为 `ap-beijing` ，存储桶为 `example-1253653367` 的生命周期配置的操作权限，其策略详细内容如下：
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
### 删除存储桶生命周期 (Delete Bucket Lifecycle) 
若授予 删除存储桶生命周期 操作权限，则策略的 `action` 为 `name/cos:DeleteBucketLifecycle` .<br>
若 可删除任意地域的存储桶的生命周期配置，则策略的 `resource` 为 `*` .<br>
若 只能删除指定地域的存储桶的生命周期配置，如只能删除 appid 为 1253653367 中 `ap-beijing` 地域的存储桶的生命周期配置，则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/*` .<br>
若 只能删除指定地域 且 指定名称的存储桶的生命周期配置，如只能删除 appid 为 1253653367 中 `ap-beijing` 地域 且 名称为 `example-1253653367` 的存储桶的生命周期配置， 则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/` .
#### 示例 
授予 只能删除 APPID 为 1253653367 ，地域为 `ap-beijing` ，存储桶为 `example-1253653367` 的生命周期配置的操作权限，其策略详细内容如下：
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
### 获取存储桶中正在分片上传信息 (List Multipart Uploads) 
若授予 获取存储桶中正在分片上传信息 操作权限，则策略的 `action` 为 `name/cos:ListMultipartUploads` .<br>
若 可获取任意地域的存储桶中的正在分片上传信息，则策略的 `resource` 为 `*` .<br>
若 只能获取指定地域的存储桶中的正在分片上传信息，如只能获取 appid 为 1253653367 中 `ap-beijing` 地域的存储桶中的正在分片上传信息，则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/*` .<br>
若 只能获取指定地域 且 指定名称的存储桶中的正在分片上传信息，如只能获取 appid 为 1253653367 中 `ap-beijing` 地域 且 名称为 `example-1253653367` 的存储桶中的正在分片上传信息， 则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/` .
#### 示例 
授予 只能获取 APPID 为 1253653367 ，地域为 `ap-beijing` ，存储桶为 `example-1253653367` 的正在分片上传信息的操作权限，其策略详细内容如下：
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

### 简单上传 (Put Object) 
若授予 简单上传 操作权限，则策略的 `action` 为 `name/cos:PutObject` .<br>
若 对象可以存储在任意位置，则策略的 `resource` 为 `*` .<br>
若 对象只可存储在指定的存储桶中，如只能存储于 appid 为 1253653367 ， 地域为 `ap-beijing` 地域 且 名称为 `example-1253653367` 的存储桶中，则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/*` .<br>
若 对象只可存储在指定的存储桶 且 指定的路径前缀下，如只能存储于 appid 为 1253653367 ， 地域为 `ap-beijing` 地域，存储桶为 `example-1253653367` 的路径为 `test` 下，则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/test/*` .<br>
若 对象只可存储在指定的绝对位置，如只能存储于 appid 为 1253653367 ， 地域为 `ap-beijing` 地域，存储桶为 `example-1253653367` ，绝对路径为 `test/audio.mp3` ，则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/test/audio.mp3` .
#### 示例 
授予 只能在 APPID 为 1253653367 ，地域为 `ap-beijing` ，存储桶为 `example-1253653367` ，路径前缀为 `test` 下简单上传的操作权限，其策略详细内容如下：
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
        "qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/test/*"
      ]
    }
  ]
}
```
### 分片上传 (Initiate Multipar tUpload, List Parts, Upload Part, Complete Multipart Upload, Abort Multipart Upload) 
若授予 分片上传 操作权限，则策略的 `action` 为 `"name/cos:InitiateMultipartUpload","name/cos:ListParts","name/cos:UploadPart","name/cos:CompleteMultipartUpload","name/cos:AbortMultipartUpload"` 的集合.<br>
若 对象可以存储在任意位置，则策略的 `resource` 为 `*` .<br>
若 对象只可存储在指定的存储桶中，如只能存储于 appid 为 1253653367 ， 地域为 `ap-beijing` 地域 且 名称为 `example-1253653367` 的存储桶中，则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/*` .<br>
若 对象只可存储在指定的存储桶 且 指定的路径前缀下，如只能存储于 appid 为 1253653367 ， 地域为 `ap-beijing` 地域，存储桶为 `example-1253653367` 的路径为 `test` 下，则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/test/*` .<br>
若 对象只可存储在指定的绝对位置，如只能存储于 appid 为 1253653367 ， 地域为 `ap-beijing` 地域，存储桶为 `example-1253653367` ，绝对路径为 `test/audio.mp3` ，则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/test/audio.mp3` .
#### 示例 
授予 只能在 APPID 为 1253653367 ，地域为 `ap-beijing` ，存储桶为 `example-1253653367` ，路径前缀为 `test` 下分片上传的操作权限，其策略详细内容如下：
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
        "qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/test/*"
      ]
    }
  ]
}
```

### Post 上传 (Post Object) 
若授予 Post上传 操作权限，则策略的 `action` 为 `name/cos:PostObject` .<br>
若 对象可以存储在任意位置，则策略的 `resource` 为 `*` .<br>
若 对象只可存储在指定的存储桶中，如只能存储于 appid 为 1253653367 ， 地域为 `ap-beijing` 地域 且 名称为 `example-1253653367` 的存储桶中，则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/*` .<br>
若 对象只可存储在指定的存储桶 且 指定的路径前缀下，如只能存储于 appid 为 1253653367 ， 地域为 `ap-beijing` 地域，存储桶为 `example-1253653367` 的路径为 `test` 下，则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/test/*` .<br>
若 对象只可存储在指定的绝对位置，如只能存储于 appid 为 1253653367 ， 地域为 `ap-beijing` 地域，存储桶为 `example-1253653367` ，绝对路径为 `test/audio.mp3` ，则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/test/audio.mp3` .
#### 示例 
授予 只能在 APPID 为 1253653367 ，地域为 `ap-beijing` ，存储桶为 `example-1253653367` ，路径前缀为 `test` 下Post上传的操作权限，其策略详细内容如下：
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
        "qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/test/*"
      ]
    }
  ]
}
```
### 检索对象 (Head Object) 
若授予 检索对象 操作权限，则策略的 `action` 为 `name/cos:HeadObject` .<br>
若 可以检索任意对象，则策略的 `resource` 为 `*` .<br>
若 只可检索指定的存储桶的任意对象，如只能检索 appid 为 1253653367 ， 地域为 `ap-beijing` 且 名称为 `example-1253653367` 的存储桶的任意对象 ，则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/*` .<br>
若 只可检索指定的存储桶 且 指定的路径前缀下的任意对象，如只能检索 appid 为 1253653367 ， 地域为 `ap-beijing` ，存储桶为 `example-1253653367` ，路径前缀为 `test` 下的任意对象，则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/test/*` .<br>
若 只可检索指定的对象，如只能检索 appid 为 1253653367 ， 地域为 `ap-beijing` ，存储桶为 `example-1253653367`  下的 `test/audio.mp3` 这个对象，则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/test/audio.mp3` .
#### 示例 
授予 只能检索 APPID 为 1253653367 ，地域为 `ap-beijing` ，存储桶为 `example-1253653367` ，路径前缀为 `test` 下对象的操作权限，其策略详细内容如下：
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
        "qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/test/*"
      ]
    }
  ]
}
```
### 下载对象 (Get Object) 
若授予 下载对象 操作权限，则策略的 `action` 为 `name/cos:GetObject` .<br>
若 可以下载任意对象，则策略的 `resource` 为 `*` .<br>
若 只可下载指定的存储桶的任意对象，如只能下载 appid 为 1253653367 ， 地域为 `ap-beijing` 且 名称为 `example-1253653367` 的存储桶的任意对象 ，则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/*` .<br>
若 只可下载指定的存储桶 且 指定的路径前缀下的任意对象，如只能下载 appid 为 1253653367 ， 地域为 `ap-beijing` ，存储桶为 `example-1253653367` ，路径前缀为 `test` 下的任意对象，则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/test/*` .<br>
若 只可下载指定的对象，如只能下载 appid 为 1253653367 ， 地域为 `ap-beijing` ，存储桶为 `example-1253653367`  下的 `test/audio.mp3` 这个对象，则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/test/audio.mp3` .
#### 示例 
授予 只能下载 APPID 为 1253653367 ，地域为 `ap-beijing` ，存储桶为 `example-1253653367` ，路径前缀为 `test` 下对象的操作权限，其策略详细内容如下：
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
        "qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/test/*"
      ]
    }
  ]
}
```
### 简单复制 (Put Object Copy) 
若授予 简单复制 操作权限，则策略的目标对象的 `action` 为 `name/cos:PutObject` ， 和 源对象的`action` 为 `name/cos:GetObject` .<br>
若 源对象或目标对象存储在任意位置，则源对象或目标对象策略的 `resource` 为 `*` .<br>
若 源对象或目标对象只存储在指定的存储桶中，如源对象或目标对象只存储于 appid 为 1253653367 ， 地域为 `ap-beijing` 地域 且 名称为 `example-1253653367` 的存储桶中，则源对象或目标对象策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/*` .<br>
若 源对象或目标对象只存储在指定的存储桶 且 指定的路径前缀下，如源对象或目标对象只存储于 appid 为 1253653367 ， 地域为 `ap-beijing` 地域，存储桶为 `example-1253653367` 的路径为 `test` 下，则源对象或目标对象策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/test/*` .
若 源对象或目标对象只存储在指定的绝对位置，如源对象或目标对象只存储于 appid 为 1253653367 ， 地域为 `ap-beijing` 地域，存储桶为 `example-1253653367` ，绝对路径为 `test/audio.mp3` ，则源对象或目标对象策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/test/audio.mp3` .
#### 示例 
授予在APPID 为 1253653367 ，地域为 `ap-beijing` ，存储桶为 `example-1253653367` 的路径前缀为 `test` 下进行简单复制的操作权限，其策略详细内容如下：
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
        "qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/test/*"
      ]
    },
    {
      "action": [
        "name/cos:GetObject"
      ],
      "effect": "allow",
      "resource": [
        "qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/test/*"    //这是源对象
      ]
    }
  ]
}
```
### 分片复制 (Upload Part Copy)
若授予 分片复制 操作权限，则策略的目标对象的 `action` 为 `action` 为 `"name/cos:InitiateMultipartUpload","name/cos:ListParts","name/cos:PutObject","name/cos:CompleteMultipartUpload","name/cos:AbortMultipartUpload"` 集合， 和 源对象的`action` 为 `name/cos:GetObject` <br>
若 源对象或目标对象存储在任意位置，则源对象或目标对象策略的 `resource` 为 `*` .<br>
若 源对象或目标对象只存储在指定的存储桶中，如源对象或目标对象只存储于 appid 为 1253653367 ， 地域为 `ap-beijing` 地域 且 名称为 `example-1253653367` 的存储桶中，则源对象或目标对象策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/*` .<br>
若 源对象或目标对象只存储在指定的存储桶 且 指定的路径前缀下，如源对象或目标对象只存储于 appid 为 1253653367 ， 地域为 `ap-beijing` 地域，存储桶为 `example-1253653367` 的路径为 `test` 下，则源对象或目标对象策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/test/*` .
若 源对象或目标对象只存储在指定的绝对位置，如源对象或目标对象只存储于 appid 为 1253653367 ， 地域为 `ap-beijing` 地域，存储桶为 `example-1253653367` ，绝对路径为 `test/audio.mp3` ，则源对象或目标对象策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/test/audio.mp3` .
#### 示例 
授予在APPID 为 1253653367 ，地域为 `ap-beijing` ，存储桶为 `example-1253653367` 的路径前缀为 `test` 下进行分片复制的操作权限，其策略详细内容如下：
```
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
### 设置对象 ACL (Put Object ACL) 
若授予 设置对象 ACL 操作权限，则策略的 `action` 为 `name/cos:PutObjectACL` .<br>
若 可以设置任意对象 ACL ，则策略的 `resource` 为 `*` .<br>
若 只可设置指定的存储桶的任意对象 ACL ，如只能设置 appid 为 1253653367 ， 地域为 `ap-beijing` 且 名称为 `example-1253653367` 的存储桶的任意对象 ACL ，则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/*` .<br>
若 只可设置指定的存储桶 且 指定的路径前缀下的任意对象 ACL ，如只能设置 appid 为 1253653367 ， 地域为 `ap-beijing` ，存储桶为 `example-1253653367` ，路径前缀为 `test` 下的任意对象 ACL ，则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/test/*` .<br>
若 只可设置指定的对象 ACL ，如只能设置 appid 为 1253653367 ， 地域为 `ap-beijing` ，存储桶为 `example-1253653367`  下的 `test/audio.mp3` 这个对象 ACL ，则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/test/audio.mp3` .
#### 示例 
授予 只能设置 APPID 为 1253653367 ，地域为 `ap-beijing` ，存储桶为 `example-1253653367` ，路径前缀为 `test` 下对象的 ACL 操作权限，其策略详细内容如下：
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
### 获取对象 ACL (Get Object ACL) 
若授予 获取对象 ACL 操作权限，则策略的 `action` 为 `name/cos:GetObjectACL` .<br>
若 可以获取任意对象 ACL ，则策略的 `resource` 为 `*` .<br>
若 只可获取指定的存储桶的任意对象 ACL ，如只能获取 appid 为 1253653367 ， 地域为 `ap-beijing` 且 名称为 `example-1253653367` 的存储桶的任意对象 ACL ，则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/*` .<br>
若 只可获取指定的存储桶 且 指定的路径前缀下的任意对象 ACL ，如只能获取 appid 为 1253653367 ， 地域为 `ap-beijing` ，存储桶为 `example-1253653367` ，路径前缀为 `test` 下的任意对象 ACL ，则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/test/*` .<br>
若 只可获取指定的对象 ACL ，如只能获取 appid 为 1253653367 ， 地域为 `ap-beijing` ，存储桶为 `example-1253653367`  下的 `test/audio.mp3` 这个对象 ACL ，则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/test/audio.mp3` .
#### 示例 
授予 只能获取 APPID 为 1253653367 ，地域为 `ap-beijing` ，存储桶为 `example-1253653367` ，路径前缀为 `test` 下对象的 ACL 操作权限，其策略详细内容如下：
```
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
### Options 请求 (Options Object) 
若授予 Options 请求 操作权限，则策略的 `action` 为 `name/cos:OptionsObject` .<br>
若 可以 Options 请求任意对象，则策略的 `resource` 为 `*` .<br>
若 只可 Options 请求指定的存储桶的任意对象，如只能 Options 请求 appid 为 1253653367 ， 地域为 `ap-beijing` 且 名称为 `example-1253653367` 的存储桶的任意对象，则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/*` .<br>
若 只可 Options 请求指定的存储桶 且 指定的路径前缀下的任意对象，如只能 Options 请求 appid 为 1253653367 ， 地域为 `ap-beijing` ，存储桶为 `example-1253653367` ，路径前缀为 `test` 下的任意对象，则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/test/*` .<br>
若 只可 Options 请求指定的对象，如只能 Options 请求 appid 为 1253653367 ， 地域为 `ap-beijing` ，存储桶为 `example-1253653367`  下的 `test/audio.mp3` 这个对象，则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/test/audio.mp3` .
#### 示例 
授予 只能 Options 请求 APPID 为 1253653367 ，地域为 `ap-beijing` ，存储桶为 `example-1253653367` ，路径前缀为 `test` 下对象的操作权限，其策略详细内容如下：
```
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
### 恢复归档 (Post Object Restore) 
若授予 恢复归档 操作权限，则策略的 `action` 为 `name/cos:PostObjectRestore` .<br>
若 可以恢复归档任意对象，则策略的 `resource` 为 `*` .<br>
若 只可恢复归档指定的存储桶的任意对象，如只能恢复归档 appid 为 1253653367 ， 地域为 `ap-beijing` 且 名称为 `example-1253653367` 的存储桶的任意对象，则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/*` .<br>
若 只可恢复归档指定的存储桶 且 指定的路径前缀下的任意对象，如只能恢复归档 appid 为 1253653367 ， 地域为 `ap-beijing` ，存储桶为 `example-1253653367` ，路径前缀为 `test` 下的任意对象，则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/test/*` .<br>
若 只可恢复归档指定的对象，如只能恢复归档 appid 为 1253653367 ， 地域为 `ap-beijing` ，存储桶为 `example-1253653367`  下的 `test/audio.mp3` 这个对象，则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/test/audio.mp3` .
#### 示例 
授予 只能恢复归档 APPID 为 1253653367 ，地域为 `ap-beijing` ，存储桶为 `example-1253653367` ，路径前缀为 `test` 下对象的操作权限，其策略详细内容如下：
```
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
### 删除对象 (Delete Object) 
若授予 删除对象 操作权限，则策略的 `action` 为 `name/cos:DeleteObject` .<br>
若 可以删除任意对象，则策略的 `resource` 为 `*` .<br>
若 只可删除指定的存储桶的任意对象，如只能删除 appid 为 1253653367 ， 地域为 `ap-beijing` 且 名称为 `example-1253653367` 的存储桶的任意对象，则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/*` .<br>
若 只可删除指定的存储桶 且 指定的路径前缀下的任意对象，如只能删除 appid 为 1253653367 ， 地域为 `ap-beijing` ，存储桶为 `example-1253653367` ，路径前缀为 `test` 下的任意对象，则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/test/*` .<br>
若 只可删除指定的对象，如只能删除 appid 为 1253653367 ， 地域为 `ap-beijing` ，存储桶为 `example-1253653367`  下的 `test/audio.mp3` 这个对象，则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/test/audio.mp3` .
#### 示例 
授予 只能删除 APPID 为 1253653367 ，地域为 `ap-beijing` ，存储桶为 `example-1253653367` 中的 `audio.mp3` 这个对象的操作权限，其策略详细内容如下：
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
### 批量删除对象 (Delete Multiple Objects) 
若授予 批量删除 操作权限，则策略的 `action` 为 `name/cos:DeleteObject` .<br>
若 可以批量删除任意对象，则策略的 `resource` 为 `*` .<br>
若 只可批量删除指定的存储桶的任意对象，如只能批量删除 appid 为 1253653367 ， 地域为 `ap-beijing` 且 名称为 `example-1253653367` 的存储桶的任意对象，则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/*` .<br>
若 只可批量删除指定的存储桶 且 指定的路径前缀下的任意对象，如只能批量删除 appid 为 1253653367 ， 地域为 `ap-beijing` ，存储桶为 `example-1253653367` ，路径前缀为 `test` 下的任意对象，则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/test/*` .<br>
若 只可批量删除指定的对象，如只能批量删除 appid 为 1253653367 ， 地域为 `ap-beijing` ，存储桶为 `example-1253653367`  下的 `test/audio.mp3` 和 `test/video.mp4` 两个对象，则策略的 `resource` 为 `qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/test/audio.mp3` ，`qcs::cos:ap-beijing:uid/1253653367:prefix//1253653367/example/test/video.mp4` 的集合.
#### 示例 
授予 只能批量删除 APPID 为 1253653367 ，地域为 `ap-beijing` ，存储桶为 `example-1253653367` 中的 `audio.mp3` 和 `video.mp4` 两个对象的操作权限，其策略详细内容如下：
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

