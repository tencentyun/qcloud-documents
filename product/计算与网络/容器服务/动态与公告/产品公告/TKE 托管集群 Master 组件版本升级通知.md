
 ## 升级时间
 容器服务 TKE 计划于2022年10月12-13、17-18、24-27日的22:00-05:00分批次对 TKE 托管集群 Master 组件的 kubernetes 版本进行小版本升级。
 
 ## 升级范围
本次升级操作的范围包括：托管集群的 Master 组件，且集群 kubernetes 的大版本在1.16至1.22之间。升级后的集群 Master 组件将维持在当前所在大版本的最新小版本（如，您集群当前 Master 版本为 v1.20.6-tke.15，TKE 发布的最新版本为 v1.20.6-tke.27，则升级后的版本为 v1.20.6-tke.27）。
 
 
 ## 升级内容
 本次升级内容主要包含：
1. **性能提升**：优化大规模集群的 kube-apiserver List 性能，提升 etcd 的存储稳定性。
2. **安全加固**：合并了社区 CVE-2022-3172 等关键漏洞修复 PR。
3. **稳定性增强**：合并社区多个特性修复 PR，完善 kubelet、kube-scheduler、HPA 等组件相关能力。
4. **特性支持**：支持原生节点专用调度器、Pod 原地升降配、超级节点创建等特性。

## 升级说明
Master 小版本升级完全向下兼容，无需重新设置 Kubernetes 组件启动参数，您原先的设置（若有）会被保留。本次升级不会改变 Master 组件所在的 Kubernetes 大版本，也不会变更 Node kubernetes 版本。若您需要了解 TKE Kubernetes Revision 版本变更详情，可参考 [TKE Kubernetes Revision 版本历史](https://cloud.tencent.com/document/product/457/9315)。感谢您对腾讯云的信赖与支持！若有任何疑问可 [联系我们](https://cloud.tencent.com/document/product/457/59560)。

<dx-alert infotype="notice" title="">
1.14及以下 Kubernetes 版本已停止版本迭代，TKE 将不再为这些版本集群提供技术支持，建议您尽快升级集群版本，操作详情见 [集群升级](https://cloud.tencent.com/document/product/457/32192)。
</dx-alert>
