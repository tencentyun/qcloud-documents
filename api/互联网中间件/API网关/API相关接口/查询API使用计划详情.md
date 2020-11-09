## 接口描述

本接口（DescribeApiUsagePlan）用于查询服务中 API 使用计划详情。
服务若需要鉴权限流生效，则需要绑定使用计划到此服务中，本接口用于查询绑定到一个服务及其中 API 的所有使用计划。


## 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数可参考 [公共请求参数](https://cloud.tencent.com/document/product/628/18814)。

| 参数名称              | 是否必选 | 类型     | 描述                  |
| ----------------- | ---- | ------ | ------------------- |
| serviceId         | 是    | String | 待查询的服务唯一 ID。         |
| offset            | 否    | Int    | 偏移量，默认为 0。           |
| limit             | 否    | Int    | 返回数量，默认为 20，最大值为 100。 |
| searchEnvironment | 否    | String | 根据使用计划环境名称模精确索。     |
| apiIds.n            | 否    | List of String | API 唯一 ID 数组，如果不传，返回当前服务下所有 API 的使用计划信息。|

## 输出参数
| 参数名称          | 类型             | 描述                                       |
| ------------- | -------------- | ---------------------------------------- |
| code          | Int            | 公共错误码, 0 表示成功，其他值表示失败。详见错误码页面的 [公共错误码](https://cloud.tencent.com/document/product/628/18822)。 |
| codeDesc      | String         | 业务侧错误码。成功时返回 Success，错误时返回具体业务错误原因。       |
| message       | String         | 模块错误信息描述，与接口相关。                          |
| totalCount    | Int            | 服务上绑定的使用计划总数。                            |
| usagePlanList | List of Arrays | 服务上绑定的使用计划列表。                            |

usagePlanList 是绑定到该服务上面的使用计划列表，它是由 usagePlanAttribute 组成的数组，usagePlanAttribute 构成如下：

| 参数名称          | 类型        | 描述          |
| ------------- | --------- | ----------- |
| usagePlanId   | String    | 使用计划的唯一 ID。   |
| usagePlanName | String    | 使用计划的名称。     |
| usagePlanDesc | String    | 使用计划的描述。    |
| environment   | String    | 使用计划绑定的服务环境。 |
| createdTime   | Timestamp | 使用计划创建时间。    |
| modifiedTime  | Timestamp | 使用计划最后修改时间。  |
| inUseRequestNum | Int    | 已经使用的配额。|
| maxRequestNum   | Int    | 请求配额总量，-1 表示没有限制。|
| maxRequestNumPreSec | Int | 请求 QPS 上限，-1 表示没有限制。|
| apiId 		| String 	| API 唯一 ID。|
| path			| String	| 请求 path。|
| method		| String    | 请求方式。|
| apiName		| String	| API 名称。|
| serviceId		| String	| 服务唯一 ID。|
| serviceName	| String	| 服务名称。|

## 示例 
```
https://apigateway.api.qcloud.com/v2/index.php?
&<公共请求参数>
&Action=DescribeApiUsagePlan
&serviceId=service-XX
```
返回示例如下：
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",      
	"totalCount":2,
	"usagePlanList":[
		{
			"maxRequestNumPreSec": 2000,
			"usagePlanId": "usagePlan-0var1p8v",
			"modifiedTime": "2018-07-31 20:26:28",
			"usagePlanDesc": "test",
			"apiId": "api-2yuua008",
			"environment": "release",
			"serviceId": "service-XX",
			"apiName": "sjiofjsdioj",
			"createdTime": "2018-07-20 14:09:47",
			"path": "/fsodjfsd",
			"usagePlanName": "test",
			"method": "GET",
			"serviceName": "test"
		}
	]
}
```




