**简介**：数据源管理 API
**HOST**：`https://{envId}.ap-shanghai.tcb-api.tencentcloudapi.com/weda`
<dx-alert infotype="explain" title="">
环境 ID（envId）可前往 [资源管理](https://console.cloud.tencent.com/lowcode/resource/index) 页面获取。
</dx-alert>

envType：正式环境传 prod，体验环境传 pre。
datasourceName：数据源名称可以在 [数据模型](https://console.cloud.tencent.com/lowcode/datasource/model) 中，对应的数据表-基础信息-标识字段查到。


## 创建数据源记录
- **接口地址**：`/odata/v1/{envType}/{datasourceName}`
- **请求方式**：`POST`
- **请求数据类型**：`application/json`
- **响应数据类型**：`*/*`

#### 请求示例
```javascript
{
    "name": "李四",
    "course": "体育",
    "score": 89,
    "semester": "第二学期"
}
```
#### 请求参数

| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|X-Request-Id|请求 requestId|header|true|string|-|
|envType|环境类型，pre 预览环境，prod 正式环境|path|true|string|-|
|datasourceName|数据源标识，示例值（student_bky05o0）|path|true|-|-|
|创建记录对象|字段标识和字段值对象|body|true|创建记录对象|字段标识：字段值|

#### 响应状态

| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|201|创建成功|-|


#### 响应参数

| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|创建记录对象|字段标识和字段值对象|创建记录对象|字段标识：字段值|
|_id|记录 id|string|-|


#### 响应示例
```javascript
{
    "@odata.context": "$metadata#student_bky05o0",
    "_id": "5b049cc8621c7f040ea751850b63e442",
    "createdAt": 1646034692306,
    "updatedAt": 1646034692306,
    "owner": "1463080581028851713",
    "createBy": "1463080581028851713",
    "updateBy": "1463080581028851713",
    "_departmentList": "[]",
    "name": "李四",
    "course": "体育",
    "score": 89.0,
    "semester": "第二学期"
}
```


## 更新数据源记录
- **接口地址**：`/odata/v1/{envType}/{datasourceName}('{recordId}')`
- **请求方式**：`PATCH`
- **请求数据类型**：`application/json`
- **响应数据类型**：`*/*`

#### 请求示例
```javascript
{
    "name": "李四",
    "course": "体育",
    "score": 89,
    "semester": "第二学期"
}
```


#### 请求参数

| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|X-Request-Id |  请求 requestId   |   header  |  true  |   string   |  -  |
|envType   |   环境类型，pre 预览环境，prod 正式环境    |   path   |    true   |  string   |  -   |
|datasourceName   |   数据源标识     |    path      |    true     |  -     |    -   |
|recordId   |   数据标识 id   |   path   |   true    |  -      |       -   |
|更新记录对象   |    字段标识和字段值对象   |body|true|更新记录对象|字段标识：字段值|


#### 响应状态

| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|204|更新成功|    -   |


#### 响应参数
暂无。




## 查询数据源记录

- **接口地址**：`/odata/v1/{envType}/{datasourceName}('{recordId}')`
- **请求方式**：`GET`
- **请求数据类型**：`application/json`
- **响应数据类型**：`*/*`

#### 请求参数

| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|X-Request-Id|请求 requestId|header|true|string|-|
|envType|环境类型，pre 预览环境，prod 正式环境|path|true|string|-|
|datasourceName|数据源标识|path|true|-|-|
|recordId|数据标识 id|path|true|-|-|


#### 响应状态

| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|查询成功|-|


#### 响应参数

| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|记录对象|字段标识和字段值对象|记录对象|字段标识：字段值|
|_id|记录 id|string|-|


#### 响应示例
```javascript
{
    "@odata.context": "$metadata#student_bky05o0",
    "_id": "5b049cc8621c7f040ea751850b63e442",
    "createdAt": 1646034692306,
    "updatedAt": 1646034692306,
    "owner": "1463080581028851713",
    "createBy": "1463080581028851713",
    "updateBy": "1463080581028851713",
    "_departmentList": "[]",
    "name": "李四",
    "course": "体育",
    "score": 89.0,
    "semester": "第二学期"
}
```


## 根据 filter 查询数据源记录

- **接口地址**：`/odata/v1/{envType}/{datasourceName}`
- **请求方式**：`GET`
- **请求数据类型**：`application/json`
- **响应数据类型**：`*/*`

#### 请求参数


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 |
| -------- | -------- | ----- | -------- | -------- |
|X-Request-Id|请求 requestId|header|true|string|
|envType|环境类型，pre 预览环境，prod 正式环境|path|true|string|
|datasourceName|数据源标识|path|true|string|
|$filter|查询条件，$filter 中判断条件包含：<br>eq：等于<br>gt：大于<br>lt：小于<br>ne：不等于<br>contains()：包含<br>其中 contains() 用法为 $filter=contains(name, '张')<br>**注意：**如果 or 和 and 并用，优先级高的需要加括号，用法为(age gt 1 and age lt 10) or age eq 20 |query|false|string|
|$skip|跳过 N 条记录|query|false|integer|
|$top|查询 N 条记录|query|false|integer|
|$orderby|排序字段，$orderby 排序支持：desc 和 asc 模式，例如需要按某字段顺序排列 $orderby=age asc|query|false|string|
|$count|获取数据总数|query|false|boolean|


#### 响应状态


| 状态码 | 说明 | 
| -------- | -------- | 
|200|查询成功|

#### 响应参数

| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|value|字段标识和字段值对象列表|array|记录列表|


#### 响应示例
```javascript
{
    "@odata.context": "$metadata#student_bky05o0",
    "@odata.count": 1,
    "value": [
        {
            "_id": "287a53aa61af01df00dc957a79c1ab3b",
            "createdAt": 1638859231940,
            "updatedAt": 1638859231940,
            "owner": "1468105174530121729",
            "createBy": "1468105174530121729",
            "updateBy": "1468105174530121729",
            "_departmentList": "[]",
            "name": "二蛋",
            "course": "语文",
            "score": 77,
            "semester": "第一学期"
          }
    ]
}

```


## 删除数据源记录

- **接口地址**：`/odata/v1/{envType}/{datasourceName}('{recordId}')`
- **请求方式**：`DELETE`
- **请求数据类型**：`application/json`
- **响应数据类型**：`*/*`

#### 请求参数


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 |
| -------- | -------- | ----- | -------- | -------- |
|X-Request-Id|请求 requestId|header|true|string|
|envType|环境类型，pre 预览环境，prod 正式环境|path|true|string|
|datasourceName|数据源标识|path|true|-|
|recordId|数据标识 id|path|true|-|


#### 响应状态

| 状态码 | 说明 |
| -------- | -------- | 
|204|删除成功|


#### 响应参数
暂无。


## 批量创建数据源记录


- **接口地址**：`/odata/v1/batch/{envType}/{datasourceName}`
- **请求方式**：`POST`
- **请求数据类型**：`application/json`
- **响应数据类型**：`*/*`

#### 请求示例

```javascript
{
    "value": [
        {
            "name": "二蛋",
            "course": "语文",
            "score": 77,
            "semester": "第一学期"
        }
    ]
}
```


#### 请求参数


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | 
| -------- | -------- | ----- | -------- | -------- | 
|X-Request-Id|请求 requestId|header|true|string|
|envType|环境类型，pre 预览环境，prod 正式环境|path|true|string|
|datasourceName|数据源标识|path|true||
|批量创建对象||body|true|
|value|字段标识和字段值对象列表||true|记录列表|


#### 响应状态


| 状态码 | 说明 | 
| -------- | -------- | 
|201|创建成功|


#### 响应参数

| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|value|字段标识和字段值对象列表|array|记录列表|



#### 响应示例
```javascript
{
    "@odata.context": "$metadata#student_bky05o0",
    "value": [
        {
            "_id": "287a53aa61af01df00dc957a79c1ab3b",
            "createdAt": 1638859231940,
            "updatedAt": 1638859231940,
            "owner": "1468105174530121729",
            "createBy": "1468105174530121729",
            "updateBy": "1468105174530121729",
            "_departmentList": "[]",
            "name": "二蛋",
            "course": "语文",
            "score": 77,
            "semester": "第一学期"
          }
    ]
}
```


## 根据 ID 批量更新数据源记录


- **接口地址**：`/odata/v1/batch/{envType}/{datasourceName}('{recordIds}')`
- **请求方式**：`PATCH`
- **请求数据类型**：`application/json`
- **响应数据类型**：`*/*`

#### 请求示例
```javascript
{  
    "name":"二蛋",  
    "course":"语文",  
    "score":77,  
    "semester":"第一学期"  
}
```


#### 请求参数

| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | 
| -------- | -------- | ----- | -------- | -------- | 
|X-Request-Id|请求 requestId|header|true|string|
|envType|环境类型，pre 预览环境，prod 正式环境|path|true|string|
|datasourceName|数据源标识|path|true||
|recordIds|数据标识 id|path|true||
|批量更新对象||body|true|


#### 响应状态


| 状态码 | 说明 |
| -------- | -------- | 
|200|更新成功|


#### 响应参数

| 参数名称 | 参数说明 | 类型 |
| -------- | -------- | ----- |
|updateCount|修改记录数|int|



#### 响应示例
```javascript
{

    "updateCount": N

}
```


## 根据ID批量查询数据源记录


**接口地址**:`/odata/v1/batch/{envType}/{datasourceName}('{recordIds}')`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|X-Request-Id|请求requestId|header|true|string||
|envType|环境类型,pre预览环境，prod正式环境|path|true|string||
|datasourceName|数据源标识|path|true|||
|recordIds|数据标识id|path|true|||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|查询成功||

**响应参数**:

| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|value|字段标识和字段值对象列表|array|记录列表|



**响应示例**:
```javascript
{
    "@odata.context": "$metadata#student_bky05o0",
    "value": [
        {
            "_id": "287a53aa61af01df00dc957a79c1ab3b",
            "createdAt": 1638859231940,
            "updatedAt": 1638859231940,
            "owner": "1468105174530121729",
            "createBy": "1468105174530121729",
            "updateBy": "1468105174530121729",
            "_departmentList": "[]",
            "name": "二蛋",
            "course": "语文",
            "score": 77,
            "semester": "第一学期"
          }
    ]
}
```


## 根据Filter批量查询数据源记录


**接口地址**:`/odata/v1/batch/{envType}/{datasourceName}`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|X-Request-Id|请求requestId|header|true|string||
|envType|环境类型,pre预览环境，prod正式环境|path|true|string||
|datasourceName|数据源标识|path|true|||
|$filter|查询条件,$filter中判断条件包含:eq：等于,gt：大于,lt：小于,ne：不等于,contains()：包含， 其中 contains() 用法为 $filter=contains(name, '张'),注意：如果 or 和 and 并用，优先级高的需要加括号，用法为(age gt 1 and age lt 10) or age eq 20 |query|false|||
|$skip|跳过N条记录|query|false|||
|$top|查询N条记录|query|false|||
|$orderby|排序字段,$orderby 排序支持:desc和asc模式, 例如需要按某字段顺序排列$orderby=age asc|query|false|||
|$count|获取数据总数|query|false|||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|查询成功||


**响应参数**:

| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|value|字段标识和字段值对象列表|array|记录列表|



**响应示例**:
```javascript
{
    "@odata.context": "$metadata#student_bky05o0",
    "@odata.count": 2,
    "value": [
        {
            "_id": "287a53aa61af01df00dc957a79c1ab3b",
            "createdAt": 1638859231940,
            "updatedAt": 1638859231940,
            "owner": "1468105174530121729",
            "createBy": "1468105174530121729",
            "updateBy": "1468105174530121729",
            "_departmentList": "[]",
            "name": "二蛋",
            "course": "语文",
            "score": 77,
            "semester": "第一学期"
          }
    ]
}
```


## 根据ID批量删除数据源记录


**接口地址**:`/odata/v1/batch/{envType}/{datasourceName}('{recordIds}')`


**请求方式**:`DELETE`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|X-Request-Id|请求requestId|header|true|string||
|envType|环境类型,pre预览环境，prod正式环境|path|true|string||
|datasourceName|数据源标识|path|true|||
|recordIds|数据标识id|path|true|||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|删除成功||


**响应参数**:

| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|deleteCount|删除记录数|integer||


**响应示例**:
```javascript
{
    "deleteCount": 3
}
```


## 查询环境下所有数据源Schema


**接口地址**:`/model/v1/getSchemaList`


**请求方式**:`GET`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|X-Request-Id|请求requestId|header|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|查询成功|公共出参对象|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|Response||公共出参对象，data类型为QueryDataSourceSchemaResultListResponse|公共出参对象，data类型为QueryDataSourceSchemaResultListResponse|
|&emsp;&emsp;RequestId|requestId|string||
|&emsp;&emsp;Error|错误信息|错误信息|错误信息|
|&emsp;&emsp;&emsp;&emsp;Code|错误码|string||
|&emsp;&emsp;&emsp;&emsp;Message|错误消息提示|string||
|&emsp;&emsp;Data||QueryDataSourceSchemaResultListResponse|QueryDataSourceSchemaResultListResponse|
|&emsp;&emsp;&emsp;&emsp;QueryDataSourceSchemaResultList|数据模型Schema数组|array|QueryDataSourceSchemaResult|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;Id|数据模型ID|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;Name|数据模型标识|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;Title|数据模型标题|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;Schema|数据模型Schema|string||
|&emsp;&emsp;&emsp;&emsp;RequestId|请求ID|string||


**响应示例**:
```javascript
{  
    "Response":{  
        "Data":{  
            "QueryDataSourceSchemaResultList":[  
                {  
                    "Id":"data-1P1UtRsJ2",  
                    "Name":"sys_user",  
                    "Title":"用户",  
                    "Schema":"model schema"  
                }  
            ],  
            "RequestId":"reqid"  
        }  
    }  
}
```


## 查询数据源Schema


**接口地址**:`/model/v1/getSchemaList/{dataSourceName}`


**请求方式**:`GET`


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|X-Request-Id|请求requestId|header|true|string||
|dataSourceName||path|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|查询成功|公共出参对象|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|Response||公共出参对象，data类型为QueryDataSourceSchemaResultListResponse|公共出参对象，data类型为QueryDataSourceSchemaResultListResponse|
|&emsp;&emsp;RequestId|requestId|string||
|&emsp;&emsp;Error|错误信息|错误信息|错误信息|
|&emsp;&emsp;&emsp;&emsp;Code|错误码|string||
|&emsp;&emsp;&emsp;&emsp;Message|错误消息提示|string||
|&emsp;&emsp;Data||QueryDataSourceSchemaResultListResponse|QueryDataSourceSchemaResultListResponse|
|&emsp;&emsp;&emsp;&emsp;QueryDataSourceSchemaResultList|数据模型Schema数组|array|QueryDataSourceSchemaResult|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;Id|数据模型ID|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;Name|数据模型标识|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;Title|数据模型标题|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;Schema|数据模型Schema|string||
|&emsp;&emsp;&emsp;&emsp;RequestId|请求ID|string||


**响应示例**:
```javascript
{  
    "Response":{  
        "Data":{  
            "QueryDataSourceSchemaResultList":[  
                {  
                    "Id":"data-1P1UtRsJ2",  
                    "Name":"sys_user",  
                    "Title":"用户",  
                    "Schema":"model schema"  
                }  
            ],  
            "RequestId":"reqid"  
        }  
    }  
}
```

## 查询选项集信息


**接口地址**:`/model/v1/describeOptionSet`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>根据选项集标识查询选项集具体信息</p>



**请求示例**:


```javascript
{
  "optionSetNames": []
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|查询选项集信息入参对象|查询选项集信息入参对象|body|true|查询选项集信息入参对象|查询选项集信息入参对象|
|&emsp;&emsp;optionSetNames|选项集标识列表||true|array|string|


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|OpenApiServerResponse查询选项集信息出参对象|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|response||公共出参对象，data类型为查询选项集信息出参对象|公共出参对象，data类型为查询选项集信息出参对象|
|&emsp;&emsp;requestId|requestId|string||
|&emsp;&emsp;error|错误信息|错误信息|错误信息|
|&emsp;&emsp;&emsp;&emsp;code|错误码|string||
|&emsp;&emsp;&emsp;&emsp;message|错误消息提示|string||
|&emsp;&emsp;data||查询选项集信息出参对象|查询选项集信息出参对象|
|&emsp;&emsp;&emsp;&emsp;total|选项集个数|integer||
|&emsp;&emsp;&emsp;&emsp;items|选项集列表|array|DescribeOptionSetDetailParam|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;name|标识|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;title|名称|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;description|描述|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;envId|所属环境|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;config|选项集KV列表|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;data|选项集kv映射结构|object||


**响应示例**:
```javascript
{
	"response": {
		"requestId": "",
		"error": {
			"code": "",
			"message": ""
		},
		"data": {
			"total": 1,
			"items": [
				{
					"name": "gender",
					"title": "性别",
					"description": "性别信息描述",
					"envId": "lowcode-a1b2c3",
					"config": "[{\"key\":\"1\",\"value\":\"男\"},{\"key\":\"2\",\"value\":\"女\"}]",
					"data": {"1":"男", "2":"女"}
				}
			]
		}
	}
}
```
