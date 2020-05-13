<head><link rel="stylesheet" href="https://doc-archer-1255486055.cos.ap-nanjing.myqcloud.com/archer.css"></head>
您可将弹性公网 IP（EIP）绑定到 CVM 实例、NAT 网关等云资源上，利用 EIP 灵活地容灾与提供公网通信服务等。

## 操作场景
- EIP 与 CVM 实例绑定，EIP 作为 CVM 实例的公网 IP，当 CVM 实例发生故障时，可解绑重新绑定到健康的 CVM 实例上，帮助快速恢复服务。
- EIP 与 NAT 网关绑定，利用 EIP 配置端口转发，使得云服务器上的资源可被公网访问。
- EIP 与 弹性网卡内网 IP 绑定，并将弹性网卡绑定到 CVM 实例上，为 CVM 实例提供公网通信服务。
- EIP 与高可用虚拟 IP 绑定，通过高可用虚拟 IP 搭建高可用主备集群，快速恢复故障的公网通信服务。

## 操作步骤
1. 登录 [EIP 控制台](https://console.cloud.tencent.com/cvm/eip)。
2. 在 EIP 管理页面，选择需要绑定云资源的 EIP 的地域，并在对应 EIP 的操作栏下，单击【更多】>【绑定】。
>? 若绑定时，EIP 已绑定云资源，请先解绑，例如，需更换故障 CVM 实例的 EIP 到健康的 CVM 实例上。
>
3. 在弹出的“绑定资源”窗口中，选择 EIP 要绑定的云资源，单击【确定】。
<div class="codetab">
 <input type="radio" name="tabs" id="tab1" class="tab-switch" checked>
<label for="tab1" class="tab-label">非带宽上移账户</label>
<input type="radio" name="tabs" id="tab2" class="tab-switch">
 <label for="tab2" class="tab-label">带宽上移账户</label>
<div id="tab-content1" class="tab-content" style="padding:0 10px;">
<p>
<table>
<thead>
<tr>
<th width="17%">绑定的云资源</th>
<th width="83%">说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>CVM 实例</td>
<td><ul>
<li>EIP 与 CVM 实例绑定，该 CVM 实例需未绑定其他 EIP ，若已有普通公网 IP，则绑定 EIP 后会释放当前 CVM 实例的普通公网 IP。</li>
<li>EIP 与 CVM 实例需处于<strong>相同地域</strong>才可进行绑定。</li>
<li>EIP 绑定 CVM 实例的数量限制，根据 CVM 实例 CPU 配置的差异有所不同，请参见 <a href="https://cloud.tencent.com/document/product/1199/41648">使用限制</a>。</li>
</ul></td>
</tr>
<tr>
<td>NAT 网关</td>
<td><ul>
<li>EIP 与 NAT 网关需处于<strong>相同地域</strong>才可进行绑定。</li>
<li>一个 NAT 网关最多可绑定10个 EIP。</li>
<li>当 NAT 网关绑定多个 EIP 时，系统会自动做负载均衡。</li></ul></td>
</tr>
<tr>
<td>弹性网卡</td>
<td>EIP 可与未绑定其他 EIP 的弹性网卡内网 IP 进行绑定：<ul>
<li>一个 EIP 仅可绑定一个弹性网卡内网 IP。</li>
<li>EIP 绑定主网卡内网 IP 时，若主网卡绑定的 CVM 实例的已有普通公网 IP，则主网卡内网 IP 绑定 EIP 后 CVM 实例当前的普通公网 IP 会被释放。</li>
<li>EIP 与 辅助网卡内网 IP 绑定时，则辅助网卡拥有了除自身的内网 IP 外的公网 IP，您可将多个绑定了 EIP 的辅助网卡绑定到 CVM 实例上，灵活利用多个公网 IP 对外提供公网通信服务，实现高可用网络方案。</td>
</tr>
<tr>
<td>高可用虚拟 IP</td>
<td>EIP 与高可用虚拟 IP 绑定，为高可用虚拟 IP 提供了与公网通信的能力。</td>
</tr>
</tbody></table>
</p>
</div>
 <div id="tab-content2" class="tab-content" style="padding:0 10px;">
<p><table>
<thead>
<tr>
<th width="15%">绑定的云资源</th>
<th width="85%">说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>CVM 实例</td>
<td><ul>
<li>EIP 与 CVM 实例绑定，该 CVM 实例需未绑定其他 EIP 和未分配普通公网 IP。</li>
<li>EIP 与 CVM 实例需处于<strong>相同地域</strong>才可进行绑定。</li>
<li>EIP 绑定 CVM 实例的数量限制，根据 CVM 实例 CPU 配置的差异有所不同，请参见 <a href="https://cloud.tencent.com/document/product/1199/41648">使用限制</a>。</li>
</ul></td>
</tr>
<tr>
<td>NAT 网关</td>
<td><ul>
<li>EIP 与 NAT 网关需处于<strong>相同地域</strong>才可进行绑定。</li>
<li>一个 NAT 网关最多可绑定10个 EIP。</li>
<li>当 NAT 网关绑定多个 EIP 时，系统会自动做负载均衡。</li></ul></td>
</tr>
<tr>
<td>弹性网卡</td>
<td>EIP 可与未绑定其他 EIP 的弹性网卡内网 IP 进行绑定：<ul>
<li>一个 EIP 仅可绑定一个弹性网卡内网 IP。</li>
<li>EIP 绑定主网卡内网 IP 时，该主网卡绑定的 CVM 实例需未分配普通公网 IP。</li>
<li>EIP 与 辅助网卡内网 IP 绑定时，则辅助网卡拥有了除自身的内网 IP 外的公网 IP，您可将多个绑定了 EIP 的辅助网卡绑定到 CVM 实例上，灵活利用多个公网 IP 对外提供公网通信服务，实现高可用网络方案。</td>
</tr>
<tr>
<td>高可用虚拟 IP</td>
<td>EIP 与高可用虚拟 IP 绑定，为高可用虚拟 IP 提供了与公网通信的能力。</td>
</tr>
</tbody></table>
</p></div>
</div>
<img src="https://main.qcloudimg.com/raw/a68a2aa1e681dd3bed4c054942aba27a.png" />
4. 在弹出的提示框中，单击【确定】，即可完成与云资源的绑定。

## 后续步骤
- 若需要为 EIP 解绑云资源，请参见 [EIP 解绑云资源](https://cloud.tencent.com/document/product/1199/41703)。
- 若需要调整 EIP 的带宽峰值，请参见 [调整带宽](https://cloud.tencent.com/document/product/1199/41705)。
- 若需要监控 EIP 的流量波动情况，请参见 [查看监控数据](https://cloud.tencent.com/document/product/1199/42105)。
