### CAM中可授权的负载均衡资源类型

| 资源类型 | 授权策略中的资源描述方法 |
| :-------- | -------------- |
| 负载均衡实例 |  ` qcs::clb:$region::clb/$loadbalancerid`  |
| 负载均衡监听器 |   `qcs::clb:$region::listener/$loadbalancerlistenerid`  |
| 负载均衡后端服务器 |   `qcs::cvm:$region:$account:instance/$cvminstanceid` |

其中所有`$regionid`应为某个region的id，或者“*”；

所有`$accountid`应为资源拥有者的AccountId，或者“*”; 

所有`$loadbalancerid`应为某个loadbalancer的id，或者“*”； 

以此类推。

### CAM中可对负载均衡进行授权的接口
在CAM中，可以对一个负载均衡资源进行以下Action的授权。
#### 负载均衡实例相关：
| API操作 | 资源描述 | 接口说明 |
| :-------- | :--------| :------ |
| DescribeLoadBalancers	|  查询负载均衡实例列表 | `*` 只对接口进行鉴权 |
| CreateLoadBalancer	|  购买负载均衡 | `qcs:$projectid:clb:$region:$account:clb/*` |
| DeleteLoadBalancers	|  删除负载均衡 | `qcs::clb:$region:$account:clb/$loadbalancerid` |
| ModifyLoadBalancerAttributes	|  修改负载均衡属性信息 | `qcs::clb:$region:$account:clb/$loadbalancerid` |
| ModifyForwardLBName	|  修改转发型负载均衡的名字 | `qcs::clb:$region:$account:clb/$loadbalancerid` |
| ModifyLBWeight	|  修改负载均衡权重 | `qcs::clb:$region:$account:clb/$loadbalancerid` |
| DeleteLBService	|  负载均衡解绑设备 | `qcs::clb:$region:$account:clb/$loadbalancerid` |
| ModifyLBHealth	|  修改负载均衡健康检查阈值 | `qcs::clb:$region:$account:clb/$loadbalancerid` |
| DescribeLBHealth	|  查询LB健康检查阈值 | `qcs::clb:$region:$account:clb/*` |
#### 负载均衡监听器相关：
| API操作 | 资源描述 | 接口说明 |
| :-------- | :---------| :------ |
|DeleteLoadBalancerListeners	|删除负载均衡监听器| `qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$loadbalancerlistenerid` |
|DescribeLoadBalancerListeners	|获取负载均衡监听器列表|	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/*` |
|ModifyLoadBalancerListener	|修改负载均衡监听器|	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$loadbalancerlistenerid` |
|CreateLoadBalancerListeners	|创建负载均衡监听器|	`qcs::clb:$region:$account:clb/$loadbalancerid` |
|DeleteForwardLBListener	|删除转发型监听器（四层和七层）|	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$loadbalancerlistenerid` |
|ModifyForwardLBSeventhListener	|修改7层监听的属性|	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$loadbalancerlistenerid` |
|ModifyForwardLBFourthListener	|修改转发型4层监听器属性|	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$loadbalancerlistenerid` |
|DescribeForwardLBListeners	|查询转发型LB的监听器|	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/*` |
|CreateForwardLBSeventhLayerListeners	|创建转发型LB的7层监听器|	`qcs::clb:$region:$account:clb/$loadbalancerid` |
|DeleteForwardLBSeventhListeners	|删除7层监听器|	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$loadbalancerlistenerid` |
|CreateForwardLBFourthLayerListeners	|创建转发型四层监听器	|`qcs::clb:$region:$account:clb/$loadbalancerid` |
#### 应用型负载均衡域名+URL相关：
| API操作 | 资源描述 | 接口说明 |
| :-------- | --------| :------ |
|ModifyForwardLBRulesDomain|	修改监听器的域名  |	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$loadbalancerlistenerid` |
|CreateForwardLBListenerRules|	创建七层监听器的转发的规则|	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$loadbalancerlistenerid` |
|DeleteForwardLBListenerRules	|删除负载均衡实例的七层监听器的规则|	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$loadbalancerlistenerid` |
|DeleteRewrite	|删除重定向关系|	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$sourceloadbalancerlistenerid` `qcs::clb:$region:$account:listener/$targetloadbalancerlistenerid` |
|ManualRewrite	|用户自定义重定向| `qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$sourceloadbalancerlistenerid` `qcs::clb:$region:$account:listener/$targetloadbalancerlistenerid` |
|AutoRewrite	|自动rewrite接口|`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$loadbalancerlistenerid` |
#### 负载均衡后端服务器相关：
| API操作 | 资源描述 | 接口说明 |
| :-------- | :--------| :------ |
|ModifyLoadBalancerBackends	| 修改负载均衡器后端服务器权重|	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::cvm:$region:$account:instance/$loadbalancerlistenerid`|
|DescribeLoadBalancerBackends	| 获取负载均衡后端服务器列表|	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/*` |
|DeregisterInstancesFromLoadBalancer |	解绑后端服务器|	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::cvm:$region:$account:instance/$cvminstanceid`|
|RegisterInstancesWithLoadBalancer	| 绑定后端服务器到负载均衡|	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::cvm:$region:$account:instance/$cvminstanceid`|
|DescribeLBHealthStatusMc	| 查询负载均衡健康状态(MC)|	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/*` |
|DescribeLBHealthStatus	| 查询负载均衡健康状态|	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/*` |
|ModifyForwardFourthBackendsPort	| 修改转发型4层监听器后端端口|	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$loadbalancerlistenerid` `qcs::cvm:$region:$account:instance/$cvminstanceid` |
|ModifyForwardFourthBackendsWeight	|修改转发型4层监听器后端权重|`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$loadbalancerlistenerid` `qcs::cvm:$region:$account:instance/$cvminstanceid` |
|RegisterInstancesWithForwardLBSeventhListener	| 绑定机器到7层监听器上|	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$loadbalancerlistenerid` `qcs::cvm:$region:$account:instance/$cvminstanceid` |
|RegisterInstancesWithForwardLBFourthListener| 绑定机器到转发型4层监听器上|	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$loadbalancerlistenerid` `qcs::cvm:$region:$account:instance/$cvminstanceid` |
|DeregisterInstancesFromForwardLBFourthListener	|将机器从转发型四层监听器上解绑|	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$loadbalancerlistenerid` `qcs::cvm:$region:$account:instance/$cvminstanceid` |
|DeregisterInstancesFromForwardLB	| 从七层监听器上解绑掉云服务器|	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$loadbalancerlistenerid` `qcs::cvm:$region:$account:instance/$cvminstanceid` |
|ModifyForwardSeventhBackends	| 修改后端rs的权重|	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::cvm:$region:$account:instance/$cvminstanceid`|
|ModifyForwardSeventhBackendsPort	| 更改后端机器的端口|`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$loadbalancerlistenerid` `qcs::cvm:$region:$account:instance/$cvminstanceid`|
|DescribeForwardLBBackends |	查询关联的机器|	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::cvm:$region:$account:instance/*`|
|DescribeForwardLBHealthStatus	| 查询转发型LB的健康检查结果|	`qcs::clb:$region:$account:clb/*`  |
|ModifyLoadBalancerRulesProbe	| 修改转发规则的健康检查|	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$loadbalancerlistenerid` |
|DescribeAllLBBackends	| 查询负载均衡后端rs信息	|`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::cvm:$region:$account:instance/*` |


