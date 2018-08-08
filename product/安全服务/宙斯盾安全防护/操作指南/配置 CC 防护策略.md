
宙斯盾安全防护（Aegis Anti-DDoS）提供 HTTP CC 高级防护策略。CC 防护策略，当设置 HTTP 请求数超过设定的 QPS 值时，才会触发 CC 防护。更详细的配置说明，详情请参见 [**自定义安全策略**](http://文档_快速入门_自定义安全策略.md "文档_快速入门_自定义安全策略")。

### 添加 CC 防护策略
1. 进入宙斯盾高防的 “CC 防护策略” 管理中心，单击【添加新策略】。添加成功后，单击 “操作” 列下的 “配置” 进入策略配置页面。
![](https://i.imgur.com/8GVJoNl.png)
2. 根据业务特点和防护需求配置 HTTP QPS 请求阈值、URL 白名单、IP 黑白名单、CC 自定义防护模式等策略。最后单击保存即添加策略成功。
![](https://i.imgur.com/Z8jUZDx.png)

### CC 防护策略直接绑定防护 IP
1. 进入 CC 防护策略列表，单击策略 ID。
![](https://i.imgur.com/u9VnZdW.png)
2. 选择绑定 IP列表，单击【添加 IP】。
![](https://i.imgur.com/yGpHoy5.png)

### DDoS 高防 IP 绑定 CC 防护策略
1. 进入 DDoS 高防 IP 列表，单击 “高防 IP”。
![](https://i.imgur.com/dwbDDpL.png)
2. 单击 “高级配置信息”。单击 “绑定”，选择好 CC 防护策略，单击【确认】。
![](https://i.imgur.com/45seGwX.png)

### 给 DDoS 高防包下的防护 IP 配置 CC 防护策略
1. 进入 DDoS 高防包列表，单击 “高防包 ID”。
![](https://i.imgur.com/2Eta12M.png)
2. 选择 “防护IP列表”，勾选需要配置的 IP，单击 “配置 CC 防护策略”
![](https://i.imgur.com/2pIa0T2.png)
