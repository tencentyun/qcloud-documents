>!在给子用户或协作者授予 API 操作权限时，请务必根据业务需要，按照最小权限原则进行授权。如果您直接授予子用户或者协作者所有资源`(resource:*)`，或所有操作`(action:*)`权限，则存在由于权限范围过大导致数据安全风险。


## 概述
对象存储 COS 使用临时密钥服务时，不同的 COS API 操作需要不同的操作权限，而且可以同时指定一个操作或一序列操作。

COS API 授权策略（policy）是一种 JSON 字符串。例如，授予 APPID 为1250000000，地域为 ap-beijing，存储桶为 examplebucket-1250000000 ，路径前缀为 doc 的上传操作（包括简单上传、表单上传、分块上传等操作）的权限，路径前缀为 doc2 的下载操作权限的策略内容如下所示：
```shell
{
	"version": "2.0",
	"statement": [{
			"action": [
				//简单上传操作 
				"name/cos:PutObject",
				//表单上传对象 
				"name/cos:PostObject",
				//分块上传：初始化分块操作 
				"name/cos:InitiateMultipartUpload",
				//分块上传：List 进行中的分块上传
				"name/cos:ListMultipartUploads",
				//分块上传：List 已上传分块操作 
				"name/cos:ListParts",
				//分块上传：上传分块块操作 
				"name/cos:UploadPart",
				//分块上传：完成所有分块上传操作 
				"name/cos:CompleteMultipartUpload",
				//取消分块上传操作 
				"name/cos:AbortMultipartUpload"
			],
			"effect": "allow",
			"resource": [
				"qcs::cos:ap-beijing:uid/1250000000:examplebucket-1250000000/doc/*"
			]
		},
		{
			"action": [
				//下载操作 
				"name/cos:GetObject"
			],
			"effect": "allow",
			"resource": [
				"qcs::cos:ap-beijing:uid/1250000000:examplebucket-1250000000/doc2/*"
			]
		}
	]
}
```

<a id="policy"></a>

## 授权策略（policy）元素说明

| 名称     | 描述                                                         |
| -------- | ------------------------------------------------------------ |
| version  | 策略语法版本，默认为2.0                                      |
| effect   | 有 allow （允许）和 deny （显式拒绝）两种情况                |
| resource | 授权操作的具体数据，可以是任意资源、指定路径前缀的资源、指定绝对路径的资源或它们的组合 |
| action   | 此处是指 COS API，根据需求指定一个或者一序列操作的组合或所有操作(`*`)，例如 action 为 `name/cos:GetService`，**请注意区分英文大小写**       |
|condition|约束条件，可以不填，具体说明请参见 [condition](https://cloud.tencent.com/document/product/598/10603#6.-.E7.94.9F.E6.95.88.E6.9D.A1.E4.BB.B6.EF.BC.88condition.EF.BC.89) 说明  |

下面列出了各 COS API 设置授权策略的示例。

## Service API

### 查询存储桶列表

API 接口为 GET Service，若授予其操作权限，则策略的 action 为 name/cos:GetService，resource为`*` 。

#### 示例 

授予查询存储桶列表操作权限的策略详细内容如下：

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

Bucket API 策略的 resource 可以归纳为以下几种情况：

- 操作全部地域的存储桶
则策略的 resource 为`*`，**该策略限定的资源范围，存在由于权限范围过大导致数据安全风险，请谨慎配置**。

- 仅允许操作指定地域的存储桶
例如只允许操作 APPID 为1250000000，地域归属于北京（ap-beijing）的存储桶 examplebucket-1250000000，则策略的 resource 为`qcs::cos:ap-beijing:uid/1250000000:examplebucket-1250000000/*`。

- 仅允许操作指定地域且指定名称的存储桶
例如只可操作 APPID 为1250000000，地域为 ap-beijing 且名称为 examplebucket-1250000000 的存储桶，则策略的 resource 为`qcs::cos:ap-beijing:uid/1250000000:examplebucket-1250000000/`。

Bucket API 策略的 action 则因操作不同而取值不同，以下列举部分 Bucket API 授权策略，其他 Bucket API 授权策略可作参照。

### 创建存储桶 

API 接口为 PUT Bucket，若授予其操作权限，则策略的 action 为 name/cos:PutBucket。

#### 示例 

授予用户 APPID 为1250000000，创建存储桶的权限。例如创建一个地域为北京地域，存储桶名称为 examplebucket-1250000000 的存储桶，则策略详细内容如下：

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
        "qcs::cos:ap-beijing:uid/1250000000:examplebucket-1250000000/"
      ]
    }
  ]
}
```

>?存储桶名称需符合命名规范，详情请参见 [存储桶命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.AD.98.E5.82.A8.E6.A1.B6.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83)。

### 检索存储桶及其权限  

API 接口为 HEAD Bucket，若授予其操作权限，则策略的 action 为 name/cos:HeadBucket。

#### 示例 

授予只能检索 APPID 为1250000000 ，地域为 ap-beijing ，存储桶为 examplebucket-1250000000 的操作权限，其策略详细内容如下：

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
        "qcs::cos:ap-beijing:uid/1250000000:examplebucket-1250000000/"
      ]
    }
  ]
}
```


