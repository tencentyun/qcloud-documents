## BGP高防IP快速接入（业务部署在非腾讯云）

**第一步** 登录控制台高防IP配置页面

登录“[大禹网络安全](https://console.qcloud.com/dayu/bgpip)”控制台，在“BGP高防IP”控制页中找到您已经开通的业务部署在非腾讯云的高防IP实例，点击实例ID，进入配置页面
![](https://mc.qcloudimg.com/static/img/6085ef927caa91a65c6b1ba4db92fd0d/image.png)
![](https://mc.qcloudimg.com/static/img/d696aa7a51b0ba6da9cfd89c256430dd/image.png)

**第二步** 新建转发规则

在“转发规则”配置栏中选择“非网站类业务”或“网站类业务”。点击“新建”按钮，新建转发规则。
![](https://mc.qcloudimg.com/static/img/f3fab5cfb86255b09630bf34f9d8b95f/image.png)
**1.非网站类业务新建转发规则**
操作按下图所示，转发协议支持TCP协议，填写转发端口（最终想通过高防IP的哪个端口来访问，一般来说跟源站端口是相同的），然后填写源站端口（源站提供服务的真实端口）和源站IP
![](https://mc.qcloudimg.com/static/img/1e44b24c1b8d75bb055b1d99b6788a61/image.png)
**注意**
**· **非网站类业务不支持配置80/443端口；
**· **非网站类业务下存量的80/443转发规则，只可以操作“编辑”和“删除”功能，如需新增80/443端口的转发规则，请在“网站类业务”下进行配置；
**· **非网站类业务与网站类业务不支持同时配置80/443端口；      
**· **请用回车分隔多个IP，最多可输入本IP转发目标区域内20个公网IP；
**· **用多个源站之间会以轮询方式做负载均衡；一个高防IP支持配置60条转发规则；
**· **点击“确定”后会生成一条转发规则。

**2.网站类业务新建转发规则**
操作按下图所示，输入域名，网站类业务转发协议支持HTTP和HTTPS协议
**2.1**选择HTTP协议时，源站端口为80，填写源站IP
注意：请用回车分隔多个IP，最多可输入本IP转发目标区域内20个公网IP
![](https://mc.qcloudimg.com/static/img/d14b767f823892dca93b3d5157efbc0d/image.png)
**2.2**选择HTTPS协议时，源站端口为443，您可以选择自有证书，也可以选择腾讯云托管证书，并填写源站IP
注意：请用回车分隔多个IP，最多可输入本IP转发目标区域内20个公网IP
![](https://mc.qcloudimg.com/static/img/327a57c3e180514bc5e9e8d5f965915c/image.png)
![](https://mc.qcloudimg.com/static/img/2a3f64de5c5270b82d8f17bc04a885ec/image.png)
**第四步** 将业务切换到高防IP即可。

## BGP高防IP快速接入（业务部署在腾讯云）
**第一步** 登录控制台高防IP配置页面

登录“[大禹网络安全](https://console.qcloud.com/dayu/bgpip)”控制台，在“BGP高防IP”控制页中找到您已经开通的业务部署在腾讯云的高防IP实例，点击实例ID，进入配置页面
![](https://mc.qcloudimg.com/static/img/deea9548b99e7fe4a8858bd0b448588f/image.png)

**第二步** 创建监听器
基本配置根据业务情况设置相应的协议端口,高防IP是四层转发,7层应用协议如http等也是选择tcp,如下图
![](https://mc.qcloudimg.com/static/img/88ad4ec2eb7dc508ac6a210e9d6a134e/image.png)
高级配置可以根据业务具体情况配置,如不清楚,默认配置即可.
![](https://mc.qcloudimg.com/static/img/484425c924a20a822596934cd951a802/image.png)
健康检查默认是开启,建议不要自行修改配置,这里可以对出故障的服务器端口进行自动踢除保障业务可用.

**第三步** 绑定云主机,设置权重即可
![](https://mc.qcloudimg.com/static/img/067bf61603249e227021053ef035d06f/image.png)

**第四步** 开启相应防护,可以设置弹性防护峰值,并开启CC防护,并设置阈值.
![](https://mc.qcloudimg.com/static/img/d00135b793b9250dd63e2efc7f2a3be5/image.png)