若云服务器公网 IP 地址遭受到 DDoS 攻击，说明当前公网 IP 地址已经暴露。因此需要在接入高防 IP 后，更换已经暴露的公网 IP 地址，以避免攻击者绕过 DDoS 高防 IP，继续直接攻击主机 IP 地址。

如需更换云服务器的公网 IP 地址，详情请参见如下操作步骤：

## 一、 腾讯云服务器转弹性 IP
若当前云服务器的公网 IP 地址还不是弹性公网 IP，则需要先转换为弹性公网 IP 地址，以便于在更换后继续保留该 IP。
首先，进入 [腾讯云服务器控制台](https://console.cloud.tencent.com/cvm/overview)。在 “主IP地址列” 下，单击 “转换为弹性 IP” 按钮，单击【确定转换】。
![](https://main.qcloudimg.com/raw/fe92e1b6dfb7db8ab4ce60b23ea20382.png)
>**说明：**
>将当前公网 IP转换为弹性 IP 地址，转发过程不会中断服务。

## 二、 弹性 IP 转公网 IP
在 “操作” 列 “更多” 下，选择 “IP 操作” 里的 “解绑弹性 IP”，并同时勾选 “解绑后免费分配公网 IP”，单击 【确定】。此时云服务器的 IP 已更为新的公网 IP 地址。
![](https://main.qcloudimg.com/raw/7b17baa39966082c9e9141df34b6da6d.png)
![](https://main.qcloudimg.com/raw/f53d07b45b605f774b92cbacd7d13234.png)

>**注意：**
>若用户的云服务器已经使用了弹性公网 IP，则可以直接绑定为其他已有的弹性公网 IP。

在选择第一步操作时，将单击 【确定转换】变为单击 【其他弹性公网 IP】；立即跳转到 “绑定弹性公网 IP”，单击 "选择弹性公网 IP" 框，选择好 IP，单击【确认】，即为云服务器分配了新的公网 IP 地址。
![](https://main.qcloudimg.com/raw/f723f59784620ef56f52bed7b5ba773d.png)
![](
https://main.qcloudimg.com/raw/b7ab651d329a3281b2095a21cfc11f37.png)
