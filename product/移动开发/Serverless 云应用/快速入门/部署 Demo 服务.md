本文向您介绍如何将 Demo 服务（Hello World项目）通过 Serverless 云应用进行部署。





## 步骤1：登录控制台

登录 [Serverless 云应用控制台](https://console.cloud.tencent.com/tcb/service)，再按需要切换到指定的环境。
![](https://main.qcloudimg.com/raw/7ccca44479b1c0cf092234a8e0f1ee5a.png)

> ?Serverless 云应用公测期间，需要先 [申请开通](https://cloud.tencent.com/apply/p/y5uji0g6a7p)，审核通过后，云开发控制台的左侧菜单才会出现 【Serverless云应用】入口，否则入口将不可见。公测结束后，**Serverless 云应用**的入口将对所有云开发用户开放。



## 步骤2：新建服务

在控制台的服务列表页面，单击【新建服务】。

填写服务名称“helloworld”、镜像仓库的使用模式选择“使用系统默认仓库”，单击【提交】。![](https://main.qcloudimg.com/raw/436e4166b88b00751bba4a2e754924f7.png)

## 步骤3：进入"helloworld"服务详情

选择服务“helloworld”，单击服务名称进入服务详情页面。

![](https://main.qcloudimg.com/raw/252af6bc138cd26f7f109fe3ed8b5fa2.png)

## 步骤4：新建版本

单击【新建版本】
![](https://main.qcloudimg.com/raw/80be0e18962acdd5d131b08a688a544d.png)





## 步骤5：配置版本

在新建版本窗口中，继续填写版本所需配置信息。

上传方式选择“镜像拉取”，来源选择“Demo”，监听端口保持默认值“80”，流量策略保持默认值“部署完成后保持流量为0，稍后手动配置流量”，高级设置保持默认值不做任何修改。![](https://main.qcloudimg.com/raw/e85900bf0f71b48acf5e80bf14235515.png)

也可上传方式选择“本地代码”，文件类型选择“zip包”，单击【Java】或任意一种其他语言的下载链接，然后将下载的zip包直接上传到附件，无需对zip包做任何操作或修改。监听端口保持默认值“80”，流量策略保持默认值“部署完成后保持流量为0，稍后手动配置流量”，高级设置保持默认值不做任何修改。

![](https://main.qcloudimg.com/raw/f56c5dd860a22a870e88c16e94c9548d.png)



## 步骤6：开始部署

在新建版本窗口中，填写完版本配置信息后，单击【开始部署】。

版本初始为“创建中”。部署成功则状态变为“正常”。

此时流量为0%，还不能接受请求。如果单击【访问服务】会看到报错。

![](https://main.qcloudimg.com/raw/73914fd4b0e1216652d421f3e073c565.png)

## 步骤7：配置流量

单击【流量配置】。为版本“helloworld-001”配置流量100%。

单击【完成】。

![](https://main.qcloudimg.com/raw/bcc46bc970c5eeecbadf5ca006d7ab6d.png)



成功后，可以看到流量变为100%。

![](https://main.qcloudimg.com/raw/dd62fe608c1afd19bf9b7e5a696a5ebf.png)

## 步骤8：访问服务

单击【访问服务】，因流量已经配置为100%，服务已经开始处理请求，可以看到 Demo 效果。

![](https://main.qcloudimg.com/raw/60119b59be875421760bc593fdbe5b24.png)
