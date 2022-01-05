[](id:UserSig)
## 什么是 UserSig？

UserSig 是腾讯云设计的一种安全保护签名，目的是为了阻止恶意攻击者盗用您的云服务使用权。
目前，腾讯云的实时音视频（TRTC）、即时通信（IM）以及移动直播（MLVB）等服务都采用了该套安全保护机制。要使用这些服务，您需要在相应 SDK 的初始化或登录函数中提供 SDKAppID，UserID 和 UserSig 三个关键信息。
其中 SDKAppID 用于标识您的应用，UserID 用于标识您的用户，而 UserSig 则是基于前两者计算出的安全签名，它由 **HMAC SHA256** 加密算法计算得出。只要攻击者不能伪造 UserSig，就无法盗用您的云服务流量。
UserSig 的计算原理如下图所示，其本质就是对 SDKAppID、UserID、ExpireTime 等关键信息进行了一次哈希加密：
```Cpp
//UserSig 计算公式，其中 secretkey 为计算 usersig 用的加密密钥

usersig = hmacsha256(secretkey, (userid + sdkappid + currtime + expire + 
                                 base64(userid + sdkappid + currtime + expire)))
```
>?
>- `currtime` 为当前系统的时间，`expire` 为签名过期的时间。
>- 上述原理图仅做 UserSig 计算原理说明，如需了解具体的 UserSig 拼接代码实现方式，请参见 [客户端计算 UserSig](#Client) 和 [服务端计算 UserSig](#Server)。

[](id:Key)
## 调试跑通阶段如何计算 UserSig？
如果您当前希望快速跑通 Demo，了解 TRTC SDK 相关能力，您可以通过 [客户端示例代码](#client) 和 [控制台](#console) 两种方法计算获取UserSig，具体请参考以下介绍。

>!
- 以上两种 UserSig 获取计算方案仅适用于调试，如果产品要正式上线，**不推荐**采用这种方案，因为客户端代码（尤其是 Web 端）中的 SECRETKEY 很容易被反编译逆向破解。一旦您的密钥泄露，攻击者就可以盗用您的腾讯云流量。
- 正确的做法是将 UserSig 的计算代码放在您的业务服务器上，然后由您的 App 在需要的时候向您的服务器获取实时算出的 UserSig。

[](id:client)
### 客户端示例代码计算 UserSig
1. **获取 SDKAPPID 和密钥**：
    1. 登录**实时音视频控制台** > **[应用管理](https://console.cloud.tencent.com/trtc/app)**。
    2. 单击您需查看的 SDKAppID 对应的**应用信息**，单击进入**快速上手**页签。
    3. 查看 **第二步 获取签发UserSig的密钥** 标签，即可获取用于计算 UserSig 的加密密钥。
    4. 单击**复制密钥**，可将密钥拷贝到剪贴板中。
![](https://main.qcloudimg.com/raw/e9b9cb9492fd350018c052364af89702.png)
>? 若查看密钥时只能获取公钥和私钥信息，请参见 [如何获取密钥](#getusersig)。
2. **计算 UserSig：**
为了方便客户端使用，我们提供各平台计算 UserSig 的源码文件，您可直接下载计算：
<table>
<thead><tr><th>适用平台</th><th>文件源码</th><th>文件相对路径</th></tr></thead>
<tbody><tr>
<td>iOS</td>
<td><a href="https://github.com/tencentyun/TRTCSDK/blob/master/iOS/TRTC-API-Example-OC/Debug/GenerateTestUserSig.h">Github</a></td>
<td>iOS/TRTC-API-Example-OC/Debug/GenerateTestUserSig.h</td>
</tr><tr>
<td>Mac</td>
<td><a href="https://github.com/tencentyun/TRTCSDK/blob/master/Mac/OCDemo/TRTCDemo/TRTC/GenerateTestUserSig.h">Github</a></td>
<td>Mac/OCDemo/TRTCDemo/TRTC/GenerateTestUserSig.h</td>
</tr><tr>
<td>Android</td>
<td><a href="https://github.com/tencentyun/TRTCSDK/blob/master/Android/TRTC-API-Example/Debug/src/main/java/com/tencent/trtc/debug/GenerateTestUserSig.java">Github</a></td>
<td>Android/TRTC-API-Example/Debug/src/main/java/com/tencent/trtc/debug/GenerateTestUserSig.java</td>
</tr><tr>
<td>Windows（C++）</td>
<td><a href="https://github.com/tencentyun/TRTCSDK/tree/master/Windows/DuilibDemo/GenerateTestUserSig.h">Github</a></td>
<td>Windows/DuilibDemo/GenerateTestUserSig.h</td>
</tr><tr>
<td>Windows（C#）</td>
<td><a href="https://github.com/tencentyun/TRTCSDK/tree/master/Windows/CSharpDemo/GenerateTestUserSig.cs">Github</a></td>
<td>Windows/CSharpDemo/GenerateTestUserSig.cs</td>
</tr><tr>
<td>Web</td>
<td><a href="https://github.com/tencentyun/TRTCSDK/blob/master/Web/base-js/js/debug/GenerateTestUserSig.js">Github</a></td>
<td>Web/base-js/js/debug/GenerateTestUserSig.js</td>
</tr><tr>
<td>微信小程序</td>
<td><a href="https://github.com/tencentyun/TRTCSDK/blob/master/WXMini/TRTCSimpleDemo/debug/GenerateTestUserSig.js">Github</a></td>
<td>WXMini/TRTCSimpleDemo/debug/GenerateTestUserSig.js</td>
</tr><tr>
<td>Flutter</td>
<td><a href="https://github.com/c1avie/trtc_demo/blob/master/lib/debug/GenerateTestUserSig.dart">Github</a></td>
<td>/lib/debug/GenerateTestUserSig.dart</td>
</tr>
</tbody></table>

我们在 TRTC SDK 的示例代码中提供了一个叫做 `GenerateTestUserSig` 的开源模块，您只需要将其中的 SDKAPPID、EXPIRETIME 和 SECRETKEY 三个成员变量修改成您自己的配置，就可以调用 `genTestUserSig()` 函数获取计算好的 UserSig，从而快速跑通 SDK 的相关功能：
![](https://qcloudimg.tencent-cloud.cn/raw/c09ab0330b7eff7e38ef60a0aa9cb03e.png)

[](id:getusersig)
#### 查看密钥时只能获取公钥和私钥信息，要如何获取密钥？
TRTC SDK 6.6 版本（2019年08月）开始启用新的签名算法 HMAC-SHA256。在此之前已创建的应用，需要先升级签名算法才能获取新的加密密钥。如不升级，您也可以继续使用 [老版本算法 ECDSA-SHA256](https://cloud.tencent.com/document/product/647/17275#Old)，如已升级，您按需切换为新老版本算法。

**升级/切换操作：**
1. 登录 [实时音视频控制台](https://console.cloud.tencent.com/trtc)。
2. 在左侧导航栏选择**应用管理**，单击目标应用所在行的**应用信息**。
3. 选择**快速上手**页签，单击**第二步 获取签发UserSig的密钥**区域的**点此升级**、**非对称式加密**或**HMAC-SHA256**。
  - 升级：
![](https://qcloudimg.tencent-cloud.cn/raw/03c0e6c5e5a9281ecfd3e37bd5434cbb.png)
  - 切换回老版本算法 ECDSA-SHA256：
![](https://qcloudimg.tencent-cloud.cn/raw/5c6eaff686a697d22a9ff5fc3ce513ad.png)
  - 切换为新版本算法 HMAC-SHA256：
![](https://qcloudimg.tencent-cloud.cn/raw/f2dae58eecc542686e034dbabb5334ff.png)


[](id:console)
### 控制台获取 UserSig
1. 登录**实时音视频控制台**，进入**开发辅助** > **[UserSig生成&校验](https://console.cloud.tencent.com/trtc/usersigtool)**。
2. 在签名（UserSig）生成工具下，选择对应的 SDKAppID 和 UserID。
3. 单击**生成签名(UserSig)**，即可计算得到对应的 UserSig。

<img src="https://qcloudimg.tencent-cloud.cn/raw/04d1da9b5465b66ff31d6307a71079b4.png" style="zoom:50%;" />


[](id:formal)
## 正式运行阶段如何计算 UserSig？

业务正式运行阶段，TRTC 提供安全等级更高的服务端计算 UserSig 的方案，可以最大限度地保障计算 UserSig 用的密钥不被泄露，因为攻破一台服务器的难度要高于逆向一款 App。具体的实现流程如下：

1. 您的 App 在调用 SDK 的初始化函数之前，首先要向您的服务器请求 UserSig。
2. 您的服务器根据 SDKAppID 和 UserID 计算 UserSig，计算源码见文档前半部分。
3. 服务器将计算好的 UserSig 返回给您的 App。
4. 您的 App 将获得的 UserSig 通过特定 API 传递给 SDK。
5. SDK 将 `SDKAppID + UserID + UserSig` 提交给腾讯云服务器进行校验。
6. 腾讯云校验 UserSig，确认合法性。
7. 校验通过后，会向 TRTCSDK 提供实时音视频服务。

![](https://main.qcloudimg.com/raw/60c419d6b977fa3cc158c57c8f3f7315.png)

为了简化您的实现过程，我们提供了多个语言版本的 UserSig 计算源代码（当前版本签名算法）：

| 语言版本 | 签名算法    | 关键函数 | 下载链接 |
| -------- | ----------- | ----------- | ----------- |
| Java     | HMAC-SHA256 | [genSig](https://github.com/tencentyun/tls-sig-api-v2-java/blob/master/src/main/java/com/tencentyun/TLSSigAPIv2.java) | [Github](https://github.com/tencentyun/tls-sig-api-v2-java)  |
| GO       | HMAC-SHA256 | [GenSig](https://github.com/tencentyun/tls-sig-api-v2-golang/blob/master/tencentyun/TLSSigAPI.go) | [Github](https://github.com/tencentyun/tls-sig-api-v2-golang) |
| PHP      | HMAC-SHA256 | [genSig](https://github.com/tencentyun/tls-sig-api-v2-php/blob/master/src/TLSSigAPIv2.php) |  [Github](https://github.com/tencentyun/tls-sig-api-v2-php)  |
| Node.js  | HMAC-SHA256 | [genSig](https://github.com/tencentyun/tls-sig-api-v2-node/blob/master/TLSSigAPIv2.js) | [Github](https://github.com/tencentyun/tls-sig-api-v2-node)  |
| Python   | HMAC-SHA256 | [genSig](https://github.com/tencentyun/tls-sig-api-v2-python/blob/master/TLSSigAPIv2.py) | [Github](https://github.com/tencentyun/tls-sig-api-v2-python) |
| C#       | HMAC-SHA256 | [GenSig](https://github.com/tencentyun/tls-sig-api-v2-cs/blob/master/tls-sig-api-v2-cs/TLSSigAPIv2.cs) |  [Github](https://github.com/tencentyun/tls-sig-api-v2-cs)   |

[](id:Old)
### 老版本签名算法 UserSig 计算源代码
为了简化签名计算难度，方便客户更快速地使用腾讯云服务，实时音视频自 2019-07-19 开始启用新的签名算法，从之前的 ECDSA-SHA256 升级为 HMAC-SHA256，也就是从 2019-07-19 之后创建的 SDKAppID 均会采用新的 HMAC-SHA256 算法。

如果您的 SDKAppID 是 2019-07-19 之前创建的，可以继续使用老版本的签名算法，算法的源码下载链接如下：

| 语言版本 |   签名算法   |                          下载链接                          |
| :------: | :----------: | :--------------------------------------------------------: |
|   Java   | ECDSA-SHA256 |  [Github](https://github.com/tencentyun/tls-sig-api-java)  |
|   C++    | ECDSA-SHA256 |    [Github](https://github.com/tencentyun/tls-sig-api)     |
|    GO    | ECDSA-SHA256 | [Github](https://github.com/tencentyun/tls-sig-api-golang) |
|   PHP    | ECDSA-SHA256 |  [Github](https://github.com/tencentyun/tls-sig-api-php)   |
|  Node.js  | ECDSA-SHA256 |  [Github](https://github.com/tencentyun/tls-sig-api-node)  |
|    C#    | ECDSA-SHA256 |   [Github](https://github.com/tencentyun/tls-sig-api-cs)   |
|  Python  | ECDSA-SHA256 | [Github](https://github.com/tencentyun/tls-sig-api-python) |
