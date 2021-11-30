
## 接口描述

- **请求 URL**：`https://ip/iam/api/resrole/user_res_policy?resroleName={resroleName}`
- **请求方式**：GET
- **请求类型**：Content-Type:application/json
- **字符编码**：UTF-8

## 请求参数

| 请求参数     | 必选/可选 | 类型   | 说明              |
| ------------ | --------- | ------ | ----------------- |
| X-Auth-Token | true      | String | 认证 API 获取 token |
| resroleName  | true      | String | 工作组名称        |

## 请求示例

```shell
https://ip/iam/api/resrole/user_res_policy?resroleName=测试
```

## 响应参数

| 返回值字段 | 类型   | 说明                                                         |
| ---------- | ------ | ------------------------------------------------------------ |
| resroles   | Array  | 工作组列表                                                   |
| users      | Array  | 用户列表                                                     |
| userId     | String | 用户 ID                                                      |
| userName   | String | 用户名称                                                     |
| userType   | String | 用户类型                                                     |
| reses      | Array  | 资源列表                                                     |
| resName    | String | 资源名称                                                     |
| ipv4       | String | IPv4                                                         |
| policies   | Array  | 策略列表                                                     |
| firstType  | int    | 一级类型：<ul><li> 2：普通策略<li>4：控制策略<li>8：审计策略 |
| secondType | int    | 二级类型：<ul><li>2：时间策略<li>4：账号策略<li>8：字符命令控制策略<li>16：图形控制策略<li>32：FTP 控制策略<li>64：字符审计策略<li>128：图形审计策略<li>256：FTP 审计策略 |
| policyName | String | 策略名称                                                     |
| result     | String | 操作结果标识：<ul><li>ok：成功<li>fail：失败                 |
| status     | int    | 状态码：<ul><li>200：处理成功<li>210：处理成功数据不存在<li>405：参数异常 |


## 响应示例

```shell
{
	"result": "ok",
"status": 200,
	"resroles: [{
		"reses: [{
			"resName": "2234",
			"ipv4": "1.1.1.5"
		}, {
			"resName": "堡垒机测试资源",
			"ipv4": "172.16.0.1"
		}],
		"policies [{
		  	"policyName": "test",
			"firstType": 2,
			"secondType": 2
		}, {
			"policyName": "test",
			"firstType": 2,
			"secondType": 4
		}],
		"users": [{
			"userType": "其他",
			"userName": "1",
			"userId": "1"
		}, {
			"userType": "其他",
			"userName": "test",
			"userId": "test"
		}]
	}]
}
```
