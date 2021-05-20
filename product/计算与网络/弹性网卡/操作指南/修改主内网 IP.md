本文介绍如何在弹性网卡控制台修改云服务器主内网IP。
>!
>+ 仅支持修改云服务器主网卡的主内网 IP，不支持修改辅助网卡的主内网 IP。
>+ 修改主网卡的主内网 IP 会导致关联的实例自动重启约30s，重启过程中会存在短暂的业务中断，重启后业务即可恢复，请您根据实际情况谨慎操作。
>+ 修改主内网 IP 也可以在云服务器控制台执行，如有需要，请参考 [修改内网 IP 地址](https://cloud.tencent.com/document/product/213/16561)。

## 前提条件
请先登录云服务器控制台，获取云服务器的主网卡 ID，具体请参考 [查看实例信息](https://cloud.tencent.com/document/product/213/16533)。

## 操作步骤
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc) 。
2. 单击左侧目录中的【IP 与网卡】>【弹性网卡】，进入弹性网卡列表页。
3. 单击需要修改的实例 ID，进入详情页。
4. 单击选项卡中的【IPv4 地址管理】，查看已绑定的主内网 IP。
![](https://main.qcloudimg.com/raw/934d05bfa4555aac06c1d5c62274336e.png)
5. 单击需要修改的主内网 IP 所在行的【修改主 IP】。
![](https://main.qcloudimg.com/raw/2b3675a7f30d2131c15bf529c2e7f6b1.png)
6. 在弹窗内输入新的主内网 IP，单击【确定】即可。
![](https://main.qcloudimg.com/raw/3cffb3d3c6f99365df2ffe75c2c4004f.png)
