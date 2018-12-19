## 1. 接口描述

域名：catapi.api.qcloud.com
接口：UpdateCatAgentGroup



修改拨测分组，入参取值示例如下：
groupId=10000888&groupName=test_group2&isDefault=0&agent.0.province=gd&agent.0.isp=cmc&agent.1.province=gd&agent.1.isp=cuc

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/405/公共请求参数" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为UpdateCatAgentGroup。

### 2.1输入参数

| 参数名称             | 必选   | 类型     | 输入内容   | 描述                                       |
| ---------------- | ---- | ------ | ------ | ---------------------------------------- |
| groupId          | 是    | Int    | 拨测分组id | 拨测分组id                                   |
| groupName        | 是    | String | 拨测分组名  | 拨测分组名称，最长32字节                            |
| isDefault        | 是    | Int    | 0/1    | 是否为默认分组。取值范围 0 或者 1                      |
| agent.0.province | 是    | String | 省份     | 省份。最大取值范围，参见下表1 中的province 列             |
| agent.0.isp      | 是    | String | 运营商    | 运营商。最大取值范围，参见下表2 中的isp 列。province, isp 需要成对地进行选择。参数对的取值范围。参见：DescribeAgentList 的返回结果中的provice, isp组合。 |
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

## 5. 示例

输入

```
https://catapi.api.qcloud.com/v2/index.php?
& <<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
&Action=UpdateCatAgentGroup
&groupId=10000888
&groupName=test_group2
&isDefault=0
&agent.0.province=gd
&agent.0.isp=cmc
&agent.1.province=gd
&agent.1.isp=cuc
```

输出

```
{
	"code": 0,
	"message": ""
}
```