<style>
    .card-container {
        width: 380px;
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

## 组件介绍
TUICallKit 是腾讯云推出一款音视频通话 UI 组件，通过集成该组件，您只需要编写几行代码就可以为您的 App 添加音视频通话功能，并且支持离线唤起能力。TUICallKit 支持 Android、iOS、Web、小程序、Flutter、UniApp 等多个开发平台，基本功能如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/08f914b45857743fd05dfaa28e2adb72.png)

>! **基于开发者反馈和市场需求调研，2022年08月 TUICalling 正式升级为 TUICallKit，新的组件升级了群内多人通话和离线唤醒等功能，并且配备了更低折扣的 TRTC 联合套餐包以及7天的免费试用期，期待您的关注！**

#### 功能优势
- 接入方便：提供带 UI 的开源组件，节省90%开发时间，快速上线音视频通话应用。
- 平台互通：各平台的 TUICallKit 组件支持相互拨打、接听、挂断等，互联互通。
- 多人通话：不仅仅支持1对1视频通话，还支持在群组内发起多人视频通话。
- 离线推送：支持Android&iOS离线推送，被叫用户 App 不在线时也能收到新的来电消息。

#### 适用场景
两人或多人进行音视频通话，覆盖游戏社交、在线客服、视频客服、在线问诊、保险咨询等场景。

