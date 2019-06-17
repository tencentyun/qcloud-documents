>!当前小程序版本 Demo 仅提供直播聊天室场景。

## 1. 创建应用

1. 登录腾讯云通信 IM [控制台](https://console.cloud.tencent.com/avc)。
2. 在【应用列表】页面，单击【创建应用接入】。
3. 在【创建新应用】弹框中，填写新建应用的信息，单击【确认】。
 ![](https://main.qcloudimg.com/raw/a7769d15f050286162b0cbcdadca5f03.png)
 应用创建完成后，自动生成一个应用标识：SDKAppID，如下图：
![](https://main.qcloudimg.com/raw/bf8fe4f38d782741a6e142c24648c9e0.png)

## 2. 配置应用

1. 在【应用列表】页面，单击对应 SDKAppID 的【应用配置】，进入应用详情页面。
 ![](https://main.qcloudimg.com/raw/b6655906590c0b9bdcd1e0c21776fa93.png)
2. 单击【帐号体系集成】右侧的【编辑】，配置**帐号管理员**信息，单击【保存】。
 ![](https://main.qcloudimg.com/raw/2ad153a77fe6f838633d23a0c6a4dde1.png)
 >?在使用云通信 IM 后台的 REST API 发送消息时会用到帐号管理员信息。

## 3. 获取测试 userSig
1. 在应用详情页面，单击**帐号体系集成**右侧的【下载公私钥】，保存 **keys.zip** 压缩文件。
 ![](https://main.qcloudimg.com/raw/c44938b9268d0ef76c68b8bf61689219.png)
2. 解压 **keys.zip** ，获得 **private_key** 和 **public_key** 文件，其中 **private_key** 即为私钥文件。
 ![](https://main.qcloudimg.com/raw/95875a7baca63c21103bc6cd6dac0279.png)
4.  在应用详情页面，选择【开发辅助工具】页签，填写【用户名（Identifier）】，拷贝私钥文件 **private_key** 中的内容至【私钥】文本框中，单击【生成】，在【签名】文本框中即可获得该云通信 IM 应用指定用户名的 UserSig。
 ![](https://main.qcloudimg.com/raw/0439e0c6f69ec2187035697f4a364b5b.png)

>?可以生成4组或以上 userid 和 usersig，方便在 Demo 中调试使用。

## 4. 运行 Demo

从 [Github](<https://github.com/tencentyun/TIMSDK/tree/master/H5/AVChatRoom>) 下载 IM SDK 和 Demo。

### 4.1 准备直播大群 ID

运行 Demo 之前，需要创建一个 AVChatRoom 类型（直播聊天室）的群组 ID。可以通过 REST API 创建，也可以使用在其他平台（Android 或者 iOS）上创建的直播聊天室 ID。详情请参考 [创建群组](https://cloud.tencent.com/doc/product/269/%E5%88%9B%E5%BB%BA%E7%BE%A4%E7%BB%84) 。

**REST API  调试地址：**`https://avc.cloud.tencent.com/im/APITester/APITester.html`

### 4.2 运行 Demo

1. 运行以下代码，修改业务信息。
```
//开发者改成自己的业务 ID
var sdkAppID = 1400001692;
//默认房间群 ID，开发者可以改成自己的直播聊天室 ID
var avChatRoomId = '@TGS#aJIPTVAEE';
``` 
 效果如下：
 ![](https://mccdn.qcloud.com/static/img/9994fb0d0f4073a77f5766a7abd5283d/image.png)
2. 模拟手机访问，按 F12，单击下图箭头所指的手机图标。
![]( https://mccdn.qcloud.com/static/img/e71c925af3ea9d2e04ca0dbbea86fcee/image.png)
3. 填写登录用户信息 `identifier` 和 `userSig`，`userSig` 需要开发者在自己的服务器调用 TLS API 生成。详情请参考 [TLS 后台 API 使用手册](https://cloud.tencent.com/doc/product/269/TLS%E5%90%8E%E5%8F%B0API%E4%BD%BF%E7%94%A8%E6%89%8B%E5%86%8C)。
![](https://mccdn.qcloud.com/static/img/c604fbde4569278532eebc6d5eb7ebc7/image.png)
4. 单击【确定】，拿到登录用户信息 `identifier` 和 `userSig` 放入 `loginInfo` 去登录 IM SDK。
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
登录成功可以进行评论，点赞：
![](https://mccdn.qcloud.com/static/img/aa37dcc2c32aa47c57f107bd0ea8785c/image.png)

## 更多操作
-  单击体验 [通用 Demo](http://avc.cloud.tencent.com/demo/webim/index.html)。
-  单击了解 [通用 Demo 运行指引](https://cloud.tencent.com/doc/product/269/4196)。
