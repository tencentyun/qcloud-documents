Cloud Load balancer routes the requests to a normally running backend CVM instance. If the demand of requests for the instance is raised, the user needs to add more instances to the cloud load balancer to process the requests. 

Unbinding backend server will end the association between cloud load balancer instance and the CVM instance, immediately stop its request forwarding, <font color="red">but will not have any effect on the life cycle of the CVM</font>. You can add the cloud load balancer instance once again to the backend server cluster when you are ready. 

If a cloud load balancer instance is associated with an auto scaling group, the instances in that group are automatically added to the cloud load balancing backend instance, and any CVM instance removed from the auto scaling group is automatically removed from the cloud load balancing backend server. 

## Adding a Cloud Load Balancing Backend Instance 
### Use the Console to Add a Cloud Load Balancing Backend Instance 

1) Login to [Cloud Load Balance Console](https://console.cloud.tencent.com/loadbalance) and click on the corresponding cloud load balancer instance ID to enter the page for cloud load balancer details.

2) In the "Bind Cloud Virtual Machine" tab, click the "Bind Cloud Virtual Machine" button. 

3) A  pop-up box appears with a list of optional CVMs<font color="red"> that are in the same region, the same network environment, not isolated or expired, and with a bandwidth (peak) being not 0 </font>.  Select all the CVMs that need to be associated and click "OK" button. 

Thus, You have completed the association between the CVM and the cloud load balancer. 

### Use API to Add a Cloud Load Balancing Backend Instance 

Please refer to the [RegisterInstancesWithLoadBalancer API](https://cloud.tencent.com/doc/api/244/1265). 

## Modifying the Weights of Load Balancing Backend Servers 
The weight of a backend server determines the relative number of forwarded requests to the CVM.  For more information on weight of the load balancing backend server, refer to [Cloud Load Balancer Round-robin Method](/doc/product/214/6153). 

### Use the Console to Modify the Cloud Load Balancing Backend Server Weights

1) Login to [Cloud Load Balance Console](https://console.cloud.tencent.com/loadbalance) and click on the corresponding cloud load balancer instance ID to enter the page for cloud load balancer details.

2) In the "Bind Cloud Virtual Machine" tab, click the "Modify" button on the corresponding CVM weight bar to modify the weight of the corresponding backend CVM. 

### Use API to Modify the Cloud Load Balancing Backend Server Weights 
Please refer to the [ModifyLoadBalancerBackends API](https://cloud.tencent.com/doc/api/244/1264). 

## Unbinding Cloud Load Balancing Backend Servers

### Use the Console to Unbind the Cloud Load Balancing Backend Server 

1) Login to [Cloud Load Balance Console](https://console.cloud.tencent.com/loadbalance) and click on the corresponding cloud load balancer instance ID to enter the page for cloud load balancer details.

2) In the "Bind Cloud Virtual Machine" tab, click the "Unbind" button behind the corresponding CVM to end the binding of the corresponding backend CVM and the cloud load balancer. 

### Use API to Modify the Cloud Load Balancing Backend Server Weights 
Please refer to [DeregisterInstancesFromLoadBalancer API](https://cloud.tencent.com/doc/api/244/1258). 

