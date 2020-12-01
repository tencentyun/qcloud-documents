负载均衡（Cloud Load Balancer，CLB）提供安全快捷的流量分发服务，访问流量经由 CLB 可以自动分配到云中的多台云服务器上，扩展系统的服务能力并消除单点故障。负载均衡支持亿级连接和千万级并发，可轻松应对大流量访问，满足业务需求。

下表为云审计支持的负载均衡操作列表：

| 操作名称                  | 资源类型 | 事件名称                                           |
|-----------------------|------|------------------------------------------------|
| 绑定目标组                 | clb  | AssociateTargetGroups                          |
| 自动 rewrite 接口           | clb  | AutoRewrite                                    |
| 批量解绑后端设备              | clb  | BatchDeregisterTargets                         |
| 批量绑定后端设备              | clb  | BatchRegisterTargets                           |
| 创建转发型四层监听器            | clb  | CreateForwardLBFourthLayerListeners            |
| 创建七层监听器的转发的规则         | clb  | CreateForwardLBListenerRules                   |
| 创建转发型 LB 的7层监听器         | clb  | CreateForwardLBSeventhLayerListeners           |
| 创建负载均衡监听器             | clb  | CreateListener                                 |
| 创建负载均衡                | clb  | CreateLoadBalancer                             |
| 创建负载均衡监听器             | clb  | CreateLoadBalancerListeners                    |
| 添加 SnatIp              | clb  | CreateLoadBalancerSnatIps                      |
| 创建负载均衡七层监听器转发规则       | clb  | CreateRule                                     |
| 创建目标组                 | clb  | CreateTargetGroup                              |
| 删除转发型监听器（四层和七层）       | clb  | DeleteForwardLBListener                        |
| 删除负载均衡实例的七层监听器的规则     | clb  | DeleteForwardLBListenerRules                   |
| 删除负载均衡监听器             | clb  | DeleteListener                                 |
| 删除负载均衡实例              | clb  | DeleteLoadBalancer                             |
| 删除负载均衡监听器             | clb  | DeleteLoadBalancerListeners                    |
| 删除负载均衡                | clb  | DeleteLoadBalancers                            |
| 删除 SnatIp              | clb  | DeleteLoadBalancerSnatIps                      |
| 删除重定向关系               | clb  | DeleteRewrite                                  |
| 删除应用型七层负载均衡监听器规则      | clb  | DeleteRule                                     |
| 删除目标组                 | clb  | DeleteTargetGroups                             |
| 从七层监听器上解绑掉云服务器        | clb  | DeregisterInstancesFromForwardLB               |
| 从转发型4层监听器上解绑机器        | clb  | DeregisterInstancesFromForwardLBFourthListener |
| 解绑后端服务器               | clb  | DeregisterInstancesFromLoadBalancer            |
| 移除目标组实例               | clb  | DeregisterTargetGroupInstances                 |
| 解绑应用型负载均衡监听器上注册的后端机器 | clb  | DeregisterTargets                              |
| 解绑传统型负载均衡的后端服务器       | clb  | DeregisterTargetsFromClassicalLB               |
| 查询负载均衡后端 rs 信息          | clb  | DescribeAllLBBackends                          |
| 获取传统型负载均衡后端的健康状态      | clb  | DescribeClassicalLBHealthStatus                |
| 获取传统型负载均衡监听器列表        | clb  | DescribeClassicalLBListeners                   |
| 获取传统型负载均衡绑定的后端服务器列表   | clb  | DescribeClassicalLBTargets                     |
| 查询关联的机器               | clb  | DescribeForwardLBBackends                      |
| 查询转发型 LB 的健康检查结果        | clb  | DescribeForwardLBHealthStatus                  |
| 查询转发型 LB 的监听器           | clb  | DescribeForwardLBListeners                     |
| 查询负载均衡健康状态            | clb  | DescribeLBHealthStatus                         |
| 查询应用型负载均衡监听器列表        | clb  | DescribeListeners                              |
| 获取负载均衡后端服务器列表         | clb  | DescribeLoadBalancerBackends                   |
| 获取负载均衡监听器列表           | clb  | DescribeLoadBalancerListeners                  |
| 拉取负载均衡应用层日志           | clb  | DescribeLoadBalancerLog                        |
| 获取负载均衡实例列表            | clb  | DescribeLoadBalancers                          |
| 查询负载均衡的详细信息           | clb  | DescribeLoadBalancersDetail                    |
| 查询重定向关系               | clb  | DescribeRewrite                                |
| 获取目标组绑定的实例列表          | clb  | DescribeTargetGroupInstances                   |
| 获取目标组列表               | clb  | DescribeTargetGroupList                        |
| 获取目标组信息               | clb  | DescribeTargetGroups                           |
| 查询后端服务健康状态            | clb  | DescribeTargetHealth                           |
| 查询应用型负载均衡云服务器列表       | clb  | DescribeTargets                                |
| 解绑目标组                 | clb  | DisassociateTargetGroups                       |
| 用户自定义重定向              | clb  | ManualRewrite                                  |
| 修改七层转发规则的域名           | clb  | ModifyDomain                                   |
| 修改七层监听器中域名级别的属性       | clb  | ModifyDomainAttributes                         |
| 修改转发型4层监听器后端端口        | clb  | ModifyForwardFourthBackendsPort                |
| 修改转发型4层监听器后端权重        | clb  | ModifyForwardFourthBackendsWeight              |
| 修改转发型4层监听器属性          | clb  | ModifyForwardLBFourthListener                  |
| 修改转发型负载均衡的名字          | clb  | ModifyForwardLBName                            |
| 修改7层监听的属性             | clb  | ModifyForwardLBSeventhListener                 |
| 修改后端 rs 的权重             | clb  | ModifyForwardSeventhBackends                   |
| 更改后端机器的端口             | clb  | ModifyForwardSeventhBackendsPort               |
| 按量计费 LB 升降配置            | clb  | ModifyLBNetwork                                |
| 修改项目 Id                | clb  | ModifyLBProjectId                              |
| 修改负载均衡监听器属性           | clb  | ModifyListener                                 |
| 修改负载均衡属性信息            | clb  | ModifyLoadBalancerAttributes                   |
| 修改负载均衡器后端服务器权重        | clb  | ModifyLoadBalancerBackends                     |
| 修改负载均衡监听器             | clb  | ModifyLoadBalancerListener                     |
| 修改转发规则的健康检查           | clb  | ModifyLoadBalancerRulesProbe                   |
| 修改应用型负载均衡监听器转发规则      | clb  | ModifyRule                                     |
| 修改目标组属性               | clb  | ModifyTargetGroupAttribute                     |
| 修改目标组内实例端口            | clb  | ModifyTargetGroupInstancesPort                 |
| 修改目标组内实例权重            | clb  | ModifyTargetGroupInstancesWeight               |
| 修改监听器绑定的后端机器的端口       | clb  | ModifyTargetPort                               |
| 修改监听器绑定的后端机器的转发权重     | clb  | ModifyTargetWeight                             |
| 绑定机器到转发型4层监听器上        | clb  | RegisterInstancesWithForwardLBFourthListener   |
| 绑定机器到7层监听器上           | clb  | RegisterInstancesWithForwardLBSeventhListener  |
| 绑定后端服务器到负载均衡          | clb  | RegisterInstancesWithLoadBalancer              |
| 添加目标组实例               | clb  | RegisterTargetGroupInstances                   |
| 绑定后端机器到监听器上           | clb  | RegisterTargets                                |
| 绑定后端服务到传统型负载均衡        | clb  | RegisterTargetsWithClassicalLB                 |
| 用新的来替换旧的证书            | clb  | ReplaceCert                                    |
| 修改 LB 维度的用户个性化配置        | clb  | SetCustomizedConfigForLoadBalancer             |
| 设置负载均衡的日志服务主题         | clb  | SetLoadBalancerClsLog                          |
| 设置应用型 LB 跨域属性           | clb  | SetLoadBalancerCrossRegion                     |
| 开始负载均衡日志              | clb  | SetLoadBalancerLog                             |
| LB 绑定安全组               | clb  | SetLoadBalancerSecurityGroups                  |
| 绑定一个安全组到 LB            | clb  | SetSecurityGroupForLoadbalancers               |
| 设置安全组                 | clb  | SetSecurityGroups                              |
