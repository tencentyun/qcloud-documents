## Creating a Service
1) Go to CCS console, click **Service**, and **New**.
![Alt text](https://mc.qcloudimg.com/static/img/11081690d6b480bd66c68a3c2982b04d/Image+007.png)


2) Enter the basic service information.

Service name can only contain lowercase letters and numbers, and begin with a lowercase letter.

To run a cluster, you need to select a running cluster with available CVMs in it.
![Alt text](https://mc.qcloudimg.com/static/img/ebe1443824bfb67dca946676d3ee6124/Image+082.png)

3) Enter the basic container settings and click **Create Service**.

Here you need to choose the latest nginx image tag. For Service Access Type, choose Public Network Cloud Load Balancer, and fill in the port mapping.

![Alt text](https://mc.qcloudimg.com/static/img/2463289d7a47b5a05a03f35b79196bc0/Image+004.png)


## Modifying Number of Pods

On the Service List page, click **Modify Number of Pods** in the specified service bar, select the new number of pods, and click **OK**.

![Alt text](https://mc.qcloudimg.com/static/img/d98db1671db63d39816ce6f4ac6240ff/Image+005.png)

## Modifying a Service
On the Service List page, click **Modify Service** in the specified service bar, and click **Start Update**.


![Alt text](https://mc.qcloudimg.com/static/img/2a58f6b08e578465367210da9ea36ffa/Image+048.png)

## Deleting a Service
On the Service List page, click **Delete** in the specified service bar, and click **OK**.
Note: All pods and public network load balancers under the service are deleted as well as you delete the service. Please back up the data in advance.
![Alt text](https://mc.qcloudimg.com/static/img/1dd519cb73e670d4082751662e5f2d0b/Image+049.png)



