云服务器（Cloud Virtual Machine，CVM）为您提供安全可靠的弹性计算服务。 只需几分钟，您就可以在云端获取和启用 CVM，用于实现您的计算需求。随着业务需求的变化，您可以实时扩展或缩减计算资源。CVM 支持按实际使用的资源计费，可以为您节约计算成本。使用 CVM 可以极大降低您的软硬件采购成本，简化 IT 运维工作。

下表为云审计支持的云服务器操作列表：

| 操作名称                         | 资源类型 | 事件名称                                     |
|------------------------------|------|------------------------------------------|
| 更换公网 IP                       | cvm  | AdjustPublicAddress                      |
| 申请 EIPV3                      | cvm  | AllocateAddresses                        |
| 创建 CDH 实例                      | cvm  | AllocateHosts                            |
| 回滚云硬盘快照                      | cvm  | ApplySnapshot                            |
| 绑定 EIPV3                      | cvm  | AssociateAddress                         |
| 绑定密钥 V3                       | cvm  | AssociateInstancesKeyPairs               |
| 实例关联安全组 V3                    | cvm  | AssociateSecurityGroups                  |
| 挂载云盘                         | cvm  | AttachCbsStorages                        |
| 绑定自动快照策略                     | cvm  | BindAutoSnapshotPolicy                   |
| 服务冷迁移实例                      | cvm  | ColdMigrateInstance                      |
| 创建自动快照策略                     | cvm  | CreateAutoSnapshotPolicy                 |
| 购买云盘                         | cvm  | CreateCbsStorages                        |
| 创建镜像 V3                       | cvm  | CreateImage                              |
| 创建密钥 V3                       | cvm  | CreateKeyPair                            |
| 创建安全组                        | cvm  | CreateSecurityGroup                      |
| 创建安全组规则                      | cvm  | CreateSecurityGroupPolicy                |
| 创建云硬盘快照                      | cvm  | CreateSnapshot                           |
| 删除自动快照策略                     | cvm  | DeleteAutoSnapshotPolicies               |
| 删除用户云盘安全配置                   | cvm  | DeleteDiskSecurityConfigurations         |
| 删除镜像 V3                       | cvm  | DeleteImages                             |
| 删除密钥 V3                       | cvm  | DeleteKeyPairs                           |
| 删除安全组                        | cvm  | DeleteSecurityGroup                      |
| 删除安全组规则                      | cvm  | DeleteSecurityGroupPolicy                |
| 删除云硬盘快照                      | cvm  | DeleteSnapshot                           |
| 查询 EIPV3                      | cvm  | DescribeAddresses                        |
| 查询块存储                        | cvm  | DescribeAllBlockStorages                 |
| 查看自动快照策略                     | cvm  | DescribeAutoSnapshotPolicies             |
| 查询绑定的自动快照策略                  | cvm  | DescribeCbsAssociatedAsp                 |
| 查询云盘                         | cvm  | DescribeCbsStorages                      |
| 查询用户云盘安全配置                   | cvm  | DescribeDiskSecurityConfigurations       |
| 查询独立母机 V3                     | cvm  | DescribeHosts                            |
| 查询镜像 V3                       | cvm  | DescribeImages                           |
| 查询镜像分享 V3                     | cvm  | DescribeImageSharePermission             |
| 查询实例带宽配置                     | cvm  | DescribeInstanceInternetBandwidthConfigs |
| 查询实例属性                       | cvm  | DescribeInstancesAttribute               |
| 查看 cvm 可挂载云盘数量                 | cvm  | DescribeInstancesCbsNum                  |
| 查看实例操作限制列表                   | cvm  | DescribeInstancesDeniedActions           |
| 查询机器能否退还                     | cvm  | DescribeInstancesReturnable              |
| 查询实例状态 V3                     | cvm  | DescribeInstancesStatus                  |
| 查询实例管理终端地址                   | cvm  | DescribeInstanceVncUrl                   |
| 查询密钥列表 V3                     | cvm  | DescribeKeyPairs                         |
| 查询安全组绑定资源数                   | cvm  | DescribeSecurityGroupAssociateInstances  |
| 查询安全组列表                      | cvm  | DescribeSecurityGroupEx                  |
| 查询安全组配额                      | cvm  | DescribeSecurityGroupLimits              |
| 查询安全组规则                      | cvm  | DescribeSecurityGroupPolicy              |
| DescribeSecurityGroupPolicys | cvm  | DescribeSecurityGroupPolicys             |
| 查询安全组                        | cvm  | DescribeSecurityGroups                   |
| 查询云硬盘快照                      | cvm  | DescribeSnapshots                        |
| 卸载云盘                         | cvm  | DetachCbsStorages                        |
| 解绑 EIPV3                      | cvm  | DisassociateAddress                      |
| 解绑密钥 V3                       | cvm  | DisassociateInstancesKeyPairs            |
| 实例解关联安全组 V3                   | cvm  | DisassociateSecurityGroups               |
| 救援模式                         | cvm  | EnterRescueMode                          |
| 退出服务热迁移                      | cvm  | ExitLiveMigrateInstance                  |
| 退出救援模式                       | cvm  | ExitRescueMode                           |
| 服务迁移数据盘                      | cvm  | ImportCbs                                |
| 导入密钥 V3                       | cvm  | ImportKeyPair                            |
| 查询云硬盘快照价格                    | cvm  | InquirySnapshotPrice                     |
| 查询云盘价格                       | cvm  | InquiryStoragePrice                      |
| 服务热迁移实例                      | cvm  | LiveMigrateInstance                      |
| 修改 EIPV3                      | cvm  | ModifyAddressAttribute                   |
| 调整 EIP 带宽 V3                    | cvm  | ModifyAddressesBandwidth                 |
| 修改自动快照策略                     | cvm  | ModifyAutoSnapshotPolicy                 |
| 设置云硬盘自动续费标记                  | cvm  | ModifyCbsRenewFlag                       |
| 修改云盘属性                       | cvm  | ModifyCbsStorageAttributes               |
| 修改用户云盘安全配置                   | cvm  | ModifyDiskSecurityConfigurations         |
| 修改 CDH 实例的属性                   | cvm  | ModifyHostsAttribute                     |
| 修改镜像 V3                       | cvm  | ModifyImageAttribute                     |
| 设置镜像分享 V3                     | cvm  | ModifyImageSharePermission               |
| 切换网络计费模式                     | cvm  | ModifyInstanceInternetChargeType         |
| 修改实例属性                       | cvm  | ModifyInstancesAttribute                 |
| 修改实例项目                       | cvm  | ModifyInstancesProject                   |
| 修改实例续费标识                     | cvm  | ModifyInstancesRenewFlag                 |
| 修改密钥 V3                       | cvm  | ModifyKeyPairAttribute                   |
| 修改安全组属性                      | cvm  | ModifySecurityGroupAttributes            |
| 修改安全组规则                      | cvm  | ModifySecurityGroupPolicys               |
| 编辑单条安全组规则                    | cvm  | ModifySingleSecurityGroupPolicy          |
| 修改云硬盘快照属性                    | cvm  | ModifySnapshot                           |
| 销毁云服务器 V3                      | cvm  | PurgeInstances                           |
| 重启云服务器 V3                      | cvm  | RebootInstances                          |
| 释放 EIPV3                      | cvm  | ReleaseAddresses                         |
| 续费云盘                         | cvm  | RenewCbsStorage                          |
| 续费 CDH 实例                      | cvm  | RenewHosts                               |
| 续费云服务器                        | cvm  | RenewInstances                           |
| 重装云服务器 V3                      | cvm  | ResetInstance                            |
| 调整实例带宽上限 V3                   | cvm  | ResetInstancesInternetMaxBandwidth       |
| 修改实例密码 V3                     | cvm  | ResetInstancesPassword                   |
| 调整子机配置 V3                     | cvm  | ResetInstancesType                       |
| 扩容云盘                         | cvm  | ResizeCbsStorage                         |
| 扩容子机数据盘 V3                    | cvm  | ResizeInstanceDisks                      |
| 创建云服务器 V3                      | cvm  | RunInstances                             |
| 启动云服务器 V3                      | cvm  | StartInstances                           |
| 关闭云服务器 V3                      | cvm  | StopInstances                            |
| 同步镜像 V3                       | cvm  | SyncImages                               |
| 销毁云硬盘                        | cvm  | TerminateCbsStorages                     |
| 删除云服务器 V3                      | cvm  | TerminateInstances                       |
| 解绑自动快照策略                     | cvm  | UnbindAutoSnapshotPolicy                 |
