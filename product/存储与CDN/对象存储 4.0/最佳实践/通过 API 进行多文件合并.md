## 准备工作

1. 多文件合并功能通过云函数（Serverless Cloud Function，SCF）实现，使用前需在对象存储控制台  [应用集成 - 多文件合并](https://console.cloud.tencent.com/cos5/application/cosConcatFile) 上创建**多文件合并**函数。创建指引请参见  [多文件合并](https://cloud.tencent.com/document/product/436/60662)。
2. 函数创建后，根据函数列表操作栏的**使用引导**，完成函数参数配置。具体函数所需参数配置请参考下文，格式为 **JSON 字符串**。
 - 对于选择云函数鉴权的函数，需要调用 SCF 提供的 [运行函数（Invoke）接口](https://cloud.tencent.com/document/api/583/17243) 来运行云函数，其中的 ClientContext 参数以 json 格式传入，请参见 [函数参数配置示例](#1)。
 - 对于选择免鉴权的函数，则可以直接向对应的 API 网关发起 HTTP 请求来调用函数。


<span id=1></span>

## 函数参数配置示例

>? 实际使用当中，需将代码中的注释去掉。
>

```plaintext
{
    "bucket": "examplebucket-1250000000",    // 最终投递合并产物文件的存储桶
    "region": "ap-guangzhou",         // 最终投递合并产物文件的存储桶所在地域
    "key": "concat.txt",              // 最终投递合并产物文件的名称

    /**
     * sourceList 用于指定需打包的源文件列表，格式为 JSON 数组
     * 每一项包含源文件 url 等信息，后续可能拓展更多参数
     * 
     * 如果源文件列表过长，可将 sourceList 参数 JSON 字符串化
     * 写入 .json 文件，上传到 COS，并通过 sourceConfigList 参数指定
     * 
     * sourceList 和 sourceConfigList 参数仅需指定一种即可
     */
    "sourceList": [
        {
            "url": "https://examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/file1.txt"
        },
        {
            "url": "https://examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/file2.txt"
        },
        {
            "url": "https://examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/file3.txt"
        }
    ],
    "sourceConfigList": [
        {
             "url": "https://examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/sourceList.json"
        }
    ]
}
```

参数说明如下：

| 参数名                  | 参数描述                                                     | 类型    | 是否必填 |
| ----------------------- | ------------------------------------------------------------ | ------- | -------- |
| bucket                  | 最终投递合并产物文件的存储桶，命名格式为 BucketName-APPID，此处填写的存储桶名称必须为此格式，例如：examplebucket-1250000000 | String  | 是       |
| region                  | 最终投递合并产物文件的存储桶所在地域，枚举值请参见 [地域和访问域名](https://cloud.tencent.com/document/product/436/6224) | String  | 是       |
| key                     | 最终投递合并产物文件的名称（Object 的名称），对象在存储桶中的唯一标识，详情请参见 [对象概述](https://cloud.tencent.com/document/product/436/13324) | String  | 是       |
| sourceList              | 源文件列表，**sourceList 和 sourceConfigList 不能同时为空**  | Array   | 是       |
| sourceList[].url        | 源文件的 URL                                                 | String  | 是       |
| sourceConfigList        | sourceList 的配置文件列表，如果您不希望在请求时携带整个 sourceList，可以将 sourceList 参数 JSON 字符串处理，生成 json 配置文件，上传到 COS，并在 sourceConfigList 中指定该文件的 URL，支持指定多个配置文件，**sourceList 和 sourceConfigList 不能同时为空** | Array   | 否       |
| sourceConfigList[].url  | sourceList 配置文件的 URL                                    | String  | 否       |

## 函数响应结果示例
```plaintext
{
    "code": 0,
    "message": "cos concat file success",
    "data": {
        "Location": "examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/concat.txt",
        "Bucket": "examplebucket-1250000000",
        "Key": "concat.txt",
        "ETag": "\"152958e4f4bfded94c0b30f03343d6b8-1\""
    }
}
```

响应参数说明如下：

| 参数名  | 参数描述                                               | 类型             |
| ------- | ------------------------------------------------------ | ---------------- |
| code    | 业务错误码，如果为 0 则说明执行成功，否则为执行失败    | Number           |
| message | 执行结果的文字说明，可能为 null                        | String           |
| data    | 执行成功的信息，如果执行成功，则包含合并产物文件的 URL 信息 | Object           |
| error   | 执行的错误信息，如执行成功则为 null                    | Object or String |

## 实际案例



### 参数配置
```plaintext
{
  "bucket": "examplebucket-1250000000",
  "region": "ap-guangzhou",
  "key": "concat.txt",
  "sourceList": [
      {
          "url": "https://examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/file1.txt"
      },
      {
          "url": "https://examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/file2.txt"
      },
      {
          "url": "https://examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/file3.txt"
      }
  ]
}
```

### 最终多文件合并产物结构

```plaintext
concat.txt
    ├── content of file1.txt
    ├── content of file2.txt
    └── content of file3.txt
```
