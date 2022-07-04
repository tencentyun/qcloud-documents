## 操作场景
本文介绍如何通过控制台访问 CHC 物理服务器的 BMC（带外管理）界面。

<dx-alert infotype="explain" title="">
不同厂商的服务器的 BMC 界面和功能并不相同，本文以 H3C 服务器的 BMC 界面为例。
</dx-alert>




## 前提条件

在进行登录操作前，您需完成 [接入指引](https://cloud.tencent.com/document/product/1448/60642) 中的前7个步骤。CHC 物理服务器应处于“可生产”或“已生产”状态。

## 操作步骤


### 准备跳板机
由于 CHC 物理服务器的带外网络不支持绑定弹性公网 IP（EIP），因此需要使用跳板机访问服务器的 BMC。跳板机需为 Windows 操作系统，且需与 CHC 物理服务器的带外 VPC 互通。常用跳板机如下：

- 在同 VPC 下创建一台 Windows 操作系统云服务器
- 在对等连接或云联网互通的 VPC 下创建一台 Windows 操作系统云服务器
- 和带外 VPC 专线可达的 IDC 的 Windows 服务器


### 访问服务器的 BMC
1. 参考 [登录 Windows 实例](https://cloud.tencent.com/document/product/213/35697)，登录 Windows 服务器。
2. 执行 ping 命令访问 CHC 物理服务器的带外 IP，判断网络是否可通。返回结果如下图所示，表示网络可通：
![](https://qcloudimg.tencent-cloud.cn/raw/7f771669c5a69d1568c12782a187e517.png)
3. 在浏览器访问输入 CHC 物理服务器带外网络的 IP 地址，访问服务器 BMC。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/8bc40e7ce0b6a8660e1aef6c53f3ef2e.png)
4. 输入用户名及密码，单击**登录**。


### 访问带外管理控制台
1. 服务器 BMC 登录成功后，选择左侧导航栏中的**远程控制**，选择合适的访问方式，即可访问带外管理控制台。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/848d259090bd95afd53bd3bde27296b4.png)
<dx-alert infotype="notice" title="">
部分服务器 BMC 仅支持通过 Java 远程控制，此时需要安装特定版本的 Java，具体版本请与服务器供应商联系。
</dx-alert>
2. 此时，可以在带外管理控制台上访问到服务器的操作系统。如下图所示：
<img src="https://qcloudimg.tencent-cloud.cn/raw/132492e809857a158d686bba91a6b6dc.png"/>










