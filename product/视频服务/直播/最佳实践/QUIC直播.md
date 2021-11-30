QUIC（Quick UDP Internet Connection）是谷歌公司研发的基于 UDP 协议的下一代高质量传输协议，自2018年开始，IETF 将 QUIC 协议确定为 HTTP/3.0 网络协议规范进行推广，QUIC 协议相对于 TCP 协议，更适合弱网络和高丢包场景下的数据传输。

当前腾讯视频云支持使用 QUIC 协议来进行 [直播推流](#push) 和 [直播拉流](#play)。

## 协议版本支持

当前云直播支持的 QUIC 协议版本：39、43、46。

> ! 推荐使用 43 版本。

## 注意事项

若需使用 QUIC 拉流功能，请 [提工单](https://console.cloud.tencent.com/workorder/category) 给腾讯云开通对应拉流域名的 QUIC 协议拉流能力。


## 直播推流

[](id:push)

### 接入方法
直播推流支持 RTMP over QUIC 协议，需使用 UDP 1935 进行推流。推流地址同 RTMP over TCP 协议一致，可以在云直播控制台的【[地址生成器](https://console.cloud.tencent.com/live/addrgenerator/addrgenerator)】中 [生成推流地址](https://cloud.tencent.com/document/product/267/35257#push)。

![](https://main.qcloudimg.com/raw/31d20b09de1c8d3c9748872e59f9a828.png)


推流接入方式有两种：

- **使用腾讯云 [移动直播 SDK](https://cloud.tencent.com/document/product/454/7873)**：使用方式同 RTMP over TCP 方式一样，SDK 会默认使用 QUIC 协议接入腾讯云。
- **使用自己的 QUIC 协议客户端**：可直接通过标准直播生成的推流地址，发起 QUIC 协议推流，RTMP over QUIC 的推流地址和 RTMP over TCP 的推流地址是一样的，QUIC 协议推流会直接接入腾讯云的 QUIC 接流服务器。

[](id:pushtest)

### 推流测试

您可以使用腾讯云 [移动直播小程序 DEMO](https://cloud.tencent.com/document/product/454/6555#.E5.B0.8F.E7.A8.8B.E5.BA.8F-demo)。

1. 打开手机微信搜索小程序 [腾讯视频云](https://cloud.tencent.com/document/product/454/6555#.E5.B0.8F.E7.A8.8B.E5.BA.8F-demo) 或扫描二维码，进入腾讯视频云微信小程序。
2. 选择【RTMP推流】，进入推流设置界面。
3. 手动输入或单击【扫码读取】扫码录入您已生成的 [推流地址](#push)。
4. 单击【开始】会默认使用 RTMP over QUIC  进行推流。
![](https://main.qcloudimg.com/raw/a4adf24a47553c6ee6694c094b5fef07.png)


## 直播拉流

[](id:play)

### 拉流接入

直播拉流支持 HTTP over QUIC 协议，需使用 UDP 443 端口进行拉流。拉流地址同 HTTP FLV 协议地址一样，也可以使用云直播控制台的【[地址生成器](https://console.cloud.tencent.com/live/addrgenerator/addrgenerator)】中 [生成拉流地址](https://cloud.tencent.com/document/product/267/35257#play)。
![](https://main.qcloudimg.com/raw/e4727db59f2e195abdd9382456212d14.png)

[](id:playtest)

### 拉流测试

您可以使用腾讯云 [TCPlayerDemo](https://imgcache.qq.com/open/qcloud/video/vcplayer/demo/tcplayer-test.html) 工具进行检验，具体步骤如下所述：
> ? Chrome 浏览器支持 QUIC 协议请求，用 Chrome 浏览器结合腾讯云 TCPlayerDemo 可以验证播放是否已使用 QUIC 协议播放。

1. 打开 Chrome 的 QUIC 开关。
   在 Chrome 浏览器地址栏输入 `chrome://flags/#enable-quic `，将开关设置成 Enabled，重启 Chrome 浏览器即可。
   ![](https://main.qcloudimg.com/raw/b5aee3532ef918518206b607cc2d8f53.png) 
2. 打开 TCPlayerDemo，填入 HTTPS 的播放地址时建议使用 FLV 和 HLS 的拉流地址，RTMP 的地址只支持 Flash 播放。单击生成连接后，单击![](https://main.qcloudimg.com/raw/5886ad8b68619d7ba99268e0a4e24f2c.png)开始播放。
![](https://main.qcloudimg.com/raw/a2e4d83ca259b97b4376875215015a22.png)
3. 在 Chrome 的开发者工具中，选择【Network】标签页，可以看到请求的 protocol 是已经是 `http/2+quic/46`。
![](https://main.qcloudimg.com/raw/e1e61b7ae544881b898ccd7aa116e8a4.png)

> ? 
> - 浏览器版本不同，QIUC 的版本号可能稍有不同。
> - 如果 Protocol 字段默认不显示，可以在显示处单击右键勾选 Protocal 即可显示。
> ![](https://main.qcloudimg.com/raw/ee21e41e7f61e87dccb2f2509ff7678d.png)
