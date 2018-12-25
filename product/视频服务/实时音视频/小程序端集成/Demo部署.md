Demo 体验
升级微信到最新版本，发现页卡 => 小程序 => 搜索“腾讯视频云”，即可打开小程序Demo：

## 再次确认您已经完成相关接口的开通
打开 [微信公众平台](https://mp.weixin.qq.com) 注册并登录小程序，并在小程序管理后台的<font color='red'> “设置 - 接口设置” </font>中自助开通该组件权限，如下图所示：

![](https://mc.qcloudimg.com/static/img/a34df5e3e86c9b0fcdfba86f8576e06a/weixinset.png)

> 注意：如果以上设置都正确，但小程序依然不能正常工作，可能是微信内部的缓存没更新，请删除小程序并重启微信后，再进行尝试。

## 安装微信小程序开发工具

下载并安装最新版本的[微信开发者工具](https://mp.weixin.qq.com/debug/wxadoc/dev/devtools/download.html)，使用小程序绑定的微信号扫码登录开发者工具。

<img style="border:0; max-width:100%; height:auto; box-sizing:content-box; box-shadow: 0px 0px 0px #ccc; margin: 0px 0px 0px 0px;" src="https://main.qcloudimg.com/raw/8e1eeee23aec979f346d4b4c05e62571.png" />


## 获取Demo源码并调试

- step1: 访问 [SDK + Demo](https://cloud.tencent.com/document/product/454/7873#XiaoChengXu)，获取小程序 Demo 源码。

- step2: 打开安装的微信开发者工具，点击【小程序项目】按钮。

- step3: 输入小程序 AppID，项目目录选择上一步下载下来的代码目录（ **注意：** 目录请选择**根目录**，根目录包含有 `project.config.json`文件，请不要只选择 `wxlite` 目录！），点击确定创建小程序项目。

- step4: 再次点击【确定】进入开发者工具。

- step5: 请使用手机进行测试，直接扫描开发者工具预览生成的二维码进入。

- step6: <font color='red'>开启调试模式</font>，体验和调试内部功能。开启调试可以跳过把这些域名加入小程序白名单的工作。

<img style="border:0; max-width:100%; height:auto; box-sizing:content-box; box-shadow: 0px 0px 0px #ccc; margin: 0px 0px 0px 0px;" src="https://main.qcloudimg.com/raw/c05e7942a54a2ad41ec2066459edb528.png" />

## Demo访问的测试地址
Demo小程序会访问如下表格中的测试服务器地址，这些服务器使用的云服务是我们为大家提供的一个体验账号，平时很多客户都会在上面做测试。如果您希望使用自己的后台服务器，以免被其他客户打扰，请关注文档后一节内容：

> 我们这里只介绍 webrtc-room 的demo，其他直播标签的demo请前往[移动直播小程序](https://cloud.tencent.com/document/product/454/12554)了解

- **&lt;webrtc-room&gt; 相关demo需要访问如下地址：**

| URL | 对应的服务 |  服务器的功能描述 |
|:------:|:------:| :---------------: |
| `https://webim.tim.qq.com` | IM云通讯后台服务地址 | 用于支持小程序里面的一些消息通讯功能 |
| `https://official.opensso.tencent-cloud.com/v4/`<br>`openim/jsonvideoapp` | WebRTC音视频鉴权服务 | 用于请求进入[&lt;webrtc-room&gt;](https://cloud.tencent.com/document/product/454/16914) 所需的 userSig 和 privateMapKey |
|`https://xzb.qcloud.com/webrtc/`<br>`weapp/webrtc_room`| WebRTC房间列表后台 | 一个简单的房间列表功能，方便Demo的测试和使用。|

因此如果你需要搭建自己的服务器，需要配置以下的安全域名

| 域名 | 说明 | 
|:-------:|---------|
|`https://official.opensso.tencent-cloud.com` | WebRTC音视频鉴权服务域名[1] | 
|`https://yun.tim.qq.com` | WebRTC音视频鉴权服务域名[2] | 
|`https://room.qcloud.com`| RoomService域名 | 
|`https://webim.tim.qq.com` | IM域名 | 


## 搭建自己的账号和后台服务器
这部分我们将介绍如何将Demo默认的测试用服务器地址，换成您自己的服务器，这样一来，您就可以使用自己的腾讯云账号实现上述功能，同时也便于您进行二次开发。


#### 搭建 &lt;webrtc-room&gt; 的服务器

##### 1 这个服务器能做什么？

- 点击demo里的互动课堂 **&lt;webrtc-room&gt;** 功能，您会看到一个房间列表，这个房间列表是怎么实现的呢？

- 在看到视频房间列表以后，如果你要创建一个视频房间，或者进入一个其他人建好的视频房间，就需要为 [&lt;webrtc-room&gt;](https://cloud.tencent.com/document/product/454/16914) 所对应的几个属性（`sdkAppID`、`userID`、`userSig`、`roomID` 和 `privateMapKey`）传递合法的参数值，这几个参数值怎么获取呢？

##### 2 这个服务器要怎么搭建？

- 下载 [webrtc_server](https://github.com/TencentVideoCloudMLVBDev/webrtc_server_java) ，这是一份 java 版本的实现，根据 README.md 中的说明就可以了解怎么使用这份源码。

##### 3 服务器建好了我怎么用？

-  [小程序](https://github.com/TencentVideoCloudMLVBDev/MiniProgram) 源码中，将 `wxlite/config.js` 文件中的 `webrtcServerUrl` 修改成：
```
https://您自己的域名/webrtc/weapp/webrtc_room
```

- 小程序实现 WebRTC 能力肯定是为了跟 Chrome 浏览器进行视频通话，浏览器端的源代码可以点击 [Chrome(src)](https://github.com/TencentVideoCloudMLVBDev/webrtc_pc) 下载到，将 `component/WebRTCRoom.js` 文件中的`serverDomain`修改成：
```
https://您自己的域名/webrtc/weapp/webrtc_room
```


## 与WebRTC端互通
### Demo 体验 
用 Chrome 浏览器打开 [体验地址](https://www.qcloudtrtc.com/miniApp/index.html#/)，即可体验 Chrome（WebRTC） + 微信（小程序）的视频通话功能，如下图所示：
![](https://main.qcloudimg.com/raw/36310afb4121a945d1119c51c3334c36.png)

### 源码调试
[github地址](https://github.com/TencentVideoCloudMLVBDev/webrtc_web_source)。
> 源码及部署方式请参考github的文档
  
