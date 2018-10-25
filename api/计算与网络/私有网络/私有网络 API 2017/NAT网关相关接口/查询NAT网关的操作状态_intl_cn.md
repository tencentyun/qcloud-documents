## 1. 接口描述

本接口(QueryNatGatewayProductionStatus)用于查询NAT网关的生产状态
接口请求域名：<font style="color:red">vpc.api.qcloud.com</font>

## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/372/4153" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为QueryNatGatewayProductionStatus。

| 参数名称 | 必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| billId | 是 | String | 创建时返回的订单ID, 用该ID查询最后结果|


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | int | 错误码。0: 成功, 其他值: 失败|
| message | string | 错误信息|
| data.status | int | 生产结果：0: 成功, 1:失败, 2:进行中 |
| data.errorCode | string | 错误码 |

 ## 4. 错误码表
 该接口没有业务错误码，公共错误码详见<a href="https://cloud.tencent.com/doc/api/245/%e7%a7%81%e6%9c%89%e7%bd%91%e7%bb%9c%e9%94%99%e8%af%af%e7%a0%81?viewType=preview" title="私有网络错误码">vpc错误码</a>



## 5. 示例
输入
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=QueryNatGatewayProductionStatus
&<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
&billId=2160000000
</pre>
输出
```
{
    "code":"0",
    "message":"",
    "data":{
          "status":0,
          "errorCode":0
		}
}
```

