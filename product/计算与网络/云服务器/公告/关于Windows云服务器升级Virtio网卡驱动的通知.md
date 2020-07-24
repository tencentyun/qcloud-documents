为了防止2016年6月－8月中旬创建的 Windows 云服务器极端情况下出现断网的问题，极端情况下可能影响到您正常业务的运行。我们提供升级程序升级 Virtio 网卡驱动，建议您按照以下升级建议安装升级程序，重启即可解决该问题。

腾讯云客户可通过以下内网地址下载升级程序，一键完成升级。用户需要 [登录 Windows 云服务器](https://cloud.tencent.com/document/product/213/5435)，并在内部访问镜像站点 `http://mirrors.tencentyun.com/install/windows/update_netkvm.exe`，下载后直接运行升级程序或保存后运行。
- 如果显示以下信息：表示驱动已经升级成功，重启系统后新的驱动生效。
![](//mc.qcloudimg.com/static/img/fed07b4028a0a281106166a7e07aa7f7/image.png)
- 如果显示以下信息：表示现有驱动没有问题，不需要升级。
![](//mc.qcloudimg.com/static/img/895ad7fd0d6e6bb58ae1eb21de9b6a12/image.png)