## 服务开通
**新版本的视频通话 SDK 需要配合专属的音视频通话套餐**，新的套餐整合了腾讯云[实时音视频 TRTC](https://cloud.tencent.com/document/product/647/16788) 和 [即时通信 IM](https://cloud.tencent.com/document/product/269/42440) 两个基础的 PaaS 服务，您可以通过在即时通信 IM 控制台一站式解锁 **即时通信 IM** 功能及其专属的**音视频通话能力**，详细的解锁流程请参考各平台：**快速接入 TUICallKit**。

### 音视频通话套餐详情
<table>
  <tr>
    <th width="100px" style="text-align:center">功能模块</th>
    <th width="100px" style="text-align:center">功能详情</th>
    <th width="100px" style="text-align:center"> 体验版</th>
    <th width="100px" style="text-align:center"> 基础版</th>
	  <th width="100px" style="text-align:center"> 进阶版</th>
    <th width="100px" style="text-align:center"> 尊享版</th>
  </tr>
   <td rowspan='16' style="text-align:center">音视频通话 TUICallKit </td>
   </tr>
	  <td style="text-align:left">微信同款UI设计</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">&#10003;</td>
		<td style="text-align:center">&#10003;</td>
    <td style="text-align:center">&#10003;</td>
  </tr>
	<tr>
    <td style="text-align:left">通话状态展示</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">&#10003;</td>
		<td style="text-align:center">&#10003;</td>
    <td style="text-align:center">&#10003;</td>
  </tr>
	<tr>
    <td style="text-align:left">通话呼叫通知</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">&#10003;</td>
		<td style="text-align:center">&#10003;</td>
    <td style="text-align:center">&#10003;</td>
  </tr>
	<tr>
    <td style="text-align:left">通话悬浮窗</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">&#10003;</td>
		<td style="text-align:center">&#10003;</td>
    <td style="text-align:center">&#10003;</td>
  </tr>
	 <tr>
    <td style="text-align:left">自定义呼叫铃声</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">&#10003;</td>
		<td style="text-align:center">&#10003;</td>
    <td style="text-align:center">&#10003;</td>
  </tr>
	<tr>
    <td style="text-align:left">通话呼叫/接听/拒绝/挂断</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">&#10003;</td>
		<td style="text-align:center">&#10003;</td>
    <td style="text-align:center">&#10003;</td>
  </tr>
  <tr>
    <td style="text-align:left">群组通话</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
		<td style="text-align:center">&#10003;</td>
    <td style="text-align:center">&#10003;</td>
  </tr>
  <tr>
    <td style="text-align:left">中途呼叫/加入三方通话</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
		<td style="text-align:center">&#10003;</td>
    <td style="text-align:center">&#10003;</td>
  </tr>
  <tr>
    <td style="text-align:left">视频通话切换语音通话</td>
    <td style="text-align:center">&#10003;</td>
    <td style="text-align:center">&#10003;</td>
		<td style="text-align:center">&#10003;</td>
    <td style="text-align:center">&#10003;</td>
  </tr>
  <tr>
    <td style="text-align:left">多端登录通话</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
		<td style="text-align:center">-</td>
    <td style="text-align:center">&#10003;</td>
  </tr>
  <tr>
    <td style="text-align:left">同平台多端登录通话</td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
		<td style="text-align:center">-</td>
    <td style="text-align:center">&#10003;</td>
  </tr>
  <tr>
    <td style="text-align:left"> AI 降噪 </td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
		<td style="text-align:center">&#10003;</td>
    <td style="text-align:center">&#10003;</td>
	<tr>
    <td style="text-align:left"> 弱网通话卡顿优化 </td>
    <td style="text-align:center">-</td>
    <td style="text-align:center">-</td>
		<td style="text-align:center">&#10003;</td>
    <td style="text-align:center">&#10003;</td>
   <tr>
    <td   colspan="1" rowspan="1" align="" valign="middle"><p>支持平台</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p>iOS、Android、Web、微信小程序、uni-app、Flutter（即将上线）</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p>iOS、Android、Web、<strong>微信小程序（限时活动）</strong>、uni-app、Flutter（即将上线）</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p>iOS、Android、Web、微信小程序、uni-app、Flutter（即将上线）</p></td>
 <td   colspan="1" rowspan="1" align="" valign="middle"><p>iOS、Android、Web、微信小程序、uni-app、Flutter（即将上线）</p></td>
</table>

## TUICallKit  下载

<div style="position: relative; box-sizing: border-box;  padding-bottom: 10px; margin-bottom: 10px; overflow:hidden">
	<div class="card-container">
			<div class="card">
					 <img src="https://main.qcloudimg.com/raw/b0211b0870806899009a17a4216ea65c.svg" data-nonescope="true">
					<p class="titlename">Android TUICallKit</p>
					<p style="color:#586376;">类“微信” UI，支持 1V1 通话、群组通话、悬浮窗、离线推送等特性，功能强大。</p>
					<a style="margin-left: 10px;" href="https://github.com/tencentyun/TUICalling"><b>Github </b></a>
					<a style="margin-left: 10px;" href="https://cloud.tencent.com/document/product/647/78729"><b>快速接入</b></a>
					<a style="margin-left: 10px;" href="https://cloud.tencent.com/document/product/647/78748"><b>API 参考</b></a>
					<a style="margin-left: 10px;" href="https://cloud.tencent.com/document/product/647/78767"><b>常见问题</b></a>
			</div>
	</div>
	<div class="card-container">
			<div class="card">
					 <img src="https://main.qcloudimg.com/raw/613f2e15bed7c8297110676b52784b71.svg" data-nonescope="true">
					<p class="titlename">iOS TUICallKit</p>
					<p style="color:#586376;">类“微信” UI，支持 1V1 通话、群组通话、悬浮窗、离线推送等特性，功能强大。</p>
					<a style="margin-left: 10px;" href="https://github.com/tencentyun/TUICalling"><b>Github </b></a>
					<a style="margin-left: 10px;" href="https://cloud.tencent.com/document/product/647/78730"><b>快速接入</b></a>
					<a style="margin-left: 10px;" href="https://cloud.tencent.com/document/product/647/78752"><b>API 参考</b></a>
					<a style="margin-left: 10px;" href="https://cloud.tencent.com/document/product/647/78768"><b>常见问题</b></a>
			</div>
	</div>
	<div class="card-container">
			<div class="card">
					 <img src="https://main.qcloudimg.com/raw/7e2651085e3e3c6e32190e401a6dfd32.svg" data-nonescope="true">
					<p class="titlename">Web TUICallKit</p>
					<p style="color:#586376;">类“微信” UI，支持 1V1 通话、群组通话、悬浮窗、离线推送等特性，功能强大。</p>
					<a style="margin-left: 10px;" href="https://github.com/tencentyun/TUICalling"><b>Github </b></a>
					<a style="margin-left: 10px;" href="https://cloud.tencent.com/document/product/647/78731"><b>快速接入</b></a>
					<a style="margin-left: 10px;" href="https://cloud.tencent.com/document/product/647/78756"><b>API 参考</b></a>
					<a style="margin-left: 10px;" href="https://cloud.tencent.com/document/product/647/78769"><b>常见问题</b></a>
			</div>
	</div>
	<div class="card-container">
			<div class="card">
					 <img src="https://main.qcloudimg.com/raw/af07e321883032c9796848d189a80f5e.png" data-nonescope="true">
					<p class="titlename">小程序 TUICallKit</p>
					<p style="color:#586376;">类“微信” UI，支持 1V1 通话、群组通话、悬浮窗、离线推送等特性，功能强大。</p>
					<a style="margin-left: 10px;" href="https://github.com/tencentyun/TUICalling"><b>Github </b></a>
					<a style="margin-left: 10px;" href="https://cloud.tencent.com/document/product/647/78733"><b>快速接入</b></a>
					<a style="margin-left: 10px;" href="https://cloud.tencent.com/document/product/647/78759"><b>API 参考</b></a>
					<a style="margin-left: 10px;" href="https://cloud.tencent.com/document/product/647/78770"><b>常见问题</b></a>
			</div>
	</div>
	<div class="card-container">
			<div class="card">
					 <img src="https://main.qcloudimg.com/raw/e9d18b164152f08bc0694c01e966daea.png" data-nonescope="true">
					<p class="titlename">uni-app（客户端） TUICallKit</p>
					<p style="color:#586376;">类“微信” UI，支持 1V1 通话、群组通话、悬浮窗、离线推送等特性，功能强大。</p>
					<a style="margin-left: 10px;" href="https://github.com/tencentyun/TUICalling"><b>Github </b></a>
					<a style="margin-left: 10px;" href="https://cloud.tencent.com/document/product/647/78732"><b>快速接入</b></a>
					<a style="margin-left: 10px;" href="https://cloud.tencent.com/document/product/647/78762"><b>API 参考</b></a>
			</div>
	</div>
	 <div class="card-container">
			<div class="card">
					 <img src="https://main.qcloudimg.com/raw/e9d18b164152f08bc0694c01e966daea.png" data-nonescope="true">
					<p class="titlename">uni-app（小程序） TUICallKit</p>
					<p style="color:#586376;">类“微信” UI，支持 1V1 通话、群组通话、悬浮窗、离线推送等特性，功能强大。</p>
					<a style="margin-left: 10px;" href="https://github.com/TencentCloud/TIMSDK"><b>Github </b></a>
					<a style="margin-left: 10px;" href="https://cloud.tencent.com/document/product/647/78912"><b>快速接入</b></a>
					<a style="margin-left: 10px;" href="https://cloud.tencent.com/document/product/647/78759"><b>API 参考</b></a>
			</div>
	</div>
</div>

## 开源建设
您可以在 [**这里**](https://github.com/tencentyun/TUICalling/tree/open) 找到升级前的 TUICalling 开源项目。
