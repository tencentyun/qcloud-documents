# 容器访问节点外服务时不做SNAT 配置



## 适用的场景

在 TKE 中无论是 Global Router 还是 VPC-CNI 网络模式，在容器内访问集群所在 VPC 网段和容器网段默认是不会做 SNAT 的，但除此之外访问其他网段都是会做 SNAT 的，当某些业务场景下需要保留容器源 IP 时，我们就需要修改相关配置来避免访问某些 IP 或网段时做 SNAT，从而实现保留容器源 IP 的需求。

## 操作步骤

在可以使用 kubectl 连接到集群的环境中，执行下面命令在资源的"NonMasqueradeCIDRs" 字段中添加不想做 SNAT 访问的目的 IP 或网段：

```bash
kubectl edit cm  ip-masq-agent-config -n kube-system
```

修改说明如下图所示（注意 YAML 格式）：

![image-20210324160422287](/Users/jokey/Library/Application Support/typora-user-images/image-20210324160422287.png)

等待 "ResyncInterval" 时间周期（默认1分钟）后测试看看配置是否生效。

