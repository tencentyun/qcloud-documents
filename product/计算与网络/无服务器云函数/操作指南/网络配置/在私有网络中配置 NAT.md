# 在私有网络中配置 NAT

部署在 VPC 中的云函数默认是和外网隔离开的，如果您想让云函数同时具备内网访问和外网访问能力，您可以选择给 VPC 添加 NAT 网关。

## 创建 NAT 网关

NAT 网关（NAT Gateway）是一种支持 IP 地址转换的网络云服务。它能够为腾讯云内的资源提供高性能的 Internet 访问服务。NAT 网关在内外网隔离时，将私有网络（Virtual Private Cloud，VPC）中内网 IP 地址和公网 IP 地址进行转换，实现私有网络访问 Internet 功能。详情请参考 [NAT 网关概述](https://cloud.tencent.com/document/product/552/12951)。

登录私有网络控制台 > [NAT 网关控制台](https://console.cloud.tencent.com/vpc/nat?rid=4)，新建一个 NAT 网关。需注意：

* NAT 网关要和函数、VPC 部署在同一地域。
* NAT 网关的所属网络需要选择函数所在的 VPC。

如下图所示：

![新建NAT网关](https://main.qcloudimg.com/raw/599bdf7444e9183d0d1b441878e75899.png)

## 创建路由策略

通过私有网络控制台左侧进入 [路由表](https://console.cloud.tencent.com/vpc/route?rid=4)，选择路由表所在的地域和 VPC 网络，单击【+新建】创建路由表。
![路由表](https://main.qcloudimg.com/raw/4c040a9412c1fe6e22fee1748c869ed6.png)

### SCF 可以访问外网所有地址

如果想让 SCF 具备所有外网的访问权限，可以在路由表中的目的端配置 IP：0.0.0.0/0，并把路由表关联到新创建好的 NAT 网关和 SCF 的子网，如下图所示：
![创建路由策略](https://main.qcloudimg.com/raw/efda02171e2eeaaa799146b36e36dce1.png)

### SCF 可以访问部分外网地址

把 SCF 需要访问的外网 IP 地址添加到路由表中，并把路由表关联到新创建好的 NAT 网关和 SCF 的子网，如下图所示：
![创建路由策略](https://main.qcloudimg.com/raw/747e594473da15a2319166923f718dda.png)
