## 1. 接口描述

本接口(QueryBmNatGatewayProductionStatus)用于查询黑石NAT网关的操作状态
接口请求域名：<font style="color:red">vpc.api.qcloud.com</font>

## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/372/4153" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为QueryBmNatGatewayProductionStatus。

| 参数名称 | 必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| taskId | 是 | String | 任务ID, 用该ID查询最后结果|


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | int | 错误码。0: 成功, 其他值: 失败|
| message | string | 错误信息|
| data.result | int | 0为正在进行，1为执行成功，2为执行失败 |

 ## 4. 错误码表
 该接口没有业务错误码.



## 5. 示例
输入
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=QueryBmNatGatewayProductionStatus
&<<a href="https://www.qcloud.com/doc/api/229/6976">公共请求参数</a>>
&taskId=2160000000
</pre>
输出
```
{
    "code":"0",
    "message":"",
    "data":{
          "result":1
		}
}
```

