本文指导您在本地数据中心完成CDC专用集群部署后，如何快速配置CDC网络并使用CDC资源实例进行业务通信。

## 前提条件
[已在本地数据中心机房配置了CDC专用集群](https://cloud.tencent.com/document/product/1346/49917)

## 操作指导
1. 登录CDC集群控制台。
2. 单击创建CDC子网，在弹出的对话框中选择您本地机房已部署的CDC集群，以及主Region需要关联的VPC，填写子网名称，CIDR，就近选择可用区，选择默认路由表即可，如果创建多个子网请单击【添加子网】。
    ![](https://main.qcloudimg.com/raw/83e0220c2931ff390e1636bc006c7998.png)

3. 完成CDC子网配置后，单击【创建】完成操作。
4. 单击【CDC本地网关】，在本地网关界面，选择本地网关需要关联的VPC，单击【确定】。
![](https://main.qcloudimg.com/raw/8850a1ea9d451b488f445f9bc2b99d19.png)
5. 如需与本地IDC通信，可配置到本地网关的路由策略。CDC默认关联VPC默认路由表，可在默认路由表中增加路由策略，也可以创建自定义路由表并增加路由策略。
   1. 登录路由表控制台。
   2. 选择CDC子网关联的路由表，并单击路由表ID进入路由表详情界面。
   3. 单击【新增路由】，目的端配置为IDC内网网段，下一跳类型选择CDC本地网关，下一跳选择步骤3中已创建的CDC本地网关ID，单击【创建】完成路由策略的配置。
   4. 您也可以创建自定义路由表，并新增路由策略，完成路由策略配置后，关联至CDC子网。
       ![](https://main.qcloudimg.com/raw/e9d9d8f76c36faf78d1c78998d803a05.png)
6. CDC子网及子网中的云资源支持网络ACL和安全组，规则使用及配置与普通子网及云服务器无差异，具体操作请参考 [网络 ACL](https://cloud.tencent.com/document/product/215/20160) 和 [安全组](https://cloud.tencent.com/document/product/215/37888)。
7. CDC支持网络流日志，具体使用与公有云无差异，请参考 [网络流日志](https://cloud.tencent.com/document/product/682/18935)。

## 测试验证
1. 测试从用户IDC网络到CDC子网实例的连接，登录IDC中的服务器，并ping CDC子网中云服务器的IP地址。
2. 测试从CDC子网中实例到用户IDC网络的连接，登录CDC子网中的云服务器，并ping 用户IDC网络中的服务器IP。
3. 测试主Region公有云VPC中实例与CDC子网实例的连接，登录CDC子网中的云服务器，并ping 主Region VPC中其他子网中某云服务器内网IP。

结论：有数据返回表示已联通