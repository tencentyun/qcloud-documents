## 接口描述

本接口（GenerateApiDocument）用于自动生成 API 文档和 SDK，一个服务的一个环境生成一份文档和 SDK。

## 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数可参考 [公共请求参数](https://cloud.tencent.com/document/product/628/18814)。

| 参数名称        | 是否必选 | 类型     | 描述            |
| ----------- | ---- | ------ | ------------- |
| serviceId   | 是    | String | 待创建文档的服务唯一 ID |
| language    | 是    | String | 待创建 SDK 的语言。当前只支持 Python 和 JavaScript |
| environment | 是    | String | 待创建 SDK 的服务所在环境 |

## 输出参数
| 参数名称         | 类型     | 描述                                       |
| ------------ | ------ | ---------------------------------------- |
| code         | Int    | 公共错误码，0表示成功，其他值表示失败。详见错误码页面的 [公共错误码](https://cloud.tencent.com/document/product/628/18822) |
| codeDesc     | String | 业务侧错误码。成功时返回 Success，错误时返回具体业务错误原因       |
| documentURL | String | 生成的 document 会存放到 COS 中，此出参返回产生文件的下载链接      |
| sdkURL | String | 生成的 SDK 会存放到 COS 中，此出参返回产生 SDK 文件的下载链接        |

## 示例 
```http
https://apigateway.api.qcloud.com/v2/index.php?
&<公共请求参数>
&Action=GenerateApiDocument
&serviceId=service-xxxx
&language=python
&environment=release
```
返回示例如下：
```json
{
	"code": "0",
	"message": "",
	"codeDesc": "Success",
	"documentURL": "http://api-document-1253970226.cosgz.myqcloud.com/service-xxxx.zip",
	"sdkURL": "http://api-sdk-python-1253970226.cosgz.myqcloud.com/service-xxxx.zip"
}
```

