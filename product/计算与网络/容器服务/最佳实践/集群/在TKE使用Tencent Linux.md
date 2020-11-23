# 在TKE使用Tencent Linux

容器的底层实现深度依赖于内核的众多特性，如 overlay 文件系统，namespace, cgroup 等，因此内核的功能和稳定性，在很大程度上，决定了整个容器PaaS平台的功能和稳定性。

Tencent Linux 是腾讯内部运营多年的Linux版本，下面会做详细介绍。 推荐TKE用户使用Tencent Linux作为节点OS镜像。

#### Tencent Linux是谁维护的？ 基于什么发行版的？

答：是腾讯内核和虚拟化团队负责维护的。Tencent Linux 2.4 基于CentOS 7, 用户态软件包保持与最新版 CentOS 7 兼容，CentOS 7 版本的软件包可以直接在 Tencent Linux 2.4 中使用

#### Tencent Linux跟CentOS有什么区别？

答：关键的区别在内核版本，本文后面会详细介绍。 用户态有少量调整，如 YUM 源的配置等，详情请参考官方介绍文档：https://cloud.tencent.com/document/product/213/38027

#### 内核是什么版本？

答：Tencent Linux 2.4 目前是4.14内核。代码和 rpm 包在 GitHub 可以获取： https://github.com/Tencent/TencentOS-kernel。 年底会推出5.4版本

#### Tencent Linux跟TKE的Optimized镜像是什么关系？

它们的内核是一样的，但Tencent Linux 2.4 是CVM公共镜像， TKE Optimized镜像是市场镜像。

TKE将使用`Tencent Linux2.4`来替代`CentOS 7.6 TKE Optimized`以及`Ubuntu18.04 TKE Optimized`。已经在使用`CentOS 7.6 TKE Optimized`和`Ubuntu18.04 TKE Optimized`的集群还可以继续使用，但以后新建集群将不再支持这两种OS镜像。

