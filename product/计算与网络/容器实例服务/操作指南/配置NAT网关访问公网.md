## 概述

CIS 实例支持配置[ NAT 网关](https://cloud.tencent.com/document/product/215/4975)和 [路由表](https://cloud.tencent.com/document/product/215/4954)与 Internet 上的资源互访。

## 配置 Internet 访问 CIS 实例

1. 登录 [腾讯云私有网络- NAT 网关](https://console.cloud.tencent.com/vpc/nat) 控制台，单击【新建】创建与 CIS 实例同地域、同 VPC 的 NAT 网关。

2. 在 NAT 网关详情页新建【端口转发】规则。

   ![][1]

3. 配置规则：

   外部 IP 端口：选择 NAT 网关的外网 IP 和期望访问的端口；

   内部 IP 端口：选择期望访问的 CIS 实例的内网 IP 和占用端口；

    ![][2]

4. 完成配置后，即可以通过 NAT 网关的外网 IP 和端口访问对应 CIS 实例提供的服务。

## 配置 CIS 实例访问 Internet

1. 登录 [腾讯云私有网络- NAT 网关](https://console.cloud.tencent.com/vpc/nat) 控制台，单击【新建】创建与 CIS 实例同地域、同 VPC 的 NAT 网关。

2. 登录 [腾讯云私有网络-路由表](https://console.cloud.tencent.com/vpc/route) 控制台，单击【新建】创建与 CIS 实例同地域、同 VPC 的路由表。

   ![][3]

3. 配置路由策略：

    目的端：选择要访问的外网 IP 地址，支持配置 CIDR，例如填写 0.0.0.0/0 会转发所有流量到 NAT 网关；

    下一跳类型：选择 【 NAT 网关】类型；

    下一跳：选择第一步创建的 NAT 网关；

     ![][4]

4. 完成配置路由后，同 VPC 的 CIS 实例即可以通过 NAT 网关的外网 IP 访问 Internet。

[1]:https://main.qcloudimg.com/raw/20cb03ac219ea914ebcc50a9ea36d354.png
[2]:https://main.qcloudimg.com/raw/d0ec9fd815138165e51037141e742dd8.png
[3]:https://main.qcloudimg.com/raw/1ebcee1dce974c6b0d459c0d7762c1fd.png
[4]:https://main.qcloudimg.com/raw/9baf3c5e5b42da47a0385db55baf27f0.png
