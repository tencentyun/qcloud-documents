
### 腾讯视频云OBS推流插件

腾讯视频云OBS推流插件，让OBS-studio(版本20.0.0及以上)推流的同时，增加了RTMP-UDP加速通道和推流质量上报的支持。如果是推流到腾讯云服务器，会启用 UDP 加速能力，开启 UDP 加速后的推流质量会比标准 RTMP 推流有更好的网络波动抵抗力，同时可以获得更好的推流速度，从而改善当前直播流的观看体验，降低全局卡顿率。如下是一组在客户现场环境下测试的对比结果：
![](https://mc.qcloudimg.com/static/img/12e966a39dc5eba5701cb2e310b16ccb/image.jpg)

**仅支持推264流**

#### 使用说明

 [下载](http://liteavsdk-1252463788.cosgz.myqcloud.com/windows/OBS_Plugins/liteav-stream-plugin-setup.exe)插件安装
 
 **需要OBS-Studio 20.0.0及以上版本**
 
![](https://main.qcloudimg.com/raw/36db0828234c4094e20a2260d5f8c097.png)


目标文件夹：插件安装包会自动检测OBS studio的安装目录，检测失败需要手动选择OBS studio安装的根目录

OBS设置-流-流类型选择Tencent Stream Service，填写推流地址，正常推流即可。

获取测试URL
[开通](https://console.cloud.tencent.com/live)直播服务后，可以使用 [直播控制台>>直播码接入>>推流生成器](https://console.cloud.tencent.com/live/livecodemanage) 生成推流地址，详细信息可以参考 [获得推流播放URL](https://cloud.tencent.com/document/product/454/7915)。

![](https://main.qcloudimg.com/raw/221ef0155c98b1ac9f9a27a59aa75e65.png)

