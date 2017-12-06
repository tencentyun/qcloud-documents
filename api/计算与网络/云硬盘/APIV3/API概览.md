
## 1. 云硬盘相关接口
| 接口功能 | Action ID | 功能描述
|---------|---------|---------|
| 修改云硬盘属性 | [ModifyDiskAttributes](/document/api/213/9388) |  用于修改云硬盘属性。
| 查询云盘列表 | [DescribeDisks](/document/api/213/9388) |  根据指定的参数，如云盘ID、云盘类型或者云盘状态等信息来查询云盘的详细信息。

## 2. 弹性云盘相关接口
| 接口功能 | Action ID | 功能描述
|---------|---------|---------|
| 创建弹性云盘 | [CreateDisks](/document/api/213/9418) | 根据指定的配置购买新的弹性云盘。
| 挂载弹性云盘 | [AttachDisks](/document/api/213/9418) | 将指定的弹性云盘挂载到指定的云主机上。
| 解挂弹性云盘 | [DetachDisks](/document/api/213/9418) | 将指定的弹性云盘从云主机上解挂。
| 续费弹性云盘 | [RenewDisk](/document/api/213/9418) | 对指定的弹性云盘进行续费操作。
| 扩容弹性云盘 | [ResizeDisk](/document/api/213/9418) | 对指定的弹性云盘进行续费操作。
| 新购弹性云盘询价 | [InquiryPriceCreateDisk](/document/api/213/9418) | 查询新购弹性云盘的价格。
| 新购弹性云盘询价 | [InquiryPriceRenewDisk](/document/api/213/9418) | 查询续费弹性云盘的价格。
| 扩容弹性云盘询价 | [InquiryPriceResizeDisk](/document/api/213/9418) | 查询扩容弹性云盘的价格。
| 扩容弹性云盘询价 | [DescribeInstancesDiskNum](/document/api/213/9418) | 查询云主机已挂载的弹性云盘数量。

## 3. 快照相关接口
| 接口功能 | Action ID | 功能描述
|---------|---------|---------|
| 创建快照 | [CreateSnapshot](/document/api/213/8836)|  对指定的云硬盘创建快照。
| 查询快照列表 | [DescribeSnapshots](/document/api/213/8836)|  根据指定的参数，如快照ID、创建快照的云硬盘ID、创建快照的云硬盘类型等信息来查询快照的详细信息。
| 修改快照属性 | [ModifySnapshotAttribute](/document/api/213/8836)|  修改指定快照的展示名称。
| 删除快照 | [DeleteSnapshots](/document/api/213/8836)|  删除指定的快照。

## 4. 定期快照策略相关接口
| 接口功能 | Action ID | 功能描述
|---------|---------|---------|
| 创建定期快照策略 | [CreateAutoSnapshotPolicy](/document/api/213/8836)|  创建一个定期快照策略。
| 查询定期快照策略 | [DescribeAutoSnapshotPolicies](/document/api/213/8836)|  查询定期快照策略详细信息。
| 修改定期快照策略 | [ModifyAutoSnapshotPolicyAttribute](/document/api/213/8836)|  修改指定定期快照策略的属性。
| 绑定定期快照策略 | [BindAutoSnapshotPolicy](/document/api/213/8836)|  将云硬盘绑定到定期快照策略。
| 解绑定期快照策略 | [UnbindAutoSnapshotPolicy](/document/api/213/8836)|  将云硬盘从定期快照策略解绑。
| 删除定期快照策略 | [DeleteAutoSnapshotPolicies](/document/api/213/8836)|  删除指定的定期快照策略。
| 查询云硬盘绑定的定期快照策略 | [DescribeDiskAssociatedAutoSnapshotPolicy](/document/api/213/8836)|  查询云硬盘关联的定期快照策略。