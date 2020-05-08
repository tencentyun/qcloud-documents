## 操作场景

本文档指导您如何更换公网 IP 地址，更换公网 IP 分为以下两种方式：
- [直接更换公网 IP](#ReplacementPublicIP)
- [先更换为弹性公网 IP，再解绑弹性公网 IP（仅非带宽上移账户适用）](#ReplacementEIP)

## 注意事项
如果您选择**直接更换公网 IP**，请注意以下事项：
- 单个账号单个地域不超过3次/天。
- 单台实例**仅允许更换1次**公网 IP。
- **更换后原公网 IP 将被释放。**

如果您选择**先更换为弹性公网 IP，再解绑弹性公网 IP**，请注意以下事项：
- 弹性 IP 地址与云服务器实例绑定时，实例的当前公网 IP 地址会被释放。
- 单个账户单个地域配额弹性公网 IP 个数为20个。
- 为保证 IP 资源有效利用，未绑定实例的弹性公网 IP，将按小时收取少量费用。
弹性公网 IP 的计费详情可参见 [弹性公网 IP 计费](https://cloud.tencent.com/document/product/213/17156)。

## 操作步骤
<span id="ReplacementPublicIP"></span>
### 方式一：直接更换公网 IP
1. 登录  [云服务器控制台](https://console.cloud.tencent.com/cvm/index)。
2. 在实例的管理页面，选择待转换 IP 的云服务器地域，并在对应云服务器所在行，单击【更多】>【IP/网卡】>【更换公网IP】，如下图所示：
![](https://main.qcloudimg.com/raw/23c277a820f39416d72115689dae3575.png)
3. 在弹出的 “更换IP” 提示框中，单击【确认】，即可完成更换。

<span id="ReplacementEIP"></span>
### 方式二：先更换为弹性公网 IP，再解绑弹性公网 IP
>?此方式仅非带宽上移账户适用。
>
#### 更换弹性公网 IP
1. 登录  [云服务器控制台](https://console.cloud.tencent.com/cvm/index)。
2. 在实例的管理页面，选择待转换 IP 的云服务器地域，并在对应云服务器所在行，单击<img src="https://main.qcloudimg.com/raw/25e8c0e37b73c12da900301f03e57dbc.png" style="margin: 0;"></img>。如下图所示：
![](https://main.qcloudimg.com/raw/37c7718c0e50992ac6b4d26b3cf7205d.png)
3. 在弹出的 “转换为弹性公网IP” 窗口中，单击【确定】。

#### 解绑弹性公网 IP
1. 待完成转换后，在对应云服务器所在行，单击【更多】>【IP/网卡】>【解绑弹性IP】。如下图所示：
![](https://main.qcloudimg.com/raw/ac7450b6bc243627597493d0aeb4502b.png)
2. 在弹出的 “解绑弹性公网IP” 窗口中，勾选【解绑后免费分配公网IP】，单击【确定】。如下图所示：
![](https://main.qcloudimg.com/raw/8197e4ea54bb8c99abd69bd64c2e97b1.png)
3. 在弹出的提示框中，单击【确定】，即可完成更换。

#### 释放弹性公网 IP（可选）
>? 由于解绑弹性公网 IP 时，解绑的弹性公网 IP 仍保留在该账号下，为避免闲置不使用的 IP 继续收取费用，建议执行以下操作，释放未绑定实例的弹性公网 IP。
>
1. 登录 [弹性公网 IP 控制台](https://console.cloud.tencent.com/cvm/eip)。
2. 在弹性公网 IP 管理页面，选择刚解绑的弹性公网 IP，单击【更多】>【释放】。
3. 在弹出的 “确定释放所选弹性公网IP？” 窗口中，勾选【确定释放以上IP】，单击【释放】。


