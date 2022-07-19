QUIC（Quick UDP Internet Connection）是谷歌公司研发的基于 UDP 协议的下一代高质量传输协议，自2018年开始，IETF 将 QUIC 协议确定为 HTTP/3.0 网络协议规范进行推广，QUIC 协议相对于 TCP 协议，更适合弱网络和高丢包场景下的数据传输。

当前腾讯视频云支持使用 QUIC 协议来进行 [直播推流](#push) 和 [直播拉流](#play)。

## 协议版本支持
当前云直播支持 IEFT QUIC 和 Google QUIC，支持的版本分别为：
- IEFT QUIC 版本：h3-27、h3-29。
- Google QUIC 版本：Q39、Q43、Q46。

## 注意事项
若需使用 QUIC 拉流功能，请 [提工单](https://console.cloud.tencent.com/workorder/category) 给腾讯云开通对应拉流域名的 QUIC 协议拉流能力。

[](id:push)
## 直播推流
[](id:push_in)
### 接入方法
1. 直播推流支持 RTMP over QUIC 协议，需使用 UDP 1935 进行推流。推流地址同 RTMP over TCP 协议一致，可以在云直播控制台的 **[地址生成器](https://console.cloud.tencent.com/live/addrgenerator/addrgenerator)** 中 [生成推流地址](https://cloud.tencent.com/document/product/267/35257#push)。
![](https://qcloudimg.tencent-cloud.cn/raw/156bc4c6c55d7ccd101cd4df1c97e0ca.png)
2. 推流接入方式有两种：
	- **使用腾讯云 [腾讯云视立方·直播 SDK](https://cloud.tencent.com/document/product/454/7873)**：使用方式同 RTMP over TCP 方式一样，SDK 会默认使用 QUIC 协议接入腾讯云。
	- **使用自己的 QUIC 协议客户端**：可直接通过标准直播生成的推流地址，发起 QUIC 协议推流，RTMP over QUIC 的推流地址和 RTMP over TCP 的推流地址是一样的，QUIC 协议推流会直接接入腾讯云的 QUIC 接流服务器。

[](id:pushtest)
### 推流测试
您可以使用腾讯云 [腾讯云视立方·直播 SDK 小程序 Demo](https://cloud.tencent.com/document/product/454/6555#.E5.B0.8F.E7.A8.8B.E5.BA.8F-demo)。
1. 打开手机微信搜索小程序 [腾讯视频云](https://cloud.tencent.com/document/product/454/6555#.E5.B0.8F.E7.A8.8B.E5.BA.8F-demo) 或扫描二维码，进入腾讯视频云微信小程序。
2. 选择下方的 **通讯** 页签，并选择 **RTMP 推流**，进入推流设置界面。
3. 手动输入或单击 **扫码读取** 扫码录入您已生成的 [推流地址](#push)。
4. 单击 **开始** 会默认使用 RTMP over QUIC  进行推流。
![](https://main.qcloudimg.com/raw/a4adf24a47553c6ee6694c094b5fef07.png)

[](id:play)
## 直播拉流
[](id:play_in)
### 拉流接入
直播拉流支持 HTTP over QUIC 协议，需使用 UDP 443 端口进行拉流。拉流地址同 HTTPS FLV 协议地址一样，也可以使用云直播控制台的 **[地址生成器](https://console.cloud.tencent.com/live/addrgenerator/addrgenerator)** 工具 [生成拉流地址](https://cloud.tencent.com/document/product/267/35257#play)。
![](https://qcloudimg.tencent-cloud.cn/raw/c75ec072b4360577b82171cc9a5c2c71.png)

### 拉流测试[](id:playtest)
您可以使用腾讯云 [TCPlayer](https://tcplayer.vcube.tencent.com) 工具进行检验，具体步骤如下所述：
> ? Chrome 浏览器支持 QUIC 协议请求，用 Chrome 浏览器结合腾讯云 TCPlayer  可以验证播放是否已使用 QUIC 协议播放。

1. 打开 Chrome 浏览器。 Chrome 浏览器目前默认使用 IEFT QUIC版本，如果要验证 Google QUIC 版本，需使用命令行工具指定 `quic-version` 打开： 打开命令行工具，进入 Chrome 安装目录，执行 `chrome --enable-quic --quic-version=QUIC_VERSION_43`。
2. 打开 Chrome 的 QUIC 开关。 在 Chrome 浏览器地址栏输入 `chrome://flags/#enable-quic`，将开关设置成 Enabled，并重启 Chrome 浏览器。
 ![](https://main.qcloudimg.com/raw/b5aee3532ef918518206b607cc2d8f53.png)
3. 打开 TCPlayer ，在URL播放地址中输入 **HTTPS** 的 FLV 播放地址。单击 **预览**，开始播放。
![](https://qcloudimg.tencent-cloud.cn/raw/26af4045fd0fadfdf9523c97264bcc06.png)
4. 在 Chrome 的开发者工具中，选择 **Network** 标签页，可以看到请求的 protocol 是已经是 QUIC 协议，根据 QUIC 的版本不同，可能显示 `http/2+quic/43` 或 `h3-29`等。
![](https://qcloudimg.tencent-cloud.cn/raw/ad09072fb3b1a930f158ba65be054df8.png)

> ?  如果 Protocol 字段默认不显示，可以在显示处单击右键勾选 Protocal 即可显示。
> ![](https://main.qcloudimg.com/raw/ee21e41e7f61e87dccb2f2509ff7678d.png)
