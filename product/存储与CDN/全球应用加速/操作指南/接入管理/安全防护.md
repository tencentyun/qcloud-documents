GAAP 默认提供基础安全防护策略（普通用户是 2Gbps 带宽，VIP 用户是 10Gbps 带宽）。如需升级到高级防护策略，可在 DDoS 高防包控制台-云资产升级防护。

另外 GAAP 控制台提供安全防护可支持配置黑白名单。详细配置方法如下：
1.	登录 [全球应用加速控制台](https://console.cloud.tencent.com/gaap)，进入“接入管理”页面，单击指定通道的 **ID/通道名**。
2.	进入到下一级页面，选择**安全防护** > **添加规则**，可进入向导，具体配置如下：
	1. 添加访问规则，选择默认准许/拒绝所有流量访问通道。
	 ![](https://main.qcloudimg.com/raw/db45ecb4382cfc75b632f086caba4d2a.png)
	2. 添加来源IP，选择协议并添加协议端口。之后选择“允许”/“拒绝”该IP的访问。
<img src="https://main.qcloudimg.com/raw/435c2ede3aa58b20060e828cad9db856.png" width="50%">
>? i. 可添加的访问规则最多为100个。
>
3.	单击**确定**。
