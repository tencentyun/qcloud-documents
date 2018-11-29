
## 1. 云硬盘相关接口

| 修改云硬盘属性 | [ModifyCbsStorageAttributes](/doc/api/364/2523) | 修改云硬盘的属性 |
| 查询云硬盘信息 | [DescribeCbsStorages](/doc/api/364/2519) | 根据用户输入的信息，如磁盘类型、可用区等查询对应云硬盘的详细信息 |

## 2. 弹性云盘相关接口

| 接口名 | Action Name | 功能描述 |
| --------- | --------- | ----- |
| 创建弹性云盘 | [CreateCbsStorages](/doc/api/364/2524) | 根据指定的配置购买新的弹性云盘 |
| 挂载弹性云盘 | [AttachCbsStorages](/doc/api/364/2520) | 将指定的弹性云盘挂载到指定的云主机上 |
| 解挂弹性云盘 | [DetachCbsStorages](/doc/api/364/2521) | 将指定的弹性云盘从云主机上解挂 |
| 续费弹性云盘 | [RenewCbsStorage](/doc/api/364/2526) | 对指定的弹性云盘进行续费操作 |
| 扩容弹性云盘 | [ResizeCbsStorage](/doc/api/364/2527) | 对指定的弹性云盘进行扩容操作 |
| 查询弹性云盘价格 | [InquiryStoragePrice](/doc/api/364/2522) | 查询指定类型的弹性云盘的价格 |
| 查询云主机已挂载弹性云盘数量 | [DescribeInstancesCbsNum](/doc/api/364/2528) | 查询云主机已挂载的弹性云盘数量 |

## 3. 快照相关接口

| 接口名称 | Action Name | 功能描述 | 
| -------- | --------- | ------ |
| 创建快照 | [CreateSnapshot](/doc/api/364/2529) | 对指定的云硬盘创建快照 |
| 查询快照列表 | [DescribeSnapshots](/doc/api/364/2530) | 根据指定的参数，如云硬盘ID、类型等查询对应的快照详细信息 |
| 修改快照名称 | [ModifySnapshot](/doc/api/364/2532) | 修改指定快照的展示名称 |
| 回滚快照 | [ApplySnapshot](/doc/api/364/2533) | 回滚快照到原云硬盘 |
| 删除快照 | [DeleteSnapshot](/doc/api/364/2531) | 删除指定的快照 |


