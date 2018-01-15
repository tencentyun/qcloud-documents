## Creating a Service
1) Go to CCS console, click **Service**, and **New**.
![Alt text](https://mc.qcloudimg.com/static/img/cce6e5a1d89d6d4172cf5f5506455153/basic_operation_of_service_1.jpg)


2) Enter the basic service information.

Service name can only contain lowercase letters and numbers, and begin with a lowercase letter.

To run a cluster, you need to select a running cluster with available CVMs in it.
![Alt text](https://mc.qcloudimg.com/static/img/ab57c7cd6ca4763fe6066568d1641045/basic_operation_of_service_2.jpg)

3) Enter the basic container settings and click **Create Service**.

Here you need to choose the latest nginx image tag. For Service Access Type, choose Public Network Cloud Load Balancer, and fill in the port mapping.

![Alt text](https://mc.qcloudimg.com/static/img/9e62b6503272876aa30b17cb858de0e2/basic_operation_of_service_3.jpg)


## Modifying Number of Pods

On the Service List page, click **Modify Number of Pods** in the specified service bar, select the new number of pods, and click **OK**.

![Alt text](https://mc.qcloudimg.com/static/img/27369cdfd95a3c906204fb4cd8bc4257/basic_operation_of_service_4.jpg)

## Modifying a Service
On the Service List page, click **Modify Service** in the specified service bar, and click **Start Update**.


![Alt text](https://mc.qcloudimg.com/static/img/deb76fe5136500b84d43383e40510b60/basic_operation_of_service_5.jpg)

## Deleting a Service
On the Service List page, click **Delete** in the specified service bar, and click **OK**.
Note: All pods and public network load balancers under the service are deleted as well as you delete the service. Please back up the data in advance.
![Alt text](https://mc.qcloudimg.com/static/img/d38e030d34a3b146540c4f67b048f6d0/basic_operation_of_service_6.jpg)

