如果您发现直播无法观看，是不是感觉非常的无奈？是不是觉得腾讯云就是个**黑盒子**，完全搞不懂里面出了什么情况？
不着急，按照下面的思路进行排查，一般都能在几十秒内确认问题原因：

![](//mc.qcloudimg.com/static/img/29c74afc399429e40a21b28e7abe87d9/image.png)

## step 1. 检查播放URL
对，在所有检查开始之前，您务必要先检查一下地址是否正确，因为这里出错概率最高，腾讯云的直播地址分推流地址和播放地址两种，我们要首先排除 <font color='red'>**误拿推流地址来播放**</font> 的错误。
![diff](//mccdn.qcloud.com/static/img/1d093770d4b9bfaec5e15b01bdb65d00/image.png)

>**小直播的播放URL**
>
>小直播的播放 URL 可以用调试的办法获取，您可以全局搜索代码寻找关键字 **startPlay**，然后在此处打下调试断点，这里是小直播对 RTMP SDK 的调用点，startPlay 的参数即为播放URL。

## step 2. 检查视频流
播放 URL 正确不代表视频就能播放，所以要检查视频流是否正常：
- 对于**直播**，如果主播已经结束推流，直播URL就不能观看了。
- 对于**点播**，如果云端的视频文件已经被移除，同样也是不能观看。

常用的解决办法就是用 VLC 检查一下，VLC 是PC上的一款开源播放器，支持的协议很多，所以最适合用来做检查：
![](//mc.qcloudimg.com/static/img/7923a14be5525bd37719c18d54243403/image.png)

## step 3. 检查播放端
如果视频流非常健康，我们就要分情况检查一下播放器是否OK：

### 3.1 Web浏览器（A）
- **格式支持**：手机浏览器 **<font color='red'>只支持</font> HLS（m3u8）和 MP4** 格式的播放地址。

- **HLS（m3u8）**：腾讯云 HLS 协议是懒启动的，简言之，只有当有观众请求 HLS 格式的观看地址后，腾讯云才会启动 HLS 格式的转码，这种懒启动策略的目的是规避资源浪费。但也就产生一个问题：**HLS 格式的播放地址要在全球首个用户发起请求后30 秒才能观看**。

- [**腾讯云Web播放器：**](https://cloud.tencent.com/document/product/454/7503) 支持同时指定多种协议的播放地址，能够根据所在的平台 （PC? Android? iOS?）采用最佳的播放策略。同时，内部的选择性重试逻辑也能针对性解决 HLS(m3u8) 懒启动的问题。

### 3.2 RTMP SDK（B）
如果 [RTMP SDK DEMO](https://cloud.tencent.com/document/product/454/6555) 本身播放没有问题，推荐你参考RTMP SDK 的播放文档（[iOS](https://cloud.tencent.com/document/product/454/7880) & [Android](https://cloud.tencent.com/document/product/454/7886)）检查一下对接逻辑是否错误？

## step 4. 防火墙拦截（C）
这是常见的一种情况，不少客户的公司网络环境会限制视频播放，限制的原理是由防火墙侦测http请求的是否是流媒体资源（公司老板都不希望员工上班看视频吗）。
 
如果您使用 4G 进行直播观看没有问题，而是用公司的Wi-Fi网络无法观看，即说明公司的网络策略有所限制，您可以尝试跟网管沟通，让TA给您的IP做一下特殊处理。

## step 5. 检查推流端（D）
如果是直播 URL 根本不能播放，而且没有 Step4 中防火墙限制的可能，那么很大概率是推流不成功，可以到 [为何推流不成功](https://cloud.tencent.com/document/product/454/7951) 继续问题的排查。


