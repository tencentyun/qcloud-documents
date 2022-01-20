NAT 防火墙 DNS 开关开启后，系统会修改所接入 VPC 的 DNS 解析地址，将 DNS 流量牵引至 NAT 边界防火墙，从而获取全流量域名。
>?腾讯云默认 DNS 为：183.60.83.19，183.60.82.98。
>

可以按照如下流程，配置 DNS 防护：
<dx-steps>
-创建相关地区 NAT 防火墙接入 VPC 网络。
-开启 NAT 防火墙开关，流量都从 NAT 防火墙经过。（涉及到路由变更网络会抖动1-2秒）
-开启 DNS 开关进行验证 DNS 地址。
-使用 NAT 防火墙访问控制限制 DNS 解析（验证）。
</dx-steps>

如下图示例：腾讯云 CVM 公网资源为默认的 DNS 服务器。
![](https://qcloudimg.tencent-cloud.cn/raw/d30c4cea6a88cd1ead35b2bb4031d066.png)
![](https://qcloudimg.tencent-cloud.cn/raw/5ccbd4362f9e3050f90ca972fe96e22b.png)

## 步骤1：创建 NAT 防火墙[](id:step1)
1. 登录 [云防火墙控制台](https://console.cloud.tencent.com/cfw/asset)，在左侧导航中，单击**防火墙开关** > **NAT 边界开关**。
2. 在 NAT 边界开关页面，单击**网络拓扑** > **创建实例**，选择所需地域。
![](https://qcloudimg.tencent-cloud.cn/raw/52ddea2afea3ed5f3cc6efaeaf0b43d0.png)
3. 在新建 NAT 边界防火墙弹窗中，配置相关参数，单击**下一步**。
![](https://qcloudimg.tencent-cloud.cn/raw/c5b25f65243eb0f72e86f0ec1720ba0e.png)
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
4. 选择需要接入的 VPC，单击**创建**。
![](https://qcloudimg.tencent-cloud.cn/raw/64b4218d798b56456fb99d81942a6aca.png)
5. 等待若干分钟后，即可在防火墙实例列表中，查看刚刚创建的实例。
![](https://qcloudimg.tencent-cloud.cn/raw/b6656b22872bb4e84573fb083e50b19c.png)


## 步骤2：开启防火墙开关
在 [NAT 边界开关页面](https://console.cloud.tencent.com/cfw/switch/nat?tab=switch)，单击**防火墙开关** ，根据实际需求选择数据库在所在的子网，单击![](https://qcloudimg.tencent-cloud.cn/raw/9345ed8d746cbba9548277c2a156c95b.png)开启防火墙开关。
![](https://qcloudimg.tencent-cloud.cn/raw/3830acc3569c4f40e7e717be0deb105a.png)


## 步骤3：开启和验证 DNS 
1. 在 [NAT 边界开关页面](https://console.cloud.tencent.com/cfw/switch/nat?tab=switch)，单击**防火墙实例** ，选择 [步骤1](#step1) 创建的防火墙实例，单击**实例配置**。
![](https://qcloudimg.tencent-cloud.cn/raw/6620a08c6cbe1af8a9a697344353033a.png)
2. 在接入 VPC 与公网 IP 页面，选择所需 ID，单击![](https://qcloudimg.tencent-cloud.cn/raw/c69a24ce06731d4a9ee567c815e80bd3.png)开启 DNS 流量。
![](https://qcloudimg.tencent-cloud.cn/raw/2184523886f230aa78b0f9e5fb5c0e5a.png)
3. 通过 `ipconfig /release Ipconfig /renew` 刷新 DNS 获取地址。
![](https://qcloudimg.tencent-cloud.cn/raw/2614729ca469a64c5e23cff791d076aa.png)


## 步骤4：限制 DNS 解析
1. 在 [NAT 边界规则页面](https://console.cloud.tencent.com/cfw/ac/nat)，选择所需地域，单击**出向规则** > **添加规格**。
![](https://qcloudimg.tencent-cloud.cn/raw/242d7c09e239ea59777b010399403bf6.png)
2. 在添加出向规则弹窗中，配置相关参数，单击**确定**。
![](https://qcloudimg.tencent-cloud.cn/raw/d5d00718805d9eadb1c8f43c01f30922.png)
**字段说明**：
     - 执行顺序：访问控制规则的执行顺序，出站规则和入站规则的执行顺序互不影响，执行顺序较高的规则被优先匹配，命中某条规则后，不再匹配后序规则。当您修改某条规则的执行顺序时，原本该位置的规则的执行顺序+1，以此类推。当您删除某条规则时，后序所有规则的执行顺序-1。
     - 访问源：出向规则访问源仅对当前地域内的所有内网资产生效，支持 IP 和 CIDR。
     - 访问目的：出向规则访问目的对所有公网 IP/域名生效，支持 IP、CIDR、域名和地理位置。
     - 目的端口：
      - TCP/UDP/ANY 规则支持单端口号、基于'/'的端口段以及英文逗号分隔的离散端口值，例如“80”、“80/80”、“-1/-1”、“1/65535”或“80,443,3380/3389”。
      - HTTP/HTTPS/SMTP/SMTPS/FTP 规则仅支持配置单端口值，且 SMTP/FTP 协议间端口不可重复。
      - ICMP 规则不需要配置端口。
     - 协议：当前版本的出向规则支持 ANY、TCP、UDP 和 ICMP 协议。
     - 策略说明：
      - 放行：放通命中规则的流量，记录命中次数但不记录访问控制日志，且记录流量日志。
      - 观察：放通命中规则的流量，记录命中次数并记录访问控制日志与流量日志。
      - 阻断：拦截命中规则的流量，记录命中次数并记录访问控制日志，但不记录流量日志。
     - 描述：用于描述规则，最多支持50个字符。
3. 配置完成后验证 DNS 是否连通。
![](https://qcloudimg.tencent-cloud.cn/raw/b0c00d40c333a8d2405804bba3b861ed.png)
