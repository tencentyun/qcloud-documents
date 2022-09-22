
## 开启内网访问后无法访问
您可以直接在容器服务控制台上 [开启内网访问](https://cloud.tencent.com/document/product/457/32191#2.-.E5.BC.80.E5.90.AF.E9.9B.86.E7.BE.A4.E8.AE.BF.E9.97.AE)。如果开启内网访问之后仍出现无法访问的情况，建议您对应集群类型进行如下检查：

#### 托管集群[](id:ManagedCluste)
参考 [查看节点安全组配置](https://cloud.tencent.com/document/product/457/40332#config) 检查集群中节点的安全组是否正确放通30000-32768端口区间。

#### 独立集群
1. 参考 [查看节点安全组配置](https://cloud.tencent.com/document/product/457/40332#config) 检查集群中节点的安全组是否正确放通30000-32768端口区间。
- 开启内网访问时，您已通过控制台设置了 VPC 子网网段，请检查集群中 Master 节点是否正确放通该 VPC 子网网段。
- 检查集群中 Master 节点的安全组是否正确放通 Master 节点所在的 VPC 网段或 VPC 子网网段。

## 开启公网访问后无法访问
您可以直接在容器服务控制台上 [开启公网访问](https://cloud.tencent.com/document/product/457/32191#2.-.E5.BC.80.E5.90.AF.E9.9B.86.E7.BE.A4.E8.AE.BF.E9.97.AE)。如果开启公网访问之后仍出现无法访问的情况，建议您对应集群类型进行如下检查：

#### 托管集群
检查安全组来源 CIDR 是否正确设置，或将来源 `0.0.0.0/0` 设置为全放通之后，再进行公网访问测试。

####  独立集群
独立集群开启公网访问之后，会在集群中自动创建 `default/kubelb-internet` Service 对象。该 Service 会自动绑定一个公网类型的 CLB，默认不会为该 CLB 绑定安全组（即全放通），且 EXTERNAL-IP 字段显示即为此 CLB 的 VIP。如下所示：
```
$ kubectl get service kubelb-internet
NAME              TYPE           CLUSTER-IP      EXTERNAL-IP    PORT(S)         AGE
kubelb-internet   LoadBalancer   172.16.252.94   152.136.8.98   443:32750/TCP   3m4s
```
1. 检查 `default/kubelb-internet` Service 对象已绑定的 CLB 是否设置了安全组，并且安全组是否正确配置。
- 参考 [查看节点安全组配置](https://cloud.tencent.com/document/product/457/40332#config) 检查集群中 Master 节点的安全组是否正确放通30000 - 32768端口区间。
- 检查集群中 Master 节点的安全组是否正确放通 Master 节点所在的 VPC 网段或 VPC 子网网段。
