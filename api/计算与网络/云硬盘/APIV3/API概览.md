
## 1. 云硬盘相关接口
| 接口功能 | Action ID | 功能描述
|---------|---------|---------|
| 修改云硬盘属性 | [ModifyDiskAttributes](/document/product/362/13165) |  用于修改云硬盘属性。
| 查询云盘列表 | [DescribeDisks](/document/product/362/13172) |  根据指定的参数，如云盘ID、云盘类型或者云盘状态等信息来查询云盘的详细信息。

## 2. 弹性云盘相关接口
| 接口功能 | Action ID | 功能描述
|---------|---------|---------|
| 创建弹性云盘 | [CreateDisks](/document/product/362/13166) | 根据指定的配置购买新的弹性云盘。
| 挂载弹性云盘 | [AttachDisks](/document/product/362/13170) | 将指定的弹性云盘挂载到指定的云主机上。
| 解挂弹性云盘 | [DetachDisks](/document/product/362/13175) | 将指定的弹性云盘从云主机上解挂。
| 续费弹性云盘 | [RenewDisk](/document/product/362/13173) | 对指定的弹性云盘进行续费操作。
| 扩容弹性云盘 | [ResizeDisk](/document/product/362/13168) | 对指定的弹性云盘进行扩容操作。
| 创建弹性云盘询价 | [InquiryPriceCreateDisk](/document/product/362/13167) | 查询新购弹性云盘的价格。
| 续费弹性云盘询价 | [InquiryPriceRenewDisk](/document/product/362/13174) | 查询续费弹性云盘的价格。
| 扩容弹性云盘询价 | [InquiryPriceResizeDisk](/document/product/362/13169) | 查询扩容弹性云盘的价格。
| 查询云主机已挂载弹性云盘数量 | [DescribeInstancesDiskNum](/document/product/362/13171) | 查询云主机已挂载的弹性云盘数量。

## 3. 快照相关接口
| 接口功能 | Action ID | 功能描述
|---------|---------|---------|
| 创建快照 | [CreateSnapshot](/document/product/362/13177)|  对指定的云硬盘创建快照。
| 查询快照列表 | [DescribeSnapshots](/document/product/362/13180)|  根据指定的参数，如快照ID、创建快照的云硬盘ID、创建快照的云硬盘类型等信息来查询快照的详细信息。
| 修改快照属性 | [ModifySnapshotAttribute](/document/product/362/13178)|  修改指定快照的属性。
| 回滚快照 | [ApplySnapshot](/document/product/362/13179)|  回滚快照到原云硬盘。
| 删除快照 | [DeleteSnapshots](/document/product/362/13178)|  删除指定的快照。
