##  购买须知
- 在购买腾讯云 GPU 云服务器前，请确保已了解 [腾讯云 GPU 云服务器](https://cloud.tencent.com/document/product/560/8015)，且已了解 [配置与价格](https://cloud.tencent.com/document/product/560/8025)，并根据实际需求购买。
- 确保了解所选 GPU 实例所在可用区，可用区信息请参考 [NVIDIA GPU 实例类型介绍](https://cloud.tencent.com/document/product/560/19700)。

##  购买步骤
本文以**实例类型 GN10** 为例，指导您按照以下步骤快速购买一台 GPU 云服务器：



### 步骤1：登录购买页面
<div style="background-color:#00A4FF; width: 190px; height: 35px; line-height:35px; text-align:center;"><a href="https://buy.cloud.tencent.com/?tab=custom&regionId=1&zoneId=100003&instanceType=GN10.2XLARGE40" target="_blank"  style="color: white; font-size:16px;" hotrep="document.guide.2764.btn2">点此进入购买页面</a></div>


### 步骤2：选择计费模式、网络、地域与机型
进入购买页后，选择计费模式、网络、地域及机型。如下图所示：
![](https://main.qcloudimg.com/raw/3e76ac796768b62a0aae9efb638008fd.png)
 - **计费模式**：**包年包月**或**按量计费**。
 - **地域及可用区**：可选择可用区以实际购买页为准，详情请参见 [NVIDIA 系列实例](https://cloud.tencent.com/document/product/560/19700)。
 - **网络**：选择现有私有网络或创建新私有网络。
 - **实例**：本文以选择 **GPU计算型GN10X**为例，请您按需选择。


### 步骤3：选择镜像

GPU 云服务器支持四种镜像类型：公共镜像、自定义镜像、共享镜像、镜像市场。详情请参见 [镜像概述](https://cloud.tencent.com/document/product/213/4940)。
刚开始使用腾讯云的用户，可选择**公共镜像**，并根据需要挑选版本。如下图所示：
![](https://main.qcloudimg.com/raw/7b249eacc1ab6d29bd9bb92bc0efcbfe.png)
<dx-alert infotype="notice" title="">
**GPU 云服务器必须具备相应的 GPU 驱动才能正常运行。** 您可通过以下4种方式，安装相应驱动：
 - 若选择**公共镜像**，则勾选**后台自动安装GPU驱动**即可预装相应版本驱动，建议您选择该方式。该方式仅支持部分 Linux 公共镜像，详情请参见 [GPU 驱动预装信息](#PreloadGPUDrive)。
 - 若选择**公有镜像**，则在 GPU 实例创建成功后，可参照 [安装 NVIDIA 驱动指引](https://cloud.tencent.com/document/product/560/8048) 手动安装相应驱动。
 - 若选择**镜像市场**，则可选择预装了 GPU 驱动的镜像，详情请参见 [使用预装 GPU 驱动的镜像](https://cloud.tencent.com/document/product/560/30129)。
 - 若您购买的是 vGPU 实例，则可选择已预装了 GRID 驱动的公共镜像，无需单独安装驱动。
</dx-alert>


### 步骤4：选择存储和带宽
1. 选择 GPU 云服务器的存储和带宽。如下图所示：
![](https://main.qcloudimg.com/raw/6be045d13c8d7d6d3aebb9571ef324e1.png)
主要参数信息如下：
	- **存储**：系统盘和数据盘类型和大小均灵活选择。
		- **系统盘**：普通云盘、SSD 云硬盘（仅限 GN2/GN8 实例）。
		- **数据盘**：普通云盘、高性能云硬盘、SSD 云硬盘（仅限 GN2/GN8 实例）。
	- **网络**：公网带宽，按固定带宽计费或按使用流量计费。
		- **按带宽计费**：选择固定带宽，超过本带宽时将丢包。适合网络波动较小的场景。
		- **按使用流量计费**：按实际使用流量收费。可限制峰值带宽，当瞬时带宽超过限制值时将丢包（适合网络波动较大的场景）。
2. 设置完成后单击**下一步：设置主机**。


### 步骤5：设置安全组和主机
1. 新建或选择已有安全组，控制端口的开放范围。如下图所示：
![](https://main.qcloudimg.com/raw/008b9429231a35c9954feebf024ca203.png)
2. 设置 GPU 云服务器登录密码。
3. 单击**下一步：确认配置信息**。 


### 步骤6：确认配置信息
1. 请在“确认配置信息”步骤中核对以下内容。如下图所示：
![](https://main.qcloudimg.com/raw/0887252d692c6016a733af7785391f61.png)
	- 确认实例规格、镜像选择、存储和带宽选择以及安全组等配置项是否符合预期。
	- 可选择或核对购买数量和购买时长。
2. 阅读并勾选“同意《腾讯云服务协议》和《退款规则》”，并单击**立即购买**。


### 步骤7：核对订单及付款
请核对订单信息，选择付款方式付款。
支付成功后，进入控制台，待实例创建启动完毕，即可进行登录操作。如下图所示：
![](https://main.qcloudimg.com/raw/f049933874cf300f16eefcd1aae5f017.png)


## 附录
### GPU 驱动预装信息[](id:PreloadGPUDrive)
GPU 云服务器支持部分 Linux 公共镜像通过后台自动安装 GPU 驱动。实例初次启动时，会根据所选版本自动安装 GPU 驱动、CUDA 及 cuDNN 库，耗时约15 - 20分钟。详细信息如下表：
<table>
        <thead>
        <tr>
            <th width="15%">GPU 驱动</th>
            <th width="15%">CUDA 版本</th>
            <th width="15%">cuDNN 版本</th>
            <th width="30%">支持的公共镜像版本</th>
            <th style="width: 26%;">支持的实例类型</th>
        </tr>
        </thead>
        <tbody>
            <tr>
                <td >450.102.04</td>
                <td>11.0.3</td>
                <td>8.1.0<br>8.0.5</td> 
                <td>CentOS 7.x<br>Ubuntu 18.04及以上</td>
                <td>GT4<br>GN10Xp<br>GN10X<br>GN8<br>GN7<br>GN6S</td>
            </tr>
        </tbody>
</table>



