
本文档介绍的是腾讯云点播的超级播放器，它可以帮助腾讯云客户通过丰富、灵活的接口，快速与自有 Web 应用集成，实现视频播放功能，本文档适合有一定 Javascript 语言基础的开发人员阅读。
[](id:introduction)
## 能力介绍
点播超级播放器是基于 HTML5 的 `<video>` 标签使用多种播放策略来实现视频播放，实现了多平台播放效果的统一，并结合腾讯云点播视频服务，提供防盗链和播放 HLS 加密视频等功能。

### 功能支持
[](id:supportFunction)
<Table>
  <tr>
    <th width="50px" style="text-align:center">功能\浏览器</th>
      <th width="50px" style="text-align:center">Chrome</th>
      <th width="50px" style="text-align:center">Firefox</th>
      <th width="50px" style="text-align:center">Edge</th>
      <th width="50px" style="text-align:center">QQ 浏览器</th>
      <th width="50px" style="text-align:center">Mac Safari</th>
      <th width="50px" style="text-align:center">iOS Safari</th>
      <th width="50px" style="text-align:center">微信 QQ</th>
      <th width="50px" style="text-align:center">Android Chrome</th>
      <th width="50px" style="text-align:center">IE 11</th>
  </tr>
   <tr>
         <td style="text-align:center">MP4 格式</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
    </tr>
      <tr>
         <td style="text-align:center">HLS 格式</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
    </tr>
         <tr>
         <td style="text-align:center">播放器尺寸设置</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
    </tr>
         <tr>
         <td style="text-align:center">续播功能</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
    </tr>
         <tr>
         <td style="text-align:center">倍速播放</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
    </tr>
         <tr>
         <td style="text-align:center">缩略图预览</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">-</td>
         <td style="text-align:center">-</td>
         <td style="text-align:center">-</td>
         <td style="text-align:center">-</td>
         <td style="text-align:center">&#10003;</td>
    </tr>
            <tr>
         <td style="text-align:center">切换 fileID 播放</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
    </tr>
            <tr>
         <td style="text-align:center">镜像功能</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
    </tr>
         <tr>
         <td style="text-align:center">进度条标记</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">-</td>
         <td style="text-align:center">-</td>
         <td style="text-align:center">-</td>
         <td style="text-align:center">&#10003;</td>
    </tr>
               <tr>
         <td style="text-align:center">HLS 自适应码率</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
    </tr>
               <tr>
         <td style="text-align:center">Referer 防盗链</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">-</td>
         <td style="text-align:center">&#10003;</td>
    </tr>
               <tr>
         <td style="text-align:center">清晰度切换提示</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">-</td>
         <td style="text-align:center">-</td>
         <td style="text-align:center">-</td>
         <td style="text-align:center">-</td>
         <td style="text-align:center">-</td>
    </tr>
               <tr>
         <td style="text-align:center">试看功能</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
    </tr>
    <tr>
         <td style="text-align:center">HLS 普通加密播放</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">-</td>
         <td style="text-align:center">-</td>
         <td style="text-align:center">-</td>
         <td style="text-align:center">-</td>
         <td style="text-align:center">-</td>
         <td style="text-align:center">-</td>
    </tr>
  	<tr>
         <td style="text-align:center">HLS 私有加密播放</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">-</td>
         <td style="text-align:center">-</td>
         <td style="text-align:center">-</td>
         <td style="text-align:center">-</td>
         <td style="text-align:center">-</td>
         <td style="text-align:center">-</td>
    </tr>
               <tr>
         <td style="text-align:center">视频统计信息</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">-</td>
         <td style="text-align:center">-</td>
         <td style="text-align:center">-</td>
         <td style="text-align:center">-</td>
         <td style="text-align:center">-</td>
    </tr>
               <tr>
         <td style="text-align:center">自定义提示文案</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
    </tr>
  	<tr>
         <td style="text-align:center">弹幕</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
         <td style="text-align:center">&#10003;</td>
    </tr>



</Table>

