### 方法一：直接下载源码并加载模块

1. 根据腾讯云上 Linux 的版本，下载对应的 TOA 包并解压。
	- **arm64**
		- [kernel-4.18.0 ](https://gaap-1251337138.file.myqcloud.com/kernel-4.18.0.rar)
	- **centos**
		- [CentOS 6.5 64](https://gaap-1251337138.file.myqcloud.com/CentOS%206.5%2064.rar)
		- [CentOS 7.2 64](https://gaap-1251337138.file.myqcloud.com/CentOS%207.2%2064.rar)
		- [CentOS 7.3 64](https://gaap-1251337138.file.myqcloud.com/CentOS%207.3%2064.rar)
		- [CentOS 7.4 64](https://gaap-1251337138.file.myqcloud.com/CentOS%207.4%2064.rar)
		- [CentOS 7.5 64](https://gaap-1251337138.file.myqcloud.com/CentOS%207.5%2064.rar)
		- [CentOS 7.6 64](https://gaap-1251337138.file.myqcloud.com/CentOS%207.6%2064.rar)
		- [CentOS 7.7 64](https://gaap-1251337138.file.myqcloud.com/CentOS%207.7%2064.rar)
		- [CentOS 7.8 64](https://gaap-1251337138.file.myqcloud.com/CentOS%207.8%2064.rar)
		- [CentOS 7.9 64](https://gaap-1251337138.file.myqcloud.com/CentOS%207.9%2064.rar)
		- [CentOS 8.0 64](https://gaap-1251337138.file.myqcloud.com/CentOS%208.0%2064.rar)
		- [CentOS 8.2 64](https://gaap-1251337138.file.myqcloud.com/CentOS%208.2%2064.rar)
	- **debian**
		- [Debian 8.2 64](https://gaap-1251337138.file.myqcloud.com/Debian%208.2%2064.rar)
		- [Debian 9.0 64](https://gaap-1251337138.file.myqcloud.com/Debian%209.0%2064.rar)
		- [Debian 10.2 64](https://gaap-1251337138.file.myqcloud.com/Debian%2010.2%2064.rar)
	- **suse linux**
		- [SUSE Linux Enterprise Server 11 SP3 64](http://toamodule-1253438722.file.myqcloud.com/SUSE%20Linux%20Enterprise%20Server%2011%20SP3%2064.zip)
		- [SUSE Linux Enterprise Server 12 64](http://toamodule-1253438722.file.myqcloud.com/SUSE%20Linux%20Enterprise%20Server%2012%2064.zip)
		- [SUSE Linux Enterprise Server 12 SP3 64](https://gaap-1251337138.file.myqcloud.com/SUSE%20Linux%20Enterprise%20Server%2012%20SP3%2064位.rar)
	- **ubuntu**
		- [Ubuntu Server 14.04.1 LTS 64](https://gaap-1251337138.file.myqcloud.com/Ubuntu%20Server%2014.04.1%20LTS%2064.rar)
		- [Ubuntu Server 16.04.1 LTS 64](https://gaap-1251337138.file.myqcloud.com/Ubuntu%20Server%2016.04.1%20LTS%2064.rar)
		- [Ubuntu Server 18.04.1 LTS 64](https://gaap-1251337138.file.myqcloud.com/Ubuntu%20Server%2018.04.1%20LTS%2064.rar)
		- [Ubuntu Server 20.04.1 LTS 64](https://gaap-1251337138.file.myqcloud.com/Ubuntu%20Server%2020.04.1%20LTS%2064.rar)
2. 解压完成后，执行 cd 命令进入刚解压的文件夹里，执行加载模块的指令：
```
insmod toa.ko
```
3.	执行下面指令确认是否已加载成功：
```
lsmod | grep toa
```
![](https://qcloudimg.tencent-cloud.cn/raw/1282241c425616a4ad4aa343ca5d4ee4.png)
4. 加载成功，在启动脚本里面加载 toa.ko 文件（重启机器 ko 文件需要重新加载）。
```
echo "insmod   xxxxx /toa.ko" >> /etc/rc.local
```
5.	（可选）临时关闭 TOA ：rmmod 路径/模块名。
```
rmmod toa.ko
```
6.	（可选）若不再需要使用 TOA 模块，执行以下命令进行卸载。
```
rmmod toa
```
7.	（可选）执行以下命令确认 TOA 模块是否卸载成功。若提示“TOA unloaded”，则说明卸载成功。
```
dmesg -T
```

### 方法二：自行编码并加载模块

若上述下载文件中没有您的操作系统版本对应的安装包，请下载 Linux 通用版的源码包，进行编译后获取（以CentOS 环境为例）。

1. 获取源码包
```
wget "https://thunder-pro-mainland-1258348367.cos.ap-guangzhou.myqcloud.com/gaap-toa.rar"
```

2.	安装编译环境。
```
yum install gcc 
yum install make
yum install kernel-headers kernel-devel –y
```
3.	解压源码包。
```
tar zxf gaap-toa.rar
```
4.	进入 TOA 目录。
```
cd toa
```
5.	编译 make。
```
make
```
6.	移动并加载模块。
```
mv toa.ko /lib/modules/`uname -r`/kernel/net/netfilter/ipvs/toa.ko

insmod /lib/modules/`uname 
¬-r`/kernel/net/netfilter/ipvs/toa.ko
```
7.	查看是否加载成功。
```
lsmod | grep toa
```
