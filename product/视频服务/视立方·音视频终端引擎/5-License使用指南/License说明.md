腾讯云视立方 License 通过一组 License URL 和 Key 来获取并校验一个应用下功能模块的授权。不同的功能模块具备不同的功能。若您下载的腾讯云视立方版本中，包含直播推流（主播开播和主播观众连麦/主播跨房 PK）或短视频（视频录制编辑/视频上传发布）功能模块，需通过购买对应的云服务的资源包免费获取 License，从而解锁对应功能模块的能力。功能模块解锁详情请参见 [SDK 下载](https://cloud.tencent.com/document/product/1449/56978)。

## 新旧 License 区别
旧版 License 仅支持一组 License URL 和 Key 解锁对应一个 SDK 功能（移动直播或短视频），相比腾讯云视立方 License 维护和使用较为繁琐；升级后的新版视立方 License 后仅需维护一组 License URL 和 Key ，便可以管理所有腾讯云音视频的终端授权。

原移动直播 License、短视频 License 可在腾讯云视立方·音视频终端引擎中继续使用，对应授权解锁腾讯云视立方·音视频终端引擎中的直播推流（主播开播、主播观众连麦/主播跨房 PK）与短视频（视频录制编辑/视频上传发布）模块，**若您使用包含上述功能模块的版本时，处于有效期内的 License 无需再次购买解锁授权**。新旧 License 对应详情如下：

<table>
<thead>
<tr>
<th colspan=2>腾讯云视立方 License</th>
<th>原 SDK License</th>
</tr>
</thead>
<tbody><tr>
<td colspan=2>直播推流 License</td>
<td>移动直播基础版 License</td>
</tr>
<tr>
<td rowspan=2>短视频 License</td>
<td>短视频精简版 License</td>
<td>短视频精简版 License</td>
</tr>
<tr>
<td>短视频基础版 License</td>
<td>短视频基础版 License</td>
</tr>
</tbody></table>

>? 若您的应用正使用旧版 License 进行校验，可继续使用旧版 License 或改用新版 License（推荐）。未来新购买获赠的 License 进行绑定时将不再提供旧版 License 的 URL 和 Key 。

## 测试版 License
您可以登录 [腾讯云视立方控制台](https://console.cloud.tencent.com/vcube) 在线申请为期28天的试用 License（试用期为14天，可免费续期一次，合计28天），该 License 可以在直播推流模块和短视频模块上使用。

> ? 
> - 每个功能模块仅可申请一次，长期使用请 [购买](https://buy.cloud.tencent.com/vcube) 正式 License。
> - 试用期内申请测试续期，则续期到期时间以申请测试时刻为准；若试用期结束后申请测试续期，则续期到期时间以申请测试续期时刻为准。
>   - 当申请测试开始时间为2021-08-12 10:28:41，则14天后到期时间为2021-08-26 10：28:41；
>   - 免费续期一次时，若在试用期14天内申请续期，则到期时间为2021-09-09 10:28:41；若在试用期14天结束后申请续期，申请续期的时间为2021-08-30 22:26:20，则续期的到期时间为2021-09-13 22:26:20。

## 正式版 License
> ! 获得 License 解锁功能模块的计费详情，请参见 [计费概述](https://cloud.tencent.com/document/product/1449/56972)。

[](id:Live)
### 直播推流模块

购买 10TB 、50TB 、200TB 、1PB 云直播流量资源包，可以解锁直播推流（主播开播和主播观众连麦/主播跨房 PK）模块，有效期一年。更多新增与续期操作请参见 [直播推流 License](https://cloud.tencent.com/document/product/1449/56981)。

> ? 小程序端的直播推流/播放功能需要先取得对应的直播相关资质，详情可参见 [小程序直播接入指引](https://cloud.tencent.com/document/product/1078/37707)。


[](id:UGSV)
### 短视频模块
- 购买 10TB 云点播流量资源包，可以解锁短视频模块（精简版），有效期一年。
- 购买 50TB 、200TB 、1PB 云点播流量资源包，可以解锁短视频模块（基础版），有效期一年。

更多新增与续期操作请参见 [短视频 License](https://cloud.tencent.com/document/product/1449/56982)。

[](id:UGSV_detail)
#### 短视频 License 功能详情
短视频 License 包括**精简版 License** 和**基础版 License**。精简版 License 支持视频生成、上传、处理、分发和播放多种功能；基础版 License 在精简版基础上增加滤镜、特效和转场等能力，快速轻松实现基于移动端的短视频应用。功能支持详情如下：

<table>        
   <tr>
      <th width="85px" style="text-align:center">功能模块</td>
      <th width="85px" style="text-align:center">功能项</td>
      <th width="0px"  style="text-align:center">功能简介</td>
      <th width="92px" style="text-align:center">精简版 License</td>
      <th width="92px" style="text-align:center">基础版 License</td>
   </tr>
   <tr>
      <td>界面</td>
      <td>自定义 UI</td>
	    <td>开发者自定义 UI。小视频 App 提供了一套完整的 UI 交互源码，可复用或自定义。</td>
      <td style="text-align:center">&#10003;</td>
      <td style="text-align:center">&#10003;</td>
   </tr>
   <tr>
      <td rowspan='18'>采集拍摄</td>
      <td>屏比</td>
      <td>支持16:9，4:3，1:1多种屏比拍摄。</td>
      <td style="text-align:center">&#10003;</td>
      <td style="text-align:center">&#10003;</td>
   </tr>
   <tr>
      <td>清晰度</td>
      <td>支持标清、高清、超清拍摄，支持自定义码率、帧率、GOP。</td>
      <td style="text-align:center">&#10003;</td>
      <td style="text-align:center">&#10003;</td>
   </tr>
   <tr>
      <td>拍摄控制</td>
      <td>拍摄前后摄像头切换、灯光的控制。</td>
      <td style="text-align:center">&#10003;</td>
      <td style="text-align:center">&#10003;</td>
   </tr>
	 <tr>
	    <td>时长设置</td>
      <td>自定义拍摄的最短和最长时长。</td>
      <td style="text-align:center">&#10003;</td>
      <td style="text-align:center">&#10003;</td>
   </tr>
	 <tr>
      <td>水印</td>
      <td>拍摄支持添加水印。</td>
      <td style="text-align:center">×</td>
      <td style="text-align:center">&#10003;</td>
   </tr>
   <tr>
      <td>焦距</td>
      <td>拍摄支持调节焦距。</td>
      <td style="text-align:center">&#10003;</td>
      <td style="text-align:center">&#10003;</td>
   </tr>
   <tr>
      <td>对焦模式</td>
      <td>支持手动对焦和自动对焦。</td>
      <td style="text-align:center">&#10003;</td>
      <td style="text-align:center">&#10003;</td>
   </tr>
   <tr>
      <td>分段录制</td>
      <td>拍摄过程中可以暂停分段并且可以回删。</td>
      <td style="text-align:center">&#10003;</td>
      <td style="text-align:center">&#10003;</td>
   </tr>
   <tr>
      <td>拍照</td>
      <td>支持拍摄照片。</td>
      <td style="text-align:center">×</td>
      <td style="text-align:center">&#10003;</td>
   </tr>
   <tr>
      <td>变速录制</td>
      <td>拍摄时支持慢速和快速录制。</td>
      <td style="text-align:center">×</td>
      <td style="text-align:center">&#10003;</td>
   </tr>
   <tr>
      <td>背景音乐</td>
      <td>拍摄前可以选择本地的 MP3 作为背景音。</td>
      <td style="text-align:center">×</td>
      <td style="text-align:center">&#10003;</td>
   </tr>
   <tr>
      <td>变声和混响</td>
      <td>拍摄前对录制的声音变声（如萝莉、大叔）和混响效果（如 KTV、会堂）。</td>
      <td style="text-align:center">×</td>
      <td style="text-align:center">&#10003;</td>
   </tr>
	<tr>
      <td>滤镜</td>
      <td>支持实时预览滑动切换滤镜的效果，支持自定义滤镜及设置滤镜程度。</td>
      <td style="text-align:center">&#10003;</td>
      <td style="text-align:center">&#10003;</td>
   </tr>  <tr>
      <td>基础美颜</td>
      <td>拍摄设置人脸的磨皮、美白、红润，并调节强度。</td>
      <td style="text-align:center">&#10003;</td>
      <td style="text-align:center">&#10003;</td>
   </tr>
   <tr>
      <td>高级美颜</td>
      <td>拍摄设置大眼、瘦脸、V 脸、下巴调整、短脸、小鼻效果，并支持调节强度。</td>
      <td style="text-align:center">×</td>
      <td style="text-align:center">×</td>
   </tr>
   <tr>
      <td>动效贴纸</td>
      <td>人脸识别，然后添加变形、覆盖贴纸挂件等效果。</td>
      <td style="text-align:center">×</td>
      <td style="text-align:center">×</td>
   </tr>
   <tr>
      <td>AI 抠图</td>
      <td>识别出人的轮廓，把背景抠除，替换成其他的元素，例如动态背景/PPT 等。</td>
      <td style="text-align:center">×</td>
      <td style="text-align:center">×</td>
   </tr>
   <tr>
      <td>绿幕抠像</td>
      <td>将画面中的绿色元素（例如纯绿背景）抠除，替换成其他的元素，例如动态背景/PPT 等。</td>
      <td style="text-align:center">×</td>
      <td style="text-align:center">×</td>
   </tr>
   <tr>
      <td rowspan='12'>特效编辑</td>
      <td>快速导入</td>
      <td>Android 支持快速导入视频。</td>
      <td style="text-align:center">&#10003;</td>
      <td style="text-align:center">&#10003;</td>
   </tr>
   <tr>
      <td>视频裁剪</td>
      <td>按照给定的时间范围精确裁剪视频。</td>
      <td style="text-align:center">&#10003;</td>
      <td style="text-align:center">&#10003;</td>
   </tr>
   <tr>
      <td>码率设置</td>
      <td>可以指定码率生成视频。</td>
      <td style="text-align:center">&#10003;</td>
      <td style="text-align:center">&#10003;</td>
   </tr>
   <tr>
      <td>获取封面</td>
      <td>根据时间获取帧图像。</td>
      <td style="text-align:center">&#10003;</td>
      <td style="text-align:center">&#10003;</td>
   </tr>
   <tr>
      <td>按帧预览</td>
      <td>移动时间线时，在预览窗口显示基准游标停留的帧图像。</td>
      <td style="text-align:center">&#10003;</td>
      <td style="text-align:center">&#10003;</td>
   </tr>
   <tr>
      <td>滤镜</td>
      <td>给视频添加滤镜，并支持设置滤镜的强度。</td>
      <td style="text-align:center">×</td>
      <td style="text-align:center">&#10003;</td>
   </tr>
   <tr>
      <td>时间特效</td>
      <td>给视频添加倒放、反复、慢动作的时间特效。</td>
      <td style="text-align:center">×</td>
      <td style="text-align:center">&#10003;</td>
   </tr>
   <tr>
      <td>滤镜特效</td>
      <td>给视频添加灵魂出窍、动感光波、分裂、幻影等特效。</td>
      <td style="text-align:center">×</td>
      <td style="text-align:center">&#10003;</td>
   </tr>
   <tr>
      <td>背景音乐</td>
      <td>选择自带声音文件或用户手机本地的 MP3 作为背景音，支持背景音乐的裁剪和设置音量大小。</td>
      <td style="text-align:center">×</td>
      <td style="text-align:center">&#10003;</td>
   </tr>
   <tr>
      <td>动态或者静态贴纸</td>
      <td>添加动态或者静态贴纸，支持设置在视频画面中显示位置和起始时间。</td>
      <td style="text-align:center">×</td>
      <td style="text-align:center">&#10003;</td>
   </tr>
   <tr>
      <td>字幕</td>
      <td>添加字幕，可以选择字幕边框背景的样式，例如气泡等，支持设置在视频画面中显示位置和起始时间。</td>
      <td style="text-align:center">×</td>
      <td style="text-align:center">&#10003;</td>
   </tr>
   <tr>
      <td>图片转场</td>
      <td>导入多张图片，并选择旋转、淡入淡出等转场效果，并生成视频。</td>
      <td style="text-align:center">×</td>
      <td style="text-align:center">&#10003;</td>
   </tr>
   <tr>
      <td rowspan='2'>视频拼接</td>
      <td>多视频拼接</td>
      <td>支持多视频前后拼接。</td>
      <td style="text-align:center">×</td>
      <td style="text-align:center">&#10003;</td>
   </tr>
   <tr>
      <td>跟拍</td>
      <td>支持根据播放的视频进行跟拍，生成双画面视频。</td>
      <td style="text-align:center">×</td>
      <td style="text-align:center">&#10003;</td>
   </tr>
   <tr>
      <td rowspan='1'>视频上传</td>
      <td>上传到云点播</td>
      <td>云点播支持媒资管理、内容审核等功能。</td>
      <td style="text-align:center">&#10003;</td>
      <td style="text-align:center">&#10003;</td>
   </tr>
   <tr>
      <td rowspan='1'>点播播放</td>
      <td>超级播放器</td>
      <td>基于点播播放器实现的集视频信息拉取、横竖屏切换、清晰度选择、弹幕、直播时移等功能于一体的解决方案，且完全开源。</td>
      <td style="text-align:center">&#10003;</td>
      <td style="text-align:center">&#10003;</td>
   </tr>
   <tr>
      <td rowspan='2'>License</td>
      <td>License 申请</td>
      <td>不同版本 SDK 需要搭配不同版本的 License 才能使用。</td>
      <td style="text-align:center"><a href="https://cloud.tencent.com/document/product/1449/56982">精简版 License</a></td>
      <td style="text-align:center"><a href="https://cloud.tencent.com/document/product/1449/56982">基础版 License</a></td>
   <tr>
      <td>套餐价格</td>
      <td>SDK 的一年使用权（精简版和基础版含腾讯云点播流量套餐）。</td>
      <td colspan=2 style="text-align:center"><a href="https://cloud.tencent.com/document/product/1449/56973#video">短视频 License 计费</td>
   </tr>
</table>

> !美颜特效更多高级美颜、动效贴纸、AI 抠图和绿幕抠图的功能能力暂通过原（移动直播/短视频）企业版 SDK 对外售卖，通过购买原移动直播企业版License、短视频企业版 License 或者短视频企业版 Pro License 后，使用对应的功能。详情请参见 [美颜特效功能概述](https://cloud.tencent.com/document/product/1449/58916)。

