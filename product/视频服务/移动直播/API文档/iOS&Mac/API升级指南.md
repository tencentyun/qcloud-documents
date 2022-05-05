## 升级概述

为了更好地满足客户的接入需求，移动直播在 API 以及支持的协议上做了重要的升级。API 2.0 相比与 API 1.0 在设计上更简洁也更实用，同时也增加了更多的能力，例如 RTC 的推流以及新的连麦方案。相对于原来的 RTMP 推流，RTC 推流具有更低地延迟，弱网下也有更好表现，全球覆盖使您出海业务更方便。另外 API 2.0 也增加了快直播播放，快直播（Live Event Broadcasting，LEB）是标准直播在超低延迟播放场景下的延伸，能够为观众提供毫秒级的极致直播观看体验。

**下面从两个方面介绍升级步骤以及注意事项：**

[](id:api_update)
## 仅 API 升级

>! **适用范围：**使用 `TXLivePusher` 和 `TXLivePlayer` API 的客户。

移动直播 SDK 从 8.4 版本开始增加了一套新的 API `V2TXLivePusher` 和 `V2TXLivePlayer` 用来替代 `TXLivePusher` 和 `TXLivePlayer` ，主要优化点有以下几个方面：
- 去掉了 V1 一些冗余接口，例如 `TXLivePushConfig#setAutoAdjustBitrate` 等。
- 简化了 V1 一些复杂的使用方式，例如 `TXLivePushConfig` 类。
- 新增了一些实用的接口，例如 `V2TXLivePremierObserver#onLicenceLoaded` 用来告知用户 Licence 设置的结果以及失败原因。
- 新增了一些特性，例如支持 [RTC 协议](https://cloud.tencent.com/document/product/454/56592#3.-.E5.88.9D.E5.A7.8B.E5.8C.96-v2txlivepusher-.E7.BB.84.E4.BB.B6) URL 推流，支持 [快直播播放](https://cloud.tencent.com/document/product/454/68195) 等。

为了方便开发者升级 API，我们在 [腾讯文档](https://docs.qq.com/sheet/DRkJUckpGdkNTUmt2?tab=BB08J2) 上做了一个 API 对比说明以供参考。

>! `TXLivePusher` 和 `TXLivePlayer` 会在未来合适的时候废弃，请尽快升级。

[](id:protocol_update)
## 推流协议升级

<dx-alert infotype="notice" title="<b>适用范围：</b>">
对延迟以及弱网表现有更高追求的客户。
</dx-alert>


移动直播 SDK V1 API 只能使用 RTMP 协议推流，V2 API 新增了 RTC 协议的推流能力。RTC 协议基于 [TRTC SDK](https://cloud.tencent.com/document/product/647/) ，在延迟以及弱网下有极佳的表现，详见 [RTC 推流优势](https://cloud.tencent.com/document/product/454/68574)。
**针对不同的业务状态升级策略会有些不同：**

[](id:push1)
### 如果您的业务不存在连麦场景
如果当前您的 App 只使用了 RTMP 协议推流，即没有连麦业务，升级到 RTC 协议推流是最简单的。


<table>
<thead>
<tr>
<th>类型</th>
<th>注意事项</th>
</tr>
</thead>
<tbody><tr>
<td>推流端</td>
<td><ul style="margin:0">
<li>必要前提：您需要升级使用 <code>V2TXLivePusher</code> 推 RTC 流。</li>
<li>RTC 推流与 RTMP 推流仅在两个 API 使用上有参数差异，其他的 API 调用方式没有任何区别。<ul>
<li>构造 <code>V2TXLivePusher</code> 对象时传入 RTC 协议参数：<code>V2TXLiveDef.V2TXLiveMode.TXLiveMode_RTC</code>，具体请参见 <a href="https://cloud.tencent.com/document/product/454/56592#3.-.E5.88.9D.E5.A7.8B.E5.8C.96-v2txlivepusher-.E7.BB.84.E4.BB.B6">摄像头推流 # 初始化 V2TXLivePusher 组件</a>。</li>
<li>启动推流时传入 RTC 协议 URL，请参见 <a href="https://cloud.tencent.com/document/product/454/56592#5.-.E5.90.AF.E5.8A.A8.E5.92.8C.E7.BB.93.E6.9D.9F.E6.8E.A8.E6.B5.81">摄像头推流 - 启动和结束推流</a>。</li>
</ul>
</li>
</ul></td>
</tr>
<tr>
<td>播放端</td>
<td>在观众端您有三种方式可以播放，CDN 最便宜但延迟最大，RTC 最贵但延迟最小，快直播是延迟和费用之间的平衡。三种协议 API 除了播放的 URL 不同，调用方式是一致的。<ul style="margin:0">
<li>播放 CDN 流：推荐您升级使用 <a href="https://cloud.tencent.com/document/product/454/56598">V2TXLivePlayer 播放</a>。当前使用 <code>TXLivePlayer</code> 仍然是可以播放的。</li>
<li>播放 RTC 流：必须升级使用 <code>V2TXLivePlayer</code> 播放。RTC 拉流的 URL 请参见 <a href="https://cloud.tencent.com/document/product/454/7915#.E8.87.AA.E4.B8.BB.E6.8B.BC.E8.A3.85-rtc-.E8.BF.9E.E9.BA.A6.2Fpk-url">自主拼装 RTC 连麦/PK URL</a>。</li>
<li>播放快直播流：必须升级使用 <code>V2TXLivePlayer</code> 播放，具体请参见 <a href="https://cloud.tencent.com/document/product/454/68195#.E6.8E.A5.E5.85.A5.E5.B7.A5.E7.A8.8B">快直播拉流</a>。</li>
</ul></td>
</tr>
</tbody></table>

[](id:push2)
### 如果您的业务即将接入连麦业务
如果当前您的 App 只使用了 RTMP 协议推流，即将接入连麦业务，此时您需要使用 RTC 实现连麦能力。
那么接入连麦后您的业务可能存在两种状态：
- 不推荐：连麦时使用 RTC 协议，非连麦使用 RTMP 协议。不推荐两种协议并存的方式，因为主播在连麦状态和非连麦状态之间切换时都需要重新推流，这会造成 CDN 观众在观看时会有中断的体验。
- 推荐：连麦和非连麦都使用 RTC 协议。推荐这种方式，主播在连麦和非连麦状态之间切换，CDN 观众观看时无感知。

**接入时需要注意**：
<table>
<thead>
<tr>
<th>类型</th>
<th>注意事项</th>
</tr>
</thead>
<tbody><tr>
<td>推流端</td>
<td><ul style="margin:0">
<li>必要前提：您需要升级使用 <code>V2TXLivePusher</code> 推 RTC 流。</li>
<li>RTC 推流与 RTMP 推流仅在两个 API 使用上有参数差异，其他的 API 调用方式没有任何区别。<ul>
<li>构造 <code>V2TXLivePusher</code> 对象时传入 RTC 协议参数：<code>V2TXLiveDef.V2TXLiveMode.TXLiveMode_RTC</code>，具体请参见 <a href="https://cloud.tencent.com/document/product/454/56592#3.-.E5.88.9D.E5.A7.8B.E5.8C.96-v2txlivepusher-.E7.BB.84.E4.BB.B6">摄像头推流 # 初始化 V2TXLivePusher 组件</a>。</li>
<li>启动推流时传入 RTC 协议 URL，请参见 <a href="https://cloud.tencent.com/document/product/454/56592#5.-.E5.90.AF.E5.8A.A8.E5.92.8C.E7.BB.93.E6.9D.9F.E6.8E.A8.E6.B5.81">摄像头推流 - 启动和结束推流</a>。</li>
<li>实现连麦的具体步骤请参见 <a href="https://cloud.tencent.com/document/product/454/52751">观众连麦</a>。</li>
</ul>
</li>
</ul>
</td>
</tr>
<tr>
<td>播放端</td>
<td>连麦的观众或者主播需要用 RTC 协议播放，非连麦的观众可以观看 CDN 流或者快直播流。三种协议 API 除了传入的 URL 不同，调用方式是一致的。<ul style="margin:0">
<li>必要前提：您需要升级使用 <code>V2TXLivePlayer</code> 来拉流播放。</li>
<li>播放 RTC 流：连麦的双方必须播放 RTC 流，具体的 API 使用请参见 <a href="https://cloud.tencent.com/document/product/454/52751">观众连麦</a>。</li>
<li>播放 CDN 流：具体 API 使用请参见 <a href="https://cloud.tencent.com/document/product/454/56598">标准直播拉流</a>。</li>
<li>播放快直播流：具体 API 使用请参见 <a href="https://cloud.tencent.com/document/product/454/68195#.E6.8E.A5.E5.85.A5.E5.B7.A5.E7.A8.8B">快直播拉流</a>。</li>
</ul>
</td>
</tr>
</tbody></table>


[](id:push3)
### 如果您的业务已有连麦业务
如果当前您的 App 已经存在连麦业务，需要升级到 RTC 连麦，您可以通过以下步骤进行。
1. 先实现：
  - 实现新连麦：使用 RTC 实现连麦能力（具体方案请参见 [即将接入连麦业务](#push2)）。
  - 增加云控：增加云控来获取当前应该使用哪一种连麦方式。
2. 再并存：
  - 逐步升级含有新连麦方式的 App 版本。
  - 因为新老版本可能会有不通的地方，所以此时不能放开新连麦方式。
2. 最终上线：
  - 版本全覆盖时通过云控全部切换为新连麦方案。
  - 下线老连麦方式。



