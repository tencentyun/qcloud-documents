## BGP高防IP快速接入（针对业务部署在非腾讯云上的用户）

**第一步 登录控制台高防IP配置页面**

登录“[大禹网络安全]()”控制台，在“BGP高防IP”控制页中找到您已经开通的业务部署在非腾讯云的高防IP实例，点击实例ID，进入配置页面

 ![](//mc.qcloudimg.com/static/img/db5df43e3e35f514ce3e04261c36c583/image.png)
 
 ![](//mc.qcloudimg.com/static/img/d1af7bb865544d4bb0b0bb9b86c83989/image.png)
 
**第二步 新建转发规则**

在“转发规则”配置栏中选择“非网站类业务”或“网站类业务”。点击“新建”按钮，新建转发规则。

 ![](//mc.qcloudimg.com/static/img/7eaa40490cbfbf604afdd01973ececbd/image.png)
 
**1.非网站类业务新建转发规则**

操作按下图所示，转发协议支持TCP协议，填写转发端口（最终想通过高防IP的哪个端口来访问，一般来说跟源站端口是相同的），然后填写源站端口（源站提供服务的真实端口）和源站IP

 ![](//mc.qcloudimg.com/static/img/e7fd75b7e97ab83d9a157d230eb1d6c8/image.png)
 
**注意**

- 非网站类业务不支持配置80/443端口；
- 非网站类业务下存量的80/443转发规则，只可以操作“编辑”和“删除”功能，如需新增80/443端口的转发规则，请在“网站类业务”下进行配置；
- 非网站类业务与网站类业务不支持同时配置80/443端口；
- 请用回车分隔多个IP，最多可输入本IP转发目标区域内20个公网IP；
- 用多个源站之间会以轮询方式做负载均衡；一个高防IP支持配置60条转发规则；
- 点击“确定”后会生成一条转发规则。

**2.网站类业务新建转发规则**

操作按下图所示，输入域名，网站类业务转发协议支持HTTP和HTTPS协议

**2.1 **选择HTTP协议时，源站端口为80，填写源站IP 

注意：请用回车分隔多个IP，最多可输入本IP转发目标区域内20个公网IP

 ![](//mc.qcloudimg.com/static/img/cab68b62607fe8fccfc1514eed4d760d/image.png)
 
**2.2 **选择HTTPS协议时，源站端口为443，您可以选择自有证书，也可以选择腾讯云托管证书，并填写源站IP

注意：请用回车分隔多个IP，最多可输入本IP转发目标区域内20个公网IP

 ![](//mc.qcloudimg.com/static/img/f56642c8a1dabf436485ab44a8eb2317/image.png)
 
 ![](//mc.qcloudimg.com/static/img/e69fe2de74fab21bc9189a10b33c2b54/image.png)
 
**第三步 将业务切换到高防IP即可。**

## BGP高防IP快速接入（业务部署在腾讯云上的用户）

**第一步 登录控制台高防IP配置页面**

登录“大禹网络安全”控制台，在“BGP高防IP”控制页中找到您已经开通的业务部署在腾讯云的高防IP实例，点击实例ID，进入配置页面

 ![](//mc.qcloudimg.com/static/img/86171ae6f5c7d06ddf5a3549049528e9/image.png)
 
**第二步 创建监听器**

基本配置根据业务情况设置相应的协议端口,高防IP是四层转发,7层应用协议如http等也是选择tcp,如下图

![](//mc.qcloudimg.com/static/img/2f0c6d6607a6626859f9e6b768d96f10/image.png)
 
高级配置可以根据业务具体情况配置,如不清楚,默认配置即可.
![](//mc.qcloudimg.com/static/img/461e7fbf6aa40f4eaa2e4f2be5e6ce0f/image.png)
 
健康检查默认是开启,建议不要自行修改配置,这里可以对出故障的服务器端口进行自动踢除保障业务可用.

**第三步 绑定云主机,设置权重即可**

 ![](//mc.qcloudimg.com/static/img/b965ac4bc71ac1a2817c7eb6e73090c7/image.png)
 
**第四步 开启相应防护,可以设置弹性防护峰值,并开启CC防护,并设置阈值.**
 
![](//mc.qcloudimg.com/static/img/097c4a80f3bf53081f874c9fe677d8dc/image.png)