### 查询对象列表

API 接口为 GET Bucket，若授予其操作权限，则策略的 action 为 name/cos:GetBucket。

#### 示例 

授予只能查询 APPID 为1250000000 ，地域为 ap-beijing，存储桶为 examplebucket-1250000000 的对象列表的操作权限，其策略详细内容如下：

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
        "qcs::cos:ap-beijing:uid/1250000000:examplebucket-1250000000/"
      ]
    }
  ]
}
```

### 删除存储桶

API 接口为 Delete Bucket，若授予其操作权限，则策略的 action 为 name/cos:DeleteBucket。

#### 示例 

授予只能删除 APPID 为1250000000 ，地域为 ap-beijing ，存储桶为 examplebucket-1250000000 的存储桶的操作权限，其策略详细内容如下：

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
        "qcs::cos:ap-beijing:uid/1250000000:examplebucket-1250000000/"
      ]
    }
  ]
}
```

### 设置存储桶 ACL 

API 接口为 Put Bucket ACL，若授予其操作权限，则策略的 action 为 name/cos:PutBucketACL。

#### 示例 

授予只能设置 APPID 为1250000000 ，地域为 ap-beijing ，存储桶为 examplebucket-1250000000 的 ACL 的操作权限，其策略详细内容如下：

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
        "qcs::cos:ap-beijing:uid/1250000000:examplebucket-1250000000/"
      ]
    }
  ]
}
```

### 查询存储桶 ACL

API 接口为 GET Bucket acl，若授予其操作权限，则策略的 action 为 name/cos:GetBucketACL。

#### 示例 

授予只能获取 APPID 为1250000000 ，地域为 ap-beijing ，存储桶为 examplebucket-1250000000 的 ACL 的操作权限，其策略详细内容如下：

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
        "qcs::cos:ap-beijing:uid/1250000000:examplebucket-1250000000/"
      ]
    }
  ]
}
```

### 设置跨域配置

API 接口为 PUT Bucket cors，若授予其操作权限，则策略的 action 为 name/cos:PutBucketCORS。

#### 示例 

授予只能设置 APPID 为1250000000 ，地域为 ap-beijing ，存储桶为 examplebucket-1250000000 的跨域配置的操作权限，其策略详细内容如下：

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
        "qcs::cos:ap-beijing:uid/1250000000:examplebucket-1250000000/"
      ]
    }
  ]
}
```

### 查询跨域配置

API 接口为 GET Bucket cors，若授予其权限，则策略的 action 为 name/cos:GetBucketCORS。

#### 示例 

授予只能查询 APPID 为1250000000 ，地域为 ap-beijing  ，存储桶为 examplebucket-1250000000 的跨域配置的操作权限，其策略详细内容如下：

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
        "qcs::cos:ap-beijing:uid/1250000000:examplebucket-1250000000/"
      ]
    }
  ]
}
```

### 删除跨域配置

API 接口为 DELETE Bucket cors，若授予其操作权限，则策略的 action 为 name/cos:DeleteBucketCORS。

#### 示例 

授予只能删除 APPID 为1250000000 ，地域为 ap-beijing ，存储桶为 examplebucket-1250000000 的跨域配置的操作权限，其策略详细内容如下：

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
        "qcs::cos:ap-beijing:uid/1250000000:examplebucket-1250000000/"
      ]
    }
  ]
}
```

### 设置生命周期

API 接口为 PUT Bucket lifecycle，若授予其操作权限，则策略的 action 为 name/cos:PutBucketLifecycle 。

#### 示例 

授予只能设置 APPID 为1250000000 ，地域为 ap-beijing ，存储桶为 examplebucket-1250000000 的生命周期配置的操作权限，其策略详细内容如下：

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
        "qcs::cos:ap-beijing:uid/1250000000:examplebucket-1250000000/"
      ]
    }
  ]
}
```

