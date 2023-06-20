私有网络 API 已全面升级至3.0版本，基于2.0版本接口访问时延较高和使用复杂的考虑，原私有网络 API 2.0 接口服务将不再提供技术支持，并于**2023年01月01日**起下线。如果您的业务还在使用私有网络 API 2.0 相关接口，建议尽快将服务升级至 API 3.0 接口，以免对您的业务造成影响。

请您参照如下对比，找到您需要升级的新接口，完成升级：
- 2.0文档：[API 概览](https://cloud.tencent.com/document/product/215/909)
- 3.0文档：[API 概览](https://cloud.tencent.com/document/product/215/15755)

## API 2.0 切换3.0接口列表
### 私有网络
<table>
<tr>
<th width="25%">接口功能</th>
<th width="25%">API 2.0</th>
<th width="25%">API 3.0</th>
<th width="25%">备注</th>
</tr>
<tr>
<td>创建私有网络</td>
<td><a href="https://cloud.tencent.com/document/api/215/1309">CreateVpc</a></td>
<td><a href="https://cloud.tencent.com/document/api/215/15774">CreateVpc</a></td>
<td>-</td>
</tr>
<tr>
<td>删除私有网络</td>
<td><a href="https://cloud.tencent.com/document/api/215/1307">DeleteVpc</a></td>
<td><a href="https://cloud.tencent.com/document/api/215/15775">DeleteVpc</a></td>
<td>-</td>
</tr>
<tr>
<td>修改私有网络名称</td>
<td><a href="https://cloud.tencent.com/document/api/215/1310">ModifyVpcAttribute</a></td>
<td><a href="https://cloud.tencent.com/document/api/215/15773">ModifyVpcAttribute</a></td>
<td>-</td>
</tr>
<tr>
<td>查询私有网络列表</td>
<td><a href="https://cloud.tencent.com/document/api/215/1372">DescribeVpcEx</a></td>
<td><a href="https://cloud.tencent.com/document/api/215/15778">DescribeVpcs</a></td>
<td>-</td>
</tr>
<tr>
<td>绑定私有网络内主机与 VIP</td>
<td><a href="https://cloud.tencent.com/document/api/215/1361">AssociateVip</a></td>
<td><a>/</a></td>
<td>本接口实现的功能已经用弹性网卡功能代替，不推荐使用该接口</td>
</tr>
<tr>
<td>创建私有网络和基础网络设备互通</td>
<td><a href="https://cloud.tencent.com/document/api/215/2098">AttachClassicLinkVpc</a></td>
<td><a href="https://cloud.tencent.com/document/api/215/15779">AttachClassicLinkVpc</a></td>
<td>-</td>
</tr>
<tr>
<td>删除私有网络和基础网络设备互通</td>
<td><a href="https://cloud.tencent.com/document/api/215/2097">DetachClassicLinkVpc</a></td>
<td><a href="https://cloud.tencent.com/document/api/215/15777">DetachClassicLinkVpc</a></td>
<td>-</td>
</tr>
<tr>
<td>查询私有网络和基础网络设备互通</td>
<td><a href="https://cloud.tencent.com/document/api/215/2112">DescribeVpcClassicLink</a></td>
<td><a href="https://cloud.tencent.com/document/api/215/15776">DescribeClassicLinkInstances</a></td>
<td>-</td>
</tr>
</table>

### 子网
<table>
<tr>
<th width="30%">接口功能</th>
<th width="35%">API 2.0</th>
<th width="35%">API 3.0</th>
</tr>
<tr>
<td>创建子网</td>
<td><a href="https://cloud.tencent.com/document/product/215/1314">CreateSubnet</a></td>
<td><a href="https://cloud.tencent.com/document/product/215/15782">CreateSubnet</a></td>
</tr>
<tr>
<td>删除子网</td>
<td><a href="https://cloud.tencent.com/document/api/215/1312">DeleteSubnet</a></td>
<td><a href="https://cloud.tencent.com/document/api/215/15783">DeleteSubnet</a></td>
</tr>
<tr>
<td>修改子网名称</td>
<td><a href="https://cloud.tencent.com/document/api/215/1313">ModifySubnetAttribute</a></td>
<td><a href="https://cloud.tencent.com/document/api/215/15781">ModifySubnetAttribute</a></td>
</tr>
<tr>
<td>查询子网列表</td>
<td><a href="https://cloud.tencent.com/document/api/215/1371">DescribeSubnetEx</a></td>
<td><a href="https://cloud.tencent.com/document/api/215/15784">DescribeSubnets</a></td>
</tr>
<tr>
<td>查询子网详情</td>
<td><a href="https://cloud.tencent.com/document/api/215/1311">DescribeSubnet</a></td>
<td><a href="https://cloud.tencent.com/document/api/215/15784">DescribeSubnets</a></td>
</tr>
</table>

### 路由表
<table>
<tr>
<th width="30%">接口功能</th>
<th width="35%">API 2.0</th>
<th width="35%">API 3.0</th>
</tr>
<tr>
<td>创建路由表</td>
<td><a href="https://cloud.tencent.com/document/api/215/1419">CreateRouteTable</a></td>
<td><a href="https://cloud.tencent.com/document/api/215/15768">CreateRouteTable</a></td>
</tr>
<tr>
<td>删除路由表</td>
<td><a href="https://cloud.tencent.com/document/api/215/1418">DeleteRouteTable</a></td>
<td><a href="https://cloud.tencent.com/document/api/215/15771">DeleteRouteTable</a></td>
</tr>
<tr>
<td>修改路由表</td>
<td><a href="https://cloud.tencent.com/document/api/215/1417">ModifyRouteTableAttribute</a></td>
<td><a href="https://cloud.tencent.com/document/api/215/15766">ModifyRouteTableAttribute</a></td>
</tr>
<tr>
<td>查询路由表</td>
<td><a href="https://cloud.tencent.com/document/api/215/1420">DescribeRouteTable</a></td>
<td><a href="https://cloud.tencent.com/document/api/215/15763">DescribeRouteTables</a></td>
</tr>
<tr>
<td>修改子网关联的路由表</td>
<td><a href="https://cloud.tencent.com/document/api/215/1416">AssociateRouteTable</a></td>
<td><a href="https://cloud.tencent.com/document/api/215/15767">ReplaceRouteTableAssociation</a></td>
</tr>
<tr>
<td>添加路由策略</td>
<td><a href="https://cloud.tencent.com/document/api/215/5688">CreateRoute</a></td>
<td><a href="https://cloud.tencent.com/document/api/215/16724">CreateRoutes</a></td>
</tr>
<tr>
<td>删除路由策略</td>
<td><a href="https://cloud.tencent.com/document/api/215/5689">DeleteRoute</a></td>
<td><a href="https://cloud.tencent.com/document/api/215/16725">DeleteRoutes</a></td>
</tr>
</table>

### 网络 ACL
<table>
<tr>
<th width="30%">接口功能</th>
<th width="35%">API 2.0</th>
<th width="35%">API 3.0</th>
</tr>
<tr>
<td>创建 VPC 网络 ACL</td>
<td><a href="https://cloud.tencent.com/document/api/215/1437">CreateNetworkAcl</a></td>
<td><a href="https://cloud.tencent.com/document/api/215/42162">CreateNetworkAcl</a></td>
</tr>
<tr>
<td>删除网络 ACL</td>
<td><a href="https://cloud.tencent.com/document/api/215/1439">DeleteNetworkAcl</a></td>
<td><a href="https://cloud.tencent.com/document/api/215/42161">DeleteNetworkAcl</a></td>
</tr>
<tr>
<td>修改网络 ACL 名称</td>
<td><a href="https://cloud.tencent.com/document/api/215/1443">ModifyNetworkAcl</a></td>
<td><a href="https://cloud.tencent.com/document/api/215/42158">ModifyNetworkAclAttribute</a></td>
</tr>
<tr>
<td>查询网络 ACL 列表</td>
<td><a href="https://cloud.tencent.com/document/api/215/1441">DescribeNetworkAcl</a></td>
<td><a href="https://cloud.tencent.com/document/api/215/42160">DescribeNetworkAcls</a></td>
</tr>
<tr>
<td>设置网络 ACL 规则</td>
<td><a href="https://cloud.tencent.com/document/api/215/1444">ModifyNetworkAclEntry</a></td>
<td><a href="https://cloud.tencent.com/document/api/215/42107">ModifyNetworkAclEntries</a></td>
</tr>
<tr>
<td>网络 ACL 绑定子网</td>
<td><a href="https://cloud.tencent.com/document/api/215/1438">CreateSubnetAclRule</a></td>
<td><a href="https://cloud.tencent.com/document/api/215/42163">AssociateNetworkAclSubnets</a></td>
</tr>
<tr>
<td>网络 ACL 解绑子网</td>
<td><a href="https://cloud.tencent.com/document/api/215/1442">DeteleSubnetAclRule</a></td>
<td><a href="https://cloud.tencent.com/document/api/215/42159">DisassociateNetworkAclSubnets</a></td>
</tr>
</table>

### 弹性网卡
<table>
<tr>
<th width="30%">接口功能</th>
<th width="35%">API 2.0</th>
<th width="35%">API 3.0</th>
</tr>
<tr>
<td>创建弹性网卡</td>
<td><a href="https://cloud.tencent.com/document/api/215/4811">CreateNetworkInterface</a></td>
<td><a href="https://cloud.tencent.com/document/api/215/15818">CreateNetworkInterface</a></td>
</tr>
<tr>
<td>删除弹性网卡</td>
<td><a href="https://cloud.tencent.com/document/api/215/4813">DeleteNetworkInterface</a></td>
<td><a href="https://cloud.tencent.com/document/api/215/15822">DeleteNetworkInterface</a></td>
</tr>
<tr>
<td>查询弹性网卡信息</td>
<td><a href="https://cloud.tencent.com/document/api/215/4814">DescribeNetworkInterfaces</a></td>
<td><a href="https://cloud.tencent.com/document/api/215/15817">DescribeNetworkInterfaces</a></td>
</tr>
<tr>
<td>弹性网卡申请内网 IP</td>
<td><a href="https://cloud.tencent.com/document/api/215/4817">AssignPrivateIpAddresses</a></td>
<td><a href="https://cloud.tencent.com/document/api/215/15813">AssignPrivateIpAddresses</a></td>
</tr>
<tr>
<td>弹性网卡退还内网 IP</td>
<td><a href="https://cloud.tencent.com/document/api/215/4819">UnassignPrivateIpAddresses</a></td>
<td><a href="https://cloud.tencent.com/document/api/215/15814">UnassignPrivateIpAddresses</a></td>
</tr>
<tr>
<td>弹性网卡绑定云服务器</td>
<td><a href="https://cloud.tencent.com/document/api/215/4820">AttachNetworkInterface</a></td>
<td><a href="https://cloud.tencent.com/document/api/215/15819">AttachNetworkInterface</a></td>
</tr>
<tr>
<td>弹性网卡解绑云服务器</td>
<td><a href="https://cloud.tencent.com/document/product/215/4822">DetachNetworkInterface</a></td>
<td><a href="https://cloud.tencent.com/document/api/215/15816">DetachNetworkInterface</a></td>
</tr>
<tr>
<td>弹性网卡迁移</td>
<td><a href="https://cloud.tencent.com/document/api/215/5384">MigrateNetworkInterface</a></td>
<td><a href="https://cloud.tencent.com/document/api/215/15821">MigrateNetworkInterface</a></td>
</tr>
<tr>
<td>内网 IP 迁移</td>
<td><a href="https://cloud.tencent.com/document/api/215/5385">MigratePrivateIpAddress</a></td>
<td><a href="https://cloud.tencent.com/document/api/215/15820">MigratePrivateIpAddress</a></td>
</tr>
</table>



### 安全组
<table>
<tr>
<th width="25%">接口功能</th>
<th width="25%">API 2.0</th>
<th width="25%">API 3.0</th>
<th width="25%">备注</th>
</tr>
<tr>
<td>查询实例关联安全组</td>
<td>DescribeInstancesOfSecurityGroup</td>
<td><a href="https://cloud.tencent.com/document/product/213/15728">DescribeInstances </a></td>
<td>Filter参数带security-group-id</td>
</tr>
<tr>
<td>查询安全组规则</td>
<td>DescribeSecurityGroupPolicys/DescribeSecurityGroupPolicy</td>
<td><a href="https://cloud.tencent.com/document/product/1108/47698">DescribeSecurityGroupPolicies</a></td>
<td>-</td>
</tr>
<tr>
<td>删除安全组</td>
<td>DeleteSecurityGroup</td>
<td><a href="https://cloud.tencent.com/document/api/215/15803">DeleteSecurityGroup</a></td>
<td>-</td>
</tr>
<tr>
<td>查看安全组</td>
<td>DescribeSecurityGroupEx/DescribeSecurityGroups</td>
<td><a href="https://cloud.tencent.com/document/api/215/15808">DescribeSecurityGroups</a></td>
<td>-</td>
</tr>
<tr>
<td>替换单条安全组规则</td>
<td>ModifySingleSecurityGroupPolicy</td>
<td><a href="https://cloud.tencent.com/document/api/215/15811">ReplaceSecurityGroupPolicy</a></td>
<td>-</td>
</tr>
<tr>
<td>修改安全组出站和入站规则</td>
<td>ModifySecurityGroupPolicy</td>
<td><a href="https://cloud.tencent.com/document/api/215/15810">ModifySecurityGroupPolicies</a></td>
<td>-</td>
</tr>
<tr>
<td>查询网卡关联安全组</td>
<td>DescribeNetworkInterfacesOfSecurityGroup</td>
<td><a href="https://cloud.tencent.com/document/api/215/15817">DescribeNetworkInterfaces</a></td>
<td>Filter参数带groups.security-group-id</td>
</tr>
<tr>
<td>添加安全组规则</td>
<td>CreateSecurityGroupPolicy</td>
<td><a href="https://cloud.tencent.com/document/api/215/15807">CreateSecurityGroupPolicies</a></td>
<td>-</td>
</tr>
</table>

### 其他
<table>
<tr>
<th width="30%">接口功能</th>
<th width="35%">API 2.0</th>
<th width="35%">API 3.0</th>
</tr>
<tr>
<td>查询VPC异步任务执行结果</td>
<td><a href="https://cloud.tencent.com/document/api/215/5094">DescribeVpcTaskResult</a></td>
<td><a href="https://cloud.tencent.com/document/api/215/59037">DescribeVpcTaskResult</a></td>
</tr>
<tr>
<td>查询账户属性</td>
<td><a href="https://cloud.tencent.com/document/api/215/9499">DescribeAccountVpcAttributes</a></td>
<td><a href="https://cloud.tencent.com/document/api/215/17875">DescribeAccountAttributes</a></td>
</tr>
</table>


