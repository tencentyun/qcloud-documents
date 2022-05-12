VPC-CNI 组件总共包括3个 kubernetes 集群组件，分别是 `tke-eni-agent`、`tke-eni-ipamd` 和 `tke-eni-ip-scheduler`。


## tke-eni-agent

以`daemonset`形式部署在集群中的每个节点上，职责：
- 拷贝 `tke-route-eni` 和 `tke-eni-ipamc` 等 CNI 插件到节点 CNI 执行文件目录（默认为 `/opt/cni/bin`）。
- 在 CNI 配置目录（默认为`/etc/cni/net.d/`）生成 CNI 配置文件。
- 设置节点策略路由和弹性网卡。
- Pod IP 分配/释放的 GRPC Server。
- 定期进行 IP 垃圾回收，回收 Pod 已不在节点上的 IP。
- 通过 kubernetes 的 [device-plugin 机制](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/) 设置网卡和 IP 的扩展资源。

## tke-eni-ipamd

以`deployment`形式部署在集群中的特定节点或 master 上，职责：

- 创建管理 CRD 资源（nec, vipc, vip, veni）。
- 非固定 IP 模式下，依据节点需求和状态创建/绑定/解绑/删除弹性网卡，分配/释放弹性网卡 IP。
- 固定 IP 模式下，依据 Pod 需求和状态创建/绑定/解绑/删除弹性网卡，分配/释放弹性网卡 IP。
- 节点弹性网卡安全组管理。
- 依据 Pod 需求创建/绑定/解绑/删除弹性公网 IP。

## tke-eni-ip-scheduler

以`deployment`形式部署在集群中的特定节点或 master 上，仅固定 IP 模式会部署，为调度扩展插件，职责：

- 多子网情况下，需要让已固定 IP 的 Pod 调度到指定子网的节点。
- 固定 IP 模式下，判断 Pod 调度的节点对应子网 IP 是否充足。