### 查询生命周期

API 接口为 GET Bucket lifecycle，若授予其操作权限，则策略的 action 为 name/cos:GetBucketLifecycle。

#### 示例 

授予只能查询 APPID 为1250000000 ，地域为 ap-beijing ，存储桶为 examplebucket-1250000000 的生命周期配置的操作权限，其策略详细内容如下：

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
        "qcs::cos:ap-beijing:uid/1250000000:examplebucket-1250000000/"
      ]
    }
  ]
}
```

### 删除生命周期

API 接口为 DELETE Bucket lifecycle，若授予其操作权限，则策略的 action 为 name/cos:DeleteBucketLifecycle。

#### 示例 

授予只能删除 APPID 为1250000000 ，地域为 ap-beijing，存储桶为 examplebucket-1250000000 的生命周期配置的操作权限，其策略详细内容如下：

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
        "qcs::cos:ap-beijing:uid/1250000000:examplebucket-1250000000/"
      ]
    }
  ]
}
```


## Object API

Object API 策略的 resource 可以归纳为以下几种情况：

- 可操作任意对象，策略的 resource 为`*`。
- 只可操作指定存储桶中的任意对象，如只可操作 APPID 为1250000000 ， 地域为 ap-beijing，且名称为 examplebucket-1250000000 的存储桶中的任意对象，则策略的 resource 为`qcs::cos:ap-beijing:uid/1250000000:examplebucket-1250000000/*`。
- 只可操作指定存储桶 且 指定路径前缀下的任意对象，如只可操作 APPID 为1250000000 ， 地域为 ap-beijing，存储桶为 examplebucket-1250000000，路径前缀为 doc 下的任意对象，则策略的 resource 为`qcs::cos:ap-beijing:uid/1250000000:examplebucket-1250000000/doc/*`。
- 只可操作指定绝对路径的对象，如只可操作 APPID 为1250000000 ， 地域为 ap-beijing，存储桶为 examplebucket-1250000000，绝对路径为`doc/audio.mp3`的对象，则策略的 resource 为`qcs::cos:ap-beijing:uid/1250000000:examplebucket-1250000000/doc/audio.mp3`。


Object API 策略的 action 则因操作不同而取值不同，以下列举所有 Object API 授权策略。

### 简单上传对象

API 接口为 PUT Object，若授予其操作权限，则策略的 action为 name/cos:PutObject。

#### 示例 

授予只能在 APPID 为1250000000 ，地域为 ap-beijing，存储桶为 examplebucket-1250000000，路径前缀为 doc 下进行简单上传的操作权限，其策略详细内容如下：

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
        "qcs::cos:ap-beijing:uid/1250000000:examplebucket-1250000000/doc/*"
      ]
    }
  ]
}
```

### 分块上传 

分块上传包含 Initiate Multipart Upload，List Multipart Uploads，List Parts，Upload Part，Complete Multipart Upload，Abort Multipart Upload。若授予其操作权限，则策略的 action 为： `"name/cos:InitiateMultipartUpload","name/cos:ListMultipartUploads","name/cos:ListParts","name/cos:UploadPart","name/cos:CompleteMultipartUpload","name/cos:AbortMultipartUpload"`的集合。

#### 示例 

授予只能在 APPID 为1250000000 ，地域为 ap-beijing ，存储桶为 examplebucket-1250000000，路径前缀为 doc 下进行分块上传的操作权限，其策略详细内容如下：

```shell
{
  "version": "2.0",
  "statement": [
    {
      "action": [
        "name/cos:InitiateMultipartUpload",
        "name/cos:ListMultipartUploads",
        "name/cos:ListParts",
        "name/cos:UploadPart",
        "name/cos:CompleteMultipartUpload",
        "name/cos:AbortMultipartUpload"
      ],
      "effect": "allow",
      "resource": [
        "qcs::cos:ap-beijing:uid/1250000000:examplebucket-1250000000/doc/*"
      ]
    }
  ]
}
```

### 查询分块上传

查询存储桶中正在分块上传信息，若授予其操作权限，则策略的 action 为 name/cos:ListMultipartUploads。

#### 示例 

授予只能查询 APPID 为1250000000 ，地域为 ap-beijing  ，存储桶为 examplebucket-1250000000 中的正在分块上传信息的操作权限，其策略详细内容如下：

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
        "qcs::cos:ap-beijing:uid/1250000000:examplebucket-1250000000/"
      ]
    }
  ]
}
```


