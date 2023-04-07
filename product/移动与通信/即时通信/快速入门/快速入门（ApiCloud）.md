本文主要介绍如何在 apicloud 平台使用腾讯云 IM 模块。

## 环境要求
|平台|版本|
|---|---|
|iOS|最低 9.0|
|Android|最低 7.0|

## 支持平台
支持 iOS 和 Android，并只适合用于在 [ApiCloud](https://www.apicloud.com) 平台创建的应用。
在 ApiCloud 平台上开发者可使用标准 HTML5（包括HTML/CSS/JS技术以及Vue/React等框架技术）或 AVM.JS 技术进行开发，一套代码同时生成 Android & iOS 原生 App。

## 前提条件

您已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号，并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。

## 操作步骤

[](id:step1)

### 步骤1：创建腾讯云应用

1. 登录 [即时通信 IM 控制台](https://console.cloud.tencent.com/im)。
  > ?如果您已有应用，请记录其 SDKAppID 并 获取密钥信息。
  > 同一个腾讯云帐号，最多可创建300个即时通信 IM 应用。若已有300个应用，您可以先 [停用并删除](https://cloud.tencent.com/document/product/269/32578#.E5.81.9C.E7.94.A8.2F.E5.88.A0.E9.99.A4.E5.BA.94.E7.94.A8) 无需使用的应用后再创建新的应用。**应用删除后，该 SDKAppID 对应的所有数据和服务不可恢复，请谨慎操作。**
2. 单击**创建新应用**，在**创建应用**对话框中输入您的应用名称，单击**确定**。
  ![](https://qcloudimg.tencent-cloud.cn/raw/febed2f15dee6ff09f066ba228c7fc27.png)
3. 请保存 SDKAppID 信息。可在控制台总览页查看新建应用的状态、业务版本、SDKAppID、标签、创建时间以及到期时间。
   ![](https://main.qcloudimg.com/raw/ed34d9294a485d8d06b3bb7e0cc5ae59.png)
4. 单击创建后的应用，左侧导航栏单击**辅助工具** > **UserSig 生成&校验**，创建一个 UserID 及其对应的 UserSig，复制签名信息，后续登录使用。
  ![](https://main.qcloudimg.com/raw/8315da2551bf35ec85ce10fd31fe2f52.png)

[](id:step2)
### 步骤2：创建 ApiCloud 应用

1. 注册并登录 [ApiCloud](https://www.apicloud.com) 平台。
2. 创建 ApiCloud 应用，请参见 [ApiCloud 新手开发指南](https://docs.apicloud.com/APICloud/junior-develop-guide)。
   
[](id:step3)
### 步骤3：在应用中添加腾讯云IM模块

**腾讯云官方IM模块名为 `tencentCloudChatSDK`。**

1. 进入 ApiCloud 网站的 [模块Store](https://www.apicloud.com/mod-sdk/ts)，搜索 `tencentCloudChatSDK` 或者直接进入 [tencentCloudChatSDK 模块页面](https://www.apicloud.com/mod_detail/147671)。
![](https://qcloudimg.tencent-cloud.cn/raw/acf5fdcb6b1a97721c9b25dc3797319e.png)
2. 单击`立即使用`，将模块添加到应用里。
3. 进入个人开发控制台，点击添加模块的App - 模块 - 已添加模块。如果看到 `tencentCloudChatSDK` 模块在已添加模块中（如图所示），则表示模块添加成功。
   ![](https://qcloudimg.tencent-cloud.cn/raw/bea0f67371f6636ada3b70ba0e088f01.png)

[](id:step4)
### 步骤4：调用 SDK 接口
1. SDK 初始化
在调用其他接口之前，需要用 sdkAppID 调用初始化接口。
```javascript
var tencentCloudChatSDK = api.require("tencentCloudChatSDK") //引用模块
        tencentCloudChatSDK.initSDK({   //调用初始化接口
            sdkAppID: '',
            logLevel: 0,
            uuid:'',
        },function(ret,err){})
```
可查看 [模块文档](https://docs.apicloud.com/Client-API/Open-SDK/tencentCloudChatSDK) 在  App 中调用相应的 SDK。
2. 用户登录
   此时，您可以使用最开始的时候，在控制台生成的测试账户，完成登录验证
```javascript
var tencentCloudChatSDK = api.require("tencentCloudChatSDK")
tencentCloudChatSDK.login({
    userID:"userID",
    userSig:"userSig"
},function(ret,err){})
```
当返回值的 code 为0时，表示登录成功。其他接口的成功返回值的 code 均为0。
>? 该账户仅限开发测试使用，应用上线前，正确的 UserSig 签发方式是将 UserSig 的计算代码集成到您的服务端，并提供面向 App 的接口。在需要 UserSig 时由您的 App 向业务服务器发起请求获取动态 UserSig。更多详情请参见 服务端生成 UserSig。
>
3. 发送单聊普通文本消息
   初始化并登录成功后可以尝试发送消息。除普通文本消息之外，SDK 还支持发送自定义、图片、文件、视频、地理位置等消息。具体内容可以参考模块文档。
```javascript
var tencentCloudChatSDK = api.require("tencentCloudChatSDK")
tencentCloudChatSDK.sendC2CTextMessage({text:"",userID:""},function(ret,err){})
```
> ?文本消息支持云端脏词过滤，如果用户发送消息时有敏感词，回调就会返回80001错误码。如果发送失败，可能是由于您的 sdkAppID 不支持陌生人发送消息，您可至控制台开启，用于测试。请在控制台关闭好友关系链检查。
> 
4. 获取会话列表 
在上一个步骤中，完成发送测试消息，现在可登录另一个测试账户，拉取会话列表。
常见应用场景为：
在启动应用程序后立即获取会话列表，然后监听长链接以实时更新会话列表的变化。
```javascript
var tencentCloudChatSDK = api.require("tencentCloudChatSDK")
tencentCloudChatSDK.getConversationList({nextSeq:,count:1},function(ret,err){})
```
>?若上一步骤消息发送成功，则可以在会话列表中看到发送成功的消息。
5. 添加高级消息的事件监听器	
可以通过添加高级消息事件监听器，在有新的消息时调用回调函数。设置事件监听器如下：
```javascript
var tencentCloudChatSDK = api.require("tencentCloudChatSDK")
tencentCloudChatSDK.addAdvancedMsgListener({"uuid":""},function(ret,err){})
```
设置成功后可以通过 setEventListener 监听。

以上您已经基本完成了 IM 模块的开发，可以发送接受消息并且进入会话列表。
您可以继续完成 群组，用户资料，关系链，离线推送，本地搜索 等相关功能开发。

### 步骤5：编译并运行

1. 下载 [Apicloud Studio](https://www.apicloud.com/studio3#downloadBtn)。
2. 点击 模块 - 自定义loader 分别编译 iOS 和 Android 自定义 loader。编译自定义 loader 需要 iOS 和 Android 证书。
   ![](https://qcloudimg.tencent-cloud.cn/raw/df26a6c3f0b70404bfddb292b5857974.png)
3. 编译后下载到相应的真机或模拟器中可以通过 ApiCloud Studio 使用 Wi-Fi 真机同步或 USB 真机同步对 App 进行实时编译调试。 具体内容可以参见 [ApiCloud 文档](https://docs.apicloud.com/apicloud3/#wifi-sync)。

### 可选操作：开通内容审核功能
在消息发送、资料修改场景中，很有可能会扩散不合适的内容，特别是与敏感事件/人物相关、黄色不良内容等令人反感的内容，不仅严重损害了用户们的身心健康，更很有可能违法并导致业务被监管部门查封。

即时通信 IM 支持内容审核（反垃圾信息）功能，可针对不安全、不适宜的内容进行自动识别、处理，为您的产品体验和业务安全保驾护航。可以通过以下两种内容审核方式来实现：
- [本地审核功能](https://cloud.tencent.com/document/product/269/83795#bdsh)：在客户端本地检测在单聊、群聊、资料场景中由即时通信 SDK 发送的文本内容，支持对已配置的敏感词进行拦截或者替换处理。此功能通过在 IM 控制台开启服务并配置词库的方式实现。
- [云端审核功能](https://cloud.tencent.com/document/product/269/83795#ydsh)：在服务端检测由单聊、群聊、资料场景中产生的文本、图片、音频、视频内容，支持针对不同场景的不同内容分别配置审核策略，并对识别出的不安全内容进行拦截。此功能已提供默认预设拦截词库和审核场景，只需在 IM 控制台打开功能开关，即可直接使用。


## 常见问题
1. 添加 `tencentCloudChatSDK`模块后编译失败？
   可能是与您的 App 中已添加的其他腾讯云 IM SDK 模块冲突。请您检查您的 App 中是否还存在其他腾讯云 IM SDK 模块，并删除。其他腾讯云 IM 模块已全部停止维护，若以前使用过其他腾讯云 IM 模块，请您移植到官方的模块。官方模块提供最全的功能并持续维护。
2. 运行时显示模块未添加，但在已添加模块中显示已添加？
   编译时使用自带的云编译会出现上述问题。需要使用自定义 loader 进行编译。


## 联系我们
如果您在接入过程中有任何疑问，请扫码加入微信群咨询。
<img src="https://qcloudimg.tencent-cloud.cn/raw/f348789d03975dc153a6203b8744f335.jpg" width="50%"></img>
