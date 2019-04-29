## 专用宿主机相关接口

| 接口名称                                        | 接口功能          |
| ----------------------------------------------- | ----------------- |
| [AllocateHosts](/document/api/213/16473)        | 创建CDH实例       |
| [DescribeHosts](/document/api/213/16474)        | 查看CDH实例列表   |
| [ModifyHostsAttribute](/document/api/213/16475) | 修改CDH实例的属性 |
| [RenewHosts](/document/api/213/16476)           | 续费CDH实例       |

## 地域相关接口

| 接口名称                                   | 接口功能       |
| ------------------------------------------ | -------------- |
| [DescribeRegions](/document/api/213/15708) | 查询地域列表   |
| [DescribeZones](/document/api/213/15707)   | 查询可用区列表 |

## 实例相关接口

| 接口名称                                                     | 接口功能                   |
| ------------------------------------------------------------ | -------------------------- |
| [DescribeInstanceFamilyConfigs](/document/api/213/15748)     | 查询所支持的实例机型族信息 |
| [DescribeInstanceInternetBandwidthConfigs](/document/api/213/15734) | 查询实例带宽配置           |
| [DescribeInstanceOperationLogs](/document/api/213/15737)     | 查询实例操作记录           |
| [DescribeInstanceTypeConfigs](/document/api/213/15749)       | 查询实例机型列表           |
| [DescribeInstances](/document/api/213/15728)                 | 查看实例列表               |
| [DescribeInstancesStatus](/document/api/213/15738)           | 查看实例状态列表           |
| [DescribeInternetChargeTypeConfigs](/document/api/213/15729) | 查询网络计费类型           |
| [InquiryPriceRenewInstances](/document/api/213/15725)        | 续费实例询价               |
| [InquiryPriceResetInstance](/document/api/213/15747)         | 重装实例询价               |
| [InquiryPriceResetInstancesInternetMaxBandwidth](/document/api/213/15732) | 调整实例带宽上限询价       |
| [InquiryPriceResetInstancesType](/document/api/213/15733)    | 调整实例配置询价           |
| [InquiryPriceResizeInstanceDisks](/document/api/213/15751)   | 扩容实例磁盘询价           |
| [InquiryPriceRunInstances](/document/api/213/15726)          | 创建实例询价               |
| [ModifyInstancesAttribute](/document/api/213/15739)          | 修改实例的属性             |
| [ModifyInstancesProject](/document/api/213/15746)            | 修改实例所属项目           |
| [ModifyInstancesRenewFlag](/document/api/213/15752)          | 修改实例续费标识           |
| [QueryMigrateTask](/document/api/213/15722)                  | 查询迁移任务进度           |
| [RebootInstances](/document/api/213/15742)                   | 重启实例                   |
| [RenewInstances](/document/api/213/15740)                    | 续费实例                   |
| [ResetInstance](/document/api/213/15724)                     | 重装实例                   |
| [ResetInstancesInternetMaxBandwidth](/document/api/213/15721) | 调整实例带宽上限           |
| [ResetInstancesPassword](/document/api/213/15736)            | 重置实例密码               |
| [ResetInstancesType](/document/api/213/15744)                | 调整实例配置               |
| [ResizeInstanceDisks](/document/api/213/15731)               | 扩容实例磁盘               |
| [RunInstances](/document/api/213/15730)                      | 创建实例                   |
| [StartInstances](/document/api/213/15735)                    | 启动实例                   |
| [StopInstances](/document/api/213/15743)                     | 关闭实例                   |
| [TerminateInstances](/document/api/213/15723)                | 退还实例                   |
| [UpdateInstanceVpcConfig](/document/api/213/15750)           | 修改实例vpc属性            |

## 密钥相关接口

| 接口名称                                                 | 接口功能       |
| -------------------------------------------------------- | -------------- |
| [AssociateInstancesKeyPairs](/document/api/213/15698)    | 绑定密钥对     |
| [CreateKeyPair](/document/api/213/15702)                 | 创建密钥对     |
| [DeleteKeyPairs](/document/api/213/15700)                | 删除密钥对     |
| [DescribeKeyPairs](/document/api/213/15699)              | 查询密钥对列表 |
| [DisassociateInstancesKeyPairs](/document/api/213/15697) | 解绑密钥对     |
| [ImportKeyPair](/document/api/213/15703)                 | 导入密钥对     |
| [ModifyKeyPairAttribute](/document/api/213/15701)        | 修改密钥对属性 |

## 镜像相关接口

| 接口名称                                                | 接口功能                     |
| ------------------------------------------------------- | ---------------------------- |
| [CreateImage](/document/api/213/16726)                  | 创建镜像                     |
| [DeleteImages](/document/api/213/15716)                 | 删除镜像                     |
| [DescribeImageQuota](/document/api/213/15719)           | 查询镜像配额上限             |
| [DescribeImageSharePermission](/document/api/213/15712) | 查看镜像分享信息             |
| [DescribeImages](/document/api/213/15715)               | 查看镜像列表                 |
| [DescribeImportImageOs](/document/api/213/15718)        | 查询外部导入镜像支持的OS列表 |
| [ImportImage](/document/api/213/15717)                  | 外部镜像导入                 |
| [ModifyImageAttribute](/document/api/213/15713)         | 修改镜像属性                 |
| [ModifyImageSharePermission](/document/api/213/15710)   | 修改镜像分享信息             |
| [SyncImages](/document/api/213/15711)                   | 同步镜像                     |