## 下载地址
[内核包下载地址>>](http://toakernel-1253438722.cossh.myqcloud.com/linux-image-4.4.87.toa_1.0_amd64.deb)


[内核 Headers 包下载地址>>](http://toakernel-1253438722.cossh.myqcloud.com/linux-headers-4.4.87.toa_1.0_amd64.deb)

## 安装方法
Headers 包为选装，可在需要做相关开发时再安装。请先安装内核包。

1. 执行下面的指令，安装内核包：
`dpkg -i linux-image-4.4.87.toa_1.0_amd64.deb`

2. 安装完成后请重启主机。

3. 执行 `lsmode | grep toa` 检查 toa 模块是否加载，若没加载，可通过 `modprobe toa` 开启，执行命令如下：
`echo “modprobe toa” >> /etc/rc.d/rc.local`
