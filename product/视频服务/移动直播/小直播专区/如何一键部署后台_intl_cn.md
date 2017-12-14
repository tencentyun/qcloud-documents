## 1. 什么是一键部署？
一键部署是为了帮助您分分钟搞定小直播业务后台部署。
![](//mc.qcloudimg.com/static/img/83d9e9a82474f771e6cc223ce71972f5/image.png)

### 1.1 准备云服务器
如果没有购买过腾讯云主机，[点击购买](https://console.cloud.tencent.com/cvm)。按照流程指引，根据自身需求，设定带宽、存储、区域、内存、cpu等机器硬件参数并购买。
注意三点：
- 1 镜像环节需要选取** 服务市场** 中的 **小直播业务后台专用** 镜像。
- 2 记住主机的**root密码**。
- 3 云主机的安全组策略选**默认安全组放通全部端口**。

![](//mc.qcloudimg.com/static/img/53d7df9e5a8bc5141e55231076cbfd74/image.png)

![](//mc.qcloudimg.com/static/img/1b38eb9a8199e86c147b1f5e56028c31/image.png)

![](//mc.qcloudimg.com/static/img/a1760be6fb4b7bcec0f65e8268f85dcc/image.png)

如果已经有现成的腾讯云主机，只需重装系统即可。
注意三点：
- 1 镜像环节需要选取** 服务市场** 中的 **小直播业务后台专用** 镜像。
- 2 记住主机的**root密码**。
- 3 确认云主机的安全组策略选的是**默认安全组放通全部端口**。


	提醒：重要数据请提前做好备份，重装后机器上的数据会丢失。
![](//mc.qcloudimg.com/static/img/fbdcf5e6938f0e72c9705a28e6f55163/image.png)

### 1.2 Web配置云服务器
云服务器参数配置，通过直播控制台的[一键部署页面](https://console.cloud.tencent.com/live/onestep/onestep)来完成操作。
- 确认直播，点播，云通信，对象存储等服务已开通。
- 填写 对象存储参数。
- 填写 云主机的**外网IP**，以及**root密码**。
- 点击开始部署按钮，若提示“部署失败”，请再次确认云主机的安全组设置。
- ![](//mc.qcloudimg.com/static/img/9b4f3117157d920d50a2685ee271c392/image.png)

- 修改直播控制台回调URL地址为 http://云主机外网IP或域名/callback/Live_callback.php 。
- ![](//mc.qcloudimg.com/static/img/00e333a3ab4b4e7737b11e56c725c6c0/image.png)

### 1.3 验证部署
在浏览器输入云主机接口访问地址。 http://云主机外网IP或者域名/interface.php 。收到如下返回请求，说明部署成功。返回的json串提示的信息不用关心。
![](//mc.qcloudimg.com/static/img/d3e3d8bf476b03ce86989740c760b25f/image.png)

## 2. 想知道更多
一键部署后小直播业务后台，对您并不是一个“黑盒”，你可以通过ssh方式登录到云主机，查看后台php源码，以及相关配置。

### 2.1 如何登陆腾讯云主机？
- 腾讯云提供了简单易用的webShell。
- ![](//mc.qcloudimg.com/static/img/1b3386560b937b23a60f87e93bcecca5/image.png)
- putty ssh连接云主机。
- ![](//mc.qcloudimg.com/static/img/d4e08150c4728a1053019d2ec73b6822/image.png)

### 2.2 小直播后台PHP源码在哪？
PHP源码在云主机的 /data/live_demo_service/目录下面。
![](//mc.qcloudimg.com/static/img/e09de7919e9820744669dc5a9e3c8edd/image.png)
### 2.3 nginx配置文件在哪？
nginx配置文件是云主机的 /etc/nginx/nginx.conf 文件。
### 2.4 如何看到更详细的log？
要开启详细log，请在 /data/live_demo_service/ 目录下创建 名为 log的目录。
## 3. 一键部署完成后
### 3.1 如何对接终端小直播？
详情请参见 [如何快速搭建小直播-终端集成](https://cloud.tencent.com/document/product/454/7999#4.-.E7.BB.88.E7.AB.AF.E9.9B.86.E6.88.90)

### 3.2 如何手动配置UGC小视频上传功能
一键部署暂时还未实现配置UGC需要用到的配置项，所以需要手动配置。

在业务服务器上依次执行如下命令
a、**wget -c http://download-1252463788.cossh.myqcloud.com/xiaozhibo_php_svr/xiaozhibo_business_svr_2.0.3.3033.zip**
b、**unzip xiaozhibo_business_svr_2.0.3.3033.zip**
c、**cp live_demo_service/interface/GetVodSignatureV2.php  /data/live_demo_service/interface/**
d、**cd /data/live_demo_service/conf/ && vim OutDefine.php**
e、按下"**I**"键进入vim的Insert模式，加上如下加粗的部分。
   &emsp;** define('CLOUD_API_SECRETID','xxxxxxxxxxxxxxxxxxxxxxxxx');**  //云API个人SecretId，用于UGC上传并落地到点播系统[云API密钥](https://console.cloud.tencent.com/capi)
   &emsp;** define('CLOUD_API_SECRETKEY','xxxxxxxxxxxxxxxxxxxxxxxxx');**  //云API个人SecrectKey，用于UGC上传并落地到点播系统[云API密钥](https://console.cloud.tencent.com/capi) 
f、按下"**Esc**"，按下"**:wq!**"，然后回车，将修改保存到配置文件中。
g、运行 **service nginx reload**，重启nginx服务即可。


