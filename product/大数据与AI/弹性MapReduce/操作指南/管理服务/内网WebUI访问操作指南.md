EMR 集群创建时，如果没有勾选“开启集群 Master 节点公网”，将不能通过组件管理页面的原生 WebUI 访问地址进入相关组件的 WebUI 界面。本文主要介绍没有开启 Master 节点公网的集群如何查看组件原生 WebUI。

## 内网访问
在内网环境中通过浏览器访问组件 WebUI。各组件原生 WebUI 链接如下表所示：

| 组件名     | 链接                      |
| ---------- | ------------------------- |
| HDFS UI    | `http://{集群内网ip}:4008`  |
| YARN UI    | `http://{集群内网ip}:5004`  |
| HBASE UI   | `http://{集群内网ip}:6001`  |
| HIVE UI    | `http://{集群内网ip}:7003`  |
| HUE UI     | `http://{集群内网ip}:13000` |
| RANGER UI  | `http://{集群内网ip}:6080`  |
| STROM UI   | `http://{集群内网ip}:15001` |
| OOZIE UI   | `http://{集群内网ip}:12000` |
| GANGLIA UI | `http://{集群内网ip}:1800`  |
| PRESTO UI  | `http://{集群内网ip}:9000`  |
| ALLUXIO UI | `http://{集群内网ip}:19999` |


## 绑定弹性公网 IP
给 Master 节点绑定一个弹性公网 IP（EIP），即可在外网环境中通过浏览器访问组件 WebUI。绑定 EIP 操作如下：
1. 登录 [EMR 控制台](https://console.cloud.tencent.com/emr)，在集群列表中单击对应的集群 **ID/名称**进入集群详情页，然后在**集群资源 > 资源管理**中选择需要绑定弹性公网 IP 的 Master 节点，单击“资源名称/资源 ID”进入云服务器控制台。
![](https://main.qcloudimg.com/raw/25a29a278ac544b437af54c40feac6aa.png)
2. 调整 CVM 实例的网络带宽设置，保证需要绑定 EIP 的 CVM 实例带宽不为0，否则会无法连接相应节点。
在云服务器控制台 CVM 实例列表中选择对应实例的**更多 > 资源调整 > 调整网络**。
![](https://main.qcloudimg.com/raw/d48157c5f3470efb9d5a987de7d43210.png)
调整合适的目标带宽上限，保证 CVM 实例带宽大于0。
![](https://main.qcloudimg.com/raw/b1faea1c23b292c0ddcbf9ddfa5dff79.png)
3. 单击 CVM 实例的实例 ID 进入实例基本信息页面，并切换到弹性网卡页面。
![](https://main.qcloudimg.com/raw/73c82695d894aaac6ad6290d5a75cc54.png)
![](https://main.qcloudimg.com/raw/5c4c02a725a7fbd925da25431c0e4a9b.png)
4. 单击**绑定**，为当前 CVM 实例绑定一个已有的 EIP 或创建一个新的 EIP。
![](https://main.qcloudimg.com/raw/8246545addd5bf3f642a0fcf726fddcc.png)
绑定 EIP 后，可以看到弹性网卡页面，主网卡已绑定公网 IP 处已有 EIP 信息。
![](https://main.qcloudimg.com/raw/bcf1098c0daf5c0e05b6bc717fe82862.png)
5. 检查 CVM 实例是否可以通过公网访问。
可以通过 ping 或 ssh 命令检查 EIP 是否生效，**要确保安全组入站规则对 ICMP 和22端口开放**。
6. 访问组件原生 WebUI。
EMR-V1.3.1、EMR-V2.0.1、EMR-V2.1.0、EMR-V3.00 已支持 Apache Knox，默认在公网访问组件原生 WebUI 经过 Knox，各组件详细 UI 链接和 Knox 使用，请参考 [Knox 开发指南](https://cloud.tencent.com/document/product/589/35278)。

>?绑定 EIP 后 EMR 控制台原生 WebUI 访问地址不会相应变更，若需要变更控制台组件访问地址，可通过 [售后支持](https://cloud.tencent.com/online-service?from=connect-us) 联系我们。
