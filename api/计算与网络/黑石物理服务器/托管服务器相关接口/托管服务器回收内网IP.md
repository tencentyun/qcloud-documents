## 功能描述

UnbindHostedLanIP 用于回收托管服务器内网IP。

接口请求域名：bm.api.qcloud.com

## 请求
### 请求示例

```
GET https://bm.api.qcloud.com/v2/index.php?Action=UnbindHostedLanIP
	&<公共请求参数>
	&instanceIds.0=<托管机器实例>
```

### 请求参数

以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见[公共请求参数页面](/document/product/386/6718)。其中，此接口的Action字段为 UnbindHostedLanIP。

| 参数名称        | 必选   | 类型     | 描述                            |
| ----------- | ---- | ------ | ----------------------------- |
| instanceIds | 是    | String | 托管机器实例ID数组，形如：["chm-xxxxxx"]。 |


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

| 参数名称     | 类型     | 描述                                       |
| -------- | ------ | ---------------------------------------- |
| code     | Int    | 错误码。0表示成功，其他值表示失败。详见错误码页面的[公共错误码](/document/product/386/6725)。 |
| message  | String | 错误信息描述，与接口相关。                            |
| codeDesc | String | 返回码信息描述。                                 |


## 错误码

| 错误代码  | 英文提示                                  | 错误描述        |
| ----- | ------------------------------------- | ----------- |
| 9003  | InvalidParameter                      | 参数错误。       |
| 9001  | InternalError.DbError                 | 数据库服务异常。    |
| 18100 | InvalidParameter.InvalidAppId         | appId无效。    |
| 18101 | InvalidParameter.InvalidDevice        | 托管设备无效。     |
| 18108 | InvalidParameter.InvalidContact       | 联系人无效。      |
| 18109 | InvalidParameter.InvalidContactMobile | 联系电话无效。     |
| 18134 | InternalError.Locked                  | 正在绑定或解绑过程中。 |
| 18113 | InvalidParameter.HostedDeviceNotExist | 托管设备不存在。    |
| 18131 | InternalError.SendMsgFailed           | 发送请求失败。     |


## 实际案例

### 输入

```
GET https://bm.api.qcloud.com/v2/index.php?Action=UnbindHostedLanIP
	&SecretId=AKIDlfdHxN0ntSVt4KPH0xXWnGl21UUFNoO5
	&Nonce=48451
	&Timestamp=1521019133
	&Region=gz
	&instanceIds.0=chm-f45zd4
	&Signature=R8iUOXFwFDCBInyWk8KQ70qr8YU%3D
```

### 输出

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
}
```