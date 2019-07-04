## 操作场景

默认情况下，Kube-proxy 使用 iptables 来实现 Service 到 Pod 之间的负载均衡。TKE 支持快速开启基于 IPVS 来承接流量并实现负载均衡。开启 IPVS 适用于大规模集群，可提供更好的可扩展性和性能。

## 注意事项

- 本功能仅在创建集群时开启，暂不支持对存量集群的修改。
- IPVS 开启针对全集群生效，建议不要手动修改集群内 IPVS 和 Iptables 混用。
- 集群开启 IPVS 后不可关闭。
- IPVS 仅针对 Kubernetes 版本1.10及以上的 TKE 集群生效。

## 操作步骤

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)。
2. 参考 [创建集群](https://cloud.tencent.com/document/product/457/32189)，在 “创建集群” 页面中，将 “Kubernetes版本” 设置为高于1.10的 Kubernetes 版本，并单击【高级设置】，开启 “ipvs 支持”。如下图所示：
![开启IPVS](https://main.qcloudimg.com/raw/a625e2d1b7ef313a65e04aab25832e18.png)
3. 按照页面提示逐步操作，完成集群的创建。

