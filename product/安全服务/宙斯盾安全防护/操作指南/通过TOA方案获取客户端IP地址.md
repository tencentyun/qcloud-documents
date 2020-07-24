业务请求经过高防 IP 的4层转发后，业务服务器端接收到报文后，其看到的源 IP 地址是高防 IP 的出口 IP 地址。为了让服务器端能够获取到用户端实际的 IP 地址，可以使用如下 TOA 的方案。在业务服务的 Linux 服务器上，安装对应的 TOA 内核包，并重启服务器后。业务侧就可以获取到用户端实际的 IP 地址。

## TOA 原理
高防转发后，数据包同时会做 SNAT 和 DNAT，数据包的源地址和目标地址均修改。
TCP 协议下，为了将客户端 IP 传给服务器，会将客户端的 IP，port 在转发时放入了自定义的 tcp option 字段。
		
    #define TCPOPT_ADDR	200  
    #define TCPOLEN_ADDR 8	/* |opcode|size|ip+port| = 1 + 1 + 6 */

    /*
    *insert client ip in tcp option, now only support IPV4,
    *must be 4 bytes alignment.
    */
    struct ip_vs_tcpo_addr {
    __u8 opcode;
    __u8 opsize;
    __u16 port;
    __u32 addr;
    }; 
Linux 内核在监听套接字收到三次握手的 ACK 包之后，会从 `SYN_REVC` 状态进入到 `TCP_ESTABLISHED` 状态。这时内核会调用 `tcp_v4_syn_recv_sock` 函数。 Hook 函数 `tcp_v4_syn_recv_sock_toa `首先调用原有的` tcp_v4_syn_recv_sock `函数，然后调用 `get_toa_data` 函数从 TCP OPTION 中提取出 TOA OPTION，并存储在 `sk_user_data` 字段中。

然后用 `inet_getname_toa hook inet_getname`，在获取源 IP 地址和端口时，首先调用原来的`inet_getname`，然后判断 `sk_user_data` 是否为空，如果有数据从其中提取真实的 IP 和 port，替换 `inet_getname` 的返回。

客户端程序在用户态调用 getpeername，返回的 IP 和 port 即为客户端的原始 IP。

## 内核包安装步骤
### Centos 6.x/7.x
安装步骤

