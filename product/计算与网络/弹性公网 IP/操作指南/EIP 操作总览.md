弹性公网 IP 是可以独立购买和持有的、某个地域下固定不变的公网 IP 地址。借助弹性公网 IP，您可以快速将地址重新映射到账户中的另一个实例或 NAT 网关实例，从而屏蔽实例故障。本文档介绍如何使用弹性 IP 地址。


## 操作指引
您可以使用如下弹性公网 IP 功能：
<table>
<tr>
<th>功能类型</th>
<th>相关文档</th>
<th>操作场景</th>
</tr>
<tr>
<td rowspan="3">获取 EIP</td>
<td><a href="https://cloud.tencent.com/document/product/1199/41698">申请 EIP</a></td>
<td>申请弹性公网 IP。</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/1199/41706">普通公网 IP 转 EIP</a></td>
<td>将云服务器的普通公网 IP 转换为弹性公网 IP，转换后，弹性公网 IP 具备随时与云服务器解绑和绑定的能力，更易于实现公网 IP 的灵活管理。</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/1199/41708">找回公网 IP 地址</a></td>
<td>若您误操作释放或退还了公网 IP 地址（包含弹性公网 IP 和普通公网 IP），可以在弹性公网 IP 控制台找回，找回后的公网 IP 为弹性公网 IP。</td>
</tr>
<tr>
<td rowspan="3">绑定 EIP</td>
<td><a href="https://cloud.tencent.com/document/product/1199/41702">EIP 绑定云资源</a></td><td>将弹性公网 IP 绑定到云服务器实例、NAT 网关等云资源上，利用弹性公网 IP 灵活地容灾与提供公网通信服务等。</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/1199/43866">CVM 主网卡绑定多 IP</a></td>
<td>为单台云服务器实例绑定多个弹性公网 IP，以实现流量转移，提高云服务器的利用率。</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/1199/44153">CVM 添加辅助网卡并绑定多 IP</a></td>
<td>若单台云服务器实例可绑定公网 IP 的限额不满足您的需求，您可以通过添加辅助网卡来绑定多个公网 IP，以实现流量转移，提高云服务器的利用率。</td>
</tr>
<tr>
<td rowspan="7">管理 EIP</td>
<td><a href="https://cloud.tencent.com/document/product/1199/41709">EIP 直通</a></td>
<td>EIP 直通功能适用于云服务器内需要查看公网 IP 的场景，例如，将内网流量和外网流量分别转发到不同的 IP 地址。</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/1199/42105">查看监控数据</a></td>
<td>弹性公网 IP（EIP）的监控功能，可以帮助您通过相关监控指标（如外网入包量）实时监测流量波动情况，及时发现异常波动，调整 EIP 带宽峰值，避免因为带宽限速导致的访问延迟。</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/1199/41705">调整网络配置</a></td>
<td>弹性公网 IP 可按需调整带宽或调整计费模式，实时生效。</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/1199/44166">EIP 加入 IP 带宽包</a></td>
<td>IP 带宽包是共享带宽包的其中一种类型，详情请参见 <a href="https://cloud.tencent.com/document/product/684/15245#.E4.BA.A7.E5.93.81.E7.B1.BB.E5.88.AB">产品概述</a>。创建 IP 带宽包实例后，您需要将使用该 IP 带宽包的 EIP 添加到 IP 带宽包实例中。</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/1199/44167">EIP 移除 IP 带宽包</a></td>
<td>支持将 EIP 从 IP 带宽包 内移除，移除后，计费模式将统一变更为按流量计费。</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/1199/43137">管理 EIP 计费</a></td>
<td>根据弹性公网 IP（EIP）的计费模式的不同，可参见如下操作：<ul>
<li><a href="https://cloud.tencent.com/document/product/1199/43137#11">调整计费模式</a></li>
<li><a href="https://cloud.tencent.com/document/product/1199/43137#22">续费包月带宽 EIP</a></li>
<li><a href="https://cloud.tencent.com/document/product/1199/43137#33">退还包月带宽 EIP</a></li></ul>
</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/1199/62617">设置 ALG 功能</a></td>
<td>弹性公网 IP 支持针对 FTP 和 SIP 协议设置 ALG 功能。开启 ALG 功能后，则可对指定协议的应用层数据载荷进行 NAT 穿透。</td>
</tr>
<tr>
<td rowspan="2">解绑/释放 EIP</td>
<td><a href="https://cloud.tencent.com/document/product/1199/41703">解绑 EIP</a></td>
<td>您可以随时将弹性公网 IP 与云资源解绑，解绑后您可以将其与其他云资源重新绑定。</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/1199/41704">释放 EIP</a></td>
<td>若您不再使用弹性公网 IP，可在控制台将其释放。</td></tr>
</table>

