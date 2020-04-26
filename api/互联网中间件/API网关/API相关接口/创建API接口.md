## 接口描述

本接口（CreateApi）用于创建 API 接口，创建 API 前，用户需要先创建服务，每个 API 都有自己归属的服务。


## 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数可参考 [公共请求参数](https://cloud.tencent.com/document/product/628/18814)。

| 参数名称                                     | 是否必选 | 类型      | 描述                                       |
| ---------------------------------------- | ---- | ------- | ---------------------------------------- |
| serviceId                                | 是    | String  | API 所在的服务唯一 ID。                            |
| apiName                                  | 否    | String  | 用户自定义的 API 名称。                             |
| apiDesc                                  | 否    | String  | 用户自定义的 API 接口描述。                           |
| apiType                                  | 否    | String  | API 接口类型，当前只有 NORMAL，后续还会增加其他类型的 API。       |
| authRequired                             | 否    | String  | 是否需要签名认证，TRUE表示需要，FALSE 表示不需要。默认为 TRUE。如果需要开放在云市场的 API，必须选择 TRUE。 |
| enableCORS                               | 否    | String  | 是否需要开启跨域，TRUE 表示需要，FALSE 表示不需要。默认为 FALSE。    |
| requestConfig.path                       | 是    | String  | API的前端路径，如/path。                         |
| requestConfig.method                     | 是    | String  | API 的前端请求方法，如 GET。                         |
| requestParameters.n.name                 | 否    | String  | API 的前端参数名称。                              |
| requestParameters.n.position             | 否    | String  | API 的前端参数位置。，当前仅支持 PATH、QUERY、HEADER。      |
| requestParameters.n.type                 | 否    | String  | API 的前端参数类型，如 String、Int 等。                 |
| requestParameters.n.defaultValue         | 否    | String  | API 的前端参数默认值。                             |
| requestParameters.n.required             | 否    | Boolean | API 的前端参数是否必填，TRUE：表示必填，FALSE：表示可选。       |
| requestParameters.n.desc                 | 否    | String  | API 的前端参数备注。                              |
| serviceType                              | 是    | String | API 的后端服务类型，现在支持三种：HTTP、MOCK、SCF。          |
| serviceTimeout                           | 是    | Int     | API 的后端服务超时时间，单位是秒。                       |
| serviceConfig.url                        | 否    | String  | API 的后端服务 URL。如果 serviceType 是 HTTP，则此参数必传，例如 http://api.tencentcs.com/apigw。   |
| serviceConfig.path                       | 否    | String  | API 的后端服务路径，如 /path。如果 serviceType 是 HTTP，则此参数必传。前后端的路径可不同。API 网关会对路径做映射。 |
| serviceConfig.method                     | 否    | String  | API 的后端服务请求方法，如 GET。如果 serviceType 是 HTTP，则此参数必传。前后端的方法可不同。API 网关会对方法做映射。 |
| serviceConfig.uniqVpcId                  | 否    | String  | 使用 VPC 时需填写，代表唯一 vpcId。 |
| serviceConfig.product                    | 否    | String  | 和 uniqVpcId 同时使用，目前仅支持 clb 场景，填写“clb”。 |
| serviceParameters.n.name                 | 否    | String  | API 的后端服务参数名称。只有 serviceType 是 HTTP 才会用到此参数。后端服务的参数名称可与前端参数名称不同。API 网关会对参数名称做映射。但后端参数值与前端参数值相同。 |
| serviceParameters.n.position             | 否    | String  | API 的后端服务参数位置，如 head。只有 serviceType 是 HTTP 才会用到此参数。后端服务的位置名称可与前端参数位置不同。API 网关会对参数位置做映射。 |
| serviceParameters.n.relevantRequestParameterName | 否    | String  | API 的后端服务参数对应的前端参数名称。只有 serviceType 是 HTTP 才会用到此参数。 |
| serviceParameters.n.relevantRequestParameterPosition | 否    | String  | API 的后端服务参数对应的前端参数位置。只有 serviceType 是 HTTP 才会用到此参数。 |
| serviceParameters.n.desc                 | 否    | String  | API 的后端服务参数备注。只有 serviceType 是 HTTP 才会用到此参数。  |
| constantParameters.n.name                | 否    | String  | 常量参数名称。只有 serviceType 是 HTTP 才会用到此参数。常量参数为 API 发布者配置在后端的参数，前端调用者不可见。 |
| constantParameters.n.desc                | 否    | String  | 常量参数描述。只有 serviceType 是 HTTP 才会用到此参数。        |
| constantParameters.n.position            | 否    | String  | 常量参数位置。目前仅支持 header 与 query。只有serviceType 是 HTTP 才会用到此参数。 | 
| constantParameters.n.defaultValue        | 否    | String  | 常量参数默认值。只有 serviceType 是 HTTP 才会用到此参数。       |
| serviceMockReturnMessage                 | 否    | String  | API 的后端 Mock 返回信息。如果 serviceType 是 Mock，则此参数必传。 |
| serviceScfFunctionName                   | 否    | String  | API 的后端 SCF 函数名称。如果 serviceType 是 SCF，则此参数必传。  |
| serviceScfFunctionNamespace              | 否    | String  | API 的后端 SCF 函数所属的命名空间。如果 serviceType 是 SCF，则此参数必传。  |
| serviceScfIsIntegratedResponse                   | 否    | String  | 是否启用 SCF 集成响应，TRUE 表示开启，FALSE 表示关闭。只有后端是 SCF 类型此参数才有效，默认为 FALSE。  |
| serviceScfFunctionQualifier                  | 否    | String  | SCF 版本号，默认为 $LATEST。  |
| responseType                             | 否    | String  | 自定义响应配置返回类型，现在只支持 HTML、JSON、TEST、BINARY、XML（此配置仅用于生成 API 文档提示调用者）。 |
| responseSuccessExample                   | 否    | String  | 自定义响应配置成功响应示例（此配置仅用于生成 API 文档提示调用者） 。     |
| responseFailExample                      | 否    | String  | 自定义响应配置失败响应示例（此配置仅用于生成 API 文档提示调用者） 。     |
| responseErrorCodes.n.code                | 否    | Int     | 自定义响应配置原始错误码（此配置仅用于生成 API 文档提示调用者）。        |
| responseErrorCodes.n.convertedCode       | 否    | Int     | 自定义响应配置映射错误码（此配置仅用于生成 API 文档提示调用者）。|
| responseErrorCodes.n.needConvert         | 否    | String  | 自定义响应配置是否开启映射（此配置仅用于生成 API 文档提示调用者）。|
| responseErrorCodes.n.msg                 | 否    | String  | 自定义响应配置错误信息（此配置仅用于生成 API 文档提示调用者）。         |
| responseErrorCodes.n.desc                | 否    | String  | 自定义响应配置错误码备注（此配置仅用于生成 API 文档提示调用者）。        |


