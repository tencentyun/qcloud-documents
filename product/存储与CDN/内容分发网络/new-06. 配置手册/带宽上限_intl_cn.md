您可以对域名设置带宽封顶阈值，当域名在一个统计周期（5分钟）内产生的带宽超过指定阈值时，会根据您的配置将所有访问返回给源站，或直接关闭 CDN 服务，所有访问均返回 404。

## 配置说明
登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，选择左侧菜单栏的【域名管理】，单击您所要编辑的域名右侧的【管理】。
![](https://mc.qcloudimg.com/static/img/f2f50e0d81eb0a8c0dcb61d2ee37e6c9/manage.png)
单击【高级配置】，您可以看到 **带宽封顶配置** 模块。
![](https://mc.qcloudimg.com/static/img/8dff0e8c681840cea53dbeabd21633da/bandwidth.png)

### 默认配置
默认情况下，带宽封顶配置为关闭状态。

### 自定义配置
单击按钮开启带宽封顶，默认情况下，带宽阈值为 **10Gbps**，到达阈值后会 **访问回源**。
![](https://mc.qcloudimg.com/static/img/f9ba5c3e65e733bcf735576ea24a2baa/bandwidth_open.png)
单击【编辑】图标，可以设置带宽阈值及超出阈值后对用户请求的处理方式。
**带宽阈值** 设置：
- 若您设置的带宽阈值为 100Mbps（即 10 兆比特位每秒），由于电脑以字节为最小存储单位，1字节=8比特位，则 100Mbps=12.5MB/s（即12.5兆字节每秒）。
- CDN 对您的域名统计周期为 5 分钟（300 秒），由此得出流量消耗的最大值为 12.5 x 300 = 3750MB 。
- 则当您设置的带宽阈值为 100Mbps 时，若该域名在 5 分钟内产生的流量消耗超过 3750MB ，超出封顶阈值。

**超出处理** 设置：
- 若您的目的是抵抗超强 DDoS 攻击，为保护您的源站，推荐您设置为【访问返回404】。
- 若您的目的是控制 CDN 费用，为不影响您的服务，推荐您设置为【访问回源】。

![](https://mc.qcloudimg.com/static/img/fcf56965292d6b98ea4f31a9736fd314/bandwidth_set.png)
超出封顶阈值后，我们会通过邮件、短信方式通知您，您可以在 CDN 控制台查看域名状态。不论设置为【访问回源】还是【访问返回 404】，域名均转为 **已关闭** 状态。【访问回源】/【访问返回 404】行为生效时间约为 **5-15 分钟**。
![](https://mc.qcloudimg.com/static/img/bcecdc954dfd6bab53f7a5104de2542a/bandwidth_over.png)
触发封顶带宽导致域名关闭后，若您希望继续使用 CDN 服务，可以在 [CDN 控制台](https://console.cloud.tencent.com/cdn) 中重新启动域名加速，具体操作请查阅 [域名操作](https://cloud.tencent.com/doc/product/228/5736)。