## 组件介绍

TUICallKit 是腾讯云最新推出一款音视频通话 UI 组件，通过集成该组件，您只需要编写几行代码就可以为您的 App 添加音视频通话功能，并且支持离线唤起能力。TUICallKit 支持 Android、iOS、Web、微信小程序、Flutter、UniApp 等多个开发平台，基本功能如下图所示：

![](https://qcloudimg.tencent-cloud.cn/raw/08f914b45857743fd05dfaa28e2adb72.png)

> ?**在 6.5.xxxx 版本以后，TUIKit 组件升级了音视频通话功能，采用了全新的 TUICallKit，新的 TUICallKit  升级了群内多人通话、中途加人、离线唤醒等多个功能**。

### 使用说明
TUICallKit 属于 IM 增值服务之一，需要您单独开通/购买后使用，免费体验&购买方法可参见 [开通音视频通话能力](#step1) ，价格与功能说明可参见 [音视频通话能力版本说明](#step2) 。

### 功能优势
- 接入方便：提供带 UI 的开源组件，节省90%开发时间，快速上线音视频通话应用。
- 平台互通：各平台的 TUICallKit 组件支持相互拨打、接听、挂断等，互联互通。
- 多人通话：不仅仅支持1对1视频通话，还支持在群组内发起多人视频通话。
- 离线推送：支持 Android & iOS 离线推送，被叫用户 App 不在线时也能收到新的来电消息。
- 更多功能：弱网环境通话卡顿优化、AI 降噪能力、通话悬浮窗，美颜设置，视频渲染参数设置等等。

### 适用场景
两人或多人进行音视频通话，覆盖游戏社交、在线客服、视频客服、在线问诊、保险咨询等场景。

更多音视频通话能力的功能说明可参见 [音视频通话常见问题](https://cloud.tencent.com/document/product/269/83725)。

[](id:step1)
## 开通音视频通话能力
1. 登录 [即时通信 IM 控制台](https://console.cloud.tencent.com/im) ，单击目标应用卡片，进入应用的基础配置页面。
2. 在页面的右下角找到**腾讯实时音视频服务 TRTC** 功能区。
 - 若您需要体验音视频通话功能，可单击卡片内的 **免费体验** 开通 TUICallKit 的 7 天免费试用服务。
<img width="690" alt="image" src="https://qcloudimg.tencent-cloud.cn/raw/a7caebe5a773c93fb23d00b4488003b1.png"> 
 - 您可参见 [音视频通话能力版本说明](#step2) 确认所需要使用的版本，单击 **[购买正式版](https://buy.cloud.tencent.com/avc)**  以购买正式的音视频通话能力。在购买页内的增值服务中勾选“音视频通话能力”，并选择所需版本即可。
<img width="691" alt="image" src="https://qcloudimg.tencent-cloud.cn/raw/c0d6f96d96a1d10a6422f143b620c94b.png"> 
<img width="1249" alt="image" src="https://qcloudimg.tencent-cloud.cn/raw/79e1c65b1cc44442b9f83ea2f62e7683.png"> 



[](id:step2)
## 音视频通话能力版本说明

<table>
<thead>
<tr>
<th colspan=2 style = "text-align:center">对比项</th>
<th style = "text-align:center;width:19%;">体验版</th>
<th style = "text-align:center;width:19%;">1v1 通话版</th>
<th style = "text-align:center;width:19%;">群组通话版-38万分钟</th>
<th style = "text-align:center;width:19%;">群组通话版-140万分钟</th>
</tr>
</thead>
<tbody><tr>
<td style="text-align: center" rowspan=2>价格</td>
<td>限时8折优惠</td>
<td style="text-align: center">0元/7天</td>
<td style="text-align: center">500元/月<br><a href="https://buy.cloud.tencent.com/avc?addRavLicense=1">立即选购</a></td>
<td style="text-align: center">1500元/月<br><a href="https://buy.cloud.tencent.com/avc?addRavLicense=1">立即选购</a></td>
<td style="text-align: center">5000元/月<br><a href="https://buy.cloud.tencent.com/avc?addRavLicense=1">立即选购</a></td>
</tr>
<tr>
<td>刊例价</td>
<td style="text-align: center">0元/7天</td>
<td style="text-align: center"><del>625</del>元/月</td>
<td style="text-align: center"><del>1875</del>元/月</td>
<td style="text-align: center"><del>6250</del>元/月</td>
</tr>
<tr>
<td colspan=2>开通条件</td>
<td style="text-align: center">IM 为任意版本均可开通</td>
<td style="text-align: center"colspan=3>IM 为专业版或旗舰版时可开通</td>
</tr>
<tr>
<td colspan=2>对应 TRTC 包月套餐</td>
<td style="text-align: center">体验版</td>
<td style="text-align: center">基础版</td>
<td style="text-align: center">尊享版</td>
<td style="text-align: center">旗舰版</td>
</tr>
<tr>
<td colspan=2>赠送音视频时长<br>（仅支持抵扣音视频时长用量）</td>
<td style="text-align: center">-</td>
<td style="text-align: center">11万 分钟/月</td>
<td style="text-align: center">38万 分钟/月</td>
<td style="text-align: center">140万 分钟/月</td>
</tr>
<tr>
<td colspan=2>超出赠送资源部分后付费</td>
<td style="text-align: center" colspan=4>通话时长后付费价格详见 <a href="https://cloud.tencent.com/document/product/647/44248">音视频时长计费说明</a>，DAU 与峰值群组数后付费价格详见 <a href="https://cloud.tencent.com/document/product/269/11673#.E5.9F.BA.E7.A1.80.E6.9C.8D.E5.8A.A1.E8.B5.84.E8.B4.B9.3Ca-id.3D.22jc.22.3E.3C.2Fa.3E">IM计费说明</a> 。</td>
</tr>
<tr>
<td style="text-align: center;width:60px" rowspan=15>通话相关功能</td>
<td>微信同款 UI 设计</td>
<td style="text-align: center">✓</td>
<td style="text-align: center">✓</td>
<td style="text-align: center">✓</td>
<td style="text-align: center">✓</td>
</tr>
<tr>
<td>通话状态展示</td>
<td style="text-align: center">✓</td>
<td style="text-align: center">✓</td>
<td style="text-align: center">✓</td>
<td style="text-align: center">✓</td>
</tr>
<tr>
<td>通话呼叫通知</td>
<td style="text-align: center">✓</td>
<td style="text-align: center">✓</td>
<td style="text-align: center">✓</td>
<td style="text-align: center">✓</td>
</tr>
<tr>
<td>通话悬浮窗</td>
<td style="text-align: center">✓</td>
<td style="text-align: center">✓</td>
<td style="text-align: center">✓</td>
<td style="text-align: center">✓</td>
</tr>
<tr>
<td>自定义呼叫铃声</td>
<td style="text-align: center">✓</td>
<td style="text-align: center">✓</td>
<td style="text-align: center">✓</td>
<td style="text-align: center">✓</td>
</tr>
<tr>
<td>呼叫/接听/拒绝/挂断</td>
<td style="text-align: center">✓</td>
<td style="text-align: center">✓</td>
<td style="text-align: center">✓</td>
<td style="text-align: center">✓</td>
</tr>
<tr>
<td>视频通话切换语音通话</td>
<td style="text-align: center">✓</td>
<td style="text-align: center">✓</td>
<td style="text-align: center">✓</td>
<td style="text-align: center">✓</td>
</tr>
<tr>
<td>群组通话</td>
<td style="text-align: center">✓</td>
<td style="text-align: center">-</td>
<td style="text-align: center">✓</td>
<td style="text-align: center">✓</td>
</tr>
<tr>
<td>中途呼叫/加入三方通话</td>
<td style="text-align: center">✓</td>
<td style="text-align: center">-</td>
<td style="text-align: center">✓</td>
<td style="text-align: center">✓</td>
</tr>
<tr>
<td>多端登录通话</td>
<td style="text-align: center">✓<br>（需配合 IM 旗舰版使用）</td>
<td style="text-align: center">-</td>
<td style="text-align: center">✓<br>（需配合 IM 旗舰版使用）</td>
<td style="text-align: center">✓<br>（需配合 IM 旗舰版使用）</td>
</tr>
<tr>
<td>同平台多端登录通话</td>
<td style="text-align: center">✓<br>（需配合 IM 旗舰版使用）</td>
<td style="text-align: center">-</td>
<td style="text-align: center">✓<br>（需配合 IM 旗舰版使用）</td>
<td style="text-align: center">✓<br>（需配合 IM 旗舰版使用）</td>
</tr>
<tr>
<td>AI 降噪</td>
<td style="text-align: center">✓</td>
<td style="text-align: center">-</td>
<td style="text-align: center">✓</td>
<td style="text-align: center">✓</td>
</tr>
<tr>
<td>弱网通话卡顿优化</td>
<td style="text-align: center">✓</td>
<td style="text-align: center">-</td>
<td style="text-align: center">✓</td>
<td style="text-align: center">✓</td>
</tr>
<tr>
<td>小程序通话加速</td>
<td style="text-align: center">✓</td>
<td style="text-align: center">-</td>
<td style="text-align: center">✓</td>
<td style="text-align: center">✓</td>
</tr>
<tr>
<td>支持平台</td>
<td style="text-align: center">iOS、Android、Web、uni-app、<strong>微信小程序</strong>、Flutter</td>
<td style="text-align: center">iOS、Android、Web、uni-app、Flutter</td>
<td style="text-align: center">iOS、Android、Web、uni-app、<strong>微信小程序</strong>、Flutter</td>
<td style="text-align: center">iOS、Android、Web、uni-app、<strong>微信小程序</strong>、Flutter</td>
</tr>
</tbody></table>

更多音视频通话能力的计费说明可参见 [音视频通话计费和购买相关问题](https://cloud.tencent.com/document/product/269/83726)。
