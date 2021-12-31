腾讯云视立方播放器 Player （以下简称播放器 Player）支持 Web、iOS、Android 和 Flutter 四大终端，云点播为客户提供了完整的 Demo 和播放器 Player 下载。
[](id:downloadSDK)
## SDK 下载 & Demo 
<table>
   <tr>
      <th width="120px" style="text-align:center">终端类别</td>
      <th width="70px" style="text-align:center">播放器类型</td>
      <th width="0px"  style="text-align:center">SDK & Demo 下载地址</td>
      <th width="0px" style="text-align:center">Demo 展示</td>
      <th width="0px"  style="text-align:center">	使用文档</td>
   </tr>
   <tr>
      <td style="text-align:center" rowspan='2'>Web 端</td>
      <td>超级播放器</td>
      <td><a href="https://cloud.tencent.com/document/product/266/58804#preparation">SDK</a></td>
      <td><a href="https://imgcache.qq.com/open/qcloud/video/tcplayer/examples/vod/tcplayer-vod-base.html">Demo</a></td>
      <td><a href="https://cloud.tencent.com/document/product/266/58804">Web - 超级播放器</a></td>
   </tr>
   <tr>
      <td>超级播放器 Adapter</td>
      <td><a href="https://cloud.tencent.com/document/product/266/58773#Integrated">SDK</a></td>
      <td>-</td>
      <td><a href="https://cloud.tencent.com/document/product/266/58773">Web - 超级播放器 Adapter</a></td>
   </tr>
   <tr>
      <td style="text-align:center" rowspan='2'>iOS 端</td>
      <td>超级播放器</td>
      <td><a href="https://github.com/tencentyun/SuperPlayer_iOS">SDK + Demo</a></td>
      <td><a><button style="width:120px;height: 120px;border:none;background-image:url(https://main.qcloudimg.com/raw/12c7da97cc910eda673cb19b66fc7cb3.png);background-size: cover;">
</button></a></td>
      <td><a href="https://cloud.tencent.com/document/product/266/58774">iOS - 超级播放器</a></td>
   </tr>
   <tr>
      <td>超级播放器 Adapter</td>
      <td><a href="https://mediacloud-76607.gzc.vod.tencent-cloud.com/TXCPlayerAdapter/Release/1.0.0/TXCPlayerAdapterSDK_1.0.0_iOS.zip">SDK</a></td>
      <td>-</td>
      <td><a href="https://cloud.tencent.com/document/product/266/58775">iOS - 超级播放器 Adapter</a></td>
   </tr>
   <tr>
      <td style="text-align:center" rowspan='2'>Android 端</td>
      <td>超级播放器</td>
      <td><a href="https://github.com/tencentyun/SuperPlayer_Android">SDK + Demo</a></td>
      <td><a><button style="width:120px;height: 120px;border:none;background-image:url(https://main.qcloudimg.com/raw/6790ddaf4ffe4afd0ceb96b309a16496.png);background-size: cover;">
</button></a></td>
      <td><a href="https://cloud.tencent.com/document/product/266/7938">Android - 超级播放器</a></td>
   </tr>
   <tr>
      <td>超级播放器 Adapter</td>
      <td><a href="https://mediacloud-76607.gzc.vod.tencent-cloud.com/TXCPlayerAdapter/Release/1.0.0/TXCPlayerAdapterSDK_1.0.0_Android.zip">SDK</a></td>
      <td>-</td>
      <td><a href="https://cloud.tencent.com/document/product/266/58777">Android- 超级播放器 Adapter</a></td>
   </tr>
   <tr>
      <td  style="text-align:center">Flutter 端</td>
      <td>超级播放器</td>
      <td><a href="https://github.com/tencentyun/SuperPlayer/tree/main/Flutter">SDK + Demo</a></td>
	     <td><a href="https://github.com/tencentyun/SuperPlayer/tree/main/Flutter">Demo</a></td>
	     <td><a href="https://cloud.tencent.com/document/product/266/58778">Flutter - 超级播放器</a></td>
   </tr>
</table>

## 功能列表
[](id:functionList)
超级播放器在各端上都提供丰富的能力接入，各平台支持的能力列表展示如下：

