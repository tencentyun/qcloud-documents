
## 接口描述

本接口（DescribeApi）用于查询用户部署于 API 网关的 API 接口的详细信息。​

## 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数可参考 [公共请求参数](/document/api/213/6976)。

| 参数名称      | 是否必选 | 类型     | 描述            |
| --------- | ---- | ------ | ------------- |
| serviceId | 是    | String | API 所在的服务唯一 ID |
| apiId     | 是    | String | API 接口唯一 ID    |

## 输出参数
| 参数名称                     | 类型             | 描述                                       |
| ------------------------ | -------------- | ---------------------------------------- |
| code                     | Int            | 公共错误码，0表示成功，其他值表示失败。详见错误码页面的 <a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="公共错误码">公共错误码</a> |
| codeDesc                 | String         | 业务侧错误码。成功时返回 Success，错误时返回具体业务错误原因       |
| message                  | String         | 模块错误信息描述，与接口相关                          |
| serviceId                | String         | API 所在的服务唯一 ID                            |
| serviceName              | String         | API 所在的服务的名称                             |
| serviceDesc              | String         | API 所在的服务的描述                             |
| apiId                    | String         | API 接口唯一 ID                               |
| apiDesc                  | String         | API 接口的描述                                |
| apiName                  | String         | API 接口的名称                                |
| createdTime              | Timestamp      | 创建时间，按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ |
| modifiedTime             | Timestamp      | 最后修改时间，按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ |
| requestConfig            | Array          | API 的前端配置字典                              |
| requestParameters        | List of Arrays | API 的前端参数数组                              |
| serviceType              | Boolean        | API 的后端服务类型，现在支持三种：HTTP，MOCK，SCF          |
| serviceTimeout           | Int            | API 的后端服务超时时间，单位是 S                       |
| serviceConfig            | Array          | API 的后端配置字典，只有后端服务类型是 HTTP 时才有此出参          |
| serviceParameters        | List of Arrays | API 的后端服务参数数组。只有serviceType是 HTTP 才有此出参    |
| constantParameters       | List of Arrays | API 的后端服务常量参数数组。只有 serviceType 是 HTTP 才会有此参数 |
| serviceMockReturnMessage | String         | API 的后端 Mock 返回信息。只有 serviceType 是 Mock 才有此出参  |
| serviceScfFunctionName   | String         | API 的后端 Scf 函数名称。只有 serviceType是Scf 才有此出参    |
| authRequired             | String         | 是否需要签名认证，TRUE 表示需要，FALSE 表示不需要            |
| enableCORS               | String         | 是否需要开启跨域，TRUE 表示需要，FALSE 表示不需要            |
| responseType             | String         | 自定义响应配置返回类型，现在只支持 HTML、JSON、TEST、BINARY、XML |
| responseSuccessExample   | String         | 自定义响应配置成功响应示例                           |
| responseFailExample      | String         | 自定义响应配置失败响应示例                           |
| responseErrorCodes       | List of Arrays | 自定义响应配置错误码信息                            |

其中前端配置 requestConfig 的构成如下：

| 参数名称   | 类型     | 描述               |
| ------ | ------ | ---------------- |
| path   | String | API 的前端路径，如 /path |
| method | String | API 的前端请求方法，如 GET |

其中前端参数 requestParameters 是由 requestParameter 构成的数组，requestParameter 的构成如下：

| 参数名称         | 类型      | 描述                                       |
| ------------ | ------- | ---------------------------------------- |
| name         | String  | API 的前端参数名称                              |
| in           | String  | API 的前端参数位置，如 head                        |
| type         | String  | API 的前端参数类型，如 String                      |
| defaultValue | String  | API 的前端参数默认值                             |
| required     | Boolean | API 的前端参数是否必填，REQUIRED：表示必填，OPTIONAL：表示可选 |
| desc         | String  | API 的前端参数备注                              |

其中，当 API 的后端服务类型 serviceType 是 HTTP 时，后端配置 serviceConfig的构成如下：

| 参数名称   | 类型     | 描述                 |
| ------ | ------ | ------------------ |
| url    | String | API 的后端服务 URL       |
| path   | String | API 的后端服务路径，如 /path |
| method | String | API 的后端服务请求方法，如 GET |

后端参数 serviceParameters 是由 serviceParameter 构成的数组，serviceParameter 的构成如下：

