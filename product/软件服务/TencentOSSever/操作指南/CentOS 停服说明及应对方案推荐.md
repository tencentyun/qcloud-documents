
## CentOS 停服背景
CentOS 官方计划停止维护 CentOS Linux 项目，CentOS 8及 CentOS 7维护情况如下表格。如需了解更多信息，请参见 [CentOS 官方公告](https://blog.centos.org/2020/12/future-is-centos-stream/?spm=a2c4g.11174386.n2.3.348f4c07hk46v4)。

<table>
<thead>
  <tr>
    <th>操作系统版本</th>
    <th>停止维护时间</th>
    <th>使用者影响</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>CentOS 8</td>
    <td>2022年01月01日</td>
    <td rowspan='2'>停止维护后将无法获得包括问题修复和功能更新在内的任何软件维护和支持。</td>
  </tr>
  <tr>
    <td>CentOS 7</td>
    <td>2024年06月30日</td>
    <td></td>
</tbody>
</table>
针对以上情况，若您需新购云服务器实例，建议选择使用免费的社区稳定版操作系统 OpenCloudOS，或由腾讯提供专业技术支持的 TencentOS Server 镜像。

## OpenCloudOS 与 TencentOS Server 介绍
- **OpenCloudOS** 由腾讯与合作伙伴共同倡议发起，是完全中立、全面开放、安全稳定、高性能的操作系统及生态。
 - 更多 OpenCloudOS 的介绍请参见： [OpenCloudOS 简介](https://cloud.tencent.com/document/product/213/70717) 。
 
- TencentOS Server 是腾讯云针对云的场景研发的 Linux 操作系统，提供特定的功能及性能优化，为云服务器实例中的应用程序提供更高的性能及更加安全可靠的运行环境。
 - 更多 TencentOS Server 的介绍请参见：[TencentOS Server 文档](https://cloud.tencent.com/document/product/1397/72777) 。

### 我们把 Linux 发行版生态供应链的各个阶段分别定义为
- L1 上游发行版，如 OpenCloudOS Stream，以及知名的 Fedora/Debian。
- L2 商业版， 通常由商业公司主导，如腾讯发行的 TencentOS Server， Redhat 发行的 RHEL，Canonical 发行的 Ubuntu。
- L3 社区稳定版，通常是商业系统的免费再发行版本，如 OpenCloudOS，原有的 CentOS 发行版，与 L2 企业版本差异较小。
- L4 社区衍生版，在 L3 基础上优化改造、特性定制的版本。
![](https://qcloudimg.tencent-cloud.cn/raw/2ceea2b0f8b4ed40c55442d31e4ea950.png)

OpenCloudOS属于L3社区稳定版，TencentOS Server属于L2商业版。OpenCloudOS和TencentOS Server的关系与CentOS和红帽RHEL的关系一致。

OpenCloudOS 来源于 TencentOS Server商业稳定版本的输出，在源代码上基本没有差异。主要的差异主要在于商业的、有SLA保障的技术支持服务。

|    |   OpenCloudOS |  TencentOS Server   |  
|-------------------|----------------------------------|----------------------------------|
| Kernel 版本        |  基于 Linux 5.4内核               | 基于 Linux 5.4内核                                                             |  
| 用户态            |  兼容 CentOS 8（OpenCloudOS 8.X） | 兼容 CentOS 7（TencentOS Server 2.4） CentOS 8 （TencentOS Server3.1） | 
| 技术支持          | 依赖 OpenCloudOS 社区  | 依赖 TencentOS Server 技术支持团队 |  
| 缺陷/安全漏洞发布 | 社区发布  | TencentOS Server 技术支持团队发布 |   

OpenCloudOS 是社区化的操作系统，可供用户免费使用，由社区开发者维护。
如果用户需要操作系统专业团队的服务及维护，可以选择购买 TencentOS Server 的订阅服务。
## CentOS迁移指引
- 如果您有需求从 CentOS 8 迁移至 OpenCloudOS，请参见 [CentOS 迁移 OpenCloudOS 指引](https://cloud.tencent.com/document/product/213/85728)。
- 如果您有需求从 CentOS 迁移至 TencentOS Server，请参见[ CentOS 迁移 TencentOS Server 指引](https://cloud.tencent.com/document/product/213/70900)。


