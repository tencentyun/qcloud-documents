Windows file system typically uses NTFS or FAT32 format, while Linux file system often uses EXT series format. When the operating system is reinstalled and changed from Windows to Linux, its type has changed but the data disk remains the old format. Thus, denied access to the data disk file system may occur in the reinstalled system. You can perform the following operations on the reinstalled Linux CVM to read data from the data disk of the original Windows system:

1) Use the following command to install ntfsprogs software on the Linux system so that Linxu can support NTFS file system:

```
yum install ntfsprogs
```

2) Mount the data disk under Windows to Linux CVM. Skip this step if the data disk has already been mounted.

Log in to Tencent Cloud console, enter "Cloud Virtual Machine" - "Cloud Block Storage" tab, click on the Windows data disk to be mounted, and then click "More" - "Mount to Cloud Virtual Machine" button.  Select reinstalled Linux CVM in the pop-up box, then click "Confirm".

3) Use`parted -l`command to check the data disk mounted from Windows:
![](//mccdn.qcloud.com/static/img/f0839d9209bc0927bd5293b45fdc7608/image.png)

4) Use `mount -t ntfs-3g data disk path mount point' command to mount the data disk:
![](//mccdn.qcloud.com/static/img/cab81165b08034f2c300a2f30fccc8a4/image.png)

5) Since the file system is identifiable, Linux system can directly perform read and write operations on the mounted data disk.