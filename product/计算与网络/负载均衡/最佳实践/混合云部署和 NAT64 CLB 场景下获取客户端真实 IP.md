本文介绍混合云部署场景和 NAT64 CLB 场景下的 CLB 的四层（仅 TCP）服务如何通过 TOA 获取客户端真实源 IP。
<dx-steps>
-[控制台开启 TOA](#loadopentoa)
-[加载 TOA 模块](#load-toa)
-[适配后端服务](#adapt-rs)
-[（可选）监控 TOA 模块状态](#monitor-toa)
</dx-steps>

>?
>- 仅北京地域支持通过 TOA 获取客户端真实源 IP。
>- 仅四层 TCP 支持通过 TOA 获取客户端真实源 IP，UDP 和七层（HTTP/HTTPS）不支持获取。
>- 该功能目前处于内测中，如需使用，请提交 [工单申请](https://console.cloud.tencent.com/workorder/category?level1_id=6&level2_id=163&source=0&data_title=%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1%20CLB&level3_id=1068&radio_title=%E9%85%8D%E9%A2%9D/%E7%99%BD%E5%90%8D%E5%8D%95&queue=96&scene_code=41669&step=2)。
>


## 应用场景
### 混合云部署场景
在 [混合云部署](https://cloud.tencent.com/document/product/214/48181) 中，IDC 的 IP 和云上 VPC 的 IP 可能会有地址重叠，因此需要配置 SNAT IP，进行 SNAT 转换源 IP。对于服务端而言，无法获得真实源 IP，因此需要通过 TOA 进行获取。

### NAT64 CLB 场景
在 NAT64 CLB 场景中，客户端真实的 IPv6 源 IP 会被转换成 IPv4 的公网 IP，因此对于真实的服务端的服务而言，无法获得真实的客户端 IPv6 IP。
腾讯云 NAT64 CLB 提供获取客户端真实 IP 的功能，即将客户端真实的源 IP 放入 TCP 协议的自定义 option 中，当被嵌入真实源 IP 的 TCP 数据包发往服务端时，服务端插入的 TOA 内核模块可提取 TCP 数据包中的真实客户端源 IP，此时客户端应用只需要调用 TOA 内核模块提供的接口即可获取真实客户端源 IP。


## 限制说明
<dx-accordion>
::: 资源限制
- 编译 TOA 内核模块环境的内核版本需要与服务所在环境的内核版本一致。
- 容器环境下需要在宿主机中加载 TOA 内核模块。
- 加载 TOA 内核模块的环境需拥有 root 权限。
:::
::: 兼容性限制
 - UDP 监听器不支持通过 TOA 获取源 IP。
 - 若客户端和真实服务端中间的设备有其他已经进行过 TOA 相关操作的设备，则可能存在冲突，无法保证服务端获取真实 IP 的有效性。
 -  插入 TOA 后，只对插入后的新建连接生效，对存量已有连接无效。
 - 由于 TOA 模块需要对 TCP option 中的地址进行提取等额外处理，因此 TOA 模块会引起服务端部分的性能下降。
 - 腾讯云的 TOA 模块无法保证和其他用户自定义的内核模块兼容，也无法保证与其他厂商或开源的 TOA 模块兼容。
 - 腾讯自研的 TencentOS 内嵌的 TOA 模块支持混合云部署场景下获取真实源 IP，因此若服务端的系统为 TencentOS 且为混合云部署时，可尝试直接执行 `modprobe toa` 命令进行加载使用。需要注意的是，TencentOS 与其他发行版 Linux 系统是两套 TOA，不支持混用。
:::
</dx-accordion>

## 控制台开启 TOA[](id:loadopentoa)
1. 已创建 NAT64 版本的 CLB 实例，详情请参见 [创建 IPv6 NAT64 负载均衡实例](https://cloud.tencent.com/document/product/214/30440)。
2. 登录 [负载均衡控制台](https://console.cloud.tencent.com/clb)，创建 TCP 监听器，详情请参见 [配置 TCP 监听器](https://cloud.tencent.com/document/product/214/36386)。
3. 在“创建监听器”对话框中，开启 TOA 开关。
![](https://qcloudimg.tencent-cloud.cn/raw/c92df2a900b94e104d261c5dbb475202.png)




## [加载 TOA 模块](id:load-toa)
1. 根据腾讯云上 Linux 的版本，下载对应的 TOA 包解压。
<dx-accordion>
::: centos
[CentOS 8.0 64](https://clb-toa-1255852779.file.myqcloud.com/CentOS%208.0.1905.zip)
[CentOS 7.6 64](https://clb-toa-1255852779.file.myqcloud.com/CentOS%207.6.1810.zip)
[CentOS 7.2 64](https://clb-toa-1255852779.file.myqcloud.com/CentOS%207.2.1511.zip)

:::
::: debian
[Debian 9.0 64](https://clb-toa-1255852779.file.myqcloud.com/Debian%209.zip)
:::
::: suse linux
[SUSE 12 64](https://clb-toa-1255852779.file.myqcloud.com/SUSE%2012.zip)
[SUSE 11 64](https://clb-toa-1255852779.file.myqcloud.com/SUSE%2011.zip)
:::
::: ubuntu
[Ubuntu 18.04.4 LTS 64](https://clb-toa-1255852779.file.myqcloud.com/Ubuntu%2018.04.4%20LTS.zip)
[Ubuntu 16.04.7 LTS 64](https://clb-toa-1255852779.file.myqcloud.com/Ubuntu%2016.04.7%20LTS.zip)
:::
</dx-accordion>

2. [](id:step2)解压完成后，执行 cd 命令进入到刚解压的文件夹里，执行以下命令加载模块：
```
insmod toa.ko
```
3. 执行以下命令确认 TOA 模块是否加载成功。若提示“toa load success”，则说明已加载成功。
```
dmesg -T | grep TOA
```
4. 加载成功以后，在启动脚本中加载 `toa.ko` 文件（重启机器 ko 文件需要重新加载）。
5. （可选）若不再需要使用 TOA 模块，执行以下命令进行卸载。
```
rmmod toa
```
6. （可选）执行以下命令确认 TOA 模块是否卸载成功。若提示“TOA unloaded”，则说明卸载成功。
```
dmesg -T
```

若上述下载文件中没有您的操作系统版本对应的安装包，则可以下载 Linux 通用版的源码包，编译后获取对应的 ko，该版本支持 Centos8、Centos7、Ubuntu18.04、Ubuntu16.04 等绝大多数具有代表性的 Linux 发行版。
>? 由于 Linux 内核版本众多，且 Linux 发行版操作系统市场庞大，版本繁多，因此考虑到内核模块的兼容性问题，建议在使用的系统上对 TOA 源码包进行编译后使用。
>
1. 下载源码包
>!Linux 与 腾讯 TLinux 的 TOA 模块不能混用，请根据对应系统选择对应的 TOA 模块源码包。
>
  - Linux
```
wget "https://clb-toa-1255852779.file.myqcloud.com/tgw_toa_linux_ver.tar.gz"
```
  - 腾讯 TLinux
```
wget "https://clb-toa-1255852779.file.myqcloud.com/tgw_toa_tlinux_ver.tar.gz"
```
2. 编译 TOA 内核模块的 Linux 环境需先安装 GCC 编译器、Make 工具和内核模块开发包。
<dx-accordion>
::: CentOS 环境下的安装操作

```
yum install gcc
yum install make
//安装内核模块开发包，开发包头文件与库的版本需要与内核版本一致
yum install kernel-devel-`uname -r`
```
:::
::: Ubuntu、Debian 环境下的安装操作

```
apt-get install gcc
apt-get install make
//安装内核模块开发包，开发包头文件与库的版本需要与内核版本一致
apt-get install linux-headers-`uname -r`
```
:::
::: SUSE 环境下的安装操作
```
zypper install gcc
zypper install make
//安装内核模块开发包，开发包头文件与库的版本需要与内核版本一致
zypper install kernel-default-devel
```
:::
</dx-accordion>

3. 编译源码，生成 toa.ko 文件。编译过程中未提示 `warning` 和 `error`，则说明编译成功。以 Linux 系统对应的源码包为例：
```
tar zxvf tgw_toa_linux_ver.tar.gz
cd tgw_toa_linux_ver//进入解压后的tgw_toa目录
make
```
4. 编译 toa.ko 成功后，执行上文 [步骤2](#step2) 中的加载 TOA 模块的操作。


## [适配后端服务](id:adapt-rs)
<dx-accordion>
::: 混合云部署场景
在混合云部署场景下适配后端服务时，无需进行代码改造，只需调用 Linux 网络编程中标准的接口即可获取访问用户的真实源 IP。例如以下的 C 代码样例。
```
struct sockaddr v4addr;  
len = sizeof(struct sockaddr);  
//get_peer_name 为 Linux 网络编程中标准接口。
if (get_peer_name(client_fd, &v4addr, &len) == 0) {  
	inet_ntop(AF_INET, &(((struct sockaddr_in *)&v4addr)->sin_addr), from, sizeof(from));  
	printf("real client v4 [%s]:%d\n", from, ntohs(((struct sockaddr_in *)&v4addr)->sin_port));   
}
```
:::
::: NAT64 CLB 场景
在 NAT64 CLB 场景中，使用 TOA 源地址透传功能，后端服务器在插入 `toa.ko` 内核模块后，还需对应用程序的源码进行改造以适配获取真实源 IP 的功能。
1. 首先定义一个用来保存地址的数据结构。
```
struct toa_nat64_peer {  
	struct in6_addr saddr;  
	uint16_t sport;  
};  
....  
struct toa_nat64_peer client_addr;  
....  
```
2. 其次定义消息并调用函数获取真实的 IPv6 源地址。
```
enum {  
	TOA_BASE_CTL            = 4096,  
	TOA_SO_SET_MAX          = TOA_BASE_CTL,  
	TOA_SO_GET_LOOKUP       = TOA_BASE_CTL,  
	TOA_SO_GET_MAX          = TOA_SO_GET_LOOKUP,  
};  
getsockopt(client_fd, IPPROTO_IP, TOA_SO_GET_LOOKUP, &client_addr, &len);  
```
3. 最后获取地址。
```
real_ipv6_saddr = client_addr.saddr;  
real_ipv6_sport = client_addr.sport;
```

完整示例如下所示：
```
//需要定义一个调用获取真实 IP 的函数的消息，值为4096即可。
enum {  
	TOA_BASE_CTL            = 4096,  
	TOA_SO_SET_MAX          = TOA_BASE_CTL,  
	TOA_SO_GET_LOOKUP       = TOA_BASE_CTL,  
	TOA_SO_GET_MAX          = TOA_SO_GET_LOOKUP,  
};  
//需要定义一个用来保存地址的数据结构。
struct toa_nat64_peer {  
	struct in6_addr saddr;  
	uint16_t sport;  
};  
//声明用来保存地址的变量，类型为自定义用来保存地址的数据结构。  
struct toa_nat64_peer client_addr;  
.……  
//获取客户端的文件描述符，其中 listenfd 为服务端的监听文件描述符。  
client_fd = accept(listenfd, (struct sockaddr*)&caddr, &length);  
//调用函数获取对应 NAT64 场景下的用户真实源 IP。  
char from[40];  
int len = sizeof(struct toa_nat64_peer);  
if (getsockopt(client_fd, IPPROTO_IP, TOA_SO_GET_LOOKUP, &client_addr, &len) == 0) {  
	inet_ntop(AF_INET6, &client_addr.saddr, from, sizeof(from));  
	//获取源IP和源port的信息  
	printf("real client [%s]:%d\n", from, ntohs(client_addr.sport));  
}  
```
:::
::: 混合云部署与 NAT64 CLB 混用场景
在混合云部署与 NAT64 CLB 混用场景中，使用 TOA 源地址透传功能，后端服务器在插入 `toa.ko` 内核模块后，还需对应用程序的源码进行改造以适配获取真实源 IP 的功能。

完整示例如下所示：
```
//需要定义一个调用获取真实 IP 的函数的消息，值为4096即可。  
enum {  
	TOA_BASE_CTL = 4096,  
	TOA_SO_SET_MAX = TOA_BASE_CTL,  
	TOA_SO_GET_LOOKUP = TOA_BASE_CTL,  
	TOA_SO_GET_MAX = TOA_SO_GET_LOOKUP,   
};  

//需要定义一个用来保存地址的数据结构。    
struct toa_nat64_peer {    
	struct in6_addr saddr;    
	uint16_t sport;    
};    

//声明用来保存地址的变量，类型为自定义用来保存地址的数据结构。    
struct toa_nat64_peer client_addr_nat64;    
.......  
//获取客户端的文件描述符，其中 listenfd 为服务端的监听文件描述符。  
//调用函数获取对应 NAT64 场景下真实的用户源 IP。   
char from[40];    
int len = sizeof(struct toa_nat64_peer);  
int ret;  
ret = getsockopt(client_fd, IPPROTO_IP, TOA_SO_GET_LOOKUP, &client_addr_nat64, &len);  
if (ret == 0) {  
	inet_ntop(AF_INET6, &(client_addr_nat64.saddr), from, sizeof(from));    
	//获取源 IP 和源 Port 的信息。   
	printf("real client v6 [%s]:%d\n", from, ntohs(client_addr_nat64.sport));   
} else if (ret != 0) {  
	struct sockaddr v4addr;  
	len = sizeof(struct sockaddr);  
	//获取源 IP 和源 Port 的信息,注意此函数获取的源地址对于:  
	//经过混合云部署场景的 SNAT IP 的链接而言为真正的源地址；  
	//不经过混合云部署场景的 SNAT IP 也不经过 NAT64 的链接而言是客户端地址，同样是真正的源地址。  
	//因此此函数的语义便为获取真正的客户端地址、端口。  
	if (get_peer_name(client_fd, &v4addr, &len) == 0) {  
		inet_ntop(AF_INET, &(((struct sockaddr_in *)&v4addr)->sin_addr), from, sizeof(from));  
		printf("real client v4 [%s]:%d\n", from, ntohs(((struct sockaddr_in *)&v4addr)->sin_port));   
	}  
}  
```
:::
</dx-accordion>


## [（可选）监控 TOA 模块状态](id:monitor-toa)
为保障 TOA 内核模块运行的稳定性，TOA 内核模块还提供了监控功能。在插入 toa.ko 内核模块后，可以在容器所在的宿主机通过以下两种方式监控 TOA 模块的工作状态。
<dx-accordion>
::: 方式一：查看 TOA 保存的连接的 IPv6 地址
执行以下命令查看 TOA 保存的连接的 IPv6 地址。
>!此命令有可能会引起性能下降，请勿频繁调用此命令查看。

```
cat /proc/net/toa_table
```
:::
::: 方式二：查看 TOA 相关的计数状态
执行以下命令查看 TOA 相关的计数状态。
```
cat /proc/net/toa_stats
```
![](https://qcloudimg.tencent-cloud.cn/raw/0dcbd6a263316481f50d99c2e4fbab7a.png)
其中主要的监控指标对应的含义如下所示：
<table>
<thead>
<tr>
<th>指标名称</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>syn_recv_sock_toa</td>
<td>接收带有 TOA 信息的连接个数。</td>
</tr>
<tr>
<td>syn_recv_sock_no_toa</td>
<td>接收并不带有 TOA 信息的连接个数。</td>
</tr>
<tr>
<td>getname_toa_ok</td>
<td>调用 getsockopt 获取源 IP 成功即会增加此计数，另外调用 accept 函数接收客户端请求时也会增加此计数。</td>
</tr>
<tr>
<td>getname_toa_mismatch</td>
<td>调用 getsockopt 获取源 IP 时，当类型不匹配时，此计数增加。例如某条客户端连接内存放的是 IPv4 源 IP，并非为 IPv6 地址时，此计数便会增加。</td>
</tr>
<tr>
<td>getname_toa_empty</td>
<td>对某一个不含有 TOA 的客户端文件描述符调用 getsockopt 函数时，此计数便会增加。</td>
</tr>
<tr>
<td>ip6_address_alloc</td>
<td>当 TOA 内核模块获取 TCP 数据包中保存的源 IP、源 Port 时，会申请空间保存信息。</td>
</tr>
<tr>
<td>ip6_address_free</td>
<td>当连接释放时，toa 内核模块会释放先前用于保存源 IP、源 port 的内存，在所有连接都关闭的情况下，所有 CPU 的此计数相加应等于 ip6_address_alloc 的计数。</td>
</tr>
</tbody>
</table>

:::
</dx-accordion>


## FAQ
<dx-accordion>
::: 为什么在 NAT64 CLB 场景下插入了 TOA 模块后仍需要改造服务端程序？
这是由于 IP 类型发生了变化导致的。在混合云部署场景下，做了 IPv4 的 Fullnat 转换，在此场景下，客户端的真实源 IP 仍然是从 IPv4 的 IP 转换成另外一个 IPv4 的 IP，因此 IP 的类型没有发生变化。但是在 NAT64 CLB 场景下，客户端真实源 IP 是从 IPv6 转换成了 IPv4，IP 类型发生了变化，因此服务端为了理解此 IPv6 的 IP，必须要对服务端程序进行改造才可以理解此 IPv6 地址的含义。
:::
::: 如何确定所用的系统是基于 Linux 的发行版还是腾讯 TLinux 的内核？
- 执行以下命令查看内核版本。若执行结果的版本中包含 `tlinux`，则为 TLinux 系统。反之则为 Linux 发行版。
```
uname -a
```
![](https://qcloudimg.tencent-cloud.cn/raw/3f266a4c245030173564cff0d3c77f73.png)

- 还可以执行以下命令，若执行结果中包含 `tlinux` 或者是 `tl2`，则为 TLinux 系统。
```
rpm -qa | grep kernel
```
<img src="https://qcloudimg.tencent-cloud.cn/raw/4559818bd61436d7a752bcd9caf1b53d.png" width="70%">
:::
::: 无法获取源地址，如何进行初步的排查？
1. 执行以下命令确认 TOA 模块是否已经加载。
```
lsmod | grep toa
```
<img src="https://qcloudimg.tencent-cloud.cn/raw/5b92aa9de0db3e43e91316c4363886f1.png" width="70%">
2. 确认服务端程序是否已经正确调用接口获取源地址，请参见以上 [适配后端服务](#adapt-rs) 内容。
3. 在服务端抓包排查，确认是否已经有携带真实源地址的 TCP 包抵达。
 - 若 tcp option 中存在 `unknown-200` 的提示，则说明经过 SNAT 后，真实的源 IP 已经插入到 TCP option 中。
 - 若存在 `unknown-253`，则说明在 NAT64 场景下的真实 IPv6 的源 IP 已经插入。
![](https://qcloudimg.tencent-cloud.cn/raw/e8fed1ab42370a97889c7dcdce660b72.png)
4. 在上一步的操作中，若确定携带 TOA 地址的包进入了服务端，则将 toa.ko 编译出 DEBUG 版本，通过内核日志便可进一步定位。在下载出的 TOA 源码目录中，将 Makefile 中添加 DEBUG 编译选项。
<img src="https://qcloudimg.tencent-cloud.cn/raw/e89cf9fd3d96a760485fb04c966ef6b0.png"width="60%">
5. 执行以下命令重新编译。
```
make clean
make
```
6. 执行以下命令卸载原有 ko，并重新插入编译出的最新 ko。
```
rmmod toa 
insmod ./toa.ko
```
7. 执行以下命令观察内核日志。
```
dmesg -Tw
```
若提示以下内容，则说明 TOA 模块正常工作，请进一步排查服务端程序是否有调用接口获取真实源 IP，或是是否接口使用错误。
![](https://qcloudimg.tencent-cloud.cn/raw/9a958fc2b0ae9d185cd228c6668c7162.png)
8. 若以上步骤皆没有排查出具体原因，请 [联系我们](https://cloud.tencent.com/online-service?from=console_bar_clb|instance)。
:::
</dx-accordion>
