腾讯视频云在流媒体传输上不断深入优化，以适应不同场景的需求，除了支持常见的 RTMP 推流协议外，目前已经支持 RTMPS 推流协议，主要适用于有加密需求的客户，尤其是有出海业务的客户。本文将主要介绍 RTMPS 推流的功能实现。

## 优势对比

常用标准 RTMP 推流协议的鉴权完全依赖 URL 增加相关参数，RTMP server 根据参数做验证，没有对传输的音视频数据包做加密，只要截取到 RTMP 包解析后就可以播放。

RTMPS 协议能够很好的解决 RTMP 安全问题。RTMPS 协议是经过 SSL 加密的 RMTP 协议，增强了数据通信的安全性，允许通过加密编码器和 CDN 之间的流来安全地进行流传输。

**各推流协议对比图：**

<table>
<tr>
<th>协议</th><th width="14%">协议类型</th><th>传输方式</th><th width="13%">延时</th><th>协议特点</th><th>应用场景</th><th>腾讯优化方案</th>
</tr><tr>
<td>RTMPS</td>
<td>流媒体协议</td>
<td>TCP</td>
<td>-</td>
<td>加密</td>
<td>加密场景</td>
<td>支持多域名多证书</td>
</tr><tr>
<td>SRT</td>
<td>流媒体协议</td>
<td>UDP</td>
<td>500ms-1s</td>
<td>低延时、抗丢包</td>
<td>OTT、跨区传输</td>
<td>-</td>
</tr><tr>
<td>WebRTC</td>
<td>流媒体协议</td>
<td>RTP</td>
<td>200ms-1s</td>
<td>低延时</td>
<td>音视频通话</td>
<td>优化秒开及卡顿快直播</td>
</tr><tr>
<td>QUIC</td>
<td>流媒体协议</td>
<td>UDP</td>
<td>-</td>
<td>抗丢包，0rtt</td>
<td>浏览器访问</td>
<td>优化首帧传输</td>
</tr></table>

 

## 注意事项

**使用 SSL 加密的 RTMPS 推流协议，需要推流域名配置证书，目前云直播默认推流域名已经配置了通用证书**。如果想使用自己的证书，必须更换端口。腾讯视频云多协议平台对 RTMPS 协议进行了优化，用户无需更换端口，可直接使用自己的证书，平台会自动根据域名去做适配，匹配到对应的证书。

> ? 
- 若您希望测试使用 RTMPS 推流，可以通过云直播默认推流域名进行接入。
- 若需要通过自有域名使用 RTMPS 推流，需要 [提交工单](https://console.cloud.tencent.com/workorder/category) 提供域名和对应的证书。

 
[](id:rtmp_push)
## RTMPS 推流

1. 生成推流地址，可通过以下两种方式进行：
   - 通过拼接规则自主拼接，详细操作请参见 [自主拼装直播 URL](https://cloud.tencent.com/document/product/267/32720#push)。
   - 进入云直播控制台的 **直播工具箱**>[**地址生成器**](https://console.cloud.tencent.com/live/addrgenerator/addrgenerator)，选择生成类型为**推流域名**，并按需填写推流地址信息，详细操作请参见 [地址生成器](https://cloud.tencent.com/document/product/267/35257#push)。
 ![](https://main.qcloudimg.com/raw/343726985cf941fdcdaa4bf03f94f23e.png)
2. 将生成的 RTMP 推流地址修改成 RTMPS 输入到 OBS 开始 RTMPS 推流，详细操作请参见 [OBS 推流](https://cloud.tencent.com/document/product/267/32726)。
![](https://main.qcloudimg.com/raw/5dc970602f53a9f5730649db70ecdc70.png)

 
[](id:rtmp_play)
## 直播拉流

按照正常拉流播放流程操作即可，具体请参见 [直播播放](https://cloud.tencent.com/document/product/267/32733)。

 

