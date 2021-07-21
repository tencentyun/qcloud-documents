VPC 支持 IPv6 功能，当您有 IPv6 业务需求时，需要先为 VPC 分配一个 IPv6 CIDR 网段，然后 VPC 内云资源才可以在 VPC 的 IPv6 CIDR 内分配到 IPv6 地址，从而进行 IPv6 业务通信。本章节介绍如何通过控制台为 VPC 分配 IPv6 CIDR。
>?目前 IPv6/IPv4 双栈 VPC 功能处于内测中，如有需要，请提交 [内测申请](https://cloud.tencent.com/apply/p/a9k0gialqhj)。
>

## 分配 IPv6 CIDR[](id:31)
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc)。
2. 在【私有网络】页面顶部，选择 VPC 所属地域。
3. 在 VPC 列表中，单击目标 VPC 右侧**操作**列选择【更多】>【编辑 IPv6 CIDR】。
![](https://main.qcloudimg.com/raw/c49782731a42f854bf4317ca3e79bfaf.png)
4. 在弹出的编辑对话框中单击【获取】，系统将为该 VPC 分配1个`/56`的 IPv6 CIDR。
	<img src="https://main.qcloudimg.com/raw/01b7354205829501fba21d99efd7d660.png" width="50%" />
5. 单击【确定】完成 IPv6 CIDR 的分配。

## 释放 IPv6 CIDR[](id:22)
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc)。
2. 在【私有网络】页面顶部，选择 VPC 所属地域。
3. 在 VPC 列表中已获取 IPv6 CIDR 的 VPC 右侧**操作**列选择【更多】>【编辑 IPv6 CIDR】。
4. 在弹出的 IPv6 CIDR 编辑对话框中，单击【释放】，在弹出的风险提示框中，知悉释放操作的风险并确认无误后，单击【确认】。
![](https://main.qcloudimg.com/raw/3308c74b8c447780f225681629649739.png)
5. 单击【确定】完成 IPv6 CIDR 的释放。
![](https://main.qcloudimg.com/raw/f6f49b4c1c5df5113690373efc7dfaeb.png)
