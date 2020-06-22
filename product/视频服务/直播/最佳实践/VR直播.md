目前腾讯云标准直播、云点播已全面适配 VR 全景视频源。您通过全景硬件设备采集视频后，可直接经过标准直播、云点播进行正常下行分发。本文将以“Insta360 pro2”相机为例介绍如何基于 VR 全景相机通过标准直播完成 VR 直播。

<span id="keyword"></span>
## 关键词说明
<table>
<thead><tr><th width="24%">关键词</th><th>描述</th></tr></thead>
<tbody><tr>
<td>360°全景拍摄</td>
<td>360°全方位无死角记录周围环境。</td>
</tr><tr>
<td>360°3D全景拍摄</td>
<td>立体呈现周围环境，带给观看者沉浸式体验。</td>
</tr><tr>
<td>RTMP</td>
<td>是 Adobe Systems 公司为 Flash 播放器和服务器之间音频、视频和数据传输开发的开放协议。目前标准直播支持 RTMP 协议进行推流拉流播放。</td>
</tr><tr>
<td>直播同时保存画面视频</td>
<td>保存当前直播输出视频到本地 SD 卡中。</td></tr>
<tr>
<td>保存6镜头原片</td>
<td>使用 Pro 2 机内拼接推流4K 2D直播时，支持存储直播视频流或单镜头高分辨率原片后期拼接8K 2D。机内拼接推流4K 3D直播时，支持存储直播视频流或单镜头高分辨率原片后期拼接6K 3D。</td>
</tr>
</tbody></table>


## 准备工作 
1. 开通腾讯云直播服务。
2. 已添加推流域名和播放域名，具体操作请参见 [添加自有域名](https://cloud.tencent.com/document/product/267/20381)。
3. 一台已经连接好的“Insta360 Pro 2”相机，具体连接操作步骤可参见 [Insta360 Pro2 说明书](https://onlinemanual.insta360.com/pro2/zh-cn/live/prepare/3)。
4.  通过[【Insta360 官网】](http://insta360.com/download/insta360-pro2?locale=zh-cn)下载 Android/iOS 手机端、Windows 端 或 Mac 端的相机控制软件。
 ![](https://main.qcloudimg.com/raw/d36bcf1b1f00c2b85889ef04f538530e.png)
5. 软件下载完成之后需要对相机进行调试，调试方法参见 [基础拍摄准备-相机调试](https://onlinemanual.insta360.com/pro2/zh-cn/basic/prepare/adjustment)。



## VR 相机推流设置
<span id="step1"> </span> 
1. 进入云直播控制台的【地址生成器】生成推流地址，具体操作请参见 [生成推流域名](https://cloud.tencent.com/document/product/267/35257#push)。
2. 打开软件之后，选择界面上的直播按钮，然后通过右上方基础设置开始设置相机参数。
![](https://main.qcloudimg.com/raw/a033e0d3a5bbaf91566834075c116954.png)
<table>
<thead><tr><th width="41%">基础设置项</th><th width="10%">必填配置项</th><th>配置说明</th></tr></thead>
<tbody><tr>
<td rowspan="10"><img src="https://main.qcloudimg.com/raw/67c21ebf51485dc1ad8854ea85bbedef.png" alt=""></td>
<td>模式</td><td>选择模式类型为『自定义 RTMP 服务器』。</td>
</tr><tr>
<td>拍摄类型</td><td>根据需求选择 <a href="#keyword">360°全景拍摄</a> 或 <a href="#keyword">3D全景拍摄</a>。</td>
</tr><tr>
<td>直播协议</td><td>请选择直播协议为『RTMP』 。</td>
</tr><tr>
<td>分辨率</td><td>根据个人所需选择分辨率。若设定中没有您所需分辨率，勾选右侧的【自定义】按钮，自定义设置。<br><b>注意：</b>4K 2D或3D的分辨率不能大于3840 * 3840。</td>
</tr><tr>
<td>帧率</td><td>默认帧率值为：30fps。若您的分辨率设置为自定义，可同时自定义帧率取值。</td>
</tr><tr>
<td>码率</td><td>自定义直播码率，在手机端观看的情况下推荐码率调整为4Mbps。
			<br><b>说明：</b>造成卡顿原因很多情况下是因为上传带宽不够。如果手机端画面卡顿，请先排除是否因为手机卡顿引起该情况。若不是，请选择更低的码率。</td>
</tr><tr>
<td>推流地址</td><td>填入<a href="#step1">步骤1</a> 所得推流地址的前部分，格式为：<code>rtmp://domain/AppName/</code>。</td>
</tr><tr>
<td>流密钥</td><td>填入<a href="#step1">步骤1</a> 所得推流地址的后部分，格式为：<code>StreamName?txSecret=xxxxx&txTime=5C1E5F7F</code>。</td>
</tr><tr>
<td><a href="#keyword">直播同时保存视频画面</a></td><td>根据个人需求勾选，是否边播边保存相关数据到机身 SD 卡中。</td>
</tr><tr>
<td><a href="#keyword">保存6镜头原片</a></td><td>根据个人需求勾选，是否边播边保存相关数据到机身 SD 卡中。</td>
</tr>
</tbody></table>

8.完成以上设置后即可单击红色的【Live】按键开始推流。
9.当【LIve】按钮变成白色就说明推流成功，即可将视频流推送到设置的推流地址中。
![](https://main.qcloudimg.com/raw/e5efed214c114b51004aa798c89282c0.png)


>? 若您需要进行更多设置，可参考 [Insta360 相机拍摄进阶说明](https://onlinemanual.insta360.com/pro2/zh-cn/live/production/1)。

## 直播播放
1. 通过云直播控制台的【地址生成器】生成对应流的播放地址，具体操作请参见 [生成播放域名](https://cloud.tencent.com/document/product/267/35257#play)。
>?播放地址 StreamName要与推流地址 StreamName 一致才能播放对应的流。
2. 通过[【Insta360 官网】](https://www.insta360.com/download/insta360-one)下载 Android/iOS 手机端、Windows 端 或 Mac 端的全景视频播放器软件。
![](https://main.qcloudimg.com/raw/a63a315890bb83f4cab383656a3c72a9.png)
3. 进入【Insta360 Player】界面，选择【文件】>【播放流媒体】。
![](https://main.qcloudimg.com/raw/d6faa10c3236315ca585d320e8f461ea.png)
4. 填写【播放地址】，单击【观看】开始播放。如播放地址可正常拉流，则会直接播放。
![](https://main.qcloudimg.com/raw/457e6bfae36185ca47d5511058d3b67c.png)


## VR 设备参考建议
| 设备                | 下载地址                                                     |
| ------------------- | ------------------------------------------------------------ |
| Insta360 pro2       | [云市场链接](https://market.cloud.tencent.com/products/20303) |
| Insta360 影石 Titan | [云市场链接](https://market.cloud.tencent.com/products/20302) |
| Insta360 影石       | [云市场链接](https://market.cloud.tencent.com/products/20148) |
| 圆周率              | [云市场链接](https://market.cloud.tencent.com/products/15866 ) |




