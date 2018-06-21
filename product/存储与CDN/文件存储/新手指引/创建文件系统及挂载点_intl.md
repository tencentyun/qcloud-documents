## Creating File System and Mount Point
1. Log in to the CFS console

2. Click the **Create** button, and the Create File System popup window appears.
![](https://main.qcloudimg.com/raw/b2c089eb76dec621eda63ef3e138efe0.png)

3. When creating a file system and mount point, select the following attributes in the popup window.

- Region: Select a region supported by CFS
- Availability zone: Select an availability zone supported by CFS
- File protocol (NFS or CIFS/SMB): Select a file system type. NFS protocol is more suitable for Linux clients, while CIFS/SMB protocol is more suitable for Windows clients.
- Network type: VPC or basic network. Note: Create and mount a file system based on the network of your CVM instance.

	- To allow a file system to be shared by CVMs under a VPC, you need to select VPC when creating a file system. When the file system belongs to VPC, only CVM instances in the same VPC can be mounted if no specific network settings are made.
	- To allow a file system to be shared by CVMs under a basic network, you need to select basic network when creating a file system. When the file system belongs to basic network, only CVM instances in the same basic network can be mounted if no specific network settings are made.
	- For more information on how to share a file system among multiple networks, please see [Cross-network Access to File System](https://cloud.tencent.com/document/product/582/9764)
	
- Permission group: Each file system must be bound to a permission group 
	
4. Obtain the mount point information: After the file system and mount point are created, go to the file system details page to obtain the mount commands for Linux and Windows. "Quantity" refers to the number of mount sources, that is, the number of mounting methods. Only mounting via IP is supported. Therefore, the value is 1.

The mount point information of NFS file system is as follows:
![](https://main.qcloudimg.com/raw/e52d235c97f0a6f16a9cbd86eabe5aa6.png)

The mount point information of CIFS/SMB file system is as follows: 
![](https://main.qcloudimg.com/raw/3a13257ec58a8de79929d8af39b4ed5a.png)


