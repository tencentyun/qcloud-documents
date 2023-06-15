## 功能介绍
软件 WebUI 入口功能是 EMR 提供的组件原生 UI 访问能力，通过 Master 节点的外网 IP（建议及时配置安全策略）可以快捷访问组件原生 UI。如果集群内网与企业网络互通，可关闭该外网 IP，直接通过内网访问组件原生 UI。
## 查看 WebUI 访问地址
1. 登录 [EMR 控制台](https://console.cloud.tencent.com/emr)，在集群列表中单击对应的集群 **ID/名称**进入集群详情页。
2. 在集群详情页中单击**集群服务**，然后单击对应的组件卡页下方 **WebUI 地址**即可访问。
访问地址需要进行身份验证，用户名为 root，默认密码为创建集群时输入的密码。如果需要修改密码，可以在此页面中单击**重置 WebUI 密码**进行修改。
![](https://qcloudimg.tencent-cloud.cn/raw/f5cf64272d81f2a8b7aa43d2d25c7a54.png)

## 访问内网 WebUI 
集群创建时，如果没有勾选**开启集群 Master 节点公网**，将不能通过组件管理页面的原生 WebUI 访问地址进入相关组件的 WebUI 界面。在内网环境中通过浏览器访问组件 WebUI。各组件原生 WebUI 链接如下表所示：


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

如需在集群创建后通过公网访问组件 WebUI，可以给主 Master 节点绑定一个弹性公网 IP（EIP）实现。绑定 EIP 操作如下：
1. 登录 [EMR 控制台](https://console.cloud.tencent.com/emr)，在集群列表中单击对应的**集群 ID/名称**进入集群详情页，然后在**集群资源 > 资源管理**中选择需要绑定弹性公网 IP 的 Master 节点，单击**资源 ID** 进入云服务器控制台。
![](https://qcloudimg.tencent-cloud.cn/raw/0fc5d2db562af38e043c22730b222c2d.png)
2. 调整 CVM 实例的网络带宽设置，保证需要绑定 EIP 的 CVM 实例带宽不为0，否则会无法连接相应节点。
在云服务器控制台 CVM 实例列表中选择对应实例的**更多 > 资源调整 > 调整网络**。
![](https://qcloudimg.tencent-cloud.cn/raw/cbedf871b3510c0bd9425ddc7bf7f816.png)
调整合适的目标带宽上限，保证 CVM 实例带宽大于0。
![](https://qcloudimg.tencent-cloud.cn/raw/6af14a978651b126f2de8c81dae2eaf4.png)
3. 单击 CVM 实例的**实例 ID** 进入实例基本信息页面，并切换到弹性网卡页面。
![](https://qcloudimg.tencent-cloud.cn/raw/a9bd5e346f589719254dfb49bd0988c5.png)
4. 单击**绑定**，为当前 CVM 实例绑定一个已有的 EIP 或创建一个新的 EIP。
![](https://qcloudimg.tencent-cloud.cn/raw/eb751f82f14e51394549ae9438b00f62.png)
绑定 EIP 后，可以看到弹性网卡页面，主网卡已绑定公网 IP 处已有 EIP 信息。
5. 检查 CVM 实例是否可以通过公网访问。
6. 可以通过 ping 或 ssh 命令检查 EIP 是否生效，要确保安全组入站规则对 ICMP 和22端口开放。访问组件原生 WebUI。

EMR-V1.3.1、EMR-V2.0.1、EMR-V2.1.0、EMR-V3.00 已支持 Apache Knox，默认在公网访问组件原生 WebUI 经过 Knox，各组件详细 UI 链接和 Knox 使用，请参考 [Knox 指引](https://cloud.tencent.com/document/product/589/35278)。

>? 绑定 EIP 后 EMR 控制台原生 WebUI 访问地址不会相应变更，若需要变更控制台组件访问地址，可通过 [在线客服](https://cloud.tencent.com/online-service?from=connect-us) 联系我们。

## 重置 WebUI 密码
访问地址需要进行身份验证，用户名为 root，默认密码为创建集群时输入的密码，如需重置 WebUI 密码可以通过以下操作实现。
1. 登录 [EMR 控制台](https://console.cloud.tencent.com/emr)，在集群列表中单击对应的集群 **ID/名称**进入集群详情页。
2. 在集群详情页中单击**集群服务**，然后单击左上角**重置 WebUI 密码**进行密码重置。
>! 
>- 密码要求：8-16个字符，至少包含大写字母、小写字母、数字和特殊字符（!@#%^*）中的三种，其中第一个字符不能为特殊字符。
>- 已安装 OpenLDAP 的集群（EMR-V2.6.0 和 EMR-V3.2.1 以后产品版本），密码调整只能在用户管理页面进行管理。如需重置 WebUI 密码，请在用户管理页面，使用新建用户功能进行操作。
>
![](https://qcloudimg.tencent-cloud.cn/raw/39378348cb520fdfd9a14c729c56ef74.png)
