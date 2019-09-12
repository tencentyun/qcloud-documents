根据腾讯云上 Linux 的版本，下载对应的 TOA 包解压：
-   [CentOS 7.2 64](http://toamodule-1253438722.file.myqcloud.com/CentOS%207.2%2064.zip)
-  [CentOS 7.3 64](http://toamodule-1253438722.file.myqcloud.com/CentOS%207.3%2064.zip)
-  [CentOS 7.4 64](http://toamodule-1253438722.file.myqcloud.com/CentOS%207.4%2064.zip)
- 	[Debian 8.2 64](http://toamodule-1253438722.file.myqcloud.com/Debian%208.2%2064.zip)
-  [Debian 9.0 64](http://toamodule-1253438722.file.myqcloud.com/Debian%209.0%2064.zip) 
-   [SUSE Linux Enterprise Server 11 SP3 64](http://toamodule-1253438722.file.myqcloud.com/SUSE%20Linux%20Enterprise%20Server%2011%20SP3%2064.zip)
-  [SUSE Linux Enterprise Server 12 64](http://toamodule-1253438722.file.myqcloud.com/SUSE%20Linux%20Enterprise%20Server%2012%2064.zip)
-  [Ubuntu Server 14.04.1 LTS 64](http://toamodule-1253438722.file.myqcloud.com/Ubuntu%20Server%2014.04.1%20LTS%2064.zip)
-  [Ubuntu Server 16.04.1 LTS 64](http://toamodule-1253438722.file.myqcloud.com/Ubuntu%20Server%2016.04.1%20LTS%2064.zip) 


1. 解压完成后，执行 cd 命令进入到刚解压的文件夹里，执行加载模块的指令：
```
insmod toa.ko
``` 
2. 执行下面指令确认是否已加载成功：
```
lsmod | grep toa
```
3. 如已加载成功，最后在启动脚本里面加载 toa.ko 文件即可（重启机器 ko 文件需要重新加载）。


如果上述下载文件中没有您的操作系统版本对应的安装包，可以下载 Linux 通用版的源码包，编译后获取，该版本支持 Centos6.9 和 Centos7、Ubuntu14.04 等绝大多数的 Linux 发行版：
1. 获取源码包
```
wget http://toamodule-1253438722.file.myqcloud.com/tencenttoa.zip
```
2. 编译文件
```
yum install gcc
yum install kernel-headers
yum install kernel-devel
```
3. 加载 toa.ko 文件
```
tar -zxvf linux_toa.tar.gz
cd toa
make
mv toa.ko /lib/modules/`uname -r`/kernel/net/netfilter/ipvs/toa.ko
insmod /lib/modules/`uname -r`/kernel/net/netfilter/ipvs/toa.ko
```
