## 操作场景
弹性公网 IP （Elastic IP，简称 EIP），是可以独立购买和持有的、某个地域下固定不变的公网 IP 地址。借助弹性公网 IP，您可以快速将地址重新映射到账户中的另一个实例或 NAT 网关实例，从而屏蔽实例故障。本文档介绍如何使用弹性 IP 地址。


## 操作指引

您可以使用如下弹性公网 IP 功能：

<table>
	<tr><th>功能类型</th><th>相关文档</th><th>操作场景</th></tr>
	<tr><td rowspan="3">获取弹性公网 IP</td><td><a href="https://cloud.tencent.com/document/product/1199/41698">申请 EIP</a></td><td>申请弹性公网 IP。</td></tr>
	<tr><td><a href="https://cloud.tencent.com/document/product/1199/41706">普通公网 IP 转 EIP</a></td><td>将云服务器的普通公网 IP 转换为弹性公网 IP，转换后，弹性公网 IP 具备随时与云服务器解绑和绑定的能力，更易于实现公网 IP 的灵活管理。</td></tr>
	<tr><td><a href="https://cloud.tencent.com/document/product/1199/41708">找回公网 IP 地址</a></td><td>若您误操作释放或退还了公网 IP 地址（包含弹性公网 IP 和普通公网 IP），可以在弹性公网 IP 控制台找回，找回后的公网 IP 为弹性公网 IP。</td></tr>
	<tr><td rowspan="3">绑定弹性公网 IP</td><td><a href="https://cloud.tencent.com/document/product/1199/41702">EIP 绑定云资源</a></td><td>将弹性公网 IP 绑定到云服务器实例、NAT 网关等云资源上，利用弹性公网 IP 灵活地容灾与提供公网通信服务等。</td></tr>
	<tr><td><a href="https://cloud.tencent.com/document/product/1199/43866">CVM 主网卡绑定多 IP</a></td><td>为单台云服务器实例绑定多个弹性公网 IP，以实现流量转移，提高云服务器的利用率。</td></tr>
	<tr><td><a href="https://cloud.tencent.com/document/product/1199/44153">CVM 添加辅助网卡并绑定多 IP</a></td><td>若单台云服务器实例可绑定公网 IP 的限额不满足您的需求，您可以通过添加辅助网卡来绑定多个公网 IP，以实现流量转移，提高云服务器的利用率。</td></tr>
	<tr><td>弹性公网 IP 直通</td><td><a href="https://cloud.tencent.com/document/product/1199/41709">EIP 直通</a></td><td>适用于云服务器内需要查看公网 IP 的场景。例如，将内网流量和外网流量分别转发到不同的 IP 地址。</td></tr>
	<tr><td>调整弹性公网 IP 带宽</td><td><a href="https://cloud.tencent.com/document/product/1199/41705">调整带宽</a></td><td>您可以根据实际需要，及时调整弹性公网 IP 带宽，实时生效。</td></tr>
	<tr><td rowspan="2">解绑/释放弹性公网 IP</td><td><a href="https://cloud.tencent.com/document/product/1199/41703">解绑 EIP</a></td><td>您可以随时将弹性公网 IP 与云资源解绑，解绑后您可以将其与其他云资源重新绑定。</td></tr>
	<tr><td><a href="https://cloud.tencent.com/document/product/1199/41704">释放 EIP</a></td><td>若您不再使用弹性公网 IP，可在控制台将其释放。</td></tr>
</table>

