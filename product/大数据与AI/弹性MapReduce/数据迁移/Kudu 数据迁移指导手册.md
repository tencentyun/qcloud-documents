Kudu 可以通过 rebalance tool 做数据迁移。
>!一次只能下线一台 tserver，如果下线多台，需重复执行下述步骤。

## Kudu 基于 rebalance tool 迁移
1. 确保集群状态ok。
```
 /usr/local/service/kudu/bin/kudu cluster ksck 10.0.1.29:7051,10.0.1.16:7051,10.0.1.36:7051
```
![](https://qcloudimg.tencent-cloud.cn/raw/7b11bf98171f44cd24bc671194fa313b.png)  

2. 使用步骤1的 ksck 命令，获取下线的节点 uid。 
![](https://qcloudimg.tencent-cloud.cn/raw/82caa032beaaa649683f80e22fd8083f.png)
以 fb9afb1b2989456cac5800bf6990dfea 节点为例子。

3. 将 fb9afb1b2989456cac5800bf6990dfea 节点进入维护模式。
```
 /usr/local/service/kudu/bin/kudu tserver state enter_maintenance 10.0.1.29:7051,10.0.1.16:7051,10.0.1.36:7051 fb9afb1b2989456cac5800bf6990dfea
```

4. 执行rebalance命令。
```
 /usr/local/service/kudu/bin/kudu cluster rebalance 10.0.1.29:7051,10.0.1.16:7051,10.0.1.36:7051 --ignored_tservers fb9afb1b2989456cac5800bf6990dfea --move_replicas_from_ignored_tservers
```
等待命令执行结束，再次用 ksck 检查，状态为 ok，继续后面步骤。

5. 暂停 fb9afb1b2989456cac5800bf6990dfea 对应节点10.0.1.45的 tserver 进程。注意此时，使用 ksck 命令，集群状态不健康，需要重启 tmaster。 
![](https://qcloudimg.tencent-cloud.cn/raw/216ee22e20f45c4ca26143dd115c694f.png)
6. 在 EMR 控制台重启 master。注意需要手动一台一台地重启（不建议使用控制台的滚动重启）。重启结束后，使用 ksck 命令，确保集群状态健康。
![](https://qcloudimg.tencent-cloud.cn/raw/c5c596e1221718dd565921d568932e84.png)
