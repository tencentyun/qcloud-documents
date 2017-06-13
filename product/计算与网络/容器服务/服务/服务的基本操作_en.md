## Creating a Service
1) Click "Service" on the Container Service page in the Console, and then click "New" on the Service List page.
![Alt text](https://mc.qcloudimg.com/static/img/11081690d6b480bd66c68a3c2982b04d/Image+007.png)


2) Enter the basic service information.

Service name can only contain lowercase letters and numbers, and begin with a lowercase letter.

To run a cluster, you need to select a running cluster with available CVMs in it.
![Alt text](https://mc.qcloudimg.com/static/img/ebe1443824bfb67dca946676d3ee6124/Image+082.png)

3) Enter the basic container settings and click "Create Service".

You can only choose images from Tencent Cloud image warehouse to create services. Images from Docker Hub and third-party image warehouse will be available in the future.

Here you need to choose the latest nginx image version. For Service Access Type, choose Public Network Cloud Load Balancer, and fill in the port mapping.

![Alt text](https://mc.qcloudimg.com/static/img/2463289d7a47b5a05a03f35b79196bc0/Image+004.png)


## Update Number of Instances

On the Service List page, click "Update Number of Instances" in the specified service bar, select the new number of instances, and click "OK".

![Alt text](https://mc.qcloudimg.com/static/img/d98db1671db63d39816ce6f4ac6240ff/Image+005.png)

## Update a Service
On the Service List page, click "Update Service" in the specified service bar, and click "Start Update" on the new page.


![Alt text](https://mc.qcloudimg.com/static/img/2a58f6b08e578465367210da9ea36ffa/Image+048.png)

## Delete a Service
On the Service List page, click "Delete" in the specified service bar, and click "OK".
Note: All instances and public network load balancers under the service will be deleted upon deletion of the service. Please back up the data in advance.
![Alt text](https://mc.qcloudimg.com/static/img/1dd519cb73e670d4082751662e5f2d0b/Image+049.png)



