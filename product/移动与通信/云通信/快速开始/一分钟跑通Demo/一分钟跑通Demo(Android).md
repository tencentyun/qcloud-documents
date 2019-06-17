
本文主要介绍如何快速地将腾讯云云通信 Demo(Android) 工程运行起来，您只需参考如下步骤依次执行即可。

## 1. 创建应用
登录腾讯云通信（IM）[控制台](https://console.cloud.tencent.com/avc)，在**应用列表**页，单击【创建应用接入】，在**创建新应用**弹框中，填写新建应用的信息，单击【确认】：
![](https://main.qcloudimg.com/raw/a7769d15f050286162b0cbcdadca5f03.png)

应用创建完成后，自动生成一个应用标识：SDKAPPID，如下图：
![](https://main.qcloudimg.com/raw/bf8fe4f38d782741a6e142c24648c9e0.png)

## 2. 配置应用
完成创建应用之后返回应用列表，单击对应 SDKAPPID 的**应用配置**链接，在应用详情页，找到当前页面的**帐号体系集成**部分，单击**编辑**链接，配置**账号管理员**信息，然后单击【保存】：

>?账号管理员可以随便填写，在使用云通信后台的 REST API 发送消息时才会用到。

![](https://main.qcloudimg.com/raw/e3ce0ef527d2d4f8d0b3a0f69cefa78e.png)


## 3. 下载公私钥
点击**下载公私钥**的链接，即可获得一个名为 **keys.zip** 的压缩包，解压后可以得到两个文件，即 public_key 和 private_key，用记事本打开 **private_key** 文件

![](https://cdn.nlark.com/yuque/0/2019/png/367185/1560754915512-fc218293-1316-445f-91aa-f7314ba23b30.png#align=left&display=inline&height=1788&name=Snip20190617_7.png&originHeight=1788&originWidth=3776&size=2105704&status=done&width=3776)


## 4. 下载 Demo 源码
从 [Github](https://github.com/tencentyun/TIMSDK/tree/master/Android) 下载Android Demo工程。

## 5. 修改源码配置
- 使用 Android Studio （3.0 以上的版本）  打开源码工程。

- 虽然工程中默认配置了测试的 SDKAPPID ，但是您需要替换成您 step 1 中您自己的 SDKAPPID ，由于每个账号同时只能有一个端登录，你可以用多台手机来登录不同的账号，以便互相通信，

- 在 /TIMSDK/Android/app/src/main/java/com/tencent/qcloud/tim/demo/utils/Constants.java 中替换您的 SDKAPPID。
![](https://main.qcloudimg.com/raw/260d0bea33a644b519fd11d612df770b.png)

- 在 step 3 中下载公私钥并打开 **private_key** 文件后，并将其中的所有内容拷贝到 **/TIMSDK/Android/app/src/main/java/com/tencent/qcloud/tim/demo/signature/GenerateTestUserSig.java** 文件中定义的常量 **PRIVATEKEY** 。
![](https://main.qcloudimg.com/raw/d9e6f60bbe4b6c23fa3886ab16a4afd3.png)

通过 **GenerateTestUserSig** 中的 **genTestUserSig** 方法就可以自动帮你帮您获取测试 **userSig** 。

>?** GenerateTestUserSig** 所使用的代码虽然能够正确计算出 UserSig，但仅适合快速调通 SDK 的基本功能。因为客户端代码中的 PRIVATEKEY 很容易被反编译逆向破解，一旦您的私钥泄露，攻击者就可以盗用您的腾讯云流量，所以更推荐的做法是将 UserSig 的计算代码放在您的业务服务器上，然后由您的 App 在需要的时候向您的业务服务器获取临时生成的 UserSig。

> ! 再次提醒的是：这里提到的获取测试 **userSig**方案仅适合本地跑通demo和功能调试，userSig 正确的签发和获取方式请参考 [服务器获取方案](https://cloud.tencent.com/document/product/269/1507)。

## 6. 编译运行
APP启动后，在不同的手机上登录不同的账号，就可以添加对方的 userId 体验收发消息，以及其他功能。

## 7. 效果图

会话列表，通讯录相关界面演示：
<div>
<img src="https://cdn.nlark.com/yuque/0/2019/gif/367185/1560518740493-e5a89223-4cb4-44df-a9a5-665e78b67983.gif#align=left&display=inline&height=674&name=%E4%BC%9A%E8%AF%9D%E5%88%97%E8%A1%A8.gif&originHeight=674&originWidth=380&size=319844&status=done&width=380" width="300" height="535">
</div>
聊天界面收发消息演示：
<div>
<img src="https://cdn.nlark.com/yuque/0/2019/gif/367185/1560519391978-f7dbd5fa-8ee7-4b4c-9e71-c7e8d6c5b01b.gif#align=left&display=inline&height=674&name=%E8%81%8A%E5%A4%A9%E6%BC%94%E7%A4%BA.gif&originHeight=674&originWidth=380&size=918355&status=done&width=380" width="300" height="535">
</div>
输入区域自定义部分功能演示：
<div>
<img src="https://cdn.nlark.com/yuque/0/2019/gif/366128/1559825875054-fdfb0919-1f59-4382-924a-b2197f813ab4.gif#align=left&display=inline&height=533&name=add.gif&originHeight=1920&originWidth=1080&size=547272&status=done&width=300" width="300" height="535">
</div>
输入区域自定义按钮事件演示：
<div>
<img src="https://cdn.nlark.com/yuque/0/2019/gif/366128/1559825509248-ebb52b9b-8fee-421f-ad32-f2a12192167c.gif#align=left&display=inline&height=533&name=replace%2B.gif&originHeight=1920&originWidth=1080&size=177751&status=done&width=300" width="300">
</div>
输入区域自定义全部功能演示：
<div>
<img src="https://cdn.nlark.com/yuque/0/2019/gif/366128/1559826601807-394ea189-6188-47e7-bfe8-bb19c67b9dbb.gif#align=left&display=inline&height=587&name=new.gif&originHeight=1920&originWidth=1080&size=508813&status=done&width=330" width="300" height="535">
</div>
