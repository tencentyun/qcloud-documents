本文档主要对 Kudu 集群类型 Core 节点 tserver 缩容时，需进行的数据搬迁进行介绍。
>? Kudu 集群类型支持 Core 节点缩容，该功能未默认开放，如有需要请您 [提交工单](https://console.cloud.tencent.com/workorder/category) 申请开通。

在进行 tserver 节点下线前，可以使用 rebalance tool 做数据迁移。请注意，一次只能下线一台 tserver，如果下线多台，需重复执行下述步骤。

## Kudu 基于 rebalance tool 迁移
1. 确保集群状态 ok。
```
/usr/local/service/kudu/bin/kudu cluster ksck $KuduMaster1_ip::port,$KuduMaster2_ip::port,$KuduMaster3_ip::port

```
其中 $KuduMaster1_ip、$KuduMaster2_ip、$KuduMaster3_ip 为 EMR 集群中3个 KuduMaster 角色所在节点的 IP；port 为链接 kudu 的端口号，默认为7051。
![](https://qcloudimg.tencent-cloud.cn/raw/5c363c32fd1b5a56ae5c0a2b76798aae.png)
2. 使用步骤1的 ksck 命令，获取下线的节点 uid。
![](https://qcloudimg.tencent-cloud.cn/raw/3e2bfb44bf57f6a22a615d6bd6a06915.png)
以 fb9afb1b2989456cac5800bf6990dfea 节点为例子。
3. 将 fb9afb1b2989456cac5800bf6990dfea 节点进入维护模式。
```
/usr/local/service/kudu/bin/kudu tserver state enter_maintenance $KuduMaster1_ip::port,$KuduMaster2_ip::port,$KuduMaster3_ip::port fb9afb1b2989456cac5800bf6990dfea
```
4. 执行 rebalance 命令
```
/usr/local/service/kudu/bin/kudu cluster rebalance $KuduMaster1_ip::port,$KuduMaster2_ip::port,$KuduMaster3_ip::port --ignored_tservers fb9afb1b2989456cac5800bf6990dfea --move_replicas_from_ignored_tservers
```
等待命令执行结束，再次用 ksck 检查，状态为 ok，继续后面步骤。
5. 暂停 fb9afb1b2989456cac5800bf6990dfea 对应节点10.0.1.45的 tserver 进程。注意此时，使用ksck命令，集群状态不健康，需要重启 master。
![](https://qcloudimg.tencent-cloud.cn/raw/48475acf8c1c4a790bfd52a8c353776a.png)
6. 在 [EMR 控制台](https://console.cloud.tencent.com/emr) 重启 master。注意需要手动一台一台的重启（不建议使用控制台的滚动重启）。重启结束后，使用ksck命令，确保集群状态健康。
![](https://qcloudimg.tencent-cloud.cn/raw/b70b4513c08c98672bc2b81eebc07bc8.png)


