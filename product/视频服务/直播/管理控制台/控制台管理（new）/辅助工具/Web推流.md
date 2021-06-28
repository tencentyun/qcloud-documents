## 操作场景
腾讯云为您提供 Web 推流功能，可实现快速生成推流地址，在线推流测试直播功能。

## 前提条件
- 已登录 [云直播控制台](https://console.cloud.tencent.com/live)。
- 已添加 [推流域名](https://cloud.tencent.com/document/product/267/20381)。
- 您的设备已安装摄像头，并浏览器支持 Flash 插件调用摄像头权限。

## 操作步骤
1. 登录云直播控制台，选择[【Web推流】](https://console.cloud.tencent.com/live/tools/webpush)。
2. 在 Web 端推流的页面进行以下设置：
	- 选择推流域名。
	- 编辑 AppName，用于区分同一个域名下多个 App 的地址路径，默认值为 live。
	- 填写自定义的流名称 StreamName，例如：`test`。
	- 选择过期时间，例如：`2021-04-02 16:37:54`。
	- 选择分辨率。默认为auto。
3. 单击【开始推流】，授权允许调用摄像头，即可开始推流。
![](https://main.qcloudimg.com/raw/84d9678499c81ae77a714986010a0a61.png)
4. 若您在【域名管理】中已添加播放域名，即可在下方查看对应生成的播放地址。其中，播放地址由以下4部分组成：
![](https://main.qcloudimg.com/raw/72989c8f55fe7f2ed596bd09882f5a09.png)
支持 RTMP、FLV 和 HLS 协议，可以单击播放地址后的二维码，通过 [腾讯云工具包 App](https://cloud.tencent.com/document/product/454/6555#rtmpdemo) 扫码查看播放地址：
![](https://main.qcloudimg.com/raw/431c2120c6460ba5953d6a1948f687a1.png)
