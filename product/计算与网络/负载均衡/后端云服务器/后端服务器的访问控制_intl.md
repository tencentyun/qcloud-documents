As with all CVMs, access to cloud load balancing backend server instances can be controlled via a security group, which acts as a firewall.  You can associate one or more security groups with a backend CVM and add one or more rules to each security group to control traffics to different servers.  You can modify the rules for a security group at any time, and the new rule is automatically applied to all instances associated with that security group.  For more information, please refer to [Security Group Product Documentation](/doc/product/213/5221).  In the [Virtual Private Cloud](/doc/product/213/5227) environment, you can also use [Network ACL](/doc/product/215/5132) for access control. 
 
You can use a security group to have the backend instance only receive traffics from the cloud load balancer, or control it to receive traffic from other sources.  However, it is important to note that <font color="red">you must ensure that the instance's security group allows the cloud load balancer to communicate with the backend instance on the corresponding listener port and health check port</font>.  In VPC, your security groups and network ACLs must allow traffics in both directions on these ports. 

## Recommendation Rules for Cloud Load Balancing Security Group 

| CVM Traffic Sources | Security Group Configuration | 
|----|------|
| Customer remote access, login to CVM | For Linux security group, please allow port 22 <br>For Windows security group, please allow port 3389 | 
| Cloud Load balancer forwarding | Private network: When users activate SNAT and source address translation is executed, for private network LB request via vpc, the client IP address is hidden to the backend CVM.  In this case, cloud load balancing VIP needs to be added to the security group Allow rules.  <br>Public network: After creating the listener and associating with the CVM, configure a security group for the CVM and add the cloud load balancing VIP to the security group Allow rules.   | 
| Cloud Load Balancer Health Check | Private network: There is no need for special configuration as the cloud automated testing machine has already been added to the whitelist for private network health check.  <br>Public network: According to the rules of the previous step, VIP access can be allowed, without special configuration.   | 

## Use the Console to Manage Backend Server Security Groups 
1) Login to [Cloud Load Balance Console](https://console.cloud.tencent.com/loadbalance) and click on the corresponding cloud load balancer instance ID to enter the page for load balancer details. 

2) In the "Backend Server" tab, click the corresponding backend server ID to enter the CVM details page. 

3) Click the "Security Group" tab, and click the "Edit" button under "Security Groups You've Joined" to edit the currently associated security group. Click "Configure Security Group" to add a new security group association. 

> Tencent Cloud recommends users to configure the backend server security group as "fully allow".  If you enable the security group access control (disable rule) function, you should pay attention to the following rules: 
> 
- You need to configure  all client IPs in the security group rules for this CVM instance IP. 
- As long as the security group is enabled, the cloud load balancing VIP must be added to the Allow rule of the backend server. 
- For some malicious IPs, you can add them to the front rules of the security group, prohibiting them from accessing the backend server.  And then allow all the IP (0.0.0.0) to the local service port, so that the normal client can access to it.  According to the security group effective rule, you can block the front IPs. 

## Use API to Manage Backend Server Security Groups 
Refer to [ModifySecurityGroupsOfInstance API](https://cloud.tencent.com/doc/api/229/1367) and [ModifySecurityGroupPolicy API](https://cloud.tencent.com/doc/api/229/1365) 

