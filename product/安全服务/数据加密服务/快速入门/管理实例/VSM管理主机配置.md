使用云加密机实例，需先通过与数据加密实例在同一个 VPC 内的 CVM 作为 VSM 管理主机，通过远程登录对 VSM 进行管理。
>! 如果所在的 VPC 下无可用的 CVM，您需要选购一台按量计费的 Windows 机型 CVM 作为管理服务器，并将该 CVM 加入指定 VPC 网络中，建议选择 CVM 最低配置即可。

## VSM 管理主机选购配置
登录 [云服务器购买页面](https://buy.cloud.tencent.com/cvm?tab=lite)，选择**自定义配置** > **按量付费模式**。
![](https://main.qcloudimg.com/raw/7be9ade3eba0bc3e543374da11207799.png)
- **地域可用区**：根据业务情况选择，目前仅支持北京二区、广州三区、上海四区。
- **私有网络**：业务应用、云加密机实例、管理主机 CVM（管理 VSM 实例）需配置同一 VPC 网络下。
- **选择镜像**：操作系统推荐 Windows 机型 CVM 最低配置。


## VSM 管理主机配置
远程登录购买的云服务器 CVM，登录前并做如图的配置，这样就可以在 VSM 管理主机中使用身份认卡 USBKey 了。 
1. 在**本地资源**中，打开**详细信息**。
![](https://main.qcloudimg.com/raw/1b43fa63182fa686294e7f4b38ea96ce.png)
2. 勾选**稍后插入的驱动器**。
![](https://main.qcloudimg.com/raw/240b7e27f6bd8af445d49085473791bc.png)
