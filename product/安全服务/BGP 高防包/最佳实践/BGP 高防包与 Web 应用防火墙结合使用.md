DDoS 高防包支持联动 Web 应用防火墙，为用户提供全方位安全防护。
- DDoS 高防包一键提供上百 Gbps DDoS 防护能力，轻松应对 DDoS 攻击，保障业务稳定运行。
- Web 应用防火墙实时防护，有效拦截 Web 攻击行为，保障用户业务的数据和信息安全。

## 部署方案
![](https://main.qcloudimg.com/raw/5cf47d62a98ffd71bfa4e349ceae5d3d.png)
## 配置过程
### 配置 Web 应用防火墙
如需快速接入 Web 应用防火墙，详情请参见 [ Web 应用防火墙快速入门](https://cloud.tencent.com/document/product/627/18635)。
### 配置 DDoS 高防包
1. 登录 [DDoS 防护管理控制台](https://console.cloud.tencent.com/dayu/overview)，在左侧导航中，选择【DDoS 高防包】>【资产列表】。
 - 若您的 DDoS 高防包实例是独享包，则选择【独享包】页签。
 - 若您的 DDoS 高防包实例是共享包，则选择【共享包】页签。
 ![](https://main.qcloudimg.com/raw/d099f26f05047950267696dca78900d5.png)
2. 选择目的高防包实例所在地域，并在目的高防包实例所在行的右侧操作栏，单击【绑定设备】。
![](https://main.qcloudimg.com/raw/17f94d9b5c4b5cd927d52d1a1036560b.png)
3. 在【绑定设备】页面，选择【关联设备类型】为【Web 应用防火墙】，设置【选择关联机器】为对应 Web 应用防火墙防护的 IP 地址。 
 >?共享包实例可绑定多个 Web 应用防火墙防护的 IP 地址。
 
 ![](https://main.qcloudimg.com/raw/6a9cfb91b61adaca6ca19829596b7f6a.png)
 
4. 设置完成后，单击【确定】即可。
>?若是负载均衡型 Web 应用防火墙，在绑定界面选择【关联设备类型】为【负载均衡】，设置【选择关联机器】为对应负载均衡的公网 IP 地址。
