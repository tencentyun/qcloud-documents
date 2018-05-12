## 1. 接口描述

本接口(ModifyVpcPeeringConnectionEx)用于修改同地域对等连接属性。
接口请求域名：<font style="color:red">vpc.api.qcloud.com</font>

## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/372/4153" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为ModifyVpcPeeringConnectionEx。

| 参数名称 | 必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| peeringConnectionId | 是 | String | 私有网络对等连接 ID，例如：pcx-krmzap90。|
| peeringConnectionName | 否 | String | 对等连接名称，可任意命名，但不得超过60个字符。|
| bandwidth | 否 | Int | 对等连接带宽上限，单位Mbps，目前支持10,20,50,100,200,500,1000。|


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 错误码。0：成功，其他值：失败。|
| message | String | 错误信息。|
| taskId | Int | 任务ID，操作结果可以用taskId查询，详见<a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2%e4%bb%bb%e5%8a%a1%e6%89%a7%e8%a1%8c%e7%bb%93%e6%9e%9c%e6%8e%a5%e5%8f%a3">查询任务执行结果接口</a>。 |

 ## 4. 错误码表
 以下错误码表仅列出了该接口的业务逻辑错误码，更多公共错误码详见<a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC错误码">VPC错误码</a>。
 
| 错误码 | 描述 |
|---------|---------|
| InvalidPeeringConnectionName | 对等连接名称不合法。可任意命名，但不得超过60个字符。 |
| InvalidVpc.NotFound | 无效的vpc，vpc资源不存在。请再次核实您输入的资源信息是否正确。 |
| InvalidPeeringConnection.NotFound | 无效的对等连接，对等连接资源不存在。请再次核实您输入的资源信息是否正确。 |

## 5. 示例
输入
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=ModifyVpcPeeringConnectionEx
&<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
&peeringConnectionId=pcx-krmzap90
&peeringConnectionName=uuuuuuu
</pre>
输出
```
{
    "code":"0",
    "message":"",
    "taskId":1235
}
```

