## 示例代码
针对开发者的接入反馈的高频问题，腾讯云提供有更加简洁的 API-Example 工程，方便开发者可以快速的了解相关 API 的使用，欢迎使用。

| 所属平台 |                         GitHub 地址                          |
| :------: | :----------------------------------------------------------: |
|   iOS    | [Github](https://github.com/LiteAVSDK/Live_iOS/tree/main/MLVB-API-Example-OC) |
| Android  | [Github](https://github.com/LiteAVSDK/Live_Android/tree/main/MLVB-API-Example) |

## 功能介绍
在了解自适应码率播放之前，首先要了解什么是无缝切流。

- **无缝切流**：在切换不同码率的转码流时，能够做到无缝衔接，不会出现声音画面中断或者跳变的情况，实现观感和听感的平滑过渡。
- **自适应码率播放**：在无缝切流的基础上更进一步，无需用户干预，完全由当前网络带宽来决定实现自动无缝切流，减少网络波动对播放流畅度的影响。

## 开启自适应播放
自适应播放功能依托于腾讯云的**直播自适应码率**支撑，如果您想要对接这个功能，需要在腾讯云的管理控制台 [开通直播自适应码率服务](https://console.cloud.tencent.com/live/config/adaptive-rate)。服务开通之后，需要创建**至少一个自适应模板并包含两个子流**，才可使用自适应播放功能。

>? 
>- 自适应播放会在创建的自适应模板模板中，通过当前网络带宽来选择一个子流进行播放
>- 在使用自适应码率功能时，会产生模板中**所有子流**的 [转码费用](https://cloud.tencent.com/document/product/267/39889)。

#### 创建自适应码率模板
1. 登录 [云直播控制台](https://console.cloud.tencent.com/live/config/transcode)，选择**功能配置** > **直播自适应码率**，创建自适应码率模板。如下图所示：
<img src="https://qcloudimg.tencent-cloud.cn/raw/844beca297d7a2beb0204f970187e75d.png" width="900">
3. **配置子流**：至少应该配置两个子流。
<img src="https://qcloudimg.tencent-cloud.cn/raw/87d4ac244b5b7cf6401bf72d16aff331.png" width="900">
3. **绑定域名**：创建转码模板之后，需要绑定域名。<br>
<img src="https://qcloudimg.tencent-cloud.cn/raw/83f7451dc3c9838e08b28b4d6c58685a.png" width="600">

>? **配置自适应码率模板的详细参数**，请参见 [直播自适应码率](https://cloud.tencent.com/document/product/267/78369)


## 获取 HLS 自适应播放地址

1. 通过 [地址生成器](https://console.cloud.tencent.com/live/addrgenerator/addrgenerator)，选择创建的自适应码率模板，单击**生成**。
 <img src="https://qcloudimg.tencent-cloud.cn/raw/8ce6df1097cc472e18cb6e57c9d3e779.jpg" width="600">
2. 通过自适应模板的名称，来拼接地址。HLS 自适应播放的格式为：
```http
http://{Domain}/{AppName}/{StreamName}_{AdaptiveTemplate}.m3u8
```
在上述的 URL 中，存在一些关键字段，关于其中关键字段的含义信息，详见下表：
<table>
<thead>
<tr>
<th>字段名称</th>
<th>字段含义</th>
</tr>
</thead>
<tbody><tr>
<td>http://</td>
<td>HLS URL 的前缀字段</td>
</tr>
<tr>
<td>Domain</td>
<td>HLS 直播播放域名</td>
</tr>
<tr>
<td>AppName</td>
<td>应用名称，指的是直播流媒体文件存放路径，默认云直播会分配一个路径：live</td>
</tr>
<tr>
<td>StreamName</td>
<td>流名称，指每路直播流唯一的标识符</td>
</tr>
<tr>
<td>AdaptiveTemplate</td>
<td>自适应码率模板名称，表明使用哪一个配置模板</td>
</tr>
</tbody></table>
URL 地址样例（hlsAutoTest 为自适应码率模板名称）：
<table>
<thead>
<tr>
<th></th>
<th>URL地址</th>
</tr>
</thead>
<tbody><tr>
<td>原始</td>
<td>http://xxx.liveplay.myqcloud.com/stream_name.m3u8</td>
</tr>
<tr>
<td>自适应播放</td>
<td>http://xxx.liveplay.myqcloud.com/stream_name_hlsAutoTest.m3u8</td>
</tr>
</tbody></table>

## 实现 HLS 自适应播放

使用 `V2TXLivePlayer` 对象可以使用 HLS 自适应播放，具体做法如下（传入正确的 URL 是关键）：

#### 示例代码
<dx-codeblock>
::: Android java
// 创建⼀个 V2TXLivePlayer 对象；
V2TXLivePlayer player = new V2TXLivePlayerImpl(mContext);
player.setObserver(new MyPlayerObserver(playerView));
player.setRenderView(mSurfaceView);
// 传⼊HLS自适应播放地址，即可开始播放；
player.startLivePlay("http://{Domain}/{AppName}/{StreamName}_{AdaptiveTemplate}.m3u8");
:::
::: iOS obj-c
// 创建⼀个 V2TXLivePlayer 对象；
V2TXLivePlayer *player = [[V2TXLivePlayer alloc] init];
[player setObserver:self];
[player setRenderView:videoView];
// 传⼊HLS自适应播放地址，即可开始播放；
[player startLivePlay:@"http://{Domain}/{AppName}/{StreamName}_{AdaptiveTemplate}.m3u8"];
:::
</dx-codeblock>


## 实现 HLS 无缝切流

使用 `V2TXLivePlayer` 对象可以使用 HLS 无缝切流，具体做法如下：
1. **播放自适应地址，并且设置 Observer 回调**
<dx-codeblock>
::: Android java
// 创建⼀个 V2TXLivePlayer 对象；
V2TXLivePlayer player = new V2TXLivePlayerImpl(mContext);
player.setObserver(new MyPlayerObserver(playerView));
player.setRenderView(mSurfaceView);
// 传⼊HLS自适应播放地址，即可开始播放；
player.startLivePlay("http://{Domain}/{AppName}/{StreamName}_{AdaptiveTemplate}.m3u8");
:::
::: iOS obj-c
// 创建⼀个 V2TXLivePlayer 对象；
V2TXLivePlayer *player = [[V2TXLivePlayer alloc] init];
[player setObserver:self];
[player setRenderView:videoView];
// 传⼊HLS自适应播放地址，即可开始播放；
[player startLivePlay:@"http://{Domain}/{AppName}/{StreamName}_{AdaptiveTemplate}.m3u8"];
:::
</dx-codeblock>
2. **在 onConnected 回调中，获取全部的子流地址**
<dx-codeblock>
::: Android java
/**
 * 已经成功连接到服务器
 * @param player    回调该通知的播放器对象
 * @param extraInfo 扩展信息
 */
public void onConnected(V2TXLivePlayer player, Bundle extraInfo){
    ArrayList<V2TXLiveStreamInfo> streams = player.getStreamList();
}
:::
::: iOS obj-c
/**
 * 已经成功连接到服务器
 * @param player    回调该通知的播放器对象
 * @param extraInfo 扩展信息
 */
- (void)onConnected:(id<V2TXLivePlayer>)player extraInfo:(NSDictionary *)extraInfo {
    self.streams = [player getStreamList]
}
:::
</dx-codeblock>
3. **切换到一个子流**
<dx-codeblock>
::: Android java
// 选择期望质量的码流 
V2TXLiveStreamInfo stream = streams.get(index);
// 切换到期望质量的码流
player.switchStream(stream.url);
:::
::: iOS obj-c
// 选择期望质量的码流 
V2TXLiveStreamInfo *streamInfo = self.streams[index];
// 切换到期望质量的码流
[self.player switchStream:streamInfo.url];
:::
</dx-codeblock>
4. **切换回自适应播放**
<dx-codeblock>
::: Android java
player.switchStream("http://{Domain}/{AppName}/{StreamName}_{AdaptiveTemplate}.m3u8");
:::
::: iOS obj-c
[self.player switchStream:@"http://{Domain}/{AppName}/{StreamName}_{AdaptiveTemplate}.m3u8"];
:::
</dx-codeblock>

