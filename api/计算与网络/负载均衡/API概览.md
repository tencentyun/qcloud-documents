## 通用负载均衡相关接口
该部分接口适用于传统型和应用型负载均衡：

| 接口名 | Action | 功能描述 |
|---------|---------|---------|
| [查询负载均衡实例价格](https://cloud.tencent.com/document/api/214/1328) | InquiryLBPrice | 查询负载均衡实例的价格。|
| [购买负载均衡](https://cloud.tencent.com/document/api/214/1254)  | CreateLoadBalancer | 通过该接口来购买负载均衡。|
| [查询负载均衡实例列表](https://cloud.tencent.com/document/api/214/1261) | DescribeLoadBalancers | 查询负载均衡实例的列表。|
| [删除负载均衡实例](https://cloud.tencent.com/document/api/214/1257)| DeleteLoadBalancers | 删除负载均衡实例。|
| [查询负载均衡异步接口的执行结果](https://cloud.tencent.com/document/product/214/4007) | DescribeLoadBalancersTaskResult | 查询负载均衡异步操作接口的执行结果。|
| [查询证书关联的负载均衡信息](https://cloud.tencent.com/document/product/214/6046)| GetCertListWithLoadBalancer | 查询证书关联的负载均衡信息。|
| [查询负载均衡应用层日志](https://cloud.tencent.com/document/product/214/12235)| DescribeLoadBalancerLog | 查询负载均衡应用层日志。|
| [查询负载均衡的监控数据](https://cloud.tencent.com/document/product/214/8801)|GetMonitorData|查询负载均衡的监控数据。|
| [更换负载均衡的证书](https://cloud.tencent.com/document/product/214/6045)|ReplaceCert|更换负载均衡使用的证书。|

## 传统型负载均衡相关接口
### 监听器相关接口

| 接口名 | Action | 功能描述 |
|---------|---------| ---------
|  [创建负载均衡监听器](https://cloud.tencent.com/document/api/214/1255)  | CreateLoadBalancerListeners | 为用户指定的负载均衡实例创建负载均衡监听器。负载均衡监听器包含了客户要转发请求的协议，端口以及健康检查的策略。|
| [获取负载均衡监听器列表](https://cloud.tencent.com/document/api/214/1260) | DescribeLoadBalancerListeners | 返回用户指定的负载均衡实例的监听器列表。包含监听器的唯一 ID，名字，端口健康检查策略等信息。|
| [删除负载均衡监听器](https://cloud.tencent.com/document/api/214/1256)  | DeleteLoadBalancerListeners |  删除用户指定的负载均衡实例的一组监听器。|
| [修改负载均衡监听器属性](https://cloud.tencent.com/document/api/214/3601)  | ModifyLoadBalancerListener |  修改负载均衡实例的监听器的属性信息，包括监听器的名字，健康检查策略等信息。|

### 后端服务器相关接口

| 接口名 | Action| 功能描述 |
|---------| ---------| ---------
| [绑定后端服务器到负载均衡](https://cloud.tencent.com/document/api/214/1265) | RegisterInstancesWithLoadBalancer | 将用户指定的一组云服务器关联到用户指定的负载均衡实例上。|
| [获取负载均衡绑定的后端服务器列表](https://cloud.tencent.com/document/api/214/1259) | DescribeLoadBalancerBackends | 获取用户输入的 *LoadBalanceId* 这个负载均衡实例上关联的云服务器列表。| 
|  [修改负载均衡后端服务器权重](https://cloud.tencent.com/document/api/214/1264) | ModifyLoadBalancerBackends | 修改关联到负载均衡实例的一组 [云服务器的权重](https://cloud.tencent.com/doc/product/214/%E5%8A%9F%E8%83%BD%E4%BB%8B%E7%BB%8D#1.3.-.E5.90.8E.E7.AB.AF.E6.9C.8D.E5.8A.A1.E5.99.A8.E6.9D.83.E9.87.8D.E9.85.8D.E7.BD.AE)。
|  [解绑后端服务器](https://cloud.tencent.com/document/api/214/1258) | DeregisterInstancesFromLoadBalancer | 将关联到负载均衡实例的云服务器进行解绑操作。|

### 健康检查相关接口

| 接口名 | Action | 功能描述 |
|---------|---------|---------|
| [查询负载均衡健康检查状态](https://cloud.tencent.com/document/product/214/1326) | DescribeLBHealthStatus | 查询负载均衡实例健康状态。|


### 实例相关接口

| 接口名 | Action | 功能描述 |
|---------|---------| ---------
| [修改负载均衡属性信息](https://cloud.tencent.com/document/product/214/1263) | ModifyLoadBalancerAttributes |  修改用户指定的负载均衡实例的属性信息，包括负载均衡实例的名字等。|


## 应用型负载均衡相关接口


### 实例相关接口

| 接口名 | Action | 功能描述 |
|---------|---------| ---------
|  [修改应用型型负载均衡的名称](https://cloud.tencent.com/document/product/214/13295) | ModifyForwardLBName | 修改应用型型负载均衡的名称。|

### 监听器相关接口

| 接口名 | Action ID | 功能描述 |
|---------|---------| ---------
| [查询应用型负载均衡监听器](https://cloud.tencent.com/document/product/214/9005) | DescribeForwardLBListeners | 查询应用型负载均衡监听器。|
| [创建应用型负载均衡七层监听器](https://cloud.tencent.com/document/product/214/9000) | CreateForwardLBSeventhLayerListeners |创建应用型七层监听器。| 
| [修改应用型负载均衡七层监听器属性](https://cloud.tencent.com/document/product/214/8997) | ModifyForwardLBSeventhListener |修改应用型负载均衡七层监听器属性。| 
| [创建应用型负载均衡四层监听器](https://cloud.tencent.com/document/product/214/9001) | CreateForwardLBFourthLayerListeners |创建应用型四层监听器。|
| [修改应用型负载均衡四层监听器属性](https://cloud.tencent.com/document/product/214/8998) | ModifyForwardLBFourthListener |修改应用型负载均衡四层监听器属性。| 
| [删除应用型负载均衡监听器](https://cloud.tencent.com/document/product/214/9004) | DeleteForwardLBListener |删除应用型负载均衡监听器。|

### 转发规则相关接口

| 接口名 | Action ID | 功能描述 |
|---------|---------| ---------
| [创建应用型负载均衡七层监听器转发规则的能力](https://cloud.tencent.com/document/product/214/9011) | CreateForwardLBListenerRules |创建应用型负载均衡七层监听器转发规则的能力。|
| [修改应用型负载均衡七层监听器下的域名](https://cloud.tencent.com/document/product/214/9007) | ModifyForwardLBRulesDomain | 修改应用型负载均衡七层监听器下的域名。|
|[ 修改应用型负载均衡七层监听器转发规则的健康检查及转发路径](https://cloud.tencent.com/document/product/214/9008) | ModifyLoadBalancerRulesProbe |修改应用型负载均衡七层监听器转发规则的健康检查及转发路径。| 
| [删除应用型负载均衡实例七层监听器的转发规则](https://cloud.tencent.com/document/product/214/9012) | DeleteForwardLBListenerRules |删除应用型负载均衡实例七层监听器的转发规则。| 

### 健康检查相关接口

| 接口名 | Action ID | 功能描述 |
|---------|---------| ---------
| [查询应用型负载均衡实例的健康检查](https://cloud.tencent.com/document/product/214/8995) | DescribeForwardLBHealthStatus | 查询应用型负载均衡实例的健康检查。|


### 云服务器相关接口

| 接口名 | Action ID | 功能描述 |
|---------|---------| ---------
| [查询应用型负载均后端绑定的云服务器器列表](https://cloud.tencent.com/document/product/214/8987) | DescribeForwardLBBackends | 查询应用型负载均后端绑定的云服务器器列表。|
| [绑定云服务器到应用型负载均衡七层监听器的转发规则](https://cloud.tencent.com/document/product/214/8988) | RegisterInstancesWithForwardLBSeventhListener | 绑定云服务器到应用型负载均衡七层监听器的转发规则。|
| [解绑云服务器从应用型负载均衡七层监听器的转发规则](https://cloud.tencent.com/document/product/214/8991) | DeregisterInstancesFromForwardLB | 解绑云服务器从应用型负载均衡七层监听器的转发规则。|
| [修改绑定到七层监听器的云服务器的端口](https://cloud.tencent.com/document/product/214/8979) | ModifyForwardSeventhBackendsPort | 修改绑定到七层监听器的云服务器的端口。|
| [修改绑定到七层监听器的云服务器的权重](https://cloud.tencent.com/document/product/214/8978) | ModifyForwardSeventhBackends | 修改绑定到七层监听器的云服务器的权重。|
| [绑定云服务器到应用型负载均衡四层监听器](https://cloud.tencent.com/document/product/214/8989) | RegisterInstancesWithForwardLBFourthListener | 绑定云服务器到应用型负载均衡四层监听器。|
| [解绑云服务器从应用型负载均衡四层监听器](https://cloud.tencent.com/document/product/214/8992) | DeregisterInstancesFromForwardLBFourthListener | 解绑云服务器从应用型负载均衡四层监听器。|
| [修改绑定到四层监听器的云服务器的端口](https://cloud.tencent.com/document/product/214/8984) | ModifyForwardFourthBackendsPort | 修改绑定到四层监听器的云服务器的端口。|
|[ 修改绑定到四层监听器的云服务器的权重](https://cloud.tencent.com/document/product/214/8981) | ModifyForwardFourthBackendsWeight | 修改绑定到四层监听器的云服务器的权重。|


### 重定向相关接口

| 接口名 | Action ID | 功能描述 |
|---------|---------| ---------
| [查询应用型负载均衡的重定向关系](https://cloud.tencent.com/document/product/214/9016) | DescribeRewrite | 查询应用型负载均衡的重定向关系。|
|[ 删除应用型负载均衡的重定向关系 ](https://cloud.tencent.com/document/product/214/9014)| DeleteRewrite | 删除应用型负载均衡的重定向关系。|
| [手动添加应用型负载均衡的重定向关系](https://cloud.tencent.com/document/product/214/9015) | ManualRewrite | 手动添加应用型负载均衡的重定向关系。|
| [自动生成应用型负载均衡的重定向关系](https://cloud.tencent.com/document/product/214/9017) | AutoRewrite | 自动生成应用型负载均衡的重定向关系。|




