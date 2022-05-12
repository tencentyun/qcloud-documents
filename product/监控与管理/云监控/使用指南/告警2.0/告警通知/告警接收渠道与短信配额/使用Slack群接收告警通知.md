您只需在 Slack 中新增应用的 Webhook 地址，并在告警通知模板配置该地址，即可使用 Slack 群接收告警通知。

> ? Slack 群接收渠道暂不支持按通知时段接收告警通知。

## 步骤1：添加应用获取 Webhook 地址 

1. 进入 [Slack 应用管理页](https://api.slack.com/apps)。
2. 点击右上角的 **Create New App**，并选择 From scratch 方式创建。
3. 在配置页面填写应用名称，并选择对于的 Slack Workspace 创建一个 Slack APP。
4. 在应用管理页面左侧菜单栏中，选择 **Incoming Webhooks** 并单击右上角的开启按钮。
5. 滑动到子窗口底部，单击 **Add New Webhook to Workspace**。
<img src="https://qcloudimg.tencent-cloud.cn/raw/5ebbe0856c58f3a841f8f9793f01c7bc.png" height="60%" width="60%"> 
6. 在配置页面中选择对应的应用，并单击 **allow**。
7. 在跳转框中复制 Webhook 地址。
![](https://qcloudimg.tencent-cloud.cn/raw/b7d1ace9e752b8049700f2150d46a646.png)


## 步骤2：配置告警接口回调

1. 进入云监控控制台 > [通知模板](https://console.cloud.tencent.com/monitor/alarm2/notice ) 页面。
2. 单击**新建**，进入新建通知模板。
3. 在新建通知模板页配置完基础信息后，在**接口回调**处填写复制好的 webhook 地址。
![](https://qcloudimg.tencent-cloud.cn/raw/c4229a94a88ab59799994651619786f3.png)
4. 进入 [告警策略列表](https://console.cloud.tencent.com/monitor/alarm2/policy)，单击需要绑定告警回调的策略名称，进入管理告警策略页，并在告警策略页绑定通知模板。
![](https://qcloudimg.tencent-cloud.cn/raw/b829d61cdb8d33eebeb1e0100a901876.png)
 配置成功后，当告警策略被触发或恢复时，您可以在 Slack 群接收到云监控发送的告警通知，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/b45f704cf364895ab5ae86c0efb9b98f.png)
