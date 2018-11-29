## 功能描述

GetBindHostedLanIPStatus用于获取托管设备绑定IP状态。

接口请求域名：bm.api.qcloud.com

## 请求
### 请求示例

```
GET https://bm.api.qcloud.com/v2/index.php?Action=GetBindHostedLanIPStatus
	&<公共请求参数>
	&instanceId=<托管机器实例>
```

### 请求参数

以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见[公共请求参数页面](/document/product/386/6718)。其中，此接口的Action字段为GetBindHostedLanIPStatus。

| 参数名称       | 必选   | 类型     | 描述                      |
| ---------- | ---- | ------ | ----------------------- |
| instanceId | 是    | String | 托管机器实例ID，形如：chm-xxxxxx。 |


## 响应
### 响应示例

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
}
```

### 响应参数

| 参数名称    | 类型            | 描述                                       |
| ------- | ------------- | ---------------------------------------- |
| code    | Int           | 错误码。0表示成功，其他值表示失败。详见错误码页面的[公共错误码](/document/product/386/6725)。 |
| message | String        | 错误信息描述，与接口相关。                            |
| data    | Array(Object) | 托管物理服务器绑定内网IP状态列表，具体结构描述如data结构所示。       |

data结构

| 参数名称      | 类型       | 描述                |
| --------- | -------- | ----------------- |
| name      | String   | 绑定内网IP过程的状态的描述。   |
| startTime | Datetime | 开始时间。             |
| endTime   | Datetime | 结束时间。             |
| current   | Int      | 是否是当前操作。0：不是。1：是。 |



## 错误码

| 错误代码  | 英文提示                               | 错误描述      |
| ----- | ---------------------------------- | --------- |
| 9003  | InvalidParameter                   | 参数错误。     |
| 9001  | InternalError.DbError              | 数据库服务异常。  |
| 10008 | InvalidParameter.InvalidAppId      | appId无效。  |
| 18137 | InvalidParameter.InvalidInstanceId | 托管机器实例无效。 |


## 实际案例

### 输入

```
GET https://bm.api.qcloud.com/v2/index.php?Action=GetBindHostedLanIPStatus
	&SecretId=AKIDlfdHxN0ntSVt4KPH0xXWnGl21UUFNoO5
	&Nonce=48451
	&Timestamp=1521019133
	&Region=gz
	&instanceId=chm-f45zd4
	&Signature=R8iUOXFwFDCBInyWk8KQ70qr8YU%3D
```

### 输出

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": [
        {
          "name": "正在申请内网IP",
          "startTime": "2018-04-24 12:00:01",
          "endTime": "2018-04-24 12:00:03",
        },
        {
          "name": "配置私有网络",
          "startTime": "2018-04-24 12:00:03",
          "endTime": "2018-04-24 12:00:05",
        },
        {
          "name": "在网卡上配置内网IP，现场服务工单 :",
          "startTime": "2018-04-24 12:00:05",
          "current": 1,
        },
        {
          "name": "正在打开交换机端口",
        },
    ]
}
```