1. 下载安装包
 (1) [Centos 6.x 下载](http://toakernel-1253438722.cossh.myqcloud.com/kernel-2.6.32-220.23.1.el6.toa.x86_64.rpm)
 (2) [Centos 7.x 下载](http://toakernel-1253438722.cossh.myqcloud.com/kernel-3.10.0-693.el7.centos.toa.x86_64.rpm)
2. 安装包文件
							
			rpm -hiv kernel-2.6.32-220.23.1.el6.toa.x86_64.rpm --force						
3. 安装完成之后重启主机

			reboot
4. 执行命令检查 toa 模块是否加载成功

			lsmod | grep toa
5. 没有加载的话手工开启
    
			modprobe toa
6. 可用下面的命令开启自动加载 toa 模块

			echo “modprobe toa” >> /etc/rc.d/rc.local
			
###  Ubuntu 16.04
下载安装包：
(1) [内核包下载](http://toakernel-1253438722.cossh.myqcloud.com/linux-image-4.4.87.toa_1.0_amd64.deb )
(2) [内核 header 包下载](http://toakernel-1253438722.cossh.myqcloud.com/linux-headers-4.4.87.toa_1.0_amd64.deb)
安装步骤：

			dpkg -i linux-image-4.4.87.toa_1.0_amd64.deb
Headers 包可不装，如需要做相关开发则安装。
安装完成之后重启主机，然后` lsmod | grep toa `检查 toa 模块是否加载 没有加载的话 `modprobe toa` 开启。
可用下面的命令开启加载 toa 模块
		
		echo “modprobe toa” >> /etc/rc.d/rc.local
		 
### Debian 8

(1) [内核包下载](http://toakernel-1253438722.cossh.myqcloud.com/linux-image-3.16.43.toa_1.0_amd64.deb)
(2) [内核 header 包下载](http://toakernel-1253438722.cossh.myqcloud.com/linux-headers-3.16.43.toa_1.0_amd64.deb)

安装方法与 Ubuntu 相同。


请根据业务服务器 Linux 操作系统的类型和版本下载对应的内核包，按如下步骤操作。如果没有和用户操作系统一致的内核包，用户还可以参考下面 TOA 源代码安装指引操作。

## TOA 源代码内核安装指引

###  源码安装

1. 下载打好[ toa 补丁](http://kb.linuxvirtualserver.org/images/3/34/Linux-2.6.32-220.23.1.el6.x86_64.rs.src.tar.gz) 的源码包，单击 toa 补丁即可下载安装包。
2. 解压。
3. 编辑 .config，将 `CONFIG_IPV6=M` 改成 `CONFIG_IPV6=y`。
4. 如果需要加上一些自定义说明，可以编辑 Makefile。
5. make -jn (n 为线程数)。
6. `make modules_install`。
7. `make install`。
8. 修改 /boot/grub/menu.lst	将 default 改为新安装的内核（title 顺序从 0 开始）。
9. Reboot 重启后即为 toa 内核。
10. `lsmode | grep toa` 检查 toa 模块是否加载	没有加载的话 `modprobe toa` 开启。

### 内核包制作

可自己制作 rpm 包，也可由我们提供。

1. 安装 kernel-2.6.32-220.23.1.el6.src.rpm 

			rpm -hiv kernel-2.6.32-220.23.1.el6.src.rpm
2. 生成内核源码目录

			rpmbuild -bp ~/rpmbuild/SPECS/kernel.spec
3. 复制一份源码目录

			cd ~/rpmbuild/BUILD/kernel-2.6.32-220.23.1.el6/ cp -a linux-2.6.32-220.23.1.el6.x86_64/ linux-2.6.32-220.23.1.el6.x86_64_new   
4. 在复制出来的源码目录中打toa 补丁

			cd ~/rpmbuild/BUILD/kernel-2.6.32-220.23.1.el6/linux-2.6.32-220.23.1.el6.x86_64_new/ 
			patch -p1 < /usr/local/src/linux-2.6.32-220.23.1.el6.x86_64.rs/toa-2.6.32-220.23.1.el6.patch
5. 编辑.config 并拷贝到 SOURCE 目录

			sed -i 's/CONFIG_IPV6=m/CONFIG_IPV6=y/g' .config 
			echo -e '\n# toa\nCONFIG_TOA=m' >> .config
			cp .config ~/rpmbuild/SOURCES/config-x86_64-generic
6. 删除原始源码中的.config

			cd ~/rpmbuild/BUILD/kernel-2.6.32-220.23.1.el6/linux-2.6.32-220.23.1.el6.x86_64 
			rm -rf .config
7. 生成最终 patch
    
			cd ~/rpmbuild/BUILD/kernel-2.6.32-220.23.1.el6/
			diff -uNr linux-2.6.32-220.23.1.el6.x86_64 linux-2.6.32-220.23.1.el6.x86_64_new/ >
			~/rpmbuild/SOURCES/toa.patch
8. 编辑 kernel.spec

    vim ~/rpmbuild/SPECS/kernel.spec
在ApplyOptionPath 下添加如下两行（还可修改 buildid 等自定义内核包名） 

			Patch999999: toa.patch
    ApplyOptionalPatch toa.patch
9. 制作 rpm 包

			rpmbuild -bb --with baseonly --without kabichk --with firmware --without debuginfo --target=x86_64 ~/rpmbuild/SPECS/kernel.spec
10. 安装内核 rpm 包
		 rpm -hiv kernel-xxxx.rpm --force
	 
重启，加载 toa 模块





