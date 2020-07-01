
## 接口描述

本接口（ModifyApi）用于修改 API 接口，可调用此接口对已经配置的 API 接口进行编辑修改。修改后的 API 需要重新发布 API 所在的服务到对应环境方能生效。

## 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数可参考 [公共请求参数](https://cloud.tencent.com/document/product/628/18814)。

| 参数名称                                     | 是否必选 | 类型      | 描述                                       |
| ---------------------------------------- | ---- | ------- | ---------------------------------------- |
| serviceId                                | 是    | String  | API 所在的服务唯一 ID。                            |
| apiId                                    | 是    | String  | API 接口唯一 ID。                               |
| apiName                                  | 否    | String  | 用户自定义的 API 名称。                             |
| authRequired                             | 否    | String  | 是否需要签名认证，TRUE 表示需要，FALSE 表示不需要。            |
| enableCORS                               | 否    | String  | 是否需要开启跨域，TRUE 表示需要，FALSE 表示不需要。            |
| apiDesc                                  | 否    | String  | 用户自定义的 API 接口描述。                           |
| requestConfig.path                       | 否    | String  | API 的前端路径，如 /path。                         |
| requestConfig.method                     | 否    | String  | API 的前端请求方法，如 GET。                         |
| requestConfig.protocol                   | 否    | String  | API 的前端请求类型，如 HTTP 或 HTTPS 或者 HTTP 和 HTTPS。      |
| requestParameters.n.name                 | 否    | String  | API 的前端参数名称。                              |
| requestParameters.n.position             | 否    | String  | API 的前端参数位置，如 head。目前支持 head、qurey、path     |
| requestParameters.n.type                 | 否    | String  | API 的前端参数类型，如 String、int。                  |
| requestParameters.n.defaultValue         | 否    | String  | API 的前端参数默认值。                             |
| requestParameters.n.required             | 否    | Boolean | API 的前端参数是否必填，TRUE：表示必填，FALSE：表示可选。       |
| requestParameters.n.desc                 | 否    | String  | API 的前端参数备注。                              |
| serviceType                              | 否    | String | API 的后端服务类型，现在支持三种：HTTP、MOCK 和 SCF。         |
| serviceTimeout                           | 否    | Int     | API 的后端服务超时时间，单位是秒。                       |
| serviceConfig.url                        | 否    | String  | API 的后端服务url。如果serviceType是HTTP，则此参数必传。   |
| serviceConfig.path                       | 否    | String  | API 的后端服务路径，如 /path。如果 serviceType 是 HTTP，则此参数必传。前后端路径可不同。 | 
| serviceConfig.method                     | 否    | String  | API的后端服务请求方法，如 GET。如果 serviceType 是 HTTP，则此参数必传。前后端方法可不同 |
| serviceParameters.n.name                 | 否    | String  | API的后端服务参数名称。只有serviceType是HTTP才会用到此参数。前后端参数名称可不同。 |
| serviceParameters.n.position             | 否    | String  | API 的后端服务参数位置，如 head。只有 serviceType 是 HTTP 才会用到此参数。前后端参数位置可配置不同。 |
| serviceParameters.n.relevantRequestParameterName | 否    | String  | API 的后端服务参数对应的前端参数名称。只有 serviceType 是 HTTP 才会用到此参数。 |
| serviceParameters.n.relevantRequestParameterPosition | 否    | String  | API 的后端服务参数对应的前端参数位置，如 head。只有 serviceType 是 HTTP 才会用到此参数。 |
| serviceParameters.n.desc                 | 否    | String  | API 的后端服务参数备注。只有 serviceType 是 HTTP 才会用到此参数。  |
| constantParameters.n.name                | 否    | String  | 常量参数名称。只有 serviceType 是 HTTP 才会用到此参数。        |
| constantParameters.n.desc                | 否    | String  | 常量参数描述。只有 serviceType 是 HTTP 才会用到此参数。        |
| constantParameters.n.position            | 否    | String  | 常量参数位置。只有 serviceType 是 HTTP 才会用到此参数。        |
| constantParameters.n.defaultValue        | 否    | String  | 常量参数默认值。只有 serviceType 是 HTTP 才会用到此参数。       |
| serviceMockReturnMessage                 | 否    | String  | API 的后端 Mock 返回信息。如果 serviceType 是 Mock，则此参数必传。 |
| serviceScfFunctionName                   | 否    | String  | API 的后端 SCF 函数名称。如果 serviceType 是 SCF，则此参数必传。  |
| serviceScfFunctionNamespace              | 否    | String  | API 的后端 SCF 函数所属的命名空间。如果 serviceType 是 SCF，则此参数必传。  |
| responseType                             | 否    | String  | 自定义响应配置返回类型，现在只支持 HTML、JSON、TEST、BINARY、XML。 |
| responseSuccessExample                   | 否    | String  | 自定义响应配置成功响应示例。                           |
| responseFailExample                      | 否    | String  | 自定义响应配置失败响应示例。                           |
| responseErrorCodes.n.code                | 否    | String  | 自定义响应配置错误码。                              |
| responseErrorCodes.n.msg                 | 否    | String  | 自定义响应配置错误信息。                             |
| responseErrorCodes.n.desc                | 否    | String  | 自定义响应配置错误码备注。                            |
| isDeleteResponseErrorCodes               | 否    | String  | 是否删除自定义响应配置错误码，如果不传或者传 FALSE，不删除，当传 TRUE 时，则删除此 API 所有自定义响应配置错误码。 |

