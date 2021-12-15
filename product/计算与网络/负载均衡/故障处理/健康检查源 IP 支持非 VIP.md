本文介绍如何将 CLB 健康检查的源 IP 由默认的 CLB 的 VIP 设置为100.64网段。

## 使用场景
1. **收敛后端服务器安全组**
健康检查源 IP 收敛为 100.64.0.0/10 网段。

2. **解决自建 Kubernetes 集群内网回环问题**
K8s 服务需要同时对集群内和集群外暴露。其中集群内通过集群内部负载均衡（IPVS）实现，集群外通过内网负载均衡 CLB 实现。IPVS 会把内网 CLB 的 IP 地址绑定在本地的一个接口上，这样集群内访问内网 CLB 的地址实际上用的是集群内的 IPVS 负载均衡。
而在容器服务 TKE 中，内网 CLB 使用了 CLB 的 VIP 地址作为健康检查源 IP，这与原生的 K8s 实现方式 IPVS 绑定的地址冲突，导致内网 CLB 健康检查失败。
设置健康检查源 IP 为100.64网段，可以避免地址冲突，解决健康检查失败问题。

## 处理步骤
将 CLB 健康检查的源 IP 由默认的 CLB 的 VIP 设置为100.64网段即可。本文以 TCP 监听器为例。
1. 登录 [负载均衡控制台](https://console.cloud.tencent.com/clb)。
2. 在“实例管理”页面左上角选择地域，在实例列表中找到目标实例，在“操作”列单击**配置监听器**。
3. 在“监听器管理”页签，找到目标监听器，单击监听器右侧的![](https://qcloudimg.tencent-cloud.cn/raw/11430ef75d92ba13520f8e05ed6d429b.svg)图标编辑监听器。
4. 在弹出的“编辑监听器”对话框中，单击**下一步**至“健康检查”页签。
5. 在“健康检查”页签中，健康检查源 IP 选择**100.64网段**，单击**下一步**后再单击**提交**。
<img src="https://qcloudimg.tencent-cloud.cn/raw/13b4fe7b91e8a3e775098a5935a35afc.png" width="70%" />

## 相关文档
- [配置健康检查](https://cloud.tencent.com/document/product/214/50011)
- [健康检查探测标识](https://cloud.tencent.com/document/product/214/6097#.E5.81.A5.E5.BA.B7.E6.A3.80.E6.9F.A5.E6.8E.A2.E6.B5.8B.E6.A0.87.E8.AF.86)
