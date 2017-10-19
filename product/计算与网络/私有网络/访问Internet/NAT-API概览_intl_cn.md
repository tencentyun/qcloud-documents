<style rel="stylesheet">
table th:nth-of-type(1){
width:200px;
}</style>
<style rel="stylesheet">
table th:nth-of-type(2){
width:200px;
}</style>
<style rel="stylesheet">
table th:nth-of-type(3){
width:200px;
}</style>
<style rel="stylesheet">
table th:nth-of-type(4){
width:200px;
}</style>
<style rel="stylesheet">
table tr:hover {
background: #efefef; 
</style>

您可以使用 API 操作来设置和管理您的 NAT 网关，有关更多 VPC 内其他资源的内容，可以查看 <a href="https://cloud.tencent.com/doc/api/245/909" target="_blank">VPC 所有 API 概览</a>。

| 接口功能 | Action ID |  功能描述 |
|:---------:|:---------:|:---------:|
| 创建 NAT 网关 | <a href="https://cloud.tencent.com/doc/api/245/4094" target="_blank">CreateNatGateway</a> |  创建 NAT 网关。 |
| 查询 NAT 网关创建状态 | <a href="https://cloud.tencent.com/doc/api/245/4089" target="_blank">QueryNatGatewayProductionStatus</a> |  查询 NAT 网关创建状态。 |
| 删除 NAT 网关 | <a href="https://cloud.tencent.com/doc/api/245/4087" target="_blank">DeleteNatGateway</a> | 删除 NAT 网关。 |
| 修改 NAT 网关 | <a href="https://cloud.tencent.com/doc/api/245/4086" target="_blank">ModifyNatGateway</a> | 修改 NAT 网关。 |
| 查询 NAT 网关 | <a href="https://cloud.tencent.com/doc/api/245/4088" target="_blank">DescribeNatGateway</a> | 查询 NAT 网关。 |
| NAT 网关绑定 EIP | <a href="https://cloud.tencent.com/doc/api/245/4093" target="_blank">EipBindNatGateway</a> | NAT 网关绑定 EIP。 |
| NAT 网关解绑 EIP | <a href="https://cloud.tencent.com/doc/api/245/4092" target="_blank">EipUnBindNatGateway</a> | NAT 网关解绑 EIP。 |
| 升级 NAT 网关规格 | <a href="https://cloud.tencent.com/doc/api/245/4090" target="_blank">UpgradeNatGateway</a> | 升级 NAT 网关规格。 |