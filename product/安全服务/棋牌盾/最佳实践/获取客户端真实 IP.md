棋牌盾使用非网站业务转发规则时，源站需使用 toa 模块获取客户端的真实 IP。

## 基本原理
棋牌盾使用公网代理模式，因此数据包的源地址和目标地址均会被修改。源站看到的数据包源地址是棋牌盾实例的回源 IP，而并非是客户端的真实 IP。为了将客户端 IP 传给源站服务器，转发时棋牌盾将客户端的 IP 和 Port 记录在自定义的 tcp option 字段中。如下：
```
#define TCPOPT_ADDR  200
#define TCPOLEN_ADDR 8      /* |opcode|size|ip+port| = 1 + 1 + 6 */

/*
 * insert client ip in tcp option, now only support IPV4,
 * must be 4 bytes alignment.
 */
struct ip_vs_tcpo_addr {
    __u8 opcode;
    __u8 opsize;
    __u16 port;
    __u32 addr;
};
```

## 支持操作系统
•	CentOS 6.x
•	CentOS 7.x
>!
- Windows 操作系统不支持使用 toa 模块获取客户端的真实 IP。
- Linux 其他版本操作系统，请联系 [腾讯云技术支持](https://cloud.tencent.com/about/connect) 咨询。

## 注意事项
- 建议先在测试环境中进行安装和测试，确认功能可用、运行稳定后再部署到正式环境。
- 如需升级内核，建议升级内核前将原内核保存，以防出现升级失败等意外。
-  toa 仅支持 IPv4，若环境默认获取 IPv6 则无法正确获得客户端 IP。

## 获取客户端真实 IP
1. 以 root 用户执行以下命令，安装编译环境。
`yum install gcc kernel-headers kernel-devel -y `
2. [下载](https://daaa-1254383475.cos.ap-shanghai.myqcloud.com/TOA_CentOS_v1.zip) 安装文件并解压。
 ```
wget  https://daaa-1254383475.cos.ap-shanghai.myqcloud.com/TOA_CentOS_v1.zip
unzip TOA_CentOS_v1.zip
 ```
 <span id="step3"></span>
3. 执行`uname -r`命令，查看内核版本。
 示例：
```
[root@VM_0_2_centos toa]# uname -r
3.10.0-514.26.2.el7.x86_64
```
4. 根据 [步骤3](#step3) 的查询结果，修改 Makefile 配置文件中的路径参数 KERNEL_DIR。
示例：
```
[root@VM_0_2_centos toa]# vim Makefile 
obj-m := toa.o
KERNEL_DIR := /usr/src/kernels/3.10.0-514.26.2.el7.x86_64/
PWD := $(shell pwd)
#EXTRA_CFLAGS+=-D__GENKSYMS__
all:
        make -C $(KERNEL_DIR) M=$(PWD) modules
clean:    
        rm *.o *.ko *.mod.c  Module.symvers modules.order
```
5. 执行`make`命令进行编译。
6. 移动模块并启动加载。
```
mv toa.ko /lib/modules/`uname -r`/kernel/net/netfilter/ipvs/toa.ko
insmod /lib/modules/`uname -r`/kernel/net/netfilter/ipvs/toa.ko
```
 - 加载成功后，可正常获取真实客户端源 IP 。
 - 如果仍无法获取客户端源 IP，可执行`lsmod | grep toa`命令检测 toa 模块加载情况。

## 卸载 toa 模块
以 root 用户执行以下命令，卸载 toa 模块。
```
rmmod /lib/modules/`uname -r`/kernel/net/netfilter/ipvs/toa.ko
```
