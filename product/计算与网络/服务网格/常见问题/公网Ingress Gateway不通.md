从公网访问 ingressgateway 不通。

## 常见原因

### 安全组没放通 NodePort

TCM 安装的 ingressgateway ，暴露方式默认使用 CLB 绑定节点 NodePort，所以流量链路是: client –> CLB –> NodePort –> ingressgateway。

关键链路在于 CLB –> NodePort，CLB 转发的数据包不会做 SNAT，所以报文到达节点时源 IP 就是 client 的公网 IP，如果节点安全组入站规则没有放通 client –> NodePort 链路的话，是访问不通的。

**解决方案1：** 节点安全组入站规则对公网访问 NodePort 区间端口(30000-32768):

![img](https://main.qcloudimg.com/raw/7a8c3388d7ad1c3797f0c3ad7ac38e33.png)

**解决方案2：** 若担心直接放开整个 NodePort 区间所有端口有安全风险，可以只暴露 ingressgateway service 所用到的 Nodeport。

**解决方案3：** 若只允许固定 IP 段的 client 访问 ingressgateway，可以只对这个 IP 段放开整个 NodePort 区间所有端口。

**解决方案4：** 为 ingressgateway 启用 CLB 直通 Pod，这样流量就不经过 NodePort，所以就没有此安全组问题。启用 CLB 直通 Pod 需要集群网络支持 VPC-CNI，详细请参考 [如何启用 CLB 直通 Pod](https://imroc.cc/k8s/tke/faq/loadblancer-to-pod-directly/) 。

