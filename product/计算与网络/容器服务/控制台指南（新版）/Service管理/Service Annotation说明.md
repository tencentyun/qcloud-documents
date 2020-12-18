您可以通过以下Annotation注解来配置Service， 实现更丰富的负载均衡的能力。

### 注解的使用方式

```yaml
apiVersion: v1
kind: Service
metadata:
  annotations:  
    service.kubernetes.io/tke-existed-lbid: lb-6swtxxxx
  name: test
........
```

### Annotation 集合

1. service.kubernetes.io/loadbalance-id
   - 只读注解，提供当前Service引用的负载均衡 LoadBalanceId
2. service.kubernetes.io/qcloud-loadbalancer-internal-subnetid
   - 通过该Annotation指定创建内网类型CLB. 取值为子网ID
   - 使用示例：`service.kubernetes.io/qcloud-loadbalancer-internal-subnetid: subnet-xxxxxxxx `
3. service.kubernetes.io/tke-existed-lbid
   - 使用已存在的clb, 注意不同使用方式对腾讯云标签的影响
   - 使用方式详情见：[Service使用已有CLB](https://cloud.tencent.com/document/product/457/45491)
4. service.kubernetes.io/local-svc-only-bind-node-with-pod
   - Serice Local模式下仅绑定有Pod存在的节点
   - 使用方式详情见：[Service Local 模式](https://cloud.tencent.com/document/product/457/45492#service-local-.E6.A8.A1.E5.BC.8F)
5. service.cloud.tencent.com/local-svc-weighted-balance
   - 在Annotation `service.kubernetes.io/local-svc-only-bind-node-with-pod`的基础上搭配使用
   - CLB后端的权重将会由节点上工作负载的数量决定
   - 使用方式详情见：[Service Local 模式](https://cloud.tencent.com/document/product/457/45492#service-local-.E6.A8.A1.E5.BC.8F)
6. service.kubernetes.io/qcloud-loadbalancer-backends-label
   - 指定标签设置负载均衡后端绑定的节点
   - 使用方式详情见：[指定接入层后端](https://cloud.tencent.com/document/product/457/45492#.E6.8C.87.E5.AE.9A.E6.8E.A5.E5.85.A5.E5.B1.82.E5.90.8E.E7.AB.AF)
7. service.cloud.tencent.com/direct-access
   - 使用负载均衡直连Pod
   - 使用方式详情见：[使用 LoadBalancer 直连 Pod 模式 Service](https://cloud.tencent.com/document/product/457/41897)
8. service.cloud.tencent.com/tke-service-config
   - 通过tke-service-config配置负载均衡CLB
   - 使用方式详情见：[Service 负载均衡配置](https://cloud.tencent.com/document/product/457/45490)
9. service.cloud.tencent.com/tke-service-config-auto
   - 通过该注解可自动创建 TkeServiceConfig
   - 使用方式详情见： [Service 与 TkeServiceConfig 关联行为](https://cloud.tencent.com/document/product/457/45490#service-.E4.B8.8E-tkeserviceconfig-.E5.85.B3.E8.81.94.E8.A1.8C.E4.B8.BA)
10. service.kubernetes.io/loadbalance-nat-ipv6
    - 只读注解：创建NAT64 IPv6负载均衡时，负载均衡的IPv6地址将会展示到注解中
    - 示例：`service.kubernetes.io/loadbalance-nat-ipv6: "2402:4e00:1402:7200:0:9223:5842:2a44"`
11. service.kubernetes.io/loadbalance-type (即将废弃)
    - 控制自动创建的负载均衡类型，传统型负载均衡、应用型负载均衡。
    - 可选值：yunapi_clb(传统型)、classic(传统型)、yunapiv3_forward_clb(应用型)
    - 默认值：yunapiv3_forward_clb(应用型)
    - 注意：除非有特殊原因，否则不推荐使用传统型负载均衡，传统型负载均衡已经停止迭代准备下线，并且缺失大量特性。
12. service.cloud.tencent.com/specify-protocol
    - 支持通过注解为指定的监听端口配置TCP、UDP、TCP SSL、HTTP、HTTPS
    - 使用方式详情见：[Service扩展协议]()
13. service.kubernetes.io/service.extensiveParameters
    - 为创建负载均衡追加自定义参数，可以参考文档：https://cloud.tencent.com/document/product/214/30692
    -  示例 
      - 创建NAT64 IPv6实例：service.kubernetes.io/service.extensiveParameters: '{"AddressIPVersion":"IPV6"}' 
      - 购买电信负载均衡：service.kubernetes.io/service.extensiveParameters: '{"VipIsp":"CTCC"}'

