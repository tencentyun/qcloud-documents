## 创建辅助 CIDR[](id:21)
>?
>- 目前辅助 CIDR 处于内测中，如有需要，请提交 [工单申请](https://console.cloud.tencent.com/workorder/category?level1_id=6&level2_id=168&source=0&data_title=%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9CVPC&step=1)。
>- 辅助 CIDR 可以和自定义路由的目的网段重叠；但需要谨慎操作，因为辅助 CIDR 的路由属于 Local 路由，Local 路由比自定义子网路由优先级更高。
>- 基础网络云服务器不支持和辅助 CIDR 内的云资源互通。
>- 目前仅云联网支持传递辅助 CIDR，即：辅助 CIDR 内的云服务器无法通过对等连接、专线接入和其他 VPC、IDC 通信。

1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc)。
2. 在“私有网络”页面顶部，选择 VPC 所属地域。
3. 在 VPC 列表中目标 VPC 右侧**操作**列单击【编辑 CIDR】。
   ![](https://main.qcloudimg.com/raw/4a481b0690c7a1660530c3b6e8804674.png)
4. 在“编辑 CIDR” 对话框的 IPv4 CIDR 下方，单击【添加】，并填写辅助 CIDR 信息，然后单击【确认】。
   ![](https://main.qcloudimg.com/raw/6c72a8da68e6156bf98a7f86349aca0e.png)
	 
## 删除辅助 CIDR[](id:32)
>?目前辅助 CIDR 处于内测中，如有需要，请提交 [工单申请](https://console.cloud.tencent.com/workorder/category?level1_id=6&level2_id=168&source=0&data_title=%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9CVPC&step=1)。
>
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc)。
2. 在“私有网络”页面顶部，选择 VPC 所属地域。
3. 在 VPC 列表中，待删除辅助 CIDR 的 VPC 右侧**操作**列单击【编辑 CIDR】。
4. 在“编辑 CIDR” 对话框的 IPv4 CIDR 中，单击辅助 CIDR 后的【删除】并确认操作即可。
