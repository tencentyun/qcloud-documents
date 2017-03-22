**1. 安全加固组件在机器上检查时为正常连接状态，但在云安全控制台页面上显示状态异常，该怎么处理？**
答：可能是安全加固组件出现了故障，建议卸载后重新下载安装。
Linux系统下，请登录云服务器使用如下命令下载安装包。
wget mirrors.tencentyun.com/install/sec/agent.zip

windows系统下，请在云服务器浏览器中通过以下地址下载安装包。（目前支持win2003、win2008和win2012）
<br>mirrors.tencentyun.com/install/windows/win-Agent-install.exe
<br>(域名为腾讯云内网域名，请使用腾讯云服务器访问该链接下载)

**2. 安全加固组件在云安全控制台显示状态异常，怎么办？**
答：安全加固组件出现异常，一般是两种情况：未安装组件和组件故障。
   若未安装安全组件，可直接根据页面上方的安装指导进行安装；
   若已安装安全组件，请先检查组件连接状态，具体操作方法请参考www.qcloud.com/doc/product/296/2222


**3. 安全加固组件如何重启？**
答：Windows系统下，
执行:
“net stop winagent”
“net start winagent”
即可重启成功。
Linux系统下，
以root权限执行/usr/local/sa/agent/restart.sh。
然后调用/usr/local/sa/agent/check.sh检查是否重启成功。
