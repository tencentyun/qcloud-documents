### Types of Load Balancer Resources that can be Authorized in CAM

| Resource type | Resource description method in authorization policy |
| :-------- | -------------- |
| Load balancer instance |  ` qcs::clb:$region::clb/$loadbalancerid`  |
| Load balancer listener |   `qcs::clb:$region::listener/$loadbalancerlistenerid`  |
| Load balancer real server |   `qcs::cvm:$region:$account:instance/$cvminstanceid` |

All `$regionid` must be id of a region, or "*";

All `$accountid` must be AccountId of resource owner, or "*"; 

All `$loadbalancerid` must be id of a loadbalancer or "*"; 

and so on.

### APIs for Load Balancer Authorization in CAM
In CAM, you can authorize the following Action for a load balancer resource.
#### Regarding Cloud Load Balancer Instances:
| API Operation | Resource Description | API Description |
| :-------- | :--------| :------ |
| DescribeLoadBalancers	| Query the cloud load balancer instance list | `*` only authenticate API |
| CreateLoadBalancer	| Purchase cloud load balancers | `qcs:$projectid:clb:$region:$account:clb/*` |
| DeleteLoadBalancers	| Delete cloud load balancers | `qcs::clb:$region:$account:clb/$loadbalancerid` |
| ModifyLoadBalancerAttributes	| Modify attributes of cloud load balancer | `qcs::clb:$region:$account:clb/$loadbalancerid` |
| ModifyForwardLBName	| Modify the name of forwarding cloud load balancer | `qcs::clb:$region:$account:clb/$loadbalancerid` |
| ModifyLBWeight	| Modify the weight of cloud load balancer | `qcs::clb:$region:$account:clb/$loadbalancerid` |
| DeleteLBService	| Unbind the device from cloud load balancer | `qcs::clb:$region:$account:clb/$loadbalancerid` |
| ModifyLBHealth	| Modify health check threshold of cloud load balancer | `qcs::clb:$region:$account:clb/$loadbalancerid` |
| DescribeLBHealth	| Query LB health check threshold | `qcs::clb:$region:$account:clb/*` |
#### Regarding Cloud Load Balancer Listeners:
| API Operation | Resource Description | API Description |
| :-------- | :---------| :------ |
| DeleteLoadBalancerListeners	| Delete cloud load balancer listeners | `qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$loadbalancerlistenerid` |
| DescribeLoadBalancerListeners	| Get load balancer listener list |	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/*` |
| ModifyLoadBalancerListener	| Modify cloud load balancer listeners |	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$loadbalancerlistenerid` |
| CreateLoadBalancerListeners	| Create cloud load balancer listeners |	`qcs::clb:$region:$account:clb/$loadbalancerid` |
| DeleteForwardLBListener	| Delete forwarding listeners (Layer-4 and Layer-7) |	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$loadbalancerlistenerid` |
| ModifyForwardLBSeventhListener	| Modify the attributes of Layer-7 listeners |	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$loadbalancerlistenerid` |
| ModifyForwardLBFourthListener	| Modify the attributes of forwarding Layer-4 listeners |	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$loadbalancerlistenerid` |
| DescribeForwardLBListeners	| Query forwarding LB listeners |	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/*` |
| CreateForwardLBSeventhLayerListeners	| Create forwarding LB Layer-7 listeners |	`qcs::clb:$region:$account:clb/$loadbalancerid` |
| DeleteForwardLBSeventhListeners	| Delete Layer-7 listeners |	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$loadbalancerlistenerid` |
| CreateForwardLBFourthLayerListeners	| Create forwarding Layer-4 listeners	|`qcs::clb:$region:$account:clb/$loadbalancerid` |
#### Regarding Application-based Cloud Load Balancer Domain + URL
| API Operation | Resource Description | API Description |
| :-------- | --------| :------ |
| ModifyForwardLBRulesDomain |	Modify the domain name of listeners |	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$loadbalancerlistenerid` |
| CreateForwardLBListenerRules |	Create forwarding rules for Layer-7 listeners |	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$loadbalancerlistenerid` |
| DeleteForwardLBListenerRules	| Delete rules for Layer-7 listeners of cloud load balancer instance |	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$loadbalancerlistenerid` |
| DeleteRewrite	| Delete redirection relationship |	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$sourceloadbalancerlistenerid` `qcs::clb:$region:$account:listener/$targetloadbalancerlistenerid` |
| ManualRewrite	| User's custom redirection | `qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$sourceloadbalancerlistenerid` `qcs::clb:$region:$account:listener/$targetloadbalancerlistenerid` |
| AutoRewrite	| Automatically rewrite API |`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$loadbalancerlistenerid` |
#### Regarding Cloud Load Balancer Real Server:
| API Operation | Resource Description | API Description |
| :-------- | :--------| :------ |
| ModifyLoadBalancerBackends	| Modify weight of load balancer real servers |	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::cvm:$region:$account:instance/$loadbalancerlistenerid` |
| DescribeLoadBalancerBackends	| Get load balancer real server list |	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/*` |
| DeregisterInstancesFromLoadBalancer |	Unbind real servers |	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::cvm:$region:$account:instance/$cvminstanceid` |
| RegisterInstancesWithLoadBalancer	| Bind real servers to cloud load balancer |	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::cvm:$region:$account:instance/$cvminstanceid` |
| DescribeLBHealthStatusMc	| Query health status of cloud load balancer (MC) |	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/*` |
| DescribeLBHealthStatus	| Query health status of cloud load balancer |	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/*` |
| ModifyForwardFourthBackendsPort	| Modify backend port of forwarding Layer-4 listeners |	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$loadbalancerlistenerid` `qcs::cvm:$region:$account:instance/$cvminstanceid` |
| ModifyForwardFourthBackendsWeight	| Modify backend weight of forwarding Layer-4 listeners | `qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$loadbalancerlistenerid` `qcs::cvm:$region:$account:instance/$cvminstanceid` |
| RegisterInstancesWithForwardLBSeventhListener	| Bind the server to Layer-7 listeners |	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$loadbalancerlistenerid` `qcs::cvm:$region:$account:instance/$cvminstanceid` |
| RegisterInstancesWithForwardLBFourthListener | Bind the server to forwarding Layer-4 listeners |	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$loadbalancerlistenerid` `qcs::cvm:$region:$account:instance/$cvminstanceid` |
| DeregisterInstancesFromForwardLBFourthListener	| Unbind the server from forwarding Layer-4 listeners |	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$loadbalancerlistenerid` `qcs::cvm:$region:$account:instance/$cvminstanceid` |
| DeregisterInstancesFromForwardLB	| Unbind the CVM from forwarding Layer-7 listeners |	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$loadbalancerlistenerid` `qcs::cvm:$region:$account:instance/$cvminstanceid` |
| ModifyForwardSeventhBackends	| Modify the weight of the real server |	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::cvm:$region:$account:instance/$cvminstanceid` |
| ModifyForwardSeventhBackendsPort	| Change the port of the real server | `qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$loadbalancerlistenerid` `qcs::cvm:$region:$account:instance/$cvminstanceid` |
| DescribeForwardLBBackends |	Query associated servers |	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::cvm:$region:$account:instance/*` |
| DescribeForwardLBHealthStatus	| Query the health check result of forwarding LB |	`qcs::clb:$region:$account:clb/*` |
| ModifyLoadBalancerRulesProbe	| Modify health check for forwarding rule |	`qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::clb:$region:$account:listener/$loadbalancerlistenerid` |
| DescribeAllLBBackends	| Query RS information of cloud load balancer	| `qcs::clb:$region:$account:clb/$loadbalancerid` `qcs::cvm:$region:$account:instance/*` |



