For newly purchased Linux CVM, the data disk is unusable without being partitioned and formatted.
>Note:

> <font color="red">Once formatted, all the data in the disk will be cleared. Make sure that there is no data left in the disk or the important data has been backed up before formatting. To avoid any service exception, make sure that the CVM has stopped providing services before formatting. </font>

## 1. View the list of disks
Use the following command to view the disk device list:
```
fdisk –l
```

For FreeBSD system, please use the following command:

```
diskinfo -v /dev/vtbd1
```
![](//mccdn.qcloud.com/img56a6086d43aa3.png)
![](//mccdn.qcloud.com/img56a616a9911da.png)

## 2. Create GPT partitions
Use parted tool to create GPT partitions 
![](//mccdn.qcloud.com/img56a608a4b9d93.png)

For FreeBSD system, please follow the following steps:
Execute ‘gpart create -s gpt vtbd1`command
![](//mccdn.qcloud.com/img56a6171206c80.png)

Execute 'gpart add -t freebsd-ufs -a 1M vtbd1' command
![](//mccdn.qcloud.com/img56a6172bb39c0.png)

## 3. View new partition information
You can use the following command to view the new partition information after a partition is created:
```
fdisk –l
```
![](//mccdn.qcloud.com/img56a608e6c6545.png)

## 4. Formatting of partitions
Use mkfs tool to format partitions
![](//mccdn.qcloud.com/img56a609267ccb7.png)


For FreeBSD system, use newfs tool to format partitions. Enter the following command:

```
newfs -j /dev/vtbd1p1
```

## 5. Mount new partitions
Use the following command to mount a new partition after formatting is completed.
```
mount file system partition path mount point
```
Now use the following command to check the remaining capacity of disk.
```
df –h
```
![](//mccdn.qcloud.com/img56a60985596aa.png)
![](//mccdn.qcloud.com/img56a617f21cae1.png)

## 6. Set up Auto Mount
Modify fstabl file to set it to mount the new partition automatically during system restart. Add the content in the last line as shown below.
![](//mccdn.qcloud.com/img56a609b19718b.png)

For FreeBSD system, modify /etc/fstab file to set it to mount the new partition automatically during system restart. Add the content in the last line as shown below.
![](//mccdn.qcloud.com/img56a6188004bac.png)