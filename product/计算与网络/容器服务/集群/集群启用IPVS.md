## 集群启用IPVS
默认情况下，Kube-proxy使用iptables来实现Service到Pod之间的负载均衡。
TKE支持快速开启基于IPVS来承接流量并实现负载均衡。
开启IPVS更适用于大规模集群，可提供更好的可扩展性和性能。

## 注意事项
1. 本功能仅在创建集群时开启，暂不支持对存量集群的修改。
2. IPVS开启针对全集群生效，强烈不建议手动修改集群内IPVS和Iptables混用。
3. 集群开启IPVS后不可关闭。
4. IPVS仅针对Kubernetes版本1.10及以上的TKE集群生效。

## 操作指引
1. 创建集群选择高于1.10的kubernetes版本
2. 高级设置开启IPVS

![开启IPVS][ipvs]

[ipvs]:https://main.qcloudimg.com/raw/a1a6de3e6f1054df1d0fb044093fd1cc.png
