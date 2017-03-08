##1.BGP高防IP快速接入（业务部署在非腾讯云）

登录“大禹网络安全”控制台，在“BGP高防IP”控制页中找到您已经开通的高防IP实例，点击实例ID，进入配置页面
![](https://mc.qcloudimg.com/static/img/fd9063bdf1f69cb2f4c5bd73d1764787/image.png)

在“转发规则”配置栏中点击“新建”按钮，新建转发规则。按下图所示，首先选择转发规则（目前支持TCP协议），再填写转发端口（最终想通过高防IP的哪个端口来访问，一般来说跟源站端口是相同的），然后填写源站端口（源站提供服务的真实端口）和源站IP

![](https://mc.qcloudimg.com/static/img/86a466a99e39b3a04685644e00d105b7/image.png)

注意：

- 如果一个域名对应多个源站IP，可以都写进去，最多支持20个。不同的源站IP之间英文分号";"分隔；
- 用多个源站之间会以轮询方式做负载均衡；
- 一个高防IP支持配置60条转发规则；

点击“确定”后会生成一条转发规则。

高防IP暂不支持配置七层转发，敬请期待。

##2.BGP高防IP快速接入（业务部署在腾讯云）
**第一步** 登陆高防IP控制后台,选择相应地域云内高防IP[https://console.qcloud.com/dayu/bgpip/list/gz](https://console.qcloud.com/dayu/bgpip/list/gz)
![](https://mc.qcloudimg.com/static/img/77f84c2fa6f0b717c14359ba034dd457/image.png)

**第二步** 创建监听器

基本配置根据业务情况设置相应的协议端口,高防IP是四层转发,7层应用协议如http等也是选择tcp,如下图
![](https://mc.qcloudimg.com/static/img/0bf032d596c4e6b36a76894b68e177a8/image.png)

高级配置可以根据业务具体情况配置,如不清楚,默认配置即可.
![](https://mc.qcloudimg.com/static/img/4882b69c1b812ed98c9840619b3b0b5f/image.png)
健康检查默认是开启,建议不要自行修改配置,这里可以对出故障的服务器端口进行自动踢除保障业务可用.

**第三步** 绑定云主机,设置权重即可
![](https://mc.qcloudimg.com/static/img/78e9673be6ff3ed2beef607b48ebd211/image.png)


**第四步** 将业务切换至高防IP即可
![](https://mc.qcloudimg.com/static/img/9d05f9c52675ffb46f01e887f6d0872e/image.png)