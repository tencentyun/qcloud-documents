## 接口描述

- **请求 URL**：`https://ip/iam/api/resrole`
- **请求方式**：PUT
- **请求类型**：Content-Type:application/json
- **字符编码**：UTF-8

## 请求参数

| 请求参数     | 必选/可选 | 类型   | 说明                |
| ------------ | --------- | ------ | ------------------- |
| X-Auth-Token | true      | String | 认证 API 获取 token |
| name         | true      | String | 工作组名称          |
| pname        | true      | String | 存储工作组节点名称  |

## 请求示例

```shell
{
  "X-Auth-Token":"fnBIaLG275EtTswn2FwP4tWNjYNCvzqM1JoCabgyHjg=",
  "name": "研发工作组",
  "pname": "北京研发部门"
}
```

## 响应参数

| 返回值字段 | 类型   | 说明                                                         |
| ---------- | ------ | ------------------------------------------------------------ |
| result     | String | 操作结果标识：<ul><li>ok：成功<li>fail：失败</ul>            |
| status     | int    | 状态码：<ul><li>200：处理成功<li>210：处理成功数据不存在<li>405：参数异常	<li>500：服务端出现异常<li>550：工作组已存在<li>610：存储工作组节点不存在</ul> |


## 响应示例

```shell
{
   "result": "ok",
   "status": 200
}

```
