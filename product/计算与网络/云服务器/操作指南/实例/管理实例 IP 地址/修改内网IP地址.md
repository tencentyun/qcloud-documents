## 操作场景

您可以在控制台中直接修改私有网络中云服务器（Cloud Virtual Machine，CVM）实例的内网 IP，也可以通过更换 CVM 实例所属的子网来更改实例的内网 IP。本文档指导您在云服务器控制台中，修改私有网络中 CVM 实例的内网 IP。
关于更换子网的操作，请参考 [更换实例子网](https://cloud.tencent.com/document/product/213/16565)。

## 限制条件

- 修改主网卡的主 IP 会导致关联的云服务器自动重启。
- 辅助网卡无法修改主 IP。

## 操作步骤

1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)。
2. 选择待修改内网 IP 的实例所属地域，并单击该实例的 ID/实例名，进入实例详情页面。
3. 在实例详情页面，选择**弹性网卡**页签，单击 <img src="https://main.qcloudimg.com/raw/57a0c76b72cd97bd80bf857cd30c867a.png" style="margin: 0;"></img> 展开主网卡。如下图所示：
![](https://main.qcloudimg.com/raw/591d5ef59e5c9d782621641065ed50fb.png)
4. 在主网卡的操作列，单击**修改主IP**。
5. 在弹出的 “修改主IP” 窗口中，输入新的 IP，单击**确定**，等待实例完成重启即可生效。
<dx-alert infotype="notice" title="">
只能填入属于当前子网 CIDR 的内网 IP。
</dx-alert>





