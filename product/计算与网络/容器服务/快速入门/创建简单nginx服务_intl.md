### Description
This document shows how to quickly create an nginx service in a container cluster.

#### Step 1: Create Cluster
First, you need a cluster where containers can run. If you have no cluster, you need to create one. For more information, please see [Create Cluster](https://www.qcloud.com/document/product/457/6779#.E5.88.9B.E5.BB.BA.E9.9B.86.E7.BE.A4).


#### Step 2: Create nginx Service

1. Go to the "Container Service" page from the console, click "Service" in the list on the left and then click the "Create" button on the service page.
![Alt text](https://mc.qcloudimg.com/static/img/11081690d6b480bd66c68a3c2982b04d/Image+007.png)

2. Enter basic service information.

Service names can only include lowercase letters and numbers, and must begin with lowercase letters. Take "nginx" as an example.

To run a cluster, you need to select a running cluster with available CVMs in it.

Currently you can only choose images in Tencent Cloud image warehouse and official Docker images in the "Image" section of the running container. The feature for creating services using images from third-party warehouses will become available in the future. Here, we take the official nginx image as an example.

Click "Display Advanced Settings" to enter parameters such as memory limit, CPU limit, operation commands and parameters, environment variables, capacity health check, etc.

Specify load balancer listening port and container port in Port Mapping.

Keep default settings for other options and click "Create Service".
![Alt text](https://mc.qcloudimg.com/static/img/c18b47dfdbe50fbb87a3f29fb45b1539/%7B24E5F58D-4F21-468C-B8D1-6481E09736C1%7D.png)

3. When creation is completed, you can click the service name in the service list to view the domain and IP of load balancer.

![Alt text](https://mc.qcloudimg.com/static/img/b5eea292a440c16cb92c29bd37fe0c69/Image+071.png)

4. Access the service using the domain or load balancer IP.
![Alt text](https://mc.qcloudimg.com/static/img/e48f617e80dce415d83aff243d299268/Image+015.png)

