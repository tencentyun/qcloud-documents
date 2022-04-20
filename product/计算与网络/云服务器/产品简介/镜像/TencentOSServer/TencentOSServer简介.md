TencentOS Server（又名 Tlinux，简称 TS）是腾讯云针对云的场景研发的 Linux 操作系统，提供特定的功能及性能优化，为云服务器实例中的应用程序提供更高的性能及更加安全可靠的运行环境。TencentOS Server 基于 Linux 内核自主研发设计，积累了腾讯在操作系统领域超过10年的技术积累，并经过了腾讯内部海量业务多年验证和打磨，在腾讯内部操作系统里占比超99%，覆盖了腾讯所有的业务。同时，腾讯有着国内最种类繁多的业务生态，从社交、游戏、金融支付、AI、安全等，其稳定性、安全性、兼容性和性能等核心能力均已得到长时间充分验证，相比社区 OS 版本，TencentOS Server 在稳定性、性能、容器基础设施等核心能力方面做了全面的增强和优化，能为企业提供稳定高可用的服务，满足业务严苛负载需求，力求打造云上最佳操作系统，也是相比于 CentOS 更佳的企业级操作系统解决方案。

TencentOS Server 目前开放使用，用户态环境与 CentOS 保持兼容，在 CentOS 上开发的应用程序可直接在 TencentOS Server 上运行。


## 适用说明
TencentOS  Server 适用于绝大多数标准机型，包括标准型、计算型、内存性、高 IO 型等。同时支持黑石物理服务器2.0及高性能计算集群等。

<dx-alert infotype="notice" title="">
若您需使用 TencentOS Server 运行 GPU 实例，则请安装对应的 GPU 驱动。
</dx-alert>


## TencentOS Server 优势
- **极致稳定，经千万级节点验证**
TencentOS Server 已经历海量业务长时间的实际考验，部署总量达千万级，整体可用性达99.999%。
- **全面优化，更高性能**
深度优化的高性能 OS，针对系统内的各类软件均已进行优化，典型业务性能提升50%以上，通过腾讯云使用 TencentOS Server 可获得更高性能。
- **开源兼容，云上更优 OS**
100%开源的 Linux 发行版，用户态保持与 CentOS 兼容，且稳定性和性能更具优势，是云上 CentOS 的更优替代方案。
- **为云而生，深度定制**
专为云开发，适用于各种工作负载，含有最新的、基于开放标准的虚拟化和云原生工具。
- **安全合规，零停机修复**
安全实验室守护系统安全，系统级安全增强，及时修复各类漏洞，并支持热补丁修复，可避免不必要的停机时间。



## TencentOS Server 镜像版本
目前腾讯云上有3款 TencentOS Server 镜像供用户选择：

<table>
<tr>
<th width="35%">镜像版本</th>
<th>说明</th>
</tr>
<tr>
<td>TencentOS Server 3.1</td>
<td>与 CentOS 8用户态完全兼容，配套基于社区5.4 LTS 内核深度优化的 tkernel4版本。</td>
</tr>
<tr>
<td>TencentOS Server 2.4</td>
<td>与 CentOS 7用户态完全兼容，配套基于社区4.14 LTS 内核深度优化的 tkernel3版本。</td>
</tr>
<tr>
<td>TencentOS Server 2.4（TK4）</td>
<td>与 CentOS 7用户态完全兼容，配套基于社区5.4 LTS 内核深度优化的 tkernel3版本。</td>
</tr>
</table>



## TencentOS Server 内核
TencentOS Server 内核（简称 tkernel）与发行版解耦，当前主力内核分两个版本，
- 基于社区5.4 LTS 深度优化的 tkernel4（简称 tk4）。
- 基于社区4.14 LTS 深度优化的 tkernel3（简称 tk3）。
详情见 [TencentOS kernel github 仓库](https://github.com/Tencent/TencentOS-kernel)。

## 使用 TencentOS Server 

### 云上使用
您可在创建实例，或重装已有实例操作系统时，选择公共镜像，并选择使用 TencentOS Server 的相应版本。操作详情请参见 [创建实例](https://cloud.tencent.com/document/product/213/4855) 及 [重装系统](https://cloud.tencent.com/document/product/213/4933)。

### 本地体验
您可以通过下列方法在本地体验 TencentOS Server：
- TencentOS Server 2.4 ：[iso](http://mirrors.tencent.com/tlinux/2.4/iso/) 及 [qcow](http://mirrors.tencent.com/tlinux/2.4/images/)。
- TencentOS Server 3.1  ：[iso](http://mirrors.tencent.com/tlinux/3.1/iso/) 及 [qcow](http://mirrors.tencent.com/tlinux/3.1/images/)。


## 更新记录
详情请参见 [TencentOS Server 镜像更新日志](https://cloud.tencent.com/document/product/213/68849)。


## 服务与更新
腾讯云为每个 TencentOS Server 大版本提供超过5年的维护和更新，包括定期更新镜像、新功能和优化引入、及时的安全漏洞修复、Bug 修复等。存量服务器可以通过yum 升级，及时完成漏洞修复。
若您需了解 TencentOS Server 更多信息，可通过小程序咨询腾讯云助手。

