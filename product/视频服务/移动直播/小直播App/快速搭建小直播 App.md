## 一、 开通云服务
### 开通直播服务

#### 1. 申请开通视频直播服务
进入 [直播管理控制台](https://console.cloud.tencent.com/live)，如果服务还没有开通，则会有如下提示:
![](https://mc.qcloudimg.com/static/img/c40ff3b85b3ad9c0cb03170948d93555/image.png)
单击申请开通，之后会进入腾讯云人工审核阶段，审核通过后即可开通。


#### 2. 配置直播码
直播服务开通后，进入[【直播控制台】>【直播码接入】>【接入配置】](https://console.cloud.tencent.com/live/livecodemanage) 完成相关配置，即可开启直播码服务：
![](https://mc.qcloudimg.com/static/img/32158e398ab9543b5ac3acf5f04aa86e/image.png)
单击【确定接入】按钮即可。

#### 3. 获取直播服务配置信息
从直播控制台获取`APP_ID`、`APP_BIZID`、`API_KEY`，后面配置服务器会用到：
![](https://main.qcloudimg.com/raw/b958c4d3ad29fd6114f92e0c8f7ca458.png)

### 开通云通信服务
#### 1. 申请开通云通讯服务
进入[云通讯管理控制台](https://console.cloud.tencent.com/avc)，如果还没有服务，直接单击**直接开通云通讯**按钮即可。新认证的腾讯云账号，云通讯的应用列表是空的，如下图：
![](https://mc.qcloudimg.com/static/img/c033ddba671a514c7b160e1c99a08b55/image.png)

单击**创建应用接入**按钮创建一个新的应用接入，即您要接入腾讯云IM通讯服务的App的名字，如下图所示：
![](https://main.qcloudimg.com/raw/fef0a15ebab000272cd74339d4e38c18.png)

单击确定按钮，之后就可以在应用列表中看到刚刚添加的项目了，如下图所示：
![](https://main.qcloudimg.com/raw/3d522dff19265a5d508ceddf64f15d0e.png)

#### 2. 配置独立模式
上图的列表中，右侧有一个**应用配置**按钮，单击这里进入下一步的配置工作，如下图所示。
![](https://mc.qcloudimg.com/static/img/3e9cd34ca195036e21cb487014cc2c81/yuntongxing3.png)

#### 3. 获取云通讯服务配置信息
从云通信控制台获取`IM_SDKAPPID`、`IM_ACCOUNTTYPE`、`ADMINISTRATOR`、`PRIVATEKEY`、`PUBLICKEY`，后面配置服务器会用到：
![](https://main.qcloudimg.com/raw/13ea29f1692106bafd9895e7624e167a.png)

从验证方式中下载公私钥，解压出来将private_key用文本编辑器打开，如：

```bash
-----BEGIN PRIVATE KEY-----
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
-----END PRIVATE KEY-----
```
将上面的内容直接复制到后面的配置脚本中，用于在小直播后台生成IM签名。
将其转换成字符串形式如下所示，后面在server配置文件(config.js)中使用，<font color='red'>请注意每行后面要加入\r\n</font>：

```bash
"-----BEGIN PRIVATE KEY-----\r\n"+
"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\r\n"+
"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\r\n"+
"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\r\n"+
"-----END PRIVATE KEY-----\r\n"
```

### 开通对象存储服务
#### 1. 申请开通对象存储服务
进入[对象存储服务控制台](https://console.cloud.tencent.com/cos5)，如果还没有服务，直接单击**创建存储桶**按钮即可，如下图：
![](https://main.qcloudimg.com/raw/caae5820c4b9ab4fa0a9803e7530d263.png)

#### 2. 创建bucket获取基本信息
填写bucket名，选择bucket所属地域，读写权限创建存储桶。
![](https://main.qcloudimg.com/raw/e2ba00ee3b3b9fd3ab40b67cfd0564c0.jpg)

单击确定按钮，之后就进入了刚刚创建的存储桶管理界面，选择基础配置获取`COSKEY_APPID`、`COSKEY_BUCKET`、`COSKEY_BUCKET_REGION`等信息，后面配置服务器会用到。
![](https://main.qcloudimg.com/raw/4a9bd0154fa2820887e1a0c79a7d7f0b.jpg)

#### 3. 获取密钥信息
进入[【对象存储控制台】>【密钥】>【云API密钥】](https://console.cloud.tencent.com/cam/capi)获取`COSKEY_SECRETID`、`COSKEY_SECRETKEY`
![](https://main.qcloudimg.com/raw/b5c6e9471d22d20591d23464dbf717a6.jpg)

## 二、 集成和部署业务后台

### 腾讯云CVM镜像部署

**第一步** [新建CVM主机](https://console.cloud.tencent.com/cvm) 
 ![](http://mc.qcloudimg.com/static/img/53d7df9e5a8bc5141e55231076cbfd74/image.png)

**第二步** 进服务市场选取镜像 推荐使用图中的**小直播镜像**。
 ![](https://main.qcloudimg.com/raw/da14288ee7196c45f0d3fcc4def88567.png)
 
**第三步** 配置硬盘和网络，以及云主机访问密码，妥善保管好密码，然后设置安全组。
![](https://main.qcloudimg.com/raw/c265b5c870f6a7ecb2f15f83f7c508c4.jpg)

**第四步** 付款后生成云主机。单击登录可以通过腾讯云的网页shell进行访问，也可以用 **putty** 或 **SecretCRT** 采用ssh登录到主机。
![](http://mc.qcloudimg.com/static/img/0f29fd40aae5fdac10d3f6262eb6a03e/image.png)

**第五步** 修改云主机配置信息

将如下脚本中的`APP_ID`、`APP_BIZID`、`API_KEY`、`COSKEY_BUCKET`、`COSKEY_BUCKET_REGION`、`COSKEY_SECRECTKEY`、 `COSKEY_APPID`、`COSKEY_SECRECTID`、`IM_SDKAPPID`、`IM_ACCOUNTTYPE`配置成上述直播服务、云通信服务、COS服务里生成的值并保存。<font color='red'>然后登录云主机，直接在云主机上执行修改后的脚本</font>。
下面代码中第一个echo后跟着的双引号内是IM私钥的文本信息，把云通信的private_key用文本编辑工具打开复制下来填到双引号内就可以了。

<font color='red'>注意：请在本地修改以下配置并复制，然后登录云主机在控制台粘贴回车执行</font>。

```bash
#!/bin/bash
echo "-----BEGIN PRIVATE KEY-----
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
-----END PRIVATE KEY-----" > /data/live_demo_service/deps/sig/private_key;
echo "<?php
define('APP_ID',123456);  //请替换为您申请的直播服务的appid
define('APP_BIZID',1234);  //请替换为您申请的直播服务的bizid
define('API_KEY','xxxxxxxx'); //api key

define('COSKEY_BUCKET','xxxxxxxx'); //请替换为对象和存储服务（COS）中您所新建的bucket
define('COSKEY_BUCKET_REGION','xxxxxxxx'); //请替换为对象和存储服务（COS）中您所新建的bucket的地域
define('COSKEY_SECRECTKEY','xxxxxxxx'); //请替换为对象和存储服务（COS）中您所新建的secrectkey
define('COSKEY_APPID',123456); //请替换为对象和存储服务（COS）的appid
define('COSKEY_SECRECTID','xxxxxxxx'); //请替换为对象和存储服务（COS）中您所新建的secrectid（和secrectkey配对）
define('COSKEY_EXPIRED_TIME',30);

define('IM_SDKAPPID',123456);   // 云通信 sdkappid
define('IM_ACCOUNTTYPE', '1234');  // 云通信 账号集成类型
?>" > /data/live_demo_service/conf/OutDefine.php;
```

**至此业务后台部署完成**

## 三、 配置 RoomService 服务

首先下载[RoomTool工具](http://download-1252463788.file.myqcloud.com/RoomTool/RoomTool.zip) 并解压缩。

**第一步** 安装Nodejs环境
![](https://main.qcloudimg.com/raw/cc2d675ae964e524a5375494b1ed4a7d.png)

**第二步** 修改工具包根目录下的config.js文件中的参数，替换成上述直播服务及云通信服务里生成的值。

 ![](https://main.qcloudimg.com/raw/7e8db26c6384433396df233ab5870e80.png)


**第三步** 提交配置参数

进入到目录RoomTool，执行以下命令提交配置参数：

```bash
node setConfigInfo.js 1   //1表示传送私钥给腾讯云RoomService后台
```

 ![](https://main.qcloudimg.com/raw/8306b0aac96fbe65b320fb07a83a8c8d.png)

提交成功后可以执行node genLoginInfo.js命令来验证参数是否配置成功。

## 四、 终端集成及回调设置

终端集成主要是小直播源码集成，主要是以下简单几步：
### 小直播源码下载
[小直播源码下载](https://cloud.tencent.com/document/product/454/7873#Xiaozhibo)，单击后下载**小直播IOS**和**小直播Android**

### 替换小直播后台服务器地址
- iOS

> 源码包解压后在 TCLVBIMDemo/Classes/LVB/Base 目录下有一个**TCConstants.h**文件，将文件里的`kHttpServerAddr`改成您的云主机服务器地址。

- Android 

> 源码包解压后在 app/src/main/java/com/tencent/qcloud/xiaozhibo/common/utils  目录下有一个**TCConstants.java**文件，将文件里的`APP_SVR_URL`改成您的云主机服务器地址。

`注意：如果服务器没有配置证书，这里的云主机服务器地址需要用http，而不能用https。`

### 设置回调地址
在直播管理控制台设置回调地址，腾讯云后台在相应事件发生时（如流状态改变、视频录制完成、截图完成等），通过该地址回调给业务服务器，业务服务器做相应处理，事件回调的详细信息可以参考[事件消息通知](https://cloud.tencent.com/document/product/267/5957)
配置方式，在[直播控制台>>直播码接入>>接入配置](https://console.cloud.tencent.com/live/livecodemanage)配置回调URL，如果您未修改过小直播业务服务器的代码，回调URL的格式为：

```bash
http://您的云主机服务器地址/callback/tape_callback.php
```

![](http://mc.qcloudimg.com/static/img/b0a78a4b974824940abe811d42fb0561/image.jpg)

