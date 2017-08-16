When you have purchased a data disk, you need to format it before use. Users who do not purchase data disk can skip this step. The following example shows the way to do this on CentOS.
> Note: It only supports partitioning of data disk, not system disk. Forced partitioning of system disk may lead to system crash or other serious problems, for which Tencent Cloud will not be held liable.

1) Log in to Linux CVM by following the instructions described in Step Four.

2) Enter the command `fdisk -l` to check the data disk information. Note that using the command `df -h` will not display the information of the data disk if it has not been partitioned and formatted. In the example below, a 54GB data disk (/vdb) needs to be mounted.
![](//mccdn.qcloud.com/static/img/c0ba873e2488ad593d7a5e16585b50fb/image.png)

3) Execute the following command to partition data disk.
```
fdisk /dev/vdb
```
By following the instructions on the interface, enter "n" (create a new partition), "p" (create an extended partition), and "1" (use the first primary partition) in turn, press Enter twice (use default settings), then enter "wq" (save partition table) and press Enter to start partitioning.
The example here creates one partition. Developers can create multiple partitions according to their needs.

![](//mccdn.qcloud.com/img56a604c2b886f.png)

Use "fdisk -l" command to check that the new partition vdb1 has been created.
![](//mccdn.qcloud.com/img56a605027a966.png)

5) The newly created partition then needs to be formatted, and you can decide which file system format, such as ext2 and ext3, to use by yourself. The example here uses "ext3".

Use the following command to format the new partition. 

```
mkfs.ext3 /dev/vdb1
```
![](//mccdn.qcloud.com/img56a6053fb5aa0.png)

2) Use the following command to create mydata directory and mount the partition under this directory:
```
mkdir /mydata
mount /dev/vdb1 /mydata
```
Finally, use the following command to make a check
```
df -h
```
The appearance of the message as shown below indicates that the mounting is successful and you can view the data disk. 
![](//mccdn.qcloud.com/img56a60615c0984.png)

7) If you want the data disk to be automatically mounted to CVM when CVM is restarted or booted up, you need to add the partition information to /etc/fstab. If you do not, the data disk will not be automatically mounted to the CVM when the CVM is restarted or rebooted.

Use the following command to add partition information:
```
echo '/dev/vdb1 /mydata ext3 defaults 0 0' >> /etc/fstab
```

Use the following command to make a check.
```
cat /etc/fstab
```

The appearance of the message as shown below indicates that the partition information has been successfully added.
![](//mccdn.qcloud.com/img56a606ad3180c.png)