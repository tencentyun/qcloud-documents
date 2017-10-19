## Push消息统一路径
消息相关的接口，统一的接口地址是`http://wns.api.qcloud.com/api/`
在统一地址后面加上不同的接口名字，实现响应的功能接口。

## 签名生成方法
sign=Base64(Hmac-sha1(plaintext, secretkey))
secretkey：摘要算法key，在腾讯云创建app时分配，
plaintext（原文）：“appid&timestamp”

## OpenApi接口说明
### 发送消息接口
接口说明：发送在线消息通知到客户端
接口名：send_msg_new
请求方法：http post方法

请求参数:

| 参数名 | 类型 | 必选 | 说明 |
|---------|---------|---------|---------|
| appid | int | 是 | 第三方appid |
| secretid | string | 是 | 第三方加密用的密钥id |
| sign | string | 是 | 第三方签名 |
| tm | int | 是 | 时间戳，防请求重放 |
| uid | string | 是 | 用户唯一标识 |
| wid | string | 是 | 用户名下的某个设备标识，需要指定某台设备时才需填写 |
| plat | string | 否 | 推送目标手机平台，默认0=所有平台 1=iphone 2=安卓 |
| tag | string | 是 | 消息标签，会填在STMsg.Tag推给客户端 |
| content | string | 是 | 消息内容 |
| aps | string | 否 | os离线消息内容，json格式，见苹果文档 |
| only_online | string | 否 | 1=表示只发当前在线用户，默认0在线离线都会发 |
| expire | string | 否 | 消息有效期，单位秒，表示从现在起经过该时间之后该消息将被丢弃 |
注：
i)uid/wid：填写一个即可
i)参数格式：将参数按query_string格式拼接，用http post发送到接口

响应参数：

| 参数名 | 类型 | 必选|说明|
|---------|---------|---------|---------|
| errno | int | 是 | 响应码 |
| msg | string | 否 | 错误信息 |
| detail | string | 否 | 终端推送结果 |
注：
i)数据格式：json格式
i)errno为0时，detail是详细信息
示例：

```
{
		"errno":0,
		"detail:"
		{
			[
				{
					 ret: 0,
					 wid: 111111
				}
			],
		}
}

```

### 获取在线状态接口
接口说明：获取指定用户或终端的在线状态
接口名：get_online_status
请求方法：http post方法
请求参数:

| 参数名 | 类型 | 必选|说明|
|---------|---------|---------|---------|
| appid | int | 是 | 第三方appid |
| secretid | string | 是 | 第三方加密用的密钥id |
| sign | string | 是 | 第三方签名 |
| tm | int | 是 | 时间戳，防请求重放 |
| uid | string | 是 | 用户唯一标识|
| wid | string | 是 | 用户名下的某个设备标识，需要指定某台设备时才需填写 |

注：
i)参数格式：json
i)uid/wid：填写一个即可，按填写的id获取在线状态
i)批量：支持批量获取，上限是100个
示例：

```
{
			"appid":65538,
			"secretid":"asdadasd",
			"sign":"SADFKLJKLJCASDK",
			"tm": 435423123132113,
			"uid":["uid1", "uid2", "uid3"],
			"wid":[wid1, wid2, wid3]
}

```

响应参数：

| 参数名 | 类型 | 必选|说明|
|---------|---------|---------|---------|
| ret | int | 是 | 响应码 |
| msg | string | 否 | 错误信息 |
| data | 数组 | 是 | 按uid和wid维度返回的在线状态数组 |
| uid |  uid在线数组 | 否 | 每个uid的在线状态( 0:离线  1:在线) |
| wid |  wid在线数组 | 否 | 每个wid的在线状态( 0:离线  1:在线) |
注：
i)参数格式：json
i)uid和wid关系：wid是设备id，一个用户(uid)可以最多登录5个设备(wid)

示例：

```
{
		"ret":0,
		"msg":"",
		"data:"
		{
			"uid":
			[
				{
					"uid1":
					[
						{"wid1": 0},
						{" wid2": 1},
						{ "wid3": 0}
					]
				},
				{
					"uid2":
					[
						{ "wid1": 0},
						{ "wid2": 0}
					]
				}
			],
			"wid":
			[
				{"wid1": 0},
				{"wid2": 0},
				{"wid3": 0}
			]
	}
}

```


### 通知在线状态
接口说明：获取指定用户或终端的在线状态
接口名：notify_online_status
请求方法：http post方法
请求参数:

| 参数名 | 类型 | 必选|说明|
|---------|---------|---------|---------|
| appid | int | 是 | 第三方appid |
| secretid | string | 是 | 第三方加密用的密钥id |
| sign | string | 是 | 第三方签名 |
| tm | int | 是 | 时间戳，防请求重放 |
| status | 状态数组 | 是 | 按uid数组推送在线状态(0:离线  1:在线)|

注：
i)参数格式：json
i)批量：支持批量获取，上限是100个

示例：

```
{
			"appid":65538,
			"secretid":"asdadasd",
			"sign":"SADFKLJKLJCASDK",
			"tm": 435423123132113,
			"status":
			[
				{
					"uid1":
					[
						{"wid1": 0},
						{"wid2": 0},
						{"wid3": 1}
					]
				},
				{
					"uid2":
					[
						{"wid1": 0},
						{"wid2": 0}
					]
				}
			]
	}

```



