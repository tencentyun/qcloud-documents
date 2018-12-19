### 1. How is elastic cloud storage billed?

Currently, elastic cloud storage only provides monthly or annual prepaid methods.

### 2. Which regions are available for purchase for elastic cloud storage?

Currently, Guangzhou Zone 2, Shanghai Zone 1 and Beijing Zone 1 are available for purchase

### 3. Can I unmount the data disk that I purchased along the CVM?

Mounting or unmounting features are not available for non-elastic cloud storage. They're under development and will be fully available in the future. All cloud block storage (data disk) of Tencent Cloud will support mounting and unmounting in the future.

### 4. How to purchase elastic cloud storage?

Log in to Tencent Cloud Console and click on the "Cloud Block Storage" tab on the left to purchase.

### 5. Can I batch mount or batch unmount elastic cloud disks?

Yes.

### 6. Are there any restrictions with purchasing elastic cloud storage?

The maximum number of disks that can be mounted to a single CVM: 10;

The maximum number of elastic cloud disks with a single purchase: 10;

The maximum number of elastic cloud disks that a single account is allowed to purchase: 500.

### 7. Do I need to reboot the CVM after I finished mounting operation in the console?

CVMs purchased after March 10, 2016 can identify newly mounted data disks without rebooting.
As for CVMs with the following operating systems purchased before the above date, it is recommended to reboot the CVM and run some commands to enable its capability of identifying elastic cloud block storage (i.e. hot-plug function), please refer to [Note about Disk Identification Capability for CVMs of Certain Systems](http://cloud.tencent.com/doc/product/362/%E9%83%A8%E5%88%86%E5%AD%98%E9%87%8F%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%99%A8%E6%97%A0%E6%B3%95%E8%AF%86%E5%88%AB%E5%BC%B9%E6%80%A7%E4%BA%91%E7%9B%98%E7%9A%84%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95).


<table>
<tbody>
<tr><th></th><th>Version of CVM Operating System</th>
<tr><td rowspan="4">CentOS</td><td> 5.11 64-bit</td>
<tr><td>5.11 32-bit</td>
<tr><td>5.8 64-bit</td>
<tr><td>5.8 32-bit</td>
<tr><td >Debian</td><td> 6.0.3 32-bit</td>
<tr><td rowspan="2">Ubuntu</td><td> 10.04 64-bit</td>
<tr><td>10.04 32-bit</td>
<tr><td rowspan="2">OpenSuse</td><td> 12.3 64-bit</td>
<tr><td>12.3 32-bit</td>
</tbody>
</table>
	

### 8. How to deal with elastic cloud block storage when it expires?

The elastic cloud storage can still be used within<font color="red"> 7 days </font>after it expires, after which it will be transferred to the Recycle Bin and become frozen for 7 days, during which any read or write operations are not allowed. Its functions will be recovered after renewal. If it is not renewed at the end of the freeze period, the hard disk will be destroyed, in which case all data will be lost permanently.

### 9. Are there any restriction with mounting disks in Linux operating system?

You can mount disks as you wish in Linux without any restrictions. 
As for common website services, vda is our system disk, and vdb is our data disk (elastic cloud storage). With df -h, we can see that the vda disk is mounted on the root partition, so you can mount the vdb disk in /data. 
As a common practice, apache/nginx and other softwares are installed into vda, that is, in the root disk; data directory of mysql and web content of nginx should point to vdb, that is, the data directory under the root.

### 10. When unmounting elastic cloud storage, will its data be lost?

We strongly recommend that: 
- In Windows operating system, in order to ensure data integrity, it is recommended that you suspend all read and write operations on all file systems of the disk, otherwise the data in the middle of read/write process will be lost. 
- In Linux operating system, you need to log in to the CVM instance and perform unmount command line operation to the disk, then enter the console to unmount the disk after the command is successfully performed.

### 11. I can't find the CVM to which I want to mount my elastic cloud storage?

Make sure that your CVM instance and disk are in the same availability zone in the same region. An independent cloud block storage can only be mounted in the same availability zone of the same region. Meanwhile, ensure that your instance is not released.

### 12. Will the data on the disk be deleted immediately when the elastic cloud storage expires?

Assume that the user's elastic cloud storage expires on March 8, 2016, Tencent Cloud will remind the user to renew 7 days before the expiration date (March 1). The user will be able to use the elastic cloud storage as usual within 7 days from the date of expiration. After 7 days from the date of expiration, the expired elastic cloud storage will be moved to the Recycle Bin, and the user will not be able to perform any operation other than renewal. If the elastic cloud storage is not renewed 7 days after being moved to the Recycle Bin, it will be released and all data on the disk will be erased.

### 13. When several elastic cloud storages with the same size and the same type are mounted on a same sub-machine, how do I distinguish the relation between these disks and the elastic cloud storage actually purchased?

For Linux operating system, you can view the relation between the elastic cloud storages and device names by executing the `ls -l /dev/disk/by-id ` command:
![](//mccdn.qcloud.com/static/img/56e625dd23adfb78829d34a7e86e9291/image.png)

For Windows operating system, you can execute the `wmic diskdrive get caption,deviceid,serialnumber` or `wmic path win32_physicalmedia get SerialNumber,Tag` command to view:
![](//mccdn.qcloud.com/static/img/205b1060c7bc7446becddee81971c506/image.png)

### 14. Is there anything I should remember when using elastic cloud block storage?
- For an independently purchased cloud block storage, when configuring static file system information using fstab, the UUID or label of the file system should be used as the file system ID, to prevent changes of the kernel name of Cloud Block Storage in the submachine due to multiple mounting/unmounting of multiple independent disks on the same submachine. 
- Note that if the elastic cloud block storage expires before the CVM, the cloud block storage will be forcibly removed from the CVM. Please renew your elastic cloud block storage in time to prevent your business from being affected.
- If the removal of elastic cloud block storage from the CVM does not affect your critical business, you can choose to use nofail option when configuring fstab, to prevent system error upon reboot after the elastic cloud block storage is removed from the CVM.
- For Windows system, it is recommended that you execute the san policy=OnlineAll operation in diskpart before using the cloud block storage.
- In Windows system, before unmounting elastic cloud block storage, it is recommended that you cancel all operations on the elastic cloud block storage and perform the "offline" operation.

