## 接口描述

- **请求 URL**：`https://ip/iam/api/user/user_res`
- **请求方式**：GET
- **请求类型**：Content-Type:application/json
- **字符编码**：UTF-8

## 请求参数

| 请求参数     | 必选/可选 | 类型   | 说明             |
| ------------ | --------- | ------ | ---------------- |
| X-Auth-Token | true      | String | 认证 API 获取 token |

## 请求示例

```shell
https://ip/iam/api/user/user_res?X-Auth-Token=fnBIaLG275EtTswn2FwP4tWNjYNCvzqM1JoCabgyHjg=
```

## 响应参数

| 返回值字段 | 类型   | 说明                                                         |
| ---------- | ------ | ------------------------------------------------------------ |
| users      | Array  | 用户列表                                                     |
| userId     | String | 用户 ID                                                      |
| userName   | String | 用户名称                                                     |
| userType   | String | 用户类型                                                     |
| reses      | Array  | 资源列表                                                     |
| resName    | String | 资源名称                                                     |
| ipv4       | String | IPv4                                                         |
| result     | String | 操作结果标识：<ul><li>ok：成功</li><li>fail：失败 </li>      |
| status     | int    | 状态码：<ul><li>200：处理成功<li>210：处理成功数据不存在<li>405：参数异常</ul> |

## 响应示例

```shell
{
	"result": "ok",
  "status": 200,
	"users: [{
		"reses: [{
			"resName": "堡垒机测试资源",
			"ipv4": "172.16.0.1"
		}],
		"userType": "其他",
		"userName": "test",
		"userId": "test"
	}]
}
```
