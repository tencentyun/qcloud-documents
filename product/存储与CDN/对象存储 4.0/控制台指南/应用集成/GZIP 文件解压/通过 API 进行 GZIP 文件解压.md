## 准备工作

1. GZIP 文件解压功能通过云函数（Serverless Cloud Function，SCF）实现。使用前，需在对象存储控制台 [应用集成 - GZIP 文件解压](https://console.cloud.tencent.com/cos5/application/cosGunzipApi) 上创建 **GZIP 文件解压** 函数。创建指引请参见 [GZIP 文件解压](https://cloud.tencent.com/document/product/436/65354)。
2. 函数创建后，根据函数列表操作栏的 **使用引导**，完成函数参数配置。具体函数所需参数配置请参考下文，格式为 **JSON 字符串**。
 - 对于选择云函数鉴权的函数，需要调用 SCF 提供的 [运行函数（Invoke）接口 ](https://cloud.tencent.com/document/api/583/17243) 来运行云函数，其中的 ClientContext 参数以 JSON 格式传入，请参见 [函数参数配置示例](#1)。
 - 对于选择免鉴权的函数，则可以直接向对应的 API 网关发起 HTTP 请求来调用函数。


<span id=1></span>
## 函数参数配置示例

>? 实际使用当中，需将代码中的注释去掉。
>

```plaintext
{
    "bucket": "examplebucket-1250000000",    // 存放 GZIP 包的源存储桶
    "region": "ap-guangzhou",         // 存放 GZIP 包的源存储桶所在地域
    "key": "example.txt.gz",              //  GZIP 包的名称
    "targetBucket": "examplebucket-1250000000",    // 最终投递解压产物的目标存储桶
    "targetRegion": "ap-guangzhou",         // 最终投递解压产物的目标存储桶所在地域
    "targetPrefix": "target/",              // 最终投递解压产物的前缀
}
```

参数说明如下：

| 参数名                  | 参数描述                                                     | 类型    | 是否必填 |
| ----------------------- | ------------------------------------------------------------ | ------- | -------- |
| bucket                  | 存放 GZIP 包的源存储桶，命名格式为 BucketName-APPID，此处填写的存储桶名称必须为此格式，例如：examplebucket-1250000000 | String  | 是       |
| region                  | 存放 GZIP 包的源存储桶所在地域，枚举值请参见 [地域和访问域名](https://cloud.tencent.com/document/product/436/6224) | String  | 是       |
| key                     |  GZIP 包的名称（Object 的名称），对象在存储桶中的唯一标识，详情请参见 [对象概述](https://cloud.tencent.com/document/product/436/13324) | String  | 是       |
| targetBucket                  | 最终投递解压产物的目标存储桶，命名格式为 BucketName-APPID，此处填写的存储桶名称必须为此格式，例如：examplebucket-1250000000 | String  | 是       |
| targetRegion                  | 最终投递解压产物的目标存储桶所在地域，枚举值请参见 [地域和访问域名](https://cloud.tencent.com/document/product/436/6224) | String  | 是       |
| targetPrefix                     | 最终投递解压产物的前缀，投递到指定目录请以斜杠 / 结尾，缺省或空字符串则视为投递到根路径下 | String  | 否       |

## 函数响应结果示例
```plaintext
{
    "code": 0,
    "message": "cos gunzip file success",
    "data": {
        "Bucket": "examplebucket-1250000000",
        "Region": "ap-guangzhou"
    }
}
```

响应参数说明如下：

| 参数名  | 参数描述                                               | 类型             |
| ------- | ------------------------------------------------------ | ---------------- |
| code    | 业务错误码，如果为0，则说明执行成功，否则为执行失败    | Number           |
| message | 执行结果的文字说明，可能为 null                        | String           |
| data    | 执行成功的信息，如果执行成功，则包含最终投递解压产物的目标存储桶信息 | Object           |
| error   | 执行的错误信息，如执行成功则为 null                    | Object or String |

## 实际案例

### 案例一：解压 *.gz 文件

#### 参数配置

```plaintext
{
  "bucket": "examplebucket-1250000000",
  "region": "ap-guangzhou",
  "key": "example.txt.gz",
  "targetBucket": "examplebucket-1250000000",
  "targetRegion": "ap-guangzhou",
  "targetPrefix": "target/"
}
```

#### 最终解压产物位置

```plaintext
target/example.txt
```

### 案例二：解压 *.tar.gz 和 *.tgz 文件

#### 参数配置
```plaintext
{
  "bucket": "examplebucket-1250000000",
  "region": "ap-guangzhou",
  "key": "example.tar.gz",
  "targetBucket": "examplebucket-1250000000",
  "targetRegion": "ap-guangzhou",
  "targetPrefix": "target/"
}
```

#### 压缩包结构

```
example.tar.gz
    ├── example-subfile-1.txt
    ├── example-subfile-2.png
    └── example-subfile-3.mp4
```

#### 最终解压产物位置

```plaintext
target/example-subfile-1.txt
target/example-subfile-2.png
target/example-subfile-3.mp4
```
