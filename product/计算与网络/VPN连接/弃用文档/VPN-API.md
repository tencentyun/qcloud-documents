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
## API 概览
您可以使用 API 操作来设置和管理您的 VPN 连接，私有网络的更多相关 API 可以参考 <a href="https://cloud.tencent.com/doc/api/245/909" target="_blank">私有网络所有 API 概览</a>
### VPN 相关接口
| 接口功能 | Action ID |  功能描述 |
|---------|:---------:|---------|
| 查询 VPN 网关价格 | <a href="http://cloud.tencent.com/doc/api/245/5104" target="_blank">InquiryVpnPrice</a> | 查询 VPN 网关价格。 |
| 购买 VPN 网关 | <a href="http://cloud.tencent.com/doc/api/245/5106" target="_blank">CreateVpn</a> | 购买 VPN 网关。 |
| 修改 VPN 网关属性 | <a href="http://cloud.tencent.com/doc/api/245/5107" target="_blank">ModifyVpnGw</a> | 修改指定 VPN 网关信息，例如名称。|
| 查询 VPN 网关列表 | <a href="http://cloud.tencent.com/doc/api/245/5108" target="_blank">DescribeVpnGw</a> | 根据用户信息，如 VPN 网关 ID，名称，查询对应 VPN 网关的信息。|
| 续费 VPN 网关 | <a href="http://cloud.tencent.com/doc/api/245/5109" target="_blank">RenewVpn</a> | 续费 VPN 网关。 |

### 对端网关相关接口
| 接口功能 | Action ID |  功能描述 |
|---------|:---------:|---------|
| 创建对端网关 | <a href="http://cloud.tencent.com/doc/api/245/5116" target="_blank">AddUserGw</a> | 创建要连接的对端网关。 |
| 删除对端网关 | <a href="http://cloud.tencent.com/doc/api/245/5117" target="_blank">DeleteUserGw</a> | 删除指定对端网关。 |
| 修改对端网关名称 | <a href="http://cloud.tencent.com/doc/api/245/5118" target="_blank">ModifyUserGw</a> | 修改对端网关名称。 |
| 查询对端网关列表 | <a href="http://cloud.tencent.com/doc/api/245/5119" target="_blank">DescribeUserGw</a> | 根据用户信息，如对端网关 ID，名称，查询对应对端网关的信息。|
| 获取可支持的对端网关厂商信息 | <a href="http://cloud.tencent.com/doc/api/245/5120" target="_blank">DescribeUserGwVendor</a> | 查询腾讯云 VPN 网关可支持的对端网关厂商信息。 |


### VPN 通道相关接口

| 接口功能 | Action ID |  功能描述 |
|---------|:---------:|---------|
| 创建 VPN 通道 | <a href="http://cloud.tencent.com/doc/api/245/5110" target="_blank">AddVpnConn</a> | 创建 VPN 加密通道，将 VPC 接入其他网络资源。 |
| 删除 VPN 通道 | <a href="http://cloud.tencent.com/doc/api/245/5111" target="_blank">DeleteVpnConn</a> | 删除指定 VPN 通道。|
| 修改 VPN 通道 | <a href="http://cloud.tencent.com/doc/api/245/5112" target="_blank">ModifyVpnConn</a> | 修改指定 VPN 通道的信息，如名称。 |
| 查询 VPN 通道列表 | <a href="http://cloud.tencent.com/doc/api/245/5113" target="_blank">DescribeVpnConn</a> | 根据用户信息，如通道  ID，名称，查询对应通道的信息。|
| 下载 VPN 通道配置 | <a href="http://cloud.tencent.com/doc/api/245/5114" target="_blank">GetVpnConnConfig</a> | 下载 VPN 通道配置，对通道配置做调整。 |
| 获取 VPN 通道的监控数据 | <a href="http://cloud.tencent.com/doc/api/245/5115" target="_blank">DescribeVpnConnMonitor</a> |  获取 VPN 通道的监控数据。 |


