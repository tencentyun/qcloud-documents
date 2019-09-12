BGP 高防包支持联动 Web 应用防火墙，为用户提供全方位安全防护。
- BGP 高防包一键提供上百Gbps DDoS 防护能力，轻松应对 DDoS 攻击，保障业务稳定运行。
- Web 应用防火墙实时防护，有效拦截 Web 攻击行为，保障用户业务的数据和信息安全。

## 部署方案
![](https://main.qcloudimg.com/raw/ee33e9c7fc15fdb97cfe784dade3a20f.png)

## 配置过程
### 配置 Web 应用防火墙
1. 登录 [ Web 应用防火墙产品管理控制台](https://console.cloud.tencent.com/guanjia/waf/overview)。
2. 选择【Web 应用防火墙】>【防护设置】。
![](https://main.qcloudimg.com/raw/09f1e144ab90c2f72b0936e643c6df30.png)
3. 单击【添加域名】，并根据实际情况设置以下参数。
 - 【域名配置】
    - 域名：输入需要防护的域名。
    - 协议类型：按实际情况选择。
    - 开启 HTTP2.0：按实际情况选择。
    - 服务器端口：按实际情况选择。
    - 源站地址：输入需要防护网站的真实 IP 源站地址，即源站的公网 IP 地址。
 - 【其他配置】
    - 代理情况，请选择【是】。
    - 开启 WebSocket、负载均衡策略：按实际情况选择。

 ![](https://main.qcloudimg.com/raw/9dbd07bff87fb60c37d537a69b62fc4e.png)
4. 单击【保存】。

### 配置 BGP 高防包
1. 登录 [DDoS 防护（大禹）管理控制台](https://console.cloud.tencent.com/dayu/overview)，选择【BGP高防包】>【资产列表】。
 - 若您的 BGP 高防包实例是独享包，则选择【独享包】页签。
 - 若您的 BGP 高防包实例是共享包，则选择【共享包】页签。
2. 选择目的高防包实例所在地域，单击目的高防包实例所在行的操作项【绑定设备】。
![](https://main.qcloudimg.com/raw/771b07d20bf4eb9d8d3d5f912660d2d0.png)
3. 在【绑定设备】页面，选择【关联设备类型】为【网站管家 WAF】，设置【选择关联机器】为对应 Web 应用防火墙防护的 IP。 
 >?共享包实例可绑定多个 Web 应用防火墙防护的 IP。
 
 ![](https://main.qcloudimg.com/raw/6a9cfb91b61adaca6ca19829596b7f6a.png)
 
4. 单击【确定】。
