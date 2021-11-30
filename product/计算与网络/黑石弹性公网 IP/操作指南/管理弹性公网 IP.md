## 操作场景
本文档指导您如何申请、绑定和解绑 EIP，以及释放弹性公网 IP 相关操作。

## 前提条件
已登录 [腾讯云控制台](https://console.cloud.tencent.com)。

## 操作步骤
### 申请 EIP
1. 打开 [黑石物理服务器控制台](https://console.cloud.tencent.com/cpm)，单击左侧菜单栏**弹性公网 IP**。
2. 单击**申请**，弹出 EIP 申请框。 
3. 选择计费模式与带宽峰值，单击**确定**，完成申请。

<dx-alert infotype="notice" title="">
- 每个腾讯云账户的每个地域最多可以申请100个黑石 EIP。
- 公网流量计费模式下设置的带宽峰值不是计费带宽，而是限速带宽，EIP 最大速率不会超过该处设置的带宽峰值。 
</dx-alert>




### 绑定 EIP
1. 打开 [黑石物理服务器控制台](https://console.cloud.tencent.com/cpm)，单击左侧菜单栏**弹性公网 IP**。
2. 找到您想用来绑定的 IP，单击**绑定**。
<dx-alert infotype="explain" title="">
若已绑定资源，则**绑定**将为不可用单击状态，需与原资源解绑后再绑定。
</dx-alert>
3. 在弹出框中选择您需要绑定的资源，单击**绑定**，即可完成绑定，此时开始收取公网出口费。
<dx-alert infotype="explain" title="">
按固定带宽计费的黑石弹性公网 IP 不可用于绑定 NAT 网关。
</dx-alert>



### 解绑 EIP
1. 打开 [黑石物理服务器控制台](https://console.cloud.tencent.com/cpm)，单击左侧菜单栏**弹性公网 IP**。
2. 在已绑定资源的黑石弹性公网 IP 列表项后，在更多选项中单击**解绑**，确认后即可解绑，此时开始收取 IP 闲置费。


### 释放弹性公网 IP
1. 打开 [黑石物理服务器控制台](https://console.cloud.tencent.com/cpm)，单击左侧菜单栏**弹性公网 IP**。
2. 在您想要释放的黑石弹性公网 IP，单击**释放**，释放后即不再计费。
<dx-alert infotype="explain" title="">
只有没有绑定资源的 EIP 才可以释放，如果已经绑定资源，请先解绑，然后再释放。
</dx-alert>


