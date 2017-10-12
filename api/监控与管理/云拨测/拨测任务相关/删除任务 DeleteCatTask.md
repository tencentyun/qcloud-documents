## 1. 接口描述

域名：catapi.api.qcloud.com
接口：DeleteCatTask



删除多个拨测任务，入参取值示例如下：
taskId.0=1&taskId.1=2&taskId.1=3

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/405/公共请求参数" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为DeleteCatTask。

### 2.1输入参数

| 参数名称     | 必选   | 类型   | 输入内容   | 描述   |
| -------- | ---- | ---- | ------ | ---- |
| taskId.0 | 是    | Int  | 拨测任务id | 正整数  |
| taskId.1 | 否    | Int  | 拨测任务id | 正整数  |
#### 

## 3. 输出参数

| 参数名称    | 类型     | 描述                  |
| ------- | ------ | ------------------- |
| code    | Int    | 错误码, 0: 成功, 其他值表示失败 |
| message | String | 返回信息                |


## 4. 错误码表

| 错误代码  | 错误描述                 | 英文描述                          |
| ----- | -------------------- | ----------------------------- |
| 10001 | 输入参数错误。结合message一起看。 | InvalidParameter              |
| 11000 | DB操作失败               | InternalError.DBoperationFail |
| 20002 | 任务id 不存在             | InvalidResource               |

## 5. 示例

输入

```
https://catapi.api.qcloud.com/v2/index.php?
& <<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
&Action=DeleteCatTask
&taskId.0=1
&taskId.1=2
&taskId.2=3
```

输出

```
{
	"code": 0,
	"message": ""
}
```