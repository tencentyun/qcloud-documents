本文为您介绍如何创建 VPN 网关，您可通过如下视频了解 VPN 网关的基本操作。
>?视频仅介绍 VPN 的基本功能，界面以实际控制台为准。
>
<div class="doc-video-mod"><iframe src="https://cloud.tencent.com/edu/learning/quick-play/1786-20142?source=gw.doc.media&withPoster=1&notip=1"></iframe></div>

## 操作步骤
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。
2. 在左侧目录中单击 **VPN 连接** > **VPN 网关**，进入管理页。
3. 选择地域，如示例中的**广州**，单击**+新建**。
>? 若**+新建**显示灰色，且鼠标移至上方时显示“无可用私有网络”，请 [创建私有网络](https://cloud.tencent.com/document/product/215/36515) 后再进行新建 VPN 网关。 
>
4. 填写 VPN 网关名称（如 TomVPNGw），选择关联网络、所属网络、带宽上限、标签、计费方式，单击**创建**即可。VPN 网关创建完成后，系统随机分配公网 IP，如：`203.195.147.82`。
>?如果 VPN 网关使用200Mbps、500Mbps、1000Mbps和3000Mbps规格的带宽，VPN 通道加密协议建议使用 AES128+MD5。
>
<img src="https://qcloudimg.tencent-cloud.cn/raw/ef90c5804e09c2c5bb76f562a2026253.png" width="70%">
>?标签为选配，请保持默认。
>

## 相关文档
[步骤2：创建对端网关](https://cloud.tencent.com/document/product/554/18990)
[步骤3：创建 VPN 通道](https://cloud.tencent.com/document/product/554/18991)
[步骤4：本地网关加载配置](https://cloud.tencent.com/document/product/554/18992)
[步骤5：配置路由表](https://cloud.tencent.com/document/product/554/18993)
[步骤6：激活 VPN 隧道](https://cloud.tencent.com/document/product/554/18994)
