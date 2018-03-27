
## 插件简介

腾讯云 QUIC 推流加速插件，能够让您的 OBS Stuidio 具备 QUIC 推流加速能力，让您获得比常规 RTMP 推流更好的网络适应性和更低的直播卡顿率。
![](https://mc.qcloudimg.com/static/img/12e966a39dc5eba5701cb2e310b16ccb/image.jpg)

插件安装后，如果是推流到腾讯云服务器，默认就会开启 QUIC 推流加速能力；如果是推流到其它云服务器，则继续使用标准 RTMP 协议进行推流。


## 使用说明

- 在 OBS Studio [官网](https://obsproject.com/)下载并安装 obs studio **20.0.0** 或以上版本。
- 点击 [DOWNLOAD](http://liteavsdk-1252463788.cosgz.myqcloud.com/windows/OBS_Plugins/liteav-stream-plugin-setup.exe) 下载 QUIC 加速插件，该插件仅能安装在 **20.0.0** 或以上版本的 OBS Studio 上。 
 ![](https://main.qcloudimg.com/raw/36db0828234c4094e20a2260d5f8c097.png)

- 插件安装完毕后，推流到腾讯云默认会开启 QUIC 加速，如果是推流到其它云服务器，则继续使用标准 RTMP 协议进行推流。
![](https://main.qcloudimg.com/raw/221ef0155c98b1ac9f9a27a59aa75e65.png)

- 可以 [开通](https://console.cloud.tencent.com/live) 腾讯云直播服务后，通过 [直播控制台>>直播码接入>>推流生成器](https://console.cloud.tencent.com/live/livecodemanage) 获取腾讯云推流地址。
