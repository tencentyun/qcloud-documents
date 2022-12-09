>?
>- IPv6 负载均衡内测中，如需使用，请提 [工单申请](https://console.cloud.tencent.com/workorder/category?level1_id=6&level2_id=163&source=0&data_title=%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1%20LB&step=1)。
>- 目前仅支持如下地域开通 IPv6 负载均衡：广州、深圳金融、上海、上海金融、南京、北京、北京金融、成都、重庆、香港、新加坡、弗吉尼亚。其中，针对地域为**深圳金融**、**上海金融**的金融行业监管要求定制的合规专区，需提交 [工单申请](https://console.cloud.tencent.com/workorder/category) 使用专区。
>- IPv6 负载均衡不支持传统型负载均衡。
>- IPv6 负载均衡支持获取客户端 IPv6 源地址。四层 IPv6 负载均衡支持直接获取客户端 IPv6 源地址，七层 IPv6 负载均衡支持通过 HTTP 的 X-Forwarded-For 头域获取客户端 IPv6 源地址。
>- 当前 IPv6 负载均衡是纯公网负载均衡，相同 VPC 的客户端无法通过内网访问该 IPv6 负载均衡。
>- 互联网 IPv6 网络大环境还处于建设初期，如出现线路访问不通的情况，请 [提交工单](https://console.cloud.tencent.com/workorder/category?level1_id=6&level2_id=163&source=0&data_title=%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1%20LB&step=1) 反馈，另外在内测期间，不提供 SLA 保障。
>


## 概述
IPv6 负载均衡是基于 IPv6 单栈技术实现的负载均衡，和 IPv4 负载均衡协同工作，实现 IPv6/IPv4 双栈通信。IPv6 负载均衡绑定的是云服务器的 IPv6 地址，并对外提供 IPv6 VIP 地址。

### IPv6 负载均衡优势
腾讯云 IPv6 负载均衡在助力业务快速接入 IPv6 时具有如下优势：
- 快速接入：秒级接入 IPv6，随买随用快速上线。
- 易于使用：IPv6 负载均衡兼容原 IPv4 负载均衡的操作流程，零学习成本，低门槛使用。
- 端到端的 IPv6 通信：IPv6 负载均衡和云服务器之间通过 IPv6 通信，可以帮助部署在云服务器的应用快速进行 IPv6 改造，并实现端到端的 IPv6 通信。

### IPv6 负载均衡架构
负载均衡支持创建 IPv6 负载均衡（下文中也叫 IPv6 CLB）实例，腾讯云会给 IPv6 CLB 实例分配一个 IPv6 公网地址（即 IPv6 版的 VIP），该 VIP 会将来自 IPv6 客户端的请求转发给后端的 IPv6 云服务器。

IPv6 CLB 实例不但可以快速接入 IPv6 公网用户访问，且通过 IPv6 协议和后端云服务器进行通信，能够帮助云上的应用快速改造 IPv6，并实现端到端的 IPv6 通信。

IPv6 负载均衡的架构如下图所示：
![](https://main.qcloudimg.com/raw/ca444992408e16390a46a3e2d9239bf5.svg)


## 步骤一：创建 IPv6 负载均衡实例
1. 登录腾讯云官网，进入 [负载均衡购买页](https://buy.cloud.tencent.com/lb)。
2. 按需选择以下负载均衡相关配置。
<dx-accordion>
::: 标准账户类型
<table>
<thead>
<tr>
<th width="18%">参数</th>
<th width="82%">说明</th>
</tr>
</thead>
<tbody>
<tr>
<td><span style="font-weight:bold">计费模式</span></td>
<td>
支持包年包月和按量计费两种计费模式。仅按量计费模式支持 IPv6 版本，其余限制情况请参见 <a href="https://cloud.tencent.com/document/product/214/33415#IP-type">IP 版本</a>。
</td>
</tr>
<tr>
<td><span style="font-weight:bold">地域</span></td>
<td>
选择所属地域。CLB 支持的地域详情请参见 <a href="https://cloud.tencent.com/document/product/214/30670#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8">地域列表</a>。
</td>
</tr>
<tr>
<td><span style="font-weight:bold">实例类型</span></td>
<td>
仅支持负载均衡实例类型。自2021年10月20日起停止购买传统型负载均衡，详情请参见 <a href="https://cloud.tencent.com/document/product/214/58185">传统型负载均衡停售公告</a>。
</td>
</tr>
<tr>
<td><span style="font-weight:bold">网络类型</span></td>
<td>网络类型分为公网和内网两种类型，详情请参见 <a href="https://cloud.tencent.com/document/product/214/33415#network-type">网络类型</a>。IPv6 负载均衡需选择公网类型。
</td>
</tr>
<tr>
<td><span style="font-weight:bold">弹性公网 IP</span></td>
<td>
	不选择弹性公网 IP。
</td>
</tr>
<tr>
<td><span style="font-weight:bold">IP 版本</span></td>
<td>
选择 IPv6 版本。
</td>
</tr>
<tr>
<td><span style="font-weight:bold">所属网络</span></td>
<td>
选择所属网络，请选择已获取的私有网络和子网。若现有的网络不合适，可 <a href="https://cloud.tencent.com/document/product/215/36515">新建私有网络</a> 或 <a href="https://cloud.tencent.com/document/product/215/36517">新建子网</a>。
</td>
</tr>
<tr>
<td><span style="font-weight:bold">运营商类型</span></td>
<td>
运营商类型为 BGP。
</td>
</tr>
<tr>
<td><span style="font-weight:bold">实例规格</span></td>
<td>支持共享型实例和性能容量型实例。
	<ul>
	<li>共享型实例中多个实例共享资源，单实例不提供可保障的性能指标。默认情况下所有实例均为共享型实例。</li>
	<li>性能容量型实例提供性能保障，无共享实例互相抢占资源，转发性能不受其它实例的影响，单实例最大可支持100万并发连接数，新建连接数10万，每秒查询数5万。目前性能容量型实例处于内测中，如需使用，请提交 <a href="https://cloud.tencent.com/apply/p/hf45esx99lf">内测申请</a>。</li>
	</ul>
</td>
</tr>
<tr>
<td><span style="font-weight:bold">双栈混绑</span></td>
<td>
启用后，该负载均衡实例的七层监听器可以同时绑定 IPv4 和 IPv6的后端服务器，四层监听器不支持混绑，只能绑定 IPv6 的后端服务器。
</td>
</tr>
<tr>
<td><span style="font-weight:bold">网络计费模式</span></td>
<td>网络计费模式分为：按流量、共享带宽包。
</td>
</tr>
<tr>
<td><span style="font-weight:bold">带宽上限</span></td>
<td>1-2048Mbps。
</td>
</tr>
<tr>
<td><span style="font-weight:bold">所属项目</span></td>
<td>选择所属项目。
</td>
</tr>
<tr>
<td><span style="font-weight:bold">标签</span></td>
<td>选择标签键和标签值，也可选择新建标签，详情请参见 <a href="https://cloud.tencent.com/document/product/651/56731">创建标签</a>。
</td>
</tr>
<tr>
<td><span style="font-weight:bold">实例名</span></td>
<td>可输入60个字符，允许英文字母、数字、中文字符、“-”、“_”、“.”。不填写时默认自动生成。
</td>
</tr>
<tr>
<td><span style="font-weight:bold">服务协议</span></td>
<td>勾选“我已阅读并同意<a href="https://cloud.tencent.com/document/product/301/1967">《腾讯云服务协议》</a>和<a href="https://cloud.tencent.com/document/product/214/35156">《负载均衡CLB服务等级协议》</a>”。
</td>
</tr>
</tbody></table>
:::
::: 传统账户类型
<table>
<thead>
<tr>
<th width="18%">参数</th>
<th width="82%">说明</th>
</tr>
</thead>
<tbody>
<tr>
<td><span style="font-weight:bold">计费模式</span></td>
<td>
仅支持按量计费模式。
</td>
</tr>
<tr>
<td><span style="font-weight:bold">地域</span></td>
<td>
选择所属地域。CLB 支持的地域详情请参见 <a href="https://cloud.tencent.com/document/product/214/30670#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8">地域列表</a>。
</td>
</tr>
<tr>
<td><span style="font-weight:bold">实例类型</span></td>
<td>
仅支持负载均衡实例类型。自2021年10月20日起停止购买传统型负载均衡，详情请参见 <a href="https://cloud.tencent.com/document/product/214/58185">传统型负载均衡停售公告</a>。
</td>
</tr>
<tr>
<td><span style="font-weight:bold">网络类型</span></td>
<td>网络类型分为公网和内网两种类型，详情请参见 <a href="https://cloud.tencent.com/document/product/214/33415#network-type">网络类型</a>。
	<ul>
	<li>公网：使用负载均衡分发来自公网的请求。</li>
	<li>内网：使用负载均衡分发来自腾讯云内网的请求。内网不支持配置以下的 <strong>IP 版本</strong>、<strong>运营商类型</strong>、<strong>实例规格</strong>，默认不显示这些配置项。</li>
	</ul>
</td>
</tr>
<tr>
<td><span style="font-weight:bold">IP 版本</span></td>
<td>
选择 IPv6 版本。使用限制详情请参见 <a href="https://cloud.tencent.com/document/product/214/33415#IP-type">IP 版本</a>。
</td>
</tr>
<tr>
<td><span style="font-weight:bold">所属网络</span></td>
<td>
负载均衡支持的所属网络分为基础网络和私有网络。
	<ul>
	<li>基础网络是腾讯云上所有用户的公共网络资源池，所有云服务器的内网 IP 地址都由腾讯云统一分配，无法自定义网段划分、IP 地址。</li>
	<li>私有网络是用户在腾讯云上建立的一块逻辑隔离的网络空间，在私有网络内，用户可以自由定义网段划分、IP 地址和路由策略。</li>
	</ul>
	两者相比，私有网络较基础网络更适合有网络自定义配置需求的场景，且基础网络产品整体将于2022年12月31日正式下线，详情请参见 <a href="https://cloud.tencent.com/document/product/215/63349">基础网络下线通知</a>。建议您选择私有网络。
</td>
</tr>
<tr>
<td><span style="font-weight:bold">运营商类型</span></td>
<td>
运营商类型为 BGP。
</td>
</tr>
<tr>
<td><span style="font-weight:bold">实例规格</span></td>
<td>支持共享型实例和性能容量型实例。
	<ul>
	<li>共享型实例中多个实例共享资源，单实例不提供可保障的性能指标。默认情况下所有实例均为共享型实例。</li>
	<li>性能容量型实例提供性能保障，无共享实例互相抢占资源，转发性能不受其它实例的影响，单实例最大可支持100万并发连接数，新建连接数10万，每秒查询数5万。目前性能容量型实例处于内测中，如需使用，请提交 <a href="https://cloud.tencent.com/apply/p/hf45esx99lf">内测申请</a>。</li>
	</ul>
</td>
</tr>
<tr>
<td><span style="font-weight:bold">网络计费模式</span></td>
<td>网络计费模式为共享带宽包。
</td>
</tr>
<tr>
<td><span style="font-weight:bold">带宽上限</span></td>
<td>1-1024Mbps。
</td>
</tr>
<tr>
<td><span style="font-weight:bold">所属项目</span></td>
<td>选择所属项目。
</td>
</tr>
<tr>
<td><span style="font-weight:bold">标签</span></td>
<td>选择标签键和标签值，也可选择新建标签，详情请参见 <a href="https://cloud.tencent.com/document/product/651/56731">创建标签</a>。
</td>
</tr>
<tr>
<td><span style="font-weight:bold">实例名</span></td>
<td>可输入60个字符，允许英文字母、数字、中文字符、“-”、“_”、“.”。不填写时默认自动生成。
</td>
</tr>
<tr>
<td><span style="font-weight:bold">服务协议</span></td>
<td>勾选“我已阅读并同意<a href="https://cloud.tencent.com/document/product/301/1967">《腾讯云服务协议》</a>和<a href="https://cloud.tencent.com/document/product/214/35156">《负载均衡CLB服务等级协议》</a>”。
</td>
</tr>
</tbody></table>
:::
</dx-accordion>
3. 在购买页选择各项配置后，单击**立即购买**。在“负载均衡订单确认”弹出窗口中，单击**确认订单**。返回至 [负载均衡实例列表页](https://console.cloud.tencent.com/loadbalance/index?rid=1&forward=1)，即可查看已购的 IPv6 负载均衡。


## 步骤二：创建 IPv6 负载均衡监听器
1. 登录 [负载均衡控制台](https://console.cloud.tencent.com/clb/index?rid=1&type=2%2C3)，单击 IPv6 负载均衡实例 ID，进入详情页。
2. 选择**监听器管理**标签页，单击**新建**，如创建一个 TCP 监听器。
>?支持创建四层 IPv6 负载均衡监听器（TCP/UDP/TCP SSL）和七层 IPv6 负载均衡监听器（HTTP/HTTPS），详情请参见 [负载均衡监听器概述](https://cloud.tencent.com/document/product/214/6151)。
>
3. 在“基本配置”中配置名称、监听协议端口和均衡方式，单击**下一步**。
![](https://main.qcloudimg.com/raw/815c00aa93b5f23408bd78791ea5b7c3.png)
4. 配置健康检查，单击**下一步**。
![](https://main.qcloudimg.com/raw/19fbf68edcb9d4f06102ae61c2228b67.png)
5. 配置会话保持，单击**提交**。
![](https://main.qcloudimg.com/raw/9743537a93828dc8c0c10e6c943f7673.png)
6. 监听器创建完成后，选中该监听器，在右侧单击**绑定**。
>?绑定云服务器前，请确定该云服务器已获取 IPv6 地址。
>
![](https://main.qcloudimg.com/raw/edf72af61361da4f833f2424a548040e.png)
7. 在弹出框中，选择需要通信的 IPv6 云服务器，并配置服务端口和权重，单击**确定**即可。
![](https://main.qcloudimg.com/raw/7eb363ea3170bbe7a881762be7968210.png)

## 更多操作
### IPv6 CLB 混绑 IPv6 和 IPv4 后端服务
开启双栈混绑后，IPv6 CLB 七层监听器，可以同时绑定 IPv6 和 IPv4 的后端云服务器，并支持从 XFF 中获取源 IP。IPv6 CLB 四层监听器不支持混绑，只能绑定 IPv6 的后端服务器。
1. 开启双栈混绑。
 -  在购买页购买 IPv6 CLB 时，启用双栈混绑。
![](https://qcloudimg.tencent-cloud.cn/raw/8bc32792b917d025ab23d5a0b7e628b6.png)
 -  在 IPv6 CLB 实例详情页面，启用双栈混绑。
 ![](https://qcloudimg.tencent-cloud.cn/raw/c9d35237274832c1fd7e9050f8c05e6d.png)
2. 创建七层 HTTP 或 HTTPS 监听器。
3. 选择绑定 IPv6 或 IPv4 类型的后端服务。
![](https://qcloudimg.tencent-cloud.cn/raw/7e5eab550ecf10307ec24fdb7d20d840.png)

## 相关文档
[购买云服务器并配置云服务器的 IPv6](https://cloud.tencent.com/document/product/215/47557#.E6.AD.A5.E9.AA.A4.E4.B8.89.EF.BC.9A.E8.B4.AD.E4.B9.B0.E4.BA.91.E6.9C.8D.E5.8A.A1.E5.99.A8.E5.B9.B6.E9.85.8D.E7.BD.AE.E4.BA.91.E6.9C.8D.E5.8A.A1.E5.99.A8.E7.9A.84-ipv6.3Ca-id.3D.22step3.22.3E.3C.2Fa.3E)


