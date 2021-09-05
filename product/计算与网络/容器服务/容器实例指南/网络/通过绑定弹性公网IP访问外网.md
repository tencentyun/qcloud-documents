
## 操作场景

当您的容器实例 EKSCI 需要连接公网时，例如部署 Nginx 服务、拉取私有镜像等，则需要为容器实例绑定弹性公网 IP 或者配置 NAT 网关，并需要支付额外的网络费用。两种使用方式介绍如下：


| 方式 | 说明及使用场景 | 费用 |
|---------|---------|---------|
| <nobr>绑定弹性公网 IP</nobr> | 弹性公网 IP （Elastic IP，简称 EIP），可以独立购买和持有、某个地域下固定不变的公网 IP 地址。<br>使用场景：单个或少量实例需要实现公网互通，例如 Nginx 服务。 | EIP 未绑定云资源时仅收取 IP 资源费用。EIP 绑定云资源后仅收取公网网络费用，详情请参见 [弹性公网 IP 计费](https://cloud.tencent.com/document/product/213/17156)。|
| 绑定 NAT 网关 | NAT 网关（NAT Gateway）是一种支持 IP 地址转换服务，可为私有网络（VPC）内的资源提供安全、高性能的 Internet 访问服务。<br>使用场景：某个 VPC 下的多个实例需要与公网通信，例如多个实例需要拉取第三方镜像仓库镜像。 | NAT 网关服务费用包含两部分：网关费用（按小时计费）和网络费用（按流量计费），详情请参见 [NAT 网关计费](https://cloud.tencent.com/document/product/552/18172)。|

本文主要介绍如何为容器实例绑定弹性公网 IP，以实现容器实例与公网互通。详细操作步骤如下：


## 操作步骤

<dx-alert infotype="explain" title="">
绑定弹性公网 IP 需要在创建容器实例时进行。
</dx-alert>




1. 登录 [容器实例控制台](https://console.cloud.tencent.com/tke2/eksci)，进入容器实例页面。
2. 单击**新建实例**，如下图所示：
![](https://main.qcloudimg.com/raw/4e76f7ed424a9e8ca35af5d77f295fe5.png)
2. 根据实际需求，设置容器实例的参数，详情请参见 [创建容器实例](https://cloud-doc.isd.com/document/product/457/57341#step2)。完成后，单击**下一步**。
3. 开启绑定弹性公网 IP，支持以下两种绑定方式，如下图所示：
![](https://main.qcloudimg.com/raw/a419b90448e11ca2b40b665073c9abea.png)
<dx-tabs>
::: 自动创建弹性公网\sIP
容器实例支持自动创建一个弹性公网 IP 并绑定，其属性如下：
- 按流量计费，如需要使用共享包等预付费模式，请选择下方绑定已有弹性公网 IP 的方式。
- 带宽峰值（需要您自定义），带宽峰值会影响计费，查看详情，请根据需求选择合适的带宽峰值。
- 生命周期与容器实例保持一致，删除容器实例时会同步删除。
:::
::: 使用已有弹性公网\sIP
容器实例同步支持您选择已有的弹性公网 IP，该方式需要您提前创建好弹性公网 IP，若无合适选项，请单击 [新建弹性公网 IP](https://console.cloud.tencent.com/cvm/eip)。
:::
</dx-tabs>
4. 单击**配置确认**，完成弹性公网 IP 绑定。
