
## 接口描述

本接口（RunApi）用于调试 API 接口。用户在配置完成后可调用此接口进行调试，无需等到发布后走正式的调用流程。


## 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数可参考 [公共请求参数](/document/api/213/6976)。

| 参数名称          | 是否必选 | 类型     | 描述                                       |
| ------------- | ---- | ------ | ---------------------------------------- |
| serviceId     | 是    | String | API 所在的服务唯一 ID。                            |
| apiId         | 是    | String | API 唯一 ID。                                 |
| requestHeader | 否    | String | API 的前端请求头部，是 json_dump 后的数据              |
| requestQuery  | 否    | String | API 的前端请求 Query，是 json_dump 后的数据           |
| requestPath   | 否    | String | API 的请求 Path，是 json_dump 后的数据              |
| requestMethod | 否    | String | API 的请求方法。只支持 HEAD、GET、POST、PUT、PATCH 和 DELETE |
| requestBody   | 否    | String | API 的请求 Body                              |
| requestBodyDict| 否 | Dict | API 的请求 Body，当 API 有设置 Body 类型入参时，用数组格式传入|
| contentType| 否 | String | 调试请求的内容类型。当前只支持 application/json 和 application/x-www-form-urlencoded，不传的话，默认为 application/x-www-form-urlencoded|

## 输出参数
| 参数名称         | 类型     | 描述                                       |
| ------------ | ------ | ---------------------------------------- |
| code         | Int    | 公共错误码, 0 表示成功，其他值表示失败。详见错误码页面的 <a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="公共错误码">公共错误码</a> |
| codeDesc     | String | 业务侧错误码。成功时返回 Success，错误时返回具体业务错误原因       |
| message      | String | 模块错误信息描述，与接口相关                         |
| returnHeader | String | API 接口的响应头部                              |
| returnBody   | String | API 接口的响应包体                              |
| returnCode   | Int    | API 接口的响应码                               |
| delay        | Int    | API 接口的响应延迟，单位 ms                         |


## 示例 

修改一个后端服务是 HTTP 的 API：
请求示例如下：
```
https://apigateway.api.qcloud.com/v2/index.php?
&<公共请求参数>
&Action=RunApi
&serviceId=service-XX
&apiId=api-XX
&requestHeader={"headerKey1":"headerValue1","headerKey2":"headerValue2"}
&requestQuery={"queryKey1":"queryValue1","queryKey2":"queryValue2"}
&requestPath={"pathKey1":"pathValue1","pathKey2":"pathValue2"}
&requestMethod=GET
&requestBody=abalabala
&contentType=application/json
```
返回示例如下：
```
{
	"code": "0",
	"message": "",
	"codeDesc": "Success",
	"returnHeader": "abcd",
	"returnBody": "efgh",
	"returnCode": 200,
	"delay": 300
}
```
