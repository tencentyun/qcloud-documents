## 操作场景
本文介绍如何在 CVM 实例上配置 EFI，实现在 VPC 网络下体验超低延迟的 RDMA 功能。**弹性 RDMA 网卡**（Elastic Fabric Interface，EFI）是一种可以绑定到 CVM 实例的虚拟网卡，EFI 必须依附于弹性网卡（ENI）开启 RDMA 设备。EFI 完全复用了弹性网卡所属的网络，让您无需改变业务组网，即可在原有网络下使用 RDMA 功能，体验 RDMA 带来的超低延迟。

EFI 相比于传统的 TCP 传输，提供更低的延迟和更高的吞吐量，能够提高实例间的通信性能，这对于扩展 HPC 和机器学习应用程序至关重要。弹性 RDMA 网卡 EFI 具有以下优势：
- **低延迟**：RDMA（Remote Direct Memory Access）功能绕过操作系统直接读写远端服务器内存，极大地降低了 CPU 负载和延迟。EFI 使弹性网卡具有传统 RDMA 网卡的优点，您可以在腾讯云 CVM 中体验超低的延迟。
- **规模部署**：传统的 RDMA 功能依赖于网络的无损特性，在规模部署时难度高且成本高。而 EFI 采用了自研的拥塞控制算法，容忍 CVM 网络中的延迟、丢包等问题，在有损的网络环境中依然可以有良好的性能表现。
- **弹性扩展**：EFI 依附于弹性网卡，您可以随时创建支持EFI的弹性网卡并绑定到 CVM 实例，也可以随时解绑或删除该附属弹性网卡，轻松实现弹性扩展。

## **操作步骤**
<dx-alert infotype="explain" title="">
EFI 功能正在邀测中，邀测支持 GPU 计算型 PNV4ne。如需使用，请提交 [内测申请](https://cloud.tencent.com/apply/p/ik9q4vieb4)。
</dx-alert>
1. 创建支持 EFI 的 CVM 实例。

   具体操作，请参见 [通过购买页创建实例](https://cloud.tencent.com/document/product/213/4855)。在创建支持 EFI 的 CVM 实例时，请注意下表中的配置项。

| 配置项       | 说明                                                         |
| ------------ | ------------------------------------------------------------ |
| 地域及可用区 | 支持选择：上海-上海五区                                      |
| 实例族及类型 | 支持 EFI 的实例规格如下：<br />实例族：GPU 机型<br />类型：GPU 计算型 PNV4ne |
| 镜像         | 从以下镜像中选择一款镜像：<br />TencentOS Server 3.1(TK4) <br />TencentOS Server 2.4 |

2. 两种方式创建启用 EFI 的弹性网卡。


 - 在实例控制台创建并绑定。

  i. 登录 [实例控制台](https://console.cloud.tencent.com/cvm/instance)。

  ii. 选择实例，选择**弹性网卡**列表页，单击**绑定弹性网卡。**

  iii. 选择**新建弹性网卡并绑定，**打开**弹性 RDMA 接口**开关。
 <dx-alert infotype="explain" title="">
- 单台实例最多绑定一个启用 EFI 的辅助弹性网卡。
- 绑定辅助网卡至实例前，请确认目标实例的主网卡和辅助网卡不在同一子网内，否则可能因为默认路由导致辅助网卡的 RDMA 功能在某些情况下不可用。如果您知道如何解决并确定要这样使用，请忽略本提示。
- 若需要实现多个支持 EFI 的实例间通信，请保证不同实例的 EFI 弹性网卡在同 vpc 同子网内。
 </dx-alert>
 
  <img style="width:750px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/da433af559635f216c064c74c8d2d9bf.png" />

 将启用 EFI 的辅助弹性网卡绑定至实例后，如需解绑，必须先停止压力，即停止实例内的通信操作。

  iv. 点击**确定**即可。
	
- 私有网络控制台创建后绑定。

  i. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc)。

  ii. 单击左侧目录中的 **IP 与网卡>弹性网卡**，进入弹性网卡列表页。

  iii. 选择地区和私有网络，单击+新建。

  iv. 在弹窗中输入名称，选择辅助弹性网卡的所属私有网络、子网后，为网卡分配 IP，打开**弹性 RDMA 接口**开关。   
	
	 <img style="width:750px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/d907dd8c2625d1c1cbebb5f3a7b90412.png" />

  v. 点击 **确定** 即可。

  vi. 登录 [实例控制台](https://console.cloud.tencent.com/cvm/instance)。

  vii. 选择实例，选择 **弹性网卡** 列表页，单击 **绑定弹性网卡。**

  viii. 选择 **绑定已有弹性网卡**，在列表中选择上述步骤中新建的弹性网卡。
 <dx-alert infotype="explain" title="">
- 单台实例最多绑定一个启用 EFI 的辅助弹性网卡。
- 绑定辅助网卡至实例前，请确认目标实例的主网卡和辅助网卡不在同一子网内，否则可能因为默认路由导致辅助网卡的 RDMA 功能在某些情况下不可用。如果您知道如何解决并确定要这样使用，请忽略本提示。
- 若需要实现多个支持 EFI 的实例间通信，请保证不同实例的 EFI 弹性网卡在同 vpc 同子网内。
 </dx-alert>
  <img style="width:750px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/883f7131ae7b8c0f36969a7ca16c1c23.png" />

 ix. 点击**确定**即可。


3. 远程连接 CVM 实例。

   具体操作，请参见 [登录 Linux 实例](https://cloud.tencent.com/document/product/213/16515)。

4. 在实例内查看弹性网卡。

 您可以执行 ifconfig 命令查看是否可以显示该网卡。某些低版本的内核可能需要手动配置 IP，具体操作，请参见 [Linux 云服务器配置弹性网卡](https://cloud.tencent.com/document/product/576/59353)。

5. 在实例内安装 EFI 驱动。

 i. 下载驱动安装包，请联系您的商务经理以获取最新版本。

 ii. 运行以下命令，解压安装包并进入文件目录。

 ```plaintext
tar -xvf vrdma_bundle.tgz && cd vrdma_bundle
 ```

 iii. 运行以下命令，安装驱动。

 ```plaintext
sh install.sh
 ```

 iv. 确认安装结果。

 - 当出现如下信息时，表示安装成功。                
  <img style="width:750px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/dfaf630688c7f409424b982d992fdbe0.png" />
 - 如果提示安装失败，您可以查看错误输出进行相关操作，尝试重新安装驱动。

