## 1. 接口描述
 
本接口(DetachClassicLinkVpc)用于删除私有网络和基础网络云主机互通。
接口请求域名：<font style="color:red">vpc.api.qcloud.com</font>

 

## 2. 输入参数
 以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/372/4153" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为DetachClassicLinkVpc。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| vpcId | 是 | String | 系统分配的私有网络ID，支持升级前的vpcId，也支持升级后的unVpcId。 |
| instanceIds.n | 是 | Array | 基础网络云主机ID，例如：instanceIds.0=ins-df221dd，可通过云api接口<a href="https://cloud.tencent.com/doc/api/229/831" title="查看实例列表">DescribeInstances</a>查询。 |
 

## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码, 0表示成功，其他值表示失败。详见错误码页面的<a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="公共错误码">公共错误码</a>。|
| message | String | 模块错误信息描述，与接口相关。|
| taskId | Int | 任务ID，操作结果可以用taskId查询，详见<a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2%e4%bb%bb%e5%8a%a1%e6%89%a7%e8%a1%8c%e7%bb%93%e6%9e%9c%e6%8e%a5%e5%8f%a3">查询任务执行结果接口</a>。|

 ## 4. 错误码表
 以下错误码表仅列出了该接口的业务逻辑错误码，更多公共错误码详见<a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC错误码">VPC错误码</a>。
 
| 错误码 | 描述 |
|---------|---------|
| InvalidInstance.NotFound | 云主机不存在，请核实您填写的instanceId是否正确，查询VPC下云主机详见<a href="https://cloud.tencent.com/doc/api/229/831" title="查看云主机实例列表">查看云主机实例列表</a>。 |
| InvalidVpc.NotFound | 无效的VPC,VPC资源不存在，请再次核实您输入的资源信息是否正确。 |

## 5. 示例
 
输入
<pre>

  https://vpc.api.qcloud.com/v2/index.php?Action=DetachClassicLinkVpc
	&<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
	&vpcId=vpc-2ari9m7h
	&instanceIds.0=ins-df454d
</pre>

输出
```

{
    "code": 0,
    "message": "",
		"taskId":135254
}

```

