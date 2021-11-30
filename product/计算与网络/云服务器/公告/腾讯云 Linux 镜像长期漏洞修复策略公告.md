腾讯云安全中心会及时关注各种安全漏洞状况。在官方发布重要安全漏洞后，腾讯云安全中心会及时跟进漏洞情况，向用户发布漏洞信息，提供漏洞修复方案。

## 腾讯云官方镜像修复周期
- 定期漏洞修复：腾讯云官方镜像将定期进行常规漏洞修复，修复频率为每年`2`次；
- 高危漏洞修复：对于高危漏洞，腾讯云将紧急修复并第一时间提供给客户

## 漏洞修复包含的镜像范围
腾讯云对于镜像的安全维护原则与上游镜像官方发行版保持一致，将针对官方维护周期内的系统版本进行安全维护。

### CentOS
CentOS 官方只针对当前所发行主要版本的最新次要版本维护软件与漏洞的更新，腾讯云与 CentOS 官方维护原则保持一致，只针对官方维护周期内各主要版本的最新次要版本进行定期漏洞修复和高危漏洞紧急修复。

腾讯云现有 CentOS 版本镜像维护说明：
- CentOS 7.6 64位（CentOS 官方维持支持）
- CentOS 7.5 64位（CentOS 官方维持支持）
- CentOS 7.4 64位（CentOS 官方维持支持）
- CentOS 7.3 64位（CentOS 官方维持支持）
- CentOS 7.2 64位（CentOS 官方维持支持）
- CentOS 7.1 64位（CentOS 官方停止支持）
- CentOS 7.0 64位（CentOS 官方停止支持）
- CentOS 6.9 32/64位（CentOS 官方维持支持到下一个版本发布）
- CentOS 6.8 32/64位（CentOS 官方停止支持）
- CentOS 6.7 32/64位（CentOS 官方停止支持）
- CentOS 6.6 32/64位（CentOS 官方停止支持）
- CentOS 6.5 32/64位（CentOS 官方停止支持）
- CentOS 6.4 32/64位（CentOS 官方停止支持）
- CentOS 6.3 32/64位（CentOS 官方停止支持）
- CentOS 6.2 64位（CentOS 官方停止支持）
- CentOS 5.11 32/64位（CentOS 官方停止支持）
- CentOS 5.8 32/64位（CentOS 官方停止支持）

### Ubuntu
Ubuntu 官方提供对 LTS 版本系统的长期软件与漏洞更新维护，每个 LTS 系统的服务器版本将维持 5 年的更新，腾讯云官方提供各个 LTS 版本服务器系统，并与 Ubuntu 发行官方保持一致，对维护周期内的镜像进行定期漏洞更新和高危漏洞紧急修复。

腾讯云现有 Ubuntu 版本镜像维护说明：
- Ubuntu 18.04 LTS 64位（Ubuntu 官方支持维护）
- Ubuntu 16.04 LTS 64位（Ubuntu 官方支持维护）
- Ubuntu 14.04 LTS 32/64位（Ubuntu 官方支持维护）
- Ubuntu 12.04 LTS 64位（Ubuntu 官方停止维护）
- Ubuntu 10.04 LTS 32/64位（Ubuntu 官方停止维护）




### Debian
Debian 官方维护两个主要分支系统：stable 和 oldstable，其中 stable 是当前稳定的版本，oldstable 是上一个稳定的版本。Debian 官方会针对 stable 系统维持软件与漏洞的更新，针对 oldstable 将由自愿者和社区提供 LTS（Long Term Support）的维护方案。腾讯云与上游官方维护策略保持一致，只针对由 Debian 官方维护的 stable 分支系统进行定期漏洞修复。

腾讯云现有 Debian 版本镜像维护说明：
- Debian 9.0  64位（Debian 官方支持维护 ）
- Debian 8.2 32/64位（预计2019年6月停止维护 ）
- Debian 7.8 32/64位（Debian 官方已停止维护）
- Debian 7.4 64位（Debian 官方已停止维护）


### openSUSE
根据 openSUSE 系统生命周期，腾讯云对受官方支持的系统进行定期镜像漏洞修复。

腾讯云现有 openSUSE 版本镜像维护说明：
- openSUSE 42.3（openSUSE 官方支持维护）
- openSUSE 13.2（openSUSE 官方已停止维护）
- openSUSE 12.3 32/64位（openSUSE 官方已停止维护）

### FreeBSD
自 FreeBSD 11.0-RELEASE 之后，FreeBSD 为 stable 分支提供 5 年的维护周期，在 11.0-RELEASE 之前的版本根据不同类型，提供不同周期的支持。腾讯云与 FreeBSD 官方维护原则保持一致。

腾讯云现有 FreeBSD 版本镜像维护说明：
- FreeBSD 11.1 64位（ FreeBSD 官方支持维护）
- FreeBSD 10.1 64位（ FreeBSD 官方已停止维护）

### 商业版系统
腾讯云不提供对商业版本系统的漏洞更新与维护。
