Windows Server 上需要配置高性能电源管理选项，才能支持实例软关机，否则控制台只能通过硬关机的方式关闭实例。
以下配置电源管理的方法以 Windows 2012 举例：
>**注意：**
>修改电源管理不需要重启计算机。

1. 登录您的腾讯云云服务器。
2. 打开实例的浏览器，到内网下载腾讯云电源修改和配置工具，另存到 C 盘。
内网下载地址：http://mirrors.tencentyun.com/install/windows/power-set-win.bat
3. 在控制台执行该工具，执行完以后使用 `powercfg -L` 语句查看当前电源管理方案。
 ![](//mccdn.qcloud.com/img56b1bee8a8fbf.png)
4. 在实例中【控制面板】>【系统和安全】>【电源选项】中修改显示器和硬盘的空闲关闭时间。
 ![](https://mc.qcloudimg.com/static/img/462c9739f3de3c65b346bb47f915dd0a/18.png)



