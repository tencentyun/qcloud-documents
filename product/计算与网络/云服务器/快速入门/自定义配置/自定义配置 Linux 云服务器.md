与快速配置云服务器相比，自定义配置提供您更丰富的镜像平台，以及存储、带宽以及安全组等高级设置，您可根据需求选择合适的配置。本文档以自定义配置为例进行介绍。
若您需要通过快速配置进行创建云服务器，可参考 [快速配置 Linux 云服务器](https://cloud.tencent.com/document/product/213/2936) 文档进行配置。

## 注册及认证

在使用云服务器之前，您需要完成以下准备工作：
1. 注册腾讯云账号，并完成实名认证。
新用户需在腾讯云官网进行 [注册](https://cloud.tencent.com/register?s_url=https%3A%2F%2Fcloud.tencent.com%2F)，具体操作可参考 [注册腾讯云](https://cloud.tencent.com/doc/product/378/9603)。
2. 访问 [腾讯云云服务器介绍页面](https://cloud.tencent.com/product/cvm)，单击**立即选购**。


## 选择机型[](id:SelectType)

<dx-alert infotype="notice" title="">
对于初次购买的账户，默认进入**快速配置**页面。对于已购买过云服务器的用户，默认进入**自定义配置**页面。若您未购买过云服务器，请选择**自定义配置**进行自定义配置操作。
</dx-alert>

1. 根据页面提示，配置以下信息：
![选择地域与机型](https://main.qcloudimg.com/raw/076bc1df02669264d96b440d254ba776.png)
<table>
<tr><th style="width: 20%">类别</th><th style="width: 12%">必选/可选</th><th>配置说明</th></tr>
<tr><td><a href="https://cloud.tencent.com/document/product/213/2180">计费模式</a></td><td>必选</td><td>请根据实际需求进行选择：<ul><li><b>包年包月</b>：云服务器的预付费模式，适用于提前预估设备需求量的场景，价格相较于按量计费模式更低廉。</li><li><b>按量计费</b>：云服务器的弹性计费模式，适用于电商抢购等设备需求量会瞬间大幅波动的场景，单价比包年包月计费模式高3－4倍。</li><li><b>竞价实例</b>：一种新实例运作模式，适用于大数据计算、采用负载均衡的在线服务和网站服务等场景，一般价格区间为按量付费的10% - 20%。</li></ul></td></tr>
<tr><td>地域</td><td>必选</td><td>建议选择与您的客户最近的地域，可降低访问时延、提高访问速度。</td></tr>
<tr><td>可用区</td><td>必选</td><td>请根据实际需求进行选择。</br>如果您需要购买多台云服务器，建议选择不同可用区，实现容灾效果。</td></tr>
<tr><td>网络</td><td>必选</td><td>表示在腾讯云上构建的逻辑隔离的网络空间，一个私有网络由至少一个子网组成。系统会为您在每个地域提供的默认私有网络和子网。</br>
如现有的私有网络/子网不符合您的要求，可以在私有网络控制台进行创建。</br><b>注意</b>：<ul><li>同一私有网络内资源默认内网互通。</li><li>购买时，云服务器需要创建在与云服务器相同可用区属性的子网内。</li></ul></td></tr>
<tr><td>实例</td><td>必选</td><td>根据底层硬件的不同，腾讯云目前提供了多种不同的实例类型。为获得最佳性能，建议使用新一代实例类型。</br>更多实例详情请参见 <a href="https://cloud.tencent.com/document/product/213/11518">实例规格</a>。</td></tr>
<tr><td>镜像</td><td>必选</td><td>腾讯云提供公共镜像、自定义镜像、共享镜像、服务市场镜像，您可参考 <a href="https://cloud.tencent.com/document/product/213/4941">镜像类型</a> 进行选择。</br>对于刚开始使用腾讯云的用户，推荐选择公共镜像。</td></tr>
<tr><td><a href="https://cloud.tencent.com/document/product/362/2353">系统盘</a></td><td>必选</td><td>用于安装操作系统，默认为50GB。</br>地域的不同将会影响可供选择的云硬盘类型，请根据实际页面提示进行选择。</br>更多关于云硬盘的介绍，请参考 <a href="https://cloud.tencent.com/document/product/362/2353">云硬盘类型</a>。</td></tr>
<tr><td><a href="https://cloud.tencent.com/document/product/362/2353">数据盘</a></td><td>可选</td><td>用于扩展云服务器的存储容量，提供高效可靠的存储设备。默认不添加云硬盘数据盘。</br>更多关于云硬盘的介绍，请参考 <a href="https://cloud.tencent.com/document/product/362/2353">云硬盘类型</a>。</td></tr>
<tr><td>定期快照</td><td>可选</td><td>可针对系统盘或数据盘设置定期快照策略。更多关于定期快照的介绍，请参见 <a href="https://cloud.tencent.com/document/product/362/8191">定期快照</a>。</td></tr>
<tr><td>公网带宽</td><td>必选</td><td>腾讯云提供以下两种网络计费方式，请根据实际需求进行选择。<ul><li><b>按带宽计费</b>：选择固定带宽，超过本带宽时将丢包。适合网络波动较小的场景。</li><li><b>按使用流量计费</b>：按实际使用流量收费。可限制峰值带宽避免意外流量带来的费用，当瞬时带宽超过该值时将丢包。适合网络波动较大的场景。</li></ul></td></tr>
<tr><td>IPv6地址</td><td>可选</td><td>开通实例的 IPv6 地址。更多关于 IPv6 的介绍，请参见 <a href="https://cloud.tencent.com/document/product/1142/38134">弹性公网 IPv6</a>。</td></tr> 
<tr><td>数量</td><td>必选</td><td>表示需购买云服务器的数量。</td></tr> 
<tr><td>时长</td><td>必选</td><td>仅限包年包月的云服务器。</br>表示云服务器的使用时长。</td></tr> 
</table>
2. 单击**下一步：设置主机**，进入设置主机页面。
 
## 设置主机
1. 根据页面提示，配置以下信息：
![](https://main.qcloudimg.com/raw/a23df22b09036729088db90600c52853.png)
<table>
<tr><th style="width: 20%">类别</th><th style="width: 12%">必选/可选</th><th>配置说明</th></tr>
<tr><td>安全组</td><td>必选</td><td>用于设置单台或多台云服务器的网络访问控制。</br><b>请确保已开放22登录端口</b>，更多信息请参见 <a href="https://cloud.tencent.com/document/product/213/12452">安全组</a>。</td></tr>
<tr><td>所属项目</td><td>必选</td><td>默认为默认项目，可根据实际需求，选择已建立的项目，用于管理不同的云服务器。</td></tr>
<tr><td>标签</td><td>可选</td><td>可按需给实例增加标签，用于云资源进行分类、搜索和聚合。关于标签更多介绍，请参见 <a href="https://cloud.tencent.com/document/product/651/13334">标签</a>。</td></tr>
<tr><td>实例名称</td><td>可选</td><td>表示需要创建的云服务器的名称。</br>用户自定义，推荐为“CVM-01”。</td></tr>
<tr><td>登录方式</td><td>必选</td><td>设置用户登录云服务器的方式，请根据实际需求进行设置。<ul><li><b>设置密码</b>：自定义设置登录实例的密码。</li><li><b>立即关联密钥</b>：关联 SSH 密钥，通过 SSH 密钥方式可以更为安全的登录云服务器。</br>如您没有密钥或现有的密钥不合适，可以单击【现在创建】进行创建。更多 SSH 密钥信息请参见 <a href="http://cloud.tencent.com/doc/product/213/SSH%E5%AF%86%E9%92%A5">SSH 密钥</a>。</li><li><b>自动生成密码</b>：自动生成的密码将会以 <a href="https://console.cloud.tencent.com/message">站内信</a> 方式发送。</li></ul></td></tr>
<tr><td>安全加固</td><td>可选</td><td>默认免费开通，帮助用户构建服务器安全防护体系，防止数据泄露。</td></tr>
<tr><td>云监控</td><td>可选</td><td>默认免费开通，提供立体化云服务器数据监控、智能化数据分析、实时化故障告警和个性化数据报表配置，让用户精准掌控业务和云服务器的健康状况。</td></tr>
<tr><td>自动化助手</td><td>可选</td><td>默认免费开通，作为 CVM 的原生运维部署工具，无需远程连接实例，可自动批量执行 Shell 命令，完成运行自动化运维脚本、轮询进程、安装/卸载软件、更新应用及安装补丁等任务。</td></tr>
<tr><td>自动续费</td><td>可选</td><td>仅限包年包月的云服务器。</br>勾选“账户余额足够时，设备到期后按月自动续费”，避免设备到期时需要进行手动续费的操作。</td></tr>
<tr><td>高级设置</td><td>可选</td><td>根据实际需求对实例做更多配置。<ul><li><b>主机名</b>：用户可以自定义设置云服务器操作系统内部的计算机名，云服务器成功生产后可以通过登录云服务器内部查看。</li><li><b>CAM角色</b>：设置角色后可以通过角色对云服务器授予腾讯云中服务、操作和资源的访问权限。具体可参考 <a href="https://cloud.tencent.com/document/product/213/47668">管理实例角色</a> 进行设置。</li><li><b>置放群组</b>：根据需要可以将实例添加到置放群组中，提高业务的可用性。具体可参考 <a href="https://cloud.tencent.com/document/product/213/15486">置放群组</a> 进行设置。</li><li><b>自定义数据</b>：指定自定义数据来配置实例，既当实例启动时运行配置的脚本。如果一次购买多台云服务器，自定义数据会在所有的云服务器上运行。Linux 操作系统支持 Shell 格式，最大支持 16KB 原始数据。具体可参考 <a href="https://cloud.tencent.com/document/product/213/17525">自定义数据</a>。</br><b>注意</b>：自定义数据配置仅支持部分带 Cloudinit 服务的公有镜像，具体可参考 <a href="https://cloud.tencent.com/document/product/213/19670">Cloud-Init</a>。</li></ul></td></tr>
</table>
2. 单击**下一步：确认配置信息**，进入确认配置信息页面。


## 确认配置信息

1. 核对购买的云服务器信息，了解各项配置的费用明细。
2. 阅读并勾选“同意《腾讯云服务协议》和《退款规则》”或“同意《腾讯云服务协议》”。
3. 您可根据实际需求，进行以下操作：
 - 选择**保存为启动模板**：将该实例的配置保存为启动模板，您可使用启动模板快速创建实例。详情请参见 [管理实例启动模板](https://cloud.tencent.com/document/product/213/62034)。
 - 选择**生成 API Explorer 最佳实践脚本**：生成已选配置对应的创建实例 OpenAPI 最佳实践脚本代码，您可保存代码用于购买同配置云服务器。详情请参见 [生成创建实例 API Explorer 最佳实践脚本](https://cloud.tencent.com/document/product/213/49856)。
3. 单击**立即购买**或**开通**，完成支付。当您付款完成后，即可进入 [云服务器控制台](https://console.cloud.tencent.com/cvm) 查收您的云服务器。
云服务器的实例名称、公网 IP 地址、内网 IP 地址、登录名、初始登录密码等信息将以 [站内信](https://console.cloud.tencent.com/message) 的方式发送到账户上。您可以使用这些信息登录和管理实例，也请尽快更改您的云服务器登录密码，以保障主机安全性。

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
 [初始化云硬盘（Linux）](https://cloud.tencent.com/document/product/362/6734#Steps)
- 磁盘容量大于等于2TB时：
 [初始化云硬盘（Linux）](https://cloud.tencent.com/document/product/362/6735#Steps)

更多操作指引请参见 [初始化场景介绍](https://cloud.tencent.com/document/product/362/33065)。