>?
>- 视频编码格式仅支持 H.264 编码。
>- Chrome、Firefox 包括 Windows、macOS 平台。
>- Chrome、Firefox、Edge 及 QQ 浏览器播放 HLS 需要加载 `hls.js`。
>- Referer 防盗链功能是基于 HTTP 请求头的 Referer 字段实现的，部分 Android 浏览器发起的 HTTP 请求不会携带 Referer 字段。

播放器兼容常见的浏览器，播放器内部会自动区分平台，并使用最优的播放方案。例如：在 Chrome 等现代浏览器中优先使用 HTML5 技术实现视频播放，而手机浏览器上会使用 HTML5 技术或者浏览器内核能力实现视频播放。



## 准备工作

超级播放器可与云点播能力结合，具体流程请参见 [使用超级播放器播放 - 接入指引](https://cloud.tencent.com/document/product/266/43629#.E5.88.9D.E7.BA.A7.E6.AD.A5.E9.AA.A4) 文档。



## 集成指引
在准备工作完成后，通过以下步骤，您就可以在网页上添加一个视频播放器。
### 步骤1：在页面中引入文件
在 html 页面引入播放器样式文件与脚本文件：
```
 <link href="https://web.sdk.qcloud.com/player/tcplayer/release/v4.2.2/tcplayer.min.css" rel="stylesheet"/>
 <!--如果需要在 Chrome 和 Firefox 等现代浏览器中通过 H5 播放 HLS 格式的视频，需要在 tcplayer.v4.2.2.min.js 之前引入 hls.min.0.13.2m.js。-->
 <script src="https://web.sdk.qcloud.com/player/tcplayer/release/v4.2.2/libs/hls.min.0.13.2m.js"></script>
 <!--播放器脚本文件-->
 <script src="https://web.sdk.qcloud.com/player/tcplayer/release/v4.2.2/tcplayer.v4.2.2.min.js"></script>
```

建议在使用播放器 SDK 的时候自行部署资源，[点击下载播放器资源](https://web.sdk.qcloud.com/player/tcplayer/release/v4.2.2/release.zip) 。

部署解压后的文件夹，不能调整文件夹里面的目录，避免资源互相引用异常。

如果您部署的地址为 `aaa.xxx.ccc`，在合适的地方引入播放器样式文件与脚本文件：
```
 <link href="aaa.xxx.ccc/tcplayer.min.css" rel="stylesheet"/>
 <!--如果需要在 Chrome 和 Firefox 等现代浏览器中通过 H5 播放 HLS 格式的视频，需要在 tcplayer.v4.2.2.min.js 之前引入 hls.min.0.13.2m.js。-->
 <script src="aaa.xxx.ccc/libs/hls.min.0.13.2m.js"></script>
 <!--播放器脚本文件-->
 <script src="aaa.xxx.ccc/tcplayer.v4.2.2.min.js"></script>
```

### 步骤2：放置播放器容器
在需要展示播放器的页面位置加入播放器容器。例如，在 index.html 中加入如下代码（容器 ID 以及宽高都可以自定义）。
```
<video id="player-container-id" width="414" height="270" preload="auto" playsinline webkit-playsinline>
</video>
```

>?
>- 播放器容器必须为 `<video>` 标签。
>- 示例中的 `player-container-id` 为播放器容器的 ID，可自行设置。
>- 播放器容器区域的尺寸，建议通过 CSS 进行设置，通过 CSS 设置比属性设置更灵活，可以实现例如铺满全屏、容器自适应等效果。
>- 示例中的 `preload` 属性规定是否在页面加载后载入视频，通常为了更快的播放视频，会设置为 `auto`，其他可选值：`meta`（当页面加载后只载入元数据），`none`（当页面加载后不载入视频），移动端由于系统限制不会自动加载视频。
>- `playsinline` 和 `webkit-playsinline` 这几个属性是为了在标准移动端浏览器不劫持视频播放的情况下实现行内播放，此处仅作示例，请按需使用。
>- 设置 `x5-playsinline` 属性在 TBS 内核会使用 X5 UI 的播放器。

### 步骤3：初始化代码
在页面初始化的代码中加入以下初始化脚本，传入在准备工作中获取到的 fileID（[**媒资管理**](https://console.cloud.tencent.com/vod/media)中的视频 ID）与 appID（在**账号信息**>[**基本信息**](https://console.cloud.tencent.com/developer)中查看）。
```
var player = TCPlayer('player-container-id', { // player-container-id 为播放器容器 ID，必须与 html 中一致
    fileID: '5285890799710670616', // 请传入需要播放的视频 fileID（必须）
    appID: '1400329073' // 请传入点播账号的 appID（必须）
  });
```

>!要播放的视频建议使用腾讯云转码，原始视频无法保证在浏览器中正常播放。



## 示例页面

单击 [示例代码](https://tcplayer-1306264703.cos.ap-nanjing.myqcloud.com/build/index.html) 进入示例页面，查看各功能使用方法和说明。



## 参数列表

播放器初始化需要传入两个参数，第一个为播放器容器 ID，第二个为功能参数对象。

```
var player = TCPlayer('player-container-id', options);
```

#### options 参数列表：

| 名称          | 类型          | 默认值                 | 说明                                                         |
| ------------- | ------------- | ---------------------- | ------------------------------------------------------------ |
| appID         | String        | 无                     | 必选。                                                       |
| fileID        | String        | 无                     | 必选。                                                       |
| width         | String/Number | 无                     | 播放器区域宽度，单位像素，按需设置，可通过 CSS 控制播放器尺寸。 |
| height        | String/Number | 无                     | 播放器区域高度，单位像素，按需设置，可通过 CSS 控制播放器尺寸。 |
| controls      | Boolean       | true                   | 是否显示播放器的控制栏。                                     |
| poster        | String        | 无                     | 设置封面图片完整地址（如果上传的视频已生成封面图，优先使用生成的封面图，详细请参见 [云点播 - 管理视频](https://cloud.tencent.com/document/product/266/36452)）。 |
| autoplay      | Boolean       | false                  | 是否自动播放。                                               |
| playbackRates | Array         | [0.5，1，1.25，1.5，2] | 设置变速播放倍率选项，仅 HTML5 播放模式有效。                |
| loop          | Boolean       | false                  | 是否循环播放。                                               |
| muted         | Boolean       | false                  | 是否静音播放。                                               |
| preload       | String        | auto                   | 是否需要预加载，有3个属性"auto"，"meta"和"none" ，移动端由于系统限制，设置 auto 无效。 |
| swf           | String        | 无                     | Flash 播放器 swf 文件的 URL。                                |
| posterImage   | Boolean       | true                   | 是否显示封面。                                               |
| bigPlayButton | Boolean       | true                   | 是否显示居中的播放按钮（浏览器劫持嵌入的播放按钮无法去除）。 |
| language      | String        | "zh-CN"                | 设置语言。                                                   |
| languages     | Object        | 无                     | 设置多语言词典。                                             |
| controlBar    | Object        | 无                     | 设置控制栏属性的参数组合，后面有详细介绍。                   |
| plugins       | Object        | 无                     | 设置插件功能属性的参数组合，后面有详细介绍。                 |
| hlsConfig     | Object        | 无                     | hls.js 的启动配置，详细内容请参见官方文档 [hls.js](https://github.com/video-dev/hls.js/blob/master/docs/API.md#fine-tuning)。 |

>! controls、playbackRates、loop、preload、posterImage 这些参数在浏览器劫持播放的状态下将无效（[什么是劫持播放？](https://cloud.tencent.com/document/product/881/20219#.E6.B5.8F.E8.A7.88.E5.99.A8.E5.8A.AB.E6.8C.81.E8.A7.86.E9.A2.91.E6.92.AD.E6.94.BE)）。

#### controlBar 参数列表

controlBar 参数可以配置播放器控制栏的功能，支持的属性有：

| 名称                      | 类型    | 默认值 | 说明                         |
| ------------------------- | ------- | ------ | ---------------------------- |
| playToggle                | Boolean | true   | 是否显示播放、暂停切换按钮。 |
| progressControl           | Boolean | true   | 是否显示播放进度条。         |
| volumePanel               | Boolean | true   | 是否显示音量控制。           |
| currentTimeDisplay        | Boolean | true   | 是否显示视频当前时间。       |
| durationDisplay           | Boolean | true   | 是否显示视频时长。           |
| timeDivider               | Boolean | true   | 是否显示时间分割符。         |
| playbackRateMenuButton    | Boolean | true   | 是否显示播放速率选择按钮。   |
| fullscreenToggle          | Boolean | true   | 是否显示全屏按钮。           |
| QualitySwitcherMenuButton | Boolean | true   | 是否显示清晰度切换菜单。     |

>! controlBar 参数在浏览器劫持播放的状态下将无效（[什么是劫持播放？](https://cloud.tencent.com/document/product/881/20219#.E6.B5.8F.E8.A7.88.E5.99.A8.E5.8A.AB.E6.8C.81.E8.A7.86.E9.A2.91.E6.92.AD.E6.94.BE)）。

#### plugins 插件参数列表

plugins 参数可以配置播放器插件的功能，支持的属性有：

| 名称 | 类型 | 默认值 | 说明 |
| ---- | ---- | ------ | ---- |
|  ContinuePlay|  Object|  无|  控制续播功能，支持的属性如下：<br><li>auto：false（是否在播放时自动续播）。<br><li>text：“上次看到”（提示文案）。<br><li>btnText：“恢复播放”（按钮文案）。<br>



## 对象方法

初始化播放器返回对象的方法列表：

| 名称                 | 参数及类型           | 返回值及类型          | 说明                                                         |
| -------------------- | -------------------- | --------------------- | ------------------------------------------------------------ |
| ready(function)      | (Function)           | 无                    | 设置播放器初始化完成后的回调。                               |
| play()               | 无                   | 无                    | 播放以及恢复播放。                                           |
| pause()              | 无                   | 无                    | 暂停播放。                                                   |
| currentTime(seconds) | (Number)             | (Number)              | 获取当前播放时间点，或者设置播放时间点，该时间点不能超过视频时长。 |
| duration()           | 无                   | (Number)              | 获取视频时长。                                               |
| volume(percent)      | (Number)[0，1][可选] | (Number)/设置时无返回 | 获取或设置播放器音量。                                       |
| poster(src)          | (String)             | (String)/设置时无返回 | 获取或设置播放器封面。                                       |
| requestFullscreen()  | 无                   | 无                    | 进入全屏模式。                                               |
| exitFullscreen()     | 无                   | 无                    | 退出全屏模式。                                               |
| isFullscreen()       | 无                   | Boolean               | 返回是否进入了全屏模式。                                     |
| on(type，listerner)  | (String, Function)   | 无                    | 监听事件。                                                   |
| one(type，listerner) | (String, Function)   | 无                    | 监听事件，事件处理函数最多只执行1次。                        |
| off(type，listerner) | (String, Function)   | 无                    | 解绑事件监听。                                               |
| buffered()           | 无                   | TimeRanges            | 返回视频缓冲区间。                                           |
| bufferedPercent()    | 无                   | 值范围[0，1]          | 返回缓冲长度占视频时长的百分比。                             |
| width()              | (Number)[可选]       | (Number)/设置时无返回 | 获取或设置播放器区域宽度，如果通过 CSS 设置播放器尺寸，该方法将无效。 |
| height()             | (Number)[可选]       | (Number)/设置时无返回 | 获取或设置播放器区域高度，如果通过 CSS 设置播放器尺寸，该方法将无效。 |
| videoWidth()         | 无                   | (Number)              | 获取视频分辨率的宽度。                                       |
| videoHeight()        | 无                   | (Number)              | 获取视频分辨率的高度。                                       |
| dispose()            | 无                   | 无                    | 销毁播放器。                                                 |

>! 对象方法不能同步调用，需要在相应的事件（如 loadedmetadata）触发后才可以调用，除了 ready、on、one 以及 off。



## 监听事件

播放器可以通过初始化返回的对象进行事件监听，示例：

```
var player = TCPlayer('player-container-id', options);
// player.on(type, function);
player.on('error', function(error) {
   // 做一些处理
});
```

其中 type 为事件类型，支持的事件有：

| 名称                | 介绍                                                         |
| ------------------- | ------------------------------------------------------------ |
| play                | 已经开始播放，调用 play() 方法或者设置了 autoplay 为 true 且生效时触发，这时 paused 属性为 false。 |
| playing             | 因缓冲而暂停或停止后恢复播放时触发，paused 属性为 false 。通常用这个事件来标记视频真正播放，play 事件只是开始播放，画面并没有开始渲染。 |
| loadstart           | 开始加载数据时触发。                                         |
| durationchange      | 视频的时长数据发生变化时触发。                               |
| loadedmetadata      | 已加载视频的 metadata。                                      |
| loadeddata          | 当前帧的数据已加载，但没有足够的数据来播放视频的下一帧时，触发该事件。 |
| progress            | 在获取到媒体数据时触发。                                     |
| canplay             | 当播放器能够开始播放视频时触发。                             |
| canplaythrough      | 当播放器预计能够在不停下来进行缓冲的情况下持续播放指定的视频时触发。 |
| error               | 视频播放出现错误时触发。                                     |
| pause               | 暂停时触发。                                                 |
| ratechange          | 播放速率变更时触发。                                         |
| seeked              | 搜寻指定播放位置结束时触发。                                 |
| seeking             | 搜寻指定播放位置开始时触发。                                 |
| timeupdate          | 当前播放位置有变更，可以理解为 currentTime 有变更。          |
| volumechange        | 设置音量或者 muted 属性值变更时触发。                        |
| waiting             | 播放停止，下一帧内容不可用时触发。                           |
| ended               | 视频播放已结束时触发。此时 currentTime 值等于媒体资源最大值。 |
| resolutionswitching | 清晰度切换进行中。                                           |
| resolutionswitched  | 清晰度切换完毕。                                             |
| fullscreenchange    | 全屏状态切换时触发。                                         |



## 错误码说明

当播放器触发 error 事件时，监听函数会返回错误码，其中3位数以上的错误码为媒体数据接口错误码。错误码列表：

| 名称  | 描述                                                         |
| ----- | ------------------------------------------------------------ |
| -1    | 播放器没有检测到可用的视频地址。                             |
| -2    | 获取视频数据超时。                                           |
| 1     | 视频数据加载过程中被中断。<br>可能原因：<br><li> 网络中断。<br><li> 浏览器异常中断。<br>解决方案：<br><li> 查看浏览器控制台网络请求信息，确认网络请求是否正常。<br><li>重新进行播放流程。 |
| 2     | 由于网络问题造成加载视频失败。<br>可能原因：网络中断。<br>解决方案:<br><li> 查看浏览器控制台网络请求信息，确认网络请求是否正常。<br><li> 重新进行播放流程。 |
| 3     | 视频解码时发生错误。<br>可能原因：视频数据异常，解码器解码失败。<br>解决方案：<br><li> 尝试重新转码再进行播放，排除由于转码流程引入的问题。<br><li> 确认原始视频是否正常。 <br><li> 请联系技术客服并提供播放参数进行定位排查。 |
| 4     | 视频因格式不支持或者服务器或网络的问题无法加载。<br>可能原因：<br><li> 获取不到视频数据，CDN 资源不存在或者没有返回视频数据。<br><li> 当前播放环境不支持播放该视频格式。<br>解决方案：<br><li> 查看浏览器控制台网络请求信息，确认视频数据请求是否正常。<br><li> 确认是否按照使用文档加载了对应视频格式的播放脚本。<br><li> 确认当前浏览器和页面环境是否支持将要播放的视频格式。 <br><li> 请联系技术客服并提供播放参数进行定位排查。 |
| 5     | 视频解密时发生错误。<br>可能原因：<br><li> 解密用的密钥不正确。<br><li> 请求密钥接口返回异常。<br><li> 当前播放环境不支持视频解密功能。<br>解决方案：<br><li> 确认密钥是否正确，以及密钥接口是否返回正常。<br><li> 请联系技术客服并提供播放参数进行定位排查。<br> |
| 10    | 点播媒体数据接口请求超时。在获取媒体数据时，播放器重试3次后仍没有任何响应，会抛出该错误。<br>可能原因：<br><li> 当前网络环境无法连接到媒体数据接口，或者媒体数据接口被劫持。<br><li> 媒体数据接口异常。<br>解决方案：<br><li> 尝试打开我们提供的 Demo 页面看是否可以正常播放。 <br><li>请联系技术客服并提供播放参数进行定位排查。<br> |
| 11    | 点播媒体数据接口没有返回数据。在获取媒体数据时，播放器重试3次后仍没有数据返回，会抛出该错误。<br>可能原因：<br><li> 当前网络环境无法连接到媒体数据接口，或者媒体数据接口被劫持。<br><li> 媒体数据接口异常。<br>解决方案：<br><li> 尝试打开我们提供的 Demo 页面看是否可以正常播放。 <br><li> 请联系技术客服并提供播放参数进行定位排查。<br> |
| 12    | 点播媒体数据接口返回异常数据。在获取媒体数据时，播放器重试3次后仍返回无法解析的数据，会抛出该错误。<br>可能原因：<br><li> 当前网络环境无法连接到媒体数据接口，或者媒体数据接口被劫持。<br><li> 播放参数有误，媒体数据接口无法处理。<br><li> 媒体数据接口异常。 <br>解决方案：<br><li> 尝试打开我们提供的 Demo 页面看是否可以正常播放。 <br><li> 请联系技术客服并提供播放参数进行定位排查。<br> |
| 13    | 播放器没有检测到可以在当前播放器播放的视频数据，请对该视频进行转码操作。 |
| 14    | HTML5 + hls.js 模式下播放 hls 出现网络异常，异常详情可在 event.source 中查看，详细介绍请看 hls.js 的官方文档 [Network Errors](https://github.com/video-dev/hls.js/blob/master/docs/API.md#network-errors)。 |
| 15    | HTML5 + hls.js 模式下播放 hls 出现多媒体异常，异常详情可在 event.source 中查看，详细介绍请看 hls.js 的官方文档 [Media Errors](https://github.com/video-dev/hls.js/blob/master/docs/API.md#media-errors)。 |
| 16    | HTML5 + hls.js 模式下播放 hls 出现多路复用异常，异常详情可在 event.source 中查看，详细介绍请看 hls.js 的官方文档 [Mux Errors](https://github.com/video-dev/hls.js/blob/master/docs/API.md#mux-errors)。 |
| 17    | HTML5 + hls.js 模式下播放 hls 出现其他异常，异常详情可在 event.source 中查看，详细介绍请看 hls.js 的官方文档 [Other Errors](https://github.com/video-dev/hls.js/blob/master/docs/API.md#other-errors)。 |
| 10008 | 媒体数据服务没有找到对应播放参数的媒体数据，请确认请求参数 appID fileID 是否正确，以及对应的媒体数据是否已经被删除。 |



## 更新日志
TCPlayer 在不断更新及完善中，下面是 TCPlayer 发布的主版本介绍。

| 日期             | 版本     | 更新内容
|-----------------|--------- |-------------------------------------------- |
| 2021.8.11       |   4.2.2  |   1. 在safari等不支持字幕的环境屏蔽字幕入口。<br>2. 微信内默认开启hls.js。<br> 3. errcode14网络问题自动重连。<br> 4.chrome模拟器ios允许播放。 |
| 2020.7.10       |   4.1    |   1. 修改默认 hls.js 版本为0.13.2。<br> 2. 支持开启 Key 防盗链功能。 <br>3. 修复其他已知问题。 |
| 2020.6.17       |   4.0    |   1. 修复试看视频时长保持显示原始时长。<br>2. 启用后台清晰度配置。 <br>3. 修复其他已知问题。 |

