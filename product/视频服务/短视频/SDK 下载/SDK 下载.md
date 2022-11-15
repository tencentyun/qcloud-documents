<style>
    .card-container {
        width: 350px;
        display: block;
        float: left;
        padding-left: 15px;
        padding-right: 15px;
        box-sizing: border-box;
    } 

    .card {
        border-radius: 10px;
        padding-top: 10px;
        padding-left: 10px;
        padding-right: 10px;
        padding-bottom: 10px;
        margin-top: 30px;
        border: 1px solid #ebeef5;
        background-color: #fff;
        overflow: hidden;
        box-shadow: 0 2px 12px 0 rgb(0 0 0 / 10%);
        text-align: center;
    }

    .markdown-text-box img {
        box-shadow: none;
    }


    .titlename {
                color:#191919;
        position: relative;
        top: -2px;
                font-weight: bolder;
                font-size: larger;
    }
        
        @media (max-width: 768px){
                .card-container,
                .scene-card-container{
                        width: 100%;
                }
                .scene-card > div{
                        width: 100%!important;
                        margin-left: 0!important;
                }
                img {
        box-shadow: none;
    }
        }
</style>

短视频 SDK 是腾讯云视立方产品家族的子产品之一，提供短视频的采集、剪辑、拼接、特效、播放、分享等功能。
您可以在 [产品功能](https://cloud.tencent.com/document/product/584/72408) 中查看 SDK 支持的功能清单，在 [Demo 体验](https://cloud.tencent.com/document/product/584/9457) 中获取 Demo 及其源码，在本页面中下载各端 SDK 。

## 短视频SDK下载
<div style="position: relative; box-sizing: border-box;  padding-bottom: 10px; margin-bottom: 10px; overflow:hidden">
		<div class="card-container">
				<div class="card">
						<img src="https://main.qcloudimg.com/raw/613f2e15bed7c8297110676b52784b71.svg" data-nonescope="true">
						<p class="titlename">iOS 短视频 SDK</p>
						<p style="color:#586376;">提供短视频采集、剪辑、拼接、特效、分享、播放等功能。</p>
						<a href="https://liteav.sdk.qcloud.com/download/latest/TXLiteAVSDK_UGC_iOS_latest.zip">ZIP 下载</a>
						<a style="margin-left: 10px;" href="https://cloud.tencent.com/document/product/584/11638">集成指引</a>
						<a style="margin-left: 10px;" href="https://cloud.tencent.com/document/product/584/9457">Demo 源码</a>
				</div>
		</div>
		<div class="card-container">
				<div class="card">
						<img class="icon" src="https://main.qcloudimg.com/raw/b0211b0870806899009a17a4216ea65c.svg" data-nonescope="true">
						<p class="titlename">Android 短视频 SDK</p>
						<p style="color:#586376;">提供短视频采集、剪辑、拼接、特效、分享、播放等功能。</p>
						<a href="https://liteav.sdk.qcloud.com/download/latest/TXLiteAVSDK_UGC_Android_latest.zip">ZIP 下载</a>
						<a style="margin-left: 10px;" href="https://cloud.tencent.com/document/product/584/11631">集成指引</a>
						<a style="margin-left: 10px;" href="https://cloud.tencent.com/document/product/584/9457">Demo 源码</a>
				</div>
		</div>
</div>

## 功能版本详情
使用短视频 SDK 需要购买短视频 License，详情参见 [价格总览](https://cloud.tencent.com/document/product/584/9368)，短视频License分为精简版和基础版，不同版本支持功能如下表。

>! 短视频 SDK 仅有一个版本，精简版 License 和 基础版 License 解锁的是同一个短视频 SDK 中的不同功能。


<table>
   <tbody><tr>
      <th width="40px" style="text-align:center">功能模块</th>
      <th width="85px" style="text-align:center">功能项</th>
      <th width="210px" style="text-align:center">功能简介</th>
      <th width="70px" style="text-align:center">精简版 License</th>
      <th width="70px" style="text-align:center">基础版 License</th>
   </tr>
        <tr>
			<td rowspan=2>SDK 下载</td>
			<td>iOS</td>
			<td>短视频 SDK（LiteAVSDK）+ Demo 源代码</td>
			<td colspan=2 style="text-align:center"><a href="https://liteav.sdk.qcloud.com/download/latest/TXLiteAVSDK_UGC_iOS_latest.zip">iOS SDK 下载</a></td>
			</tr>
			<tr>
			<td>Android</td>
			<td>短视频 SDK（LiteAVSDK）+ Demo 源代码</td>
			<td colspan=2 style="text-align:center"><a href="https://liteav.sdk.qcloud.com/download/latest/TXLiteAVSDK_UGC_Android_latest.zip">Android SDK 下载</a></td>
			</tr>
			<tr>
			<td rowspan=3>License</td>
			<td>License 申请</td>
			<td>短视频 SDK 需购买 License 后方可使用，不同 License 可解锁的功能不同</td>
			<td style="text-align:center"><a href="https://cloud.tencent.com/document/product/584/20333#.E8.B4.AD.E4.B9.B0.E6.AD.A3.E5.BC.8F.E7.89.88-license">精简版 License</a></td>
			<td style="text-align:center"><a href="https://cloud.tencent.com/document/product/584/20333#.E8.B4.AD.E4.B9.B0.E6.AD.A3.E5.BC.8F.E7.89.88-license">基础版 License</a></td>
			</tr>
			<tr>
			<td rowspan=2>License 价格</td>
			<td>购买方式1：<a href="https://cloud.tencent.com/document/product/584/9368#.E8.B5.84.E6.BA.90.E5.8C.85.E4.BB.B7.E6.A0.BC">购买云点播流量包赠送 License</a></td>
			<td style="text-align:center">￥1699元/年</td>
			<td style="text-align:center">￥8399元/年</td>
			</tr>
	    <tr>
	 		<td>购买方式2：<a href="https://cloud.tencent.com/document/product/584/9368#.E7.8B.AC.E7.AB.8B-license-.E4.BB.B7.E6.A0.BC">直接购买独立 License</a></td>
      <td style="text-align:center">￥3299元/年</td>
      <td style="text-align:center">￥16699元/年</td>
   </tr>
        <tr>
      <td rowspan="3">美颜特效<br>（增值能力）</td>
      <td>高级美颜</td>
      <td>拍摄设置大眼、瘦脸、V 脸、下巴调整、短脸、小鼻效果，并支持调节强度</td>
      <td style="text-align:center" rowspan="3" colspan="2">美颜特效相关功能为增值能力，短视频 SDK 不支持此功能。若需结合使用，请购买腾讯特效 SDK 套餐包，解锁腾讯特效（美颜特效）功能模块。
          <li><a href="https://cloud.tencent.com/product/x-magic">了解腾讯特效 SDK</a>
          </li><li><a href="https://cloud.tencent.com/document/product/616/36807">腾讯特效 SDK 价格总览</a>
          </li><li><a href="https://buy.cloud.tencent.com/vcube?type=magic">购买腾讯特效 SDK</a>
          </li><li><a href="https://cloud.tencent.com/document/product/616/65885">腾讯特效 SDK 集成至短视频 SDK 指引</a></li></td>
</tr>
<tr>
<td>动效贴纸</td>
<td>定位五官位置，然后添加变形、覆盖贴纸挂件等效果</td>
</tr>
<tr>
<td>人像分割</td>
<td>识别出背景轮廓，把背景抠除，替换成素材视频的元素</td>
</tr>
 <tr>
      <td>界面</td>
      <td>自定义 UI</td>
      <td>开发者自定义 UI，小视频 App 提供了一套完整的 UI 交互源码，可复用或自定义</td>
      <td style="text-align:center">&#10003;</td>
      <td style="text-align:center">&#10003;</td>
   </tr>
   <tr>
      <td rowspan="14">采集拍摄</td>
      <td>屏比</td>
      <td>支持16:9、4:3、1:1多种屏比拍摄</td>
      <td style="text-align:center">&#10003;</td>
      <td style="text-align:center">&#10003;</td>
   </tr>
   <tr>
      <td>清晰度</td>
      <td>支持标清、高清、超清拍摄，支持自定义码率、帧率、GOP</td>
      <td style="text-align:center">&#10003;</td>
      <td style="text-align:center">&#10003;</td>
   </tr>
   <tr>
      <td>拍摄控制</td>
      <td>拍摄前后摄像头切换、灯光的控制</td>
      <td style="text-align:center">&#10003;</td>
      <td style="text-align:center">&#10003;</td>
   </tr>
   <tr>
      <td>时长设置</td>
      <td>自定义拍摄的最短和最长时长</td>
      <td style="text-align:center">&#10003;</td>
      <td style="text-align:center">&#10003;</td>
   </tr>
   <tr>
      <td>水印</td>
      <td>拍摄支持添加水印</td>
      <td style="text-align:center">×</td>
      <td style="text-align:center">&#10003;</td>
   </tr>
   <tr>
      <td>焦距</td>
      <td>拍摄支持调节焦距</td>
      <td style="text-align:center">&#10003;</td>
      <td style="text-align:center">&#10003;</td>
   </tr>
   <tr>
      <td>对焦模式</td>
      <td>支持手动对焦和自动对焦</td>
      <td style="text-align:center">&#10003;</td>
      <td style="text-align:center">&#10003;</td>
   </tr>
   <tr>
      <td>分段录制</td>
      <td>拍摄过程中可以暂停分段并且可以回删</td>
      <td style="text-align:center">&#10003;</td>
      <td style="text-align:center">&#10003;</td>
   </tr>
   <tr>
      <td>拍照</td>
      <td>支持拍摄照片</td>
      <td style="text-align:center">×</td>
      <td style="text-align:center">&#10003;</td>
   </tr>
   <tr>
      <td>变速录制</td>
      <td>拍摄时支持慢速和快速录制</td>
      <td style="text-align:center">×</td>
      <td style="text-align:center">&#10003;</td>
   </tr>
   <tr>
      <td>背景音乐</td>
      <td>拍摄前可以选择本地的 MP3 作为背景音</td>
      <td style="text-align:center">×</td>
      <td style="text-align:center">&#10003;</td>
   </tr>
   <tr>
      <td>变声和混响</td>
      <td>拍摄前对录制的声音变声（如萝莉、大叔）和混响效果（如 KTV、会堂）</td>
      <td style="text-align:center">×</td>
      <td style="text-align:center">&#10003;</td>
   </tr>
   <tr>
      <td>滤镜</td>
      <td>支持实时预览滑动切换滤镜的效果，支持自定义滤镜及设置滤镜程度</td>
      <td style="text-align:center">&#10003;</td>
      <td style="text-align:center">&#10003;</td>
   </tr><tr>
      <td>基础美颜</td>
      <td>拍摄设置面部磨皮、美白、红润并调节强度</td>
      <td style="text-align:center">&#10003;</td>
      <td style="text-align:center">&#10003;</td>
   </tr>
  <tr>
      <td rowspan="12">特效编辑</td>
      <td>快速导入</td>
      <td>Android 支持快速导入视频</td>
      <td style="text-align:center">&#10003;</td>
      <td style="text-align:center">&#10003;</td>
   </tr>
   <tr>
      <td>视频裁剪</td>
      <td>按照给定的时间范围精确裁剪视频</td>
      <td style="text-align:center">&#10003;</td>
      <td style="text-align:center">&#10003;</td>
   </tr>
   <tr>
      <td>码率设置</td>
      <td>可以指定码率生成视频</td>
      <td style="text-align:center">&#10003;</td>
      <td style="text-align:center">&#10003;</td>
   </tr>
   <tr>
      <td>获取封面</td>
      <td>根据时间获取帧图像</td>
      <td style="text-align:center">&#10003;</td>
      <td style="text-align:center">&#10003;</td>
   </tr>
   <tr>
      <td>按帧预览</td>
      <td>移动时间线时，在预览窗口显示基准游标停留的帧图像</td>
      <td style="text-align:center">&#10003;</td>
      <td style="text-align:center">&#10003;</td>
   </tr>
   <tr>
      <td>滤镜</td>
      <td>给视频添加滤镜，并支持设置滤镜的强度</td>
      <td style="text-align:center">×</td>
      <td style="text-align:center">&#10003;</td>
   </tr>
   <tr>
      <td>时间特效</td>
      <td>给视频添加倒放、反复、慢动作的时间特效</td>
      <td style="text-align:center">×</td>
      <td style="text-align:center">&#10003;</td>
   </tr>
   <tr>
      <td>滤镜特效</td>
      <td>给视频添加灵魂出窍、动感光波、分裂、幻影等特效</td>
      <td style="text-align:center">×</td>
      <td style="text-align:center">&#10003;</td>
   </tr>
   <tr>
      <td>背景音乐</td>
      <td>选择自带声音文件或用户手机本地的 MP3 作为背景音，支持背景音乐的裁剪和设置音量大小</td>
      <td style="text-align:center">×</td>
      <td style="text-align:center">&#10003;</td>
   </tr>
   <tr>
      <td>动态或者静态贴纸</td>
      <td>添加动态或者静态贴纸，支持设置在视频画面中显示位置和起始时间</td>
      <td style="text-align:center">×</td>
      <td style="text-align:center">&#10003;</td>
   </tr>
   <tr>
      <td>字幕</td>
      <td>添加字幕，可以选择字幕边框背景的样式，例如气泡等，支持设置在视频画面中显示位置和起始时间</td>
      <td style="text-align:center">×</td>
      <td style="text-align:center">&#10003;</td>
   </tr>
   <tr>
      <td>图片转场</td>
      <td>导入多张图片，并选择旋转、淡入淡出等转场效果，并生成视频</td>
      <td style="text-align:center">×</td>
      <td style="text-align:center">&#10003;</td>
   </tr>
   <tr>
      <td rowspan="2">视频拼接</td>
      <td>多视频拼接</td>
      <td>支持多视频前后拼接</td>
      <td style="text-align:center">×</td>
      <td style="text-align:center">&#10003;</td>
   </tr>
   <tr>
      <td>跟拍</td>
      <td>支持根据播放的视频进行跟拍，生成双画面视频</td>
      <td style="text-align:center">×</td>
      <td style="text-align:center">&#10003;</td>
   </tr> <tr>
      <td rowspan="1">视频上传</td>
      <td>上传到腾讯云点播</td>
      <td>腾讯云点播支持媒资管理、内容审核等功能</td>
      <td style="text-align:center">&#10003;</td>
      <td style="text-align:center">&#10003;</td>
   </tr><tr>
      <td rowspan="1">点播播放</td>
      <td>超级播放器</td>
      <td>基于点播播放器实现的集视频信息拉取、横竖屏切换、清晰度选择、弹幕、直播时移等功能于一体的解决方案，且完全开源</td>
      <td style="text-align:center">&#10003;</td>
      <td style="text-align:center">&#10003;</td>
   </tr>
   </tbody></table>


>? **如果您对 SDK 支持的功能还有疑问，请参见 [功能答疑](https://cloud.tencent.com/document/product/584/17535)。**
