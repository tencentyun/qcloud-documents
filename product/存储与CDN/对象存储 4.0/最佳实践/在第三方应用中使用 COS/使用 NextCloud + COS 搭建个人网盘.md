## 前言

NextCloud 是一款用于创建网络硬盘的开源客户端和服务器软件。每个人都可以借助该软件自行搭建私人的网盘服务。

NextCloud 的服务端采用 PHP 编写，底层存储默认保存在服务器的本地硬盘中。通过修改 NextCloud 配置，可以使用腾讯云对象存储 COS 作为底层存储，享受对象存储 COS 带来的更低廉的存储成本、更高的可靠性和容灾能力，以及无限的存储空间。

本文将介绍 NextCloud 服务端所依赖的环境，并分析对比本地存储与对象存储 COS 的区别，最后将讲解实战搭建个人网盘。

>! 将现有 NextCloud 服务端实例从本地存储更改为使用腾讯云对象存储可能导致已有的文件不可见。如需修改已有实例的存储方式，建议依照本教程搭建全新的 NextCloud 服务端并配置使用腾讯云对象存储，随后将旧实例的数据迁移至新实例。

## NextCloud 服务端环境简介

NextCloud 服务端采用 PHP 编写，数据库可以使用 SQLite、MySQL、MariaDB 或 PostgreSQL，其中 SQLite 由于性能上的限制，通常不建议在实际应用中使用。虽然 PHP、MySQL 及相关的服务器软件都有 Windows 版本，但是根据 NextCloud 社区的反馈，在 Windows 下运行 NextCloud 服务端会存在文字编码等问题，因此官方宣称不支持在 Windows 下部署 NextCloud 服务端。

<span id=1>

### 服务器配置

腾讯云云服务器 CVM 目前有多个实例族，每个实例族中又分为多个子类型。不同的实例族有不同的侧重点，例如大内存或高 IO 等。NextCloud 定位于个人、家庭或中小企业用户，对各项硬件资源需求都不高，因此选择各项资源均衡的标准型即可满足需求。对于子类型，通常来说最新的子类型将拥有更高的性价比，一般情况下选择最新的子类型即可。

在确定好实例族和子类型后，还会面临具体的 vCPU 与内存规格选择，此外不同的 vCPU 与内存规格还有对应的内网带宽和网络收发包。PHP 可以使用 OPcache 提升性能，而 NextCloud 服务端支持使用 APCu 内存缓存进一步提升性能，因此在规格的选择上，建议选择较大的内存。

由于 CVM 在购买后支持配置的调整，我们可以先购买配置比较低的规格，例如1核 vCPU 与4GB内存，在完成搭建并实际上线使用后，根据用户数、文件数以及 CVM 的相关监控数据在判断是否需要提高规格提升性能。如果您预期在家庭或中小企业等多用户场景下使用，那么建议选购2核8GB到4核16GB的配置，以提供足够的性能满足多用户的使用。

### 服务器操作系统

主流的 Linux 发行版都可以很好的支持 NextCloud 服务端运行，除了不同系统在安装软件包时使用的命令（即包管理工具）有所差别外，其余的配置工作没有区别。

>?本文将以运行 CentOS 7.7操作系统的云服务器 CVM 为例进行后续的演示。

### 数据库

如上文所述，在实际应用中通常使用 MySQL 搭配 PHP 使用，而 MariaDB 是 MySQL 的“复刻”版本，与 MySQL 保持高度的兼容，因此 MySQL 5.7+或 MariaDB 10.2+均可以很好的配合 NextCloud 服务端使用。

腾讯云提供托管的云数据库 MySQL 和云数据库 MariaDB，相对于在 CVM 上自建数据库，云数据库默认采用一主一备的高可用模式，具有更高的可靠性，且提供自动备份等方便的运维操作，因此强烈建议在实际应用中使用云数据库。

>?本文将以云数据库 MySQL 5.7版本为例进行后续的演示。

### Web 服务器及 PHP 运行时

NextCloud 服务端通过`.htaccess`指定了部分配置，因此使用 Apache 服务器软件时可直接使用 NextCloud 服务端自带的配置项。Nginx 是近些年发展较快的 Web 服务器软件，相对 Apache 具有安装配置简单、资源占用少、负载能力更强的优点，通过将 NextCloud 服务端中的`.htaccess`配置转写为 Nginx 的配置，亦可很好的支持 NextCloud 服务端的运行，本文将使用 Nginx 服务器软件，并提供完整的 Nginx 配置示例可供参考。

