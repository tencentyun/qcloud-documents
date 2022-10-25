您可以通过以下 Annotation 注解配置 Ingress，以实现更丰富的负载均衡的能力。

## 注解使用方式

```yaml
apiVersion: 
kind: Ingress
metadata:
    annotations:  
      kubernetes.io/ingress.class: "qcloud"
    name: test
........
```

## Annotation 集合



### kubernetes.io/ingress.class

   
**说明：**
配置 Ingress 类型。当前组件管理未配置该注解，或注解内容为 qcloud 的 Ingress 资源。  		 

**使用示例：**
`kubernetes.io/ingress.class: "qcloud"`
 
--- 
### kubernetes.io/ingress.qcloud-loadbalance-id
   
**说明：**
只读注解，组件提供当前 Ingress 引用的负载均衡 LoadBalanceId。
  
   
**使用示例：**
`kubernetes.io/ingress.qcloud-loadbalance-id: "lb-3imskkfe"`
 
--- 
### ingress.cloud.tencent.com/loadbalance-nat-ipv6
   
**说明：**
只读注解，当用户配置或申请的为 NAT IPv6负载均衡时，提供 IPv6地址。
 
--- 
### ingress.cloud.tencent.com/loadbalance-ipv6
   
**说明：**
只读注解，当用户配置或申请的为 FullStack IPv6负载均衡时，提供 IPv6地址。
 
--- 
### kubernetes.io/ingress.internetChargeType
   
**说明：**
负载均衡的付费类型，当前仅在创建时支持配置，创建后不支持修改付费类型，创建后修改本注解无效。
指定创建负载均衡时，负载均衡的付费类型。请配合 `kubernetes.io/ingress.internetMaxBandwidthOut` 注解一起使用。     

**可选值：**
- TRAFFIC_POSTPAID_BY_HOUR 按流量按小时后计费。  
- BANDWIDTH_POSTPAID_BY_HOUR 按带宽按小时后计费。       
   
**使用示例：**
`kubernetes.io/ingress.internetChargeType: "TRAFFIC_POSTPAID_BY_HOUR"`
 
--- 
### kubernetes.io/ingress.internetMaxBandwidthOut

   
**说明：**
CLB 带宽设置，当前仅在创建时支持配置，创建后不支持修改带宽，创建后修改本注解无效。
指定创建负载均衡时，负载均衡的最大出带宽，仅对公网属性的 LB 生效。需配合 `kubernetes.io/ingress.internetChargeType` 注解一起使用。

**可选值：**
范围支持1到2048，单位 Mbps。


   
**使用示例：**
`kubernetes.io/ingress.internetMaxBandwidthOut: "2048"`
 
--- 
### kubernetes.io/ingress.extensiveParameters
   
