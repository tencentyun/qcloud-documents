## 接口描述

- **请求 URL**：`https://ip/iam/api/user`
- **请求方式**：PUT
- **请求类型**：Content-Type:application/json
- **字符编码**：UTF-8

## 请求参数

| 请求参数     | 必选/可选 | 类型   | 说明                |
| ------------ | --------- | ------ | ------------------- |
| X-Auth-Token | true      | String | 认证 API 获取 token |
| uid          | true      | String | 用户账号            |
| name         | true      | String | 用户名称            |
| typeStr      | false     | String | 用户类型            |
| mobile       | true      | String | 电话号码            |
| email        | true      | String | 邮箱                |
| desc         | false     | String | 描述                |

## 请求示例

```shell
{
  "X-Auth-Token":"fnBIaLG275EtTswn2FwP4tWNjYNCvzqM1JoCabgyHjg=",
  "uid": "test",
  "name": "测试用户",
  "typeStr": "测试",
  "email": "test@qq.com",
  "mobile": "18888888888",
  "desc": "ceshi"
}

```

## 响应参数

| 返回值字段 | 类型   | 说明                                                         |
| ---------- | ------ | ------------------------------------------------------------ |
| result     | String | 操作结果标识：<ul><li>ok：成功<li>fail：失败</ul>            |
| status     | int    | 状态码：<ul><li>200：处理成功<li>210：处理成功数据不存在<li>405：参数异常	<li>500：服务端出现异常<li>550：用户已存在<li>6595：未配置初始化信息<li>698：用户邮箱为空<li>699：用户手机为空</ul> |


## 响应示例

```shell
{
    "result": "ok",
    "status": 200
}

```