PHP 运行时目前已经发展到 PHP 7，主要维护的版本包括7.2、7.3和7.4，这3个版本均支持 NextCloud 服务端，我们使用最新的7.4即可。此外，NextCloud 还依赖 PHP 的部分扩展模块，下文将详细介绍具体的扩展模块要求。

### 腾讯云网络环境

腾讯云目前提供基础网络和私有网络（VPC）环境。基础网络是腾讯云上所有用户的公共网络资源池，所有 CVM 的内网 IP 地址都由腾讯云统一分配，无法自定义网段划分、IP 地址。私有网络是用户在腾讯云上建立的一块逻辑隔离的网络空间，在私有网络内，用户可以自由定义网段划分、IP 地址和路由策略。目前基础网络由于资源紧缺且无法扩增等功能，新注册账号及部分新建可用区均不再支持基础网络，因此本文将以私有网络为例进行后续的演示。

>?有关私有网络的进一步介绍，请参阅 [私有网络产品概述](https://cloud.tencent.com/document/product/215/20046)。

## 云硬盘 CBS 与对象存储 COS 的对比

在云服务器 CVM 中，云硬盘 CBS 将以 CVM 中的本地硬盘的形式挂载在操作系统中，NextCloud 默认使用文件系统存储网盘数据，因此可以直接将 NextCloud 的数据存储在操作系统中的云硬盘。那么与云硬盘 CBS 相比，使用对象存储 COS 有哪些优势呢？下面从几个维度讲解一下两者之间的区别。

### 应用场景

#### 云硬盘 CBS

云硬盘 CBS 属于块存储，可直接挂载到 CVM 操作系统中作为硬盘使用，通常情况被操作系统独占，即只能挂载在一台 CVM 中，但其拥有较高的读写性能，适用于高 IO 低延时且不需要与其他 CVM 共享的场景。

#### 对象存储 COS

对象存储 COS 以 http 协议对外提供读写接口，需要通过编程的方式访问 COS 的存储的对象（文件）。对象存储使用对象键（Key，可以理解为文件路径）作为索引，无存储容量的限制。由于使用网络传输，在速度和延时上相对较大，但因为操作是对象级别，因此一个软件完成一个对象的操作后，另一个软件即可马上操作同一对象，适用于对性能要求不高、需要低成本大容量存储或有共享访问需求的场景。由于网盘应用本身通过网络传输，对延时的要求不高，且从网盘客户端到网盘服务端再到 COS 的链路中，影响速度与时延的因素主要在于客户端所处的网络环境，而 COS 本身不限速，因此 COS 更适合搭配网盘应用。

### 费用

#### 云硬盘 CBS

云硬盘 CBS 根据性能和地域定价有所不同，由于网盘应用对延时和 IOPS 要求不高，这里我们以高性能云硬盘为例（由于普通云硬盘为上一代产品，未来将主推高性能云硬盘，故此处以高性能云硬盘为例），上海地域高性能云硬盘包年包月的费用为0.35元/GB/月，实际采购时3年或以上执行5折优惠。

#### 对象存储 COS

对象存储 COS 根据地域定价有所不同，且存在预付费和后付费模式，后付费模式为按需付费，上海地域标准存储单价为0.118元/GB/月，在用于 NextCloud 时，需要使用与 CVM 相同地域的 COS 服务，此时网络流量走腾讯云的内网，不收取流量费用；此外，COS 还会涉及一个请求费用，上海地域单价为0.01元/万次，在网盘应用中，该费用每月仅约几分钱，基本可以忽略。

#### 对比

除了 COS 在单价上已经接近 CBS 的1/3，由于 COS 后付费为按需付费，而 CBS 需要预先购买，在实际花费上还要为 CBS 暂时没有用到的空间付费，因此使用 COS 的费用还可以更节省。如果在使用 COS 的过程中容量需求较大，还可以以更优惠的价格采购 COS 资源包（即 COS 预付费模式），例如您当前的网盘已经占用560GB，那么采购500GB的标准存储容量包（39.53元/月）+60GB后付费（0.118\*60=7.08元/月），实际每月消耗仅需要不到50元。而使用 CBS，按照560GB 精打细算也要196元/月，实际使用时至少需要预留20%的可用空间，那么费用更是高达244元/月。

### 维护

#### 云硬盘 CBS

云硬盘 CBS 为固定容量，可通过控制台或云 API 扩容，扩容后还需要在操作系统中扩展分区，且在扩展分区时有一定的分区异常风险，有一定的维护成本。

#### 对象存储 COS

对象存储 COS 按需使用，不限制总容量，也不限制对象数（文件数），完全无需维护。

### 数据安全

云硬盘 CBS 和对象存储 COS 均使用多副本等手段保证数据的可靠性。

## 搭建 NextCloud 服务端运行环境

### 准备 NextCloud 服务端依赖的云产品

#### 云服务器 CVM

1. 打开并登录 [云服务器选购](https://buy.cloud.tencent.com/cvm) 页面，进入【自定义配置】选项卡，根据下表说明进行配置：

| 配置项           | 值                                                           |
| ---------------- | ------------------------------------------------------------ |
| 计费模式         | 包年包月                                                     |
| 地域             | 选择与您所在地最近的地域，请注意不要选择金融专区（带“金融”字样的地域） |
| 可用区           | 随机可用区                                                   |
| 网络类型（如有） | 私有网络                                                     |
| 网络             | 选择 Default-VPC 和 Default-Subnet                           |
| 实例             | 根据 [服务器配置](#1) 中的说明，选择机型和规格，例如标准型 SA2/1核/4GB |
| 镜像             | 公共镜像，CentOS 64位，CentOS 7.7 64位（或其他7.x版均可以）  |
| 系统盘、数据盘   | 保持默认                                                     |
| 定期快照         | 建议勾选“对系统盘设置定期快照”以避免数据被误删或感染病毒等情况导致的数据异常 |
| 公网带宽         | 对于使用频率较低的个人和家庭用户，推荐选择按流量计费，同时为了保证峰值带宽，可以将带宽充分利用；对于使用频率较高、有一定的带宽利用率的企业用户，可以考虑使用按带宽计费，并选择合适的带宽。有关公网带宽的对比和计量计费，可进一步参考页面中的相关链接文档。 |
| 数量             | 1                                                            |
| 时长             | 根据需求进行选择，购买时长越长可享有更多折扣。               |

2. 单击【下一步：设置主机】，根据下表说明进行配置：

| 配置项           | 值                                                           |
| ---------------- | ------------------------------------------------------------ |
| 所属项目         | 默认项目                                                     |
| 安全组           | 新建安全组，放通常用 IP/端口里勾选：ICMP、TCP:22、TCP:80、放通内网 |
| 安全组规则       | 保持默认                                                     |
| 实例名称         | 不填或自定义一个名称                                         |
| 登录方式         | 选择设置密码                                                 |
| 密码、确认密码   | 设置一个足够复杂的密码并牢记                                 |
| 安全加固、云监控 | 勾选免费开通                                                 |
| 自动续费         | 勾选                                                         |

3. 单击【下一步：确认配置信息】，展开【地域和机型】，记录**地域**和**可用区**，并确认全部信息无误后，勾选【同意《腾讯云服务协议》和《退款规则》】，单击【立即购买】。

>?在商品确认页面，可以选择加购对象存储 COS 资源包和高可用版 MySQL，因为 COS 和 MySQL 均为本教程中会用到的云产品，因此强烈建议此时加购，享受更多折扣。

4. 单击【加购对象存储 COS 资源包】，根据下表说明进行配置：

| 配置项     | 值                                                           |
| ---------- | ------------------------------------------------------------ |
| 资源包类型 | 标准存储容量                                                 |
| 地域类型   | 根据 CVM 所属地域选择                                        |
| 规格       | 根据预估在网盘中存储的数据量进行购买，COS 资源包可以叠加，因此您可以先购买一个较小规格的资源包，当需要时再叠加购买用以抵扣更多的标准存储容量。 |
| 有效时长   | 根据需求进行选择，如果考虑后续购买更大资源包，可以选择较短时长并及时续购。 |
| 购买数量   | 1个。购买多个将叠加所抵扣的标准存储容量，不如直接购买较大规格的资源包折扣高。 |

5. 单击【立即购买】将 COS 资源包加入订单，然后单击【加购高可用版 MySQL】，根据下表说明进行配置：

| 配置项     | 值                                                           |
| ---------- | ------------------------------------------------------------ |
| 地域、网络 | 与 CVM 的【地域】和【可用区】保持一致                        |
| 项目       | 保持默认                                                     |
| 数据库版本 | MySQL5.7                                                     |
| 规格       | 1核，1000MB内存，50GB硬盘（如果您对性能或空间有更高需求，也可以选择更高配置，或在未来有需要时随时调整配置） |
| 数量       | 1                                                            |
| 时长       | 根据需求进行选择                                             |

6. 单击【确认加购】完成 MySQL 的加购，确认订单内容无误后，单击【提交订单】并根据提示完成支付。

#### 云数据库 MySQL

如果您在购买云服务器 CVM 时没有加购云数据库 MySQL，那么您需要先购买 MySQL；如果已经购买 MySQL 则可以跳过购买 MySQL 环节，直接跳转至 [配置 MySQL](#2)。

##### 购买 MySQL

1. 打开并登录 [云数据库 MySQL 选购](https://buy.cloud.tencent.com/cdb) 页面，根据下表说明进行配置：

| 配置项             | 值                                                           |
| ------------------ | ------------------------------------------------------------ |
| 计费模式           | 包年包月                                                     |
| 地域               | 与所购 CVM 保持一致                                          |
| 数据库版本         | MySQL5.7（请注意不要选择 CynosDB 版本）                      |
| 架构               | 高可用版                                                     |
| 主可用区           | 与所购 CVM 保持一致                                          |
| 备可用区（如可选） | 与主可用区保持一致                                           |
| 实例规格           | 1核1000MB（如果您对性能更高需求，也可以选择更高配置，或在未来有需要时随时调整配置） |
| 硬盘               | 50GB（如果您对空间有更高需求，也可以选择更高配置，或在未来有需要时随时调整配置） |
| 网络               | 私有网络（如有）Default-VPC，Default-Subnet                  |
| 安全组             | default 或放通全部端口。如果列表中无相应选项，可单击下方【新建安全组】链接，使用【放通全部端口】模板创建新的安全组，并返回该页面，刷新安全组列表后选择刚才创建的安全组。 |
| 指定项目           | 保持默认                                                     |
| 实例名             | 立即命名，并指定一个实例名称，例如 nextcloud。（该实例名并非数据库名，可任意指定，后期也可修改） |
| 购买数量           | 1                                                            |
| 购买时长           | 根据需求进行选择                                             |
| 自动续费、服务条款 | 勾选                                                         |

2. 单击【立即购买】，确认订单内容无误后，单击【提交订单】并根据提示完成支付。

<span id=2>

##### 配置 MySQL

1. 打开并登录 [MySQL 控制台](https://console.cloud.tencent.com/cdb)，选择先前购买 MySQL 时选择的地域，并选择所购的 MySQL 示例，单击更多操作中的【初始化】，根据下表说明进行配置：

| 配置项                       | 值                           |
| ---------------------------- | ---------------------------- |
| 支持字符集                   | UTF8MB4                      |
| 表名大小写敏感               | 开启                         |
| 自定义端口                   | 3306                         |
| 设置 root 帐号密码、确认密码 | 设置一个足够复杂的密码并牢记 |

2. 单击【确定】，预计5-10分钟后完成 MySQL 实例初始化，如果实例状态一直没有变化为【运行中】，可刷新实例列表查看最新状态。

#### 对象存储 COS

1. 打开并登录 [对象存储控制台](https://console.cloud.tencent.com/cos5)（首次使用需先开通对象存储服务），进入【存储桶列表】，单击【创建存储桶】，根据下表说明进行配置：

| 配置项   | 值                                                           |
| -------- | ------------------------------------------------------------ |
| 名称     | 输入一个自定义的存储桶名称，例如 nextcloud。注意，该名称确定后将不允许更改 |
| 所属地域 | 与所购 CVM 所属地域保持一致                                  |
| 其他     | 保持默认                                                     |

2. 完成以上配置后，单击【确定】完成创建。

### 安装、配置 Web 服务器和 PHP 进行时

#### 安装 Nginx

1. 使用 SSH 工具登录到新购服务器。
2. 执行下述命令安装 Nginx：
```bash
yum install nginx
```
当提示以下信息时，按 `Y` 并回车确认安装（下同）。
```bash
Is this ok [y/d/N]:
```
3. 当出现以下信息时，表示安装完成。
```bash
Complete!
[root@VM-0-10-centos ~]#
```
4. 接下来执行以下命令，验证是否可以正常查看 Nginx 版本。
```bash
nginx -v
```
假如出现以下信息，则验证安装完成。
```bash
nginx version: nginx/1.16.1
```

#### 安装 PHP

1. 使用 SSH 工具登录到新购服务器。
2. 执行下述命令开始安装 PHP 7.4：
```bash
yum install epel-release yum-utils
```

继续依次执行下述命令：
**命令1：**
```bash
yum install http://rpms.remirepo.net/enterprise/remi-release-7.rpm
```

>?执行上述命令时如遇速度过慢、进度长时间不动，可以按 `Ctrl-C` 取消并重新执行该条命令（下同）。

**命令2：**
```bash
yum-config-manager --enable remi-php74
```
**命令3：**
```bash
yum install php php-fpm
```

3. 安装完成后，执行以下命令，验证是否可以正常查看 PHP 版本。
```bash
php -v
```
假如出现以下信息，则验证安装完成。
```bash
PHP 7.4.8 (cli) (built: Jul 9 2020 08:57:23) ( NTS )
Copyright (c) The PHP Group
Zend Engine v3.4.0, Copyright (c) Zend Technologies
```

#### 安装 PHP 模块

除了基本的 PHP 外，NextCloud 还依赖其他 PHP 模块来实现部分功能。有关 NextCloud 依赖的详细模块信息，可参阅 [NextCloud 官方文档](https://docs.nextcloud.com/server/19/admin_manual/installation/source_installation.html#prerequisites-for-manual-installation)。

本教程中将安装 NextCloud 必选的 PHP 模块，如果您计划后续使用 NextCloud 的其他可选功能，请留意并自行安装所依赖的其他 PHP 模块。

1. 使用 SSH 工具登录到新购服务器。
2. 执行下述命令安装 PHP 模块：
```bash
yum install php-xml php-gd php-mbstring php-mysqlnd php-intl php-zip
```
3. 安装完成后，执行以下命令查看已安装的 PHP 模块。
```bash
php -m
```
4. 如果还需要安装其他模块，重复执行 `yum install <php-module-name>` 即可。

#### 上传并解压 NextCloud 服务端代码

1. 在 [NextCloud 官网](https://nextcloud.com/install/#instructions-server) 下载 NextCloud 服务端最新版安装包，并上传至服务器 `/var/www/` 目录下，您可以通过以下方法上传：
    a）使用 `wget` 命令直接在服务器上下载安装包，例如：进入 `/var/www/` 目录后，执行命令 `wget https://download.nextcloud.com/server/releases/nextcloud-19.0.1.zip`。
    b）下载到本地计算机上，然后通过 SFTP 或 SCP 等软件将安装包上传至 `/var/www/` 目录。
    c）下载到本地计算机上，使用 lrzsz 上传，方法是：
  1. 使用 SSH 工具登录到新购服务器。
  2. 执行 `yum install lrzsz` 安装 lrzsz。
  3. 执行 `cd /var/www/` 进入目标目录。
  4. 执行 `rz -bye`，随后在 SSH 工具中选择下载到本地的 NextCloud 服务端安装包（依据 SSH 工具的不同，此处操作将不尽相同）。
2. 使用 SSH 工具登录到新购服务器。
3. 执行 `unzip nextcloud-<version>.zip` 解压安装包，例如 `unzip nextcloud-19.0.1.zip`。

#### 配置 PHP

1. 使用 SSH 工具登录到新购服务器。
2. 执行 `vim /etc/php-fpm.d/www.conf` 打开 PHP-FPM 的配置文件，并依次修改配置项（关于 vim 的具体使用请参阅相关资料，您也可以使用其他方式修改该配置文件）。
   a）将 `user = apache` 修改为 `user = nginx`。
    b）将 `group = apache` 修改为 `group = nginx`。
3. 修改完成后，输入 `:wq` 保存文件并退出（有关 vim 的详细操作指引，请参阅相关文档）。
4. 执行下述命令修改目录所有者，使 PHP 能够适配 Nginx 使用：
```bash
chown -R nginx:nginx /var/lib/php
```
5. 依次执行下述命令，并启动 PHP-FPM 服务：
**命令1：**
```bash
systemctl enable php-fpm   # 命令1
```
**命令2：**
```bash
systemctl start php-fpm   # 命令2
```

#### 配置 Nginx

1. 使用 SSH 工具登录到新购服务器。
2. 执行下述命令修改网站目录所有者：
```bash
chown -R nginx:nginx /var/www
```
3. 备份当前的 Nginx 配置文件 `/etc/nginx/nginx.conf`，您可以：
   a）执行 `cp /etc/nginx/nginx.conf ~/nginx.conf.bak` 将当前配置文件备份到家（HOME）目录。
   b）使用 SFTP 或 SCP 等软件将当前配置文件下载到本地计算机。
4. 将`/etc/nginx/nginx.conf` 修改或替换为如下内容：

```plaintext
# For more information on configuration, see:
#   * Official English Documentation: http://nginx.org/en/docs/
#   * Official Russian Documentation: http://nginx.org/ru/docs/

user nginx;
worker_processes auto;
error_log /var/log/nginx/error.log;
pid /run/nginx.pid;

# Load dynamic modules. See /usr/share/doc/nginx/README.dynamic.
include /usr/share/nginx/modules/*.conf;

events {
    worker_connections 1024;
}

http {
    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile            on;
    tcp_nopush          on;
    tcp_nodelay         on;
    keepalive_timeout   65;
    types_hash_max_size 2048;

    include             /etc/nginx/mime.types;
    default_type        application/octet-stream;

    # Load modular configuration files from the /etc/nginx/conf.d directory.
    # See http://nginx.org/en/docs/ngx_core_module.html#include
    # for more information.
    include /etc/nginx/conf.d/*.conf;

    server {
        listen       80 default_server;
        listen       [::]:80 default_server;
        server_name  _;
        root         /var/www/nextcloud;

        add_header Referrer-Policy "no-referrer" always;
        add_header X-Content-Type-Options "nosniff" always;
        add_header X-Download-Options "noopen" always;
        add_header X-Frame-Options "SAMEORIGIN" always;
        add_header X-Permitted-Cross-Domain-Policies "none" always;
        add_header X-Robots-Tag "none" always;
        add_header X-XSS-Protection "1; mode=block" always;

        client_max_body_size 512M;
        fastcgi_buffers 64 4K;

        gzip on;
        gzip_vary on;
        gzip_comp_level 4;
        gzip_min_length 256;
        gzip_proxied expired no-cache no-store private no_last_modified no_etag auth;
        gzip_types application/atom+xml application/javascript application/json application/ld+json application/manifest+json application/rss+xml application/vnd.geo+json application/vnd.ms-fontobject application/x-font-ttf application/x-web-app-manifest+json application/xhtml+xml application/xml font/opentype image/bmp image/svg+xml image/x-icon text/cache-manifest text/css text/plain text/vcard text/vnd.rim.location.xloc text/vtt text/x-component text/x-cross-domain-policy;

        # Load configuration files for the default server block.
        include /etc/nginx/default.d/*.conf;

        location / {
            try_files $uri $uri/ =404;
            index index.php;
        }

        location ~ ^\/(?:build|tests|config|lib|3rdparty|templates|data)\/ {
            deny all;
        }
        location ~ ^\/(?:\.|autotest|occ|issue|indie|db_|console) {
            deny all;
        }

        location ~ ^\/(?:index|remote|public|cron|core\/ajax\/update|status|ocs\/v[12]|updater\/.+|oc[ms]-provider\/.+)\.php(?:$|\/) {
            fastcgi_split_path_info ^(.+?\.php)(\/.*|)$;
            set $path_info $fastcgi_path_info;
            try_files $fastcgi_script_name =404;
            include fastcgi_params;
            fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
            fastcgi_param PATH_INFO $path_info;
            fastcgi_param modHeadersAvailable true;
            fastcgi_pass 127.0.0.1:9000;
            fastcgi_intercept_errors on;
            fastcgi_request_buffering off;
        }

        location ~ ^\/(?:updater|oc[ms]-provider)(?:$|\/) {
            try_files $uri/ =404;
            index index.php;
        }

        location ~ \.(css|js|svg|gif)$ {
            add_header Cache-Control "max-age=15778463";
        }

        location ~ \.woff2?$ {
            add_header Cache-Control "max-age=604800";
        }
    }

# Settings for a TLS enabled server.
#
#    server {
#        listen       443 ssl http2 default_server;
#        listen       [::]:443 ssl http2 default_server;
#        server_name  _;
#        root         /usr/share/nginx/html;
#
#        ssl_certificate "/etc/pki/nginx/server.crt";
#        ssl_certificate_key "/etc/pki/nginx/private/server.key";
#        ssl_session_cache shared:SSL:1m;
#        ssl_session_timeout  10m;
#        ssl_ciphers HIGH:!aNULL:!MD5;
#        ssl_prefer_server_ciphers on;
#
#        # Load configuration files for the default server block.
#        include /etc/nginx/default.d/*.conf;
#
#        location / {
#        }
#
#        error_page 404 /404.html;
#            location = /40x.html {
#        }
#
#        error_page 500 502 503 504 /50x.html;
#            location = /50x.html {
#        }
#    }

}
```

5. 依次执行下述命令，并启动 Nginx 服务：
   **命令1：**
```bash
systemctl enable nginx
```
**命令2：**
```bash
systemctl start nginx
```

## 配置 NextCloud 服务端使用对象存储 COS

### 获取 COS 相关信息

1. 登录到腾讯云 [对象存储控制台](https://console.cloud.tencent.com/cos5)。
2. 找到此前创建的存储桶，并单击右侧【配置管理】。
   ![](https://main.qcloudimg.com/raw/3af907cf7791d30af7fd9bff6df3df45.png)
3. 在跳转界面中，记录【基本信息】中的**空间名称**和**所属地域**中的英文部分。
   ![](https://main.qcloudimg.com/raw/4b4ca9a2cd911991ce4b41863bccec2c.png)

### 获取 API 密钥

1. 登录腾讯云 [访问密钥控制台](https://console.cloud.tencent.com/cam/capi)。
2. 记录表格中【密钥】中的**SecretId**和**SecretKey**。如果表格中没有有效密钥，可单击左上角【新建密钥】创建新的密钥。
   ![](https://main.qcloudimg.com/raw/39ad3be8edd97e4c72d4b5c745032b16.png)

### 修改 NextCloud 服务端配置文件

1. 使用文本编辑工具创建 `config.php`，输入如下内容并根据注释修改相关的值：

```php
<?php
$CONFIG = array(
  'objectstore' => array(
    'class' => '\\OC\\Files\\ObjectStore\\S3',
    'arguments' => array(
      'bucket' => 'nextcloud-1250000000', // 存储桶名称（空间名称）
      'autocreate' => false,
      'key'  => 'AKIDxxxxxxxx', // 替换为用户的 SecretId
      'secret' => 'xxxxxxxxxxxx', // 替换为用户的 SecretKey
      'hostname' => 'cos.<Region>.myqcloud.com', // 将 <Region> 修改为所属地域，如 ap-shanghai
      'use_ssl' => true,
    ),
  ),
);

```

如下图所示：
![](https://main.qcloudimg.com/raw/b14a23e2cac3ac988745fcd82fe56e18.png)

2. 将该文件保存并上传到 `/var/www/nextcloud/config/` 目录下（保持文件名为`config.php`），您可以通过 SFTP 或 SCP 软件上传文件，也可以通过 `rz -bye` 命令上传。
3. 执行下述命令修改配置文件的所有者：
```bash
chown nginx:nginx /var/www/nextcloud/config/config.php
```

## 配置域名

若您计划使用自己的域名而不是 IP 地址访问您的 NextCloud 服务端，您可参考各域名注册商（例如腾讯云 [域名注册](https://dnspod.cloud.tencent.com/)）和相关域名解析服务（例如腾讯云 [DNS 解析](https://cloud.tencent.com/product/cns)）的说明文档，注册新域名并将域名解析到您 CVM 的 IP 地址并完成备案。

由于 NextCloud 服务端在安装过程中会记录安装时使用的域名或 IP 地址，因此建议您在开始安装前完成域名的注册、解析和备案，并使用域名访问 NextCloud 服务端的安全界面。

如果您在完成 NextCloud 服务端后需要更换域名或 IP 地址，您可以自行修改 `/var/www/nextcloud/config/config.php` 配置文件中的 `trusted_domains`，详情请参阅 [NextCloud 官方文档](https://docs.nextcloud.com/server/19/admin_manual/installation/installation_wizard.html#trusted-domains)。

## 安装 NextCloud 服务端

1. 使用浏览器访问 NextCloud 服务端，创建并牢记管理员用户名和密码。
2. 展开【存储与数据库】，根据下表说明进行配置：

| 配置项                             | 值                                      |
| ---------------------------------- | --------------------------------------- |
| 数据名录                           | /var/www/nextcloud/data（保持默认）     |
| 配置数据库                         | MySQL/MariaDB                           |
| 数据库用户                         | root                                    |
| 数据库密码                         | 初始化云数据库 MySQL 时填写的 root 密码 |
| 数据库名                           | nextcloud（或其他未被使用的数据库名）   |
| 数据库主机（默认显示为 localhost） | 云数据库 MySQL 的内网地址               |

![](https://main.qcloudimg.com/raw/56558537c7d968c762a062dae1d9d182.png)

3.   单击【安装完成】，等待 NextCloud 服务端完成安装。
4.   如果安装过程中出现504 Gateway Timeout 等错误信息，可直接刷新重试。
5.   安装完成后，使用管理员账号登录 NextCloud 服务端即可开始使用网页版 NextCloud。

## NextCloud 服务端调优

### 后台任务

NextCloud 服务端有时需要在无需用户交互时执行一些后台任务，例如数据库清理等操作。PHP 的运行特性限制了基于 PHP 的程序无法内部维持一个独立的工作进程或线程，因此类似后台任务的场景需要由外部主动调用对应的 PHP 程序来执行。

NextCloud 服务端提供3种后台任务的调用方式，默认是通过网页端的登录用户，在浏览器自动发起 AJAX 请求来唤起服务端的后台任务执行，这种方式严重依赖用户的登录情况，如果没有用户登录，那么这些后台任务将无法执行，因此可靠性最低。

为了避免基于 AJAX 的后台任务可靠性低的问题，我们推荐使用 Linux 下的 cron 来配置后台任务，Linux 下的 cron 可以精确的控制任务被唤起的时间，例如每5分钟（分钟数为5的整数倍）或每个整点的第10分钟等等，可定义的时间粒度包括分钟、小时、一个月中的某天、月份和星期几，一些操作系统还支持秒和年，因此具备高度灵活性。有关 cron 的相关说明和配置，您可参考相关资料。

下面将介绍下如何配置 cron 来满足 NextCloud 服务端的后台任务：

1. 使用 SSH 工具登录到新购服务器。
2. 执行下述命令安装 PHP 模块：
```bash
yum install php-posix
```
3. 执行下述命令打开或创建用于 nginx 账户的 cron 配置：
```bash
crontab -u nginx -e
```
4.   接下来的编辑界面为 vi/vim，按 `i` 键进入编辑模式，插入一行，内容如下：
```plaintext
*/5 * * * * php -f /var/www/nextcloud/cron.php
```
随后按 `ESC` 退出编辑模式，输入 `:wq` 保存退出（有关 vi/vim 的详细操作指引，请参阅相关文档）。
上述配置使用了 NextCloud 官方推荐的每5分钟执行一次（分钟数是5的整数倍）。待5分钟后后台任务执行完成，可以打开浏览器登录 NextCloud 服务端，单击右上角用户名首字母图标，进入【设置】，在左侧菜单进入【基本设置】，可以看到【后台任务】处默认选中了 Cron。

![](https://main.qcloudimg.com/raw/7f3c9999efbd5a357aa10597b6c4edf0.png)

### 内存缓存

PHP 可以使用 OPcache 提升性能，NextCloud 服务端也支持使用 APCu 内存缓存进一步提升性能，下面将介绍下相关的操作流程：

1. 使用 SSH 工具登录到新购服务器。
2. 执行下述命令安装 PHP 模块：
```bash
yum install php-pecl-apcu
```
3. 依次执行下述命令重启 Nginx 和 PHP-FPM：
   **命令1：**
```bash
systemctl restart nginx
```
**命令2：**
```bash
systemctl restart php-fpm
```
4. 执行 `vim /var/www/nextcloud/config/config.php`，打开 NextCloud 服务端的配置文件，在 `$CONFIG = array (` 中添加一行：`'memcache.local' => '\OC\Memcache\APCu',`，随后保存文件并退出；
   ![](https://main.qcloudimg.com/raw/eaa28e013991aad579cf6abc2a34d9bb.png)
5. 如果配置了 cron 来优化后台任务，那么还需要修改 PHP 的 apc 配置：执行 `vim /etc/php.d/40-apcu.ini`，打开 PHP APCu 的配置文件，将 `;apc.enable_cli=0` 修改为 `apc.enable_cli=1`（请注意需要同时去掉前面分号），保存退出。如果路径 `/etc/php.d/40-apcu.ini` 不存在，那么请自行在 `/etc/php.d/` 目录下查找并编辑有 apc 或 apcu 字样的 `.ini` 配置文件。
   ![](https://main.qcloudimg.com/raw/1c57fe0a2078aa0ca5dd7ba07b23fe86.png)

## 配置客户端访问

NextCloud 官方提供桌面同步客户端和移动客户端，可在 NextCloud 官网或各大应用商店下载。在配置 NextCloud 时需输入 NextCloud 的服务端地址（域名或 IP），随后输入自己的用户名和密码并登录，即可开始使用客户端。
