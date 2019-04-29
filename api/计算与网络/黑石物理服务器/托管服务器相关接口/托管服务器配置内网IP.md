## 功能描述

BindHostedLanIP 用于配置托管服务器的内网IP。

接口请求域名：bm.api.qcloud.com

## 请求
### 请求示例

```
GET https://bm.api.qcloud.com/v2/index.php?Action=BindHostedLanIP
	&<公共请求参数>
	&instances.0.instanceId=<托管机器实例>
	&instances.0.userName=<托管机器登录用户名>
	&instances.0.password=<托管机器登录用密码>
	&unVpcId=<私有网络唯一ID>
	&unSubnetId=<子网唯一ID>
	&gatewayIp=<网关IP>
	&operateMode=<操作模式>
	&contacts=<联系人>
	&mobile=<联系电话>
```

### 请求参数

以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见[公共请求参数页面](/document/product/386/6718)。其中，此接口的Action字段为BindHostedLanIP。

| 参数名称        | 必选   | 类型            | 描述              |
| ----------- | ---- | ------------- | --------------- |
| instances   | 是    | Array(Object) | 托管服务器数组。        |
| unVpcId     | 是    | String        | 私有网络唯一ID。       |
| unSubnetId  | 是    | String        | 子网唯一ID。         |
| gatewayIp   | 是    | String        | 网关IP。           |
| operateMode | 是    | Int           | 0：操作前授权。1：直接操作。 |
| contacts    | 是    | String        | 联系人。            |
| mobile      | 是    | String        | 联系电话。           |



instance结构

| 参数名称       | 必选   | 类型     | 描述          |
| ---------- | ---- | ------ | ----------- |
| instanceId | 是    | String | 托管服务器实例ID。  |
| userName   | 是    | String | 托管服务器登录用户名。 |
| password   | 是    | String | 托管服务器登录密码。  |



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
| 18102 | InvalidParameter.InvalidVpcId         | 私有网络Id无效。   |
| 18103 | InvalidParameter.InvalidSubnetId      | 子网Id无效。     |
| 18106 | InvalidParameter.InvalidOperateMode   | 操作模式无效。     |
| 18108 | InvalidParameter.InvalidContact       | 联系人无效。      |
| 18109 | InvalidParameter.InvalidContactMobile | 联系电话无效。     |
| 18107 | InvalidParameter.InvalidUsername      | 用户名无效。      |
| 18115 | InvalidParameter.InvalidPassword      | 密码无效。       |
| 18110 | InternalError.LanIPExist              | 内网IP已经存在。   |
| 18111 | InvalidParameter.VpcIdNotExist        | 私有网络不存在。    |
| 18112 | InvalidParameter.SubnetNotExist       | 子网不存在。      |
| 18113 | InvalidParameter.HostedDeviceNotExist | 托管服务器不存在。   |
| 18134 | InternalError.Locked                  | 正在绑定或解绑过程中。 |
| 18113 | InvalidParameter.HostedDeviceNotExist | 托管设备不存在。    |
| 18131 | InternalError.SendMsgFailed           | 发送请求失败。     |
| 18133 | InternalError.InvalidState            | 状态无效。       |


## 实际案例

### 输入

```
GET https://bm.api.qcloud.com/v2/index.php?Action=BindHostedLanIP
	&SecretId=AKIDlfdHxN0ntSVt4KPH0xXWnGl21UUFNoO5
	&Nonce=48451
	&Timestamp=1521019133
	&Region=gz
	&Signature=R8iUOXFwFDCBInyWk8KQ70qr8YU%3D
	&instances.0.instanceId=chm-gr9wprj0
	&instances.0.userName=root
	&instances.0.password=password
	&unVpcId=vpc-6t44o010
	&unSubnetId=subnet-fa1lzxhz
	&gatewayIp=10.10.2.1
	&operateMode=0
	&contacts=张三
	&mobile=13800000000
```

### 输出

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
}
```