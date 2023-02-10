磁盘 IO 精细调度能力提供了一系列功能，保证业务磁盘方面的服务质量保证。全方位磁盘网络表现，以及灵活限制容器对网络的使用。

## 使用限制

1. 部署 [QoS Agent](https://cloud.tencent.com/document/product/457/79774)。
2. 在集群里的“扩展组件”页面，找到部署成功的 QoS Agent，单击右侧的**更新配置**。
3. 在修改 QoS Agent 的组件配置页面，勾选 **磁盘 IO QoS 增强**。
4. 输入参数指定限制的磁盘名称，如：vda,vdb。
5. 单击**完成**。

开启功能之后，还需要执行如下操作（如果有两个磁盘，则需要执行两次如下命令，第二次执行时将第一行的磁盘名字更换成第二个磁盘的名字）：

```shell
DISK_HOLDER=vda
# 开启BFQ
echo bfq > /sys/block/${DISK_HOLDER}/queue/scheduler
# 针对多容器场景下，提升调度均衡性
echo bfq > /sys/block/$DISK_HOLDER/queue/scheduler
echo 0 > /sys/block/$DISK_HOLDER/queue/iosched/low_latency
echo 1 > /sys/block/$DISK_HOLDER/queue/iosched/better_fairness
echo 1 > /sys/block/$DISK_HOLDER/queue/iosched/group_share
echo 50 > /sys/block/$DISK_HOLDER/queue/iosched/timeout_sync
# 增大磁盘队列深度
echo 1000 >  /sys/block/$DISK_HOLDER/queue/nr_requests
echo 64 > /sys/block/$DISK_HOLDER/queue/max_sectors_kb
```



## 功能一：磁盘 IOPS 限制（direct IO + buffer IO）

1. 根据上述使用限制部署组件、打开相关开关、输入相关磁盘、执行相关命令。
2. 部署业务。
3. 部署关联该业务的 PodQOS 对象，选择需要作用的业务，示例如下：
```yaml
apiVersion: ensurance.crane.io/v1alpha1
kind: PodQOS
metadata:
  name: a
spec:
  labelselector:
    matchLabels:
      k8s-app: a	# 选择业务的 Label
  resourceQOS:
    diskIOQOS:
      diskIOLimit:
        readIOps: 1024	# readIOps 代表限制 Pod 读 IO 的量，单位为 IOPS/s
        writeIOps: 1024	# writeIOps 代表限制 Pod 写 IO 的量，单位为 IOPS/s
```



### 针对 buffer IO 的限速机制

由于低版本内核或 cgroup v1 对 Buffer IO 无法有效限速，有可能造成 Buffer IO 干扰业务正常 IO（数据库场景经常使用direct IO）。TKE 基于 cgroup v1 提供了 Buffer IO 限速功能。基于 cgroup v2 的 Buffer IO 限速和上游内核保持一致。

cgroup v1 无法支持限速的主要原因在于异步刷脏页的时候，内核无法得知这个 IO 应该提交给哪个 blkio cgroup。示例如下：
![img](https://qcloudimg.tencent-cloud.cn/raw/e66eaa44fe26b9759bb1f6102b5dda50.png)        

为了解决这个记账问题，TKE 将 page cache 所属的 cgroup 和对应的 blkio cgroup 进行绑定。之后异步刷盘时，内核线程便可以确定目标 blkio cgroup。



## 功能二：磁盘 BPS 限制（direct IO + buffer IO)

1. 根据上述使用限制部署组件、打开相关开关、输入相关磁盘、执行相关命令。
2. 部署业务。
3. 部署关联该业务的 PodQOS 对象，选择需要作用的业务，示例如下：
```yaml
apiVersion: ensurance.crane.io/v1alpha1
kind: PodQOS
metadata:
  name: a
spec:
  labelselector:
    matchLabels:
      k8s-app: a
  resourceQOS:
    diskIOQOS:
      diskIOLimit:
        readBps: 1048576	# readBPS 限制 Pod 读带宽，单位为 mbps
        writeBps: 1048576	# writeBPS 限制 Pod 写带宽，单位为 mbps
```
