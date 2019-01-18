尊敬的客户您好，感谢您关注腾讯云移动直播（Mobile Live Video Broadcasting）服务！

## 什么是移动直播？
移动直播并不是一个具体的服务，而是一套**帮助您在智能手机上做直播**的解决方案，它是腾讯云直播服务（LVB）在移动终端方向的技术延伸，您可以根据当前情况选择最适合自己的组合方案：

- **如果您有成熟终端解决方案**
如果您已经有成熟的终端解决方案，只是想要选择更加优秀的直播云服务，推荐您直接转 [直播云服务](https://cloud.tencent.com/product/LVB) 了解云端对接解决方案即可。

- **如果您只想对接推流和播放**
如果您想要在自己的 APP 里集成直播推流和播放功能，推荐您选择 [快速版集成方案](#.E5.BF.AB.E9.80.9F.E7.89.88.E9.9B.86.E6.88.90.E6.96.B9.E6.A1.88)，接入非常简单，最快一天内就能搞定直播功能。

- **如果您想做完善的直播服务**
如果您想要在自己的 APP 里集成整套完善的直播能力，诸如文字互动、弹幕消息、飘星点赞、美颜增白、动效蒙皮、连麦互动、身份认证等功能，推荐您选择 [一体化集成方案](#.E4.B8.80.E4.BD.93.E5.8C.96.E9.9B.86.E6.88.90.E6.96.B9.E6.A1.88)。

## 快速版集成方案
![](//mc.qcloudimg.com/static/img/92a464fc26bbe52fea8816f8e6061ef3/image.jpg)

如果您想要在自己的 APP 里集成直播推流和播放功能，下面三步就能达成目标：
<table class="t" style="margin-left:75px; width:auto;">
<tbody><tr>
<th width="120" style="text-align: center;"> 对接步骤
</th><th width="200" style="text-align: center;"> 步骤说明
</th><th width="300" style="text-align: center;"> 参考文档
</th><th width="150" style="text-align: center;"> 研发人员
</th></tr>
<tr>
<td style="text-align: center;"> step1
</td><td style="text-align: center;"> 开通直播服务
</td><td style="text-align: center;"> <a href="https://console.cloud.tencent.com/live" target="_blank"> 直播控制台开通！ </a>
</td><td style="text-align: center;"> 无要求
</td></tr>
<tr>
<td rowspan="4" style="text-align: center;"> step2
</td><td rowspan="4" style="text-align: center;"> 集成 RTMP SDK
</td><td style="text-align: center;"> <a href="https://cloud.tencent.com/document/product/454/7879" target="_blank"> RTMP SDK - iOS 平台推流 </a>
</td><td rowspan="4" style="text-align: center;"> 终端研发工程师
</td></tr>
</td><td style="text-align: center;"> <a href="https://cloud.tencent.com/document/product/454/7880" target="_blank"> RTMP SDK -  iOS 平台播放 </a>
</td></tr>
</td><td style="text-align: center;"> <a href="https://cloud.tencent.com/document/product/454/7885" target="_blank"> RTMP SDK -  Android 平台推流 </a>
</td></tr>
</td><td style="text-align: center;"> <a href="https://cloud.tencent.com/document/product/454/7886" target="_blank"> RTMP SDK -  Android 平台播放 </a>
</td></tr>
<td rowspan="3" style="text-align: center;"> step3
</td><td rowspan="3" style="text-align: center;"> 对接直播流管理
</td><td style="text-align: center;"> <a href="https://cloud.tencent.com/document/product/454/7915" target="_blank">云端API - 如何获取推流URL？</a>
</td><td rowspan="3" style="text-align: center;"> 后端研发工程师
</td></tr>
<td style="text-align: center;"> <a href="https://cloud.tencent.com/document/product/454/7916" target="_blank">云端API - 如何构建房间列表？</a>
</td></tr>
<td style="text-align: center;"> <a href="https://cloud.tencent.com/document/product/454/7920" target="_blank">云端API - 如何管理直播流？</a>
</td></tr>
</tbody></table>

## 一体化集成方案
如果您想要在自己的 APP 里集成整套完善的直播能力，诸如文字互动、弹幕消息、飘星点赞、美颜增白、动效蒙皮、连麦互动、身份认证等功能，可以尝试参考 **小直播**：
![](//mc.qcloudimg.com/static/img/e7ce9dbe3274f8704643030e9b2ee38c/image.jpg)

小直播是有腾讯云研发团队提供的一套开源源码集，致力于以 DEMO 的形式向您展示：如何利用腾讯云直播(LVB)、点播(VOD)、云通信(IM) 和 对象存储(COS)等几项服务组合构建出适合您的直播解决方案。

您可以参考 [如何快速完成搭建](https://cloud.tencent.com/document/product/454/7999) 来快速构建您自己的“小直播”调试环境，它能够为您的工程提供尽可能多的代码参考以及二次开发环境。