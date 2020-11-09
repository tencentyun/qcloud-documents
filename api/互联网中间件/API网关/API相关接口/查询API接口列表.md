## 接口描述
本接口（DescribeApisStatus）用于查看一个服务下的某个 API 或所有 API 列表及其相关信息。

## 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数可参考 [公共请求参数](https://cloud.tencent.com/document/product/628/18814)。

| 参数名称       | 是否必选 | 类型     | 描述                                       |
| ---------- | ---- | ------ | ---------------------------------------- |
| serviceId  | 是    | String | API 所在的服务唯一 ID。                            |
| apiIds.n   | 否    | String | API 接口唯一 ID 数组。                             |
| offset     | 否    | Int    | 偏移量，默认为 0。                                |
| limit      | 否    | Int    | 返回数量，默认为 20，最大值为 100。                      |
| orderby    | 否    | String | 根据哪个字段排序。                                |
| order      | 否    | String | 排序方式。                                    |
| searchName | 否    | String | 按照 API 路径名字模糊搜索。                           |
| searchId   | 否    | String | 按照 API 唯一 ID 精确搜索。                           |


## 输出参数
| 参数名称           | 类型            | 描述                                       |
| -------------- | ------------- | ---------------------------------------- |
| code           | Int           | 公共错误码, 0 表示成功，其他值表示失败。详见错误码页面的  [公共错误码](https://cloud.tencent.com/document/product/628/18822)。 |
| codeDesc       | String        | 业务侧错误码。成功时返回 Success，错误时返回具体业务错误原因。       |
| message        | String        | 模块错误信息描述，与接口相关。                          |
| serviceId      | String        | API 所在的服务唯一 ID。                            |
| totalCount     | Int           | 符合条件的 API 接口数量。                            |
| apiIdStatusSet | List of Array | API 接口列表。                                 |

其中，apiIdStatusSet 是 apiIdStatus 构成的数组，apiIdStatus 的构成如下：

| 参数名称         | 类型        | 描述                                       |
| ------------ | --------- | ---------------------------------------- |
| apiId        | String    | API 接口唯一 ID。                               |
| apiDesc      | String    | 用户自定义的 API 接口描述。                           |
| apiName      | String    | API 接口的名称。                                |
| apiType      | String    | API 接口的类型，当前只有 NORMAL，后续还会增加其他类型的 API。      |
| path         | String    | API 请求 path。                               |
| method       | String    | API 请求方式。                                 |
| createdTime  | Timestamp | 创建时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。 |
| modifiedTime | Timestamp | 最后修改时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。 |
| authRequired | String    | 是否需要签名认证，TRUE 表示需要，FALSE 表示不需要。            |

## 示例 

查询一个后端是 HTTP 服务的 API 接口的详细信息：

请求示例如下：
```
https://apigateway.api.qcloud.com/v2/index.php?
&<公共请求参数>
&Action=DescribeApisStatus
&serviceId=service-XX
&apiIds.0=api-XX
&apiIds.1=api-XXX
&offet=0
&limit=2
&orderby=createdTime
&order=desc
&searchKey=aa
```
返回示例如下：
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success", 
    "serviceId":"service-XX",
    "totalCount":2,
	"apiIdStatusSet":[
		{
			"apiId":"api-XX",
			"apiName":"apiXXXX",
			"apiType":"NORMAL",
			"apiDesc":"apiDescription1",
			"path":"path1",
			"method":"http",
			"serviceId":"serviceId-XXX",
			"createdTime":"2017-08-07T00:00:00Z",
			"modifiedTime":"2017-08-07T00:00:00Z",
			"authRequired":"TRUE"
		},
		{
			"apiId":"api-XXX",
			"apiName":"apiXXXX",
			"apiType":"NORMAL",
			"apiDesc":"apiDescription2",
			"path":"path2",
			"method":"https",
			"serviceId":"serviceId-XXXX",
			"createdTime":"2017-08-07T00:10:00Z",
			"modifiedTime":"2017-08-07T00:10:00Z",
			"authRequired":"TRUE"
		}
	]
}
```
