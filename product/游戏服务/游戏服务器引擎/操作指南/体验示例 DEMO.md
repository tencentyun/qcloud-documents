## 操作场景
本文档主要指导您如何使用“快捷实验”工具，体验 GSE 主流程，入门游戏服务器托管服务。


## 前提条件
已填写 [游戏服务器引擎申请表](https://cloud.tencent.com/apply/p/k0b6pvbhs6)，并获得使用资格。

## 整体流程
![](https://main.qcloudimg.com/raw/7b9bc4a44cd555b4ecadb4385c0fc36a.png)

调用 GSE 包含4个步骤：
1. 集成 ServerSDK。
2. 发布并集成 ServerSDK 的程序。
3. 调用云 API（创建游戏服务器会话、玩家会话），请求服务地址。
4. 访问服务。

## 操作步骤
### 快捷实验，体验全流程



1. 登录 [游戏服务器引擎控制台](https://console.cloud.tencent.com/gse)，选择左侧菜单【快捷实验】>【示范 DEMO】。
2. 选择左上侧服务区域，单击【一键上传示范包】，提示创建成功后，进入【下一步】。
![](https://main.qcloudimg.com/raw/7cb6102e553e388cbd3abc0f5febd188.png)
>?此步骤为开发者的代码集成 ServerSDK，请将代码和依赖上传，GSE 为您提供示范包，并可一键上传。
3. 单击【一键创建服务器舰队】，提示创建成功后，进入【下一步】。
![](https://main.qcloudimg.com/raw/a0b0b580ccb3a47843bb8d9f22a08a89.png)
4. 单击【创建游戏服务器会话】，提示创建游戏服务器会话成功。
![](https://main.qcloudimg.com/raw/bb917d621c170e2fb9433c2abefa6fff.png)
>?此步骤为开发者通过调用云 API 完成，该页面快速创建。
5. 单击【创建玩家会话】，提示创建玩家会话成功。单击一次【创建玩家会话】可以打开一个客户端网页。
![](https://main.qcloudimg.com/raw/41335db73cd7e32e5850dbcfeb9c3d30.png)
6. 单击【跳转至客户端网页】，进入客户端连接游戏服务器页面，单击【连接】，提示服务器：连接成功。
![](https://main.qcloudimg.com/raw/9d9e0fc4ffd3d8dd89e42f988f244483.png)
>?此步骤为开发者通过上一步调用云 API 返回的 IP、port 连接游戏服务器进程，此步骤模拟了整个连接过程。 



  


### 演示弹性伸缩能力

#### 修改扩缩容配置
1. 登录 [游戏服务器引擎控制台](https://console.cloud.tencent.com/gse)，单击左侧菜单【服务器舰队】。
2. 选择刚一键创建的服务器舰队 ID，进入舰队详情，选择【扩缩容】。
![](https://main.qcloudimg.com/raw/02d4e99967944a70cac891c7c39821a2.png)
3. 在其页面单击右上角【修改】，修改扩缩容配置，详情如下：
 - 游戏服务会话缓冲配置成50%，当服务器承载的游戏对局超过50%时，即会扩容。
 - 实例范围调整到0 - 3，让其有扩的空间。
 ![](https://main.qcloudimg.com/raw/30f5e5f9b8ed46ba9c008438c0b6e965.png)
4. 修改配置完成后，单击【确定】。


#### 创建多个游戏服务器会话，触发扩容

>?
- DEMO 默认配置1台服务器承载10个游戏服务器会话，直到第5个游戏服务器会话时，缓冲是50%。
- 超过5个游戏服务器会话需进行扩缩。需要创建6个游戏服务器会话。

1. 选择【快捷实验】>【部署示范包】，连续再单击5次【创建游戏服务器会话】，从而共创建6个游戏服务器会话。
![](https://main.qcloudimg.com/raw/569510c2d9de270bd785bb57e177a9b7.png)
2. 单击左侧菜单[【服务器舰队】](https://console.cloud.tencent.com/gse/fleet)，选择刚一键创建的服务器舰队 ID，进入舰队详情，选择【实例列表】。在其页面观察服务实例数量，2分钟后，您将发现服务器被扩容至2台。
![](https://main.qcloudimg.com/raw/2788ac8033205adf171005938179365a.png)


#### 结束游戏服务器会话，触发缩容
1. 选择【快捷实验】>【部署示范包】，每一个游戏服务器会话，创建一个玩家会话，并进入客户端页面，单击【结束游戏会话】，即可结束游戏服务器会话。分别操作5次，即可结束5个游戏服务器会话。
![](https://main.qcloudimg.com/raw/7f11e71ad1876b51682820b9465ed616.png)
2. 单击左侧菜单[【服务器舰队】](https://console.cloud.tencent.com/gse/fleet)，选择刚一键创建的服务器舰队 ID，进入舰队详情，选择【实例列表】。在其页面观察服务实例数量，2分钟后，您将发现服务器被缩容至1台。
![](https://main.qcloudimg.com/raw/65104c873e5e606e3b79a45b9ab17c2b.png)
