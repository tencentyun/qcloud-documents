说明：本文档用来指导用户使用直播软件FMLE进行直播发布。

注意：FMLE 在多种操作系统都可以正常使用，支持通过摄像头，进行单独音频、单独视频、音视频混合的现场录制、直播，因此必须保证运行FMLE的机器上面安装有摄像头装置，使用相对比较简单，建议在直播过程中关掉预览功能，这样可以降低系统资源的消耗。但不支持抓屏等功能，建议在需要抓屏功能时，还是使用OBS或XSplit。
1.	下载和安装软件FMLE
进入adobe官方网页：http://offers.adobe.com/en/na/leap/landings/fmle3.html，填写完右侧的相关信息，就可以进入下载页面，选择合适的版本进行下载和安装。
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/FMLE-1.png)
2.	设置推流地址（FMS URL + Stream）
在右下角的“Stream to Flash Media Server”面板中，设置推流地址，由FMS URL和Stream组成，如下图所示，同时，可以选择是否保存当前录制的视频到文件中。
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/FMLE-2.png)
其中完整的RTMP地址与推流地址中FMS URL和Stream的对应关系如下所示：
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/FMLE-3.png)
设置好了FMS URL和Stream后，单击Connect即可以与推流服务端建立连接。
3.	配置直播的音频和视频
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/FMLE-4.png)
在上图的video面板中，可以设置视频的设备、格式、码率和分辨率等等，在上图的audio，可以设置音频输入设备、格式(当前支持AAC)、频道、采样频率、比特率以及声音大小，可以按需进行选择。
4.	开始编码推送
在配置好音视频后，单击“start”按钮，就可以开始推送。
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/FMLE-5.png)
●  注意事项
●  如果还有其他的问题可以参考FMLE官方文档：
    http://help.adobe.com/en_US/FlashMediaLiveEncoder/3.2/Using/index.html