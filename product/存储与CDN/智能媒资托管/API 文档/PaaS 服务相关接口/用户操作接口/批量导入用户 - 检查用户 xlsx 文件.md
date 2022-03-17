## 功能描述

检查批量导入使用的 xlsx 文件内容是否符合模板。


#### 接口说明

权限要求：超级管理员或系统管理员。

## 请求

#### 请求示例

POST /user/v1/allowlist/`{OrganizationId}`/batch-import/`{FilePath}`?checkOnly?user_token=`{UserToken}`

请求参数：
  - OrganizationId：组织 ID，必选参数。
  - UserToken：用户令牌，必选参数。
  - FilePath：用户表格文件 path，即获取用户 xlsx 简单上传文件参数中的响应字段 path。

#### 请求体

该请求无请求体。

## 响应

#### 响应码

- 同步检查完成：HTTP 200 OK。
- 启用异步检查：HTTP 202 Accepted。 


#### 响应体

application/json

- 响应体示例：
启用异步检查，返回异步任务 ID。
```json
{
  "taskId": 28
}
```
同步检查完成，返回检查结果。
- 格式检查正确响应体示例
```json
[
  {
    "taskId": 28,
    "status": 200,
    "result": [
      {
        "status": 200
      }
    ]
  }
]
```
- 格式检查错误响应体示例
```json
[
    {
        "taskId": 28,
        "status": 400,
        "result": [
            {
              "status": 400,
              "code": "InvalidBatchAllowlistInfo",
              "message": "Name/phone/capacity/sector columns are required"
            }
        ]
    }
]
```
- 响应体字段说明：
    - taskId：整数，任务 ID。
    - status：整数，任务状态码。
	 - 202：任务进行中。
	 - 200：任务成功完成且有返回结果，返回结果在 result 字段中。
	 - 204：任务成功完成且无返回结果。
	 - 500：任务执行失败。
	 - 499：用户取消。
	 - 207： 多状态。
    - result：对象数组，任务成功完成后的返回结果。
        - status：数字，检查结果，200 表示格式符合要求。
        - code：字符串，错误码，格式不合要求时返回。
        - message：字符串，错误信息，格式不合要求时返回。

