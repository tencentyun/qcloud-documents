




## Mounting a data disk automatically when launching a new instance using custom image and data disk snapshot (Linux)
When a new CVM instance is launched, if you specify ***custom image*** and ***data disk snapshot***, Tencent Cloud's cloud disk can be automatically mounted after the launch of CVM instance (read and write data directly without the need to perform operations such as addition, partitioning and formatting). You need to perform some operations on the original instance before making custom images and data disk snapshots, which will be described in detail below.

On the Linux system, if you want the cloud disk produced from the specified data disk snapshot to be automatically mounted to the new CVM instance, the specified custom image and data disk snapshot must meet the following requirements:
- The data disk ***must*** be formatted before the snapshot is generated. That is, the data disk has been successfully mounted to the original CVM.
- Before making a custom image on the system disk, you need to add the following command to the file `/etc/rc.local` to write the data disk mount point to the file:

```
mkdir -p <mount-point>
mount <device-id> <mount-point>
```

Enter the mount point of file system in `<mount-point>`, such as `/mydata`, and the actual file partition location in `<device-id>`, such as `/dev/vdb (device without partition and with file system)` and `/dev/vdb1 (device with both partition and file system)`.

Only when both of the conditions are met can the data disk of the launched Linux CVM instance be automatically recognized and mounted.




---





## Mounting a data disk automatically when launching a new instance using custom image and data disk snapshot (Windows)
When a new CVM instance is launched, if you specify ***custom image*** and ***data disk snapshot***, Tencent Cloud's cloud disk can be automatically mounted after the launch of CVM instance (read and write data directly without the need to perform operations such as addition, partitioning and formatting). You need to perform some operations on the original instance before making custom images and data disk snapshots, which will be described in detail below.

On the Windows system, if you want the cloud disk produced from the specified data disk snapshot to be automatically mounted to the new CVM instance, the specified custom image and data disk snapshot must meet the following requirements:

- The SAN policy in the custom image is `onlineAll`. Public images for Windows provided by Tencent Cloud have been configured as such, but it is recommended to check the configuration before creating any custom image by following the step below:
![](//mccdn.qcloud.com/static/img/74e490afd81bd7ad9fc9590565b48a80/image.jpg)

- The data disk must have been formatted as `ntfs` or `fat32` before you make a snapshot.

Only when both of the conditions are met can the data disk of the launched Windows CVM instance be automatically recognized and mounted.
