下面将为您介绍在官网购买 NAT 网关的具体操作。


## 操作步骤
### 标准型 NAT 网关
>?标准型 NAT 网关正在灰度测试中，目前支持北京、上海、广州、成都、重庆，如需使用，请提交 [内测申请](https://cloud.tencent.com/apply/p/ojxjirnd5yi)。
>
1. 登录[ NAT 网关控制台](https://console.cloud.tencent.com/vpc/nat?fromNav)。
2. 选择地区和私有网络，单击**新建**。
3. 在 NAT 网关购买页中按需输入或确定相关参数，根据官网指引完成购买。
![](https://qcloudimg.tencent-cloud.cn/raw/e6705fe25a06d151f7debdc55f4da80a.png)
<table>
<thead>
<tr>
<th width="14%">参数</th>
<th>说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>网关配置</td>
<td><ul><li>计费模式：按量计费。</li><li>网关类型：选择标准型 NAT 网关，默认规格为200万并发连接数、10万新建连接数、5Gbps带宽。<li>网关名称：按需输入 NAT 网关名称，支持60个字符。</li><li>地域：选择 NAT 网关所属地域，当前标准型 NAT 网关仅支持北京、上海、广州、成都、重庆。</li><li>私有网络：选择 NAT 网关所属的私有网络。</li><li>所属子网：选择子网。</li></ul></td>
</tr>
<tr>
<td>弹性公网 IP 配置</td>
<td>有两种方式来配置 NAT 网关上绑定的弹性公网 IP 资源。<ul><li>已有弹性公网 IP：选择此方式时，需要该账户下有与 NAT 网关同地域的闲置 EIP 资源，通过下拉选择已有 EIP，并根据需要配置 EIP 的带宽上限。</li><li>新建弹性公网：选择此方式时，系统将自动创建按流量计费的常规 BGP IP，可按需选择新建 EIP 的数量和 EIP 带宽上限。</li></ul></td>
</tr>
<tr>
<td>其他配置</td>
<td>可选配置，可根据需要选择是否为该实例设置标签信息，如不需要可跳过。</td>
</tr>
</tbody></table>


### 传统型 NAT 网关
>?原小型、中型、大型 NAT 网关已更名为传统型 NAT 网关-小型、传统型 NAT 网关-中型、传统型 NAT 网关-大型，详情请参见 [NAT 网关类型更名公告](https://cloud.tencent.com/document/product/552/83165)。
>
1. 登录[ NAT 网关控制台](https://console.cloud.tencent.com/vpc/nat?fromNav)。
2. 选择地区和私有网络，单击**新建**。
3. 在 NAT 网关购买页中按需输入或确定相关参数，根据官网指引完成购买。
<table>
<thead>
<tr>
<th width="14%">参数</th>
<th>说明</th>
</tr>
</thead>
<tbody>
<tr>
<td> 网关配置</td>
<td><ul><li>计费模式：按量计费。</li><li>网关类型：<ul><li>小型（最大100万连接数）</li><li>中型（最大300万连接数）</li><li>大型（最大1000万连接数）</li></ul><li>出带宽上限：NAT 网关的最大出带宽上限，可选值有（单位：Mbps）：10，20，50，100，200，500，1000， 2000，5000。<li>网关名称：按需输入 NAT 网关名称，支持60个字符。</li><li>地域：选择 NAT 网关所属地域。</li><li>私有网络：选择 NAT 网关所属的私有网络。</li><li>所属子网：选择子网。</li></ul></td>
</tr>
<tr>
<td>弹性公网 IP 配置</td>
<td>有两种方式来配置 NAT 网关上绑定的弹性公网 IP 资源。<ul><li>已有弹性公网 IP：选择此方式时，需要该账户下有与 NAT 网关同地域的闲置 EIP 资源，通过下拉选择已有 EIP，并根据需要配置 EIP 的带宽上限。</li><li>新建弹性公网：选择此方式时，系统将自动创建按流量计费的常规 BGP IP，可按需选择新建 EIP 的数量和 EIP 带宽上限。</li></ul></td>
</tr>
<tr>
<td>其他配置</td>
<td>可选配置，可根据需要选择是否为该实例设置标签信息，如不需要可跳过。</td>
</tr>
</tbody></table>
<dx-alert infotype="explain" title="">
访问公网流量同时受到 NAT 网关和弹性公网 IP 的带宽上限限制，最终以较小上限值为准，请合理配置二者的出带宽上限。
</dx-alert>