### 表单上传对象

API 接口为 POST Object，若授予其操作权限，则策略的 action 为 name/cos:PostObject。

#### 示例 

授予只能在 APPID 为1250000000 ，地域为 ap-beijing ，存储桶为 examplebucket-1250000000，路径前缀为 doc 下进行 POST 上传的操作权限，其策略详细内容如下：

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
        "qcs::cos:ap-beijing:uid/1250000000:examplebucket-1250000000/doc/*"
      ]
    }
  ]
}
```

### 追加上传对象

API 接口为 Append Object，若授予其操作权限，则策略的 action为 name/cos:AppendObject。

#### 示例 

授予只能在 APPID 为1250000000 ，地域为 ap-beijing，存储桶为 examplebucket-1250000000，路径前缀为 doc 下进行追加上传的操作权限，其策略详细内容如下：

```shell
 {
  "version": "2.0",
  "statement": [
    {
      "action": [
        "name/cos:AppendObject"
      ],
      "effect": "allow",
      "resource": [
        "qcs::cos:ap-beijing:uid/1250000000:examplebucket-1250000000/doc/*"
      ]
    }
  ]
}
```

### 查询对象元数据

API 接口为 HEAD Object，若授予其操作权限，则策略的 action 为 name/cos:HeadObject。

#### 示例 

授予只能查询 APPID 为1250000000 ，地域为 ap-beijing ，存储桶为 examplebucket-1250000000，路径前缀为 doc 中的对象的操作权限，其策略详细内容如下：

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
        "qcs::cos:ap-beijing:uid/1250000000:examplebucket-1250000000/doc/*"
      ]
    }
  ]
}
```

### 下载对象

API 接口为 GET Object，若授予其操作权限，则策略的 action 为 name/cos:GetObject。

#### 示例 

授予只能下载 APPID 为1250000000 ，地域为 ap-beijing，存储桶为 examplebucket-1250000000，路径前缀为 doc 中的对象的操作权限，其策略详细内容如下：

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
        "qcs::cos:ap-beijing:uid/1250000000:examplebucket-1250000000/doc/*"
      ]
    }
  ]
}
```

### 复制对象

API 接口为 Put Object Copy，若授予其操作权限，则策略的目标对象的 action 为 name/cos:PutObject，和源对象的 action 为 name/cos:GetObject。

#### 示例 

授予在 APPID 为1250000000 ，地域为 ap-beijing，存储桶为 examplebucket-1250000000 的路径前缀为 doc 和路径前缀为 doc2 间进行分块复制的操作权限，其策略详细内容如下：

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
        "qcs::cos:ap-beijing:uid/1250000000:examplebucket-1250000000/doc/*"
      ]
    },
    {
      "action": [
        "name/cos:GetObject"
      ],
      "effect": "allow",
      "resource": [
        "qcs::cos:ap-beijing:uid/1250000000:examplebucket-1250000000/doc2/*"
      ]
    }
  ]
}
```

其中`"qcs::cos:ap-beijing:uid/1250000000:examplebucket-1250000000/doc2/*"`为源对象。

### 复制分块

API 接口为 Upload Part - Copy，若授予其操作权限，则策略的目标对象的 action 为 action 为`"name/cos:InitiateMultipartUpload","name/cos:ListMultipartUploads","name/cos:ListParts","name/cos:PutObject","name/cos:CompleteMultipartUpload","name/cos:AbortMultipartUpload"`集合， 和源对象的 action 为 name/cos:GetObject。

#### 示例 

授予在 APPID 为1250000000 ，地域为 ap-beijing，存储桶为 examplebucket-1250000000 的路径前缀为 doc 和路径前缀为 doc2 间进行分块复制的操作权限，其策略详细内容如下：

