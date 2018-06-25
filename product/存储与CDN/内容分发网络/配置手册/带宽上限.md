> 您可以对域名设置带宽封顶阈值，当域名在一个统计周期（5分钟）内产生的带宽超过指定阈值时，会根据您的配置将所有访问返回给源站，或直接关闭 CDN 服务，所有访问均返回 404。

## 配置指引

登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，选择左侧菜单栏的【域名管理】，单击您所要编辑的域名右侧的【管理】。
![](https://mc.qcloudimg.com/static/img/1f2cb594cd614b62b589cb20a20ed362/basic-config-1.png)
单击【高级配置】，您可以看到 **带宽封顶配置** 模块：
![](https://mc.qcloudimg.com/static/img/2cf8058f794333208085528176eaa1dc/cap-config-1.png)默认情况下，带宽封顶配置为关闭状态。单击按钮开启带宽封顶，默认情况下，带宽阈值为 **10Gbps**，到达阈值后会 **访问回源**：![](https://mc.qcloudimg.com/static/img/7d6147223cf12c886ddc2ca304db4f8e/cap-config-2.png)

![](https://mc.qcloudimg.com/static/img/6e6494dd03a95d0d3724d6f7f6062428/cap-config-3.png)

单击【编辑】图标，可以设置带宽阈值及超出阈值后对用户请求的处理方式。

- 若您的目的是抵抗超强 DDoS 攻击，为保护您的源站，推荐您设置为【访问返回404】。
- 若您的目的是控制 CDN 费用，为不影响您的服务，推荐您设置为【访问回源】。

超出封顶阈值后，我们会通过邮件、短信方式通知您，您可以在 CDN 控制台查看域名状态。不论设置为【访问回源】还是【访问返回 404】，域名均转为 **已关闭** 状态。【访问回源】/【访问返回 404】行为生效时间约为 **5-15 分钟**。
![](https://main.qcloudimg.com/raw/36f46240addd5c4cee2f68c52641ebce.png)
触发封顶带宽导致域名关闭后，若您希望继续使用 CDN 服务，可以在 [CDN 控制台](https://console.cloud.tencent.com/cdn) 中重新启动域名加速，具体操作请查阅 [域名操作](https://cloud.tencent.com/doc/product/228/5736)。

## 配置案例

若域名```www.test.com``` 配置如下：![](https://mc.qcloudimg.com/static/img/909fa76389ca8e486b7b1673885bddc8/cap-config-new-1.png)

CDN 会定频检测该域名最近的带宽统计监控数据，若 12:15:00 发现该域名在 12:05:00 时间点（代表12:05:00 ~ 12:10:00产生的数据）带宽值大于 1Kbps，超出设置上限，会立即下发配置，使请求回源，由于全网CDN节点的配置是批量下发，逐步生效，因此带宽会慢慢下降，约在12:20:00 左右全网生效。