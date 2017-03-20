## 1. 负载均衡实例相关接口

| 接口名 | Action ID | 功能描述 |
|---------|---------|---------|
| [查询负载均衡实例价格](/doc/api/244/1328) | InquiryLBPrice | 根据用户输入的负载均衡实例类型，返回相应类型负载均衡实例的价格。|
| [购买负载均衡](/doc/api/244/1254)  | CreateLoadBalancer | 根据用户输入的参数，返回负载均衡实例的唯一ID，即 *LoadBalancerId*。|
| [查询负载均衡实例列表](/doc/api/244/1261) | DescribeLoadBalancers | 根据用户的输入返回符合条件的负载均衡实例列表。|
| [修改负载均衡属性信息](/doc/api/244/修改负载均衡属性信息) | ModifyLoadBalancerAttributes |  修改用户指定的负载均衡实例的属性信息，包括负载均衡实例的名字等。|
| [查询云服务器关联的负载均衡实例](/doc/api/244/查询云服务器关联的负载均衡实例) | DescribeLoadBalancersByInstances | 根据用户输入的一组云服务器，返回这组云服务器关联的负载均衡实例列表。|
| [删除负载均衡实例](/doc/api/244/删除负载均衡)| DeleteLoadBalancers | 删除用户指定的负载均衡实例列表。|

## 2. 负载均衡监听器相关接口
| 接口名 | Action ID | 功能描述 |
|---------|---------|
|  [创建负载均衡监听器](/doc/api/244/创建负载均衡监听器)  | CreateLoadBalancerListeners | 为用户指定的负载均衡实例创建负载均衡监听器。负载均衡监听器包含了客户要转发请求的协议，端口以及健康检查的策略。|
| [获取负载均衡监听器列表](/doc/api/244/获取负载均衡监听器列表) | DescribeLoadBalancerListeners | 返回用户指定的负载均衡实例的监听器列表。包含监听器的唯一ID，名字，端口健康检查策略等信息。|
| [删除负载均衡监听器](/doc/api/244/删除负载均衡监听器)  | DeleteLoadBalancerListeners |  删除用户指定的负载均衡实例的一组监听器。|
| [修改负载均衡监听器属性](/doc/api/244/修改负载均衡监听器属性)  | ModifyLoadBalancerListener |  修改负载均衡实例的监听器的属性信息，包括监听器的名字，健康检查策略等信息。|

## 3. 负载均衡后端服务器相关接口
| 接口名 | Action ID | 功能描述 |
|---------|---------|
| [绑定后端服务器到负载均衡](/doc/api/244/绑定后端服务器到负载均衡) | RegisterInstancesWithLoadBalancer | 将用户指定的一组云服务器关联到用户指定的负载均衡实例上。|
| [获取负载均衡绑定的后端服务器列表](/doc/api/244/获取负载均衡绑定的后端服务器列表) | DescribeLoadBalancerBackends | 获取用户输入的 *LoadBalanceId* 这个负载均衡实例上关联的云服务器列表。| 
|  [修改负载均衡后端服务器权重](/doc/api/244/修改负载均衡器后端服务器权重) | ModifyLoadBalancerBackends | 修改关联到负载均衡实例的一组[云服务器的权重](https://www.qcloud.com/doc/product/214/%E5%8A%9F%E8%83%BD%E4%BB%8B%E7%BB%8D#1.3.-.E5.90.8E.E7.AB.AF.E6.9C.8D.E5.8A.A1.E5.99.A8.E6.9D.83.E9.87.8D.E9.85.8D.E7.BD.AE)。
|  [解绑后端服务器](/doc/api/244/解绑后端服务器) | DeregisterInstancesFromLoadBalancer | 将关联到负载均衡实例的云服务器进行解绑操作。|

## 4. 负载均衡健康检查相关接口
| 接口名 | Action ID | 功能描述 |
|---------|---------|---------|
| [查询负载均衡健康检查阈值](/doc/document/api/214/1326) | DescribeLBHealth | 查询负载均衡实例默认的健康检查参数。|
| [查询负载均衡健康检查状态](/doc/api/244/查询负载均衡健康检查状态) | DescribeLBHealthStatus | 查询负载均衡实例默认的健康状态。|
| [修改负载均衡健康检查属性](/doc/api/244/修改负载均衡健康检查属性) | ModifyLBHealth | 修改负载均衡实例默认的健康检查属性信息。|

## 5. 负载均衡监控相关接口
| 接口名 | Action ID | 功能描述 |
|---------|---------|
| [监控负载均衡](https://www.qcloud.com/doc/api/244/%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1%E7%9B%91%E6%8E%A7%E6%8E%A5%E5%8F%A3) | GetMonitorData | 获取负载均衡实例关于流量以及带宽的相关信息。| 


## 6. 负载均衡通用接口
| 接口名 | Action ID | 功能描述 |
|---------|---------|
| [查询负载均衡异步接口的执行结果](/doc/api/244/4007) | DescribeLoadBalancersTaskResult | 查询负载均衡异步操作接口的执行结果。|