## 输出参数
| 参数名称     | 类型     | 描述                                       |
| -------- | ------ | ---------------------------------------- |
| code     | Int    | 公共错误码, 0 表示成功，其他值表示失败。详见错误码页面的 [公共错误码](https://cloud.tencent.com/document/product/628/18822)。 |
| codeDesc | String | 业务侧错误码。成功时返回 Success，错误时返回具体业务错误原因。       |
| message  | String | 模块错误信息描述，与接口相关。                          |


## 示例 

修改一个后端服务是 HTTP 的 API：
请求示例如下：
```
https://apigateway.api.qcloud.com/v2/index.php?
&<公共请求参数>
&Action=ModifyApi
&serviceId=service-XX
&apiId=api-XX
&apiDesc=myTestApi
&requestConfig.path=/path
&requestConfig.method=GET
&requestConfig.protocol=Http
&requestParameters.0.name=age
&requestParameters.0.location=head
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
&serviceParameters.0.location=head
&serviceParameters.0.relevantRequestParameterName=age
&serviceParameters.0.relevantRequestParameterIn=head
&serviceParameters.0.defaultValue=18
&serviceParameters.0.description=年龄
```
返回示例如下：
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success"
}
```

修改一个后端服务是 MOCK 的 API：
请求示例如下：
```
https://apigateway.api.qcloud.com/v2/index.php?
&<公共请求参数>
&Action=ModifyApi
&serviceId=service-XX
&apiId=api-XX
&apiDescription=myTestApi
&requestConfig.path=/path
&requestConfig.method=GET
&requestConfig.protocol=Http
&requestParameters.0.name=age
&requestParameters.0.location=head
&requestParameters.0.type=Int
&requestParameters.0.defaultValue=18
&requestParameters.0.required=REQUIRED
&requestParameters.0.description=年龄
&serviceType=MOCK
&serviceTimeout=60
&serviceMockReturnMessage=MOCK 的返回信息
```
返回示例如下：
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success"    
}
```

修改一个后端服务是 SCF 的 API：
请求示例如下：
```
https://apigateway.api.qcloud.com/v2/index.php?
&<公共请求参数>
&Action=ModifyApi
&serviceId=service-XX
&apiId=api-XX
&apiDescription=myTestApi
&requestConfig.path=/path
&requestConfig.method=GET
&requestConfig.protocol=Http
&requestParameters.0.name=age
&requestParameters.0.location=head
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
    "code":"0",
    "message":"",
    "codeDesc":"Success"   
}
```
