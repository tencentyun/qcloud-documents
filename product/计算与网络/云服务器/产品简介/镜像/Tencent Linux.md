
Tencent Linux（简称 Tlinux）是腾讯针对云的场景研发的 Linux 操作系统，提供了专门的功能特性和性能优化，为云服务器实例中的应用程序提供高性能，且更加安全可靠的运行环境。Tencent Linux 使用免费，在 CentOS（及发行版）上开发的应用程序可直接在 Tencent Linux 上运行，用户还可持续获得腾讯云的更新维护和技术支持。

## 适用说明
Tencent Linux 适用于下列场景：
- 绝大部分云服务器各规格族实例，包括黑石2.0服务器。
- 启动实例时，需要通过用户数据（即 userdata 的方式）将相关操作传递到 cloud-init，以达到在实例启动时进行动态配置的目的。

## 主要特性
### 内核定制
基于内核社区长期支持的4.14.105版本定制而成，增加适用于云场景的新特性、改进内核性能并修复重大缺陷

### 容器支持
针对容器场景进行优化，提供了隔离增强和性能优化特性：
- meminfo、vmstat、cpuinfo、stat、loadavg 等隔离
- Sysctl 隔离，如 tcp_no_delay_ack、tcp_max_orphans
- 大量文件系统和网络的 BUGFIX

### 性能优化
计算、存储和网络子系统均经过优化，包括：
- 优化 xfs 内存分配，解决 xfs kmem_alloc 分配失败告警
- 优化网络收包大内存分配问题，解决 UDP 包量大时，占据过多内存问题
-	限制系统 page cache 占用内存比例，从而避免内存不足影响业务的性能或者 OOM

### 软件包
-	基于 CentOS 7 版本的软件包定制而成
-	用户态软件包与 CentOS 7 版本兼容，该版本用户态软件包可直接在 Tencent Linux 环境使用
-	使用 YUM 更新和安装软件包
-	通过 YUM 安装 epel-release 包后，可以使用 epel 源中的软件包

### 缺陷支持
- 提供操作系统崩溃后的 kdump 内核转储能力
-	提供内核的热补丁升级能力

### 安全更新
Tencent Linux 会定期进行更新，增强安全性及功能。

### 发布说明


| 发布时间 | 镜像版本 | 版本说明 |
|---------|---------|---------|
| 2019年9月17日 | Tencent Linux release 2.4 (Final) | 镜像 ID：img-hdt9xxkt<br>内核版本：4.14.105<br>发布地域：所有地域 |


## 获取 Tlinux
腾讯云在 [云服务器控制台](https://console.cloud.tencent.com/cvm) 提供了 Tencent Linux 公共镜像，您可通过下列方法获取并使用 Tencent Linux。
- 创建云服务器实例时，选择公共镜像，并选择 Tencent Linux 的相应版本。
操作详情请参见 [创建实例](https://cloud.tencent.com/document/product/213/4855)。
- 已创建的云服务器实例，可通过重装系统将现有操作系统更换为 Tencent Linux。
操作详情请参见 [重装系统](https://cloud.tencent.com/document/product/213/4933)。

## 技术支持
腾讯云为 Tencent Linux 提供如下技术支持：
在 YUM 源提供安全更新（Security Updates），运行 `yum update` 命令即可更新至新版本。
