腾讯云视立方·播放器 SDK Demo 提供完整的产品级交互界面和业务源码，开发者可按需取用。

## 功能体验 Demo

您可通过下述地址/二维码获得 Demo 进行功能体验。
<style>
.markdown-text-box table th,.markdown-text-box table td{
    text-align: center;
}
/*卡片*/
.preview-demo-section .preview-demo-item {
    display: inline-block;
    width: 226px;
    height: 300px;
    background: #fff;
    box-shadow: 0 1px 8px 0 rgb(156 175 204 / 25%);
    border-radius: 1px;
    text-align: center;
    padding: 0 15px;
    margin: 10px 13px 10px 7px;
    vertical-align: top;
}
/*顶部icon距离卡片上方的尺寸*/
.preview-demo-section .preview-demo-item .demo-item-header {
    margin-top: 30px;
}
/*卡片文字描述字体大小，如web：功能演示·示例代码*/
.preview-demo-section .preview-demo-item .demo-item-desc {
    font-size: 12px;
}
/*web底部链接*/
.preview-demo-section .preview-demo-item .demo-item-link-web {
    font-size: 14px;
	 margin-top: 53px;
}
/*iOS/Android底部链接*/
.preview-demo-section .preview-demo-item .demo-item-link {
    font-size: 14px;
	 margin-top: 5px;
}
/*卡片标题*/
.preview-demo-section .preview-demo-item .demo-item-platform {
    font-size: 20px;
    font-weight: bold;
}
/*卡片顶部icon和标题的距离
.preview-demo-section .preview-demo-item .demo-logo-wrapper {
    line-height: 1;
}
/*顶部icon图标大小*/
.preview-demo-section .preview-demo-item .demo-item-header img {
    box-shadow: none;
    width: 40px;
    height: 40px;
}
/*底部二维码的距离上方位置*/
.preview-demo-section .preview-demo-item.style-qrcode .demo-item-download {
    margin-top: 5px;
}
/*web按钮距离上方位置*/
.preview-demo-section .preview-demo-item.style-web .demo-item-download {
    margin-top: 40px;
}
/*底部二维码大小*/
.preview-demo-section .preview-demo-item .demo-item-download img {
    box-shadow: none;
    width: 110px;
    height: 110px;
}
/*web内部按钮*/
.preview-demo-section .preview-demo-item.style-web .demo-item-download .demo-item-download-btn {
    color: #fff;
		border-radius: 20px;
    background-color: #00a4ff;
    height: 35px;
		width: 170px;
    line-height: 35px;
    margin-bottom: 6px;
		margin: auto;
}
/*内部按钮悬停展示手图标*/
.preview-demo-section .preview-demo-item .demo-item-download .demo-item-download-btn:hover {
    cursor: pointer;
}

</style>

<div class="preview-demo-section" id="demo-card">
 <div class="preview-demo-item style-web">
        <div class="demo-item-header">
            <div class="demo-logo-wrapper">
                <img src="https://qcloudimg.tencent-cloud.cn/raw/ff4dc34a1c72fdb26fc41c1268898025.svg" data-nonescope="true">
            </div>
            <div class="demo-item-platform">Web</div>
        </div>
        <div class="demo-item-desc">
           功能演示 · 示例代码
        </div>
        <div class="demo-item-download">
            <div class="demo-item-download-btn" onclick="window.open('https://tcplayer.vcube.tencent.com/');reportEvent({name: 'demo-click-web', ext1: 'api-sample'});">立即体验</div>
        </div>
				<div class="demo-item-link-web">
				<a href="https://cloud.tencent.com/document/product/881/77877">集成指引</a>
        </div>
	 </div>
	 <div class="preview-demo-item style-qrcode">
        <div class="demo-item-header">
            <div class="demo-logo-wrapper">
                <img src="https://qcloudimg.tencent-cloud.cn/raw/36154dc8bb7c93826dbdc6fdcec4e194.svg" data-nonescope="true">
            </div>
            <div class="demo-item-platform">iOS</div>
        </div>
        <div class="demo-item-desc">
           影视剧集 · 短视频· Feed流
        </div>
        <div class="demo-item-download">
            <img src="https://qcloudimg.tencent-cloud.cn/raw/52c58077ac1f0f35b505324fbb7080a5.png">
        </div>
								<div class="demo-item-link">
				<a href="https://github.com/LiteAVSDK/Player_iOS">Demo 源码</a>
				 <a style="margin-left: 10px;" href="https://cloud.tencent.com/document/product/881/77878">集成指引</a>
        </div>
    </div>
    <div class="preview-demo-item style-qrcode" style="margin-left:0">
        <div class="demo-item-header">
            <div class="demo-logo-wrapper">
                <img src="https://qcloudimg.tencent-cloud.cn/raw/53be7f245c4d11d3aefcb6dc53918757.svg" data-nonescope="true">
            </div>
            <div class="demo-item-platform">Android</div>
        </div>
        <div class="demo-item-desc">
           影视剧集 · 短视频· Feed流
        </div>
        <div class="demo-item-download">
            <img src="https://main.qcloudimg.com/raw/6790ddaf4ffe4afd0ceb96b309a16496.png">
        </div>
					<div class="demo-item-link">
				<a href="https://github.com/LiteAVSDK/Player_Android">Demo 源码</a>
				 <a style="margin-left: 10px;" href="https://cloud.tencent.com/document/product/881/77881">集成指引</a>
        </div>
				 </div>		
    </div>
    </div>
