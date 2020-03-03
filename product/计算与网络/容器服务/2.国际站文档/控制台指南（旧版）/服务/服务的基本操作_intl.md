## Creating Service
1. Log in to the [Tencent Cloud TKE console](https://console.cloud.tencent.com/ccs).
2. Click **Service** in the left navigation bar, and click **New** in the service list page.
![](https://mc.qcloudimg.com/static/img/71f5e69fc5a7fcb9e31ed8b09245481f/image.png)
3. Configure basic service information.
 - **Service Name**: The name of the service to be created, which has a length limited to 63 characters comprised of lowercase letters, numbers and "-". It starts with a lowercase letter and ends with a lowercase letter or a number.
 - **Region**: Select the region where the service is deployed.
 - **Cluster**: Select a cluster to run your service. You need to select a running cluster with available CVMs in it.
 - **Service description**: Information of created service. This information is displayed in **Service Information** page.
![](https://mc.qcloudimg.com/static/img/290a099685a1d4ca873dcb862fb5af1b/image.png)
4. Configure volume.
Click **Add Volume** when you specify a specific path to which a container is mounted.
>**Note:**
>If no source path is specified, a temporary path is assigned by default.

 - **Type**: Four types of volumes are supported: local disk, cloud disk, NFS disk, and configuration file. For more information, please see [How to Use TKE Volume](https://cloud.tencent.com/document/product/457/9112#.E5.AE.B9.E5.99.A8.E6.9C.8D.E5.8A.A1.E6.95.B0.E6.8D.AE.E5.8D.B7.E4.BD.BF.E7.94.A8.E8.AF.B4.E6.98.8E).
 - **Name**: Volume name.
 - **Path**: Specify the path to which a container is mounted.
 ![](//mc.qcloudimg.com/static/img/2f3c75de6cb710e4163ff8c468a7e287/image.png)
5. Configure a container.
 - **Name**: The name of the container to be created, with a length limited to 63 characters.
 - **Image**: Click **Select Image** to create a service under My Images, My Favorites, TencentHub Image, DockerHub Image or other images.
 - **Tag**: The default image tag for TKE. If you need to use a different image tag, click tag display window to select one.
![](https://mc.qcloudimg.com/static/img/320fb05512b5d3d1b4c8b8e48c60cb75/image.png)
6. Other settings
 -  **Number of pods**: A pod consists of one or more relevant containers. You can specify the number of pods by clicking + or -.
 -  **Service access method**: The method for accessing a service determines the network attribute of this service. Different access methods offer different network capabilities. For more information about the four access methods, please see [Configuration of Service Access Methods](https://cloud.tencent.com/document/product/457/9098).
![](https://mc.qcloudimg.com/static/img/20a878637084281eb9f42e1d9878e6f4/image.png)
7. Click **Create Service** to complete the creation process.

## Updating the Number of Pods
1. Click **Services** in the left navigation bar of TKE console to enter the service list, and click **Update Number of Pods**.
![](https://mc.qcloudimg.com/static/img/1c4c201e5e81a8b07ef347119150c380/image.png)
2. You can specify the number of pods by clicking + or -. Click **OK** after the configuration is completed.
![](//mc.qcloudimg.com/static/img/a39aeaaeba2870606e610723b6fb5ddc/image.png)

## Updating Service
1. Click **Services** in the left navigation bar of TKE console to enter the service list, and click **Update Service**.
![](https://mc.qcloudimg.com/static/img/053cf5dcc9540e6a59f479a1e46fadba/image.png)
2. Click **Start Update**.
Two updating methods are available.
 -  **Rolling update**: Update pods one by one, which allows you to update the service without interrupting the business.
 -  **Quick update**: Directly close all current pods, and launch the same number of new pods.
 
## Redeployment
Redeployment is to redeploy the containers under a service and pull a new image.
1. Click **Services** in the left navigation bar of TKE console to enter the service list, and click **More** -> **Redeploy**.
![](https://mc.qcloudimg.com/static/img/377fa0a76b9f1523919234f607a44484/image.png)
2. Click **OK**.
![](//mc.qcloudimg.com/static/img/1132a05be3cb4258cee3c591bdc50111/image.png)

## Deleting Service
1. Click **Services** in the left navigation bar of TKE console to enter the service list, and click **More** -> **Delete**.
![](https://mc.qcloudimg.com/static/img/a64421d525fba54880bb606328666416/image.png)
2. Click **OK**.
![](https://mc.qcloudimg.com/static/img/1d0620fad4e3dac9e2bdce13b87d98d0/image.png)
>**Note**:
>Deleting the service will delete all the pods and public network load balancers under the service. Back up your data in advance.




