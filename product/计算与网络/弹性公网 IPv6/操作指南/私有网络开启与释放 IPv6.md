>?目前弹性公网 IPv6 处于内测中，如有需要，请提交 [内测申请](https://cloud.tencent.com/apply/p/c28sebss8v)。

1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc)。
2. 在“私有网络”列表上方，选择【地域】，将会展示所属地域下的所以私有网络信息。
3. 在需要开启 IPv6 的 VPC 所在行的操作栏下，单击【编辑 CIDR】。
4. 在弹框中，可进行如下操作：
 - 若该 VPC 尚未获取 IPv6 CIDR，可单击【获取】并确认操作，系统将为该 VPC 分配1个`/56`的 IPv6 CIDR。
 - 若该 VPC 已获取到 IPv6 CIDR，可单击【释放】并确认操作，系统将释放该 VPC 的 IPv6 CIDR。
![](https://main.qcloudimg.com/raw/2b4081c5d2a48fcb576834251bcf9eef.png)
