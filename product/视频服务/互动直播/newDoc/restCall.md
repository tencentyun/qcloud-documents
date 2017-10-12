# 后台接口

除了客户端sdk接口，互动直播后台也提供了一些接口，供开发者从自己的服务器发起调用。当前支持的接口有    

1. 录制。
2. 旁路直播。

## 调用格式

请求数据为HTTPs Req+JSON格式的Content Body，应答数据为HTTPs Rsp+JSON格式的Content Body。

## 双向认证
为系统安全性考虑，第三方后台请求要求双向认证。双向认证证书申请请参考腾讯云官网相关文档：[产品文档-云通信-第三方回调回调-双向认证配置指南-Nginx双向认证配置指南](http://cloud.tencent.com/doc/product/269/Nginx双向认证配置指南)


## HTTPs 请求的格式
HTTP请求的格式为：`POST URL HTTP/1.1\r\n`

## 后台服务URL格式

URL的格式为：`/ver/servicename/command?parameter/`，其中`ver`为版本号，目前为`v3`。servicenanme为`openim`。command根据请求的不同而设置。

例如，音频后台请求为：`v3/openim/videorelay`

### 域名:

测试环境为：<https://test.tim.qq.com/><br/>
正式环境为：<https://openapi.tim.qq.com/>

### Comand：

| Command | 说明 |
|---------|---------|
| videorelay | 视频聊天服务 |

### Parameter

Parameter的格式为：`usersig=xxxx& identifier=xxxx&sdkappid=xxxx&random=xxxxx&apn=x/`

| 参数名称 | 类型 | 说明 | 备注 |
| --- | --- | --- | --- |
| sdkappid | unsigned int | 使用open APP sdk时分配的appid | 在应用列表-应用配置-应用信息找到 |
| usersig | String | open app sdk的token | 在应用列表-应用配置-帐号集成体系-下载用户凭证找到。 |
| identifier | String | 管理员帐号 | 在应用列表-应用配置-帐号集成体系-帐号管理员由开发者创建 |
| random | unsigned int | 标识当前请求的整数随机数参数 | 32位整数随机数 |
| apn | unsigned int | 网络类型，0未知、1  wifi、2 2G、3 3G、4 4G | 后台操作填0 |

### 示例
完整的url如下：<
https://openapi.tim.qq.com/v3/openim/videorelay?usersig=xxxx&apn=1&identifier=xxxx&sdkappid=xxxx&random=xxxx&contenttype=json>

# 后台接口的内容定义

## 包体结构
### 请求内容由通用包头(GVCommOprHead)和具体包体两部分组成。如下所示：

【请求格式】

	{
		"reqhead":object of GVCommOprHead
		"reqbody":由GVCommOprHead中子命令决定
	}

| 参数名称 | 类型 | 说明 | 备注 |
| --- | --- | --- | --- |
| reqhead | GVCommOprHead | 音视频服务通用包头 |   |
| reqbody | 由GVCommOprHead中子命令决定 |   |   |    |
### 响应内容由通用包头(GVCommOprHead)和具体包体两部分组成。如下所示：
【响应格式】

		{
		"reqhead":object of GVCommOprHead
		"rspbody":由GVCommOprHead中子命令决定
		}

| 参数名称 | 类型 | 说明 | 备注 |
| --- | --- | --- | --- |
| reqhead | GVCommOprHead | 音视频服务通用包头 |   |
| rspbody | 由GVCommOprHead中子命令决定 |   |    |   |

## 通用包头(GVCommOprHead)定义

	{
	 "uint32_sub_cmd":xxx,
	 "uint32_seq":xxx,
	 "uint32_auth_key":xxxx,
	 "uint32_sdk_appid":xxx,
	 "str_av_token":"xxx",
	 "str_openid:"xxxx",
	 "rpt_to_Account":["xxxx"],
	 "bytes_cookie_buff":"xxxx",
	 "uint32_result:"xxxx",
	 "str_error_msg:"xxxx"
	}

| 参数名称 | 类型 | 说明 | 备注 |
| --- | --- | --- | --- |
| uint32_sub_cmd | unsigned int/必填 | 子命令：0x5:请求录制和停止录制 0x6：请求推流和停止推流 |   |
| uint32_seq | unsigned int/必填 | 请求序号 | 需要第三方原样带回 |
| uint32_auth_key | unsigned int/必填 | 群组号码 | 第三方定义的群组 |
| uint32_sdk_appid | unsigned int/必填 | 开放sdk appid |   |
| str_av_token | String/可选 | 第三方调用QQ音视频服务鉴权标识（无需填写）  |   |
| str_openid | String/可选 | 发起操作的openid后台操作时无需填写 |   |
| rpt_to_Account | String/可选 | 被操作的openid列表， **最多10个** ，具体含义参见业务包体 | **对于0x5、0x6请求只支持一个** |
| uint32_result | int/可选 | 非业务结果（0：成功，非0：失败）-1：表示解包错误-2：包体错误-3：内部服务失败-4：包头校验失败-5 ：av_token校验不通过 | 响应消息才用到 |
| str_error_msg | String/可选 | 错误消息 | 响应消息才用到 |
| bytes_cookie_buff | String | 业务cook，响应时原样带回 |   |

【代码示例】

	"reqhead":
	{
		"uint32_sub_cmd":6,
		"uint32_seq":xxx,
		"uint32_auth_key":xxx,
		"uint32_sdk_appid":xxx,
		"rpt_to_Account":["xxx"],
		"bytes_cookie_buff":"xxxx"
	},