| 功能点         | 功能说明                                               | iOS & Android |
| ----------- | -------------------------------------------------- | ------------- |
| 多种格式        | 支持 RTMP、FLV、HLS、MP4、WebRTC 等丰富的音视频格式              | ✓             |
| URL 播放      | 支持网络视频的 URL 方式播放                                   | ✓             |
| DASH 协议     | 支持标准协议的 DASH 格式视频                                  | ×             |
| FileID 播放   | 支持使用云点播的 FileID 方式播放                               | ✓             |
| 首屏秒开预加载     | 支持视频内容预加载，视频首屏可达到秒开                                | ✓             |
| 快速 seek     | 支持精准快速的 seek 到指定位置播放                               | ✓             |
| H.265 硬解    | 支持对 H.265 硬解码播放                                    | ✓             |
| 软硬解自动切换     | 当终端不支持硬件解码时自动切换到软解                                 | ✓             |
| 自适应码流       | 播放 HLS 自适应码流时，支持手动指定或根据网络带宽自动选择清晰度流进行播放            | ✓             |
| 清晰度切换       | 支持用户流畅无卡顿的切换多路清晰度流                                 | ✓             |
| 清晰度命名       | 支持为不同清晰度流进行自定义命名                                   | ✓             |
| 播放控制        | 支持开始、结束、暂停、自动播放、循环播放、断点续播、重播等播放控制功能                | ✓             |
| 倍速播放        | 支持0.5倍 - 2倍的视频变速播放，可保证音频变速不变调                      | ✓             |
| 自定义启播时间     | 支持自定义视频开启播放的时间                                     | ✓             |
| 试看功能        | 支持播放开启试看功能的视频                                      | ✓             |
| 进度条操作       | 拖拽进度条切换进度                                          | ✓             |
| 进度条标记及缩略图预览 | 支持在进度条上添加标记信息，并支持缩略图（雪碧图）预览                        | ✓             |
| 播放器尺寸       | 支持自定义设置播放器尺寸                                       | ✓             |
| 屏幕填充适应      | 支持为视频画面选择不同填充模式，适应屏幕大小                             | ✓             |
| 小窗播放        | 支持切换到小窗播放                                          | ✓             |
| 视频镜像        | 支持水平、垂直等方向的镜像                                      | ✓             |
| 视频旋转        | 支持对视频画面按角度旋转，同时支持根据视频文件内部 rotate 参数自动旋转视频            | ✓             |
| 亮度调节        | 支持播放视频时调节系统亮度                                      | ✓             |
| 音量调节        | 支持播放视频时调节系统音量和静音操作                                 | ✓             |
| 双声道音频       | 支持播放双声道音频                                          | ✓             |
| 锁定屏幕        | 支持锁屏功能，包含锁定旋转和隐藏界面元素                               | ✓             |
| 弹幕          | 支持在视频上方展示弹幕                                        | ✓             |
| 图片贴片        | 支持暂停时，增加图片贴片用于广告展示                                 | ✓             |
| 视频截图        | 支持截取播放画面的任意一帧                                      | ✓             |
| 字幕导入        | 支持导入自定义字幕文件                                        | ✓             |
| 设置封面        | 支持设置播放视频的封面                                        | ✓             |
| 多实例         | 支持在一个界面添加多个播放器同时播放                                 | ✓             |
| 边下边播        | 支持视频播放的同时缓存下载后面的内容                                 | ✓             |
| Referer 防盗链 | 支持通过播放请求中携带的 Referer 字段识别请求的来源，以黑名单或白名单方式对来源请求进行控制 | ✓             |
| Key 防盗链     | 支持在播放链接中加入控制参数，控制链接的有效时间、试看时长、允许播放的 IP 数等          | ✓             |
| HLS 加密      | 支持基于 HLS 提供的 AES encryption 方案，使用密钥对视频数据加密。        | ✓             |
| 私有协议加密      | 支持在云端通过私有协议对视频进行加密，且仅能通过播放器 SDK 对加密后的视频进行解密播放。       | ✓             |
| 离线下载        | 支持离线下载加密视频后，仅可通过播放器 SDK 对视频进行解密播放。                   | ✓             |
| 播放回调        | 支持对播放状态回调、首帧回调、播放完成或失败回调                           | ✓             |
| 支持 HTTPS    | 支持播放 HTTPS 的视频资源                                   | ✓             |
| 自定义 HTTP 头部 | 请求视频资源时，自定义 HTTP Headers 内容                        | ✓             |

>?表中“-”表示该端无需具备相应功能或不存在相关概念。
