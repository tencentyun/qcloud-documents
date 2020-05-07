1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。
2. 在左侧目录中单击【VPN连接】>【VPN网关】，进入管理页。
3. 选择地域，如示例中的广州，单击【+新建】。
4. 在弹出的“新建VPN网关”窗口中，填写 VPN 网关名称（如 TomVPNGw），选择关联网络、带宽上限、计费方式，单击【创建】即可。VPN 网关创建完成后，系统随机分配公网 IP，如 `203.195.147.82`。
 - 网关名称：填写 VPN 网关名称，不超过60个字符。
 - 关联网络：选择云联网。
 - 带宽上限：按需选择 VPN 网关的带宽上限。
 - 计费方式：按需选择 VPN 网关的计费方式。
    - 按流量计费：适用于带宽波动较大的场景。
     - 包年包月： 适用于带宽较稳定的场景。
![](https://main.qcloudimg.com/raw/a524d91fc73e82de17efe299d5a26a0e.png)
5. 单击已创建的云联网型 VPN 网关 ID，进入详情页。
![](https://main.qcloudimg.com/raw/6a63fef0d1e854e3e7ba2520fe2008f6.png)
6. 单击所属网络右侧的<img src="https://main.qcloudimg.com/raw/7b27e195bfc7f7ee82118f80c4c96b28.png" style="margin:-4px 0;"/>，选择需要关联的云联网，并单击【保存】，将云联网型 VPN 网关关联至云联网实例。
![](https://main.qcloudimg.com/raw/4b201b74b503d320ebd837403990ded5.png)
7. 完成云联网型 VPN 网关关联至云联网实例后，请执行如下操作：
 - [创建对端网关](https://cloud.tencent.com/document/product/554/18990)
 - [创建 VPN 通道](https://cloud.tencent.com/document/product/554/18991)（VPN 网关类型请选择云联网）
8. 在创建 VPN 通道过程中，会设置 SPD 策略，SPD 策略中的对端网段可以加入云联网中，具体操作如下：
 1. 在完成 VPN 通道创建后，单击云联网型 VPN 网关 ID，进入 VPN 网关详情页。
![](https://main.qcloudimg.com/raw/6a63fef0d1e854e3e7ba2520fe2008f6.png)
 2. 选择【IDC网段】标签页，在该页面启用或停用需要加入到云联网的 IDC 网段。
![](https://main.qcloudimg.com/raw/a89ee3e76a107910127c9a1d959930bb.png)
 3. 启用 IDC 网段后，IDC 网段将加入云联网中，云联网中路由表指向该 IDC 网段的下一跳为该云联网型 VPN 网关。
12. 完成如上配置后，IDC 通过 VPN 网关接入云联网的配置完成。
