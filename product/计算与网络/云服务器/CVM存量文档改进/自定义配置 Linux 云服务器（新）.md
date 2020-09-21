与快速配置云服务器相比，自定义配置提供您更丰富的镜像平台，以及存储、带宽以及安全组等高级设置，您可根据需求选择合适的配置。本文档以自定义配置为例进行介绍。
若您需要通过快速配置进行创建云服务器，可参考 [快速配置 Linux 云服务器](https://cloud.tencent.com/document/product/213/2936) 文档进行配置。

## 注册及认证

在使用云服务器之前，您需要完成以下准备工作：
1. 注册腾讯云账号，并完成实名认证。
新用户需在腾讯云官网进行 [注册](https://cloud.tencent.com/register?s_url=https%3A%2F%2Fcloud.tencent.com%2F)，具体操作可参考 [注册腾讯云](https://cloud.tencent.com/doc/product/378/9603)。
2. 访问 [腾讯云云服务器介绍页面](https://cloud.tencent.com/product/cvm)，单击【立即选购】。

<span id="SelectType"></span>
## 选择机型
>! 对于初次购买的账户，默认进入【快速配置】页面。对于已购买过云服务器的用户，默认进入【自定义配置】页面。若您未购买过云服务器，请选择【自定义配置】进行自定义配置操作。
>
1. 根据页面提示，配置以下信息：
![选择地域与机型](https://main.qcloudimg.com/raw/2a8b97914126cfc18d61754d3039765f.png)
<table>
<tr><th style="width: 20%">类别</th><th>配置说明</th></tr>
<tr><td>计费模式</td><td>请根据实际需求进行选择：<ul><li><b>包年包月</b>：云服务器的预付费模式，适用于提前预估设备需求量的场景，价格相较于按量计费模式更低廉。</li><li><b>按量计费</b>：云服务器的弹性计费模式，适用于电商抢购等设备需求量会瞬间大幅波动的场景，单价比包年包月计费模式高3－4倍。</li></ul></td></tr>
<tr><td>地域</td><td>建议选择与您的客户最近的地域。</td></tr>
<tr><td>可用区</td><td>如果您需要购买多台云服务器，建议选择不同可用区，实现容灾效果。</td></tr>
<tr><td>网络</td><td>腾讯云提供以下两种网络，请根据实际需求进行选择：<ul><li><b>基础网络</b>：同一用户同地域下的服务器默认内网互通，不同地域内网不通。</br>2017年6月13日后，新注册的账号已不支持基础网络，推荐您使用私有网络。</li><li><b>私有网络</b>：适合更高阶的用户，不同私有网络间逻辑隔离。</li></ul></td></tr>
<tr><td>实例</td><td>根据底层硬件的不同，腾讯云目前提供了<b>系列1</b>和<b>系列2</b>（也称为<b>上一代实例</b>和<b>当前一代实例</b>）两种不同的实例系列。<ul><li>上一代实例：标准型 S1，高 IO 型 I1，内存型 M1</li><li>当前一代实例：<a href="https://cloud.tencent.com/document/product/213/11518#S2">标准型 S2</a>，<a href="https://cloud.tencent.com/document/product/213/11518#I2">高 IO 型 I2</a>，<a href="https://cloud.tencent.com/document/product/213/11518#M2">内存型 M2</a>，<a href="https://cloud.tencent.com/document/product/213/11518#C2">计算型 C2</a>，<a href="https://cloud.tencent.com/document/product/560/11625">GPU 型 G2</a>，<a href="https://cloud.tencent.com/document/product/565/10417">FPGA 型 FX2</a> 等。为获得最佳性能，建议使用当前一代实例。</li></ul>
不同的地域与可用区下的系列、机型会有所不同，更多实例详情请参见 <a href="https://cloud.tencent.com/document/product/213/11518">实例规格</a>。</td></tr>
<tr><td>镜像</td><td>腾讯云提供公共镜像、自定义镜像、共享镜像、服务市场，您可参考 <a href="https://cloud.tencent.com/document/product/213/4941">镜像类型</a> 进行选择。
对于刚开始使用腾讯云的用户，推荐选择公共镜像。</td></tr>
<tr><td>系统盘</td><td rowspan=2>腾讯云提供以下两种类型，请根据实际需求进行设置。<ul><li><b><a href="https://cloud.tencent.com/document/product/362/2353">云硬盘</a></b>：采用一盘三备的分布式存储方式，数据可靠性高。</li><li><b>本地硬盘</b>：处在云服务器所在的物理机上的存储设备，可以获得较低的时延，但存在单点丢失风险。</li></ul>系统盘默认为50GB，数据盘默认不添加。</td></tr>
<tr><td>数据盘</td></tr>
<tr><td>公网带宽</td><td>腾讯云提供以下两种网络计费方式，请根据实际需求进行选择。<ul><li><b>按带宽计费</b>：选择固定带宽，超过本带宽时将丢包。适合网络波动较小的场景。</li><li><b>按使用流量计费</b>：按实际使用流量收费。可限制峰值带宽避免意外流量带来的费用，当瞬时带宽超过该值时将丢包。适合网络波动较大的场景。</li></ul></td></tr>
<tr><td>公共网关</td><td>公网网关是私有网络与公网的一种接口，可转发私有网络中不同子网内无外网 IP 的云服务器请求。</br>更多详情请参见 <a href="https://cloud.tencent.com/document/product/215/20078">公网网关</a>。</td></tr> 
<tr><td>数量</td><td>表示需购买云服务器的数量。</td></tr> 
<tr><td>时长</td><td>仅限包年包月的云服务器。</br>表示云服务器的使用时长。</td></tr> 
</table>
2. 单击【下一步：设置主机】，进入设置主机页面。
 
## 设置主机
1. 根据页面提示，配置以下信息：
![安全组和主机](https://main.qcloudimg.com/raw/d0594ea95229b46c5624fd0be3e9788c.png)
<table>
<tr><th style="width: 20%">类别</th><th>配置说明</th></tr>
<tr><td>所属项目</td><td>默认为默认项目，可根据实际需求，选择已建立的项目，用于管理不同的云服务器。</td></tr>
<tr><td>安全组</td><td>用于设置单台或多台云服务器的网络访问控制。</br><b>请确保已开放22登录端口</b>，更多信息请参见 <a href="https://cloud.tencent.com/document/product/213/12452">安全组</a>。</td></tr>
<tr><td>实例名称</td><td>表示需要创建的云服务器的名称。</br>用户自定义，推荐为“CVM-01”。</td></tr>
<tr><td>登录方式</td><td>设置用户登录云服务器的方式，请根据实际需求进行设置。<ul><li><b>设置密码</b>：自定义设置登录实例的密码。</li><li><b>立即关联密钥</b>：关联 SSH 密钥，通过 SSH 密钥方式可以更为安全的登录云服务器。</br>如您没有密钥或现有的密钥不合适，可以单击【现在创建】进行创建。更多 SSH 密钥信息请参见 <a href="http://cloud.tencent.com/doc/product/213/SSH%E5%AF%86%E9%92%A5">SSH 密钥</a>。</li><li><b>自动生成密码</b>：自动生成的密码将会以 <a href="https://console.cloud.tencent.com/message">站内信</a> 方式发送。</li></ul></td></tr>
<tr><td>安全加固</td><td>默认免费开通，帮助用户构建服务器安全防护体系，防止数据泄露。</td></tr>
<tr><td>云监控</td><td>默认免费开通，提供立体化云服务器数据监控、智能化数据分析、实时化故障告警和个性化数据报表配置，让用户精准掌控业务和云服务器的健康状况。</td></tr>
<tr><td>自动续费</td><td>仅限包年包月的云服务器。</br>勾选【账户余额足够时，设备到期后按月自动续费】，避免设备到期时需要进行手动续费的操作。</td></tr>
<tr><td>高级设置</td><td>根据实际需求对实例做更多配置。<ul><li><b>主机名</b>：用户可以自定义设置云服务器操作系统内部的计算机名，云服务器成功生产后可以通过登录云服务器内部查看。</li><li><b>置放群组</b>：根据需要可以将实例添加到置放群组中，提高业务的可用性。具体可参考 <a href="https://cloud.tencent.com/document/product/213/15486">置放群组</a> 进行设置。</li><li><b>标签</b>：设置标签之后可以对云服务器实现资源的分类管理。具体可参考 <a href="https://cloud.tencent.com/document/product/213/19548">标签</a> 进行设置。</li><li><b>自定义数据</b>：指定自定义数据来配置实例，既当实例启动时运行配置的脚本。如果一次购买多台云服务器，自定义数据会在所有的云服务器上运行。Linux 操作系统支持 Shell 格式，最大支持 16KB 原始数据。具体可参考 <a href="https://cloud.tencent.com/document/product/213/17525">自定义数据</a>。</br><b>注意</b>：自定义数据配置仅支持部分带 Cloudinit 服务的公有镜像，具体可参考 <a href="https://cloud.tencent.com/document/product/213/19670">Cloud-Init</a>。</li></ul></td></tr>
</table>
2. 单击【下一步：确认配置信息】，进入确认配置信息页面。


## 确认配置信息

1. 核对购买的云服务器信息。
2. 勾选【同意《退款规则》】（仅限包年包月的云服务器）。
3. 单击【立即购买】，完成支付。当您付款完成后，即可进入 [云服务器控制台](https://console.cloud.tencent.com/cvm) 查收您的云服务器。
云服务器的实例名称、公网 IP 地址、内网 IP 地址、登录名、初始登录密码等信息将以 [站内信](https://console.cloud.tencent.com/message) 的方式发送到账户上。您可以使用这些信息登录和管理实例，也请尽快更改您的 Linux 登录密码保障主机安全性。

## 登录及连接实例

当您完成云服务器操作后，您可以尝试通过腾讯云控制台登录您的云服务器，并根据您的实际需求，进行建站等操作。
关于如何通过腾讯云控制台登录云服务器，请根据实际需求，选择相应的登录方式：
- [使用标准登录方式登录 Linux 实例（推荐）](https://cloud.tencent.com/document/product/213/5436)
- [使用远程登录软件登录 Linux 实例](https://cloud.tencent.com/document/product/213/35699)
- [使用 SSH 登录 Linux 实例](https://cloud.tencent.com/document/product/213/35700)

## 数据盘分区及格式化

如果您在 [选择机型](#SelectType) 时，添加了数据盘，则需要在登录实例后对数据盘进行格式化和分区。**如果您未添加数据盘，则可跳过此步骤。**
请根据磁盘容量大小、云服务器操作系统类型选择合适的操作指引：
- 磁盘容量小于2TB时：
 [初始化云硬盘（Linux）](https://cloud.tencent.com/document/product/362/6734#Linux)
- 磁盘容量大于等于2TB时：
 [初始化云硬盘（Linux）](https://cloud.tencent.com/document/product/362/6735#2TBLinux)

更多操作指引请参见 [初始化场景介绍](https://cloud.tencent.com/document/product/362/33065)。
