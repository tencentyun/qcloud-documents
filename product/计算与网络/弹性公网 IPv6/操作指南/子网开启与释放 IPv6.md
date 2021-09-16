>? 目前弹性公网 IPv6 处于内测中，如有需要，请提交 [内测申请](https://cloud.tencent.com/apply/p/a9k0gialqhj)。
>

1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc)。
2. 在左侧目录单击**子网**，在“子网”列表上方，选择**地域**和**私有网络**，将会展示所属地域和私有网络下的所有子网信息。
3. 选择一个未获取到 IPv6 CIDR 子网，在其所在行的操作栏下，选择**更多** > **获取 IPv6 CIDR**，并确认操作，系统将为该子网分配 1 个`/64`的 IPv6 CIDR。 
![](https://main.qcloudimg.com/raw/5e17f34c9acd1931042ebbf2bb6c1155.png)
4. 选择一个已获取到 IPv6 CIDR 的子网，在其所在行的操作栏下，选择**更多** > **释放 IPv6 CIDR**，并确定操作，系统将回收该子网的 IPv6 CIDR。
![](https://main.qcloudimg.com/raw/597025125e3034a3859d26d19b1441e8.png)


