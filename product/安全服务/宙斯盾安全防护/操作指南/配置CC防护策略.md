##配置CC防护策略
宙斯盾安全防护（Aegis Anti-DDoS）提供HTTP CC高级防护策略。CC防护策略，当设置HTTP请求数超过设定的QPS值时，才会触发CC防护。更详细的配置说明，【请参见】[**自定义安全策略**](http://文档_快速入门_自定义安全策略.md "文档_快速入门_自定义安全策略")。

###添加CC防护策略
1.进入宙斯盾高防的“CC防护策略”管理中心，点击“添加新策略”。添加成功后，点击“操作”列下的“配置”进入策略配置页面。

![](https://i.imgur.com/8GVJoNl.png)

2.根据业务特点和防护需求配置HTTP QPS请求阈值，URL白名单，IP黑白名单，CC自定义防护模式等策略。最后点击保存即添加策略成功。

![](https://i.imgur.com/Z8jUZDx.png)

###一、CC防护策略直接绑定防护IP
进入CC防护策略列表，点击策略ID，选择添加IP。

![](https://i.imgur.com/u9VnZdW.png)

![](https://i.imgur.com/yGpHoy5.png)

###二、DDoS高防IP绑定CC防护策略
进入DDoS高防IP列表，点击高防IP，点击高级配置信息。“绑定”，选择好CC防护策略点击确认。

![](https://i.imgur.com/dwbDDpL.png)

![](https://i.imgur.com/45seGwX.png)

###三、给DDoS高防包下的防护IP配置CC防护策略
进入DDoS高防包列表，点击高防包ID，选择“防护IP列表”，勾选需要配置的IP，点击“配置CC防护策略”。

![](https://i.imgur.com/2Eta12M.png)

![](https://i.imgur.com/2pIa0T2.png)
