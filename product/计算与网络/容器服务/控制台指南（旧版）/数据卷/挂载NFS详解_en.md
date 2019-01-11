## Preconditions
A file system is required for mounting CFS. If you don't have one, create a file system first. For more information about how to create a file system, please see [Create a file system and a mount point](/doc/product/582/9132).

>**Note:**
>You need to create a subdirectory before mounting one, because directories that do not exist cannot be automatically created during the process of CFS disk mounting in CCS.

## Viewing a File System
1. Log in to [File Storage Console](https://console.cloud.tencent.com/cfs).
2. View the availability zones in​the file system. Take Beijing Zone 1 as an example. Click ID/Name (e.g. cf-xxxxv0z) to go to the file system details page.
![](//mc.qcloudimg.com/static/img/50dbda0d284e1e428bedcbf157af69ae/image.png)
3. Click "Mount Point Information" to obtain the network information and the mount path (used for subsequent service creation),  as shown below:
 - **Network information**: docker-test and docker.
 - **Mount path**: `10.0.0.7:/`.
![](//mc.qcloudimg.com/static/img/c3286b417a5a73278a35665e4ef4e739/image.png)
 
## Creating a Cluster 
File systems can only be mounted to the cluster within the same VPC network and subnet. Therefore, you need to create the cluster in the VPC network and subnet where the file system resides. For more information on how to create a cluster, please see [New Cluster](/doc/product/457/9091). Pay attention to the followings when you create a cluster:
- **Availability Zone**: Select the same availability zone as the file system. Here, select Beijing Zone 1.
- **Node Network**: Select the same network information as the file system. Here, select docker-test and docker.
- **Container Network**: Select the same IP address range where the file system resides.
![](//mc.qcloudimg.com/static/img/f0a3e622d4fc71b354bb44e7faf38e73/image.png)

## Creating a Service
For more information about how to create a service, please see [Basic Operations of Service](/doc/product/457/9096). Pay attention to the followings when you create a service:
1. Add data volume.
 - **Type**: Select NFS disk.
 - **Name**: The name of data volume. Here, it is cfs.
 - **Path**: Enter the mount path of the file system. Here, enter `10.0.0.7:/`.
![](//mc.qcloudimg.com/static/img/a514e6fcb76a07182ced69ddfcd68df1/image.png)
2. Set a mount point.
Click "Advanced Settings" under the running container. Enter the details of the mount point.
![](//mc.qcloudimg.com/static/img/1e6f5c80d5f78e58fb475d82676f9e88/image.png)

