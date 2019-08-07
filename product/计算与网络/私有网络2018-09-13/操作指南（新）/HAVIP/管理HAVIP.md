>?HAVIP 目前处于灰度阶段，如有需要，请提交 [内测申请](https://cloud.tencent.com/apply/p/ednylty94f) 。

## 创建 HAVIP
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/)，在左侧导航栏中，选择【IP 与网卡】>【高可用虚拟 IP】。
2. 在 HAVIP 管理页面，选择所在地域，单击【申请】。
![](https://main.qcloudimg.com/raw/96ae45153eac7166d866ab3147f58736.png)
3. 输入名称，选择 HAVIP 所在的私有网络和子网，单击【确定】即可。
>?HAVIP 的 IP 地址可以自动分配，也可以手动指定（手动指定的合法校验跟普通内网 IP 一致）。
>
![](https://main.qcloudimg.com/raw/036b8d78f4b0de150fbd2d1bb2ae143d.png)

## 绑定和解绑 HAVIP
HAVIP 不是从控制台绑定，而是由后端云服务器根据心跳检测，协商和声明与 HAVIP 的绑定关系，此处与传统模式一致。您也可以通过更改 HA 应用的配置文件来更改绑定关系。
如 keepalived 方案下，在 keepalived.conf 中指定 virtual_address，请参见最佳实践 [VPC 内通过 keepalived 搭建高可用主备集群](https://cloud.tencent.com/document/product/215/20186)。如果是其他方案，在对应的配置文件中指定 virtual IP 为 HAVIP 即可。

## 释放 HAVIP
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/)，在左侧导航栏中，选择【IP 与网卡】>【高可用虚拟 IP】，在列表中找到需要释放的 HAVIP。
2. 单击操作栏下的【释放】，在弹出框中选择【确认】即可。
>!释放后请更改云服务器中的配置文件。
>
![](https://main.qcloudimg.com/raw/fca4f75f622cdeada644a1a8974ba3f4.png)
