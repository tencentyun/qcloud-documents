## PING 127.0.0.1出现错误怎么办？
Windows 运行一段时间以后，由于系统本身原因或第三方软件，有可能出现PING失败，启动后出现环回地址127.0.0.1不存在的现象。可尝试使用下面的方法解决。

问题举例如下图：
![](//mccdn.qcloud.com/static/img/ff82d382b0bdfa9c2163e80e1e90815d/image.png)

腾讯提供了zipconfig_service服务来配置和修复IP地址错误，以上错误可以下载该服务的升级包来修复。

执行方法：下载工具包zipconfig\_update1.0.0.6.zip，解压后执行里面的zipconfig\_update.bat。
内网地址：http://mirrors.tencentyun.com/install/windows/zipconfig_update1.0.0.6.zip

执行后示例如下：
![](//mccdn.qcloud.com/static/img/7ff1fc9dc1a9ff9201eea4237e6c6148/image.png)
执行后，一般情况下不需要重启计算机。

## Windows系统制作自定义镜像失败怎么办？
若windows系统制作镜像失败，请依次做如下检查。

1) 请确保以下服务正常运行
<table class="t">
<tbody><tr>
<th width="100"> <b>程序名</b>
</th><th width="100"><b>安装位置</b>
</th><th width="100"><b>服务名称</b>
</th></tr>
<tr>
<td>QcloudService.exe
</td><td>C:\Windows\
</td><td>Qcloud服务
</td></tr>
<tr>
<td>WinAgent.exe
</td><td>C:\WinAgent\
</td><td>WinAgent Display Name
</td></tr>
<tr>
<td>win-agent.exe
</td><td>C:\win-agent\
</td><td>win-agent
</td></tr></tbody></table>

请确保以上服务以及所有腾讯云官方提供的以 Win_Agent 开头的服务运行正常。

2) 自定义镜像制作依赖微软自带的Windows Modules Installer服务，请确保该服务运行正常。

3) 一些杀毒工具或安全狗拦截自定义镜像制作脚本的执行，为避免制作失败，建议在制作自定义镜像前先关闭这些工具。

4) 若以上三步仍不能解决问题，可能是由于云服务器内部的一些设置，导致镜像制作工具在执行时被系统弹窗所中断，请远程登录云服务器查看并调整云服务器设置避免弹窗。