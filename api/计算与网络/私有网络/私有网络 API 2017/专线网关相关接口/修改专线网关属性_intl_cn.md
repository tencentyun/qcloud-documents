## 1. 接口描述

本接口(ModifyDirectConnectGateway)用于修改专线网关属性
接口请求域名：<font style="color:red">vpc.api.qcloud.com</font>

目前仅支持修改专线网关属性中的名称。

## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/372/4153" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为ModifyDirectConnectGateway。

| 参数名称 | 必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| vpcId | 是 | String | 系统分配的私有网络ID，例如：vpc-7t9nf3pu。|
| directConnectGatewayId | 是 | String | 系统分配的专线网关ID，例如：dcg-7t9nf3pu。|
| directConnectGatewayName | 是 | String | 专线网关名称，取值：1-25个中文、英文大小写的字母、数字和下划线分隔符。|


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 错误码。0: 成功, 其他值: 失败。|
| message | String | 错误信息。|
| taskId | Int | 任务ID，操作结果可以用taskId查询，详见查询任务执行结果接口。|

 ## 4. 错误码表
  以下错误码表仅列出了该接口的业务逻辑错误码，更多公共错误码详见<a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC错误码">VPC错误码</a>。
 
| 错误码 | 描述 |
|---------|---------|
| InvalidDirectConnectGatewayName | 专线网关名称不合法。专线网关名称取值范围：1-60个中文、英文大小写的字母、数字和下划线分隔符。 |
| InvalidVpc.NotFound | 无效的VPC。VPC资源不存在，请再次核实您输入的资源信息是否正确。 |
| InvalidDirectConnectGateway.NotFound | 无效的专线网关。专线网关资源不存在，请再次核实您输入的资源信息是否正确。 |

## 5. 示例
输入
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=ModifyDirectConnectGateway
&<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
&vpcId=vpc-dfgg190
&directConnectGatewayId=dcg-ddf14d
&directConnectGatewayName=专线网关1
</pre>
输出
```
{
    "code":"0",
    "message":"",
    "taskId":16284
}
```

