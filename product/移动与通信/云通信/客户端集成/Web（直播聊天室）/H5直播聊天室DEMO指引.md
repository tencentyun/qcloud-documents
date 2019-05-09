## 官网 SDK 和 Demo



## 1. 创建应用

登录腾讯云通信（IM）[控制台](https://console.cloud.tencent.com/avc)，在**应用列表**页，单击【创建应用接入】，在**创建新应用**弹框中，填写新建应用的信息，单击【确认】：
![](https://main.qcloudimg.com/raw/a7769d15f050286162b0cbcdadca5f03.png)

应用创建完成后，自动生成一个应用标识：SdkAppId，如下图：
![](https://main.qcloudimg.com/raw/bf8fe4f38d782741a6e142c24648c9e0.png)

## 2. 配置应用

完成创建应用之后返回应用列表，单击对应 SdkAppId 的**应用配置**链接，在应用详情页，找到当前页面的**帐号体系集成**部分，单击**编辑**链接，配置**账号管理员**信息，然后单击【保存】：

>   ?账号管理员可以随便填写，在使用云通信后台的 REST API 发送消息时才会用到。

![](https://main.qcloudimg.com/raw/e3ce0ef527d2d4f8d0b3a0f69cefa78e.png)

## 3. 获取测试 userSig

完成账号管理员配置后，单击**下载公私钥**的链接，即可获得一个名为 **keys.zip** 的压缩包。解压后可以得到两个文件，即 public_key 和 private_key，用记事本打开 **private_key** 文件，并将其中的内容拷贝到**开发辅助工具**的私钥文本输入框中。

其中：**identifier** 即为您的测试账号（也就是 userId），私钥为 private_key 文件里的文本内容，生成的签名就是**userSig**。identifier 和 userSig 是一一对应的关系。

>   ! 可以多生成4组以上的 userid 和 usersig，方便在 Demo 中调试使用。

![](https://main.qcloudimg.com/raw/a1b9bb35760e1e52825c754bd3ef9a52.png)



## 4. 运行 Demo

从 [Github](<https://github.com/tencentyun/TIMSDK/tree/master/H5-AVChatRoom>) 下载 SDK 和 Demo

### 4.1 准备直播大群 ID

运行 Demo 之前，需要创建一个 AVChatRoom 类型（直播聊天室）的群组 ID。可以通过 restapi 创建，也可以使用在其他平台（Android 或者 iOS）上创建的直播聊天室 ID。详情请参考 [创建群组](https://cloud.tencent.com/doc/product/269/%E5%88%9B%E5%BB%BA%E7%BE%A4%E7%BB%84) 。

**restapi 调试地址：**

`https://avc.cloud.tencent.com/im/APITester/APITester.html`



### 4.2 运行 Demo

**修改业务信息：**

```
var sdkAppID = 1400001692;//开发者改成自己的业务 ID
```

**修改直播大群 ID：**

```
//默认房间群ID，开发者可以改成自己的直播聊天室 ID
var avChatRoomId = '@TGS#aJIPTVAEE';
```

访问 Demo，这里以谷歌浏览器为例，**打开浏览器输入地址：**

`http://localhost:8080/webim/biggroup/mobile/index.html`

**效果如下：**

![](//mccdn.qcloud.com/static/img/9994fb0d0f4073a77f5766a7abd5283d/image.png)

**模拟手机访问，按 F12，单击下图箭头所指的手机图标：**


![](//mccdn.qcloud.com/static/img/e71c925af3ea9d2e04ca0dbbea86fcee/image.png)

填写登录用户信息 `identifier` 和 `userSig`，`userSig` 需要开发者在自己的服务器调用 TLS API 生成。详情参考 [TLS 后台 API 使用手册](https://cloud.tencent.com/doc/product/269/TLS%E5%90%8E%E5%8F%B0API%E4%BD%BF%E7%94%A8%E6%89%8B%E5%86%8C)。

![](//mccdn.qcloud.com/static/img/c604fbde4569278532eebc6d5eb7ebc7/image.png)

单击确定，拿到登录用户信息 `identifier` 和 `userSig` 放入 `loginInfo` 去登录 SDK。

```javascript
//当前用户身份
var loginInfo = {
     'sdkAppID': sdkAppID, //用户所属应用 ID,必填
     'appIDAt3rd': sdkAppID, //用户所属应用 ID，必填
     'identifier': ‘xxxxxx’, //当前用户 ID，需要开发者填写
     'identifierNick': null, //当前用户昵称，选填
     'userSig': 'xxxxxxx', //当前用户身份凭证，需要开发者填写
     'headurl': 'img/2016.gif'//当前用户默认头像，选填
 };
```

**登录成功可以进行评论，点赞：**

![](//mccdn.qcloud.com/static/img/aa37dcc2c32aa47c57f107bd0ea8785c/image.png)




-  单击体验 [通用 Demo](http://avc.cloud.tencent.com/demo/webim/index.html)。

-  单击了解 [通用 Demo 运行指引](https://cloud.tencent.com/doc/product/269/4196)。