## 1. 小直播前后台结构图

![](//mc.qcloudimg.com/static/img/491b2ff7a8dcd38948d2ad1fd02a90f2/image.png)

- **腾讯云:** 提供了**云直播（LVB）**，**点播（VOD）**，**云通信（IM）**， **对象存储（COS）**和**云主机（CVM）**等云服务产品。
- **业务服务器:** 又称为客户业务后台，实现客户自身的业务需求。在终端和腾讯云之间起到“胶水”的作用。
- **终端:** 集成包括了文字互动、弹幕消息、飘星点赞、美颜增白、动效蒙皮、连麦互动、身份认证等能力，提供了**IOS**和**Android**平台的相应的开发包供开发集成。


| 交互关系 | 主要交互内容 | 
|:--------:|:---------:|
|业务服务器 - 腾讯云|腾讯云回调业务服务器通知状态，如录制完成通知。|
|业务服务器 - 终端| 直播/回看 列表管理；IM房间管理 ；COS上传签名的生成；推流地址生成。|
|终端 - 腾讯云|音视频流的推送，拉取；IM消息的发送接收| 


## 2. 相关云服务及开通

### 2.1 小直播用到的各项云服务一览:

| 开通入口 | 服务简称 | 功能描述 | 试用支持 | 是否可替换|
|:--------:|:---------:|---------|:-----: |:----:|
| [直播](https://cloud.tencent.com/document/product/454/7953#1.1-.E5.A6.82.E4.BD.95.E5.BC.80.E9.80.9A.E8.A7.86.E9.A2.91.E7.9B.B4.E6.92.AD.E6.9C.8D.E5.8A.A1) | LVB | 必选服务，推流和观看都需要使用它，也是唯一需要腾讯云**人工审核**才能开通的服务。 | 10G 免费试用 | 支持|
| [点播](https://cloud.tencent.com/document/product/454/7953#2.1-.E5.A6.82.E4.BD.95.E5.BC.80.E9.80.9A.E8.A7.86.E9.A2.91.E7.82.B9.E6.92.AD.E6.9C.8D.E5.8A.A1) | VOD| 小直播支持将直播过程录制下来并以回放列表的形式进行展现，而视频文件的存储依赖腾讯云点播服务。| 7 天免费试用|支持|
| [云通信](https://cloud.tencent.com/document/product/454/7953#3.-.E4.BA.91.E9.80.9A.E8.AE.AF.E6.9C.8D.E5.8A.A1.EF.BC.88im.EF.BC.89) | IM | 提供消息的发送、接收、上下线状态、离线消息缓存以及聊天室等基础消息服务，小直播的互动消息、弹幕、点赞等功能都是基于这种互动消息而实现的。| 日活跃用户10W以下免费 | 支持 |
| [对象存储](https://cloud.tencent.com/document/product/454/7953#4.-.E5.AF.B9.E8.B1.A1.E5.AD.98.E5.82.A8.E6.9C.8D.E5.8A.A1.EF.BC.88cos.EF.BC.89) | COS | 用于小直播中的直播封面、用户头像等图片文件的上传和下载，如果您已经有自己的文件服务器，可以替换之。| 50G 免费空间 | 支持 |

### 2.2 云服务开通
请参见 [如何开通各项云服务？](https://cloud.tencent.com/document/product/454/7953)


	特别说明：
	
	腾讯云回调业务服务器是通过 业务服务器上的Live_callback.php 接口来实现回调处理逻辑。 
	
	直播控制台 回调URL需要配置为：http://业务服务器IP或域名/callback/Live_callback.php

## 3. 业务后台集成和部署
### 3.1. 后台部署主要步骤和方式
**部署步骤**
- **step 1 准备服务器和网络**
- **step 2 部署环境**
- **step 3 配置腾讯云服务参数**
- **step 4 部署完成验证**

**部署方式**
- **方式1 自有服务器 - 集成部署**
如果您具有后台研发能力，有后台服务器资源，希望和自己的后台已有业务进行整合，建议您走方式一。

- **方式2 腾讯云CVM云主机 - 快捷部署**
如果您没有后台开发资源，或者小直播的这套功能已经满足您的要求了，你又想快速上线和体验，建议您走方式二。

### 3.2. 部署环境介绍
我们提供了一套** nginx + php + mysql** 的业务后台源码，建议部署在**CentOS 64位**系统上。appstore上体验用的小直播，就是使用这套源码搭建的业务后台。


|环境|简介|版本推荐|指引|
|--|--|:--|:--:|--:|
|**nginx**|是一款轻量级的Web 服务器/反向代理服务器，其特点是**内存占用少**，**并发能力强**。|最新稳定版|[官网](http://nginx.org/)|
|**php**|是一种通用开源脚本语言。**易于学习**且**使用广泛**，主要适用于Web开发领域，其特点是**执行效率高**。|最新稳定版|[官网](http://www.php.net/)|
|**mysql**|是**最流行**的关系型数据库管理系统，在 WEB 应用方面MySQL是最好的 RDBMS 应用软件之一。|5.6及以上|[官网](http://www.mysql.com/)|

### 3.3. 腾讯云服务参数说明
 腾讯云服务，LVB，IM，VOD，COS等系统相对独立，彼此都有一套对内调用完成功能集成和对外的API供客户的业务服务调用，VOD本质上是依赖COS的。云服务的参数主要作用无外乎以下三类：
 - **身份识别**，各种ID，区分应用，业务，客户等。
 - **安全调用相关**，各种key，主要基于数字签名技术或者对称加密+MD5技术实现接口调用的访问安全。
 - **内部系统所需参数**，典型的就是COS 的 bucket 参数，一个bucket可以想象成是一个硬盘，VOD的文件是存放在COS上的，VOD需要您指定存放的硬盘的位置。

**小直播用到的云服务参数一览**

|所属服务| 参数名称| 含义| 获取方法 |
|--| :-------------------------- |: ----------------- | ---- |
|LVB|bizid     | 区分云直播业务，ID 一般是4位数   | [DOC](https://cloud.tencent.com/document/product/454/7953#1.4-.E6.9F.A5.E8.AF.A2.E6.88.91.E7.9A.84.E7.9B.B4.E6.92.ADbizid) |
|LVB| appid | 区分云直播应用，ID 一般是10位数  | [DOC](https://cloud.tencent.com/document/product/454/7953#1.3-.E6.9F.A5.E8.AF.A2.E6.88.91.E7.9A.84.E7.9B.B4.E6.92.ADappid) |
|LVB| 推流防盗链KEY | 用于确保推流链接的来源是有效性和合法性    | [DOC](https://cloud.tencent.com/document/product/454/7953#1.5-.E6.9F.A5.E8.AF.A2.E6.8E.A8.E6.B5.81.E9.98.B2.E7.9B.97.E9.93.BEkey) |
|LVB| API鉴权KEY| 用于业务后台鉴定URL回调的合法性 | [DOC](https://cloud.tencent.com/document/product/454/7953#1.6-.E6.9F.A5.E8.AF.A2api.E8.AE.BF.E9.97.AE.E9.89.B4.E6.9D.83key) |
|COS| APPID      |区分对象存储应用 | [DOC](https://cloud.tencent.com/document/product/454/7953#4.4-.E6.9F.A5.E8.AF.A2.E6.88.91.E7.9A.84cos-appid) |
|COS| Bucket名称  | 指定对象存储，文件要存放的位置 | [DOC](https://cloud.tencent.com/document/product/454/7953#4.3-.E6.9F.A5.E8.AF.A2.E6.88.91.E7.9A.84bucketname) |
|COS| SecretId |COS 存储API，钥匙串ID，COS一般会提供两套备用 | [DOC](https://cloud.tencent.com/document/product/454/7953#4.5-.E6.9F.A5.E8.AF.A2.E6.88.91.E7.9A.84cos-secretid-.E5.92.8C-secretkey) |
|COS| SecretKey |COS存储API，钥匙串Key，和钥匙串ID配对使用，确保API调用请求的合法性 | [DOC](https://cloud.tencent.com/document/product/454/7953#4.5-.E6.9F.A5.E8.AF.A2.E6.88.91.E7.9A.84cos-secretid-.E5.92.8C-secretkey) |

### 3.4. 自有服务器 - 集成部署
- **step1. 准备服务器和网络**
> 腾讯云在录制结束，直播结束等情况下会通过您在直播控制台指定的回调URL参数，来通知您的业务服务器，因此需要确保服务器具有外网IP**能被外网访问**。
- **step2. 部署环境**
> - 下载并安装，nginx，php，mysql等软件及其依赖软件并启动mysql。
> - 下载[小直播php源码](https://cloud.tencent.com/document/product/454/6991)，上传到业务服务器。
> - 解压源码，运行createDB.sh创建数据库，运行之前确保msyql服务处在运行状态。
> ![](//mc.qcloudimg.com/static/img/c35c3ddb8c1204cba4d4cfa1e4870a88/image.png)
- **step3. 配置腾讯云服务参数**
> - 在压缩包的live_demo_service/conf目录下找到 OutDefine.php文件，修改相应的参数。并保存。
> ![](//mc.qcloudimg.com/static/img/fb1623bc86f24257f470414a3c1715ae/image.png)
> ![](//mc.qcloudimg.com/static/img/52f024b246a9d329cec083184c64acab/image.png)
> ![](//mc.qcloudimg.com/static/img/134809e0b53e2ee3e07a1c37066ccd09/image.png)
> - 在压缩包中有live_demo.nginx和nginx.conf这两个文件，拷贝live_demo.nginx文件到/etc/nginx/ 目录下，将live_demo_service目录拷到 /data 目录下。在/etc/nginx 目录下有一个nginx.conf文件，参照压缩包中的 nginx.conf文件修改，主要确认http配置选项下有 **"include live_demo.nginx;"**。确保live_demo.nginx中root参数和小直播源码路径一致。
> ![](//mc.qcloudimg.com/static/img/83a38d5cd81059642eb381270dec6d35/image.png)
> - 启动PHP，随后启动nginx。
> 
- **step4. 部署完成验证**
> 在浏览器输入 http://您的服务器ip/interface.php， 如果返回如下结果“{"returnValue":4001,"returnMsg":"json format error","returnData":[]}” ，说明PHP处于运行状态，并且接口可以被外部访问。说明业务后台部署完成。
> 这里提示**“json format error”**是因为请求没有带参数，小直播终端源码对接口请求做了封装，对接终端源码后请求就是正常的。详细的接口使用可以参考 [小直播前后台协议解析](https://cloud.tencent.com/document/product/454/7895)。


###  3.5.  腾讯云CVM云主机 - 快捷部署
和**自有服务器 - 集成部署**差不多 后两步是一样的，简化了前两步。[腾讯云云主机](https://cloud.tencent.com/document/product/213/495)再结合**镜像市场**服务，轻松搞定。

**准备一台腾讯CVM云主机：**
- **第一步** [新建CVM主机](https://console.cloud.tencent.com/cvm) 
> ![](//mc.qcloudimg.com/static/img/53d7df9e5a8bc5141e55231076cbfd74/image.png)

- **第二步** 进服务市场选取镜像 推荐使用图中所给的**PHP运行环境（CentOS 64位 PHP5.4 Niginx）**。
> ![](//mc.qcloudimg.com/static/img/568a25630c61d22f43171b2df59c213a/image.png)
> 
- **第三步** 配置硬盘和网络，以及云主机访问密码，妥善保管好密码。

- **第四步** 付款后生成云主机。点击登录可以通过腾讯云的网页shell进行访问，也可以用 **putty** 或 **SecretCRT** 采用ssh登录到主机。
> ![](//mc.qcloudimg.com/static/img/0f29fd40aae5fdac10d3f6262eb6a03e/image.png)

剩下步骤和**自有服务器 - 集成部署**一样，参考上文。

**至此业务后台部署完成后，集成就完成了一大半了，剩下的终端集成相对就更加简单了。**

## 4. 终端集成及回调设置

终端集成主要是小直播源码集成，主要是以下简单几步：
### 4.1. 小直播源码源码下载
[小直播源码下载](https://cloud.tencent.com/document/product/454/6991)，点击后如图，下载**小直播IOS**和**小直播Android**

### 4.2. 终端参数一览
**各个参数及其意义** 

| 参数名称| Android变量名|IOS变量名|含义|
|------------|----------|----------|----------|
| **SdkAppId**|IMSDK_APPID|kTCIMSDKAppId|IM相关 标识一个IM应用|
|**AccountType**|IMSDK_ACCOUNT_TYPE|kTCIMSDKAccountType|IM相关 账号类型，小直播采用的是[托管模式](https://cloud.tencent.com/document/product/269/1509)，创建IM应用的时候务必选择托管模式；另一种是[独立模式](https://cloud.tencent.com/document/product/269/1508) 主要用在需要和自己已有的账号体系进行集成。|
|**APPID**|COS_APPID|kTCCOSAppId|区分对象存储应用|
|**Bucket名称**|COS_BUCKET|kTCCOSBucket|指定对象存储，文件要存放的位置|
|**区域代码**|COS_REGION|kTCCOSRegion|COS相关 指定Bucket所在区域，COS实际所在机房，目前有华东（sh），华北（tj），华南（gz）三个区域。|
|**ServerAddr**|SVR_POST_URL|kHttpServerAddr|业务服务器后台请求地址: `http://您的服务器地址或域名/interface.php`  |

### 4.3. 终端参数替换
Android 源码包解压后在app/src/main/java/com/tencent/qcloud/xiaozhibo/base目录下有一个**TCConstants.java**文件；同样在在IOS源码包解压后在TCLVBIMDemo/Classes/LVB/Base 目录下有一个**TCConstants.h**文件。并替换对应的字段值，源码中默认是**空值或0**。
**参数获取：**
[SdkAppId获取](https://cloud.tencent.com/document/product/454/7953#3.2-im-sdk-appid)，[AccountType获取](https://cloud.tencent.com/document/product/454/7953#3.3-im-sdk-.E8.B4.A6.E5.8F.B7.E7.B1.BB.E5.9E.8B)，[COS Region 获取](https://cloud.tencent.com/document/product/454/7953#4.-.E5.AF.B9.E8.B1.A1.E5.AD.98.E5.82.A8.E6.9C.8D.E5.8A.A1.EF.BC.88cos.EF.BC.89)。

### 4.4. 设置回调地址
在直播管理控制台设置回调地址，腾讯云后台在相应事件发生时（如流状态改变、视频录制完成、截图完成等），通过该地址回调给业务服务器，业务服务器做相应处理，事件回调的详细信息可以参考[事件消息通知](https://cloud.tencent.com/document/product/267/5957)
配置方式：
在[直播控制台>>直播码接入>>接入配置](https://console.cloud.tencent.com/live/livecodemanage)配置回调URL，如果您未修改过小直播业务服务器的代码，回调URL的格式为：`http://您的服务器地址或域名/callback/Live_callback.php`
![](//mc.qcloudimg.com/static/img/b0a78a4b974824940abe811d42fb0561/image.jpg)

### 4.5. 真机编译运行
Android 推荐使用**Android Studio 2.2**。IOS推荐使用**XCode8.1**。
源码结构具体可以参见 [Android代码说明](https://cloud.tencent.com/document/product/454/7892) 和 [iOS代码说明](https://cloud.tencent.com/document/product/454/7894)。

### 4.6. 验证各项功能
- 登录
- 开播推流
- 拉取播放列表
- 播放直播和**回看**
	> 
	> **特别提醒: 小直播回看功能 用到了转码录制功能，每路每月 30元，路数是指并发推流的个数。比如您月内最高并发推流2路，那么月底的账单就有30*2=60元的录制费用产生。**
	> 
	测试期间建议用一路，节约您的成本，如果您想多路调试又尽量减少录制费用，你可以通过修改小直播后台** RequestLVBAddr.php **文件，将拼接的URL参数 **record=flv|hls** 去掉。或者在终端代码里面将请求到的推流地址中的 **record=flv|hls** 参数删除，来暂时屏蔽录制功能，待上线后打开。推流地址带参数启动录制的原理可以参见[录制和回看](https://cloud.tencent.com/document/product/454/6852)
 

- 修改头像
- 上传封面
- 评论
- 弹幕
- 点赞
- 美颜
- **连麦** 小直播1.8.2版本支持，[连麦原理](https://cloud.tencent.com/document/product/454/8092)。
- ** 动效** 需要签订协议付费使用，源码不包含此功能。

**至此小直播的前后端集成完成。验证功能过程中若遇到问题，请查看集成可能遇到的问题表现及排查方法。**

## 5. 集成可能遇到的问题表现及排查方法
### 5.1. Apple ATS支持
苹果审核新政要求 ios 应用使用ATS，强制推行时间由原来的2017年1月1日，改为推迟执行。ATS会影响ios 小直播和业务后台的通信。
要支持ATS需要做两件事：
- 业务后台支持**HTTPS**。
> HTTPS要求业务服务器具有CA颁发的DV证书做域名验证，如果您没有证书，可以[申请腾讯云免费证书](https://console.cloud.tencent.com/ssl) 有效期1年。 证书申请前得准备好域名，我们提前在腾讯云[购买域名](https://buy.cloud.tencent.com/domain?tlds=.cn)，本文中购买的域名是tcmlvb.cn（25元/年）并将cgi.tcmlvb.cn和证书绑定。确保cgi.tcmlvb.cn 域名指向CVM上购买好的云主机的外网IP。
> **第一步 申请免费证书：**
> ![](//mc.qcloudimg.com/static/img/603afe4ae7fa1aba61f2aad11e8d2fbc/image.png)
> 
> ![](//mc.qcloudimg.com/static/img/028bae9f244a013b13b1a7c003f67930/image.png)
> 
> ![](//mc.qcloudimg.com/static/img/7274fefc07fe6b16bbb9eb61a944ca4f/image.png)
> **第二步 审核通过后业务后台部署：**
> 首先[下载证书](https://console.cloud.tencent.com/ssl)，找到对应证书点击下载按钮，并通过WinScp等工具上传至业务服务器。然后参考[证书部署](https://cloud.tencent.com/document/product/400/4143#2.-nginx-.E8.AF.81.E4.B9.A6.E9.83.A8.E7.BD.B2)，修改live_demo.nginx相应的配置。保存修改并重启， shell 命令：**nginx -s reload**
> **第三步 证书部署完成验证：**
> 在浏览器地址栏输入 https://cgi.tcmlvb.cn/interface.php，返回结果表名https部署成功。
> 
> ![](//mc.qcloudimg.com/static/img/d3e3d8bf476b03ce86989740c760b25f/image.png)
- **kHttpServerAddr **改用 https协议：https://业务服务器域名/interface.php。

### 5.2. 如何使用自己的账号体系？
请您参考 [使用自己的账号体系？](https://cloud.tencent.com/document/product/454/7981)

### 5.3. 如何加强登录鉴权检查?
请您参考 [加强登录鉴权检查?？](https://cloud.tencent.com/document/product/454/6562)

### 5.4. 其它问题
其他问题请参见 [如何排查常见问题？](https://cloud.tencent.com/document/product/454/8110)


