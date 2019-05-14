小直播 App 是一套开源的完整的在线直播解决方案，它基于腾讯云直播服务（LVB）、云通讯服务（TIM）和对象存储服务（COS）构建，并使用云主机（CVM）提供简单的后台服务，可以实现登录、注册、开播、房间列表、连麦互动、文字互动和弹幕消息等功能。

本文主要介绍如何一步步地将小直播 App 的前后台代码运行起来，以便能够快速看到运行效果，整个过程大约耗时10 - 20 分钟。

## 一、 开通云服务
### 1.1 开通直播服务

#### step1. 申请开通视频直播服务
进入 [直播管理控制台](https://console.cloud.tencent.com/live)，如果服务还没有开通，单击申请开通。

#### step2. 申请测试 License
点击 [移动直播 License](https://console.cloud.tencent.com/live/license) 申请测试 license（基础版，有效期28天），并填写相应的信息：在 Package Name 中填写 Android 的包名，Bundle Id 中填写 iOS 的 bundleId。
![](https://main.qcloudimg.com/raw/edd99f145276ad5250f0ca5d0f5d4980.png)
创建成功后页面会显示生成的 License 信息，这里需要记下 Key 和 LicenseUrl，在 SDK 的初始化时需要传入这两个参数。
![](https://main.qcloudimg.com/raw/ce722e4038a86b85d96b2cb9f5a058e8.png)

#### step3. 在应用管理中添加一个新的应用
开通直播服务并获取到 License 后，进入【直播控制台】=>【直播SDK】=>【[应用管理](https://console.cloud.tencent.com/live/license/appmanage)】，点击【创建应用】开始创建一个新的应用。
![](https://main.qcloudimg.com/raw/ccc83c93aa7d85aa1f84ca620ee8f5cb/AppMgr.png)

>? 这一步的目的是创建一个 TIM 云通信应用，并将当前直播账号和云通信应用绑定起来，云通信应用能够为小直播 App 提供聊天室和连麦互动的能力。

#### step4.  获取直播服务配置信息
点击创建好的应用，可以看下如下所示界面，记录其中的 SDKAPPID，后续步骤中会用到。
![](https://main.qcloudimg.com/raw/818886698bca6e6f331458146cca04c0.jpg)

点击【应用管理】=>【编辑】，创建一个管理员帐号，然后点击【下载公私钥匙】，解压后可以获得公私钥文件：
![](https://main.qcloudimg.com/raw/d8da2aacfea26602100d525ec579eb74.png)

公私钥文件内容如图所示，其中 `-----BEGIN PRIVATE KEY-----` 开始的内容即为私钥，后续步骤中会用到。
![](https://main.qcloudimg.com/raw/956876a4ce087051d6b1e85cbb5d60c0.png)

### 1.2 开通对象存储服务
对象存储服务主要用于小直播 App 中的直播封面图片存储，过程如下所示。

#### step1. 申请开通对象存储服务
进入[对象存储服务控制台](https://console.cloud.tencent.com/cos5)，如果还没有服务，直接单击**创建存储桶**按钮即可，如下图：
![](https://main.qcloudimg.com/raw/813c62b547c0921134aefea5d25b2ec9.jpg)

#### step2. 创建存储桶并获取基本信息
填写名称，选择所属地域，使用**公有读私有写**权限创建存储桶，存储桶标签在这里不被使用，可以留空。
![](https://main.qcloudimg.com/raw/cd92d21f4473fa86125719ca1033e65b/new_cos_dialog.jpg)

单击确定按钮，之后就进入了刚刚创建的存储桶管理界面，点击【基础配置】菜单，记录`存储空间名称`、`所属地域`，分对应于下文"修改云主机配置信息"中的 `COSKEY_BUCKET` 和 `COSKEY_BUCKET_REGION`，这两个数值会在后续步骤中用到。
![](https://main.qcloudimg.com/raw/fb059908dd4b13ffbf82814fbca4f020.png)

#### 3. 获取密钥信息
进入[【对象存储控制台】=>【密钥管理】=>【云API密钥】](https://console.cloud.tencent.com/cam/capi)获取`APPID`、`SecretId`和`SecretKey`， 分别对应于下文"修改云主机配置信息"中的 `COSKEY_APPID`、`COSKEY_SECRETID`和`COSKEY_SECRETKEY`。
![](https://main.qcloudimg.com/raw/b5c6e9471d22d20591d23464dbf717a6.jpg)

## 二、 腾讯云CVM镜像部署

小直播 App 单靠一套客户端源码还不能正常运行，需要一个简单的账号管理服务器，用于提供登录和注册的服务。同时，我们还在该后台上开发了“精彩回放”的功能，也就是过往的直播会被录制下来存入“回放列表”。由于直播的录制和存储都是腾讯云实现的，所以该服务器的作用仅仅是记录历史视频文件的列表，并提供给小直播 App 进行拉取和查询。

### 2.1 创建虚拟主机
进入 [CVM控制台](https://console.cloud.tencent.com/cvm) 点击【新建】开始创建虚拟主机。
![](https://mc.qcloudimg.com/static/img/53d7df9e5a8bc5141e55231076cbfd74/image.png)

### 2.2 选取镜像
进服务市场选取镜像 推荐使用图中的**小直播镜像**。
![](https://main.qcloudimg.com/raw/da14288ee7196c45f0d3fcc4def88567.png)
 
### 2.3 配置主机
配置硬盘和网络，以及云主机访问密码，**妥善保管好root密码**将用于下文"修改云主机配置信息"，然后设置安全组。
![](https://main.qcloudimg.com/raw/c265b5c870f6a7ecb2f15f83f7c508c4.jpg)

### 2.4 查看主机信息
付款后生成云主机。**请记录外网 IP**用于下文“配置录制回调”及“终端集成”中的操作。
![](https://main.qcloudimg.com/raw/7565c1a85318d56ab93571149a5c3855/cvm_list.jpg)

## 三、直播录制与回调配置
小直播 App 中的“精彩回放”功能依托于云直播的录制功能，配置方法如下。

### 3.1 配制录制参数

在视频直播菜单栏内选择【功能模板】=>【录制配置】，单击 "+" 进行设置。
![](https://main.qcloudimg.com/raw/40d0e5c555262246d6a8f3cfd2cfe144.png)
设置基本信息, 填写【模板名称】，并选择录制文件类型（HLS、MP4 或者 FLV）后点击【保存】。
![](https://main.qcloudimg.com/raw/61be5f5e822f048229191c16fba41d03.png)

### 3.2 配置录制回调
在视频直播菜单栏内选择【功能模板】=>【回调配置】，单击 "+" 创建回调模板。
![](https://main.qcloudimg.com/raw/9b364488f509080abfa3d00b41048465.png)

表单中只需填写【回调密钥】和【录制回调】。请记录【回调密钥】并在【录制回调】请填写 `http://您的云主机服务器的公网地址/callback/tape_callback.php`，点击【保存】。

![](https://main.qcloudimg.com/raw/d31e9dcabf17fd394b56207c0d9d557a.png)

### 3.3 应用配置到域名
进入直播控制台 [域名管理](https://console.cloud.tencent.com/live/domainmanage)，点击默认域名后的【管理】按钮。
![](https://main.qcloudimg.com/raw/55ce80bbc36364587fe6db830fd02b2f/doman_mgr.png)

点击【模板配置】，分别点击【回调配置】和【录制配置】，选择上述步骤中建立好的模板。
![](https://main.qcloudimg.com/raw/aab97213e80dfc428f7c201ec89f450b/domain_cfg.png)

## 四、修改云主机配置信息

### 4.1 准备配置文件
将以下内容粘贴到文本编辑器（比如记事本），按照下方脚本中的注释填写各项内容，其中 xxxx 的部分在本文前半部分均能找到对应的值。

```bash
#!/bin/bash
echo "-----BEGIN PRIVATE KEY-----
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
-----END PRIVATE KEY-----" > /data/live_demo_service/deps/sig/private_key;
echo "<?php

define('IM_SDKAPPID',123456);   // 请替换为“获取直播服务配置信息”中获取到的 SDKAppID
define('API_KEY','xxxxxxxx');   // 请替换为“配置录制回调”中获取到的回调密钥

define('COSKEY_BUCKET','xxxxxxxx'); // 请替换为“创建存储桶并获取基本信息“中获取的“存储空间名称”
define('COSKEY_BUCKET_REGION','xxxxxxxx'); // 请替换为“创建存储桶并获取基本信息“中获取的“所属地域”
define('COSKEY_SECRECTKEY','xxxxxxxx'); // 请替换为“获取密钥信息”中您所新建的 secrectKey
define('COSKEY_APPID',123456); // 请替换为“获取密钥信息”中您所新建的 APPID
define('COSKEY_SECRECTID','xxxxxxxx'); //  请替换为“获取密钥信息”中您所新建的 secrectId

define('COSKEY_EXPIRED_TIME',30); // 无需修改
define('IM_ACCOUNTTYPE', '1234');  // 无需修改
define('APP_ID',123456);  // 无需修改
define('APP_BIZID',1234);  // 无需修改

?>" > /data/live_demo_service/conf/OutDefine.php;
```

> 上面代码中第一个 echo 后跟着的双引号内是 IM 私钥的内容，将上述步骤中下载的“公私钥文件”(authkeys.txt) 中的私钥（`-----BEGIN PRIVATE KEY-----` 开始的内容）填到双引号内即可

### 4.2 登录云主机
在[CVM控制台](https://console.cloud.tencent.com/cvm)点击【登录】目标主机
![](https://main.qcloudimg.com/raw/f1b5c3f646e7db26f9b595642e8efd17.png)

选择**标准登录**方式，填写上文“配置主机”中设置的密码，点击【确认】：
![](https://main.qcloudimg.com/raw/97c7747e9948574cd5a64297313d2de1.png)

### 4.3 修改配置
登录成功后会进入一个网页版的控制台界面，您只需要直接将 4.1 中编辑好的文本粘贴过来，按【回车】键确认即可：
![](https://main.qcloudimg.com/raw/a9ec373ecfcc20a1cd961b4e299069f1.png)

**至此业务后台部署完成**

## 五、终端集成
终端集成主要是修改小直播 App 源码中的配置信息，主要是以下几步：

### 5.1 小直播源码下载
小直播 App 的源码位于 Github 仓库中，clone或下载源码后，可以在`Android/XiaoZhiBo`和`iOS/XiaoZhiBo`分别获取到 Android 和 iOS 的源码。
- [iOS 版本](https://github.com/tencentyun/MLVBSDK/tree/master/iOS/XiaoZhiBo)
- [Android 版本](https://github.com/tencentyun/MLVBSDK/tree/master/Android/XiaoZhiBo)

### 5.2 替换小直播后台服务器地址
小直播后台服务的地址为 `http://云主机服务器公网地址`。如 `http://134.175.197.138`:

- iOS
打开 `iOS/XiaoZhiBo/XiaoZhiBoApp/Classes/App/` 目录下的 **TCConstants.h** 文件，将文件里的 `kHttpServerAddr` 改为您的小直播后台服务的地址。

- Android 
打开 `Android/XiaoZhiBo/app/src/main/java/com/tencent/qcloud/xiaozhibo/common/utils/` 目录下的 **TCConstants.java** 文件，将文件里的 `APP_SVR_URL` 改为您的小直播后台服务的地址。

### 5.3 替换小直播 License 配置
进入【直播控制台】=>【直播SDK】=>【License管理】复制 License 的 URL 和 Key：

- iOS
    打开 `iOS/XiaoZhiBo/XiaoZhiBoApp/Classes/App/` 目录下的 **AppDelegate.m** 文件，将`[TXLiveBase setLicenceURL: key:]`调用的参数替换为您的 License URL 和 Key。
- Android 
    打开 `Android/XiaoZhiBo/app/src/main/java/com/tencent/qcloud/xiaozhibo/` 目录下的 **TCApplication.java** 文件，将`String licenceUrl`, 和 `String licenseKey` 的内容分别替换为您的 License URL 和 Key。

### 5.4 运行并测试
至此小直播的所有配置均已完成，您可以运行 App 体验小直播的各项功能。
