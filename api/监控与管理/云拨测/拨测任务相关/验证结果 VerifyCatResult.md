## 1. 接口描述

域名：catapi.api.qcloud.com
接口：VerifyCatResult



验证拨测任务，结果验证查询

验证成功的，才建议调用CreateCatTask 正式创建拨测任务。

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/405/公共请求参数" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为VerifyCatResult。

### 2.1输入参数

| 参数名称     | 必选   | 类型               | 输入内容 | 描述   |
| -------- | ---- | ---------------- | ---- | ---- |
| resultId | 是    | Int要查询的拨测任务的结果id |      | 正整数  |
#### 

## 3. 输出参数

| 参数名称        | 类型     | 描述                  |
| ----------- | ------ | ------------------- |
| code        | Int    | 错误码, 0: 成功, 其他值表示失败 |
| message     | String | 返回信息                |
| errorReason | String | 拨测失败的原因             |
| suggestion  | String | 解决建议                |


## 4. 错误码表

| 错误代码  | 错误描述                 | 英文描述                          |
| ----- | -------------------- | ----------------------------- |
| 10001 | 输入参数错误。结合message一起看。 | InvalidParameter              |
| 11000 | DB操作失败               | InternalError.DBoperationFail |
| 20002 | 结果id 不存在             | InvalidResource               |

## 5. 示例

输入

```
https://catapi.api.qcloud.com/v2/index.php?
& <<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
&Action=VerifyCatResult
&resultId=100
```

输出

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "errorReason": "验证尚未完成",
    "suggestion": ""
}
```