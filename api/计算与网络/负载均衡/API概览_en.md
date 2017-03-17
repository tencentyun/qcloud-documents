## 1. Relevant APIs for Cloud Load Balancer Instances

| API | Action ID | Description |
|---------|---------|---------|
| [Query Prices of Cloud Load Balancer Instances](/doc/api/244/1328) | InquiryLBPrice | Return the corresponding price for the cloud load balancer instance type that is entered by the user. |
| [Purchase Cloud Load Balancer](/doc/api/244/1254)  | CreateLoadBalancer | Return the unique ID of the cloud load balancer instance (*LoadBalancerId*) based on parameters entered by the user. |
| [Query List of Cloud Load Balancer Instances](/doc/api/244/1261) | DescribeLoadBalancers | Return a list of cloud load balancer instances that meet the conditions entered by the user. |
| [Modify Cloud Load Balancer Attribute Information](/doc/api/244/修改负载均衡属性信息) | ModifyLoadBalancerAttributes |  Modify the attribute information of user-specified cloud load balancer instance, such as name of the instance, etc. |
| [Query Cloud Load Balancer Instances Associated with the CVM](/doc/api/244/查询云服务器关联的负载均衡实例) | DescribeLoadBalancersByInstances | Return a list of cloud load balancer instances associated with the group of CVMs entered by the user. |
| [Delete Cloud Load Balancer Instances](/doc/api/244/删除负载均衡)| DeleteLoadBalancers | Delete the cloud load balancer instance list specified by the user. |

## 2. Relevant APIs for Cloud Load Balancer Listeners
| API | Action ID | Description |
|---------|---------|
|  [Create Cloud Load Balancer Listeners](/doc/api/244/创建负载均衡监听器)  | CreateLoadBalancerListeners | Create cloud load balancer listeners for the instance specified by the user. The cloud load balancer listener contains protocols of the requests that the user wants to forward, the port, and health check policies. |
| [Obtain Cloud Load Balancer Listener List](/doc/api/244/获取负载均衡监听器列表) | DescribeLoadBalancerListeners | Return the list of listeners of the cloud load balancer instance specified by the user. This include information such as listener's unique ID, name, port health check policy and so on. |
| [Delete Cloud Load Balancer Listeners](/doc/api/244/删除负载均衡监听器)  | DeleteLoadBalancerListeners |  Delete a group of listeners of the cloud load balancer instance specified by the user. |
| [Modify Cloud Load Balancer Listener Information](/doc/api/244/修改负载均衡监听器属性)  | ModifyLoadBalancerListener |  Modify attribute information of cloud load balancer instance listeners, such as their names and health check policies. |

## 3. Relevant APIs for Cloud Load Balancer Backend Server
| API | Action ID | Description |
|---------|---------|
| [Bind Backend Server to Cloud Load Balancer](/doc/api/244/绑定后端服务器到负载均衡) | RegisterInstancesWithLoadBalancer | Associate a group of CVMs specified by the user with the cloud load balancer instance specified by the user. |
| [Obtain List of Backend Servers Bound with Cloud Load Balancer](/doc/api/244/获取负载均衡绑定的后端服务器列表) | DescribeLoadBalancerBackends | Obtain a list of CVMs that are associated with the cloud load balancer instance *LoadBalanceId*, which is entered by the user. | 
|  [Modify Weight of Cloud Load Balancer Backend Servers](/doc/api/244/修改负载均衡器后端服务器权重) | ModifyLoadBalancerBackends | Modify [Weight of a Group of CVMs](https://www.qcloud.com/doc/product/214/%E5%8A%9F%E8%83%BD%E4%BB%8B%E7%BB%8D#1.3.-.E5.90.8E.E7.AB.AF.E6.9C.8D.E5.8A.A1.E5.99.A8.E6.9D.83.E9.87.8D.E9.85.8D.E7.BD.AE) that are associated with the cloud load balancer instance.
|  [Unbind Backend Servers](/doc/api/244/解绑后端服务器) | DeregisterInstancesFromLoadBalancer | Unbind CVMs that are associated with the cloud load balancer instance. |

## 4. Relevant APIs for Cloud Load Balancer Health Check
| API | Action ID | Description |
|---------|---------|---------|
| [Query Cloud Load Balancer Health Check Threshold](/doc/api/244/查询负载均衡健康检查阈值) | DescribeLBHealth | Query default health check parameters for the cloud load balancer instance. |
| [Query Cloud Load Balancer Health Check Status](/doc/api/244/查询负载均衡健康检查状态) | DescribeLBHealthStatus | Query default health status for the cloud load balancer instance. |
| [Modify Cloud Load Balancer Health Check Attributes](/doc/api/244/修改负载均衡健康检查属性) | ModifyLBHealth| Modify default health check attribute information for the cloud load balancer instance. |

## 5. Relevant APIs for Cloud Load Balancer Monitoring
| API | Action ID | Description |
|---------|---------|
| [Monitor Cloud Load Balancer](https://www.qcloud.com/doc/api/244/%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1%E7%9B%91%E6%8E%A7%E6%8E%A5%E5%8F%A3) | GetMonitorData | Acquire information related to the traffic and bandwidth of the cloud load balancer instance. | 


## 6. General APIs for Cloud Load Balancer
| API | Action ID | Description |
|---------|---------|
| [Query the Operation Result of Cloud Load Balancer Asynchronous APIs](/doc/api/244/4007) | DescribeLoadBalancersTaskResult | Query the operation result of cloud load balancer asynchronous task APIs. |



