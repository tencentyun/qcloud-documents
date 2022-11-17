## 创建NAT网关
NAT网关可以为您私有网络内的云资源提供统一的公网访问出口。本文指导您如何创建一个公网NAT网关。
NAT网关分为传统型NAT网关和标准型NAT网关。如您申请开通了标准型NAT网关，则原小型、中型、大型NAT网关自动更名为传统型NAT网关，如未开通，则控制台只能创建传统型NAT网关，显示为NAT网关。
>?标准型NAT网关目前正在灰度测试中，如有需要，请[提交工单]()。



## 操作步骤
1. 登录[ NAT 网关控制台](https://console.cloud.tencent.com/vpc/nat?fromNav)。
2. 选择地区和私有网络，单击**新建**。
3. 在 NAT 网关购买页中按需输入或确定相关参数，根据官网指引完成购买。
<table>
<thead>
<tr>
<th>参数</th>
<th>说明</th>
</tr>
</thead>
<tbody>
<tr>
<td> 网关配置</td>
<td><ul><li>计费模式：按量计费。<li>网关类型：如您申请开通了标准型NAT网关，则可以看到标准型NAT网关和传统型NAT网关，如未开通则仅能创建传统型NAT网关。<ul><li>标准型NAT网关：目前默认规格为200万并发连接数、10万新建连接数、5Gbps带宽<li>传统型NAT网关：支持小型（最大并发连接数100万）、中型（最大并发连接数300万）、大型（最大并发连接数1000万）类型；出带宽上限支持选择：10Mbps、20Mbps、50Mbps、100Mbps、200Mbps、500Mbps、1000Mbps、2000Mbps、5000Mbps</ul><li>网关名称：自定义填写网关名称，最多输入60个字符。<li>地域：选择需要创建NAT网关所在地域。标准型NAT网关仅支持北京、上海、广州；传统型NAT网关支持所有地域。<li>可用区：仅传统型NAT网关支持选择NAT网关部署的所属可用区，该功能为白名单功能。<li>私有网络：选择私有网络。<li>子网：选择子网。<li</td>
</tr>
<tr>
<td>弹性公网 IP 配置</td>
<td>可选择绑定<strong>已有弹性公网 IP</strong> 或 <strong>新建弹性公网 IP</strong> 来配置 NAT 网关上绑定的弹性公网 IP 资源。<ul><li>已有弹性公网 IP，选择此方式时，需要该账户下有与 NAT 网关同地域的闲置 EIP 资源，通过下拉选择已有 EIP，并根据需要配置 EIP 的带宽上限。</li><li>新建弹性公网，选择此方式时，系统将自动创建按流量计费的常规 BGP IP，可按需选择新建 EIP 的数量和 EIP 带宽上限。</li></ul></td>
</tr>
<tr>
<td>其他配置</td>
<td>可选配置，可根据需要选择是否为该实例设置标签信息，如不需要可跳过。</td>
</tr>
</tbody></table>

>?	
>- 访问公网流量同时受到 NAT 网关和弹性公网 IP 的带宽上限限制，最终以较小上限值为准，请合理配置二者的出带宽上限。
>- 更多 NAT 网关相关操作，请参见 [快速入门](https://cloud.tencent.com/document/product/552/18186)。

![](https://qcloudimg.tencent-cloud.cn/raw/e6705fe25a06d151f7debdc55f4da80a.png)
![](https://qcloudimg.tencent-cloud.cn/raw/3f5d7feb0cf4cef5a0b8704bd72e3cc7.png)