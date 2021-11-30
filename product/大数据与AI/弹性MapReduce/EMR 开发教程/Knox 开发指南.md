目前 EMR-V1.3.1 和 EMR-V2.0.1 版本已经支持 [Apache Knox](https://knox.apache.org/?spm=a2c4g.11186623.2.10.22b554deZiOUor)，完成以下准备工作后，即可在公网直接访问 Yarn、HDFS 等服务的 Web UI。

## 准备工作
- 确认您已开通腾讯云，并且创建了一个 EMR 集群。
- EMR-V1.3.1 和 EMR-V2.0.1 默认在创建集群时，Knox 作为必选组件。如果您的集群是老集群，目前可通过 [联系客服](https://cloud.tencent.com/about/connect) 安装 Knox。

## 开始访问 Knox
使用集群公网 IP 地址访问。建议修改集群拥有公网 IP 的 CVM 安全组规则，限定 TCP:30002 端口的访问 IP 端为您的 IP 端。
1. 通过集群详情查看公网 IP。
2. 在浏览器中访问相应服务的 URL。
   - HDFS UI：https://{集群公网ip}:30002/gateway/emr/hdfs
   - Yarn UI：https://{集群公网ip}:30002/gateway/emr/yarn
   - Hive UI：https://{集群公网ip}:30002/gateway/emr/hive
   - Hbase UI：https://{集群公网ip}:30002/gateway/emr/hbase/webui
   - HUE UI：https://{集群公网ip}:30002/gateway/emr/hue
   - Storm UI：https://{集群公网ip}:30002/gateway/emr/stormui
   - Ganglia UI：https://{集群公网ip}:30002/gateway/emr/ganglia/
   - Presto UI：https://{集群公网ip}:30002/gateway/emr/presto/
   - Oozie UI：https://{集群公网ip}:30002/gateway/emr/oozie/
3. 浏览器显示**您的链接不是私密链接**，是因为 Knox 服务使用了自签名证书，请再次确认访问的是自己集群的公网 IP，并且端口为30002。选择**高级 > 继续前往**。
4. 弹出的验证登录框，用户名为 root，默认密码为创建集群时输入的密码。建议您修改密码，可以在该页面中单击**重置原生 UI 密码**进行修改。


