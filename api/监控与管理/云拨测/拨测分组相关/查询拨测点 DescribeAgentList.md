## 1. 接口描述

域名：catapi.api.qcloud.com
接口：DescribeAgentList



查询本用户可选的拨测点列表

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/405/公共请求参数" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为DescribeAgentList。

### 2.1输入参数

| 参数名称 | 必选   | 类型   | 输入内容 | 描述   |
| ---- | ---- | ---- | ---- | ---- |
| 无    |      |      |      |      |
#### 

## 3. 输出参数

| 参数名称    | 类型     | 描述                  |
| ------- | ------ | ------------------- |
| code    | Int    | 错误码, 0: 成功, 其他值表示失败 |
| message | String | 返回信息                |
| data    | Array  | 结果数据                |

### 3.1 data 的结构

| 参数名称  | 类型    | 描述    |
| ----- | ----- | ----- |
| agent | Array | 运营商列表 |

#### 3.1.1 agent元素  的结构  

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
&Action=DescribeAgentList

```

输出

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "agent": [
            {
                "province": "sichuan",
                "provinceName": "四川",
                "isp": "cmc",
                "ispName": "移动"
            },
            {
                "province": "heilongjiang",
                "provinceName": "黑龙江",
                "isp": "cmc",
                "ispName": "移动"
            }
        ]
    }
}
```