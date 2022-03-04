
开源操作系统社区 OpenCloudOS 由腾讯与合作伙伴共同倡议发起，是完全中立、全面开放、安全稳定、高性能的操作系统及生态。OpenCloudOS 沉淀了多家厂商在软件和开源生态的优势，继承了腾讯在操作系统和内核层面超过10年的技术积累，在云原生、稳定性、性能、硬件支持等方面均有坚实支撑，可以平等全面地支持所有硬件平台。OpenCloudOS 8.5是 OpenCloudOS 社区发布首个正式版本，其基础库和用户态组件完全与 CentOS8兼容，并通过内核层面的优化和增强，能够提供给用户相比于 CentOS8更优的解决方案。

## 适用说明
OpenCloudOS 适用于云上绝大多数机型生产实例，包括云服务器，黑石物理服务器2.0等。

<dx-alert infotype="notice" title="">
目前 OpenCloudOS 未预装 GPU驱动，若需在 GPU 实例上使用，则请手动安装 GPU 驱动。
</dx-alert>




## OpenCloudOS 镜像版本
目前已支持在腾讯云上使用 OpenCloudOS 8.5版本镜像，该镜像与 CentOS 8用户态完全兼容，配套了基于社区5.4 LTS 的 OpenCLoudOS Kernel。


## OpenCloudOS 内核
OpenCloudOS Kernel为基于社区5.4 LTS打造的稳定、高性能 kernel； 不但包含社区最新关键特性，还包含针对不同业务场景做的针对性优化。在保证kernel稳定的同时，保持技术上不断的更新迭代。

## 使用 OpenCloudOS
您可在创建实例，或重装已有实例操作系统时，选择公共镜像，并选择使用 OpenCloudOS 的相应版本。操作详情请参见  [创建实例](https://cloud.tencent.com/document/product/213/4855) 及 [重装系统](https://cloud.tencent.com/document/product/213/4933)。

## 获取 OpenCloudOS
请前往 [OpenCloudOS 8.5](http://mirrors.tencent.com/opencloudos/8.5/isos/) 获取 OpenCloudOS。


## 服务与更新
OpenCloudOS 社区将为每个 OpenCloudOS 大版本（例如 OpenCloudOS 8）提供有长达10年的维护和更新，包括最新的 kernel 特性、安全漏洞修复及 bug 修复等。存量服务器可以通过 yum 升级，及时完成漏洞修复。
