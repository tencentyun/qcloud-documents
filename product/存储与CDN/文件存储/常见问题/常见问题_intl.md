## FAQ
### Which platforms are supported by CFS?
Linux, Unix, Windows, and other clients.

### How is CFS billed?
CFS is billed only based on actual storage (peak storage per hour).

### Which access protocols are supported by CFS?
NFS v3.0/v4.0 and CIFS/SMB protocols. The CIFS/SMB protocol is under public trial, and you can submit a ticket to apply for a trial.


Because operation system clients include Windows， Linux 3.10 (eg CentOS 6.* ) and it's previous kernel version are incompatible with the NFS 4.0 protocol, they cannot work normally after being mounted with NFS 4.0. Use NFS 3.0 to mount such clients.


### CFS-related concepts
File system: A file system is a file storage instance. After a file system is mounted to a CVM, you can use it in the same way as you use a local storage. It can be mounted to a directory.
Mount point: The mount point is an entry for the computing node to access the file storage. It defines the type of network for the computing node and the permission used to access the file storage.

### How many file systems can be created for each user?
A maximum of 10 file systems can be created for ​a single user in each region. Submit a ticket to apply for more quota.

### The file system cannot be mounted to the mount point
- See the error message.
- Check whether nfs-utils, nfs-common and cifs-utils are installed.
- Check whether the local mount directory exists.
- Check whether the VPC of the mount point is the same as that of the client VM, and whether they share the same region.
- Check whether the VM hosting the CFS client is configured with a security group policy that prohibits access to external ports. For more information on specific ports, please see [File System Port](https://cloud.tencent.com/document/product/582/9551#.E6.96.87.E4.BB.B6.E7.B3.BB.E7.BB.9F.E7.AB.AF.E5.8F.A3.E9.97.AE.E9.A2.98). 

### Data cannot be written into CFS
- See the error message.
- Check whether the network of the VM hosting the client is normal, and whether the port of telnet mount point is opened. For more information on specific ports, please see [File System Port](https://cloud.tencent.com/document/product/582/9551#.E6.96.87.E4.BB.B6.E7.B3.BB.E7.BB.9F.E7.AB.AF.E5.8F.A3.E9.97.AE.E9.A2.98). 
- If the file system is not mounted to the mount point root directory, check whether the corresponding mount point directory exists. (The common error message here is "Stale file handle". You can check whether the subdirectory exists through the device that has been mounted to the root directory.)

### File system port

File System Protocol | Open Port | Check Network Connectivity
------- | ------- | ---------
NFS 3.0 | 111, 892, 2049 | telnet file system IP 2049
NFS 4.0 | 2049 | telnet file system IP 2049
CIFS/SMB | 445 | telnet file system IP 445 

Note: CFS does not currently support ping.

### How do permissions take effect?
NFS file system supports configuring multiple rules which take effect based on their priorities.

- If a single IP conflicts with an IP of the IP address range in the same permission group, the rule with a higher priority takes effect. If the priority is the same, the permission of the single IP prevails.
- If two overlapped IP address ranges are configured with different permissions but the same priority, the permission of the overlapped IP address range takes effect randomly. Please avoid configuring overlapped IP address ranges. 

**Note: CIFS/SMB file system does not support priorities, so the permission does not take effect.**

### Accelerate copying local files to CFS
For Linux, use the following shell script to accelerate the copying of local files to CFS. The "number of threads" in the following code can be adjusted as needed.

```

threads=<number of threads>; src=<source path/>; dest=<destination path/>; rsync -av -f"+ */" -f"- *" $src $dest && (cd $src && find . -type f | xargs -n1 -P$threads -I% rsync -av % $dest/% )

<!--for example, threads=24; src=/root/github/swift/; dest=/nfs/; rsync -av -f"+ */" -f"- *" $src $dest && (cd $src && find . -type f | xargs -n1 -P$threads -I% rsync -av % $dest/% )-->

```

### An exception occurred while modifying file name/directory name in Windows
If a read/write exception or a failure to rename folder/file occurred while using the default subdirectory "nfs" to mount the file system, use FSID for mounting. The mount command is as follows. (FSID can be found in **Console** -> **File System Details** -> **Mount Point Information**.)
> mount <mount point IP>:/FSID <shared directory name>:
> //For example: mount 10.10.0.12:/z3r6k95r X:

![](https://main.qcloudimg.com/raw/d30598951413f86722aed46482e053f9.png)


### The file system has no write permission in Windows after being mounted using NFS
Add AnonymousUid and AnonymousGid to the registry as instructed, and then restart the system and try again. [View instructions](https://cloud.tencent.com/document/product/582/9133#.E5.9C.A8-windows-.E4.B8.8A.E4.BD.BF.E7.94.A8.E6.96.87.E4.BB.B6.E7.B3.BB.E7.BB.9F)
.

### Windows IIS cannot use mapped driver
Configure the correct NFS client program and modify the registry (add users who access the system) by following the steps in [Use File System in Windows](https://cloud.tencent.com/document/product/582/9133#.E5.9C.A8-windows-.E4.B8.8A.E4.BD.BF.E7.94.A8.E6.96.87.E4.BB.B6.E7.B3.BB.E7.BB.9F).
After the client is restarted, open the IIS configuration page, add a site, and click **Advanced Settings** to set the "Physical path" as the CFS mount point.

![](https://main.qcloudimg.com/raw/83580529ff0f22032f891e442dff1235.png)
![](https://main.qcloudimg.com/raw/b1a83b2a698428e569ab833f5132e37d.png)

### How can I continue using CFS in an availability zone with the CFS resources sold out?
Take Shanghai as an example. You have a CVM in Shanghai Zone 1 and you need to use CFS. However, you cannot directly create a file system, because the resources have been sold out in Shanghai Zone 1.

**In VPC network**
If the CVM resides in the "subnet of Shanghai Zone 1" in a VPC, you can log in to the [VPC console](https://console.cloud.tencent.com/vpc) to find the VPC and create a subnet of "Shanghai zone 2" for it.
![](https://main.qcloudimg.com/raw/a849aa72a6419206d43ab084a3e72f3d.png)
![](https://main.qcloudimg.com/raw/13d6a643a5a47d041ecfb5c01e24257f.png)
![](https://main.qcloudimg.com/raw/eab7adc8dc279c2baca89b9baec3a7fd.png)

After creating the subnet successfully, go back to the CFS console, and select this VPC and the subnet you just created to create resources in Shanghai Zone 2. The CFS file system can be directly mounted to the CVM in the subnet of Shanghai Zone 1 in this VPC. [View the file system mounting help documentation](https://cloud.tencent.com/document/product/582/11523).


**In basic network** 
If the CVM resides in a basic network, you can create a VPC and a subnet in Shanghai Zone 2, and then create a file system in this network. With "Classiclink", you can connect the CVM's basic network and the VPC to realize the access. [View Classiclink help documentation](https://cloud.tencent.com/document/product/215/5002).

### File update is not synced (metadata cache and noac option)

**Issue**
A NFS file system is mounted to two Linux CVMs. Use "append" to write a file to CVM A, and use "tail -f" to observe the changes to the file on CVM B. After data has been written into the file on CVM A, it takes 10-30 seconds for the updated content to display on CVM B. However, in the same scenario, if you open the file directly on CVM B (e.g. using the vi command), you can view the update immediately.

**Reason**
This issue is related to the option of the NFS mount command and the implementation of tail -f.

Mount command: sudo mount -t nfs -o vers=4 <mount point IP>:/ <target mount directory>  
 
If CVM B mounts the file system using NFS mount command, the kernel maintains a metadata cache of the file and directory attributes (including permissions, size, timestamp) by default. The purpose of caching is to reduce the number of NFSPROC_GETATTR Remote Procedure Calls (RPCs).

tail -f observes the changes to file attributes (mainly the file size) through sleep+fstat, then it reads the file and outputs the content. The result of fstat determines whether tail -f can output the file content in real time. However, due to the metadata cache of file and directory attributes, fstat cannot poll real-time file attributes. As a result, the file on the NFS server has been updated, but tail -f cannot observe the change, which causes output delay.

**Solution**
Add the noac option when mounting the file system with the mount command to disable the caching of file and directory attributes. The mount command is as follows:
sudo mount -t nfs -o vers=4 noac <mount point IP>:/ <target mount directory>
sudo mount -t nfs -o vers=3 noac,nolock,proto=tcp <mount point IP>:/<FSID or subdirectory> <target mount directory>




