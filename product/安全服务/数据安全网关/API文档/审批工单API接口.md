## 接口描述

- **请求 URL**：`https://ip/iam/api/work_order/authzinfo`
- **请求方式**：PUT
- **请求类型**：Content-Type:application/json
- **字符编码**：UTF-8

## 请求参数

| 请求参数               | 必选/可选 | 类型   | 说明                                                         |
| ---------------------- | --------- | ------ | ------------------------------------------------------------ |
| X-Auth-Token           | true      | String | 认证 API 获取 token                                          |
| applicantUid           | true      | String | 审批人 UID                                                   |
| id                     | false     | String | 工单 ID                                                      |
| cause                  | true      | String | 工单描述                                                     |
| accountPolicyName      | false     | String | 账号策略名称                                                 |
| timePolicyName         | false     | String | 时间策略名称                                                 |
| cmdCtrlPolicyName      | false     | String | 字符命令控制策略名称                                         |
| dbCmdCtrlPolicyName    | false     | String | 数据库命令控制策略名称                                       |
| graphicCtrlPolicyName  | false     | String | 图形控制策略名称                                             |
| xftpCmdCtrlPolicyName  | false     | String | FTP 控制策略名称                                             |
| cmdAuditPolicyName     | false     | String | 字符审计策略名称                                             |
| graphicAuditPolicyName | false     | String | 图形审计策略名称                                             |
| xftpAuditPolicyName    | false     | String | FTP 审计策略名称                                             |
| userIds                | true      | List   | 执行人列表 UID                                               |
| reses                  | true      | List   | 授权资源列表                                                 |
| resType                | true      | String | 资源类型：<ul><li>unix：Unix/Linux<li>windows：Windows<li>database：数据库</ul> |
| ip                     | true      | String | 资源 IP                                                      |

## 请求示例

```shell
{
	"X-Auth-Token":"fnBIaLG275EtTswn2FwP4tWNjYNCvzqM1JoCabgyHjg=",
	"applicantUid": "shenpiren",
	"accountPolicyName": "账号策略",
	"timePolicyName": "时间策略",
	"cmdCtrlPolicyName": "字符命令控制策略",
	"dbCmdCtrlPolicyName": "数据库命令控制策略",
	"graphicCtrlPolicyName": "图形控制策略",
	"xftpCmdCtrlPolicyName": "FTP控制策略",
	"cmdAuditPolicyName": "字符审计策略",
	"graphicAuditPolicyName": "图形审计策略",
	"xftpAuditPolicyName": "FTP审计策略",
	"userIds": ["zhixingren", "zhixingren1"],
	"reses": [{
		"resType": "unix",
		"ip": "192.168.19.147"
	}, {
		"resType": "unix",
		"ip": "192.168.19.145"
	}],
	"cause": "测试",
	"id": "PF_20200617123343_07039198"
}

```

## 响应参数

| 返回值字段 | 类型   | 说明                                                         |
| ---------- | ------ | ------------------------------------------------------------ |
| result     | String | 操作结果标识：<ul><li>ok：成功<li>fail：失败</ul>            |
| status     | int    | 状态码：<ul><li>200：处理成功<li>210：处理成功数据不存在<li>405：参数异常	<li>500：服务端出现异常<li>6596：未配置邮箱服务<li>6598：未配置短信配置 </ul> |


## 响应示例

```shell
{
  "result": "ok",
  "status": 200
}

```
