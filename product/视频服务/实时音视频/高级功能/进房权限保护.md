## 内容介绍

如果您希望给某些房间中加入进房限制或者上麦限制，也就是仅允许指定的用户去进房或者上麦，而您又担心在客户端判断权限很容易遭遇破解攻击，那么可以考虑**开启高级权限控制**。

在如下场景下，您并不需要开启高级权限控制的：

- 情况1：本身希望越多的人观看越好，对进入房间的权限控制无要求。
- 情况2：对攻击者破解客户端的防范需求不迫切。

在如下场景下，建议您开启高级权限控制以获得更佳的安全性：

- 情况1：对安全性要求较高的视频通话或者语音通话场景。
- 情况2：对不同房间设置不同进入权限的场景。
- 情况3：对观众上麦有权限控制的场景。


## 支持的平台

|   iOS    | Android  |  Mac OS  | Windows  | Electron | 微信小程序 | Web 端 |
| :------: | :------: | :------: | :------: | :------: | :--------: | :-----------: |
| &#10003; | &#10003; | &#10003; | &#10003; | &#10003; |  &#10003;  |   &#10003;    |

## 高级权限控制的原理

开启高级权限控制后，TRTC 的后台服务系统就不会仅校验 UserSig 这一个“进房票据”，还会校验一个叫做 **PrivateMapKey**  的“权限票据”，权限票据中包含了一个加密后的 roomid 和一个加密后的“权限位列表”。

由于 PrivateMapKey 中包含 roomid，所以当用户只提供了 UserSig 没有提供 PrivateMapKey 时，并不能进入指定的房间。

PrivateMapKey 中的“权限位列表”使用了一个 byte 中的 8 个比特位，分别代表了持有该票据的用户，在该票据指定的房间中所拥有的八种具体的功能权限：

| 位数    | 二进制表示 | 十进制数字 | 权限含义                             |
| ------- | ---------- | :--------: | ------------------------------------ |
| 第 1 位 | 0000 0001  |     1      | 创建房间的权限                       |
| 第 2 位 | 0000 0010  |     2      | 进入房间的权限                       |
| 第 3 位 | 0000 0100  |     4      | 发送语音的权限                       |
| 第 4 位 | 0000 1000  |     8      | 接收语音的权限                       |
| 第 5 位 | 0001 0000  |     16     | 发送视频的权限                       |
| 第 6 位 | 0010 0000  |     32     | 接收视频的权限                       |
| 第 7 位 | 0100 0000  |     64     | 发送辅路（也就是屏幕分享）视频的权限 |
| 第 8 位 | 1000 0000  |    128     | 接收辅路（也就是屏幕分享）视频的权限 |


## 开启高级权限控制
[](id:step1)
### 步骤1：在 TRTC 控制台中开启高级权限控制

