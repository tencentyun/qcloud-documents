## 1. 接口描述

本接口（DeleteNatGateway）用于删除 NAT 网关
接口请求域名：vpc.api.qcloud.com 

删除 NAT 网关后，系统会自动删除路由表中包含此 NAT 网关的路由项。

## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，详情请参见<a href="https://cloud.tencent.com/document/product/215/4772" title="公共请求参数"> 公共请求参数 </a>页面。其中，此接口的 Action 字段为 DeleteNatGateway。

| 参数名称 | 必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| vpcId | 是 | String | 私有网络 ID 或者统一 ID，建议使用统一 ID，例如 vpc-xfd55df |
| natId | 是 | String | 系统分配的高可用网关统一 ID，例如 nat-7t9nf3pu |


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 错误码。0: 成功，其他值: 失败|
| message | String | 错误信息|
| taskId | Int | 任务ID，操作结果可以用 taskId 查询，详见<a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2%e4%bb%bb%e5%8a%a1%e6%89%a7%e8%a1%8c%e7%bb%93%e6%9e%9c%e6%8e%a5%e5%8f%a3"> 查询任务执行结果接口</a>

 ## 4. 错误码表
以下错误码表仅列出了该接口的业务逻辑错误码，更多公共错误码详见<a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC错误码"> VPC 错误码</a>。

| 错误码 | 描述 |
|---------|---------|
| InvalidVpc.NotFound | 无效的 VPC，VPC 资源不存在。请再次核实您输入的资源信息是否正确，可通过<a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx"> DescribeVpcEx </a>接口查询 VPC |
| InvalidNatGatewayId.NotFound | 无效的 NAT 网关，NAT 网关资源不存在。请再次核实您输入的资源信息是否正确，可通过<a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2NAT%e7%bd%91%e5%85%b3?viewType=preview" title="DescribeNatGateway"> DescribeNatGateway </a>接口查询 NAT 网关 |


## 5. 示例
输入
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=DeleteNatGateway
&<公共请求参数>
&vpcId=190
&natId=nat-7t9nf3pu
</pre>
输出
```
{
    "code":"0",
    "message":"",
    "taskId":"16284"
}
```