```shell
{
  "version": "2.0",
  "statement": [
    {
      "action": [
        "name/cos:InitiateMultipartUpload",
        "name/cos:ListMultipartUploads",
        "name/cos:ListParts",
        "name/cos:PutObject",
        "name/cos:CompleteMultipartUpload",
        "name/cos:AbortMultipartUpload"
      ],
      "effect": "allow",
      "resource": [
        "qcs::cos:ap-beijing:uid/1250000000:examplebucket-1250000000/doc/*"
      ]
    },
    {
      "action": [
        "name/cos:GetObject"
      ],
      "effect": "allow",
      "resource": [
        "qcs::cos:ap-beijing:uid/1250000000:examplebucket-1250000000/doc2/*" 
      ]
    }
  ]
}
```

其中`"qcs::cos:ap-beijing:uid/1250000000:examplebucket-1250000000/doc2/*"`为源对象。

### 设置对象 ACL

API 接口为 Put Object ACL，若授予其操作权限，则策略的 action 为 name/cos:PutObjectACL 。

#### 示例 

授予只能设置 APPID 为1250000000 ，地域为 ap-beijing ，存储桶为 examplebucket-1250000000，路径前缀为 doc 中的对象 ACL 操作权限，其策略详细内容如下：

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
        "qcs::cos:ap-beijing:uid/1250000000:examplebucket-1250000000/doc/*"
      ]
    }
  ]
}
```

### 查询对象 ACL

API 接口为 Get Object ACL，若授予其操作权限，则策略的 action 为 name/cos:GetObjectACL。

#### 示例 

授予只能查询 APPID 为1250000000 ，地域为 ap-beijing，存储桶为 examplebucket-1250000000，路径前缀为 doc 中的对象 ACL 操作权限，其策略详细内容如下：

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
        "qcs::cos:ap-beijing:uid/1250000000:examplebucket-1250000000/doc/*"
      ]
    }
  ]
}
```

### 预请求跨域配置

API 接口为 OPTIONS Object，若授予其操作权限，则策略的 action 为 name/cos:OptionsObject。

#### 示例 

授予只能在 APPID 为1250000000 ，地域为 ap-beijing，存储桶为 examplebucket-1250000000，路径前缀为 doc 下进行 Options 请求 的操作权限，其策略详细内容如下：

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
        "qcs::cos:ap-beijing:uid/1250000000:examplebucket-1250000000/doc/*"
      ]
    }
  ]
}
```

### 恢复归档对象

API 接口为 Post Object Restore，若授予其操作权限，则策略的 action 为 name/cos:PostObjectRestore。

#### 示例 

授予只能在 APPID 为1250000000 ，地域为 ap-beijing，存储桶为 examplebucket-1250000000，路径前缀为 doc 下进行恢复归档的操作权限，其策略详细内容如下：

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
        "qcs::cos:ap-beijing:uid/1250000000:examplebucket-1250000000/doc/*"
      ]
    }
  ]
}
```

### 删除单个对象

API 接口为 DELETE Object，若授予其操作权限，则策略的 action 为 name/cos:DeleteObject。

#### 示例 

授予只能删除 APPID 为1250000000 ，地域为 ap-beijing ，存储桶为 examplebucket-1250000000 中的 audio.mp3 这个对象的操作权限，其策略详细内容如下：

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
        "qcs::cos:ap-beijing:uid/1250000000:examplebucket-1250000000/audio.mp3"
      ]
    }
  ]
}
```

### 删除多个对象

API 接口为 DELETE Multiple Objects，若授予其操作权限，则策略的`action`为`name/cos:DeleteObject`。

#### 示例 

授予只能批量删除 APPID 为1250000000 ，地域为 ap-beijing，存储桶为 examplebucket-1250000000 中的 audio.mp3 和 video.mp4 两个对象的操作权限，其策略详细内容如下：

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
        "qcs::cos:ap-beijing:uid/1250000000:examplebucket-1250000000/audio.mp3",
        "qcs::cos:ap-beijing:uid/1250000000:examplebucket-1250000000/video.mp4"
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
        "name/cos:HeadObject",
        "name/cos:GetObject",
        "name/cos:GetBucket",
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
授予用户只能访问存储桶 examplebucket-1250000000 中路径前缀为 doc 下的文件，且无法操作其它路径文件的操作权限，该策略详细内容如下：
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
        "qcs::cos:ap-shanghai:uid/1250000000:examplebucket-1250000000/doc/*"
      ]
    }
  ]
}
```

