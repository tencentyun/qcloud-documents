## 购买须知
- 在购买腾讯云 GPU 云服务器前，请确保已了解 [腾讯云 GPU 云服务器](https://cloud.tencent.com/document/product/560/8015)，且已了解 [配置与价格](https://cloud.tencent.com/document/product/560/8025)，并根据实际需求购买。
- 确保了解所选 GPU 实例所在可用区，可用区信息请参考 [AMD GPU 实例类型介绍](https://cloud.tencent.com/document/product/560/19701)。

##  购买步骤
本文以渲染型 **GA2 实例**为例，指导您按照以下步骤快速购买一台 GPU 云服务器。
>?GPU 渲染型 GA2 现处于内测阶段，如需使用，请前往 [内测申请](https://cloud.tencent.com/apply/p/0pz3p9aubg29)。

### 步骤1：登录购买页面
<div style="background-color:#00A4FF; width: 190px; height: 35px; line-height:35px; text-align:center;"><a href="https://buy.cloud.tencent.com/cvm?regionId=8&zoneId=800002&generation=v2&deviceType=ga&tabIndex=1" target="_blank"  style="color: white; font-size:16px;" hotrep="document.guide.2764.btn2">点此进入购买页面</a></div>


### 步骤2：选择地域与机型
进入购买页后，选择计费模式、网络、地域及机型。如下图所示：
![](https://main.qcloudimg.com/raw/30c66ecd0fe51767638e0acf975e373d.png)
- **计费模式**：【包年包月】或【按量计费】。
- **地域及可用区**：目前 GPU GA2 型云服务器仅支持**北京二区**。
- **网络**：选择现有私有网络或创建新私有网络。
- **实例**：机型选择【GPU机型】>【GPU渲染型GA2】。


### 步骤3：选择镜像<span id="Step3"></span>

GPU 渲染型 GA2 支持四种镜像类型：公共镜像、自定义镜像、共享镜像及镜像市场。详情请参见 [镜像概述](https://cloud.tencent.com/document/product/213/4940)。
刚开始使用腾讯云的用户，可选择【公共镜像】，并根据需要挑选版本。如下图所示：
![](https://main.qcloudimg.com/raw/3eca7d75defa296316eb976a4881cf59.png)
>!GA2 搭载了 AMD S7150 GPU，主机内需要安装对应的驱动程序才可正常使用。若选择了【公有镜像】，则需安装 GPU 驱动程序。
>
请从 `http://mirrors.tencentyun.com/install/windows/s7150_guest_driver.7z` 下载驱动。（腾讯云内网链接，需要在服务器内访问）然后执行 Setup.exe 进行安装即可。安装完成后，查看设备管理器，如下图所示则表明安装成功。
![设备管理器](//mc.qcloudimg.com/static/img/831923fe6942f4cb03640cffdb5883fd/image.png)

### 步骤4：选择存储与网络
1. 选择 GPU 云服务器的存储和带宽。如下图所示：
![](https://main.qcloudimg.com/raw/6be045d13c8d7d6d3aebb9571ef324e1.png)
主要参数信息如下：
	- **存储**：根据 [步骤3](#Step3) 选择的配置，GPU 云服务器的系统盘和数据盘大小已确定。
		- **系统盘**：SSD 云硬盘
		2. **数据盘**：SSD 云硬盘。也可在成功购买 GPU 实例后，[创建云硬盘 ](/doc/product/362/5744#.E5.88.9B.E5.BB.BA.E5.BC.B9.E6.80.A7.E4.BA.91.E7.9B.98)并挂载。
	- **网络**：选择网络类型（基础网络或私有网络）及公网带宽（按固定带宽计费或按使用流量计费）。
		- **网络类型**：
			1. 基础网络：适合新手用户，同一用户的云服务器内网互通。
			2. 私有网络：适合更高阶的用户，不同私有网络间逻辑隔离。
		2. **公网带宽**：
			1. 按带宽计费：选择固定带宽，超过本带宽时将丢包。适合网络波动较小的场景。
			2. 按使用流量计费：按实际使用流量收费。可限制峰值带宽，当瞬时带宽超过限制值时将丢包（适合网络波动较大的场景）。
2. 确定服务器数量及购买时长。
3. 设置完成后单击【下一步：设置主机】。

### 步骤5：设置主机
1. 新建或选择已有安全组，控制端口的开放范围。如下图所示：
![](https://main.qcloudimg.com/raw/008b9429231a35c9954feebf024ca203.png)
2. 设置 GPU 云服务器登录密码。
3. 单击【下一步：确认配置信息】。

### 步骤6：确认配置信息
1. 请在“确认配置信息”步骤中核对以下内容。如下图所示：
![](https://main.qcloudimg.com/raw/0f38e04d1daca2bd4c87832980df204d.png)
	- 确认实例规格、镜像选择、存储和带宽选择以及安全组等配置项是否符合预期。
	- 可选择或核对购买数量和购买时长。
2. 阅读并勾选“同意《腾讯云服务协议》和《退款规则》”，并单击【立即购买】。

### 步骤7：查收服务器

核实信息后完成支付，即可进入 [控制台](https://console.cloud.tencent.com/cvm) 的邮箱中查收云服务器。
完成 GA2 实例的购买后，您将会收到站内信，内容包括实例名称、公网 IP 地址、内网 IP 地址、登录名、初始登录密码等信息。可以使用这些信息登录和管理实例，也请尽快更改登录密码以保障主机安全性。