## 输出参数
| 参数名称        | 类型        | 描述                                       |
| ----------- | --------- | ---------------------------------------- |
| code        | Int       | 公共错误码，0表示成功，其他值表示失败。详见错误码页面的 [公共错误码](https://cloud.tencent.com/document/product/628/18822)。 |
| codeDesc    | String    | 业务侧错误码。成功时返回 Success，错误时返回具体业务错误原因。       |
| message     | String    | 模块错误信息描述，与接口相关。                          |
| apiId       | String    | API 接口唯一 ID。                               |
| path        | String    | 路径。                                      |
| method      | String    | 请求方法。                                    |
| createdTime | Timestamp | 创建时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。 |


## 示例 

**创建一个后端服务是 HTTP 的 API**
请求示例如下：
```
https://apigateway.api.qcloud.com/v2/index.php?
&<公共请求参数>
&Action=CreateApi
&serviceId=service-XX
&apiDesc=myTestApi
&requestConfig.path=/path
&requestConfig.method=GET
&requestParameters.0.name=age
&requestParameters.0.position=HEADER
&requestParameters.0.type=Int
&requestParameters.0.defaultValue=18
&requestParameters.0.required=REQUIRED
&requestParameters.0.description=年龄
&serviceType=Http
&serviceTimeout=60
&serviceConfig.url=cloud.tencent.com
&serviceConfig.path=/path
&serviceConfig.method=GET
&serviceParameters.0.name=age
&serviceParameters.0.in=HEADER
&serviceParameters.0.relevantRequestParameterName=age
&serviceParameters.0.relevantRequestParameterIn=HEADER
&serviceParameters.0.defaultValue=18
&serviceParameters.0.desc=年龄
&constantParameters.0.name=aa
&constantParameters.0.desc=aa
&constantParameters.0.position=HEADER
&constantParameters.0.defaultValue=aa
```

返回示例如下：
```
{
	"code": "0",
	"message": "",
	"codeDesc": "Success",
	"apiId": "api-XX",
	"path": "/path",
	"method": "GET",
	"createdTime": "2017-08-07T00:00:00Z"
}
```

**创建一个后端服务是 MOCK 的 API**
请求示例如下：
```
https://apigateway.api.qcloud.com/v2/index.php?
&<公共请求参数>
&Action=CreateApi
&serviceId=service-XX
&apiDescription=myTestApi
&requestConfig.path=/path
&requestConfig.method=GET
&requestConfig.protocol=Http
&requestParameters.0.name=age
&requestParameters.0.in=HEADER
&requestParameters.0.type=Int
&requestParameters.0.defaultValue=18
&requestParameters.0.required=REQUIRED
&requestParameters.0.desc=年龄
&serviceType=MOCK
&serviceTimeout=60
&serviceMockReturnMessage=MOCK 的返回信息
```

返回示例如下：
```
{
	"code": "0",
	"message": "",
	"codeDesc": "Success",
	"apiId": "api-XXX",
	"path": "/path",
	"method": "GET",
	"createdTime": "2017-08-07T00:00:00Z"
}
```

**创建一个后端服务是 SCF 的 API**
请求示例如下：
```
https://apigateway.api.qcloud.com/v2/index.php?
&<公共请求参数>
&Action=CreateApi
&serviceId=service-XX
&apiDescription=myTestApi
&requestConfig.path=/path
&requestConfig.method=GET
&requestConfig.protocol=Http
&requestParameters.0.name=age
&requestParameters.0.in=HEADER
&requestParameters.0.type=Int
&requestParameters.0.defaultValue=18
&requestParameters.0.required=REQUIRED
&requestParameters.0.description=年龄
&serviceType=SCF
&serviceTimeout=60
&serviceScfFunctionName=myScfFunction
```

返回示例如下：
```
{
	"code": "0",
	"message": "",
	"codeDesc": "Success",
	"apiId": "api-XXXX",
	"path": "/path",
	"method": "GET",
	"createdTime": "2017-08-07T00:00:00Z"
}
```


