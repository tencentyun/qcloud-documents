您可以通过以下 Annotation 注解配置 Service，以实现更丰富的负载均衡的能力。

## 注解使用方式

```yaml
apiVersion: v1
kind: Service
metadata:
    annotations:  
      service.kubernetes.io/tke-existed-lbid: lb-6swtxxxx
    name: test
........
```

## Annotation 集合


### service.kubernetes.io/loadbalance-id
**说明：**
只读注解，提供当前 Service 引用的负载均衡 LoadBalanceId。您可以在腾讯云 CLB 控制台查看与集群在同一 VPC 下的 CLB 实例 ID。
 
---
### service.kubernetes.io/qcloud-loadbalancer-internal-subnetid
**说明：**
通过该 Annotation 指定创建内网类型 CLB，取值为子网 ID。

**使用示例：**
`service.kubernetes.io/qcloud-loadbalancer-internal-subnetid: subnet-xxxxxxxx`
 
---
### service.kubernetes.io/tke-existed-lbid
**说明：**
使用已存在的 CLB，需注意不同使用方式对腾讯云标签的影响。

**使用示例：**
使用方式详情见 [Service 使用已有 CLB](https://cloud.tencent.com/document/product/457/45491)。
 
---
### service.kubernetes.io/local-svc-only-bind-node-with-pod
**说明：**
Service Local 模式下仅绑定有 Pod 存在的节点。

**使用示例：**
使用方式详情见 [Service Local 模式](https://cloud.tencent.com/document/product/457/45492#service-local-.E6.A8.A1.E5.BC.8F)。
 
---
### service.cloud.tencent.com/local-svc-weighted-balance
**说明：**
- 与 Annotation `service.kubernetes.io/local-svc-only-bind-node-with-pod` 搭配使用。
- CLB 后端的权重将会由节点上工作负载的数量决定。


**使用示例：**
使用方式详情见 [Service Local 模式](https://cloud.tencent.com/document/product/457/45492#service-local-.E6.A8.A1.E5.BC.8F)。
 
---
### service.kubernetes.io/qcloud-loadbalancer-backends-label
**说明：**
指定标签设置负载均衡后端绑定的节点。

**使用示例：**
使用方式详情见 [指定接入层后端](https://cloud.tencent.com/document/product/457/45492#.E6.8C.87.E5.AE.9A.E6.8E.A5.E5.85.A5.E5.B1.82.E5.90.8E.E7.AB.AF)。
 
---
### service.cloud.tencent.com/direct-access
**说明：**
使用负载均衡直连 Pod。

**使用示例：**
使用方式详情见 [使用 LoadBalancer 直连 Pod 模式 Service](https://cloud.tencent.com/document/product/457/41897)。
 
---
### service.cloud.tencent.com/tke-service-config
**说明：**
通过 tke-service-config 配置负载均衡 CLB。

**使用示例：**
使用方式详情见 [Service 负载均衡配置](https://cloud.tencent.com/document/product/457/45490)。
 
---
### service.cloud.tencent.com/tke-service-config-auto
**说明：**
通过该注解可自动创建 TkeServiceConfig。

**使用示例：**
使用方式详情见 [Service 与 TkeServiceConfig 关联行为](https://cloud.tencent.com/document/product/457/45490#service-.E4.B8.8E-tkeserviceconfig-.E5.85.B3.E8.81.94.E8.A1.8C.E4.B8.BA)。
 
---
### service.kubernetes.io/loadbalance-nat-ipv6
**说明：**
只读注解，创建 NAT64 IPv6 负载均衡时，负载均衡的 IPv6 地址将会展示到注解中。

**使用示例：**
`service.kubernetes.io/loadbalance-nat-ipv6: "2402:4e00:1402:7200:0:9223:5842:2a44"`
 
---
### service.kubernetes.io/loadbalance-type（即将废弃）
**说明：**
- 控制自动创建的负载均衡类型，传统型负载均衡、应用型负载均衡。
- 可选值：yunapi_clb（传统型）、classic（传统型）、yunapiv3_forward_clb（应用型）
- 默认值：yunapiv3_forward_clb（应用型）
>! 除非有特殊原因，否则不推荐使用传统型负载均衡，传统型负载均衡已经停止迭代准备下线，并且缺失大量特性。
 
---
### service.cloud.tencent.com/specify-protocol
**说明：**
支持通过注解为指定的监听端口配置 TCP、UDP、TCP SSL、HTTP、HTTPS。

**使用示例：**
使用方式详情见 [Service 扩展协议](https://cloud.tencent.com/document/product/457/51259)。
 
---
### service.kubernetes.io/service.extensiveParameters
**说明：**
该 Annotation 使用的是 CLB 创建时的参数，当前仅在创建时支持配置，创建后不支持修改，创建后修改本注解无效。
参考 [创建负载均衡实例](https://cloud.tencent.com/document/product/214/30692) 为创建负载均衡追加自定义参数。

**使用示例：**
- 创建 NAT64 IPv6 实例：
 service.kubernetes.io/service.extensiveParameters: '{"AddressIPVersion":"IPV6"}' 
- 购买电信负载均衡：
  service.kubernetes.io/service.extensiveParameters: '{"VipIsp":"CTCC"}'
- 创建时自定义 CLB 名字：
  service.kubernetes.io/service.extensiveParameters: '{"LoadBalancerName":"my_cutom_lb_name"}'


 
---
### service.cloud.tencent.com/enable-grace-shutdown
**说明：**
支持 CLB 直连模式的优雅停机。Pod 被删除，此时 Pod 里有 DeletionTimestamp，且状态置为 Terminating。此时调整 CLB 到该 Pod 的权重为 0。

**使用示例：**
仅在直连模式下支持，需要配合使用 `service.cloud.tencent.com/direct-access`，使用方式详情见 [Service 优雅停机](https://cloud.tencent.com/document/product/457/60064)。


---
### service.cloud.tencent.com/enable-grace-shutdown-tkex
**说明：**
支持 CLB 直连模式的优雅退出。Endpoint 对象中 endpoints 是否 not-ready，将 not-ready 的 CLB 后端权重置为 0。

**使用示例：**
仅在直连模式下支持，需要配合使用 `service.cloud.tencent.com/direct-access`，使用方式详情见 [Service 优雅停机](https://cloud.tencent.com/document/product/457/60064)中的相关能力。

 
---
### kubernetes.io/service.internetChargeType
**说明：**
负载均衡的付费类型，当前仅在创建时支持配置，创建后不支持修改付费类型，创建后修改本注解无效。
指定创建负载均衡时，负载均衡的付费类型。请配合 `kubernetes.io/service.internetMaxBandwidthOut` 注解一起使用。

**可选值：**
<table>
<tbody><tr>
<td>BANDWIDTH_POSTPAID_BY_HOUR</td>
<td>按带宽按小时后计费</td>
</tr>
<tr>
<td>TRAFFIC_POSTPAID_BY_HOUR</td>
<td>按流量按小时后计费</td>
</tr>
</tbody></table>


**使用示例：**
`kubernetes.io/service.internetChargeType: "TRAFFIC_POSTPAID_BY_HOUR"`
 
---
### kubernetes.io/service.internetMaxBandwidthOut
**说明：**
CLB 带宽设置，当前仅在创建时支持配置，创建后不支持修改带宽，创建后修改本注解无效。
指定创建负载均衡时，负载均衡的最大出带宽，仅对公网属性的 LB 生效。需配合 `kubernetes.io/service.internetChargeType` 注解一起使用。

**可选值：**
范围支持1到2048，单位 Mbps。

**使用示例：**
`kubernetes.io/service.internetMaxBandwidthOut: "2048"`
 


---
### service.cloud.tencent.com/security-groups

**说明：**
通过该 Annotation 可以为 CLB 类型的 Service 绑定安全组，单个 CLB 最多可绑定5个安全组。

**注意：**

- 请查看 CLB 使用安全组的[使用限制](https://cloud.tencent.com/document/product/214/14733)。
- 通常需要配合安全组默认放通的能力，CLB 和 CVM 之间默认放通，来自 CLB 的流量只需通过 CLB 上安全组的校验。对应 Annotation 为：`service.cloud.tencent.com/pass-to-target`
- 对于 [Service 使用已有 CLB](https://cloud.tencent.com/document/product/457/45491) 的场景，若多个 Service 声明了不同的安全组，会有逻辑冲突的问题。

**使用示例：**
`service.cloud.tencent.com/security-groups: "sg-xxxxxx,sg-xxxxxx"`

---

### service.cloud.tencent.com/pass-to-target

**说明：**
通过该 Annotation 可以为 CLB 类型的 Service 配置安全组默认放通的能力，CLB 和 CVM 之间默认放通，来自 CLB 的流量只需通过 CLB 上安全组的校验。

**注意：**

- 请查看 CLB 使用安全组的[使用限制](https://cloud.tencent.com/document/product/214/14733)。
- 通常需要配合绑定安全组的能力。对应 Annotation 为：`service.cloud.tencent.com/security-groups`
- 对于 [Service 使用已有 CLB](https://cloud.tencent.com/document/product/457/45491) 的场景，若多个 Service 声明了不同的放通配置，会有逻辑冲突的问题。



**使用示例：**
`service.cloud.tencent.com/pass-to-target: "true"`



