移动直播中使用的 TIM 云通信组件和 MLVBLiveRoom 组件会用到 UserSig。UserSig 本质是一种签名，类似直播推流地址里的防盗链签名，但 UserSig 的计算方式相对复杂些。
本文主要介绍 UserSig 在移动直播服务中的作用以及计算方法。

<span id="UserSig"></span>
## UserSig 介绍

UserSig 是腾讯云 MLVBLiveRoom 组件和云通信 TIMSDK 会用到的一种“签名”，计算方法是对 SDKAppID、UserID 和过期时间进行非对称签名，签名算法为 ECDSA，下图展示了 UserSig 的原理。
![](https://main.qcloudimg.com/raw/dd87ed980127527e5b4b8023aa7170a7.png)

1. 您的 App 在使用 MLVBLiveRoom 组件（该组件内部会使用 TIM 云通信服务）之前，首先要向您的服务器请求 UserSig。
2. 您的服务器根据（SDKAppID + UserID）计算 UserSig，计算方法和源代码请参考 [生成 UserSig](#Generate)。
3. 服务器将计算好的 UserSig 返回给您的 App。
4. 您的 App 将获得的 UserSig 通过接口函数（MLVBLiveRoom#login）传递给 MLVBLiveRoom 组件。
5. MLVBLiveRoom 将（SDKAppID + UserID + UserSig）提交给腾讯云服务器进行校验。
6. 腾讯云校验 UserSig，确认合法性。
7. 校验通过后，会向 MLVBLiveRoom 提供其所需的音视频、连麦和云通信服务。

<span id="PrivateKey"></span>
## 下载签名私钥（PrivateKey）

1. 登录【直播控制台】>【直播SDK】>【[应用管理](https://console.cloud.tencent.com/live/license/appmanage)】页面。
  >?如果您还没有应用，请先创建应用，然后执行 [步骤2](#step2)。
<span id="step2"></span>
2. 单击目标应用所在行的【管理】，进入【应用管理】页面。
![](https://main.qcloudimg.com/raw/ae78e63cf40bfc16cd59cf08f6299c7c.png)
3. 单击【下载公私钥】，保存 `authkeys.txt` 文件。
文本中 `-----BEGIN PRIVATE KEY-----` 开始的内容即为**私钥**，私钥可以配合 SHA256withECDSA 算法计算出合法的 UserSig。
![](https://main.qcloudimg.com/raw/398091b0beb19a9e13c0b6d9af518c08.png)

<span id="Generate"></span>
## 生成 UserSig

UserSig 的计算过程就是对 SDKAppID、UserID、过期时间等几个关键值进行非对称签名。我们准备了各个平台的示例代码，您可以直接下载后集成到您的服务器上。

| 语言版本 | 关键函数 | 下载链接 |
|:---------:|:---------:|:---------:|
| Java | `genSig` | [Github](https://github.com/tencentyun/tls-sig-api-java)|
| GO | `genSig` | [Github](https://github.com/tencentyun/tls-sig-api-golang)|
| PHP | `genSig` | [Github](https://github.com/tencentyun/tls-sig-api-php)|
| Node.js | `genSig` | [Github](https://github.com/tencentyun/tls-sig-api-node)|
| C++ | `gen_sig` | [Github](https://github.com/tencentyun/tls-sig-api)|
| C# | `genSig` | [Github](https://github.com/tencentyun/tls-sig-api-cs)|
| Python | `gen_sig` | [Github](https://github.com/tencentyun/tls-sig-api-python)|

>!您也可以在客户端计算 UserSig，但在客户端计算 UserSig 意味着要在客户端的代码里写明 PrivateKey，很容易引起 PrivateKey 泄露。
>为了您的账号安全，建议将 UserSig 计算代码放在您的服务器上，降低客户端被破解导致 PrivateKey 泄露的风险。

