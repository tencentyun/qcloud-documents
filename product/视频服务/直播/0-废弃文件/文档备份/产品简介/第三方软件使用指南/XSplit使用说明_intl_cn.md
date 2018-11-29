说明：本文档用来指导用户使用直播软件XSplit进行直播发布。
1.	下载XSplit并注册帐号
登录网站https://www.xsplit.com/download，下载XSplit，选择XSplit Broadcast进行下载
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/XSplit-1.png)
右上角点击注册帐号的接口，然后去邮箱激活。下载完成后，安装软件，打开软件，输入账号密码登录。在登录后会提示购买软件，等几秒后点击右下角Continue即可，若有更多功能需要，可以购买该软件。下图是登陆成功后的主界面。
2.	添加直播资源
见下图，XSplit软件支持的直播资源包括屏幕捕捉、游戏捕捉、媒体文件（图像、视频、HTML）、网络摄像机、采集卡和视频设备，左击菜单栏的添加资源按钮即可自行选择。
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/XSplit-2.png)
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/XSplit-3.png)
以添加视频资源为例，在选择了视频资源后，主界面的直播区如下图
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/XSplit-4.png)
3.	设置直播参数
XSplit提供直播的视频的分辨率和帧率的设置，如下，单击菜单栏的“查看”进行设置
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/XSplit-5.png)
关于视频的参数设置，可以右击视频，即可以进行设置。
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/XSplit-6.png)
4.	添加直播频道
选择好直播资源，设置好参数，下面进行添加频道进行视频广播发布，按照（“广播”菜单项——“添加频道”——custom RTMP）操作后，频道属性设置界面。
在频道属性界面，主要输入频道名、RTMP URL、Stream Name，其他可以保持默认不变。
当前视频编码支持x264，音频支持AAC。
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/XSplit-7.png)
其中完整的RTMP地址与频道属性中RTMP URL和Stream Name的对应关系如下所示：
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/XSplit-8.png)
5.	开启/结束直播推流
加入频道test后，在广播菜单项下会多一个test子选项，单击即可以开启/结束直播推流，在开启直播推流后，见下图，在标题栏会显示推流进度。
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/XSplit-9.png)
注意事项
Q1：在登录XSplit时，可能会报出如下的警告“port 443 is blocked”。
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/XSplit-10.png)
这时可以点击图中“here”链接参考网页http://xspl.it/how-to-unblock-port-443。若还是没有解决443端口堵塞的问题，可以参考网页http://chris-wang.iteye.com/blog/297663。

Q2：如果我想直播桌面，那该怎么添加直播资源？
按照添加资源——屏幕捕捉操作后，选择捕捉区域时，点击桌面就是直播整个桌面的内容，点击一个窗口的内部就只直播这个窗口。

Q：如果还有其他的问题，可以参考什么？
推荐参考XSplit软件的使用说明http://api.xsplit.com/broadcaster/help/