11月下旬TKE用户可以自行在控制台操作，将集群新创建的节点的OS镜像切换为`Tencent Linux2.4`，操作入口如下图(把操作系统修改为`Tencent Linux2.4`)：
!['image.png'](https://main.qcloudimg.com/raw/776bd979d6e48701ad1a591a45f8a83c.png)

#### 相比 CentOS 和 Ubuntu 等发行版有什么优势？

A: 主要优势如下， 后文会详细介绍：

1. 经过腾讯大量内部业务多年的验证和打磨。
2. 顶级内核专家团队的支持。
3. 包含一些关键的性能优化和针对容器场景的定制特性。

## 腾讯内部业务多年的验证和打磨

Tencent Linux 从 2010 年启动研发，在腾讯内部已经上线运营了 10 年，总部署量已经是百万级，在腾讯内部 Linux 系统里占比 99%，覆盖了腾讯所有的业务，同时腾讯有着国内最种类繁多的业务生态，从社交，游戏，到金融支付，AI, 安全等, 所以对底层操作系统的稳定性，性能，兼容性等都有更强的要求。

对于容器场景来讲，腾讯大量核心业务几乎已经部分或全部容器化，例如微信所有的逻辑业务全部容器化， 针对微信业务特点，进行系列优化，顺利保障了每年春节的红包高峰运营，同时在数据安全方面，也跟微信紧密合作，提供解决方案。

## 内核专家团队的支持

目前有三十多位全职内核专家为这个内核版本提供支持。其中有 kvm 维护者，还有很多内核网络，存储，cgroup，调度等各个子系统的专家。

支持力度也体现在版本更新节奏和热补丁服务。

从版本记录(https://github.com/Tencent/TencentOS-kernel/releases) 可以看到，从 7 月到 10 月， Tencent Linux 4.14 内核系列发布了 5 个版本。腾讯内部业务和腾讯云外部客户碰到的绝大多数问题，都能及时得到定位和修复。

另外我们针对一些重要的修复，会提供内核热补丁的在线修复方式。热补丁的安装和生效，不需要重启机器，在不中断客户业务的情况下，提升客户业务的时延 SLA。

对于漏洞修复，Tencent Linux 有着全套的热补丁方案，包括：应用程序级热补丁，内核级热补丁等。每年发布 100 多个热补丁。 大多数漏洞在一周内提供修复方案。

 

## 性能优化

Tecent Linux 在根据内部与外部的用户在大规模落地实践中遇到的问题，针对容器场景也做了大量性能优化，包括但不限于:

1. 解决 IPVS 模式高并发场景下，连接复用引发连接异常的问题 ([#81775](https://github.com/kubernetes/kubernetes/issues/81775))。
2. 解决 IPVS 模式在高配节点 (核数多) 下 IPVS 规则过多引发网络毛刺的问题。
3. 解决在容器密集场景下(单节点上容器数量较多)，cAdvisor 读取 memcg 陷入内核态过久引发网络毛刺的问题。
4. 解决大 Pod (占用核数多，单核占用高) 在高配节点 (核数多) 场景下，CPU 负载均衡引发网络毛刺的问题。
5. 解决高并发场景下的 TCP 连接监控(比如单独部署 cAdvisor 配置监控 TCP 连接) 引发网络周期性抖动问题。
6. 优化网络收包软中断，提升网络性能。

这些针对各种容器场景的优化效果非常显著，以第 3 点为例，ping 时延监控效果图如下 (11:00 之后是优化后):
!['image.png'](https://main.qcloudimg.com/raw/ac2cd0103df4c893070ea4f0169e4ab1.png)

 

## 容器定制特性

#### 容器资源展示隔离

很多 golang, java 程序的高效运行依赖于正确获取进程可用的 CPU 和内存资源。但这类程序在容器中获取到的是节点的 CPU 和内存资源， 与实际容器所分配的资源并不匹配，往往会造成进程的线程池等参数不合理，从而带来问题。

社区主流的解决方案是通过部署 FUSE 实现的 LXCFS 来实现/proc/cpuinfo, /proc/meminfo等资源展示按容器隔离。这个方案需要在节点部署 LXCFS 文件系统， 也需要往 POD sepc 中插入相关 volume 和挂载点的配置。详情可以参考：[Kubernetes Demystified: Using LXCFS to Improve Container Resource Visibility](https://dzone.com/articles/kubernetes-demystified-using-lxcfs-to-improve-cont)

Tencnet Linux内核中实现了类似 LXCFS 特性，用户无需在节点部署 LXCFS 文件系统， 也无需修改 POD spec。只需在节点开启一个全局开关（`sysctl -w kernel.stats_isolated=1`）， 容器中读取 /proc/cpuinfo, /proc/meminfo 等文件获取的就是按容器隔离的，就是这么简单。

另外，考虑到有些特殊容器， 比如节点监控组件， 可能就是需要读取节点级的信息。为了解决这个问题，专门增加了容器级的开关`kernel.container_stats_isolated`。在主机级开关开启的情况下，只需要在容器的启动脚本里面，关闭容器级的开关(`sysctl -w kernel.container_stats_isolated=0`)，以后在这个容器里面读取 /proc/cpuinfo, /proc/meminfo 等文件获取的就是主机的信息了。(注： 容器级开关必须在容器中设置，才能对本容器生效)

请参考详细使用文档：[容器内CPU、内存、进程、磁盘等信息隔离](https://github.com/Tencent/TencentOS-kernel/wiki/container-resource-view-isolation)

#### 更多内核参数的隔离

- net.ipv4.tcp_max_orphans
- net.ipv4.tcp_workaround_signed_windows
- net.ipv4.tcp_rmem
- net.ipv4.tcp_wmem
- vm.max_map_count

这些内核参数都是业务经常需要定制修改的。但是社区内核里面并没有对这些参数做 namespace 化隔离。一个容器对以上参数的修改，会对主机以及所有其他容器都起作用。 Tencent Linux根据内外部客户的需求，实现了这些内核参数的 namespace 化隔离，业务容器可以放心的对这些参数进行个性化设置而不用担心对其他业务的干扰了。

#### 容器缺省内核参数优化

在高并发的情况下，可能会发生半连接队列满而丢包， 可以通过调大 `net.core.somaxconn` 来缓解问题。但是容器网络 namespace 里面的 `net.core.somaxconn` 缺省值只有 128，而且是代码写死的。 在 Tencent Linux 内核中，我们把这个缺省值调整到 4096， 从而可以减少高并发情况下半连接队列满的丢包问题。

 

## 在 TKE 如何使用 Tencent Linux

如果希望 TKE 集群的节点使用 Tencent Linux 的操作系统，需要在创建 TKE 集群时，操作系统选择 `Tencent Linux` :

!['image.png'](https://main.qcloudimg.com/raw/db64d889459d9defba710151b0a9d973.png)

> **注:** Tencent Linux 除了支持普通的云服务器机型外，还支持黑石物理机与 Nvidia GPU 的机型。

## 参考资料

- [Tencent Linux 官方介绍文档](https://cloud.tencent.com/document/product/213/38027)
- [Tencent Linux 内核代码](https://github.com/Tencent/TencentOS-kernel)
- [容器资源展示隔离使用文档](https://github.com/Tencent/TencentOS-kernel/wiki/container-resource-view-isolation)
