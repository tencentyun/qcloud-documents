## 私有网络 VPC 定价

- VPN 网关定价
VPN 网关提供包年包月计费模式，单价已包含 IDC 带宽费用，云主机无需重复购买网络带宽。
 
- NAT 网关定价
NAT 网关提供按网关租用和按流量使用两种计费模式，其中流量使用费仅计算从 NAT 网关流向 Internet 单向流量。

- 跨地域对连接定价
按天后付费日结，由对等连接发起方支付。
计算双方出流量当日带宽峰值，乘以所在阶梯的单价。
带宽峰值计算方式：每5分钟采集一次，取当日最大值作为每日带宽峰值

### 免费套餐

- 私有网络、子网、路由表、网络ACL、安全组的使用免费。
- 内网通信免费，即不同子网中实例间通信不需要支持带宽费用。
- 云服务在私有网络中价格与基础网络中保持一致，不额外收取费用。如云主机、云数据库等
- 同地域对等连接免费。

### 定价详情

<table class="cvmMonth">
<tr>

<th style="width: 10%;" rowspan="2">功能</th>

<th style="width: 10%;" rowspan="2">计费模式</th>

<th style="width: 30%;" rowspan="2">配置</th>

<th style="width: 50%;" colspan="4">价格</th>

</tr>


<tr>

<th>北京<br>上海<br>上海金融<br>广州<br>深圳金融</th>

<th>中国香港</th>

<th>新加坡</th>

<th>多伦多</th>

</tr>


<tr>
<td>自定义私有网络</td>
<td colspan="6" rowspan="3" align="center">免费</td>
</tr>

<tr>
<td>自定义子网</td>
</tr>

<tr>
<td>自定义路由</td>
</tr>



<tr>

<td rowspan="5">VPN网关</td>

<td rowspan="5">包年包月按带宽付费<br>（元/月）</td>

<td>5Mbps</td>

<td>380</td>

<td>380</td>

<td>380</td>

<td>480</td>

</tr>


<tr>

<td>10Mbps</td>
<td>880</td>

<td>880</td>

<td>880</td>

<td>1330</td>

</tr>


<tr>

<td>20Mbps</td>

<td>1880</td>

<td>1880</td>

<td>1880</td>

<td>2330</td>

</tr>



<tr>

<td>50Mbps</td>

<td>4880</td>

<td>4880</td>

<td>4880</td>

<td>5330</td>

</tr>


<tr>

<td>100Mbps</td>

<td>9880</td>

<td>9880</td>

<td>9880</td>

<td>10330</td>

</tr>


<tr>

<td rowspan="4">NAT网关</td>

<td rowspan="3">网关租用费<br>（元/小时）</td>

<td>小型</td>

<td>0.5</td>

<td>0.75</td>

<td>0.75</td>

<td>0.8</td>

</tr>


<tr>

<td>中型</td>

<td>1.5</td>

 <td>2.25</td>

 <td>2.25</td>

 <td>2.4</td>

</tr>


<tr>

<td>大型</td>

<td>5</td>

<td>7.5</td>

<td>7.5</td>

<td>8</td>

</tr>


<tr>
<td colspan="2">流量使用费用（仅计算从NAT网关流向Internet单向流量）<br>（元/GB）</td>

<td>0.8</td>

<td>1.0</td>

<td>0.8</td>

<td>0.5</td>

</tr>
<tr>

<td>同地域对等连接</td>

<td colspan="6" rowspan="1" align="center">免费</td>

</tr>

<tr>

<td rowspan="5">跨地域对等连接</td>

<td rowspan="5">带宽峰值（出 max + 入 max）<br><br>按天计费（元 / Mbps / 天）<br><br>峰值带宽按每 5min 平均带宽计<br></td>
                        <td>0Mbps - 20Mbps</td>

<td>20</td>

<td>120</td>

<td>120</td>

<td>120</td>

</tr>



<tr>

<td>20Mbps - 100Mbps</td>

<td>12</td>

<td>80</td>

<td>80</td>

<td>80</td>

</tr>
<tr>
<td>100Mbps - 500Mbps</td>
<td colspan="4" rowspan="3">请与商务洽谈<br><br></td>
</tr>
<tr>
<td>500Mbps - 2000Mbps</td>
</tr>
<tr>
<td >大于2000Mbps</td>
</tr>
</table>

## 购买指导

### 控制台购买

划分网段、设定路由、购买VPN网关搭建通道等一系列操作均可通过控制台进行。

### API 购买

详情请参见 [私有网络API](http://cloud.tencent.com/doc/api/245/%E7%AE%80%E4%BB%8B)

## 到期提醒

### VPN 网关

- 从 VPN 到期时刻起，VPN 网关仍然可以继续使用7天。此期间您可以续费 VPN 网关，新的有效期将基于上一次到期时间进行计算，即您需要支付欠费期间 VPN 网关的使用费用。

- VPN 网关欠费超过7天后将自动销毁，路由表中所有与此 VPN 网关的关联项将一并销毁。

### NAT网关

- 当您的账户余额不足。从余额为0的时刻开始，2小时内 NAT 网关可继续使用且继续扣费。

- 2小时后，若您的账户仍未充值，NAT 网关将自动停止服务并停止扣费。

- NAT 网关停止服务后的24小时内，若您的账户余额仍未充值到大于0，则保持为不可用状态；若充值到余额大于0，则网关重新可用，且计费重新开始。
 
- NAT 网关停止服务后，余额小于0的时间达到24小时，NAT 网关将被立即回收。

- NAT 网关回收时，我们将通过邮件及短信的方式通知到腾讯云账户的创建者以及所有协作者。

### 跨地域对等连接

- 当您的账户余额不足，从余额为0的时刻开始，跨地域对等连接可继续使用7天且继续扣费。

- 若您的账户仍未充值到大于0，7天后跨地域对等连接的带宽上限将变为0（此时连接不可用），且停止扣费。

- 当充值且账户余额大于0后，跨地域对等连接带宽上限将恢复用户设置值，且恢复可用。
