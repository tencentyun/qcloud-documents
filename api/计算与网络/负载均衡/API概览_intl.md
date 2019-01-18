## Common Load Balancer-Related APIs
This kind of APIs are applicable to the traditional and application-based load balancers:

| API | Action | Description |
|---------|---------|---------|
| [Query Load Balancer Instance Price](https://cloud.tencent.com/document/api/214/1328) | InquiryLBPrice | Query the price of load balancer instance. |
| [Purchase Load Balancer](https://cloud.tencent.com/document/api/214/1254) | CreateLoadBalancer | Used to purchase a load balancer. |
| [Query Load Balancer Instance List](https://cloud.tencent.com/document/api/214/1261) | DescribeLoadBalancers | Query the list of load balancer instances. |
| [Delete Load Balancer Instance](https://cloud.tencent.com/document/api/214/1257) | DeleteLoadBalancers | Delete a load balancer instance. |
| [Query Result of Load Balancer Asynchronous API](https://cloud.tencent.com/document/product/214/4007) | DescribeLoadBalancersTaskResult | Query the result of executing load balancer asynchronous API. |
| [Query Load Balancer Associated with Certificate](https://cloud.tencent.com/document/product/214/6046) | GetCertListWithLoadBalancer | Query the information of load balancer associated with a certificate. |
| [Query Load Balancer Application-Layer Log](https://cloud.tencent.com/document/product/214/12235) | DescribeLoadBalancerLog | Query the application-layer log of a load balancer. |
| [Query Load Balancer Monitoring Data](https://cloud.tencent.com/document/product/214/8801) | GetMonitorData | Query the monitoring data of a load balancer. |
| [Replace Load Balancer Certificate](https://cloud.tencent.com/document/product/214/6045) | ReplaceCert | Replace the certificate of a load balancer. |

## Traditional Load Balancer-Related APIs
### Listener-related APIs
| API | Action | Description |
|---------|---------|
| [Create Load Balancer Listener](https://cloud.tencent.com/document/api/214/1255) | CreateLoadBalancerListeners | Create listeners for the specified load balancer instance. The load balancer listeners contain the protocols for the requests to be forwarded, as well as ports and health check policies. |
| [Obtain Load Balancer Listener List](https://cloud.tencent.com/document/api/214/1260) | DescribeLoadBalancerListeners | Return the list of listeners for the specified load balancer instances. This include the listeners' unique IDs, names, ports, health check policies, and other information. |
| [Delete Load Balancer Listener](https://cloud.tencent.com/document/api/214/1256) | DeleteLoadBalancerListeners | Delete a set of listeners for the specified load balancer instance. |
|[Modify Load Balancer Listener Attributes](https://cloud.tencent.com/document/api/214/3601)  |  ModifyLoadBalancerListener | Modify the attributes of the listener for the specified load balancer instance, including the listener name, health check policy and other information. |

### Backend CVM-related APIs
| API | Action | Description |
|---------|---------|
| [Bind Backend CVM to Load Balancer](https://cloud.tencent.com/document/api/214/1265) | RegisterInstancesWithLoadBalancer | Bind a set of specified CVMs to the specified load balancer instance. |
| [Obtain List of Backend CVMs Bound to Load Balancer](https://cloud.tencent.com/document/api/214/1259) | DescribeLoadBalancerBackends | Obtain the list of CVMs bound to the load balancer instance identified by *LoadBalanceId*. | 
| [Modify Weight of Load Balancer's Backend CVMs](https://cloud.tencent.com/document/api/214/1264) | ModifyLoadBalancerBackends | Modify the [weights of a set of CVMs](https://cloud.tencent.com/doc/product/214/%E5%8A%9F%E8%83%BD%E4%BB%8B%E7%BB%8D#1.3.-.E5.90.8E.E7.AB.AF.E6.9C.8D.E5.8A.A1.E5.99.A8.E6.9D.83.E9.87.8D.E9.85.8D.E7.BD.AE) bound to the load balancer instance.
| [Unbind Backend CVM](https://cloud.tencent.com/document/api/214/1258) | DeregisterInstancesFromLoadBalancer | Unbind CVMs from the load balancer instance. |

### Health check-related APIs
| API | Action | Description |
|---------|---------|---------|
| [Query Load Balancer Health Check Status](https://cloud.tencent.com/document/product/214/1326) | DescribeLBHealthStatus | Query the health status of a load balancer instance. |


### Instance-related APIs
| API | Action | Description |
|---------|---------|
| [Modify Load Balancer Attributes](https://cloud.tencent.com/document/product/214/1263) | ModifyLoadBalancerAttributes | Modify the attributes of the specified load balancer instance, including the load balancer instance name. |


## Application-Based Load Balancer-Related APIs


### Instance-related APIs
| API | Action | Description |
|---------|---------|
| [Modify Application-Based Load Balancer Name](https://cloud.tencent.com/document/product/214/10008) | ModifyForwardLBName | Modify the name of an application-based load balancer. |

### Listener-related APIs
| API | Action | Description |
|---------|---------|
| [Query Application-Based Load Balancer Listener](https://cloud.tencent.com/document/product/214/9005) | DescribeForwardLBListeners | Query the listeners of an application-based load balancer. |
| [Create Application-Based Load Balancer Layer-7 Listener](https://cloud.tencent.com/document/product/214/9000) | CreateForwardLBSeventhLayerListeners | Create a layer-7 listener for an application-based load balancer. | 
| [Modify Application-Based Load Balancer Layer-7 Listener Attributes ](https://cloud.tencent.com/document/product/214/8997) | ModifyForwardLBSeventhListener | Modify the attributes of the layer-7 listener of an application-based load balancer. | 
| [Create Application-Based Load Balancer Layer-4 Listener](https://cloud.tencent.com/document/product/214/9001) | CreateForwardLBFourthLayerListeners | Create a layer-4 listener for an application-based load balancer. |
| [Modify Application-Based Load Balancer Layer-4 Listener Attributes](https://cloud.tencent.com/document/product/214/8998) | ModifyForwardLBFourthListener | Modify the attributes of the layer-4 listener of an application-based load balancer. | 
| [Delete Application-Based Load Balancer Listener](https://cloud.tencent.com/document/product/214/9004) | DeleteForwardLBListener | Delete the listener of an application-based load balancer. |

### Forwarding rule-related APIs
| API | Action | Description |
|---------|---------|
| [Create Application-Based Load Balancer Layer-7 Listener Forwarding Rules](https://cloud.tencent.com/document/product/214/9011) | CreateForwardLBListenerRules | Create forwarding rules for the layer-7 listener of an application-based load balancer. |
| [Modify Domain Name Under Application-Based Load Balancer Layer-7 Listener](https://cloud.tencent.com/document/product/214/9007) | ModifyForwardLBRulesDomain | Modify the domain name under the layer-7 listener of an application-based load balancer. |
| [Modify Health Check and Forwarding Path of Application-Based Load Balancer Layer-7 Listener Forwarding Rules](https://cloud.tencent.com/document/product/214/9008) | ModifyLoadBalancerRulesProbe | Modify the health check and forwarding path for the forwarding rules of layer-7 listener of an application-based load balancer. | 
| [Delete Application-Based Load Balancer Layer-7 Listener Forwarding Rules](https://cloud.tencent.com/document/product/214/9012) | DeleteForwardLBListenerRules | Delete the forwarding rules of the layer-7 listener of an application-based load balancer. | 

### Health check-related APIs
| API | Action | Description |
|---------|---------|
| [Query Application-Based Load Balancer Instance Health Check](https://cloud.tencent.com/document/product/214/8995) | DescribeForwardLBHealthStatus | Query the health check of an application-based load balancer instance. |


## CVM-Related APIs
| API | Action | Description |
|---------|---------|
| [Query List of CVMs Bound to Application-Based Load Balancer](https://cloud.tencent.com/document/product/214/8987) | DescribeForwardLBBackends | Query the list of CVMs bound to an application-based load balancer. |
| [Bind CVM to Application-Based Load Balancer Layer-7 Listener Forwarding Rules](https://cloud.tencent.com/document/product/214/8988) | RegisterInstancesWithForwardLBSeventhListener | Bind a CVM to the forwarding rules of layer-7 listener of an application-based load balancer. |
| [Unbind CVM from Application-Based Load Balancer Layer-7 Listener Forwarding Rules](https://cloud.tencent.com/document/product/214/8991) | DeregisterInstancesFromForwardLB | Unbind a CVM from the forwarding rules of layer-7 listener of an application-based load balancer. |
| [Modify Port of CVM Bound to Layer-7 Listener](https://cloud.tencent.com/document/product/214/8979) | ModifyForwardSeventhBackendsPort | Modify the port of a CVM bound to the layer-7 listener. |
| [Modify Weight of CVM Bound to Layer-7 Listener](https://cloud.tencent.com/document/product/214/8978) | ModifyForwardSeventhBackends | Modify the weight of a CVM bound to the layer-7 listener. |
| [Bind CVM to Application-Based Load Balancer Layer-4 Listener](https://cloud.tencent.com/document/product/214/8989) | RegisterInstancesWithForwardLBFourthListener | Bind a CVM to the layer-4 listener of an application-based load balancer. |
| [Unbind CVM from Application-Based Load Balancer Layer-4 Listener](https://cloud.tencent.com/document/product/214/8992) | DeregisterInstancesFromForwardLBFourthListener | Unbind a CVM from the layer-4 listener of an application-based load balancer. |
| [Modify Port of CVM Bound to Layer-4 Listener](https://cloud.tencent.com/document/product/214/8984) | ModifyForwardFourthBackendsPort | Modify the port of a CVM bound to the layer-4 listener. |
| [Modify Weight of CVM Bound to Layer-4 Listener](https://cloud.tencent.com/document/product/214/8981) | ModifyForwardFourthBackendsWeight | Modify the weight of a CVM bound to the layer-4 listener. |


### Redirect-related APIs
| API | Action | Description |
|---------|---------|
| [Query Application-Based Load Balancer Redirect Relationship](https://cloud.tencent.com/document/product/214/9016) | DescribeRewrite | Query the redirect relationship of an application-based load balancer. |
| [Delete Application-Based Load Balancer Redirect Relationship](https://cloud.tencent.com/document/product/214/9014)| DeleteRewrite | Delete the redirect relationship of an application-based load balancer. |
| [Add Application-Based Load Balancer Redirect Relationship Manually](https://cloud.tencent.com/document/product/214/9015) | ManualRewrite | Add redirect relationship for an application-based load balancer manually. |
| [Generate Application-Based Load Balancer Redirect Relationship Automatically ](https://cloud.tencent.com/document/product/214/9017) | AutoRewrite | Generate the redirect relationship for an application-based load balancer automatically. |





