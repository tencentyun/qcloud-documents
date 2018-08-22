## 体验

![](https://mc.qcloudimg.com/static/img/9851dba2c86161bc9e14a08b5b82dfd2/image.png)

> 打开微信，在小程序中搜索 “腾讯视频云”或者扫描上面的二维码，即可体验我们的官方 DEMO。

## 注册小程序并开通类目与推拉流标签【重要】
打开 [微信公众平台](https://mp.weixin.qq.com) 注册并登录小程序，出于政策和合规的考虑，微信暂时没有放开所有小程序对 &lt;live-pusher&gt; 和 &lt;live-player&gt; 标签的支持：

- 个人账号和企业账号的小程序暂时只开放如下表格中的类目：

<table>
<tr align="center">
<th width="200px">主类目</th>
<th width="700px">子类目</th>
</tr>
<tr align="center">
<td>【社交】</td>
<td>直播</td>
</tr>
<tr align="center">
<td>【教育】</td>
<td>在线教育</td>
</tr>
<tr align="center">
<td>【医疗】</td>
<td>互联网医院，公立医院</td>
</tr>
<tr align="center">
<td>【政务民生】</td>
<td>所有二级类目</td>
</tr>
<tr align="center">
<td>【金融】</td>
<td>基金、信托、保险、银行、证券/期货、非金融机构自营小额贷款、征信业务、消费金融</td>
</tr>
</table>

- 符合类目要求的小程序，需要在小程序管理后台的<font color='red'> “设置 - 接口设置” </font>中自助开通该组件权限，如下图所示：

![](https://mc.qcloudimg.com/static/img/a34df5e3e86c9b0fcdfba86f8576e06a/weixinset.png)

注意：如果以上设置都正确，但小程序依然不能正常工作，可能是微信内部的缓存没更新，请删除小程序并重启微信后，再进行尝试。

## 安装微信小程序开发工具

下载并安装最新版本的[微信开发者工具](https://mp.weixin.qq.com/debug/wxadoc/dev/devtools/download.html)，使用小程序绑定的微信号扫码登录开发者工具。

![微信开发者工具](https://mc.qcloudimg.com/static/img/4fd45bb5c74eed92b031fbebf8600bd2/1.png)

## 下载 Demo

访问 [GitBub地址](https://github.com/TencentVideoCloudMLVBDev/RTCRoomDemo)，获取小程序 Demo源码。

## 本地调试小程序代码

1.打开安装的微信开发者工具，点击【小程序项目】按钮。
2.输入小程序 AppID，项目目录选择上一步下载下来的代码目录，点击确定创建小程序项目。
3.再次点击【确定】进入开发者工具。

> **注意：** 目录请选择 `RTMPRoom` 根目录。包含有 `project.config.json`，请不要只选择 `wxlite` 目录！

![上传代码](https://mc.qcloudimg.com/static/img/fd7074730e5b37af8a4d86dc8125d120/xiaochengxustart.png)

4.请使用手机进行测试，直接扫描开发者工具预览生成的二维码进入，<font color='red'> 这里使用的是腾讯云提供的官方Demo测试后台，小程序控制台没有配置域名白名单，一定要开启调试: </font>

![开启调试](https://mc.qcloudimg.com/static/img/1abfe50750f669ca4e625ec3cdfbd411/xiaochengxutiaoshi.png)

至此，您已经可以在本地修改调试小程序代码了，如果您需要上线，则需要部署自己的后台环境，请参考后台自行部署。

##后台自行部署

### WebRTC解决方案 （Java版） 

实现了一个简单的房间列表功能，同时包含**webrtc-room**标签几个所需参数的生成代码

1.Java后台自行部署

下载 [WebRTC后台源码](https://github.com/TencentVideoCloudMLVBDev/webrtc_server_java)，根据README.md中的指引部署后台服务。

2.小程序部署

下载 [小程序](https://github.com/TencentVideoCloudMLVBDev/RTCRoomDemo) 源码，将wxlite/config.js文件中的`webrtcServerUrl`修改成 *https://您自己的域名/webrtc/weapp/webrtc_room*

3.web端部署

下载 [web端](https://github.com/TencentVideoCloudMLVBDev/webrtc_pc) 源码，将component/WebRTCRoom.js文件中的`serverDomain`修改成 *https://您自己的域名/webrtc/weapp/webrtc_room*

### RTCRoom解决方案（Java版） 

RTCRoom 是 **live-room**（直播连麦）和 **rtc-room**（视频通话）的后台组件，源码下载后可部署于自己的业务服务器上。

1.Java后台自行部署

下载 [RTCRoom后台源码](https://github.com/TencentVideoCloudMLVBDev/rtcroom_server_java)，根据README.md中的指引部署后台服务。

2.小程序部署

下载 [小程序](https://github.com/TencentVideoCloudMLVBDev/RTCRoomDemo) 源码，将wxlite/config.js文件中的`serverUrl`和 `roomServiceUrl`修改成*https://您自己的域名/roomservice/*

3.windows Demo部署

下载 [windows web demo](https://github.com/TencentVideoCloudMLVBDev/webexe_web) 源码，将liveroom.html、double.html文件中的`RoomServerDomain`修改成*https://您自己的域名/roomservice/*

### RTCRoom解决方案（NodeJS一键部署） 

RTCRoom是 **live-room**（直播连麦）和 **rtc-room**（视频通话）的后台组件，源码下载后可部署于自己的业务服务器上。

1.NodeJS一键部署(包含了小程序&后台)

- 下载 [小程序](https://github.com/TencentVideoCloudMLVBDev/RTCRoomDemo) 源码，根据README.md中的指引一键部署。

- wxlite/config.js文件中的`serverUrl`和 `roomServiceUrl`修改成*https://您自己的域名/roomservice/*

2.windows Demo部署

下载 [windows web demo](https://github.com/TencentVideoCloudMLVBDev/webexe_web) 源码，将liveroom.html、double.html文件中的`RoomServerDomain`修改成*https://您自己的域名/roomservice/*
