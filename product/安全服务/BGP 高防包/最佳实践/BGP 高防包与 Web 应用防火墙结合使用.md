BGP 高防包支持联动 Web 应用防火墙，为用户提供全方位安全防护。
- BGP 高防包一键提供上百Gbps DDoS 防护能力，轻松应对 DDoS 攻击，保障业务稳定运行。
- Web 应用防火墙实时防护，有效拦截 Web 攻击行为，保障用户业务的数据和信息安全。

## 部署方案
![](https://main.qcloudimg.com/raw/ee33e9c7fc15fdb97cfe784dade3a20f.png)

## 配置过程
### 配置 Web 应用防火墙
1. 登录 [Web 应用防火墙（网站管家）管理控制台](https://console.cloud.tencent.com/guanjia/waf/overview)。
2. 选择【网站应用防火墙】>【防护设置】。
 ![](https://main.qcloudimg.com/raw/b7d0c8b43b54a46b02f35543e366eeaa.png)
3. 单击【添加域名】，并根据实际情况设置以下参数。
 - 【域名配置】
    - 域名：输入需要防护的域名。
    - 协议类型：按实际情况选择。
    - 服务器端口：按实际情况选择。
    - 源站地址：输入需要防护网站的真实 IP 源站地址，即源站的公网 IP 地址。
 - 【其他配置】
 代理情况，请选择【是】。
 
 ![](https://main.qcloudimg.com/raw/8c8a5418fa322573433d98e8975c83fa.png)
3. 单击【保存】。

### 配置 BGP 高防包
1. 登录 [DDoS 防护（大禹）管理控制台](https://console.cloud.tencent.com/dayu/overview)，选择【BGP高防包】>【资产列表】，选择地域。
 - 若您的 BGP 高防包实例是独享型（单 IP 服务），则选择【单IP列表】页签。
 - 若您的 BGP 高防包实例是共享型（多 IP 服务），则选择【多IP列表】页签。
2. 单击目标 BGP高防包实例所在行的【绑定设备】或【更换设备】。
3. 在【绑定设备】页面，选择【关联设备类型】为【网站管家WAF】，设置【选择关联机器】为对应的 Web 应用防火墙（网站管家）的 IP。
 >?共享型 BGP 高防包（多 IP）实例可绑定多个网站管家 IP。
 
 ![](https://main.qcloudimg.com/raw/cba22debd9a1f5db3a2e64e3b30cf677.png)
4. 单击【确定】。
