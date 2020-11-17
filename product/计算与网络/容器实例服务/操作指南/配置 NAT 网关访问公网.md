## 概述
CIS 实例支持配置 [ NAT 网关](https://cloud.tencent.com/document/product/215/4975) 和 [路由表](https://cloud.tencent.com/document/product/215/4954) ，实现与 Internet 上的资源互访。

## 配置 Internet 访问 CIS 实例
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/nat)，进入左侧导航 **NAT网关** 控制台，单击【新建】，创建与 CIS 实例同地域、同 VPC 的 NAT 网关。
![][1]
2. NAT网关创建完成后，单击新建 NAT 网关的 **ID/名称**，进入详情页。单击【端口转发】>【新建】开始创建端口转发规则。
配置规则：
 - 外部 IP 端口：选择 NAT 网关的外网 IP 和期望访问的端口；
 - 内部 IP 端口：选择期望访问的 CIS 实例的内网 IP 和占用端口。
![][2]
3. 完成配置后，即可通过 NAT 网关的外网 IP 和端口访问对应 CIS 实例提供的服务。

## 配置 CIS 实例访问 Internet
<a id="step1"></a>
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/nat)，进入左侧导航 **NAT网关** 控制台，单击【新建】，创建与 CIS 实例同地域、同 VPC 的 NAT 网关。
![][1]

2. 进入左侧导航 **路由表** 控制条，单击【新建】，弹出新建路由表窗口，开始创建与 CIS 实例同地域、同 VPC 的路由表。
![][3]

3. 填写路由表名称、选择所属网络，配置路由策略。
路由策略配置规则：
 - 目的端：选择要访问的外网 IP 地址，支持配置 CIDR，例如填写 0.0.0.0/0 会转发所有流量到 NAT 网关。
 - 下一跳类型：选择 【 NAT 网关】类型。
 - 下一跳：选择 <a href="#step1">第1步</a> 创建的 NAT 网关。
![][4]

4. 完成配置路由后，同 VPC 的 CIS 实例即可通过 NAT 网关的外网 IP 访问 Internet。

[1]:https://main.qcloudimg.com/raw/20cb03ac219ea914ebcc50a9ea36d354.png
[2]:https://main.qcloudimg.com/raw/e7827f278e950527847f34a5e77275e4.png
[3]:https://main.qcloudimg.com/raw/1ebcee1dce974c6b0d459c0d7762c1fd.png
[4]:https://main.qcloudimg.com/raw/9baf3c5e5b42da47a0385db55baf27f0.png
