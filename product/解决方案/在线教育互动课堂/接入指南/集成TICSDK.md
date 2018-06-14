# 集成TICSDK
### 1. 简介
腾讯互动课堂（Tencent Interact Class，TIC）SDK 是一个提供在线教育场景下综合解决方案的SDK，它对腾讯云已经技术积累多年的`iLiveSDK`、`IMSDK`和`BoardSDK`、`COSSDK`  四个SDK进行了集成封装，提供了【多人音视频】，【多人即时通信】，【多人互动画板】【文档云端转码预览】等功能。适用于在线互动课堂，在线会议，你画我猜等场景。

### 2. 开发前必看

#### 1）名词解释
##### 统一名词
请阅读[名词解析](https://cloud.tencent.com/document/product/647/17230)。

##### TIC特有名词：
* roomID：课堂ID，一个课堂的唯一标识，在调用TICSDK的创建房间和加入房间时，由外部传入。

#### 2）接入概览

![](https://main.qcloudimg.com/raw/1924c82283cd5e15da0518d97154e0bb.png)

接入TICSDK之后，整体的架构如上图，腾讯云互动课堂解决方案提供了强大的能力支持，在此基础上，客户只需要完成一些必须的工作和自己的业务层逻辑，即可快速搭建起一个全平台的在线互动课堂产品。

介绍下业务侧需要完成的主要工作：
##### a）业务侧登录和userSig生成：

TICSDK虽然有登录/登出接口，但是登录时使用的是`identifier`和`userSig`，客户不能直接使用，还需实现业务层的登录逻辑，如图：

![](https://main.qcloudimg.com/raw/e5e4e33ea06db665a249844f928f0094.png)

业务终端先用业务侧的用户名密码登录开发者自己的服务器，然后开发者服务器使用腾讯云提供的工具生成登录TICSDK所需要的`userSig`（这一步相当于在腾讯云后台注册了一个账号，用户名为业务侧的用户名，密码为生成的`userSig`），并将其返回终端，终端拿到后就可以使用用户名(即`identifier`)和`userSig`去调用TICSDK的登录接口，最后腾讯云后台负责校验登录信息的正确性，返回登录结果。

开发者需要做的就是图片`开发者服务器`上标注的，调用工具生成userSig，并返回给终端的逻辑（通常做法为在业务侧登录接口回包中返回`userSig`）。

当然，如果在开发调试阶段，也可以使用实时音视频控制台生成`identifier`和`userSig`用于测试开发，详情请参考：[生成签名](https://cloud.tencent.com/document/product/647/17275)

##### b）界面布局：

当然，客户还需要自己完成自己的产品的界面布局，但是为了进一步减小开发者的接入开发成本，我们之后有计划开发一套在线课堂通用的UI模板，敬请期待。

##### c）课堂管理：
TICSDK有创建课堂的接口，但是课堂ID (roomID) 由外面传入，TICSDK内部并不维护`roomID`，所以业务在调用TICSDK接口创建课堂时，需要维护`roomID`的唯一性（创建重复的课堂TICSDK将会返回创建失败及错误信息）

另根据具体业务需要，业务侧可能还需要维护一个当前的课堂列表。

##### d）COS 签名生成：
如果客户业务需要在课堂展示本地文档，则需要用到腾讯云对象存储服务（COS），在对对象存储进行操作时，需要COS签名用于检验身份，这个COS签名需要开发者的后台生成，传给客户端，详情请参考：[业务后台集成腾讯云服务](https://github.com/zhaoyang21cn/edu_project/blob/master/%E6%8E%A5%E5%85%A5%E6%8C%87%E5%BC%95%E6%96%87%E6%A1%A3/%E6%8E%A5%E5%85%A5%E6%8C%87%E5%8D%97/%E4%B8%9A%E5%8A%A1%E5%90%8E%E5%8F%B0%E6%8E%A5%E5%85%A5%E8%85%BE%E8%AE%AF%E4%BA%91%E6%9C%8D%E5%8A%A1.md)。


### 3. 客户端 SDK 文档

* [Windows SDK](https://github.com/zhaoyang21cn/edu_project/blob/master/%E6%8E%A5%E5%85%A5%E6%8C%87%E5%BC%95%E6%96%87%E6%A1%A3/%E5%AE%A2%E6%88%B7%E7%AB%AFSDK%E9%9B%86%E6%88%90/Windows/TICSDK%E6%96%87%E6%A1%A3.md)
* [Web SDK](https://github.com/zhaoyang21cn/edu_project/blob/master/%E6%8E%A5%E5%85%A5%E6%8C%87%E5%BC%95%E6%96%87%E6%A1%A3/%E5%AE%A2%E6%88%B7%E7%AB%AFSDK%E9%9B%86%E6%88%90/Web/TICSDK%E6%96%87%E6%A1%A3.md)
* [Android SDK](https://github.com/zhaoyang21cn/edu_project/blob/master/%E6%8E%A5%E5%85%A5%E6%8C%87%E5%BC%95%E6%96%87%E6%A1%A3/%E5%AE%A2%E6%88%B7%E7%AB%AFSDK%E9%9B%86%E6%88%90/Android/TICSDK%E6%96%87%E6%A1%A3.md)
* [iOS SDK](https://github.com/zhaoyang21cn/edu_project/blob/master/%E6%8E%A5%E5%85%A5%E6%8C%87%E5%BC%95%E6%96%87%E6%A1%A3/%E5%AE%A2%E6%88%B7%E7%AB%AFSDK%E9%9B%86%E6%88%90/iOS/TICSDK%E6%96%87%E6%A1%A3.md)

