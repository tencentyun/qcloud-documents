In [WordPress with Single Pod](/doc/product/457/7205), we described how to quickly create a WordPress service. The data of WordPress with single pod is written to the MySQL database running in the same container, which can ensure quick start but may incur an issue, that is, if the container is stopped for some reason, the database and storage-related files will be lost.

This document explains how to configure the MySQL database to make sure that it continue running when the pod/container restarts. Persistent data storage can be achieved by using [CDB](https://cloud.tencent.com/product/cdb-overview).

## Prerequisites
You need to create a cluster first. For more information on how to create a cluster, please see [Basic Operations of Cluster](/doc/product/457/9091).

## Procedure
### Step 1: Create a CDB
1. Log in to the [VPC Console](https://console.cloud.tencent.com/vpc/vpc?rid=1).
2. Click the ID/name (e.g. vpc-xxxxx) on the VPC list page.
![](//mc.qcloudimg.com/static/img/33830d9c88d9cb332b1ce148588cdbf5/image.png)
3. On the VPC Details page, select **MySQL** in the database directory, and click **Add** on the right.
![](//mc.qcloudimg.com/static/img/6b93fb0bc0ea4937a77ce77564934ed5/image.png)
4. Select the configuration to purchase, and complete the payment. For more information, please see [Database MySQL](/doc/product/236/5147).
5. The purchased MySQL will appear in the MySQL instance list.
![](//mc.qcloudimg.com/static/img/d5d50b0f9406856b875ba1171e7e8a1f/image.png)
6. Initialize the MySQL instance. Click **Initialize** under the **Operation** column on the right side.
![](//mc.qcloudimg.com/static/img/2f548123653b1b80b90bd61c74ac495f/image.png)
7. Configure initialization parameters, and then click **OK** to start initialization.
 - **Supported character set**: Select the character set supported by the MySQL database.
 - **Case-sensitivity of the table name**: Whether the table name is case sensitive. Default is "Yes".
 - **Custom port**: Database access port. Default is 3306.
 - **Root account password**: The default user name for the new MySQL database is "root". This is used to set the password of the root account.
 - **Confirm password**: Enter the password again.
 ![](//mc.qcloudimg.com/static/img/9d4b57c8c8dd4b5000521ff9049dbb81/image.png)
8. The status of the target MySQL instance becomes **Running**, which indicates it has been initialized successfully.
![](//mc.qcloudimg.com/static/img/c285fb82e354ba127cd0cce01804a197/image.png)

### Step 2: Create WordPress service
1. Log in to the [Tencent Cloud TKE console](https://console.cloud.tencent.com/ccs).
2. Click **Service** in the left navigation bar, and click **New** in the service list page.
![](//mc.qcloudimg.com/static/img/11f7f75d7b051a815da8bfe1e744a8e8/image.png)
3. Configure basic service information.
 - **Service Name**: The name of the service to be created, which is comprised of lowercase letters, numbers and "-". It starts with a lowercase letter and ends with a lowercase letter or a number.
 - **Region**: Select the closest region based on your location.
 - **Cluster**: Select a cluster to run your service. You need to select a running cluster with available CVMs in it.
 - **Service description**: Information of the created service. This information is displayed on the **Service Information** page.
![](//mc.qcloudimg.com/static/img/9254649a08d86761bcb8287fe5a45141/image.png)
4. Click **Display Advanced Settings** under the running container. In the drop-down list, click **New Variable** under Environment Variables. Enter:
WORDPRESS_DB_HOST = Address of CDB for MySQL
WORDPRESS_DB_PASSWORD = Password entered during initialization
![](//mc.qcloudimg.com/static/img/6508b3858d0bba46510a81279aad2e15/image.png)
5. Configure port mapping. Set both container port and service port to 80.
![](//mc.qcloudimg.com/static/img/0b068b42b7f6d585769b5f2d94d798f2/image.png)
6. Click **Create Service** to complete the creation of the WordPress service.

## Accessing WordPress Service
1. Click **Service Information** on the service page to check the load balancer IP.
![](//mc.qcloudimg.com/static/img/f92f30a3360c46ac0e6e76d045f4484f/image.png) 
2. Enter the IP in the browser to access the service.
![Alt text](https://mc.qcloudimg.com/static/img/c0132b35996db099c02af7f2cf747137/Image+023.png)

