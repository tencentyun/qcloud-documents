### 什么是 TencentOS Server ？
TencentOS Server（又名 Tencent Linux，简称 TS 或 tlinux）是腾讯针对云场景研发的 Linux 操作系统，提供特定的功能及性能优化，为云服务器实例中的应用程序提供高性能及更加安全可靠的运行环境。
TencentOS Server 包含腾讯 OS 团队研发的 TencentOS 内核，基于云环境深度定制，将最新的 Linux 创新推向市场，为企业各类软件提供了超强性能、高可伸缩性和可靠性。TencentOS Server 提供免费使用，用户可持续获得腾讯 OS 团队的更新维护和技术支持。

### TencentOS Server 有哪些特点 ？
TencentOS Server 产品特点如下：
- 深度定制，开箱即用，无需复杂配置。
- 安全合规，支持热补丁，零停机修复。
- 长期支持，拥有强大的运营支撑团队，且全面开源。
- 专为云场景设计，全面优化的高性能 OS。

### 相比其他 Linux 操作系统，TencentOS Server 有哪些优势？
TencentOS Server 相比 CentOS 和 Ubuntu 等发行版的主要优势如下：
- 经过腾讯大量内部业务十多年的验证和打磨。
- 权威内核专家团队的支持。
- 开箱即用，具备关键的性能优化和针对云与容器场景的定制特性。
- 强大的运营支持团队，只需支付少量费用，即可获得强力的商业支持。

### TencentOS Server 包含哪些版本 ？
目前包含以下两个版本：
- TencentOS Server 2 (TS2)：基于 CentOS 7 最新用户态包。
- TencentOS Server 3 (TS3)：基于 RHEL 8 最新用户态包。

TencentOS Server 用户态软件包保持与 RHEL 100%二进制兼容。

### TencentOS Server 的内核包含哪些版本 ？
TencentOS Server 的内核（简称 TK）包含以下两个版本：
- TK3：基于社区4.14 longterm 内核版本。
- TK4：基于社区5.4 longterm 内核版本。
 
TK 的代码可前往 GitHub 获取，详情请参见 [TencentOS-kernel](https://github.com/Tencent/TencentOS-kernel)。

### TencentOS Server 的生命周期有多久 ？
各版本 TencentOS Server 生命周期如下所示，在生命周期未结束前会持续提供 bugfix 和安全补丁更新。
- TencentOS Server 2发行版：维护至2024年12月31日。
- TencentOS Server 3发行版：维护至2029年12月31日。

### 如何在腾讯云上使用 TencentOS Server ？
腾讯云提供了 TencentOS Server 两个版本的公共镜像，您可在创建 Linux 操作系统的云服务器时，选择使用 TencentOS Server 镜像版本。

### TencentOS Server 支持哪些云服务器实例类型？
TencentOS Server 支持大部分云服务器实例类型，您可在 [云服务器购买页面](https://buy.cloud.tencent.com/cvm?regionId=1&projectId=-1) 选择镜像开始使用。

### 在云服务器中使用 TencentOS Server 是否收费？
否。TencentOS Server 本身不收取任何费用，您只需支付云服务器运行费用。

### 使用 TencentOS Server 后，如何安装和升级软件？
TencentOS Server 发行版可以通过 `yum` 命令管理软件包，也可以通过 TencentOS Server 自带的 `t` 命令来管理软件包。其中，TencentOS Server 3 还可以通过 `dnf` 命令管理软件包。

### 是否可以在本地安装使用 TencentOS Server ？
是。TencentOS Server 发行版 ISO 可前往腾讯云软件源进行下载（[点此下载](http://mirrors.tencent.com/tlinux/2.4/iso/) TencentOS Server 2，[点此下载](http://mirrors.tencent.com/tlinux/3.1/iso/x86_64/) TencentOS Server 3）。
您可以在本地服务器或 virtualbox 等虚拟机中安装使用。

### 是否可以查看 TencentOS Server 的源代码 ？
TencentOS Server 全面开源。您可前往 [腾讯云软件源](http://mirrors.tencent.com/) 获取源码包，也可以在系统中使用 `yum downloader --source glibc` 命令获取。

### TencentOS Server 是否支持32位应用程序和库？
暂不支持。TencentOS Server 2 仅支持通过 yum 安装部分32位软件包。

### TencentOS Server 如何保证系统的安全？
TencentOS Server 版本与 RHEL7 和 RHEL8 二进制兼容，遵从 RHEL 的安全规范。腾讯云从以下方面保证 TencentOS Server 系统的安全性：
- 使用腾讯自研的漏洞扫描工具和业内标准的漏洞扫描与安全检测工具，定期进行安全扫描。
- 与腾讯安全团队合作，支持对 TencentOS Server 的安全扫描和安全加固。
- 定期评估 RHEL 和社区的 CVE 补丁，定期更新用户态软件包，修补安全漏洞。
- 通过腾讯云的主机安全功能，定期对系统进行安全体检，并发布用户安全警告和修复方案。



