DDoS 高防包支持联动 Web 应用防火墙，为用户提供全方位安全防护。
- DDoS 高防包一键提供上百 Gbps DDoS 防护能力，轻松应对 DDoS 攻击，保障业务稳定运行。
- Web 应用防火墙实时防护，有效拦截 Web 攻击行为，保障用户业务的数据和信息安全。

## 部署方案
![](https://main.qcloudimg.com/raw/5cf47d62a98ffd71bfa4e349ceae5d3d.png)

## 配置过程
### 配置 Web 应用防火墙
如需快速接入 Web 应用防火墙，详情请参见 [ Web 应用防火墙快速入门](https://cloud.tencent.com/document/product/627/18635)。
### 配置 DDoS 高防包
1. 登录 [DDoS 高防包（新版）控制台](https://console.cloud.tencent.com/ddos/antiddos-native/package)，在左侧操作栏中，单击【高防包】。
2. 选择目的高防包实例所在地域，单击目的高防包实例所在行的操作项【管理防护对象】。
![](https://main.qcloudimg.com/raw/648442ef2abb4a46860a294313b3ebdc.png)
3. 在管理防护对象页面，根据实际防护需求选择“关联设备类型”与“选择资源实例”。
  - 关联设备类型：支持云服务器，负载均衡，Web 应用防火墙等公有云具有公网IP的资源。
  - 选择资源实例：允许多选，选择资源实例数量不得超过“可绑定 IP 数”。
![](https://main.qcloudimg.com/raw/823086290f675dc43e109e28fda3b8d9.png)
4. 设置完成后，单击【确定】即可。
