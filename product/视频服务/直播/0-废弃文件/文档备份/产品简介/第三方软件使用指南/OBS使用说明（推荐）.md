如下为第三方直播软件使用方法。用户可以借助这些软件实现上行RTMP推流。
注意：当前RTMP输入推流端编码支持视频H.264编码，音频AAC编码，码率建议不超过1.5Mbps。
	
1.	什么是OBS
OBS是用于推送直播视频源到服务器的工具,可以到下面下载链接根据操作系统类型进行下载
下载连接:https://obsproject.com/download

2.	快速入门
安装结束后，打开主界面，选择设定
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/OBS-1.png)
获取直播源的入口
在控制台直播源设置处，单击复制按钮，将地址复制到剪贴板,获得地址
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/OBS-2.png)
在广播设定处填写FMS url 
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/OBS-3.png)
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/OBS-4.png)
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/OBS-5.png)
单击开始串流，就可以进行直播了
\
查看直播是否发送推流，可以在状态栏处查看速度等内容
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/OBS-6.png)
3.	常见问题和处理技巧
●  提示80004005错误处理办法
去微软官网下载相关更新
1)  DIRECTX
下载链接 http://www.microsoft.com/zh-cn/download/details.aspx?id=35
2)  VC++ 2008
下载连接 http://www.microsoft.com/zh-cn/download/details.aspx?id=5582
3)  NET FRAMEWORK 4.0
下载链接 http://www.microsoft.com/zh-cn/download/details.aspx?id=24872
●  视频清晰度相关设置
这部分取决于带宽。
在 设置 -> 编码处设置最大比特率和品质,品质值越大视频质量越高, 当前音频编码支持AAC方式。
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/OBS-7.png)
附分辨率与建议码率图![]()
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/OBS-8.png)
分辨率设定
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/OBS-9.png)
●  录制视频路径设置
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/OBS-10.png)
●  音画不同步问题
在设定->高级处，启用固定帧率
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/OBS-11.png)
●  其他视频来源(电脑摄像头，窗口)
您可能需要播放摄像头，某个窗口，或者游戏内容或者同时播放多个窗口
●  使用摄像头设备
打开您所使用的摄像头应用程序，然后在主界面空白处右键添加视频设备捕捉
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/OBS-12.png)
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/OBS-13.png)
●  捕获某个窗口内容
在主界面来源空白处右击->添加->捕获窗口
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/OBS-14.png)
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/OBS-15.png)
