## 1. 接口描述
域名：vpc.api.qcloud.com
接口名：InquiryNatPrice

查询NAT网关价格。

## 2. 输入参数
| 参数名称 | 必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| maxConcurrent | 是 | Int | NAT网关最大并发连接|


## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 错误码。0：成功，其他值：失败|
| message | String | 错误信息|
| data | Array | 返回的价格数组 |

data结构

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| data.price | Int | 描述（待补充）| 
| data.totalCost | Int | 描述（待补充）| 
| data.realTotalCost | Int | 描述（待补充）| 
| data.timeSpan | Int | 描述（待补充）| 
| data.timeUnit | String | 描述（待补充）| 
| data.goodsNum | Int | 描述（待补充）| 
| data.policy | Int | 描述（待补充）| 
| data.unitPrice | Int | 描述（待补充）| 


## 4. 示例
输入
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=InquiryNatPrice
&maxConcurrent=2000000
&<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>
</pre>
输出
```
{
    "code":"0",
    "message":"",
    "data":[
        {
            "price":"150",
            "totalCost":"150",
            "realTotalCost":"150",
            "timeSpan":"1",
            "timeUnit":"h",
            "goodsNum":"1",
            "policy":"100",
            "unitPrice":"150"
        }
    ]
}
```
 
 
