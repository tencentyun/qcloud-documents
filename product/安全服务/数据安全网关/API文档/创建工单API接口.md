## 接口描述

- **请求 URL**：`https://ip/iam/api/work_order/basicinfo`
- **请求方式**：PUT
- **请求类型**：Content-Type:application/json
- **字符编码**：UTF-8

## 请求参数

| 请求参数     | 必选/可选 | 类型   | 说明                |
| ------------ | --------- | ------ | ------------------- |
| X-Auth-Token | true      | String | 认证 API 获取 token |
| title        | true      | String | 标题                |
| cause        | false     | String | 描述                |
| begTimeStr   | true      | String | 开始时间            |
| endTimeStr   | true      | String | 结束时间            |
| applicantUid | true      | String | 申请人 UID           |
| designUid    | true      | String | 审批人 UID           |


## 请求示例

```shell
{
	"X-Auth-Token":"fnBIaLG275EtTswn2FwP4tWNjYNCvzqM1JoCabgyHjg=",
	"applicantUid": "shenqingren",
	"endTimeStr": "2020-06-17 11:00:00",
	"designUid": "shenpiren",
	"cause": "测试",
	"title": "测试工单",
	"begTimeStr": "2020-06-16 11:00:00"
}
```

## 响应参数

| 返回值字段 | 类型   | 说明                                                         |
| ---------- | ------ | ------------------------------------------------------------ |
| result     | String | 操作结果标识：<ul><li>ok：成功<li>fail：失败</ul>            |
| status     | int    | 状态码：<ul><li>200：处理成功<li>210：处理成功数据不存在<li>405：参数异常	<li>500：服务端出现异常<li>559：审批人越权 <li>6596：未配置邮箱服务<li>6598：未配置短信配置 </ul> |


## 响应示例

```shell
{
   "result": "ok",
   "status": 200
}

```