</div> 


### Web端（TCPlayer）

Web 端播放器支持 PC 端和移动端的浏览器视频播放，[Web 播放器 Demo](https://tcplayer.vcube.tencent.com/) 提供了可对比查看视频播放功能效果及其配套代码的 Demo 体验页面，您可以通过修改示例代码，即时的在播放区域内查看修改后的功能效果。
![](https://qcloudimg.tencent-cloud.cn/raw/14a24cd718e2f3c6350a04622298699f.png)

> ? 通过腾讯云账号/手机/邮箱登录后即可体验。

### 移动端

腾讯云音视频 App 是腾讯云音视频开发的集多款产品及功能于一身的最佳体验方案，您可根据自身需求选择相应功能进行体验。

**体验路径**： [扫码下载腾讯云音视频 App](https://cloud.tencent.com/document/product/881/20204) - 社交娱乐(底部 Tab) - 视频播放（顶部 Tab）- 视频播放卡片 
- 在 **剧集** 中，您可以体验到常见的影视剧集视频播放场景样式，类似“腾讯视频”的剧集选择及播放场景。
- 在 **热点** 中，您可以体验到类似“腾讯新闻”的 Feed 流播放场景。
- 在 **发现** 中，您可以体验到类似“腾讯微视”的沉浸式短视频播放场景。
<img src="https://qcloudimg.tencent-cloud.cn/raw/ff683370629f327b2520f6206fb8cefd.png" width=80%>

## 开发调试 Demo 

为了帮助开发者更好的理解播放器 SDK 的使用方式，播放器 SDK 移动端提供了可供开发调试的 Demo 源代码及接口使用说明，您可参考下述步骤使用。 
![](https://qcloudimg.tencent-cloud.cn/raw/21a5d9960d4b4af39938d6997dac2f8c.png)


### 步骤一：获取 Demo 工程源码

您可访问下述 GitHub 地址获取调试 Demo 源代码，或者下载对应的 ZIP 包。

| 平台    | 源码地址                                              | ZIP 包下载                                                   |
| ------- | ----------------------------------------------------- | ------------------------------------------------------------ |
| iOS     | [GitHub](https://github.com/LiteAVSDK/Player_iOS)     | [ZIP 包](https://liteav.sdk.qcloud.com/download/latest/TXLiteAVSDK_Player_iOS_latest.zip) |
| Android | [GitHub](https://github.com/LiteAVSDK/Player_Android) | [ZIP 包](https://liteav.sdk.qcloud.com/download/latest/TXLiteAVSDK_Player_Android_latest.zip) |
| Flutter | [GitHub](https://github.com/LiteAVSDK/Player_Flutter) | -                                                            |

### 步骤二：配置 License

播放器 SDK 移动端（ iOS & Android & Flutter）需获取 License 后方可使用。
1. 登录 [腾讯云视立方控制台](https://console.cloud.tencent.com/vcube/mobile)，在左侧菜单中选择 **License 管理** > **移动端 License**，单击**新建测试 License**。 
![](https://qcloudimg.tencent-cloud.cn/raw/5005c15ecc868621f077357847f12957.png)
2. 根据实际需求填写 `App Name`、`Package Name` 和 `Bundle ID`，勾选功能模块 **视频播放**，单击**确定**。
 - **Package Name**：请在 App 目录下的 **build.gradle** 文件查看 **applicationId** 。
 - **Bundle ID**：请在 **xcode** 中查看项目的 **Bundle Identifier** 。
 > ! 如果在腾讯云控制台申请 Package Name 或 Bundle ID ，和工程中实际的 Package Name 或 Bundle ID 不一致，将会播放失败。

 ![](https://qcloudimg.tencent-cloud.cn/raw/02149b53f71f8deb9ab373890a172728.png)

3. 测试版 License 成功创建后，页面会显示生成的 License 信息。**在 SDK 初始化配置时需要传入 License URL 和 License Key 两个参数，请妥善保存以下信息。**
![](https://qcloudimg.tencent-cloud.cn/raw/e13b6129902cd8435f351f39f5779abf.png)

4. 获取到 Licence URL 和 Licence Key 后，请参考下面的教程把它们配置到 Demo 工程。
<dx-tabs>
::: Android 端配置 Licence
打开 Demo/app/src/main/java/com/tencent/liteav/demo/TXCSDKService.java 文件， 把 Licence URL 和 License Key 替换成申请到的 Licence 内容。
![](https://qcloudimg.tencent-cloud.cn/raw/211621c3fb8f4bb4b0a266ad48e5006a.png)
:::
::: iOS 端配置 Licence
打开 Demo/TXLiteAVDemo/App/config/Player.plist 文件， 把 Licence URL 和 Licence Key 替换成申请到的 Licence 内容。
![](https://qcloudimg.tencent-cloud.cn/raw/5aa5ff4527ec77117b78afa5adeb751b.png)
:::
::: Flutter 端配置 Licence
打开 Flutter/example/lib/main.dart 文件， 把 Licence URL 和 Licence Key 替换成申请到的 Licence 内容。
![](https://qcloudimg.tencent-cloud.cn/raw/3b8854fe0f482f61cafb3b0586338137.png)
:::
</dx-tabs>
