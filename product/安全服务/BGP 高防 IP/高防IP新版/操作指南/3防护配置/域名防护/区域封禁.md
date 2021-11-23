DDoS 高防 IP 支持对已接入防护的网站业务设置基于地理区域的访问请求封禁策略。开启针对域名的区域封禁功能后，您可以一键阻断指定地区来源IP对网站业务的所有访问请求。支持多地区、国家进行流量封禁。
>?在配置了区域封禁后，该区域的攻击流量依然会被平台统计和记录，但不会流入业务源站。

## 前提条件
您需要成功 [购买 DDoS 高防 IP ](https://cloud.tencent.com/document/product/1014/44082) ，并设置防护对象并接入了域名业务的防护。

## 操作步骤
1. 登录 [DDoS 高防 IP（新版）管理控制台](https://console.cloud.tencent.com/ddos/antiddos-advanced/config/port) ，在左侧导航中，单击 **DDoS 高防 IP** > **防护配置**。
2. 在左边的列表选中有接入域名防护的高防 IP 的 ID，如“xxx.xx.xx.xx bgpip-000003n2”。
![](https://qcloudimg.tencent-cloud.cn/raw/3ec2332faedae900f600877e17fa2bf7.png)
3. 在右侧卡片中单击**区域封禁**卡片中的**设置**，进入区域封禁页面。
![](https://qcloudimg.tencent-cloud.cn/raw/5dff892b71192f133334966272a5abbb.png)
4. 在区域封禁页面，单击**新建**。
![](https://qcloudimg.tencent-cloud.cn/raw/cb96e3225162b7d051aeb5739f7ed7f1.png)
5. 在新建区域封禁弹窗中，选择 IP、协议、域名和所封禁的区域，单击**确定**，创建区域封禁规则。
![](https://qcloudimg.tencent-cloud.cn/raw/6fc4b90e54bab026b6c4eb7f2829077d.png)
6. 新建完成后，在区域封禁列表，将新增一条区域封禁规则，可以在右侧操作列，单击**配置**，修改区域封禁规则。
![](https://qcloudimg.tencent-cloud.cn/raw/7973de77786cafea3fa79b626bd91418.png)
