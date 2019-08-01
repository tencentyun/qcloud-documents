## 绑定和解绑 HAVIP
HAVIP 不是从控制台绑定，而是由后端云服务器根据心跳检测，协商和声明绑定 HAVIP 的设备，此处与传统模式一致。您也可以通过更改 HA 应用的配置文件来更改绑定关系。
如，在 keepalived 方案下，在 keepalived.conf 中指定 virtual_address。如果是其他方案，在对应的配置文件中指定 virtual IP 为 HAVIP 即可。

详细操作步骤（以 keepalived 为例），请参见最佳实践 [VPC 内通过 keepalived 搭建高可用主备集群](https://cloud.tencent.com/document/product/215/20186)。

## 释放 HAVIP
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/)，在左侧导航栏中，选择【IP 与网卡】>【高可用虚拟 IP】，在列表中找到需要释放的 HAVIP。
2. 单击操作栏下的【释放】，在弹出框中选择【确认】即可。
>!释放后请更改云服务器中的配置文件。
>
![](https://main.qcloudimg.com/raw/d5856d81f3e04348e59a7212c2e6e469.png)