**说明：**
该 Annotation 使用的是 CLB 创建时的参数，当前仅在创建时支持配置，创建后不支持修改，创建后修改本注解无效。
参考 [创建负载均衡实例](https://cloud.tencent.com/document/product/214/30692#4.-.E7.A4.BA.E4.BE.8B) 为创建负载均衡追加自定义参数。  		 

**使用示例：**
- 创建 NAT64 IPv6 实例：
  `kubernetes.io/ingress.extensiveParameters: '{"AddressIPVersion":"IPV6"}'`
- 创建 IPv6 实例：
  `kubernetes.io/ingress.extensiveParameters: '{"AddressIPVersion":"IPv6FullChain"}'`
- 购买电信负载均衡：
  `kubernetes.io/ingress.extensiveParameters: '{"VipIsp":"CTCC"}'`
- 指定可用区创建：
  `kubernetes.io/ingress.extensiveParameters: '{"ZoneId":"ap-guangzhou-1"}'`
- 创建时自定义 CLB 名字：
  `kubernetes.io/ingress.extensiveParameters: '{"LoadBalancerName":"my_cutom_lb_name"}'`
 
--- 
### kubernetes.io/ingress.subnetId
   
**说明：**
指定创建内网类型的负载均衡，并指定负载均衡所属子网。  		 

**使用示例：**
`kubernetes.io/ingress.subnetId: "subnet-3swgntkk"`
 
--- 
### kubernetes.io/ingress.existLbId
   
**说明：**
指定使用已有负载均衡作为接入层入口资源。
>! 使用已有负载均衡时，需要保证其不包含其他监听器。



   
**使用示例：**
`kubernetes.io/ingress.existLbId: "lb-342wppll"`
 
--- 
### kubernetes.io/ingress.rule-mix: 
### kubernetes.io/ingress.http-rules: 
### kubernetes.io/ingress.https-rules:
   
**说明：**
支持配置混合协议，支持转发路径同时在 HTTP 和 HTTPS 上进行转发。支持手动配置重定向规则。  	

**使用示例：**
使用方式详情见 [Ingress 混合使用 HTTP 及 HTTPS 协议](https://cloud.tencent.com/document/product/457/45693)。
 
--- 
### ingress.cloud.tencent.com/direct-access
   
**说明：**
支持七层直连用户负载均衡。需要注意在各种不同的网络下，直连接入的服务依赖。  		 

**使用示例：**
使用方式详情见 [使用 LoadBalancer 直连 Pod 模式 Service](https://cloud.tencent.com/document/product/457/41897)。
 
--- 
### ingress.cloud.tencent.com/tke-service-config
   
**说明：**
通过 tke-service-config 配置负载均衡相关配置，包括监听器、转发规则等。  		 

**使用示例：**
`ingress.cloud.tencent.com/tke-service-config: "nginx-config"`，详情可参见 [Ingress 使用 TkeServiceConfig 配置 CLB](https://cloud.tencent.com/document/product/457/45700)。
 
--- 
### ingress.cloud.tencent.com/tke-service-config-auto
   
**说明：**
通过该注解可自动创建 TkeServiceConfig 资源，并提供配置的模板，用户可以按需进行配置。  		

**使用示例：**
`ingress.cloud.tencent.com/tke-service-config-auto: "true"`，详情可参见 [Ingress 使用 TkeServiceConfig 配置 CLB](https://cloud.tencent.com/document/product/457/45700)。
 
--- 
### ingress.cloud.tencent.com/rewrite-support
   
**说明：**
- 可以配合 `kubernetes.io/ingress.http-rules`、`kubernetes.io/ingress.https-rules` 实现手动重定向能力。
- 可以配合 `ingress.cloud.tencent.com/auto-rewrite` 实现自动重定向能力。
   
**使用示例：**
`ingress.cloud.tencent.com/rewrite-support: "true"`
 
--- 
### ingress.cloud.tencent.com/auto-rewrite
   
**说明：**
为 HTTP 端口提供自动重定向能力，所有在 HTTPS 端口声明的转发规则都会创建对应的重定向规则。需要配合 `ingress.cloud.tencent.com/rewrite-support` 注解开启重定向的管理能力。  		 

**使用示例：**
`ingress.cloud.tencent.com/auto-rewrite: "true"`
 
--- 
### ingress.cloud.tencent.com/cross-region-id
   
**说明：**
Ingress 跨域绑定功能，指定需要从哪个地域接入。需要和 `kubernetes.io/ingress.existLbId`或`ingress.cloud.tencent.com/cross-vpc-id` 配合使用。  		 

**使用示例：**
- 创建异地接入的负载均衡：
  `ingress.cloud.tencent.com/cross-region-id: "ap-guangzhou"`
  `ingress.cloud.tencent.com/cross-vpc-id: "vpc-646vhcjj"`
- 选择已有负载均衡进行异地接入：
  `ingress.cloud.tencent.com/cross-region-id: "ap-guangzhou"`
  `kubernetes.io/ingress.existLbId: "lb-342wppll"`
 
--- 
### ingress.cloud.tencent.com/cross-vpc-id
   
**说明：**
Ingress 跨域绑定功能，指定需要接入的 VPC。可以和 `ingress.cloud.tencent.com/cross-region-id` 注解配合指定其他地域 VPC。
>! 适用于 TKE 创建并管理的负载均衡，对使用已有负载均衡的场景该注解无效。
>

   
**使用示例：**
创建异地接入的负载均衡：
`ingress.cloud.tencent.com/cross-region-id: "ap-guangzhou"`
`ingress.cloud.tencent.com/cross-vpc-id: "vpc-646vhcjj"`
 
--- 
### ingress.cloud.tencent.com/enable-grace-shutdown
   
**说明：**
支持 CLB 直连模式的优雅停机。Pod 被删除，此时 Pod 里有 DeletionTimestamp，且状态置为 Terminating。此时调整 CLB 到该 Pod 的权重为 0。 

**使用示例：**
仅在直连模式下支持，需要配合使用 `ingress.cloud.tencent.com/direct-access`，使用方式详情见 [Ingress 优雅停机](https://cloud.tencent.com/document/product/457/60065)。

---
### ingress.cloud.tencent.com/enable-grace-shutdown-tkex
**说明：**
支持 CLB 直连模式的优雅退出。Endpoint 对象中 endpoints 是否 not-ready，将 not-ready 的 CLB 后端权重置为 0。

**使用示例：**
仅在直连模式下支持，需要配合使用 `ingress.cloud.tencent.com/direct-access`，使用方式详情见 [Ingress 优雅停机](https://cloud.tencent.com/document/product/457/60065)中的相关能力。

---
### ingress.cloud.tencent.com/security-groups

**说明：**
通过该 Annotation 可以为 CLB 类型的 Ingress 绑定安全组，单个 CLB 最多可绑定5个安全组。

**注意：**
- 请查看 CLB 使用安全组的[使用限制](https://cloud.tencent.com/document/product/214/14733)。
- 通常需要配合安全组默认放通的能力，CLB 和 CVM 之间默认放通，来自 CLB 的流量只需通过 CLB 上安全组的校验。对应 Annotation 为：`ingress.cloud.tencent.com/pass-to-target`

**使用示例：**
`ingress.cloud.tencent.com/security-groups: "sg-xxxxxx,sg-xxxxxx"`

---

### ingress.cloud.tencent.com/pass-to-target 

**说明：**
通过该 Annotation 可以为 CLB 类型的 Ingress 配置安全组默认放通的能力，CLB 和 CVM 之间默认放通，来自 CLB 的流量只需通过 CLB 上安全组的校验。

**注意：**

- 请查看 CLB 使用安全组的[使用限制](https://cloud.tencent.com/document/product/214/14733)。
- 通常需要配合绑定安全组的能力。对应 Annotation 为：`ingress.cloud.tencent.com/security-groups`

**使用示例：**
`ingress.cloud.tencent.com/pass-to-target: "true"`
