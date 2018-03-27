
### 通知在线状态
接口说明：获取指定用户或终端的在线状态
接口名：notify_online_status
请求方法：http post 方法
请求参数:

| 参数名 | 类型 | 必选|说明|
|---------|---------|---------|---------|
| appid | int | 是 | 第三方 appid |
| secretid | string | 是 | 第三方加密用的密钥 id |
| sign | string | 是 | 第三方签名 |
| tm | int | 是 | 时间戳，防请求重放 |
| status | 状态数组 | 是 | 按 uid 数组推送在线状态(0:离线  1:在线)|

注：
i)参数格式：json
i)批量：支持批量获取，上限是 100 个

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
