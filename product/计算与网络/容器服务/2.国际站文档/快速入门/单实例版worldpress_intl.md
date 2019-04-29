WordPress is a blogging platform developed with PHP. You can use it as a content management system, or use it to create websites on services that support PHP and MySQL databases.

This document describes how to use the `tutum/wordpress` image to create a publicly accessible WordPress website.

>**Note:**
>The created WordPress with single pod is for testing purpose only. The image includes all operating environments for WordPress, allowing you to pull and create the service directly. However, using WordPress with single pod cannot ensure persistent data storage, so it is recommended that you use the self-built MySQL or Tencent Cloud CDB to store your data. For more information, please see [WordPress with CDB](/doc/product/457/7447).

## Prerequisites
You need to create a cluster first. For more information on how to create a cluster, please see [Basic Operations of Cluster](/doc/product/457/9091).

## Procedure
1. Log in to the [Tencent Cloud TKE console](https://console.cloud.tencent.com/ccs).
2. Click **Service** in the left navigation bar, and click **+ New** in the service list page.
![](//mc.qcloudimg.com/static/img/11f7f75d7b051a815da8bfe1e744a8e8/image.png)
3. Configure basic service information.
 - **Service Name**: The name of the service to be created, which is comprised of lowercase letters, numbers and "-". It starts with a lowercase letter and ends with a lowercase letter or a number.
 - **Region**: Select the closest region based on your location.
 - **Cluster**: Select a cluster to run your service. You need to select a running cluster with available CVMs in it.
 - **Service description**: Information of the created service. This information is displayed on the **Service Information** page.
![](//mc.qcloudimg.com/static/img/9254649a08d86761bcb8287fe5a45141/image.png)
4. Image configuration.
 - **Name**: Enter the name of the running container (here is WordPress).
 - **Image**: Enter `tutum/wordpress`.
 - **Version (Tag)**: Enter "latest".
![](//mc.qcloudimg.com/static/img/b5c035081625c15a1dcbdf0a3cabf6a7/image.png)
5. Configure port mapping. Set both container port and service port to 80.
![](//mc.qcloudimg.com/static/img/a86f50da339892896871ab9408514433/image.png)
6. Click **Create Service** to complete the creation of the WordPress service.
>**Note**: Keep default settings for other options.

## Accessing WordPress Service
1. Click **Service Information** on the service page to check the load balancer IP.
![](//mc.qcloudimg.com/static/img/f92f30a3360c46ac0e6e76d045f4484f/image.png) 
2. Enter the IP in the browser to access the service.
![Alt text](https://mc.qcloudimg.com/static/img/c0132b35996db099c02af7f2cf747137/Image+023.png)


