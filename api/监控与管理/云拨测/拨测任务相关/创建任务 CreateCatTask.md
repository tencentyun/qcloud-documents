## 1. 接口描述

域名：catapi.api.qcloud.com
接口：CreateCatTask



创建或修改 拨测任务。
如果验证未成功，请先验证成功。避免创建失败率100%的拨测任务。对于已存在的任务id，会执行修改操作。

注意：如果修改拨测分组agentGroupId 后，需要调用pauseCatTask、runCatTask 重新运行任务，以使新拨测分组的改动立即生效。

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/405/公共请求参数" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为CreateCatTask。

### 2.1输入参数

| 参数名称         | 必选   | 类型     | 输入内容   | 描述                                       |
| ------------ | ---- | ------ | ------ | ---------------------------------------- |
| taskId       | 是    | Int    | 拨测任务id | 正整数。验证成功的拨测任务id                          |
| agentGroupId | 是    | Int    | 拨测分组id | 体现本拨测任务要采用那些运营商作为拨测源。一般可直接填写本用户的默认拨测分组。参见：DescribeCatAgentGroupList 接口，本参数使用返回结果里的groupId的值。 |
| catTypeName  | 是    | String | 拨测类型   | http, https, ping, tcp 之一                |
| url          | 是    | String | 拨测的url | 例如：www.baidu.com (url域名解析需要能解析出具体的ip)    |
| host         | 否    | String | ip     | 需要满足ip 的格式                               |
| period       | 是    | Int    | 拨测周期   | 取值可为1,5,15,30之一, 单位：分钟。精度不能低于用户等级规定的最小精度 |
| taskName     | 否    | String | 拨测任务名称 | 不能超过32个字符。同一个用户创建的任务名不可重复                |
#### 2.1.1 可选参数（catTypeName= http, https之一时）

| 参数名称      | 必选   | 类型     | 描述                                       |
| --------- | ---- | ------ | ---------------------------------------- |
| sslVer    | 否    | String | url中含有https时有用。缺省为SSLv23。需要为 TLSv1_2, TLSv1_1, TLSv1, SSLv2, SSLv23, SSLv3 之一 |
| postData  | 否    | String | POST 请求数据。空字符串表示非POST请求                  |
| userAgent | 否    | String | 用户agent 信息                               |
| checkStr  | 否    | String | 要在结果中进行匹配的字符串                            |
| checkType | 否    | String | 1 表示通过检查结果是否包含checkStr 进行校验              |
| cookie    | 否    | String | 需要设置的cookie信息                            |



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
| 20004 | 调用teg拨测服务失败                         | InternalError                 |

## 5. 示例

输入

```
https://catapi.api.qcloud.com/v2/index.php?
& <<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
&Action=CreateCatTask
&taskName=test_http
&taskId=24454
&catTypeName=http
&period=15
&agentGroupId=1510
&url=www.tencent2.com
```

输出

```
{
    "code": 0,
    "message": ""
}
```