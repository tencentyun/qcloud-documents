## 1. 接口描述

域名：catapi.api.qcloud.com
接口：UpdateCatAlarmPloicy



为拨测任务修改告警策略，入参取值示例如下：
policyId=2695&taskId=24418&interval=1&operate=lt&threshold=70&receiverGroupId=1513

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/405/公共请求参数" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为UpdateCatAlarmPloicy。

### 2.1输入参数

| 参数名称            | 必选   | 类型     | 输入内容     | 描述                                       |
| --------------- | ---- | ------ | -------- | ---------------------------------------- |
| policyId        | 是    | Int    | 策略id     | 拨测告警策略id                                 |
| taskId          | 是    | Int    | 拨测任务id   | 正整数。                                     |
| interval        | 是    | Int    | 持续周期     | 持续周期。值为任务的period 乘以0、1、2、3、4。单位：分钟       |
| operate         | 是    | String | lt       | 目前取值仅支持 lt (小于)                          |
| threshold       | 是    | Int    | 百分比      | 门限百分比。比如：80，表示80%。成功率低于80%时告警。           |
| receiverGroupId | 是    | Int    | 告警接收组的id | 参见： DescribeAlarmGroupList 接口。从返回结果里的groupId 中选取一个。 |
#### 

## 3. 输出参数

| 参数名称    | 类型     | 描述                  |
| ------- | ------ | ------------------- |
| code    | Int    | 错误码, 0: 成功, 其他值表示失败 |
| message | String | 返回信息                |


## 4. 错误码表

| 错误代码  | 错误描述                                | 英文描述                          |
| ----- | ----------------------------------- | ----------------------------- |
| 10001 | 输入参数错误。可能是达到最大拨测分组数限制。结合message一起看。 | InvalidParameter              |
| 11000 | DB操作失败                              | InternalError.DBoperationFail |
| 20002 | 策略id 不存在                            | InvalidResource               |

## 5. 示例

输入

```
https://catapi.api.qcloud.com/v2/index.php?
& <<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
&Action=UpdateCatAlarmPloicy
&policyId=2695
&taskId=24418
&interval=1
&operate=lt
&threshold=70
&receiverGroupId=1513
```

输出

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success"
}
```