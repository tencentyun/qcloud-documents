## 内核定制
基于内核社区长期支持的版本定制而成，增加适用于云场景的新特性、改进内核性能并修复重大缺陷。

## 容器场景性能优化
针对容器场景进行优化，提供了隔离增强和性能优化特性：
- meminfo、vmstat、cpuinfo、stat、loadavg 等隔离。
- Sysctl 隔离，如 tcp_no_delay_ack、tcp_max_orphans。
- 大量文件系统和网络的 BUGFIX。
- 解决 IPVS 模式高并发场景下，连接复用引发连接异常的问题。
- 解决 IPVS 模式在高配节点（核数多）时，IPVS 规则过多引发网络毛刺的问题。
- 解决在容器密集场景下（单节点上容器数量较多），cAdvisor 读取 memcg 陷入内核态过久引发网络毛刺的问题。
- 解决大 Pod（占用核数多，单核占用高）在高配节点（核数多）场景下，CPU 负载均衡引发网络毛刺的问题。
- 解决高并发场景下的 TCP 连接监控（例如，单独部署 cAdvisor 配置监控 TCP 连接）引发网络周期性抖动问题。
- 优化网络收包软中断，提升网络性能。

## 容器定制特性
### 容器资源展示隔离
- 增加主机级开关：内核已实现了类似 LXCFS 特性。用户无需在节点部署 LXCFS 文件系统及修改 POD spec，仅需在节点开启全局开关（`sysctl -w kernel.stats_isolated=1`），`/proc/cpuinfo` 及 `/proc/meminfo` 等文件获取即可按容器隔离。
<dx-alert infotype="notice" title="">
仅 TencentOS Server 2.4 版本支持 `kernel.stats_isolated` 参数，TencentOS Server 2.4（TK4）及 3.1 后续更新版本不支持。
</dx-alert>
- 增加容器级开关：针对类似节点监控组件等特殊容器，增加了容器级开关 `kernel.container_stats_isolated`。在主机级开关开启时，仅需在容器启动脚本中关闭容器级开关（`sysctl -w kernel.container_stats_isolated=0`），即可在容器中读取 `/proc/cpuinfo` 及 `/proc/meminfo` 文件时获取到主机信息。

### 内核参数隔离
实现以下内核参数的 namespace 化隔离：
- `net.ipv4.tcp_max_orphans`
- `net.ipv4.tcp_workaround_signed_windows`
- `net.ipv4.tcp_rmem`
- `net.ipv4.tcp_wmem`
- `vm.max_map_count`

### 容器缺省内核参数优化
将容器网络 namespace 中的 `net.core.somaxconn` 缺省值调至4096，减少高并发情况下半连接队列满的丢包问题。

## 性能优化
计算、存储和网络子系统均经过优化，包括：
- 优化 xfs 内存分配，解决 xfs kmem_alloc 分配失败告警。
- 优化网络收包大内存分配问题，解决 UDP 包量大时，占据过多内存问题。
- 限制系统 page cache 占用内存比例，从而避免内存不足影响业务的性能或者 OOM。

## 软件包支持
- TencentOS Server 2用户态软件包保持与最新版 CentOS 7兼容，即 CentOS 7版本的软件包可以直接在 TencentOS Server 2.4 中使用。
- TencentOS Server 3用户态软件包保持与最新版 RHEL 8兼容，即 RHEL 8版本的软件包可以直接在 TencentOS Server 3.1 中使用。
- 支持使用 YUM 更新和安装软件包。
- 通过 YUM 安装 epel-release 包后，可以使用 epel 源中的软件包。

## 缺陷支持
- 提供操作系统崩溃后的 kdump 内核转储能力。
- 提供内核的热补丁升级能力。

## 安全更新
TencentOS Server 会定期进行更新，增强安全性及功能。
