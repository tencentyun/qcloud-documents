VPC 支持添加一个主 CIDR，且主 CIDR 创建后不可更改，当主 CIDR 不满足业务分配时，您可以创建辅助 CIDR 来扩充网段，一个 VPC 支持添加多个辅助 CIDR。
子网支持从主 CIDR 或者辅助 CIDR 中分配网段，无论子网属于主 CIDR 还是辅助 CIDR，同一 VPC 下不同子网均默认互通。

## 使用限制
+ 基础网络云服务器不支持和辅助 CIDR 内的云资源互通。
+ 对等连接不支持传递辅助 CIDR。
+ 云联网、VPN网关、标准型专线网关支持传递辅助 CIDR，其中专线网关还存在如下限制：
  - 金融云地域的标准型专线网关不支持传递辅助 CIDR。
  - 标准型专线网关支持传递10个辅助 CIDR。
  -  NAT型专线网关不支持传递辅助 CIDR。



## 创建辅助 CIDR[](id:21)
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc)。
2. 在【私有网络】页面顶部，选择 VPC 所属地域。
3. 在 VPC 列表中目标 VPC 右侧**操作**列选择【更多】>【编辑 IPv4 CIDR】。
	![](https://main.qcloudimg.com/raw/18d633a474b1818329fff952542f6bb2.png)
4. 在弹出编辑对话框中单击【添加】，并编辑辅助 CIDR。
>!辅助 CIDR 可以和自定义路由的目的网段重叠，但需要谨慎操作，因为辅助 CIDR 的路由属于 Local 路由，Local 路由比自定义子网路由优先级更高。
>
 <img src="https://main.qcloudimg.com/raw/775126708149064bad3383f873fcc654.png" width="50%" />
5. 单击【确定】完成辅助 CIDR 的创建。

## 删除辅助 CIDR[](id:32)
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc)。
2. 在【私有网络】页面顶部，选择 VPC 所属地域。
3. 在 VPC 列表中，待删除辅助 CIDR 的 VPC 右侧**操作**列选择【更多】>【编辑 IPv4 CIDR】。
4. 在弹出的编辑对话框中，单击辅助 CIDR 后的【删除】。
<img src="https://main.qcloudimg.com/raw/10602971a87c4babc86e2bb400cbc1b7.png" width="50%" />
5. 单击【确定】完成删除操作。
