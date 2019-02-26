### Description
In the example of Wordpress with single pod, we showed how to install WordPress quickly. 
The data in the example is written into MySQL databases that run in the same container. This configuration allows quick launch, but it also brings a problem: if the container stops for any reason, the files in the database or storage will be lost.

In this tutorial, we will show you how to set MySQL database, which will be still available when the pod/container restarts. Persistent storage can be realized by using CDB.

### Steps
#### Step 1: Create Container Service Cluster
First, you need a cluster where containers can run. If you have no cluster, you need to create one. For more information, please see [Create Cluster](https://cloud.tencent.com/document/product/457/6779#.E5.88.9B.E5.BB.BA.E9.9B.86.E7.BE.A4).

#### Step 2: Create CDB
Select a network to which the cluster belongs, and add MySQL database. (The cluster can be located outside the VPC, in which case it can only be accessed through public network)
![Alt text](https://mc.qcloudimg.com/static/img/22ae8f766708955e4badfa4dd8d3cc8a/Image+036.png)

Select the configuration to purchase, wait for the creation process to complete and initialize the CDB database. You can also use self-built MySQL service or existing CDB service.

![Alt text](https://mc.qcloudimg.com/static/img/f3d39903a1d54a2927e9bcbf7e749744/Image+037.png)
#### Step 3. Create Wordpress Service
Enter environment variables:
WORDPRESS_DB_HOST = CDB MySQL address
WORDPRESS_DB_PASSWORD = Password entered during initialization
Click "Finish" to complete the creation process.

![Alt text](https://mc.qcloudimg.com/static/img/523f276c9c722503ff538392d4d63c9c/Image+039.png)
#### Step 4: Access test
![Alt text](https://mc.qcloudimg.com/static/img/c0132b35996db099c02af7f2cf747137/Image+023.png)