| 参数名称                         | 类型     | 描述                         |
| ---------------------------- | ------ | -------------------------- |
| name                         | String | API 的后端服务参数名称              |
| position                     | String | API 的后端服务参数位置，如 head        |
| relevantRequestParameterName | String | API 的后端服务参数对应的前端参数名称       |
| relevantRequestParameterIn   | String | API 的后端服务参数对应的前端参数位置，如 head |
| desc                         | String | API 的后端服务参数备注              |

常量参数 constantParameters 是由 constantParameter 构成的数组，constantParameter 的构成如下

| 参数名称         | 类型     | 描述       |
| ------------ | ------ | -------- |
| name         | String | 常量参数名称  |
| desc         | String | 常量参数描述  |
| position     | String | 常量参数位置  |
| defaultValue | String | 常量参数默认值 |


## 示例 

查询一个后端是 HTTP 服务的 API 接口的详细信息：

请求示例如下：
```
https://apigateway.api.qcloud.com/v2/index.php?
&<公共请求参数>
&Action=DescribeApi
&serviceId=service-XX
&apiId=api-XX

```
返回示例如下：
```
{
	"code": "0",
	"message": "",
	"codeDesc": "Success",
	"serviceId": "service-XX",
	"serviceName": "test",
	"serviceDesc": "testDesc",
	"apiId": "api - XX",
	"apiName": "apiXXXX",
	"apiType": "NORMAL",
	"apiDesc": "myHTTPTestApi",
	"createdTime": "2017-08-07T00:00:00Z",
	"modifiedTime": "2017-08-07T00:00:00Z",
	"requestConfig": {
		"path": "/path",
		"method": "GET"
	},
	"requestParameters": [{
		"name": "age",
		"in": "HEADER",
		"type": "Int",
		"defaultValue": 18,
		"required": "True",
		"desc": "年龄 "
	}],
	"serviceType": "HTTP",
	"serviceTimeout": 60,
	"serviceConfig": {
		"url": "cloud.tencent.com",
		"path": "/path",
		"method": "GET"
	},
	"serviceParameters": [{
		"name": "age",
		"in": "HEADER",
		"relevantRequestParameterName": "age",
		"relevantRequestParameterIn": "HEADER",
		"defaultValue": 18,
		"desc": "年龄"
	}]
}
```

查询一个后端是 MOCK 的 API 接口的详细信息：

请求示例如下：
```
https://apigateway.api.qcloud.com/v2/index.php?
&<公共请求参数>
&Action=DescribeApi
&serviceId=service-XX
&apiId=api-XXX

```
返回示例如下：
```
{
	"code": "0",
	"message": "",
	"codeDesc": "Success",
	"serviceId": "service-XX",
	"serviceName": "test",
	"serviceDesc": "testDescription",
	"apiId": "api - XXX",
	"apiName": "apiXXXX",
	"apiType": "NORMAL",
	"apiDesc": "myMockTestApi",
	"createdTime": "2017-08-07T00:00:00Z",
	"modifiedTime": "2017-08-07T00:00:00Z",
	"requestConfig": {
		"path": "/path",
		"method": "GET"
	},
	"requestParameters": [{
		"name": "age",
		"in": "HEADER",
		"type": "Int",
		"defaultValue": 18,
		"required": "REQUIRED",
		"desc": "年龄"
	}],
	"serviceType": "MOCK",
	"serviceTimeout": 60,
	"serviceMockReturnMessage": "MOCK的返回信息"
}
```

查询一个后端是 SCF 的 API 接口的详细信息：

请求示例如下：
```
https://apigateway.api.qcloud.com/v2/index.php?
&<公共请求参数>
&Action=DescribeApi
&serviceId=service-XX
&apiId=api-XXXX

```
返回示例如下：
```
{
	"code": "0",
	"message": "",
	"codeDesc": "Success",
	"serviceId": "service-XX",
	"serviceName": "test",
	"serviceDesc": "testDescription",
	"apiId": "api-XXXX",
	"apiName": "apiXXXX",
	"apiType": "NORMAL",
	"apiDesc": "mySCFTestApi",
	"createdTime": "2017-08-07T00:00:00Z",
	"modifiedTime": "2017-08-07T00:00:00Z",
	"requestConfig": {
		"path": "/path",
		"method": "GET"
	},
	"requestParameters": [{
		"name": "age",
		"in": "HEADER",
		"type": "Int",
		"defaultValue": 18,
		"required": "REQUIRED",
		"desc": "年龄 "
	}],
	"serviceType": "SCF",
	"serviceTimeout": 60,
	"serviceScfFunctionName": "myScfFunction"
}
```
