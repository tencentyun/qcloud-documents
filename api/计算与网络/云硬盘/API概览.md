## 1. 云硬盘相关接口

| 接口名 | Action Name | 功能描述 |
| --------- | --------- | ----- |
| [修改云硬盘属性](/doc/api/364/2523) | ModifyCbsStorageAttributes | 修改云硬盘的属性 |
| [查询云硬盘信息](/doc/api/364/2519) | DescribeCbsStorages | 根据用户输入的信息，如磁盘类型、可用区等查询对应云硬盘的详细信息 |

## 2. 弹性云盘相关接口

| 接口名 | Action Name | 功能描述 |
| --------- | --------- | ----- |
| [创建弹性云盘](/doc/api/364/2524) | CreateCbsStorages | 根据指定的配置购买新的弹性云盘 |
| [挂载弹性云盘](/doc/api/364/2520)  | AttachCbsStorages| 将指定的弹性云盘挂载到指定的云服务器上 |
| [解挂弹性云盘](/doc/api/364/2521) | DetachCbsStorages | 将指定的弹性云盘从云服务器上解挂 |
| [续费弹性云盘](/doc/api/364/2526) | RenewCbsStorage | 对指定的弹性云盘进行续费操作 |
| [扩容弹性云盘](/doc/api/364/2527) | ResizeCbsStorage | 对指定的弹性云盘进行扩容操作 |
| [查询弹性云盘价格](/doc/api/364/2522) | InquiryStoragePrice | 查询指定类型的弹性云盘的价格 |
| [查询云服务器已挂载弹性云盘数量](/doc/api/364/2528)  | DescribeInstancesCbsNum | 查询云服务器已挂载的弹性云盘数量 |

## 3. 快照相关接口

| 接口名称 | Action Name | 功能描述 | 
| -------- | --------- | ------ |
| [创建快照](/doc/api/364/2529) | CreateSnapshot | 对指定的云硬盘创建快照 |
| [查询快照列表](/doc/api/364/2530) | DescribeSnapshots | 根据指定的参数，如云硬盘ID、类型等查询对应的快照详细信息 |
| [修改快照名称](/doc/api/364/2532) | ModifySnapshot | 修改指定快照的展示名称 |
| [回滚快照](/doc/api/364/2533) | ApplySnapshot | 回滚快照到原云硬盘 |
| [删除快照](/doc/api/364/2531) | DeleteSnapshot | 删除指定的快照 |
| [查询快照价格]() | InquirySnapshotPrice | 查询对指定大小指定类型指定时长的云硬盘创建快照所需费用 |

## 4. 定期快照相关接口

| 接口名称 | Action Name | 功能描述 | 
| -------- | --------- | ------ |
| [创建定期快照策略]() | CreateAutoSnapshotPolicy | 创建一个定期快照策略 |
| [查询定期快照策略]() | DescribeAutoSnapshotPolicies | 查询定期快照策略详细信息 |
| [修改定期快照策略]() | ModifyAutoSnapshotPolicy | 修改定期快照策略 |
| [绑定定期快照策略]() | BindAutoSnapshotPolicy | 将云硬盘绑定到定期快照策略 |
| [解绑定期快照策略]() | UnbindAutoSnapshotPolicy | 将云硬盘从定期快照策略解绑 |
| [删除定期快照策略]() | DeleteAutoSnapshotPolicies | 删除指定的定期快照策略 |
| [查询云硬盘关联定期快照策略]() | DescribeCbsAssociatedAsp | 查询云硬盘关联的定期快照策略 |
