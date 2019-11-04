>? 弹性公网 IPv6 即将开启内测，敬请期待。 

1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc)。
2. 在“私有网络”列表上方，选择【地域】，将会展示所属地域下的所以私有网络信息。
3. 在需要开启 IPv6 的 VPC 所在行的操作栏下，单击【编辑 CIDR】。
4. 在弹框中的 IPv6 CIDR 单击【获取】并确认操作，系统将为该 VPC 分配1个`/56`的 IPv6 CIDR。
![](https://main.qcloudimg.com/raw/048e6e83270bac19e8eeb7ff04213861.png)
4. 已获取到 IPv6 CIDR 的 VPC，可单击操作栏下的【编辑 CIDR】，在弹框中的 IPv6 CIDR 单击【释放】来释放 IPv6 地址段。
5. 在左侧目录单击【子网】，在“子网”列表上方，选择【地域】和【私有网络】，将会展示所属地域和私有网络下的所有子网信息。
6. 选择一个子网，单击【获取 IPv6 CIDR】，系统将为该子网分配1个`/64`的 IPv6 CIDR。 
![](https://main.qcloudimg.com/raw/3db90f85772ffa7db85197801b1f05c5.png)
7. 选择一个已获取到 IPv6 CIDR 的子网，单击【释放 IPv6】并确定操作，系统将回收该子网的 IPv6 CIDR。
![](https://main.qcloudimg.com/raw/eeb1861a719274c1526e6301952c54c9.png)
