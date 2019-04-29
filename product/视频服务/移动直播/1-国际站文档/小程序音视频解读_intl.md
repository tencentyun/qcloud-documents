## Background

In the second half of 2017, WeChat has integrated Mobile LVB SDK into Mini Program solution, and wrap TXLivePusher and TXLivePlayer APIs of LiteAVSDK using &lt;live-pusher&gt; and &lt;live-player&gt; tags.

![](https://main.qcloudimg.com/raw/abae9bac64d940b5ece0f20c730364e8.png)

These two simple tags can implement audio/video capabilities in most application scenarios. The following describes how to use these capabilities in typical scenarios.

## User Experience
- **WeChat (Mini Program)**
![](https://mc.qcloudimg.com/static/img/9851dba2c86161bc9e14a08b5b82dfd2/image.png)

- [**Enterprise (PC)**](http://img.qcloud.com/open/qcloud/video/act/liteavWeb/avsolution/Index.html)
![](https://main.qcloudimg.com/raw/81edf044e0a40ccfd4794b91185f1f82.jpg)

| Feature | Mini Program Component | Experience on PC | Dependent Cloud Service | Description |
|:--------:|:--------------:|:-----------------:|:------------------:| :---------:|
| Mobile LVB | [&lt;live-room&gt;](https://cloud.tencent.com/document/product/454/15368) | N/A | LVB+IM | Demonstrate personnel live video solution based on Mini Program | 
| PC LVB | [&lt;live-room&gt;](https://cloud.tencent.com/document/product/454/15368) | [WebEXE](http://img.qcloud.com/open/qcloud/video/act/liteavWeb/webexe/webexe.html) | LVB+IM | Demonstrate features related to live classroom broadcasting and teacher-student interaction (in combination with PC) |
| One-on-one video chat | [&lt;rtc-room&gt;](https://cloud.tencent.com/document/product/454/15364) | [WebEXE](http://img.qcloud.com/open/qcloud/video/act/liteavWeb/webexe/webexe.html) | LVB+IM | Demonstrate one-on-one video chat feature which is applicable to online customer service |
| Multi-person video chat | [&lt;rtc-room&gt;](https://cloud.tencent.com/document/product/454/15364) | N/A | LVB+IM | Demonstrate multi-person video chat feature which is applicable to temporary meetings |
| WebRTC | [&lt;webrtc-room&gt;](https://cloud.tencent.com/document/product/454/16914) | [Chrome](http://img.qcloud.com/open/qcloud/video/act/liteavWeb/webrtc/webrtc.html) | Real-Time Audio/Video | Demonstrate the capability of interconnection between Mini Program and Chrome browser |
| RTMP Push | [&lt;live-pusher&gt;](https://cloud.tencent.com/document/product/454/12518) | N/A | LVB | Demonstrate basic RTMP push feature |
| LVB Player | [&lt;live-player&gt;](https://cloud.tencent.com/document/product/454/12519) | N/A | LVB | Demonstrate LVB playback feature based on RTMP and FLV protocols |

## How to Enable

- **Step 1: Enable access to tags**
 For policy and compliance considerations, &lt;live-pusher&gt; and &lt;live-player&gt; are only supported for the categories in the following table.
 For mini programs meeting requirements of categories, you need to enable the access to these two tags in <font color='red'>**Settings** -> **API Settings**</font> of the Mini Program management backend.
<table>
  <tr align="center">
    <th width="200px">Primary Category</th>
    <th width="700px">Sub-category</th>
  </tr>
  <tr align="center">
    <td>"Social"</td>
		<td>LVB</td>
  </tr>
	<tr align="center">
    <td>"Education"</td>
		<td>Online education</td>
  </tr>
	<tr align="center">
    <td>"Healthcare"</td>
		<td>Internet hospital and public hospital</td>
  </tr>
	<tr align="center">
    <td>"Government Affairs and Livelihood"</td>
		<td>All secondary categories</td>
  </tr>
	<tr align="center">
    <td>"Finance"</td>
		<td>Funds, trusts, insurance, banking, securities/futures, micro-credit of non-financial institutions, credit investigation, and consumer finance</td>
  </tr>
</table>
- **Step 2: Activate Tencent Cloud LVB service**
Audio/video capability for mini programs relies on Tencent Cloud [LVB](https://console.cloud.tencent.com/live) and [IM](https://console.cloud.tencent.com/avc) services, which can be activated free of charge by clicking the link. IM service can be used immediately once activated. LVB service that has a high risk of posting pornographic and political content requires users to go through Tencent Cloud's manual audit.


<h2 id="Live">Standard LVB scenario: Online Training</h2>

![](https://main.qcloudimg.com/raw/6eb5cc063929da3e6158941382aee794.png)

#### Introduction

Online Training is a very typical online LVB scenario, where you just need to join two tags together. &lt;live-pusher&gt; is used to upload local video images and audios to Tencent Cloud, while &lt;live-player&gt; is used to pull video streams for playback.

Tencent Cloud, as a signal amplifier, is responsible for amplifying a video stream from &lt;live-pusher&gt; across the country, allowing every &lt;live-player&gt; to pull the smooth video stream in real time from a closest CVM. This stable and reliable technique with simple principles enables millions of viewers to watch online video at the same time in case of high concurrency, and thus is the basis to implement scenarios from online education and sport events to game LVB and Huajiao.

The latency of this solution is 2 to 5 seconds on average, which can be set by using min-cache and max-cache tags of &lt;live-player&gt;. The smaller the value is, the lower the latency is, and therefore the higher the probability of stutter becomes.

#### Integration

- Step 1 Obtain URL: See [Quickly Obtain URL](https://cloud.tencent.com/document/product/454/7915) or document on how to [construct URL](https://cloud.tencent.com/document/product/454/9875).

- Step 2 Integrate push: Use [&lt;live-pusher&gt;](https://cloud.tencent.com/document/product/454/12518) tag to push video streams to the RTMP push address (domain name: livepush.mycloud.com) obtained in step 1, and set the mode to **HD**. If any failure occurs, use the debug feature in &lt;live-pusher&gt; to locate problems or refer to [DOC](https://cloud.tencent.com/document/product/454/7951) for troubleshooting.

- Step 3: Integrate playback: Use [&lt;live-player&gt;](https://cloud.tencent.com/document/product/454/12519) to play RTMP or HTTP-FLV (recommended) address specified by SRC, and set the mode to **live**. "min-cache" and "max-cache" can be set to 1 and 3 respectively.


<h2 id="Latency">Scenario with ultra-low latency: Remote control</h2>

![](https://main.qcloudimg.com/raw/d1f656ed345daf47cb2e308d34573107.png)

#### Introduction
In security monitoring scenario, the IPCamera for home use comes with head rotation feature, that is, the rotation of camera is remotely controlled. In case of higher latency, viewers will wait for a longer period of time to watch moving images, thus resulting in poor user experience.

Let's take online prize claw which is very popular in 2017 as another example. If the latency in remote players' video images is quite high, it is impossible to control the price claw remotely because no one can really claw a toy.

To meet this requirement, ordinary online LVB technique is no longer applicable, and we need to use ultra-low latency mode, i.e., the RTC mode of &lt;live-player&gt;. Meanwhile, we should also join the playback URL with a hotlink protection signature to use Tencent Cloud's ultra-low latency linkage.

#### Integration
- Step 1 Obtain URL: See [Quickly Obtain URL](https://cloud.tencent.com/document/product/454/7915) or document on how to [construct URL](https://cloud.tencent.com/document/product/454/9875).

- Step 2 Integrate push: You can use [LiteAVSDK(TXLivePusher)](https://cloud.tencent.com/document/product/454/7885) for Android on your device to push streams. For other solutions, contact us by submitting a ticket or calling the number starting with 400.

- Step 3 Low latency URL: Append a [Hotlink Protection Signature](https://cloud.tencent.com/document/product/454/9875#Secret) to an ordinary RTMP:// playback URL to convert an ordinary URL to a low latency URL, as shown below:

| Item | Example | Latency |
|---------|---------| ----- |
| Ordinary LVB URL | rtmp://3891.liveplay.myqcloud.com/live/3891_test_clock_for_rtmpacc | >2s |
| Ultra-low latency URL | rtmp://3891.liveplay.myqcloud.com/live/3891_test_clock_for_rtmpacc?bizid=bizid&txTime=5FD4431C&txSerect=20e6d865f462dff61ada209d53c71cf9 | <500 ms | 

- Step 4: RTC playback: Use the low latency URL in step 3 as the **src** attribute parameter of the [&lt;live-player&gt;](https://cloud.tencent.com/document/product/454/12519) tag, and set the mode to **RTC**. In this case, **low latency control** and **UDP acceleration** features of &lt;live-player&gt; are enabled.


<h2 id="Double">Two-way video chat: Video customer service</h2>

![](https://main.qcloudimg.com/raw/c6e233d6808c65223ad63faef031dbc6.png)

#### Introduction
In financial account opening scenario, it is critical for banks or security companies to authenticate the identity of applicants for opening an account, and audio and video recordings are also required. However, applicants are always attracted by promotions or advertisements to open an account, but it is difficult to require them to install an App before completing the entire process. Mini Program can solve this problem well. It is acceptable to users because of its formality, and thus is perfect for online financial account opening.

Likewise, insurance claim is another typical application scenario. By quickly installing and launching a mini program, the attendance of loss assessors can be reduced to save operating cost.

#### Integration (based on native tag)

- Step 1 Preparation: Understand how to obtain a low latency URL and how does RTC mode work by referring to the [Scenario with Ultra-low Latency](#Latency) solution.

- Step 2 Customer service: Push a video stream to Tencent Cloud. and send the low latency playback URL A to URL B after receiving **1002** of onPushEvent. Mini program is no longer applicable to customer service, we can use [IE](https://cloud.tencent.com/document/product/454/13644), [C++](https://cloud.tencent.com/document/product/454/13671) or [C#](https://cloud.tencent.com/document/product/454/13626) solution.

- Step 3 User: Create a [&lt;live-player&gt;](https://cloud.tencent.com/document/product/454/12519) tag, set the mode to RTC, and specify SRC as URL A.

- Step 4 User: Create a [&lt;live-pusher&gt;](https://cloud.tencent.com/document/product/454/12518) tag, set the mode to RTC, and send the low latency playback URL B to URL A after receiving **1002** of onPushEvent.

- Step 5 Customer service: Play low latency URL B. Mini program is no longer applicable to customer service, we can use [IE](https://cloud.tencent.com/document/product/454/13644), [C++](https://cloud.tencent.com/document/product/454/13671) or [C#](https://cloud.tencent.com/document/product/454/13626) solution.

#### Integration (based on &lt;rtc-room&gt;)
If the integration solution based on the native &lt;live-pusher&gt; and &lt;live-player&gt; is complicated, you can also implement integration based on &lt;rtc-room&gt; tag.

- Step 1: Activate Tencent Cloud [LVB](https://console.cloud.tencent.com/live) and [IM](https://console.cloud.tencent.com/avc) services.

- Step 2 Mini Program: Use a custom component [&lt;rtc-room&gt;](https://cloud.tencent.com/document/product/454/15364) to implement video chat. For 1v1 chat mode, the template of &lt;rtc-room&gt; can be set to **1v1**. You can also [customize](https://cloud.tencent.com/document/product/454/15364#CustomUI) UI layout.

- Step 3 Windows: We provide [API](https://cloud.tencent.com/document/product/454/15364#PLATFORM) for multiple platforms simultaneously for you to choose based on your project needs.

<h2 id="RTCRoom">Multi-person video chat: Remote hearing (RTCRoom)</h2>

![](https://main.qcloudimg.com/raw/155dc1fe17cb0a293d66f267946de0d1.png)

#### Introduction
The reform of "Internet + Government affairs service" performed by Chinese government is aimed at "Provide more information and streamline procedures". Remote hearing is a typical application scenario.

The mini program of multi-person video chat is perfect for establishing a remote hearing solution. On one hand, the installation and launch of a mini program are hassle-free, making it easy for parties involved or witnesses who are inconvenient to directly appear in court to participate in hearings. On the other hand, users will feel secure with the mini program because of its formality.

#### Integration

- Step 1: Activate Tencent Cloud [LVB](https://console.cloud.tencent.com/live) and [IM](https://console.cloud.tencent.com/avc) services.

- Step 2: Use a custom component [&lt;rtc-room&gt;](https://cloud.tencent.com/document/product/454/15364) to implement video chat. You can choose one from our pre-defined modes as the template, or [customize](https://cloud.tencent.com/document/product/454/15364#CustomUI) UI layout by yourself.

- Step 3 Windows: We provide [API](https://cloud.tencent.com/document/product/454/15364#PLATFORM) for multiple platforms simultaneously for you to choose based on your project needs.


<h2 id="LiveRoom">Hybrid scenario: LVB+Joint broadcasting (LiveRoom)</h2>

![](https://main.qcloudimg.com/raw/3ae5c28b5095fe0b37d45d06ea3f87ca.png)

#### Introduction
LVB scenario needs to allow millions of viewers to watch video at the same time and initiate a request for joint broadcasting to VJ, in which case hybrid scenario solution is required. Hybrid scenario is implemented by adding the joint broadcasting capability to a standard LVB scenario solution.

A common application scenario is interactive class. [&lt;rtc-room&gt;](https://cloud.tencent.com/document/product/454/12723) can be directly used for small-class teaching with just a few students in a lesson. But for large-class teaching, hybrid solution must be used.

Tencent Cloud &lt;live-room&gt; hybrid solution comes with a separate PPT whiteboard component which is built based on the Canvas control of Mini Program.

#### Integration

- Step 1: Activate Tencent Cloud [LVB](https://console.cloud.tencent.com/live) and [IM](https://console.cloud.tencent.com/avc) services.

- Step 2 Mini Program: Use a custom component [&lt;live-room&gt;](https://cloud.tencent.com/document/product/454/15368) to implement LVB+Joint broadcasting. You can choose one from our pre-defined modes as the template, or [customize](https://cloud.tencent.com/document/product/454/15368#CustomUI) UI layout by yourself.

- Step 3 Windows: We provide [API](https://cloud.tencent.com/document/product/454/15368#PLATFORM) for multiple platforms simultaneously for you to choose based on your project needs.

## Recording
Tencent Cloud supports recording of the entire LVB session at the service end of Mini Program audio/video solution. You can enable cloud recording by following the steps below. If recording is not enabled, server nodes of Tencent Video Cloud are only responsible for transferring audio/video data without further processing.

- Step 1: [Activate](https://console.cloud.tencent.com/video) Tencent Cloud VOD service.

- Step 2: Log in to the [LVB console](https://console.cloud.tencent.com/live) (based on which the Mini Program audio/video streaming media is built), enable recording feature by going to **Access Management** -> **Access Configuration** -> **LVB Recording**. (Note: The fee here is charged by the number of concurrent recordings, not by video stream)
![](https://main.qcloudimg.com/raw/6dfeba07c25151be7025dab0245398ff.jpg)

- Step 3: These recorded files can be found on the [Video Management](https://console.cloud.tencent.com/video/videolist) interface of VOD, or obtained by calling the [REST API](https://cloud.tencent.com/document/product/266/10688) of VOD.



