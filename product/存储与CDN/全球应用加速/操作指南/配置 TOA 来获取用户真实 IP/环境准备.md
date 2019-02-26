###  下载文件
- [下载地址>>](https://mc.qcloudimg.com/static/archive/5e5b31b327f3bbdd395ce426cccc3d08/windows_toa.zip)

- 解压密码：Qcloud
- 文件说明：
WinPcap_4_1_3.exe：WinPcap 驱动，详细说明可参见 [WinPcap 文档](https://www.winpcap.org/)。
lib_toa.lib：静态库。
toa_fetcher.h：静态库依赖的头文件。
pcap.h：静态库依赖的头文件。

###  安装和添加
1. 安装 winpcap 驱动：双击 WinPcap_4_1_3.exe（不需重启系统）。
2. 添加 lib_toa.lib 到服务端工程的 lib 库路径下。
3. 添加 toa_fetcher.h，pcap.h 到服务端工程的头文件中。
