## 操作场景
本文将指导您如何申请 EIP 并绑定云服务器。同时在 DNSPod 将 EIP 反向解析至域名，用于提升服务器 IP 及域名的信誉度。

## 前提条件
已购买 [PTR 反向解析增值服务](https://buy.dnspod.cn/dns/services)。

## 操作步骤

### 申请 EIP
1. 登录 [EIP 控制台](https://console.cloud.tencent.com/cvm/eip)。
2. 在 EIP 管理页面上方选择地域后，单击**申请**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/ded3c0945a742e9188780eaa892b9973.png)
3. 在弹出的 “申请EIP” 窗口中，输入需要申请的 EIP 数量后，单击**确定**即完成 EIP 的申请。
4. 返回 EIP 列表页面，可查看已申请的 EIP，此时处于未绑定状态。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/881bbe8e2f3f28d0b854e9bd83caab48.png)

### 绑定云服务器 CVM
1. 在 EIP 管理页面，选择已申请 EIP 所在行右侧的**更多** > **绑定**。
2. 在弹出的“绑定资源”窗口中，选择 EIP 要绑定的云服务器 CVM，单击**确定**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/01f14e9f4eae19a8ed2944dbacd00e41.png)
3. 在弹出的“确认绑定”提示框中，单击**确定**，即可完成与云资源的绑定。

### 添加 PTR 反向解析
1. 登录 DNSPod DNS 解析管理控制台，选择左侧导航栏中的 **DNS 解析** > **[反向解析](https://console.dnspod.cn/dns/ptr)**。
2. 在“反向解析”页面中，单击**添加 PTR 反向解析**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/f88b6da65507f35788e6486e40eb4bce.png)
3. 在弹出的“添加反向解析”窗口中，参考以下信息进行配置。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/b850e58f14c6ed0e1ce7fbbdeafa6b71.png)
 - **公网 IP**： 请选择上述已申请的弹性公网 IP。
 - **域名**： 请输入您希望公网 IP 所指向的域名名称。
 - **TTL 值**： 请选择您的 TTL 值。TTL 值越小，解析生效越快，TTL值越大，解析生效越慢。一般情况下生效时间于设置的 TTL 值相同。
4. 单击**确定**，即可完成操作。
<dx-alert infotype="explain" title="">
添加完成后需要等待解析生效，一般情况下生效时间与设置的 TTL 值相同。
</dx-alert>

