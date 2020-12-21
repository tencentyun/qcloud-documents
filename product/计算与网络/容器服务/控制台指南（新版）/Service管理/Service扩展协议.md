##  Service默认支持的协议

 Service是Kubernetes暴露应用程序到集群外的一种机制与抽象， 可以通过Serivce访问集群内的应用程序。

默认情况下Service在协议上支持：

- ClusterIP和NodePort模式下可以支持TCP/UDP协议，并支持混合使用。
- LoadBalancer模式下支持TCP或UDP协议， 不支持混合使用。



## TKE 扩展Service转发协议

在原生的Service支持的协议的规则上， 存在部分场景需要在Service上同时支持TCP和UDP混合， 期望Service能够支持TCP SSL、HTTP、HTTPS协议。 

TKE针对LoadBalancer模式扩展了更多协议的支持。



### 前置说明

1. 扩展协议仅对LoadBalancer模式的Service生效。
2. 扩展协议通过注解annatition的形式描述协议与端口的关系。
3. 扩展协议与注解annatition关系如下：
   1. 当扩展协议注解中没有覆盖Service Spec中描述的端口时，Service Spec按照用户描述配置。
   2. 当扩展协议注解中描述的端口在Service Spec中不存在时，忽略该配置。
   3. 当注展协议解中描述的端口在Service Spec中存在时，覆盖用户在Service Spec中声明的协议配置。
4. TCP SSL是负载均衡器内测功能，需要提交工单申请。



### 扩展协议使用说明

```yaml
apiVersion: v1
kind: Service
metadata:
  annotations:  
    service.cloud.tencent.com/specify-protocol: {"80":{"protocol":["TCP_SSL"],"tls":"cert-secret"}}
  name: test
 ....
```

注解名称：service.cloud.tencent.com/specify-protocol

扩展的协议注解示例：

- TCP SSL示例
  - {"80":{"protocol":["TCP_SSL"],"tls":"cert-secret"}}
- HTTP示例
  - {"80":{"protocol":["HTTP"],"hosts":{"[a.tencent.com](http://a.tencent.com/)":{},"[b.tencent.com](http://b.tencent.com/)":{}}}}
- HTTPS示例
  - {"80":{"protocol":["HTTPS"],"hosts":{"[a.tencent.com](http://a.tencent.com/)":{"tls":"cert-secret-a"},"[b.tencent.com](http://b.tencent.com/)":{"tls":"cert-secret-b"}}}}
- 混合示例
  - {"80":{"protocol":["TCP","UDP"]}}
  - {"80":{"protocol":["TCP_SSL","UDP"],"tls":"cert-secret"}}