1. 在腾讯云实时音视频控制台中单击左侧的 [**应用管理**](https://console.cloud.tencent.com/trtc/app)。
2. 在右侧的应用列表中选择想要开启高级权限控制的一款应用，并单击 **功能配置**。
3. 在“功能配置”页卡中打开 **启用高级权限控制** 按钮，单击 **确定**，即可开启高级权限控制。
![](https://main.qcloudimg.com/raw/8fd4b0d09aeea46a15714c59e5e0419e.png)


>!当某一个 SDKAppid 开启高级权限控制后，使用该 SDKAppid 的所有用户都需要在 TRTCParams 中传入 `privateMapKey` 参数才能成功进房（如 [步骤 2](#step2) 所述），如果您线上有使用此 SDKAppid 的用户，请不要轻易开启此功能。

[](id:step2)
### 步骤2：在您的服务端计算 PrivateMapKey

由于 PrivateMapKey 的价值就是为了防止客户端被逆向破解，从而出现“非会员也能进高等级房间”的破解版本，所以它只适合在您的服务器计算再返回给您的 App，绝不能在您的 App 端直接计算。

我们提供了 Java、GO、PHP、Node.js、Python、C# 和 C++ 版本的 PrivateMapKey 计算代码，您可以直接下载并集成到您的服务端。

| 语言版本 |                         关键函数                         |                           下载链接                           |
| :------: | :------------------------------------------------------: | :----------------------------------------------------------: |
|   Java   | `genPrivateMapKey` 和 `genPrivateMapKeyWithStringRoomID` | [Github](https://github.com/tencentyun/tls-sig-api-v2-java/blob/master/src/main/java/com/tencentyun/TLSSigAPIv2.java) |
|    GO    | `GenPrivateMapKey` 和 `GenPrivateMapKeyWithStringRoomID` | [Github](https://github.com/tencentyun/tls-sig-api-v2-golang/blob/master/tencentyun/TLSSigAPI.go) |
|   PHP    | `genPrivateMapKey` 和 `genPrivateMapKeyWithStringRoomID` | [Github](https://github.com/tencentyun/tls-sig-api-v2-php/blob/master/src/TLSSigAPIv2.php) |
|  Node.js | `genPrivateMapKey` 和 `genPrivateMapKeyWithStringRoomID` | [Github](https://github.com/tencentyun/tls-sig-api-v2-node/blob/master/TLSSigAPIv2.js) |
|  Python  | `genPrivateMapKey`和 `genPrivateMapKeyWithStringRoomID`  | [Github](https://github.com/tencentyun/tls-sig-api-v2-python/blob/master/TLSSigAPIv2.py) |
|    C#    | `genPrivateMapKey`和 `genPrivateMapKeyWithStringRoomID`  | [Github](https://github.com/tencentyun/tls-sig-api-v2-cs/blob/master/tls-sig-api-v2-cs/TLSSigAPIv2.cs) |
|   C++    | `genPrivateMapKey`和 `genPrivateMapKeyWithStringRoomID`  | [GitHub](https://github.com/tencentyun/tls-sig-api-v2-cpp/blob/master/src/tls_sig_api_v2.cpp) |

[](id:step3)
### 步骤3：由您的服务端将 PrivateMapKey 下发给您的 App

![](https://main.qcloudimg.com/raw/108b2c9e60cf28c24c2a42f5f2ce0110.png)
如上图所示，当您的服务器计算好 PrivateMapKey 之后，就可以下发给您的 App，您的 App 可以通过两种方案将 PrivateMapKey 传递给 SDK：

#### 方案一：在 enterRoom 时传递给 SDK
如果想要控制用户进入房间的权限，您可以在调用 `TRTCCloud` 的 `enterRoom` 接口时，通过设置 [TRTCParams](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#interfaceTRTCParams) 中的 **privateMapKey** 参数即可实现。

这种进房时校验 PrivateMapKey 的方案比较简单，非常适合于在用户进入房间前就能将用户权限确认清楚的场景。

#### 方案二：通过实验性接口更新给 SDK
在直播场景中，往往都会有观众上麦变成主播的连麦场景。当观众变成主播时，TRTC 会再校验一次进房时在进房参数 `TRTCParams` 中携带的 PrivateMapKey，如果您将 PrivateMapKey 的有效期设置得比较短，例如“5分钟”，就会很容易触发校验失败进而导致用户被踢出房间。

要解决这个问题，除了可以延长有效期（例如将“5分钟”改成“6小时”），还可以在观众通过 `switchRole` 将自己的身份切换成主播之前，重新向您的服务器申请一个 privateMapKey，并调用 SDK 的实验性接口 `updatePrivateMapKey` 将其更新到 SDK 中，示例代码如下：
[](id:example_code)
<dx-codeblock>
::: Android java
JSONObject jsonObject = new JSONObject();
try {
    jsonObject.put("api", "updatePrivateMapKey");
    JSONObject params = new JSONObject();
    params.put("privateMapKey", "xxxxx"); // 填写新的 privateMapKey
    jsonObject.put("params", params);
    mTRTCCloud.callExperimentalAPI(jsonObject.toString());
} catch (JSONException e) {
    e.printStackTrace();
}
:::
::: iOS ObjectiveC
NSMutableDictionary *params = [[NSMutableDictionary alloc] init];
[params setObject:@"xxxxx" forKey:@"privateMapKey"]; // 填写新的 privateMapKey
NSDictionary *dic = @{@"api": @"updatePrivateMapKey", @"params": params};
NSData *jsonData = [NSJSONSerialization dataWithJSONObject:dic options:0 error:NULL];
NSString *jsonStr = [[NSString alloc] initWithData:jsonData encoding:NSUTF8StringEncoding];
[WXTRTCCloud sharedInstance] callExperimentalAPI:jsonStr];
:::
::: C++ C++
std::string api = "{\"api\":\"updatePrivateMapKey\",\"params\":{\"privateMapKey\":"xxxxx"}}";
TRTCCloudCore::GetInstance()->getTRTCCloud()->callExperimentalAPI(api.c_str());
:::
::: C# C#
std::string api = "{\"api\":\"updatePrivateMapKey\",\"params\":{\"privateMapKey\":"xxxxx"}}";       
mTRTCCloud.callExperimentalAPI(api);
:::
</dx-codeblock>

## 常见问题
[](id:q1)
#### 1. 线上的房间为什么都进不去了？

房间权限控制一旦开启后，当前 SDKAppid 下的房间就需要在 `TRTCParams` 中设置 privateMapKey 才能进入，所以如果您线上业务正在运营中，并且线上版本并没有加入 privateMapKey 的相关逻辑，请不要开启此开关。

[](id:q2)
#### 2. PrivateMapKey 和 UserSig 有什么区别？

- UserSig 是 TRTCParams 的必选项，作用是检查当前用户是否有权使用 TRTC 云服务，用于防止攻击者盗用您的 SDKAppid 账号内的流量。
- PrivateMapKey 是 TRTCParams 的非必选项，作用是检查当前用户是否有权进入指定 roomid 的房间，以及该用户在该房间所能具备的权限，当您的业务需要对用户进行身份区分的时候才有必要开启。
