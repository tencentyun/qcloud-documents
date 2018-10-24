### Description
WordPress is a personal information publishing platform focusing on aesthetics, ease of use and network standards. As a free open-source software, it features user-friendly graphic user interface with elegant look and fresh style.

The following shows how to use Docker image "tutum/wordpress" to create a Wordpress website which allows public access.

The created Wordpress with single pod is for testing purposes only. The image includes all operating environments for Wordpress, thus you can simply pull and create the service. However, using Wordpress with single pod cannot ensure persistent data storage, so it is recommended that you use self-built MySQL or Tencent Cloud CDB to store your data. For more information, please see [Create Wordpress with CDB](https://cloud.tencent.com/document/product/457/7447).

### Steps
#### Step 1: Create Cluster
1. First, you need a cluster where containers can run. If you have no cluster, you need to create one. For more information, please see [Create Cluster](https://cloud.tencent.com/document/product/457/6779#.E5.88.9B.E5.BB.BA.E9.9B.86.E7.BE.A4).


#### Step 2. Create Wordpress Service

1. Enter service name, and select a running cluster.

2. Enter image "tutum/wordpress", and select "latest" version.

3. Enter port mapping information.

![Alt text](https://mc.qcloudimg.com/static/img/27a0a00a151c5f5ebacffca5fc8f832a/Image+025.png)

4. Click "Create Service" to complete the configuration.
### Access Wordpress Service
Click on the service to view its public IP. Enter this IP address in the browser to access the service.
![Alt text](https://mc.qcloudimg.com/static/img/c0132b35996db099c02af7f2cf747137/Image+023.png)

