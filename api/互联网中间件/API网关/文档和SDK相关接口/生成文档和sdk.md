
# GenerateApiDocument

## 接口描述

	此接口用于自动生成API文档和SDK，一个服务的一个环境生成一份文档和SDK。​

## 1、输入参数

以下请求参数列表仅列出了接口请求参数，其它参数可参考[公共请求参数](/document/api/213/6976)。

| 参数名称        | 是否必选 | 类型     | 描述            |
| ----------- | ---- | ------ | ------------- |
| serviceId   | 是    | String | 待创建文档的服务唯一Id。 |
| language    | 是    | String | 待创建SDK的语言。当前只支持"python"和"javascript"。 |
| environment | 是    | String | 待创建SDK的服务所在环境。 |

## 2、输出参数
| 参数名称         | 类型     | 描述                                       |
| ------------ | ------ | ---------------------------------------- |
| code         | Int    | 公共错误码, 0表示成功，其他值表示失败。详见错误码页面的<a href="https://www.qcloud.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="公共错误码">公共错误码</a>。 |
| codeDesc     | String | 业务侧错误码。成功时返回Success，错误时返回具体业务错误原因。       |
| documentURL | String | 生成的document会存放到cos中，此出参返回产生文件的下载链接。      |
| sdkURL | String | 生成的SDK会存放到cos中，此出参返回产生SDK文件的下载链接。        |

## 3、示例 
```
https://apigateway.api.qcloud.com/v2/index.php?
&<公共请求参数>
&Action=GenerateApiDocument
&serviceId=service-xxxx
&language=python
&environment=release
```
返回示例如下：
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",      
    "documentURL":"http://api-document-1253970226.cosgz.myqcloud.com/service-xxxx.zip",
	"sdkURL":"http://api-sdk-python-1253970226.cosgz.myqcloud.com/service-xxxx.zip",
}
```




