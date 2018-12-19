This document describes how to share [CBS Cloud Disk](https://cloud.tencent.com/document/product/362/2345) by building NFS service with containers.

NFS is short for Network File System. With NFS, users and programs can access files on remote systems in the same way as accessing local files.

### Preconditions
Create a cluster first if you don't have one. For more information on how to create a cluster, see [New Cluster](https://cloud.tencent.com/document/product/457/9091).
### Steps
**Step 1**: Create a service
On [CCS Console](https://console.cloud.tencent.com/ccs) page, click **Services**, and then click "New" on the service list page.
![](//mc.qcloudimg.com/static/img/9770c91c39779859f75153b6709ff75b/image.gif)
**Step 2**: Add data volume
![](//mc.qcloudimg.com/static/img/ae63d74d7b78d2b74ad2590606c24cd7/image.gif)
>**Note**:
> -  If you are prompted that"**No cloud disk available**", go to [Cloud Disk Console](https://console.cloud.tencent.com/cvm/cbs), and click "New" to buy a cloud disk.
> - It is recommended to enable "Auto Renewal" for the cloud disk to avoid unnecessary data loss due to arrears.

**Step 3**: Set a mount point in the container configuration
1. Click "**Advanced Settings**" under the running container.
2. Set a mount path.

>**Note**:
>Make sure to mount the cloud disk into **/exports** as shown in the following figure.

![Alt text](https://mc.qcloudimg.com/static/img/a54be48bcbe8e24410361b5a2860c43f/image.png)
**Step 4**: Select an image
- **Image**: Select ccr.ccs.tencentyun.com/library/nfs-server in the TencentHub image.
- **Version**: Select latest.

![Alt text](https://mc.qcloudimg.com/static/img/6238482728fbffc531c9b029bcf78eff/image.png)
**Step 5**: Select**Access within Cluster** as the service access method
![](//mc.qcloudimg.com/static/img/b33610a809d2eb036b053a84a76203e0/image.gif)

**Step 6**: Add port mapping
Add three port mappings: 111, 2049, 20048.
![](//mc.qcloudimg.com/static/img/422f5cb9570b9674450cd8ea4d4a4a10/image.gif)
**Step 7**: Enable privilege level on the container
![Alt text](https://mc.qcloudimg.com/static/img/1a739ddd2e4933285af85954c4c59aea/image.png)
**Step 8**: Complete container creation
After the service is created, you can create a test service that mounts the NFS disk within the same cluster. Since any image is applicable to the test service, you can mount the newly created NFS disk when creating the test service.
The followings are parameter samples for mounting an NFS disk when a test service is created:
**Type**: Select an NFS disk.
**Name**: Name of data volume. Take nnnfs as an example.
**Path**: Enter **Service IP:/exports**.
>**Note:**
>Service IP is the IP of the newly created NFS disk service.

![](https://mc.qcloudimg.com/static/img/9ce501057b5cad2a2271716725be0606/1212.png)
If the test service starts successfully, you have completed the building of NFS service. For more information on how to mount an NFS disk, please see [Mounting Details](/doc/product/457/9112).

>**Note:**
> If NFS disk mounting failed and you are prompted the event `mount:  wrong fs type, bad option, bad superblock on ip:path, missing codepage or helper program, or other error (for several filesystems (e.g. nfs, cifs) `, perhaps you are using an old cluster that do not contain NFS tool library. Such problem will not happen in new clusters. To solve this problem, you can log in to the cluster node, and execute the following command depending on your system:

>- For Ubuntu 16.04 system:  
```shell
apt-get install nfs-kernel-server -y
``` 
- For CentOS 7.2 system:  
```shell
yum install nfs-utils -y
``` 

