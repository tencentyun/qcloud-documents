VPC CIDR（主）创建后不可修改，当 VPC 的主 CIDR 不满足业务分配时，您可以创建辅助 CIDR 来扩充网段，然后在辅助 CIDR 上创建网络资源以满足实际网络需求。

>?
>- 目前辅助 CIDR 处于内测中，如有需要，请提交 [工单申请](https://console.cloud.tencent.com/workorder/category?level1_id=6&level2_id=168&source=0&data_title=%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9CVPC&step=1)。
>- 辅助 CIDR 可以和自定义路由的目的网段重叠；但需要谨慎操作，因为辅助 CIDR 的路由属于 Local 路由，Local 路由比自定义子网路由优先级更高。
>- 基础网络云服务器不支持和辅助 CIDR 内的云资源互通。
>- 目前仅云联网支持传递辅助 CIDR，即：辅助 CIDR 内的云服务器无法通过对等连接、专线接入和其他 VPC、IDC 通信。

## 创建辅助 CIDR[](id:21)
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc)。
2. 在【私有网络】页面顶部，选择 VPC 所属地域。
3. 在 VPC 列表中目标 VPC 右侧**操作**列选择【更多】>【编辑IPv4 CIDR】。
	![](https://main.qcloudimg.com/raw/18d633a474b1818329fff952542f6bb2.png)
4. 在弹出编辑对话框中单击【添加】，并编辑辅助 CIDR。
<img src="https://main.qcloudimg.com/raw/775126708149064bad3383f873fcc654.png" width="50%" />
5. 单击【确定】完成辅助 CIDR 的创建。

## 删除辅助 CIDR[](id:32)
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc)。
2. 在【私有网络】页面顶部，选择 VPC 所属地域。
3. 在 VPC 列表中，待删除辅助 CIDR 的 VPC 右侧**操作**列选择【更多】>【编辑 IPv4 CIDR】。
4. 在弹出的编辑对话框中，单击辅助 CIDR 后的【删除】。
<img src="https://main.qcloudimg.com/raw/10602971a87c4babc86e2bb400cbc1b7.png" width="50%" />
5. 单击【确定】完成删除操作。
