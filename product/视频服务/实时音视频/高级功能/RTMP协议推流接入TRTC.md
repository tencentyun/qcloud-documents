
## 方案背景
为降低客户接入门槛，TRTC 支持 RTMP 标准协议推流，您可根据实际情况选择安装 [OBS](https://obsproject.com/download) 或 FFmpeg 进行推流。OBS 是一款好用的第三方开源程序直播流媒体内容制作软件，为用户提供免费使用，它可支持 OS X、Windows、Linux 操作系统，适用多种直播场景，满足大部分直播行为的操作需求，您可以到 [OBS 官网](https://obsproject.com/download?spm=a2c4g.11186623.2.15.6aac1445JPlKR8) 下载最新版本软件，使用 OBS 推流时无需安装插件。

本功能目前免费开放内测中（后续若收费会提前通知），但接入的 RTMP 流会作为房间中的虚拟用户产生正常的通话费用，详情参见 [计费概述](https://cloud.tencent.com/document/product/647/17157)。如果您需要申请使用此功能，请单击 [立即申请](https://cloud.tencent.com/apply/p/4mycyipdsp8)。

>! 不支持 RTMP 从 TRTC 拉流，如果需要旁路 CDN 直播观看，请参见 [实现 CDN 直播观看](https://cloud.tencent.com/document/product/647/16826)。

## 应用场景
<table>
<thead><tr><th width=22%>场景类型</th><th>说明</th></tr></thead>
<tbody><tr>
<td>在线教育场景</td>
<td>老师展示视频课件教学视频时，可以通过 PC 端 OBS 或者 FFmpeg 把绝大多数媒体格式以 RTMP 推流至 TRTC 房间，房间内的学生通过 TRTC SDK 拉流，可以保证观看到相同进度的教学视频，课件播放跳转进度、调整速度、切换下一章等全部可由老师控制，各学生端观看对齐课堂秩序好，教学质量更稳定。</td>
</tr><tr>
<td>一起看球赛场景</td>
<td>比赛流媒体是赛事供应方固定以 RTMP 格式流的方式提供赛事画面，通过 RTMP 协议推流至 TRTC 房间，实现 TRTC  房间内同步观看超低延时的比赛直播，配合 TRTC 的实时互动能力，与好友语音/视频讨论，一起喝彩加油，不会错过每一个精彩瞬间的共享体验。</td>
</tr><tr>
<td>更多场景</td>
<td>任何基于媒体流的实时互动体验玩法，均可通过 RTMP 协议推流帮您实现，等多玩法等待您的探索。</td>
</tr></tbody></table>


## OBS 推流设置
### 准备工作[](id:ready)
安装并打开 [OBS](https://obsproject.com/download?spm=a2c4g.11186623.2.15.6aac1445JPlKR8) 工具进行下述操作。

### 步骤1：选择输入源[](id:step1)
查看底部工具栏的**来源**标签，单击 **+** 按钮，根据您的业务需要选择输入源。常用来源输入有：

| 输入源         | 说明                                                         |
| :------------- | :----------------------------------------------------------- |
| 图像           | 适用于单张图像直播                                         |
| 图像幻灯片放映 | 可循环或者顺序多张播放图片                                 |
| 场景           | 实现各种强大的直播效果。此时，另一个场景是作为来源被添加进当前场景的，可以实现整个场景的插入 |
| 媒体源         | 可上传本地视频，并本地点播视频文件进行直播化处理           |
| 文本           | 实时添加文字在直播窗口中                                   |
| 窗口捕获       | 可根据您选择的窗口进行实时捕获，直播仅显示您当前窗口内容，其他窗口不会进行直播捕获 |
| 视频捕获设备   | 实时动态捕捉摄像设备，可将摄像后的画面进行直播             |
| 音频输入捕获   | 用于音频直播活动（音频输入设备）                           |
| 音频输出捕获   | 用于音频直播活动（音频输出设备）                           |


![](https://main.qcloudimg.com/raw/c59eff44ffd2ac4c785fe4e4e3bd79b8.png)


### 步骤2：设置推流参数[](id:step2)
1. 通过底部工具栏的 **控件>设置** 按钮进入设置界面。
![img](https://main.qcloudimg.com/raw/56e4c19f24d08df7b8f8815f1ffb6857.png)
2. 单击 **推流** 进入推流设置页签，选择服务类型为**自定义**。
3. 服务器填写：`rtmp://rtmp.rtc.qq.com/push/`。
4. 填写串流密钥格式如下：
```
房间号?sdkappid=应用&userid=用户名&usersig=签名
```
其中房间号、应用、用户名、签名需要换成业务的，例如：
```
22998?sdkappid=140*****66&userid=******rtmp2&usersig=eJw1jdE***************ZLgi5UAgOzoMhrayt*cjbmiCJ699T09juc833IMT94Ld7I0iHZqVDzvVAqkZsG-IKlzLiXOnEhswHu1iUyTc9pv*****D8MQwoA496Ke6U1ip4EAH4UMc5H9pSmv6MeTBWLamhwFnWRBZ8qKGRj8Yp-wVbv*mGMVZqS7w-mMDQL
```
	- 为简化参数，只支持字符串房间号，不超过64个字符，字符只能是数字、字母、下划线。TRTC 其他端如果要观看 RTMP 流，需要使用**字符串房间号进房**。
	- usersig 的生成规则，请参见 [UserSig 相关](https://cloud.tencent.com/document/product/647/17275) （**请注意签名要在有效期内**）。
	- 以上服务器地址 + 串流密钥组成 RTMP 推流地址，也可以供 FFmpeg 或其他 RTMP 库推流。
![](https://qcloudimg.tencent-cloud.cn/raw/bc4be526005a7ac4f81ec6badd507271.png)

### 步骤3：设置输出[](id:step3)
RTMP 后台不支持传输 B 帧，用户可以通过如下设置调整推流端软件的视频编码参数来去除 B 帧。
1. 在**设置**中单击**输出**页签进行配置。
2. 在**输出模式**中选择**高级**，**关键帧间隔建议填写1或2**，单击**确定**保存设置。

![](https://qcloudimg.tencent-cloud.cn/raw/6f331bf0f0299060470008acab20954a.png)  


### 步骤4：设置视频选项[](id:step4)
在**设置**中单击**视频**页签，设置分辨率和帧率。分辨率决定了观众看到的画面清晰程度，分辨率越高画面越清晰。FPS 是视频帧率，它控制观看视频的流畅，普通视频帧率有24帧 - 30帧，低于16帧画面看起来有卡顿感，而游戏对帧率要求比较高，一般小于30帧游戏会显得不连贯。
![](https://qcloudimg.tencent-cloud.cn/raw/a67ecbbdf5e44c9316604bef3a20ca05.png)


### 步骤5：设置高级选项[](id:step5)
- 建议不启用**串流延迟**以减少端到端延迟。
- 启动**自动重连**，建议设置**重试延迟**时长尽量短，网络抖动时如果连接断开可尽快重连上。
![](https://qcloudimg.tencent-cloud.cn/raw/f500c91d29963f7f772a084ccea2d930.png)


### 步骤6：单击推流[](id:step6)
1. 查看 OBS 底部工具栏的 **控件**，单击 **开始推流**。
![](https://qcloudimg.tencent-cloud.cn/raw/22953d87c6a7cbfa34b9e7639507be37.png)
2. 推流成功后，正常情况在界面底部会展示推流状态，TRTC 控制台仪表盘上有该用户进房记录。
![](https://qcloudimg.tencent-cloud.cn/raw/a4b27551f991d73539bb5d2f834a4d38.png)

### 步骤7：其他端观看[](id:step7)
如前面 [设置推流参数](#step2) 所说，TRTC 其他端进房需要使用字符串房间号，[Web 端](https://cloud.tencent.com/document/product/647/17021#.E8.B7.A8.E5.B9.B3.E5.8F.B0-demo) 观看 RTMP 流的效果如下所示：
![](https://qcloudimg.tencent-cloud.cn/raw/ae71beea5458b056697433acdbf6844e.png)

## FFmpeg 设置[](id:FFmpeg)
如果需要用命令行或其他 RTMP 库推流，请参见 [设置推流参数](#step2) 中服务器地址 + 串流密钥组成标准 RTMP 推流地址，可供 FFmpeg 或其他 RTMP 库推流，视频编码使用 H.264，音频编码使用 AAC，容器格式使用 FLV，建议 GOP 设置为2s或1s。
FFmpeg 不同场景下指令配置参数不同，因此需要您具有一定的 FFmpeg 使用经验，以下列出 FFmpeg 常用命令行选项，更多 FFmpeg 选项请参见 [FFmpeg 官网](https://ffmpeg.org/ffmpeg.html)。

### FFmpeg 命令行[](id:order)
```
ffmpeg [global_options] {[input_file_options] -i input_url} ... {[output_file_options] output_url} 
```

### 常见的 FFmpeg 选项[](id:set)
<table>
<thead><tr><th>选项</th><th>说明</th></tr></thead>
<tbody><tr>
<td>-re</td><td>以 native 帧率读取输入，通常只用于读取本地文件</td>
</tr></tr></tbody></table>

其中 **output_file_options** 可配置选项包括：

<table>
<thead><tr><th>选项</th><th>说明</th></tr></thead>
<tbody><tr>
<td>-c:v</td><td>视频编码，建议用 <code>libx264</code></td>
</tr><tr>
<td>-b:v</td><td>视频码率，例如 1500k 表示 1500kbps</td>
</tr><tr>
<td>-r</td><td>视频帧率</td>
</tr><tr>
<td>-profile:v</td><td>视频 profile，指定 baseline 将不编码 B 帧，TRTC 后端不支持 B 帧</td>
</tr><tr>
<td>-g</td><td>GOP 帧数间隔</td>
</tr><tr>
<td>-c:a</td><td>音频编码，建议用 <code>libfdk_aac</code></td>
</tr><tr>
<td>-ac</td><td>声道数，填2或1</td>
</tr><tr>
<td>-b:a</td><td>音频码率</td>
</tr><tr>
<td>-f</td><td>指定格式，固定填 <code>flv</code>，发送到 TRTC 使用 FLV 容器封装</td>
</tr></tbody></table>
下面的例子是读取文件推到 TRTC。

```
ffmpeg -loglevel info -re -i sample.flv -c:v libx264 -preset fast -profile:v baseline -g 30 -sc_threshold 0 -b:v 1500k -c:a libfdk_aac -ac 2 -b:a 128k -f flv 'rtmp://rtmp.rtc.qq.com/push/hello-string-room?userid=rtmpForFfmpeg&sdkappid=140xxxxxx&usersig=xxxxxxxxxx'
```

### Web 端观看效果[](id:view)
![](https://qcloudimg.tencent-cloud.cn/raw/323175a92a936e5c7dcfdef5a2575e60.png)


