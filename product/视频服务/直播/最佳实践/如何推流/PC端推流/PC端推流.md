# PC端推流

   腾讯云PC直播是在PC（windows/mac）上借助安装的推流软件OBS（推荐）或者XSplit向腾讯视频云的推流地址，推送经过压缩编码现场活动、教学、投影或者游戏等画面，同时观众可以通过和推流地址相对应的播放地址收看实时画面。
	 ![](https://main.qcloudimg.com/raw/67cdbb198cbdaf68d63f2993f12a8d17.png)
	
## 直播前准备
安装推流软件
OBS 安装
可以到[OBS官网](https://obsproject.com/download)下载相应的安装包，按照默认设置进行安装，OBS支持 Windows/Mac/Linux 等系统，确认是Open Broadcaster Software，OBS也提供OBS Studio，不是本文介绍的软件。
XSplit 安装
也可以到[XSplit官网](https://www.xsplit.com/zh-cn)下载安装包，安装默认设置进行安装，XSplit 是收费的，如果预算不够的话，推荐用OBS（Free）。XSplit游戏直播有单独的安装包，非游戏直播推荐使用BroadCaster。

## 推流
1. 登录 [视频直播控制台](https://cloud.tencent.com/login?s_url=https%3A%2F%2Fconsole.cloud.tencent.com%2Flive)。
2. 单击**域名管理**， 选择您创建的推流域名。
3. 使用**管理**中**推流配置**里面的推流地址生成器。
4. 输入**过期时间**和**StreamName**。
5. 单击**生成推流地址**。
6. 设置推流地址
假设准备好的推流地址为：rtmp://3891.livepush.myqcloud.com/live/3891_test?bizid=3891&txSecret=xxx&txTime=58540F7F

  设置时会分为前后两部分进行设置：
  其中推流地址前半部分rtmp://3891.livepush.myqcloud.com/live/，一般被称为 FMS URL；
推流地址的后半部分3891_test?bizid=3891&txSecret=xxx&txTime=58540F7F，一般被称为串流码。

  OBS推流地址设置
	 关于OBS推流工具的使用及设置，详情参见[OBS推流]()。
此处obs版本为19.0.3，单击界面右下角【设置】选中【流】，依次配置串流类型为【自定义流媒体服务器】、URL 为推流地址的前半部分、流密钥为推流地址的后半部分。
![](https://main.qcloudimg.com/raw/e6ae494cf56cca6025951f8507d78d08.jpg)


## 播流
1. 确认播放地址。
如果推理地址（livepush）为：`rtmp://3891.livepush.myqcloud.com/live/3891_test?bizid=3891&txSecret=xxx&txTime=58540F7F`，那么播放地址（liveplay）即：

| 播放协议 | 播放地址 | 
|---------|---------|
| RTMP |  [rtmp://3891.<font color='red'>liveplay</font>.myqcloud.com/live/3891_test]() |
| FLV | [http://3891.<font color='red'>liveplay</font>.myqcloud.com/live/3891_test.flv]() |
| HLS(m3u8) | [http://3891.<font color='red'>liveplay</font>.myqcloud.com/live/3891_test.m3u8]() |

 这里推荐使用flv播放。

2. 下载 [VLC](http://www.videolan.org/vlc/)，安装按照默认设置即可。本文中VLC版本为2.2.4。
3. 打开后单击【媒体菜单】，选择【打开网络串流】，填写播放地址，再单击【播放】。
![](https://main.qcloudimg.com/raw/4f53fbc0a0c559d849e8379e3d1374f1.jpg)

4. 或者 [下载 RTMP DEMO](https://cloud.tencent.com/document/product/454/6555)，将播放地址用在线二维码 [生成器](http://cli.im/) 生成二维码后，即可扫码播放。
