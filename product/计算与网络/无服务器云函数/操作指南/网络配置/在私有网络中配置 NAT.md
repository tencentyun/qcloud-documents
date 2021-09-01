## 操作场景
部署在私有网络（VPC）中的云函数默认隔离外网，如果您想让云函数同时具备内网访问和外网访问能力，您可以选择给 VPC 添加 NAT 网关。



## 前提条件
已 [创建云函数](https://cloud.tencent.com/document/product/583/37509)。

## 操作步骤
## 创建 NAT 网关
NAT 网关（NAT Gateway）是一种支持 IP 地址转换的网络云服务。它能够为腾讯云内的资源提供高性能的 Internet 访问服务。NAT 网关在内外网隔离时，将私有网络（Virtual Private Cloud，VPC）中内网 IP 地址和公网 IP 地址进行转换，实现私有网络访问 Internet 功能。详情请参考 [NAT 网关概述](https://cloud.tencent.com/document/product/552/12951)。

1. 登录 [NAT 网关控制台](https://console.cloud.tencent.com/vpc/nat)，单击**+新建**。
2. 在弹出页面上填写相关信息，本文创建 NAT 网关如下图所示：
>!
> - NAT 网关要和函数、VPC 部署在同一地域。
> - NAT 网关的所属网络需要选择函数所在的 VPC。
> 
![](https://main.qcloudimg.com/raw/237b8a755f875a051622e0fd80e0dffa.png)

## 创建路由策略 
选择似有网络控制台左侧的 **[路由表](https://console.cloud.tencent.com/vpc/route)** ，在页面上方选择路由表所在地域，并单击**+新建**。如下图所示：
![](https://main.qcloudimg.com/raw/29d4c362ff256d92630d75191f51011e.png)
在弹出页面上，您可根据以下两种设置方式选择对应配置，对 SCF 访问公网进行管理。

### SCF 可以访问外网所有地址
若您想使 SCF 具备所有外网的访问权限，可以在路由表中的目的端配置 `IP：0.0.0.0/0`，并把路由表关联到新创建好的 NAT 网关和 SCF 的子网。如下图所示：
![](https://main.qcloudimg.com/raw/ea39bfa1922670751efe58278cac24c5.png)

### SCF 可以访问部分外网地址
若您想使用 SCF 访问部分外网地址，则需添加可访问外网地址至路由表中，并把路由表关联到新创建好的 NAT 网关和 SCF 的子网，如下图所示：
![](https://main.qcloudimg.com/raw/b88ff58541c8f2addb73b72913d2ce80.png)
选择完成后，单击**创建**即可。



