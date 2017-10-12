## 1. 接口描述

域名：catapi.api.qcloud.com
接口：DescribeCatAgentGroup



查询拨测分组的详情，入参取值示例如下：
groupId=10000888

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/405/公共请求参数" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为DescribeCatAgentGroup。

### 2.1输入参数

| 参数名称    | 必选   | 类型   | 输入内容   | 描述     |
| ------- | ---- | ---- | ------ | ------ |
| groupId | 是    | Int  | 拨测分组id | 拨测分组id |
#### 

## 3. 输出参数

| 参数名称    | 类型     | 描述                  |
| ------- | ------ | ------------------- |
| code    | Int    | 错误码, 0: 成功, 其他值表示失败 |
| message | String | 返回信息                |
| data    | Array  | 结果数据                |

### 3.1 data 元素的结构

| 参数名称      | 类型     | 描述        |
| --------- | ------ | --------- |
| groupId   | Int    | 拨测分组id    |
| name      | String | 拨测分组名称    |
| isDefault | Int    | 是否缺省      |
| taskNum   | Int    | 采用本分组的任务数 |
| agent     | Array  | Agent列表   |

#### 3.1.1 agent 元素的结构  

| 参数名称         | 类型     | 描述    |
| ------------ | ------ | ----- |
| province     | String | 省份    |
| provinceName | String | 省份名称  |
| isp          | String | 运营商   |
| ispName      | String | 运营商名称 |

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
&Action=DescribeCatAgentGroup
&groupId=10000888

```

输出

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "groupName": "test_group",
        "groupDesc": "",
        "isDefault": 0,
        "agent": [
            {
                "province": "gd",
                "provinceName": "广东",
                "isp": "ctc",
                "ispName": "电信"
            },
            {
                "province": "gd",
                "provinceName": "广东",
                "isp": "cuc",
                "ispName": "联通"
            }            
        ]
    }
}
```