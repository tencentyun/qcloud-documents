Now, **the public network application LB** supports cross-region CVM binding, allowing you to select the region of backend servers to realize cross-VPC/region backend instance binding. Load balancer cross-region binding feature allows you to modify the region attributes of your backend CVM. The feature is in the process of beta test for now. If you want to try it, submit a [Ticket](https://console.cloud.tencent.com/workorder/category/create?level1_id=6&level2_id=163&level1_name=%E8%AE%A1%E7%AE%97%E4%B8%8E%E7%BD%91%E7%BB%9C&level2_name=%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1%20LB) for application.

## Application Scenarios
1. Global service for P2P and other game business. With the backend server cluster built in Guangzhou, you can create LBs in Shanghai, Beijing, and other cities, and bind the LBs to the same backend server cluster in Guangzhou for game acceleration and traffic convergence, thus effectively guaranteeing data transmission quality and reducing latency.
2. In financial business payment, order payment, and other scenarios, the transmission quality and consistency of key business data can be effectively guaranteed.
![](https://mc.qcloudimg.com/static/img/d45c523e673169d01b85b079d5770799/image.png)

## Operation Example
After purchasing public network application cloud load balancer, you can view the region attributes of the backend CVM on the instance details page. The region attribute of backend CVM is the same with that of cloud load balancer by default.
If the application LB is bound to a CVM in the same region, you need to unbind the CVM before switching the LB to another region.

![](https://mc.qcloudimg.com/static/img/e538b364bf6c28f09be6f015aebce668/image.jpg)

You can click "Edit" to modify the region and network attributes of the backend CVM. The bandwidth cost incurred for cross-region binding is billed by day and bandwidth. After modification, you can select the CVM in the corresponding backend region on the Bind to CVM page for cross-region binding. **Now, only intra-region backend CVMs are allowed to be bound.**

![](https://mc.qcloudimg.com/static/img/74cd39722b4df5ae6ef949571e600161/image.jpg)

> Note:
> When you modify the region attribute of a backend instance, if this region is different from that of a CLB, it cannot be changed back to the intra-region with CLB for binding.
> Intra-region and cross-VPC binding of cloud load balancer and CVM is not supported for now
> Scenarios of cross-VPC/basic network are also supported

## Billing
The cross-region binding is realized based on the principle of cross-region peering connection. For more information on billing, see [Billing](https://cloud.tencent.com/document/product/214/8848).

