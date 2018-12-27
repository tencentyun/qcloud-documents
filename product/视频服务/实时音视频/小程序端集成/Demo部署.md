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

- step1: 访问 [SDK + Demo](https://gitee.com/vqcloud/MiniProgram-TRTC)，获取小程序 Demo 源码。

- step2: 打开安装的微信开发者工具，点击【小程序项目】按钮。

- step3: 输入小程序 AppID，项目目录选择上一步下载下来的代码目录（ **注意：** 目录请选择**根目录**，根目录包含有 `project.config.json`文件），填写自己的小程序的AppID，点击确定创建小程序项目。

- step4: 再次点击【确定】进入开发者工具。

- step5: 请使用手机进行测试，直接扫描开发者工具预览生成的二维码进入。

- step6: <font color='red'>开启调试模式</font>，体验和调试内部功能。开启调试可以跳过把这些域名加入小程序白名单的工作。

<img style="border:0; max-width:100%; height:auto; box-sizing:content-box; box-shadow: 0px 0px 0px #ccc; margin: 0px 0px 0px 0px;" src="https://main.qcloudimg.com/raw/44ec8f6bb6c1e24abb1e9920b7ec2a50.png" />

## webrtc-room组件会访问以下地址

- **&lt;webrtc-room&gt; 组件内部需要访问如下地址：**

> 将以下域名在[微信公众平台](https://mp.weixin.qq.com)-开发-开发设置-服务器域名配置

| 域名 | 说明 | 
|:-------:|---------|
|`https://official.opensso.tencent-cloud.com` | WebRTC音视频鉴权服务域名[1] | 
|`https://yun.tim.qq.com` | WebRTC音视频鉴权服务域名[2] | 
|`https://cloud.tencent.com`| 推流域名 | 
|`https://webim.tim.qq.com` | IM域名 |
