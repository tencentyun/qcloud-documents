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
	 margin-top: 55px;
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
腾讯云视立方·播放器 SDK Demo 提供完整的产品级交互界面和业务源码，开发者可按需取用。
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
            <img src="https://qcloudimg.tencent-cloud.cn/raw/728d7f5fb63e5790ea3555e5940ef446.png">
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
