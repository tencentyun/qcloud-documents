NAT 边界防火墙开关支持基于内网资产进行流量管控与安全防护，同时支持基于 SNAT、DNAT 进行的网络流量转发。
## 操作指南
1. 登录 [云防火墙控制台](https://console.cloud.tencent.com/cfw)，在左侧导航栏中，选择**防火墙开关** > **NAT边界开关**，进入 NAT 边界开关页面。
>?当某个 NAT 边界防火墙开关开启后，对应子网的互联网流量将经过防火墙，届时访问控制规则、入侵防御功能将对其生效，流量日志也会生成。
2. 在 “NAT 边界开关”页面，可进行创建实例、同步资产、查看并监控基于 NAT 边界的带宽情况等操作。

###  **创建实例**	
1. 在 [NAT 边界开关页面](https://console.cloud.tencent.com/cfw/switch/nat) 下，单击**创建实例**。
![](https://main.qcloudimg.com/raw/57aef4dbbc56957be8b0be12567dc321.png)
2. 在“新建 NAT 边界防火墙”弹窗中，可为当前账号创建一个新的 NAT 边界防火墙实例，填写相关字段，单击**下一步**。
>?创建“NAT 边界防火墙”实例，涉及大量后台配置工作，这个步骤可能需要持续若干分钟。
>
	![](https://main.qcloudimg.com/raw/dada8612c7f4278e4c1415fbb17929dd.png)
	**字段说明：**
	- **地域**：选择创建地域，支持国内所有地域，创建实例后不可更改。
>?用户可在拥有 VPC 的所有国内地域（支持中国香港地域）中进行地域选择，同地域下可创建多个防火墙实例，但总带宽不能超过限定规格。
	- **可选区**：根据需求选择合适的可用区。
	- **实例名称**：输入实例名称。
	- **带宽规格**：根据需求选择带宽规格，最小20Mbps，如需更多带宽请 [升级扩容](https://buy.cloud.tencent.com/cfw?type=modify&adtag=cfw.from.console.page.buy)。
>?互联网带宽保持一致，如果分了多个 NAT 防火墙，那么多个 NAT 防火墙的带宽之和，要小于等于互联网边界的带宽。
	- **模式**：分为新增模式和接入模式。
		- **新增模式**：若当前地域没有 NAT 网关，新增模式可以通过 NAT 边界防火墙内置的 NAT 功能，实现指定实例通过防火墙访问互联网。
		- **接入模式**：若当前地域已有 NAT 网关，或者希望公网对外的出口 IP 保持不变，接入模式可以将 NAT 边界防火墙平滑接入到 NAT 网关与 CVM 实例之间。
	- **弹性 IP**：若选择新建弹性 IP，系统会自动为用户申请一个弹性 IP，用户也可从所有闲置的弹性 IP 中选择一个进行绑定。
3. 选择需要接入的 VPC 或 NAT，单击**创建**,即可创建成功。


### **网络拓扑**
云防火墙提供了一个可视化视图，帮助您快速梳理 NAT 边界的访问关系。在 NAT 边界可视化视图中，私有网络展现了 VPC 实例。
1. 在 [NAT 边界开关页面](https://console.cloud.tencent.com/cfw/switch/nat) 下，单击**网络拓扑**，可查看 NAT 边界的访问关系。
![](https://main.qcloudimg.com/raw/54a0d19fdc727d18f4b1f881c6b58914.png)
2. 单击某个 VPC 节点，可查看对应子网列表，可以只针对当前子网开启或关闭防火墙开关。
![](https://main.qcloudimg.com/raw/3038c664f8b44abb950378f396e84acf.png)

### 防火墙开关
在 [防火墙开关页面](https://console.cloud.tencent.com/cfw/switch/nat?tab=switch)，支持开启或关闭 NAT 边界防护。云防火墙会定时自动同步云资产，因此不用担心资产变更后的防火墙配置（例如，变更了某个子网，防火墙会在短时间内自动同步）。
- **开启防护**
>!开启开关后，请勿在 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1) 中手动变更开关对应的路由，否则将导致防火墙丢失路由而引发网络中断。
>
	- **方式1**：在实例列表上方，单击**开启防护**，所有未开启的 NAT 边界防火墙开关将被打开，所有路由表将会自动添加下一跳类型为 NAT 边界防火墙的路由策略，所有子网的互联网流量将会经过 NAT 边界防火墙。
>?若用户选择开启同一路由表关联的所有子网，系统会自动在该路由表中增加一条下一跳指向 NAT 边界防火墙的路由策略，并关闭原访问公网的路由策略，因此该路由表关联的所有子网的互联网流量，将会经过 NAT 边界防火墙。
>
		![](https://main.qcloudimg.com/raw/f5a6cb3777494e6c6f7faa5a2ec3cb74.png)
	- **方式2**：单独开启防火墙开关。
		- **新增模式**：如想开启对某个子网实例的 NAT 边界防护，可以在右侧操作栏，单击“防火墙开关”按钮，开启防火墙开关后，将开启对该子网资产的防护。
>?若用户仅选择开启某个子网，系统会自动为当前子网创建新的路由表，复制现有的全部路由策略，在新路由表中增加一条下一跳指向 NAT 边界防火墙的路由策略，并关闭原访问公网的路由策略，因此该子网的互联网流量，将会经过 NAT 边界防火墙。
>
![](https://main.qcloudimg.com/raw/dbad366888b468b30205e5ae1ab95036.png)
		- **接入模式**：一个防火墙开关对应一个子网，用来控制流量是否经过 NAT 边界防火墙，关联了同一个路由表的子网将会同时开启或关闭，创建 NAT 边界防火墙（接入模式）后，系统会自动开启防火墙开关，以保证网络不中断。
>?开启开关后，系统会自动修改子网关联路由表的路由策略，以及子网对应的端口转发规则，该子网的流量牵引至 NAT 边界防火墙。
>
![](https://main.qcloudimg.com/raw/8df50a9eced91ff15eff901c3f7421a6.png)
- **关闭防护**
	- **方式1**：在实例列表上方，单击**关闭防护**，所有已开启的 NAT 边界防火墙开关将被关闭，NAT 边界防火墙会自动关闭下一跳类型为 NAT 边界防火墙的所有路由表的路由策略，所有子网将断开与互联网的连接，用户需要在 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1) 手动启动新的路由策略。
>?若用户选择关闭同一路由表关联的所有子网，系统会自动关闭该路由表中下一跳指向 NAT 边界防火墙的路由策略，该路由表关联的所有子网将会断开与互联网的连接。
>
![](https://main.qcloudimg.com/raw/e4aef85f8fec9e5d9a8e7afae6e0d9aa.png)
 		- **方式2**：单独关闭防火墙开关。
			- **新增模式**：如想关闭对某个子网实例的NAT边界防护，可以在防火墙操作栏，单击“防火墙开关”按钮，关闭对该子网资产的防护，关闭开关后，用户需要前往 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1) 手动启用新的路由策略。
>?若用户仅选择关闭某个子网，系统会自动为当前子网创建新的路由表，复制现有的全部路由策略，并关闭下一跳指向 NAT 边界防火墙的路由策略，该子网将会断开与互联网的连接。
>
![](https://main.qcloudimg.com/raw/b0a7d83c39201adfca9d215dfb6093ab.png)
			- **接入模式**：接入模式下，如想单独关闭防火墙开关，可以在防火墙操作栏，单击“防火墙开关”按钮，接入模式关联了同一个路由表的子网将会同时关闭。
>?关闭开关后，系统会自动恢复子网关联路由表的路由策略，以及子网子网对应的端口转发规则，该子网的流量将恢复原先路径，不会经过 NAT 边界防火墙。
>
![](https://main.qcloudimg.com/raw/25de90f0acc96be53dc16393b0ee49d2.png)

### 接入域名管理
在 [接入域名管理](https://console.cloud.tencent.com/cfw/switch/nat?tab=domain) 页面，可进行新增域名、编辑域名、开启或关闭微信远程运维服务等操作。

- **新增域名**
 1. 单击**新增域名**，下拉选择想要创建的地域。
>!一个地域仅能创建一个域名。创建域名前请先检查是否已创建 NAT 防火墙。
>
![](https://main.qcloudimg.com/raw/8f6c28d11cad1d593ee509f6ac266702.png)
 2. 选择需要绑定的防火墙实例，并填写好域名前缀，单击**确定**完成新建。
>?
>- 对于单地域多防火墙实例场景下，域名绑定某个实例后，该地域均可通过该域名进行互联网访问。
>- 创建后域名15天内不可修改，请仔细确认域名信息。

- **编辑域名**
 1. 选中想要编辑域名前的![](https://main.qcloudimg.com/raw/402e69e68d90fe16581bb35b5a4c83e1.png)，并单击**编辑域名**。
 ![](https://main.qcloudimg.com/raw/016b33e21c3a2f001b74a77e50400bbc.png)
 2. 在编辑域名弹窗中，修改绑定的实例或域名前缀，单击**确定**保存修改。
>!域名每15天仅可编辑一次，请仔细确认域名信息。
>
![](https://main.qcloudimg.com/raw/e79dde2f61721f777848829c328fe73d.png)

- **微信远程运维服务**
在域名卡片的右侧可以开启或关闭微信远程运维功能。新增域名默认开启。
 - 开启后，该地域 NAT 边界防火墙下的实例就可以通过 NAT 边界防火墙进行远程运维的管控。您可以通过 NAT 边界防火墙访问全部公网 SSH/RDP 服务，以及该地域的全部内网 SSH/RDP 服务。
 - 关闭后，域名将不再解析已接入的资产实例。对应地域已接入的内网资产无法再使用微信远程运维功能，公网资产仅支持通过公共域名登录。

![](https://main.qcloudimg.com/raw/1bbe1ae47829471ad09b015d2ee5342f.png)

- **数据库防护服务**
在域名卡片的右侧可以开启或关闭数据库防护功能。新增域名默认开启。
 - 开启后，该地域NAT边界防火墙下的数据库实例将支持防火墙的入侵检测能力和访问控制管控。您可以配置白名单策略来限制数据库的访问。
 - 关闭后，域名将不再解析已接入的数据库实例，所有流量均不再经过防火墙。如需恢复外网访问，请重新开启开关或开启接入前域名解析。

![](https://main.qcloudimg.com/raw/d5be6cb0154a4aa7fc7fa105cb216d79.png)
 
### 实例配置
 在 [NAT 边界开关页面](https://console.cloud.tencent.com/cfw/switch/nat) 下，单击对应**实例 ID**，可以进行实例配置。
- **端口转发**
在右侧边栏中可以查看用户基于 NAT 边界防火墙实例所添加的 DNAT 端口转发规则，以及与实例关联的弹性 IP。
>?
>- 接入模式中，NAT 边界防火墙会自动同步现有NAT网关的端口转发规则，从而保证流量通行，后续对于该规则的操作，请在 [云防火墙控制台](https://console.cloud.tencent.com/cfw/ac/nat) 中进行。
>- 开启防火墙开关的子网 SNAT、DNAT 流量都会经过防火墙，关闭开关的子网 SNAT、DNAT 流量都走原先路径。
>- 请勿前往私有网络控制台操作端口转发规则，否则可能造成网络中断。
>
![](https://main.qcloudimg.com/raw/987948ac445541239938616a1dbf0bd2.png)
	1. 在实例配置页面的端口转发页签下，单击**新建规则**。
![](https://main.qcloudimg.com/raw/2b23d9c276686ceaf47772970d9d7890.png)
	2. 在“新建端口转发规则”弹框中，用户可为当前 NAT 边界防火墙实例添加一条外部 IP 为用户所绑定的弹性 IP 的 DNAT 规则。
>?
>- 在外部 IP 端口下拉框内，提供的选项为当前 NAT 边界防火墙实例所绑定的弹性 IP。
>- 输入内部 IP 地址时，用户需填写本地域 VPC 网段内可用的 IP。
>
![](https://main.qcloudimg.com/raw/0ac292a32d8ab33fb3e166af890db1a9.png)
- **出口绑定**
在新增模式下，当规则列表为空时，所有 VPC 的子网将随机选择 NAT 网关访问互联网。
>!接入模式暂不支持出口绑定。
>
	1. 在实例配置页面的出口绑定页签下，单击**新建规则**。
![](https://main.qcloudimg.com/raw/b5a17b6832d01348bd50fc4a4f93a743.png)
	2. 在“新建出口绑定规则”弹框中，提供防火墙实例 ID 信息，用户可为当前 NAT 边界防火墙添加 SNAT 规则。
>?协议可选子网和私有网络，VPC 或子网的选项选择接入 NAT 边界防火墙，且当前没有绑定出口 NAT 规则的 VPC 或子网。
>
![](https://main.qcloudimg.com/raw/3964cb064bb8e4853f8385997990d253.png)
- **接入 VPC 与公网 IP**
在实例配置页面的接入 VPC 与公网 IP 页签下，可以增加接入的 VPC 或者重新选择 VPC。
 - 增加接入的 VPC
 单击**增加接入 VPC**，选择需要增加接入的VPC，单击**确定**。
 ![](https://main.qcloudimg.com/raw/d0f5278c2167f2e5467b2e325b0d6302.png)
 - 重新选择 VPC
 单击**重新选择 VPC** > **确定**，即可重新选择 VPC。
>?必须关闭当前防火墙实例下的所有子网开关和 DNS 流量开关。
>
 ![](https://main.qcloudimg.com/raw/817ad9156d4f6a21069650947ff09470.png) 
-  接入 DNS 流量
 - 单击![](https://main.qcloudimg.com/raw/4810bf867dec5152045bc24a9ca018c5.png)开启对应 VPC 右侧的DNS流量开关，开启开关后，系统会修改所接入 VPC 的 DNS 解析地址，将 DNS 流量牵引至 NAT 边界防火墙，从而获取全流量域名。
>?接入 VPC 中若存在未开启防火墙开关的子网，可能导致该子网 DNS 解析产生明显延迟，建议开启全部防火墙开关后再启用此开关。
>
![](https://main.qcloudimg.com/raw/901b75396d80a5c125baa2e34bbd9a03.png)
 - 关闭开关后，系统会恢复所接入 VPC 的 DNS 解析地址，DNS 流量将恢复原先路径，不再经过 NAT 边界防火墙。
 
- **应用场景**：NAT 防火墙支持将用户的 DNS 解析地址改为 NAT 防火墙的 IP，从而将用户的 DNS 流量牵引至防火墙，防火墙继续请求真实 DNS 解析服务器，并返回 DNS 响应给指定的服务器，不区分 NAT 防火墙的模式。
	1. 在 [NAT 边界规则](https://console.cloud.tencent.com/cfw/ac/nat) 页面，单击**出向规则**。
	2. 在出向规则页签中，单击**添加规则**。
	3. 在添加规则页面，填写相关字段，并选择 DNS 协议。
		![](https://main.qcloudimg.com/raw/247aebda68b11b47b32707fb8bee1017.png)
- **关联弹性 IP**
	1. 在实例配置页面右侧的“关联弹性 IP”模块，单击**+绑定弹性IP**。
	2. 在单选下拉框内，用户可为当前 NAT 边界防火墙实例绑定一个系统新建的弹性 IP，或在当前地域拥有的所有闲置弹性 IP 里选择一个进行绑定。
>?
>- 关联弹性 IP 功能目前只支持新增模式，暂未支持迁移模式。
>- 解除绑定某个弹性 IP 时，页面上与其相应的 DNAT 规则也会消失。
>
![](https://main.qcloudimg.com/raw/48461beaa0162204aa2db464d949458a.png)


### 升级扩容
1. 在 [NAT 边界开关](https://console.cloud.tencent.com/cfw/switch/nat) 页面下，单击**升级扩容**。
![](https://main.qcloudimg.com/raw/ff67ed7ed725dcaa53a9dd2b13791da5.png)
2. 在 NAT 边界网关页面，可以直接调整带宽规格，单击**确定**即可调整带宽规格。
>?
>- 调整的范围与互联网带宽保持一致，如果分了多个 NAT 防火墙，那么多个 NAT 防火墙的带宽之和，要小于等于互联网边界的带宽。
>- 如果目标带宽超过当前购买的带宽规格，可以单击 [升级扩容](https://buy.cloud.tencent.com/cfw?type=modify&adtag=cfw.from.console.page.buy)，来调整互联网边界带宽。
>- 如果是小范围调整带宽，后台修改，无需切换网络。在较大范围调整带宽时，需要重新配置网络，否则会造成业务闪断。
>
![](https://main.qcloudimg.com/raw/3038bb363ab8ce1914400287ea18da82.png)

### 监控情况
在 [NAT 边界开关](https://console.cloud.tencent.com/cfw/switch/nat) 页面，可进行查看并监控基于 NAT 边界的带宽情况、同步资产、网络拓扑等。
1. 在状态监控面板右上角，单击统计按钮，进入防火墙状态监控页面。
![](https://main.qcloudimg.com/raw/b2bde53bb5413094f075911a883608dd.png)
2. 在防火墙状态监控页面，可实时查看并监控基于 NAT 边界的带宽情况，可避免因 NAT 边界防火墙带宽超出规格而带来网络丢包和波动，从而及时作出扩容或关闭部分开关等调整。
![](https://main.qcloudimg.com/raw/4b2b7b993418e8287b0d3debea58cdd7.png)

### 同步资产
在 [NAT 边界开关](https://console.cloud.tencent.com/cfw/switch/nat) 页面下，单击**同步资产**，可以主动调用后台接口重新读取并同步用户子网的资产信息，可避免发生因用户资产规模在后台轮询间隔内发生变化，但尚未被同步的情况。
![](https://main.qcloudimg.com/raw/562aca3bf423d65b4f42fd7d5b469e67.png)

### 对 VPC 及 NAT 进行其他操作
#### **增加接入 VPC/NAT**
- **新增模式**：
	1. 在 [NAT 边界开关](https://console.cloud.tencent.com/cfw/switch/nat) 页面右上角，单击更多按钮，在下拉框中，单击**增加接入VPC**。
![](https://main.qcloudimg.com/raw/d3af811c1b49792fb9eac7c884f6f3e9.png)
	2. 在增加需要接入的 NAT 弹框中，选择需要的 NAT，单击**确定**，即可配置完成。
>?
>- 支持私有网络 ID/名称、IPv4 CIDR 关键字搜索。
>- 复选框：默认已点选用户当前 VPC，已选择的 VPC 无法取消。
>- 单击**增加需要接入的 NAT**后，即触发当前地域下 NAT 边界防火墙开关锁，直至重新选择完毕，单击**确定**后解锁。在开关锁期间，若有当前地域其他用户有开启开关请求，会提示有其他用户正在重新接入 NAT，开关被锁定，请稍后重试。
>
![](https://main.qcloudimg.com/raw/0da193e1e78d589ba64033aca7a7cd06.png)
- **接入模式**：
	1. 在 [NAT 边界开关](https://console.cloud.tencent.com/cfw/switch/nat) 页面右上角，单击更多按钮，在下拉框中，单击**增加接入 NAT**。
	2. 在增加需要接入的 VPC 弹框中，选择需要的 VPC，单击**确定**，即可配置完成。
>?
>- 支持关键字模糊搜索：支持 NAT 实例 ID/名称、关联弹性 IP、私有网络 ID/名称搜索。
>- 复选框：默认已点选用户当前NAT防火墙实例已经接入的 NAT 网关并无法取消。
>
![](https://main.qcloudimg.com/raw/cb8f1cef4a08eff10d1fee3f2235f52e.png)

#### 重新选择接入 VPC/NAT
- **新增模式**：
	1. 在 [NAT 边界开关](https://console.cloud.tencent.com/cfw/switch/nat) 页面右上角，单击更多按钮，在下拉框中，单击**重新选择接入 VPC**。
>!请先检查开关是否全部关闭，重新选择接入 VPC 需要关闭全部开关（不包含关闭中的开关）。
	2. 在选择需要接入的 VPC 中，可查看用户当前地域的 VPC，选择需要接入的 VPC，单击**确定**，即可配置完成。
>?
>- 支持关键字模糊搜索：支持私有网络 ID/名称、IPv4 CIDR 关键字搜索。
>- 复选框：默认已点选用户当前VPC，已选择的VPC无法取消。
>
![](https://main.qcloudimg.com/raw/84c28123657f84e2a66ccd151217facb.png)

- **接入模式**
	1. 在 [NAT 边界开关](https://console.cloud.tencent.com/cfw/switch/nat) 页面右上角，单击更多按钮，在下拉框中，单击**重新选择接入 NAT**。	
>!请先检查开关是否全部关闭，重新选择接入 VPC 需要关闭全部开关（不包含关闭中的开关）。
>
![](https://main.qcloudimg.com/raw/d17c154d67078beead27c238df9fce2b.png)
	2. 在选择需要接入的 NAT 中，显示用户当前地域的NAT实例，选择需要接入的 NAT。
>?单击**选择需要接入的 NAT**后，即触发当前地域下 NAT 边界防火墙开关锁，直至重新选择完毕，单击**确定**后解锁。在开关锁期间，若有当前地域其他用户有开启开关请求，会提示有其他用户正在重新接入 NAT，开关被锁定，请稍后重试。
>
![](https://main.qcloudimg.com/raw/2ceceebd9fec596963f24f4c6c417719.png)

#### 销毁实例
1. 在 [NAT 边界开关](https://console.cloud.tencent.com/cfw/switch/nat) 页面右上角，单击更多按钮，在下拉框中，单击**销毁实例**。
>!
>- 销毁实例前必须关闭全部防火墙开关。
>- 用户由于业务变更，需要自主销毁实例，可自行在页面操作。
>- 销毁实例后会删除这个实例的所有配置，会保留日志，销毁完毕，会归还配额，自动恢复为原先的路由和端口转发，更新地域展示情况，只展示剩余地域。若无剩余地域，则页面回到创建实例初始页。
>
![](https://main.qcloudimg.com/raw/d02369cd9ee02750c30864d851f3e957.png)
2. 在弹出的确认框中，单击**确定**，即可删除这个实例的所有配置。
![](https://main.qcloudimg.com/raw/8f2e51da92b8c51d84430899a6073241.png)


## 相关信息
- 如需对所持有的公网 IP 以及关联的云上资产，配置对应的防火墙开关，可参见 [互联网边界防火墙开关](https://cloud.tencent.com/document/product/1132/46928) 进行操作。
- 如需自动探测 VPC 信息与互通关系，并在每一对互通的 VPC 间，建立云防火墙开关，可参见 [VPC 间防火墙开关](https://cloud.tencent.com/document/product/1132/46930) 进行操作。
- 已绑定外网 IP 的主机，如需直接通过外网 IP 访问，请参见 [调整 NAT 网关和 EIP 的优先级](https://cloud.tencent.com/document/product/552/30012) 文档。
- 如遇到 NAT 边界防火墙相关问题，可参见 [NAT 边界防火墙](https://cloud.tencent.com/document/product/1132/56868) 文档。
