Grafana 可视化服务预设了远程图片渲染服务器，您无需任何额外操作即可使用图片渲染能力，本文列举常见的图片渲染使用场景。

## 操作前提
1. 登录 [Grafana 可视化服务控制台](https://console.cloud.tencent.com/monitor/grafana)。
2. 在实例列表中，找到对应的实例，单击 **Grafana 图标<img src="https://main.qcloudimg.com/raw/978c842f0c093a31df8d5240dd01016d.png" width="2%">**。
3. 输入 Grafana 账号和密码，进入 Grafana 后单击任意 Dashboard 。



## 分享面板

1. 在任意面板中，单击“标题”，选择弹窗中的“Share”。
   ![](https://qcloudimg.tencent-cloud.cn/raw/5762b723909024dab95eed1a9eed577d.png)
2. 单击弹窗尾部的 **Direct link rendered image**。
   ![](https://qcloudimg.tencent-cloud.cn/raw/49479bdfbb036b8cc69a7adb0f36fd6f.png)
3. 获得渲染为图片的面板地址并进行分享。
   ![](https://qcloudimg.tencent-cloud.cn/raw/324a5b8f710948d446525b8c550a18ad.png)


## 设置告警
同样，您可以在告警通道中选择 **Include Image**，在告警时将告警面板渲染为图片，具体设置可参考下图：
	![](https://qcloudimg.tencent-cloud.cn/raw/65eaa9e1ab618bc42c0f634c652ab250.png)

>?远程图片渲染不支持数据源为 Browser 类型的面板渲染。
