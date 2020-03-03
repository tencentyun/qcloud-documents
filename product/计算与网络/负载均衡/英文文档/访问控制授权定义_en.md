## Definition of CLB CAM Authorization

### Types of Load Balancer Resources that can be Authorized in CAM

| Resource Type | Resource Description Method in Authorization Policy |
| :-------- | -------------- |
| Load balancer instance |  ` qcs::clb:$region::clb/$loadbalancerid`  |
| Load balancer listener |   `qcs::clb:$region::listener/$loadbalancerlistenerid`  |
| Load balancer backend server |   `qcs::cvm:$region:$account:instance/$cvminstanceid` |

All `$regionid` must be id of a region, or "*";

All `$accountid` must be AccountId of resource owner, or "*"; 

All `$loadbalancerid` must be id of a loadbalancer or "*"; 

and so on.

### API in CAM that can Authorize Load Balancer
In CAM, you can authorize the following Action for a load balancer resource.
#### Regarding Cloud Load Balancer Instances:
| API Operation | Resource Description | API Description |
| :-------- | :--------| :------ |
| DescribeLoadBalancers	|  Query cloud load balancer instance list | `*` Only authenticate API |
| CreateLoadBalancer	|  Purchase cloud load balancers | `qcs:$projectid:clb:$region:$account:clb/*` |
| DeleteLoadBalancers	|  Delete cloud load balancers | `qcs::clb:$region:$account:clb/$loadbalancerid` |
| ModifyLoadBalancerAttributes	|   Modify attributes of cloud load balancer | `qcs::clb:$region:$account:clb/$loadbalancerid` |
| ModifyForwardLBName	|  Modify the name of application cloud load balancer | `qcs::clb:$region:$account:clb/$loadbalancerid` |
| ModifyLBWeight	|  Modify the weight of cloud load balancer | `qcs::clb:$region:$account:clb/$loadbalancerid` |
| DeleteLBService	|  Unbind the device from cloud load balancer | `qcs::clb:$region:$account:clb/$loadbalancerid` |
| ModifyLBHealth	|  Modify health check threshold of cloud load balancer | `qcs::clb:$region:$account:clb/$loadbalancerid` |
| DescribeLBHealth	|  Query LB health check threshold | `qcs::clb:$region:$account:clb/*` |
#### Regarding Cloud Load Balancer Listeners:
| API Operation | Resource Description | API Description |
| :-------- | :---------| :------ |
| DeleteLoadBalancerListeners	| Delete cloud load balancer listeners | `qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$loadbalancerlistenerid` |
| DescribeLoadBalancerListeners	| Get load balancer listener list|	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/*` |
| ModifyLoadBalancerListener	| Modify cloud load balancer listeners |	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$loadbalancerlistenerid` |
| CreateLoadBalancerListeners	| Create cloud load balancer listeners |	`qcs::clb:$region:$account:clb/$loadbalancerid` |
| DeleteForwardLBListener	| Delete application listeners (Layer-4 and Layer-7) |	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$loadbalancerlistenerid` |
| ModifyForwardLBSeventhListener	| Modify the attributes of Layer-7 listeners |	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$loadbalancerlistenerid` |
| ModifyForwardLBFourthListener	| Modify the attributes of application Layer-4 listeners |	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$loadbalancerlistenerid` |
| DescribeForwardLBListeners	| Query application LB listeners |	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/*` |
|CreateForwardLBSeventhLayerListeners	| Create application LB Layer-7 listeners |	`qcs::clb:$region:$account:clb/$loadbalancerid` |
| DeleteForwardLBSeventhListeners	| Delete Layer-7 listeners |	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$loadbalancerlistenerid` |
| CreateForwardLBFourthLayerListeners	| Create application Layer-4 listeners	|`qcs::clb:$region:$account:clb/$loadbalancerid` |
#### Regarding Application Cloud Load Balancer Domain + URL
| API Operation | Resource Description | API Description |
| :-------- | --------| :------ |
| ModifyForwardLBRulesDomain |	Modify the domain name of listeners |	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$loadbalancerlistenerid` |
| CreateForwardLBListenerRules |	Create forwarding rules for Layer-7 listeners |	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$loadbalancerlistenerid` |
| DeleteForwardLBListenerRules	| Delete rules for Layer-7 listeners of cloud load balancer instance |	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$loadbalancerlistenerid` |
| DeleteRewrite	| Delete redirection relationship |	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$sourceloadbalancerlistenerid` `qcs::clb:$region:$account:listener/$targetloadbalancerlistenerid` |
| ManualRewrite	| Users custom redirection | `qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$sourceloadbalancerlistenerid` `qcs::clb:$region:$account:listener/$targetloadbalancerlistenerid` |
| AutoRewrite	| Automatically rewrite API |`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$loadbalancerlistenerid` |
#### Regarding Cloud Load Balancer Backend Server:
| API Operation | Resource Description | API Description |
| :-------- | :--------| :------ |
| ModifyLoadBalancerBackends	| Modify weight of load balancer backend servers |	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::cvm:$region:$account:instance/$loadbalancerlistenerid`|
| DescribeLoadBalancerBackends	| Get load balancer backend server list |	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/*` |
| DeregisterInstancesFromLoadBalancer |	Unbind backend servers |	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::cvm:$region:$account:instance/$cvminstanceid`|
| RegisterInstancesWithLoadBalancer	| Bind backend servers to cloud load balancer |	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::cvm:$region:$account:instance/$cvminstanceid`|
| DescribeLBHealthStatusMc	| Query health status of cloud load balancer (MC) |	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/*` |
| DescribeLBHealthStatus	| Query health status of cloud load balancer |	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/*` |
| ModifyForwardFourthBackendsPort	| Modify backend port of application Layer-4 listeners |	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$loadbalancerlistenerid` `qcs::cvm:$region:$account:instance/$cvminstanceid` |
| ModifyForwardFourthBackendsWeight	| Modify backend weight of application Layer-4 listeners |`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$loadbalancerlistenerid` `qcs::cvm:$region:$account:instance/$cvminstanceid` |
| RegisterInstancesWithForwardLBSeventhListener	| Bind the machine to Layer-7 listeners |	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$loadbalancerlistenerid` `qcs::cvm:$region:$account:instance/$cvminstanceid` |
| RegisterInstancesWithForwardLBFourthListener | Bind the machine to application Layer-4 listeners |	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$loadbalancerlistenerid` `qcs::cvm:$region:$account:instance/$cvminstanceid` |
| DeregisterInstancesFromForwardLBFourthListener	| Unbind the machine from application Layer-4 listeners |	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$loadbalancerlistenerid` `qcs::cvm:$region:$account:instance/$cvminstanceid` |
| DeregisterInstancesFromForwardLB	| Unbind the CVM from application Layer-7 listeners |	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$loadbalancerlistenerid` `qcs::cvm:$region:$account:instance/$cvminstanceid` |
| ModifyForwardSeventhBackends	| Modify the weight of backend rs |	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::cvm:$region:$account:instance/$cvminstanceid`|
| ModifyForwardSeventhBackendsPort	| Change the port of backend machines |`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$loadbalancerlistenerid` `qcs::cvm:$region:$account:instance/$cvminstanceid`|
| DescribeForwardLBBackends |	Query associated machines |	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::cvm:$region:$account:instance/*`|
| DescribeForwardLBHealthStatus	| Query the health check result of application LB |	`qcs::clb:$region:$account:clb/*`  |
| ModifyLoadBalancerRulesProbe	| Modify health check for forwarding rules |	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$loadbalancerlistenerid` |
| DescribeAllLBBackends	| Query backend rs information of cloud load balancer	|`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::cvm:$region:$account:instance/*` |



