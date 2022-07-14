## 接口描述

- **请求 URL**：`https://ip/iam/api/resrole/res`
- **请求方式**：PUT
- **请求类型**：Content-Type:application/json
- **字符编码**：UTF-8

## 请求参数

| 请求参数     | 必选/可选 | 类型   | 说明                                                         |
| ------------ | --------- | ------ | ------------------------------------------------------------ |
| X-Auth-Token | true      | String | 认证 API 获取 token                                          |
| resroleName  | true      | String | 工作组名称                                                   |
| resList      | true      | List   | 资源列表                                                     |
| resIpv4      | true      | String | IPv4，与 resIpv6 参数二选一                                  |
| resIpv6      | true      | String | IPv6，与 resIpv4 参数二选一                                  |
| resType      | true      | String | 资源类型：<ul><li>unix：Unix/Linux<li>windows：Windows<li>database：数据库</ul> |

## 请求示例

```shell
{
	"X-Auth-Token":"fnBIaLG275EtTswn2FwP4tWNjYNCvzqM1JoCabgyHjg=",
	"resroleName": "测试",
	"resList": [{
		"resIpv4": "1.1.1.1",
		"resType": "unix"
	}, {
		"resIpv4": "1.1.1.1",
		"resType": "windows"
	}]
}
```

## 响应参数

| 返回值字段 | 类型   | 说明                                                         |
| ---------- | ------ | ------------------------------------------------------------ |
| result     | String | 操作结果标识：<ul><li>ok：成功<li>fail：失败</ul>            |
| status     | int    | 状态码：<ul><li>200：处理成功<li>210：处理成功数据不存在<li>405：参数异常	<li>500：服务端出现异常</ul> |


## 响应示例

```shell
{
  "result": "ok",
  "status": 200
}

```
