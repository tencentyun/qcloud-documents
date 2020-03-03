## 官网 SDK 和 Demo



## 1. 创建应用

登录腾讯即时通信（IM）[控制台](https://console.cloud.tencent.com/avc)，在**应用列表**页，单击【创建应用接入】，在**创建新应用**弹框中，填写新建应用的信息，单击【确认】：
![](https://main.qcloudimg.com/raw/a7769d15f050286162b0cbcdadca5f03.png)

应用创建完成后，自动生成一个应用标识：SdkAppId，如下图：
![](https://main.qcloudimg.com/raw/bf8fe4f38d782741a6e142c24648c9e0.png)

## 2. 配置应用

完成创建应用之后返回应用列表，单击对应 SdkAppId 的**应用配置**链接，在应用详情页，找到当前页面的**帐号体系集成**部分，单击**编辑**链接，配置**账号管理员**信息，然后单击【保存】：

>   ?账号管理员可以随便填写，在使用即时通信后台的 REST API 发送消息时才会用到。

![](https://main.qcloudimg.com/raw/e3ce0ef527d2d4f8d0b3a0f69cefa78e.png)

## 3. 获取测试 userSig

完成账号管理员配置后，单击**下载公私钥**的链接，即可获得一个名为 **keys.zip** 的压缩包。解压后可以得到两个文件，即 public_key 和 private_key，用记事本打开 **private_key** 文件，并将其中的内容拷贝到**开发辅助工具**的私钥文本输入框中。

其中：**identifier** 即为您的测试账号（也就是 userId），私钥为 private_key 文件里的文本内容，生成的签名就是**userSig**。identifier 和 userSig 是一一对应的关系。

>   ! 可以多生成4组以上的 userid 和 usersig，方便在 Demo 中调试使用。

![](https://main.qcloudimg.com/raw/a1b9bb35760e1e52825c754bd3ef9a52.png)



## 运行 Demo

从 [Github](<https://github.com/tencentyun/TIMSDK/tree/master/H5-AVChatRoom>) 下载 SDK 和 Demo


### 运行 Demo


- 编辑 Demo 根目录下的 `index.html`。

- 修改业务信息：

```javascript
//demo appid
var sdkAppID = 1400001533;//开发者改成自己的业务 ID
```

- 访问 Demo，这里拿谷歌浏览器举例。进入登录页：

![](https://mccdn.qcloud.com/static/img/100c4f8b786c2ffa2f0c3ee3cff5f226/image.png)

- 填写登录用户信息 `identifier` 和 `userSig`，`userSig` 需要开发者在自己的服务器调用 TLS API 生成。详细参见 [TLS 后台 API 使用手册](https://cloud.tencent.com/document/product/269/1510)。

![](//mccdn.qcloud.com/static/img/8ae083b639696feec038a69861464e46/image.png)

- 单击确定，拿到登录用户信息 `identifier` 和 `userSig` 放入 `loginInfo` 去登录 SDK。

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

- 登录成功，这样就可以进行查找好友，建群，聊天等操作了。
 ![](https://mccdn.qcloud.com/static/img/fd864c05877f3d2d7229041a0e33ca9d/image.png)

- 和好友聊天：
 ![](https://mccdn.qcloud.com/static/img/456ac262b7b13ae8946e2875c68bd3de/image.png)

- 群聊：
 ![](https://mccdn.qcloud.com/static/img/22b8afaab9f244e9bcf4cf34c4f0e42a/image.png)
