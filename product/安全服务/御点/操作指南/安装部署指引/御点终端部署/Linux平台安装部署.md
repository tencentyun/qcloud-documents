1. 若计算机系统为 Linux，请下载 Linux 版的御点进行安装。64位系统请下载 Linux x64 的版本进行安装，32位系统请下载 Linux x86 进行安装，将下载的压缩文件拷贝或传输到目标 Linux 主机上。
![](https://main.qcloudimg.com/raw/9965bda7e1ef45616fdf40232de59ef0.png)
2. 解压 zip 安装包。
```
[root@localhost ft_local]# unzip
PCMgr_Setup_Linux64_cfg(192.168.126.190_80).zip
Archive: PCMgr_Setup_Linux64_cfg(192.168.126.190_80).zip
```
3. 获取 root 权限。执行 `su`命令，并输入 root 密码。
4. 执行以下命令，进入到安装目录。
` [root@localhost ft_local]# cd linux64_(2.0.138.146)`
5. 执行以下命令，修改文件权限。
` [root@localhost linux64_(2.0.138.146)]# chmod 777 *`
6. 执行`./install.sh`进行安装。
![](https://main.qcloudimg.com/raw/499428d1fa11aec843e1f9d6754b7cd3.png)
7. 观察进程是否启动。
	- 执行`ps aux|grep TavDaemon`命令，若如下图所示说明进程已启动。
![](https://main.qcloudimg.com/raw/f9dc60baf693ae8efb89c41054b77f5c.png)
	- 或使用`systemctl status tavd`命令，观察进程是否启动。
![](https://main.qcloudimg.com/raw/6b1937b01ae1044d21c2a0bfe22a3d0c.png)
8. 检查御点控制中心 Linux 终端是否在线。在御点控制中心 Web 界面选择 Linux 版本查看，如下图所示 Linux 终端已上线。
![](https://main.qcloudimg.com/raw/9de18780439123e23476f2c4c4edc22d.png)
若 Linux 终端不在线，请检查配置文件的服务器 IP 和端口是否设置正确。检查方法：回到 Linux 终端查看`vi/usr/local/bin/tavdaemon.cfg`如下所示，请确保 IP 和端口正确。  
![](https://main.qcloudimg.com/raw/34f3efa5c85cbd90e469212b129a071a.png)
9. 查看日志。如需查看 Linux 终端日志，可以在`/opt/tav/log/scanlog/`目录下创建 logopen 文件，即可在该目录下查看到日志：
![](https://main.qcloudimg.com/raw/afbff95ed396c4f3b8f07cb39aac5595.png)
若 Linux 终端发生异常情况，无法定位 Linux 御点是否有异常，请将日志交给后台管理员进行分析定位。
