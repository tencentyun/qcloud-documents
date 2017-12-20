** 下载后直接安装即可，具体可参考: **
```
https://console.cloud.tencent.com/yunjing/index/addMachine
```

** 步骤 **
1. 检测 linux 客户端安装成功状态：
执行完安装命令后查看进程，命令为：` ps -ef|grep YD`
![image](https://mc.qcloudimg.com/static/img/25c18ce3ed1673ca7d47425c28c3b8ef/image.png)
1. 如果进程没有起来，可以手动运行进程：`/usr/local/qcloud/YunJing/YDEyes/YDService`
1. 检测 windows 安装成功状态：
打开任务管理器，查看 `YDService`，`YDLive`进程是否有调用，有调用则安装成功。
![image](https://mc.qcloudimg.com/static/img/faab29e472bfb6b446ae3963eddd6377/image.png)
1. 建议防火墙策略放过云镜后台服务器访问地址：
域名：`s.yd.qcloud.com; l.yd.qcloud.com; u.yd.qcloud.com`
端口：`5574,8080,80,9080`
