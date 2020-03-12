1. 登录 [EIP 控制台](https://console.cloud.tencent.com/cvm/eip)。
2. 在 EIP 管理页面，选择需要绑定云资源的 EIP，单击【更多】>【绑定】。
>? 若绑定时，EIP 已绑定云资源，请先解绑。
>
3. 在弹出的窗口中，选择 EIP 要绑定的云资源，单击【确定】。
<table>
<thead>
<tr>
<th width="15%">绑定的云资源</th>
<th width="85%">说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>CVM 实例</td>
<td><ul><li>EIP 与 CVM 实例绑定，CVM 实例当前的普通公网 IP 会被释放。</li><li>使用 EIP 作为公网 IP，当 CVM 实例发生故障时，可解绑重新绑定到健康的 CVM 实例上，帮助快速恢复服务。</li></ul></td>
</tr>
<tr>
<td>NAT 网关</td>
<td><ul><li>EIP 与 NAT 网关绑定，利用 EIP 配置端口转发，使得云服务器上的资源可被公网访问。</li><li>当 NAT 网关绑定多个 EIP 时，系统会自动做负载均衡。</li></ul></td>
</tr>
<tr>
<td>弹性网卡</td>
<td>EIP 与弹性网卡绑定，使 EIP 成为了弹性网卡的公网 IP：
<ul><li>若绑定的弹性网卡为主网卡，该 EIP 会成为主网卡绑定的 CVM 实例的公网 IP，且 CVM 实例当前的普通公网 IP 会被释放。</li><li>若绑定的弹性网卡为辅助网卡，则辅助网卡拥有了除自身的内网 IP 外的公网 IP，您可将多个绑定了 EIP 的辅助网卡绑定到 CVM 实例上，灵活利用多个公网 IP 对外提供公网通信服务，实现高可用网络方案。</td>
</tr>
<tr>
<td>高可用虚拟 IP</td>
<td>EIP 与高可用虚拟 IP 绑定，为高可用虚拟 IP 提供了与公网通信的能力。</td>
</tr>
</tbody></table>
<img src="https://main.qcloudimg.com/raw/2e33d2036ca79f08fc2e3c7992cfe977.png" />
4. 在弹出的提示框中，单击【确定】，即可完成与云资源的绑定。
