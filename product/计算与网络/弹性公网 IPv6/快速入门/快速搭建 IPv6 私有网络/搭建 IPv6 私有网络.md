本教程将帮助您搭建一个具有 IPv6 CIDR 的私有网络（VPC），并为 VPC 内的云服务器开启 IPv6，实现 IPv6 的内外网通信。

## 操作场景
- 云服务器启用 IPv6，和 VPC 内其他云服务器的 IPv6 内网互通。
- 云服务器启用 IPv6，和 Internet 的 IPv6 用户进行双向通信。
![](https://main.qcloudimg.com/raw/245f8acb1bea7b002035193b089bf1b7.png)

## 前提条件
目前弹性公网 IPv6 处于内测中，如需使用，请提交 [内测申请](https://cloud.tencent.com/apply/p/c28sebss8v)。

## 操作须知
- 在开始使用腾讯云产品前，您需要先 [注册腾讯云账号](https://cloud.tencent.com/register?s_url=https%3A%2F%2Fcloud.tencent.com%2F)。
- 目前支持 IPv6 的地域为北京、上海、广州、上海金融、北京金融、深圳金融、成都、南京、香港、新加坡，弗吉尼亚。请在这些地域部署 IPv6 服务。
- IPv6 地址为 GUA 地址，每个 VPC 分配1个`/56`的 IPv6 CIDR，每个子网分配1个`/64`的 IPv6 CIDR，每个弹性网卡分配1个 IPv6 地址。
- 主网卡、辅助网卡均支持申请 IPv6 地址。想要了解更多云服务器和弹性网卡的关系，请参见 [弹性网卡](https://cloud.tencent.com/document/product/576) 产品文档。

## 操作步骤
### 步骤一：VPC 分配 IPv6 CIDR[](id:step1)
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc)。
2. 选择支持 IPv6 的地域，在 VPC 所在行的右侧操作栏下，选择【更多】>【编辑 IPv6 CIDR】。
3. 在“编辑 IPv6 CIDR” 弹框中，单击【获取】并确认相关信息后，单击【确定】。
系统将为 VPC 分配一个`/56`的 IPv6 地址段，您可以在列表中，查看到 IPv6 地址段的详细信息。
![](https://main.qcloudimg.com/raw/8b8774b80c053c4a879f1f1b055945a5.png)


### <span id="step2" />步骤二：为子网分配 IPv6 CIDR
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc)。
2. 在左侧目录下选择【子网】，进入管理页面。
3. 在 [步骤一](#step1) 中的 VPC 所属子网所在行的操作栏下，单击【获取 IPv6 CIDR】并确认操作。
系统将从 VPC 的`/56` IPv6 CIDR 分配一个`/64`的 IPv6 CIDR。
![](https://main.qcloudimg.com/raw/9b32564f2bc5df09ec198716b46f7cc2.png)

### <span id="step3" />步骤三：购买云服务器并配置云服务器的 IPv6
为 VPC 和子网分配 IPv6 CIDR 后，您可在该子网下创建一个具有 IPv6 地址的云服务器，也可以为该子网下运行中的云服务器获取 IPv6 地址。
>?
>由于 IPv6 地址目前还不支持自动下发到网卡，因此从在控制台获取 IPv6 地址后，您还需要登录云服务器进行 IPv6 的配置。


1. 登录 [云服务器购买页](https://buy.cloud.tencent.com/cvm?tab=cvm)。
2. 在云服务器购买页上方，单击【自定义配置】。
3. 在自定义设置页面，完成云服务器各种配置操作，具体操作请参见 [快速搭建IPv4私有网络](https://cloud.tencent.com/document/product/215/30716#.E6.AD.A5.E9.AA.A4.E4.BA.8C.EF.BC.9A.E8.B4.AD.E4.B9.B0.E4.BA.91.E6.9C.8D.E5.8A.A1.E5.99.A8)。
>!在选择机型时，请注意如下参数：
 - 地域：北京、上海、广州、上海金融、深圳金融、成都、南京、新加坡。
 - 网络：选择 [步骤一](#step1) 中 VPC 和[ 步骤二](#step2) 中的子网。
 - IPv6 地址：勾选【免费分配 IPv6 地址】。
4. 核对购买的云服务器信息，并进行支付。
5. 云服务器购买成功后，即可在 [云服务器实例列表](https://console.cloud.tencent.com/cvm/instance/index?rid=1)  查看到 IPv6 地址信息。
![](https://main.qcloudimg.com/raw/a427545faa7aa68ae6d5f6d80a93aa9e.png)
>?
>- 如果云服务器在购买时未分配 IPv6 地址，可在对应云服务器实例所在行的操作栏下，选择【更多】>【IP 和网卡】>【管理 IPv6】，为主网卡分配 IPv6 地址。
>- 如果想要给云服务器的其他弹性网卡也分配 IPv6 地址，请参见 [申请和释放 IPv6
](https://cloud.tencent.com/document/product/576/37972) 进行操作。
>
6. 登录云服务器配置 IPv6，由于各类云服务器操作系统配置 IPv6 的方式不同，详细操作方法请参见  [Linux 云服务器配置 IPv6 ](https://cloud.tencent.com/document/product/1142/47666) 和  [Windows 云服务器配置 IPv6](https://cloud.tencent.com/document/product/1142/47667)。

### 步骤四：（可选）为云服务器的 IPv6 地址开通公网
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc)。
2. 在左侧目录下，选择【IP 与网卡】>【弹性公网 IPv6】。
3. 选择云服务器的所在地域，单击【申请】。
4. 进入管理页面，勾选云服务器的 IPv6 地址、设置目标带宽上限	，单击【提交】即可。

>?
>- 云服务器申请了 IPv6 地址后，默认关闭了公网访问能力，可通过弹性公网 IPv6 [管理 IPv6 公网](https://cloud.tencent.com/document/product/1142/38141) 能力。
>- 当运营商类型为 BGP 时，弹性公网 IPv6 地址即为云服务器获取到的 IPv6 地址，所以请确保云服务器已经获取到 IPv6 地址。
>- 单次操作可支持最多100个 IPv6 地址同时开通公网，如果超过100个 IPv6 地址需要开通公网，请分多次操作。
>
![](https://main.qcloudimg.com/raw/f66f01c4b1a0791f956663188e2b702b.png)

### 步骤五：配置 IPv6 的安全组规则
>?出入方向的安全组规则支持配置来源为单个 IPv6 地址或者 IPv6 CIDR，其中`::/0`代表所有的 IPv6 源地址。
>
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc)。
2. 在左侧目录下，选择【安全】>【安全组】，单击云服务器绑定的安全组 ID，进入详情页。
3. 在详情页添加入站规则与出站规则：

 - 选择【入站规则】>【添加规则】，添加 IPv6 的入方向安全组规则，单击【完成】即可。
![](https://main.qcloudimg.com/raw/73ff04af93a1f13eef92d4f74ac30fc2.png)
 - 选择【出站规则】>【添加规则】，添加 IPv6 的出方向安全组规则，单击【完成】即可。
![](https://main.qcloudimg.com/raw/c0d255728fa6b48292f425c5ffb6559f.png)

### 步骤六：测试 IPv6 的连通性
下面分别介绍 [Linux 云服务器](#gjpz) 和 [Windows 云服务器](#Windows云服务器) 如何测试 IPv6 的连通性。
>?
>- 如果测试公网连通性，请确保已经在“安全组”设置 IPv6 策略、并在“弹性公网 IPv6”设置 IPv6 公网带宽。
>- 如果未开通 IPv6 公网，但需要测试 IPv6 云服务器的连通性（Ping 测试、SSH、远程桌面测试），可使用同一私有网络下已经获取 IPv6 地址的云服务器进行连通性测试。
>- 如果云服务器镜像开启了 IPv6，系统则会为每个网卡默认分配一个“FE80”开头的 link-local 地址，该link-local 并不能作为内外网通信的 IPv6 地址。

<span id="gjpz"></span>

#### Linux 云服务器
- Linux 云服务器可通过 Ping 或 SSH 等操作来测试 IPv6 的连通性。

 - **方式1：**通过 Ping 进行测试，操作如下：
 在云服务器中执行 `ping6 IPv6地址`进行测试，例如，`ping6 240c::6666` 、 `ping6 www.qq.com`、`ping6 同一私有网络下的 IPv6 地址`，成功结果如下图所示：
![](https://main.qcloudimg.com/raw/de0f8028e1ab3c670428ce65e47c7c63.png)
 
 - **方式2：**通过 IPv6 地址 SSH 云服务器，操作如下：
  执行如下命令查看 IPv6 地址，并用 PuTTY 或者 Xshell 等软件，测试能否通过 IPv6 地址 SSH 到云服务器。
	```
  ifconfig
	 ```

  ![](https://main.qcloudimg.com/raw/16838301e15e59ec20f8d3ffb1dd5a69.png)
  成功结果如下图所示：
  ![](https://main.qcloudimg.com/raw/c951d48a32b010d00b481ed26082a1bb.png)

 <span id="Windows云服务器"></span>

#### Windows 云服务器
Windows 云服务器可通过 Ping 或远程桌面测试 IPv6 连通性。
 - **方式1**：通过 Ping 进行测试，操作如下：
在操作系统界面，选择左下角的<img src="https://main.qcloudimg.com/raw/87d894e564b7e837d9f478298cf2e292.png" style="margin:-3px 0px;width:25px">，单击 <img src="https://main.qcloudimg.com/raw/f0c84862ef30956c201c3e7c85a26eec.png" style="margin: -3px 0px;">，打开 “Windows PowerShell” 窗口，执行`ping -6 IPv6 地址`进行测试，例如，`ping -6 240c::6666`或`ping -6 同一私有网络下的 IPv6 地址`，成功如下图所示。
![](https://main.qcloudimg.com/raw/51c8b10298aa8cdca15b4f67ff54396c.png)
 - **方式2**：通过 IPv6 地址进行远程桌面，远程桌面操作详情请参见 [使用远程桌面连接登录 Windows 实例](https://cloud.tencent.com/document/product/213/35703)。

   ![](https://main.qcloudimg.com/raw/ba325fb98c4efe86a1f3a4bcd55f77be.png)
