

容器的底层实现深度依赖于内核的众多特性。例如，overlay 文件系统、namespace 及 cgroup 等。因此内核的功能和稳定性，在很大程度上决定了整个容器 PaaS 平台的功能和稳定性。Tencent Linux 是腾讯官方运营的 Linux 版本，您可通过本文了解 Tencent Linux 并开始使用。


##  Tencent Linux 概述
Tencent Linux 由腾讯内核和虚拟化团队负责维护。Tencent Linux 2.4 基于 CentOS 7 版本，用户态软件包保持与最新版 CentOS 7 兼容，CentOS 7 版本软件包可以直接在 Tencent Linux 2.4 中使用。

## Tencent Linux 内核版本
Tencent Linux 2.4目前是4.14内核，可获取 [代码和 rpm 包](https://github.com/Tencent/TencentOS-kernel)。

## Tencent Linux 与 CentOS 的区别
关键区别在于内核版本的不同。例如用户态的少量调整、YUM 源的配置等，详情可参见 [Tencent Linux](https://cloud.tencent.com/document/product/213/38027)。

## Tencent Linux 与 TKE Optimized 镜像的关系
Tencent Linux 和 TKE Optimized 镜像的内核相同，但 Tencent Linux 2.4是腾讯云服务器 CVM 公共镜像，TKE Optimized 镜像是市场镜像。

容器服务 TKE 将使用 `Tencent Linux2.4` 来替代 `CentOS 7.6 TKE Optimized` 以及 `Ubuntu18.04 TKE Optimized`。目前使用 `CentOS 7.6 TKE Optimized` 和 `Ubuntu18.04 TKE Optimized` 的集群仍可以继续使用，但新建集群将不再支持以上两种 OS 镜像。用户可参考 [修改操作系统](#revise) 步骤，将集群新创建的节点的 OS 镜像切换为 `Tencent Linux2.4`。

## Tencent Linux 优势
Tencent Linux 相比 CentOS 和 Ubuntu 等发行版的主要优势在于：
- 经过腾讯大量内部业务多年的验证和打磨。
- 顶级内核专家团队的支持。
- 包含一些关键的性能优化和针对容器场景的定制特性。

### 内部业务验证与打磨

Tencent Linux 从2010年启动研发，在腾讯内部已经上线运营了10年，总部署量已达到百万级，在腾讯内部 Linux 系统里占比99%，覆盖了腾讯所有的业务。腾讯有着国内最种类繁多的业务生态，例如社交、游戏、金融支付、AI、安全等，因此对底层操作系统的稳定性、性能、兼容性等都有严格的要求。
在容器场景中，腾讯大量核心业务已经部分或全部容器化，例如微信的逻辑业务全部容器化，已针对微信业务特点，进行系列优化，顺利保障了每年春节的红包高峰运营，同时在数据安全方面也跟微信紧密合作，提供解决方案。

### 内核专家团队支持

目前有三十多位全职内核专家为此内核版本提供支持。其中有 kvm 维护者，还有很多内核网络、存储、cgroup、调度等各个子系统的专家。
支持力度也体现在版本更新节奏和热补丁服务。从7月到10月，Tencent Linux 4.14内核系列发布了5个版本，详情可参见 [版本记录](https://github.com/Tencent/TencentOS-kernel/releases)。腾讯内部业务和腾讯云外部客户遇到的绝大多数问题，都能及时得到定位和修复。针对一些重要的修复，Tencent Linux 提供内核热补丁的在线修复方式。用户无需重启机器即可完成热补丁的安装和生效，在不中断用户业务的情况下，提升用户业务的时延 SLA。针对漏洞修复，Tencent Linux 有着全套的热补丁方案，其中包括了应用程序级热补丁、内核级热补丁等。Tencent Linux 每年发布100多个热补丁，对于大多数漏洞可以在一周内提供修复方案。

### 性能优化

Tecent Linux 根据内部与外部的用户在大规模落地实践中遇到的问题，针对容器场景做了大量性能优化，包括但不限于：
1. 解决 IPVS 模式高并发场景下，连接复用引发连接异常的问题（[#81775](https://github.com/kubernetes/kubernetes/issues/81775)）。
2. 解决 IPVS 模式在高配节点（核数多）下 IPVS 规则过多引发网络毛刺的问题。
3. [](id:three)解决在容器密集场景下（单节点上容器数量较多），cAdvisor 读取 memcg 陷入内核态过久引发网络毛刺的问题。
4. 解决大 Pod（占用核数多，单核占用高）在高配节点（核数多）场景下，CPU 负载均衡引发网络毛刺的问题。
5. 解决高并发场景下的 TCP 连接监控（例如单独部署 cAdvisor 配置监控 TCP 连接）引发网络周期性抖动问题。
6. 优化网络收包软中断，提升网络性能。

以上针对各种容器场景的优化效果非常显著，以 [第3点](#three) 为例，ping 时延监控效果图如下所示（11:00之后是优化后）：
!['image.png'](https://main.qcloudimg.com/raw/ac2cd0103df4c893070ea4f0169e4ab1.png)

 
### 容器定制特性
#### 容器资源展示隔离
很多 golang、java 程序的高效运行依赖于正确获取进程可用的 CPU 和内存资源。但这类程序在容器中获取到的是节点的 CPU 和内存资源，与实际容器所分配的资源并不匹配，往往会造成进程的线程池等参数不合理，从而带来问题。
社区主流的解决方案是通过部署 FUSE 实现的 LXCFS 来实现 `/proc/cpuinfo`，`/proc/meminfo` 等资源展示按容器隔离。此方案需要在节点部署 LXCFS 文件系统，也需要在 POD sepc 中插入相关 volume 和挂载点的配置。详情可参见 [Kubernetes Demystified: Using LXCFS to Improve Container Resource Visibility](https://dzone.com/articles/kubernetes-demystified-using-lxcfs-to-improve-cont)。
Tencnet Linux 内核中实现了类似 LXCFS 特性，用户无需在节点部署 LXCFS 文件系统，也无需修改 POD spec。只需执行以下命令，在节点开启一个全局开关，然后在容器中读取 `/proc/cpuinfo`，`/proc/meminfo` 等文件后获取的信息即已经过容器隔离。
```
sysctl -w kernel.stats_isolated=1
```
另外，考虑到有些特殊容器，例如节点监控组件，可能需要读取节点级的信息。为了解决这个问题，专门增加了容器级的开关`kernel.container_stats_isolated`。在主机级开关开启的情况下，只需要在容器的启动脚本里面，执行以下命令，关闭容器级的开关，在此容器中读取 `/proc/cpuinfo`，`/proc/meminfo` 等文件后获取的就是主机的信息了。
```
sysctl -w kernel.container_stats_isolated=0
```
>! 容器级开关必须在容器中设置，才能对本容器生效。使用详情可参见 [容器内 CPU、内存、进程、磁盘等信息隔离](https://github.com/Tencent/TencentOS-kernel/wiki/container-resource-view-isolation)。

#### 更多内核参数隔离
- net.ipv4.tcp_max_orphans
- net.ipv4.tcp_workaround_signed_windows
- net.ipv4.tcp_rmem
- net.ipv4.tcp_wmem
- vm.max_map_count

业务经常需要定制修改以上内核参数，但是社区内核里面并没有对这些参数做 namespace 化隔离。一个容器对以上参数的修改，会对主机以及所有其他容器都起作用。Tencent Linux 根据内外部客户的需求，实现了这些内核参数的 namespace 化隔离，业务容器可以放心的对这些参数进行个性化设置而不用担心对其他业务的干扰了。

#### 容器缺省内核参数优化
在高并发的情况下，可能会发生半连接队列满而丢包，可以通过调大 `net.core.somaxconn` 来缓解问题。但是容器网络 namespace 中的 `net.core.somaxconn` 缺省值只有128，而且是代码写死的。在 Tencent Linux 内核中，已将此缺省值调整到4096，从而可以减少高并发情况下半连接队列满的丢包问题。

 ## 操作步骤
如需在 TKE 集群的节点中使用 Tencent Linux 的操作系统，则需在 [创建集群](https://cloud.tencent.com/document/product/457/32189) 时，在设置集群的基本信息页面选择操作系统 `Tencent Linux`。如下图所示：
![](https://main.qcloudimg.com/raw/9376e923fb4e30de1e05f89708fa46c6.png)

>! Tencent Linux 除了支持普通的云服务器机型外，还支持黑石物理机与 Nvidia GPU 的机型。

## 相关操作
### 修改操作系统[](id:revise)
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2) ，单击左侧导航栏中的**集群**。
2. 单击需修改操作系统的集群 ID，进入集群的“基本信息”页面。
3. 在集群“基本信息”页面的节点和网络信息模块，单击默认操作系统右侧的![](https://main.qcloudimg.com/raw/3b38ca6981068a10b031df5708bc4f41.png)。如下图所示：
![](https://main.qcloudimg.com/raw/3a20aa7a26bc0049451edcf5389ed720.png)
4. 在弹出窗口中选择 “Tencent Linux 2.4 64bit” 并单击**提交**，完成操作系统的修改。如下图所示：
![](https://main.qcloudimg.com/raw/17c6da91e1c29af2dd4186c0ea0ff81f.png)



## 相关文档

- [Tencent Linux 官方介绍文档](https://cloud.tencent.com/document/product/213/38027)
- [Tencent Linux 内核代码](https://github.com/Tencent/TencentOS-kernel)
- [容器资源展示隔离使用文档](https://github.com/Tencent/TencentOS-kernel/wiki/container-resource-view-isolation)
