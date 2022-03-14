## 简介

本文档将会为您介绍存储网关（Cloud Storage Gateway，CSG）相关可授权的资源类型，API 操作以及预设策略。您可以在访问管理（Cloud Access Management，CAM）控制台，使用可视化的操作授予子账号预设的权限策略，如您需要授予子账号更为细致的权限，请参考本文档下方相关产品接口说明以及 [授权策略语法](https://cloud.tencent.com/document/product/581/47926)。

## 预设策略



### CSG 预设策略

CSG 预设授权策略如下：

| 策略                    | 说明                                    |
| ----------------------- | --------------------------------------- |
| QcloudCSGFullAccess     | 拥有操作主账号下 CSG 所有资源的权限     |
| QcloudCSGReadOnlyAccess | 拥有主账号下 CSG 所有资源的只读权限 |

### 其他产品预设策略

CSG 预设策略中不包含腾讯云其他产品的相关权限，通常情况下，您还需要授予其他产品预设策略，才能正常使用存储网关控制台的全部功能，您可以授予子账号以下相关的预设策略：

| 策略                    | 说明                                    |
| ----------------------- | --------------------------------------- |
| QcloudCOSBucketConfigRead | 拥有主账号下 COS 存储桶相关配置的只读权限     |
| QcloudCamReadOnlyAccess | 拥有主账号下 CAM 所有配置的只读权限     |
| QcloudVPCReadOnlyAccess | 拥有主账号下 VPC 所有资源的只读权限 |
| QcloudTAGReadOnlyAccess | 拥有主账号下 TAG 所有配置的只读权限 |
| QcloudTAGFullAccess | 拥有操作主账号下 TAG 所有配置的权限 |

>? 标签 TAG 相关说明请参考 [标签概述](https://cloud.tencent.com/document/product/581/49174)。


## 自定义策略


### 可授权的资源类型

资源级授权指主账号能够授予子账号对特定资源进行特定操作的权限，CSG 绝大部分 API 支持资源级授权。例如，授予子账号拥有主账号广州地域存储网关操作权限，请参考 [授权策略示例](https:///cloud.tencent.com/document/product/581/47927#.E6.8E.88.E6.9D.83.E7.94.A8.E6.88.B7.E6.8B.A5.E6.9C.89.E7.89.B9.E5.AE.9A.E5.9C.B0.E5.9F.9F-csg-.E7.9A.84.E6.93.8D.E4.BD.9C.E6.9D.83.E9.99.90.E7.AD.96.E7.95.A5)。
在访问管理（Cloud Access Management，CAM）中 CSG 可授权的资源类型如下：

| 资源类型     | 授权策略中的资源描述方法                                     |
| :----------- | ------------------------------------------------------------ |
| 网关实例     | ` qcs::csg:${Region}:uin/${OwnerUin}:gateway/${gatewayid} `  |
| 文件系统实例 | `qcs::csg:${Region}:uin/${OwnerUin}:gateway `<br>`/${gatewayid}/fileshare/${fileshareid} ` |

### 可授权的 CSG API 列表

| **API 操作**                       | **可授权的资源**                                             | **说明**               |
| ---------------------------------- | ------------------------------------------------------------ | ---------------------- |
| csg:ListGateways                   | ` qcs::csg::uin/${OwnerUin}:gateway/* `<br>` qcs::csg:${Region}:uin/${OwnerUin}`<br>`:gateway/${gatewayid} ` | 列出存储网关资源       |
| csg:DescribeCOS<br>GatewayCache    | ` qcs::csg::uin/${OwnerUin}:gateway/* `<br>` qcs::csg:${Region}:uin/${OwnerUin}`<br>`:gateway/${gatewayid} ` | 查看存储网关缓存状态   |
| csg:StartGateway                   | ` qcs::csg::uin/${OwnerUin}:gateway/* `<br>` qcs::csg:${Region}:uin/${OwnerUin}`<br>`:gateway/${gatewayid} ` | 启动存储网关           |
| csg:Shutdown<br>Gateway            | ` qcs::csg::uin/${OwnerUin}:gateway/* `<br>` qcs::csg:${Region}:uin/${OwnerUin}`<br>`:gateway/${gatewayid} ` | 停止存储网关           |
| csg:Terminate<br>Gateway           | ` qcs::csg::uin/${OwnerUin}:gateway/* `<br>` qcs::csg:${Region}:uin/${OwnerUin}`<br>`:gateway/${gatewayid} ` | 删除存储网关           |
| csg:Describe<br>GatewayInformation | ` qcs::csg::uin/${OwnerUin}:gateway/* `<br>` qcs::csg:${Region}:uin/${OwnerUin}`<br>`:gateway/${gatewayid} ` | 查看存储网关详情       |
| csg:Update<br>GatewayInformation   | ` qcs::csg::uin/${OwnerUin}:gateway/* `<br>` qcs::csg:${Region}:uin/${OwnerUin}`<br>`:gateway/${gatewayid} ` | 更新存储网关基础配置   |
| csg:Describe<br>BandwidthRateLimit | ` qcs::csg::uin/${OwnerUin}:gateway/* `<br>` qcs::csg:${Region}:uin/${OwnerUin}`<br>`:gateway/${gatewayid} ` | 查看存储网关带宽限制   |
| csg:UpdateBand<br>widthRateLimit   | ` qcs::csg::uin/${OwnerUin}:gateway/* `<br>` qcs::csg:${Region}:uin/${OwnerUin}`<br>`:gateway/${gatewayid} ` | 修改存储网关带宽限制   |
| csg:ListLocalDisks                 | ` qcs::csg::uin/${OwnerUin}:gateway/* `<br>` qcs::csg:${Region}:uin/${OwnerUin}`<br>`:gateway/${gatewayid} ` | 列出存储网关已挂载磁盘 |
| csg:AddCache                       | ` qcs::csg::uin/${OwnerUin}:gateway/* `<br>` qcs::csg:${Region}:uin/${OwnerUin}`<br>`:gateway/${gatewayid} ` | 给存储网关挂载新磁盘   |
| csg:CreateCOS<br>FileShare         | ` qcs::csg::uin/${OwnerUin}:gateway/* `<br>` qcs::csg:${Region}:uin/${OwnerUin}`<br>`:gateway/${gatewayid} ` | 创建文件系统           |
| csg:ListFileShares                 | ` qcs::csg::uin/${OwnerUin}:gateway/* `<br>` qcs::csg:${Region}:uin/${OwnerUin}`<br>`:gateway/${gatewayid}/fileshare/* `<br>` qcs::csg:${Region}:uin/${OwnerUin}`<br>`:gateway/${gatewayid}/fileshare/${fileshareid}` | 列出文件系统           |
| csg:DescribeCOS<br>FileShare       | ` qcs::csg::uin/${OwnerUin}:gateway/* `<br>` qcs::csg:${Region}:uin/${OwnerUin}`<br>`:gateway/${gatewayid}/fileshare/* `<br>` qcs::csg:${Region}:uin/${OwnerUin}`<br>`:gateway/${gatewayid}/fileshare/${fileshareid}` | 查看文件系统详情       |
| csg:DeleteFileShare                | ` qcs::csg::uin/${OwnerUin}:gateway/* `<br>` qcs::csg:${Region}:uin/${OwnerUin}`<br>`:gateway/${gatewayid}/fileshare/* `<br>` qcs::csg:${Region}:uin/${OwnerUin}`<br>`:gateway/${gatewayid}/fileshare/${fileshareid}` | 删除文件系统           |
| csg:UpdateCOS<br>FileShare         | ` qcs::csg::uin/${OwnerUin}:gateway/* `<br>` qcs::csg:${Region}:uin/${OwnerUin}`<br>`:gateway/${gatewayid}/fileshare/* `<br>` qcs::csg:${Region}:uin/${OwnerUin}`<br>`:gateway/${gatewayid}/fileshare/${fileshareid}` | 更新文件系统配置       |


### 可授权的其他产品权限

为了正常使用存储网关控制台服务，您需要授予子账号其他产品的相关接口权限，具体权限如下：

| API 操作           | 说明                                                         |
| ------------------ | ------------------------------------------------------------ |
| cam:ListAttachedRolePolicie         | 使用存储网关服务，需要确认子账户对应主账户是否授予了存储网关服务角色相关权限 |
| cos:GetService         | 创建文件系统的时候，CSG 控制台需要通过该接口拉取对应地域的存储桶列表 |
| cos:GetBucketLifecycle | 文件系统详情页通过该接口拉取对应存储桶的生命周期配置信息     |
| vpc:DescribeVpcEx      | 购买网关时，购买页需要通过该接口拉取用户的 VPC 列表          |
| vpc:DescribeSubnetEx   | 购买网关时，购买页需要通过该接口拉取用户对应 VPC 下的子网列表 |
| tag:DescribeResourceTags   | 拉取资源的标签 |
| tag:DescribeResourceTagsByResourceIds   | 根据资源 ID 拉取相关标签 |
| tag:DescribeTagKeys   | 拉取标签键 |
| tag:DescribeTagValues   | 拉取标签值 |
| tag:ModifyResourceTags   | 修改标签 |


>? 由于 VPC 在 CAM 配置的策略接口和实际调用的接口存在差异，即若您未授予 DescribeVpcEx 购买页权限会提示无 DescribeVpcs 权限，同理，若您未授予 DescribeSubnetEx 购买页权限会提示无 DescribeSubnets 权限；如需相关产品更为详细的访问管理说明，请参照 COS 的 [访问控制基本概念](https://cloud.tencent.com/document/product/436/30749) 以及 VPC 的 [访问管理概述](https://cloud.tencent.com/document/product/215/39265)。

