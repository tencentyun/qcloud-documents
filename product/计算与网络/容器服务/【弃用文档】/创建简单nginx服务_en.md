This document aims to help create an "nginx" service in a container cluster.

## Preconditions
To create an "nginx" service, you must create a cluster first. For more information on how to create a cluster, please see [Create Cluster](https://cloud.tencent.com/document/product/457/9091).

## Steps
1. Log in to [CCS Console](https://console.cloud.tencent.com/ccs).
2. Click "Service" in the left navigation bar, and click "+ New" in the service list page.
![](//mc.qcloudimg.com/static/img/11f7f75d7b051a815da8bfe1e744a8e8/image.png)
3. Enter basic service information.
 - **Service name**: The name of the service to be created, which is comprised of lowercase letters, numbers and "-". It starts with a lowercase letter and ends with a lowercase letter or a number. In this example, the name is "nginx".
 - **Region**: Select a closest region based on your location.
 - **Running cluster**: Select an appropriate cluster and Namespace.
 - **Service description**: Service information. This information is displayed in **Service Information** page.
 ![](//mc.qcloudimg.com/static/img/abb593719ae3c4b7b3b3f79ce68b75a7/image.png)
4. Select an image. Enter the name of the running container, which is "nginx" here. Click [Select Image].
![](//mc.qcloudimg.com/static/img/2ecf52cd54db7b3cd44eda24f3b3a452/image.png)
Click [DockerHub Image], and select "**nginx**". Click [OK].
![](//mc.qcloudimg.com/static/img/0cec90a9a793d8769d586376935bf361/image.png)
Version (Tag): latest. By default, the latest version is used for CCS.
![](//mc.qcloudimg.com/static/img/247064bd27464737d06d02d846c2c227/image.png)
5. Configuring port mapping. Set both container port and service port to 80.
![](//mc.qcloudimg.com/static/img/a86f50da339892896871ab9408514433/image.png)
6. Click [Create Service] to complete the creation of "nginx" service.
>**Note**: Keep default settings for other options.

## Accessing "nginx" Service
1. Click "Service Information" on the service page to check the load balancer ID and load balancer IP. 
![](//mc.qcloudimg.com/static/img/ce1634fd0c84c6aecfec315f3126d9d6/image.png)
2. Accessing "nginx" service by the following ways.
 - Via load balancer IP.
 - Via **domain name**.
 Copy the domain name by clicking "Load Balance" -> "TCP/UDP" in the left navigation bar of the container console to access the service.
 ![](//mc.qcloudimg.com/static/img/23885bb932bdffb91d0a03b899429225/image.png)
 - Other services or containers in the cluster can be accessed directly by the service name.
3. Go to "nginx" server's default welcome page.
![](//mc.qcloudimg.com/static/img/a3cbbc5c902bd162210a4615c0955f19/image.png)

#### More "nginx" Settings

See [Use Tencent Cloud CCS to Build a Simple Web Service](https://cloud.tencent.com/community/article/223421).

