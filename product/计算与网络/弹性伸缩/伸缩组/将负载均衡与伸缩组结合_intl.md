When adding and deleting CVM instances in an AS, you need to ensure that the traffic of applications is allocated across all CVM instances. If you want the created scale-up machines to be under a certain load balancer and receive the traffic forwarded by the load balancer without your intervention, you can specify a load balancer for your machine. The load balancer will be the single point of contact for all incoming traffic towards the instances in your Auto Scaling group.

**Add load balancer to the scaling group**

Integrate scaling group and CLB so that you can attach the CLB to the existing scaling group. Once the CLB is attached, it will automatically register the instances in the group and distribute inbound traffic to these instances.

In the AS [Console](https://console.cloud.tencent.com/autoscaling), click **New** and select the load balancer you need from the **Load Balance** option at the bottom of the page. If you did not create it in advance, click the **New** below the option to create a new load balancer.

> Note:
> The load balancer instance associated with the scaling group must be in the same network environment (VPC or the basic network of the same region) as the scaling group.


**Remove load balancer from scaling group**

Click to enter the detail page of the scaling group, and click "Modify" below the details to delete the corresponding LB.

Once the LB is deleted, the machines in the scaling group will also be automatically unbound from the deleted load balancer.
