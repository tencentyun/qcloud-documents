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
TUICallKit 是腾讯云推出一款音视频通话 UI 组件，通过集成该组件，您只需要编写几行代码就可以为您的 App 添加音视频通话功能，并且支持离线唤起能力。TUICallKit 支持 Android、iOS、Web、微信小程序、Flutter、UniApp 等多个开发平台，基本功能如下图所示：
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

**TUICallKit 需要获取音视频通话 SDK 套餐使用**，音视频通话 SDK 在整合了腾讯云 [实时音视频 TRTC](https://cloud.tencent.com/document/product/647/16788) 和 [即时通信 IM](https://cloud.tencent.com/document/product/269/1498) 两个基础 PaaS 服务的基础上，在视频通话场景进行深度融合，推出针对通话场景的功能和 UI 设计。您可以在音视频通话 SDK 控制台中，一站式为您的应用 [开通音视频通话业务](https://cloud.tencent.com/document/product/1640/79983#a3c3d156-aa4d-46ba-a0d0-44237a79db8f)；或者在 IM 控制台中，为您已有的 IM 聊天应用的基础上 [开通音视频通话服务](https://cloud.tencent.com/document/product/269/72445#.E6.AD.A5.E9.AA.A41.EF.BC.9A.E5.BC.80.E9.80.9A.E9.9F.B3.E8.A7.86.E9.A2.91.E6.9C.8D.E5.8A.A1)。

## 功能与计费说明

音视频通话 SDK 提供了 7 天的免费试用，您可以在控制台自助领取；您也可以 [前往购买页选购正式版本](https://buy.cloud.tencent.com/vcube?type=call) 开通正式的通话服务。
音视频通话 SDK 套餐内包含了音视频通话功能和 IM 基础服务功能，购买套餐会赠送对应的资源，超出赠送部分会按照对应产品的计费策略进行结算：

- 购买套餐会赠送 TRTC 时长包，可抵扣音频或按比例抵扣不同分辨率视频的通话分钟消耗。可以额外购买 [TRTC 时长包](https://cloud.tencent.com/document/product/647/44247#year) 或者按 [音视频时长后付费价格](https://cloud.tencent.com/document/product/647/44248) 来结算超出部分的通话时长。
- 购买套餐会赠送 1 万日活跃用户数（DAU）额度和 10 万峰值群组数，超出部分会按  [IM 后付费价格](https://cloud.tencent.com/document/product/269/11673#.E5.9F.BA.E7.A1.80.E6.9C.8D.E5.8A.A1.E8.B5.84.E8.B4.B9.3Ca-id.3D.22jc.22.3E.3C.2Fa.3E) 进行结算

音视频通话 SDK 套餐的价格和功能对比参见表格，计费详细说明可参见 [音视频通话 SDK 计费说明](https://cloud.tencent.com/document/product/1640/79968)：

<table>
  <tr>
    <th colspan="2" style="text-align:center"> 对比项 </th>
    <th style="text-align:center"> 体验版</th>
    <th style="text-align:center"> 基础版</th>
	  <th style="text-align:center"> 进阶版</th>
    <th style="text-align:center"> 尊享版</th>
  </tr>
	<tr>
    <td colspan="2" width="100px" style="text-align:center"> <b>价格</b> </td>
    <td style="text-align:center"> 0元/7天</td>
    <td style="text-align:center"> 1499元/月 <br /><a href="https://buy.cloud.tencent.com/vcube?type=call">立即选购</a></td>
	  <td style="text-align:center"> 1999元/月 <br /><a href="https://buy.cloud.tencent.com/vcube?type=call">立即选购</a></td>
    <td style="text-align:center"> 4499元/月 <br/><a href="https://buy.cloud.tencent.com/vcube?type=call">立即选购</a></td>
  </tr>
	<td rowspan='4' width='150px' style="text-align:center"> <b>赠送资源</b><br/>(超出后付费)</td>
	<tr>
    <td style="text-align:center"> 通话时长</td>
    <td style="text-align:center"> -</td>
	  <td style="text-align:center"> 110,000分钟/月 </td>
    <td style="text-align:center"> 235,000分钟/月 </td>
		<td style="text-align:center"> 380,000分钟/月 </td>
  </tr>
	<tr>
    <td style="text-align:center"> 日活跃用户数（DAU）</td>
    <td style="text-align:center"> 根据 IM 版本而定 </td>
	  <td style="text-align:center"> 10,000 DAU </td>
    <td style="text-align:center"> 10,000 DAU </td>
		<td style="text-align:center"> 10,000 DAU </td>
  </tr>
	<tr>
    <td style="text-align:center"> 峰值群组数 </td>
    <td style="text-align:center"> 根据 IM 版本而定 </td>
	  <td style="text-align:center"> 100000个/月 </td>
    <td style="text-align:center"> 100000个/月</td>
		<td style="text-align:center"> 100000个/月 </td>
  </tr>
	<td rowspan='14' style="text-align:center"> <b> 通话相关功能 </b> </td>
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
	 <tr>
    <td colspan="2" width="100px" style="text-align:center"> <b>即时通信相关功能</b> </td>
    <td style="text-align:center"> 可配合</br> IM 不同版本试用 </td>
    <td style="text-align:center"> 详见 <br /><a href="https://cloud.tencent.com/document/product/269/11673#.E5.9F.BA.E7.A1.80.E6.9C.8D.E5.8A.A1.E8.AF.A6.E6.83.85"> IM 专业版功能 </a></td>
	  <td style="text-align:center"> 详见 <br /><a href="https://cloud.tencent.com/document/product/269/11673#.E5.9F.BA.E7.A1.80.E6.9C.8D.E5.8A.A1.E8.AF.A6.E6.83.85"> IM 专业版功能 </a> </td>
    <td style="text-align:center"> 详见 <br /><a href="https://cloud.tencent.com/document/product/269/11673#.E5.9F.BA.E7.A1.80.E6.9C.8D.E5.8A.A1.E8.AF.A6.E6.83.85"> IM 专业版功能 </a> </td>
  </tr>
	<tr>
    <td colspan="2" width="100px" style="text-align:center"> <b>超出赠送资源部分后付费</b> </td>
    <td  colspan="4"  style="text-align:center"> 通话时长后付费价格详见<a href="https://cloud.tencent.com/document/product/647/44248"> 音视频时长计费说明 </a>，DAU 与 峰值群组数后付费价格详见 <a  href="https://cloud.tencent.com/document/product/269/11673#.E5.9F.BA.E7.A1.80.E6.9C.8D.E5.8A.A1.E8.B5.84.E8.B4.B9.3Ca-id.3D.22jc.22.3E.3C.2Fa.3E"> IM 计费说明 </a></td>
  </tr>
	<tr>
    <td colspan="2" width="100px" style="text-align:center"> <b>支持平台</b> </td>
    <td  colspan="4"  style="text-align:center"> iOS、Android、Web、<b> 微信小程序（进阶版与尊享版支持）</b>、uni-app、Flutter（即将上线）  </a></td>
  </tr>
</table>
