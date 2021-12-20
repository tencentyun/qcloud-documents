1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。
2. 在左侧目录中单击【VPN 连接】>【VPN 网关】，进入管理页。
3. 选择地域，如示例中的**东京**，单击【+新建】。
>? 若【+新建】显示灰色，且鼠标移至上方时显示“无可用私有网络”，请 [创建私有网络](https://cloud.tencent.com/document/product/215/36515#.E5.88.9B.E5.BB.BA-vpc.3Ca-id.3D.221.22.3E.3C.2Fa.3E) 后再进行新建 VPN 网关。 
>
![](https://main.qcloudimg.com/raw/ec9534a52ebcc712430ae1b8d3f8b094.png)
4. 在弹出的创建对话框中填写 VPN 网关名称（如 VPN1），选择关联网络为私有网络、所属网络选择 VPC1，设置带宽上限及计费方式等。
>?
>- 200MB、500MB和1000MB带宽目前仅华北地区（北京）、华东地区（上海）、华南地区（广州）、西南地区（成都）、港澳台地区（香港）、华东地区（南京）和华北地区（北京金融）等可用区开放，如需请 <a href="https://console.cloud.tencent.com/workorder/category">提交工单</a>。
>- 200MB、500MB和1000MB带宽仅支持新建网关，存量量网关暂不支持。
>- 如果 VPN 网关使用200MB、500MB和1000MB规格的带宽，VPN 通道加密协议建议使用 AES128+MD5。
>
![](https://main.qcloudimg.com/raw/a83b3302580faaa5faec4e1d79d96f66.png)
5. 单击【创建】。VPN 网关创建完成后，系统随机分配公网 IP，如：`124.156.239.133`。
  ![](https://main.qcloudimg.com/raw/e906f7c547bb29fb267c3370039c3541.png)
