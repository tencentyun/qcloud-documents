默认情况下，Kube-proxy 使用 iptables 来实现 Service 到 Pod 之间的负载均衡。
TKE 支持快速开启基于 IPVS 来承接流量并实现负载均衡的操作。
开启 IPVS 更适用于大规模集群，可提供更好的可扩展性和性能。

## 注意事项
1. 本功能仅在创建集群时开启，暂不支持对存量集群的修改。
2. IPVS 开启针对全集群生效，强烈不建议手动修改集群内 IPVS 和 Iptables 混用。
3. 集群开启 IPVS 后不可关闭。
4. IPVS 仅针对 Kubernetes 版本 1.10 及以上的 TKE 集群生效。

## 操作指引
1. 创建集群选择高于 1.10 的 kubernetes 版本。
2. 高级设置开启 IPVS。

![](https://main.qcloudimg.com/raw/ebdddea2522a44ca9ecc58065a3ee3ee.png)
