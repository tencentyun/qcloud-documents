在使用腾讯云服务网格（Tencnet Cloud Mesh，TCM）的过程中，涉及到服务网格相关云资源的使用，为了您能正常使用 TCM 的功能，您需要对 TCM 的服务角色 `TCM_QCSRole` 进行授权，授权后，TCM 服务才能使用相关云资源。

需要服务授权的场景主要包含 [首次登录 服务网格控制台](#TCMRole) 以及 [首次使用 TCM 一键体验功能](#TCMRoleInSample) 两个场景，分别对应 ` QcloudAccessForTCMRole ` 和 ` QcloudAccessForTCMRoleInSampleDeployment ` 两个预设策略。



## 首次登录服务网格控制台[](id:TCMRole)

### 授权场景

当您已注册并登录腾讯云账号后，首次登录 [服务网格控制台](https://console.cloud.tencent.com/tke2/mesh) 时，需前往**访问管理**页面对当前账号授予腾讯云服务网格操作容器服务（TKE）、SSL证书（SSL）、日志服务（CLS）等云资源的权限。该权限授予通过关联预设策略 ` QcloudAccessForTCMRole ` 至 TCM 服务角色 `TCM_QCSRole` 完成。如您之前未创建过 TCM 服务角色，该授权流程还会涉及 TCM 服务角色的创建。

### 授权步骤

1. 首次登录 [服务网格控制台](https://console.cloud.tencent.com/tke2/mesh)，自动弹出**服务授权**窗口。
![](https://qcloudimg.tencent-cloud.cn/raw/c084fdc252866cbae3b02656c3302316.png)
2. 单击**前往访问管理**，进入 CAM 控制台服务授权页面。
3. 单击**同意授权**，完成身份验证后即可成功授权。
![](https://main.qcloudimg.com/raw/5177ba8f982f5af6099d739adaa24c8e.png)

### 权限内容

**容器服务（TKE）相关**

| 权限 | 描述 | 资源 |
| :-------- | :--------| :------ |
| DescribeClusterSecurity |  查询集群密钥 | 所有资源 `*` |

 **SSL 证书（SSL）相关**

| 权限 | 描述 | 资源 |
| :-------- | :--------| :------ |
| DescribeCertificateDetail | 获取证书详情 | 所有资源 `*` |

 **日志服务（CLS）相关**

| 权限 | 描述 | 资源 |
| :-------- | :--------| :------ |
| getLogset | 获取日志集详情 | 所有资源 ` * ` |
| getTopic | 获取日志主题详情 | 所有资源 ` * ` |
| createLogset | 创建日志集 | 所有资源 ` * ` |
| createTopic | 创建日志主题 | 所有资源 ` * ` |
| modifyIndex | 修改索引 | 所有资源 ` * ` |
| listLogset | 获取日志集列表 | 所有资源 ` * ` |
| listTopic | 获取日志主题列表 | 所有资源 ` * ` |


## 首次使用 TCM 一键体验功能[](id:TCMRoleInSample)

### 授权场景

首次使用 TCM 一键体验功能时，您需要前往**访问管理**对当前账号授予腾讯云服务网格操作私有网络（VPC）、云联网（CCN）、容器服务（TKE）、云服务器（CVM）等云资源以及购买云服务器（CVM）的财务权限。该权限授予通过关联预设策略 ` QcloudAccessForTCMRoleInSampleDeployment ` 至 TCM 服务角色 `TCM_QCSRole` 完成。如您之前未创建过 TCM 服务角色，该授权流程还会涉及 TCM 服务角色的创建。

### 授权步骤

1. 登录 [服务网格控制台](https://console.cloud.tencent.com/tke2/mesh)，鼠标移动至**一键体验**按钮，单击**服务授权**弹出授权提示窗口。
<img src="https://main.qcloudimg.com/raw/9b4d253fb770bb36656495d71c61488b.png" width="70%"><br>
2. 单击**前往访问管理**，进入 CAM 控制台服务授权页面。
![](https://qcloudimg.tencent-cloud.cn/raw/681ebc366acace2f6be549942bb7e0bf.png)
3. 单击**同意授权**，完成身份验证后即可成功授权。
![](https://main.qcloudimg.com/raw/0373980842d048081947d20885555cc5.png)

### 权限内容

 **私有网络（VPC）相关**

| 权限 | 描述 | 资源 |
| :-------- | :--------| :------ |
| CreateSubnet |  创建子网 | 所有资源 ` * ` |
| CreateVpc |  创建私有网络 | 所有资源 ` * ` |
| DeleteVpc |  删除私有网络 | 所有资源 ` * ` |
| DescribeVpcEx | 查询私有网络列表 | 所有资源 ` * ` |
| DescribeSubnetEx | 查看子网列表 | 所有资源 ` * ` |

**云联网（CCN）相关**

| 权限 | 描述 | 资源 |
| :-------- | :--------| :------ |
| AttachCcnInstances |  关联云联网实例 | 所有资源 ` * ` |
| CreateCcn |  创建云联网 | 所有资源 ` * ` |
| DeleteCcn | 删除云联网 | 所有资源 ` * ` |
| DescribeCcnAttachedInstances | 查询云联网关联实例列表 | 所有资源 ` * ` |
| DescribeCcns |  查询云联网列表 | 所有资源 ` * ` |

 **容器服务（TKE）相关**

| 权限 | 描述 | 资源 |
| :-------- | :--------| :------ |
| CreateCluster |  创建集群 | 所有资源 ` * ` |
| CreateClusterEndpointVip |  开启集群访问端口（托管集群外网） | 所有资源 ` * ` |
| DeleteCluster |  删除集群 | 所有资源 ` * ` |
| DeleteClusterEndpoint | 删除集群访问端口 | 所有资源 ` * ` |
| DeleteClusterEndpointVip | 删除集群访问端口（托管集群外网） | 所有资源 ` * ` |
| DescribeClusterEndpointVipStatus | 查询集群开启访问端口状态（托管集群外网）| 所有资源 ` * ` |
| DescribeClusters | 获取集群列表 | 所有资源 ` * ` | 

 **云服务器（CVM）相关**

| 权限 | 描述 | 资源 |
| :-------- | :--------| :------ |
| CreateSecurityGroup | 创建安全组 | 所有资源 ` * ` |
| DeleteSecurityGroup |  删除安全组 | 所有资源 ` * ` |
| DescribeImages |  查询镜像 | 所有资源 ` * ` |
| DescribeInstances | 查询云主机 | 所有资源 ` * ` |
| DescribeSecurityGroups | 查询安全组 | 所有资源 ` * ` |
| ModifySecurityGroupPolicys | 修改安全组规则 | 所有资源 ` * ` |
| RunInstances | 创建云主机 | 所有资源 ` * ` | 

**财务权限**

| 权限 | 描述 | 资源 |
| :-------- | :--------| :------ |
| `finance:*` |  购买云服务器的财务权限 | 云服务器 ` qcs::cvm:::* ` |
