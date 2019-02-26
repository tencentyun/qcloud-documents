The file system format of Windows is generally NTFS or FAT32, while that of Linux is EXT series. When the operating system is reinstalled and changed from Linux to Windows, its type has changed but the data disk remains the old format. Thus, denied access to the data disk file system may occur in the reinstalled system. You can perform the following operations on the reinstalled Windows CVM to read data from the data disk of the original Linux system:

1) Assume that the data disk of Linux CVM has two partitions:
![](//mccdn.qcloud.com/static/img/4a77fec831a1ad58b18cd86c31952789/image.png)

2) Download and install DiskInternals Linux Reader software on the reinstalled Windows CVM (For download address, please click [here](http://www.diskinternals.com/download/Linux_Reader.exe)).

3) Mount the data disk under Linux to Windows CVM. Skip this step if the data disk has already been mounted.

Log into Tencent Cloud console, enter "Cloud Virtual Machine" - "Cloud Block Storage" tab, click on the Linux data disk, and then click "More" - "Mount to Cloud Virtual Machine" button. Select reinstalled Windows CVM in the pop-up box, then click "Confirm".

4) Click to run DiskInternals, and you can see the information of data disk just mounted. /root/mnt and /root/mnt1 are for partitions vdb1 and vdb2 respectively:
![](//mccdn.qcloud.com/static/img/de1d02ddf0793da5911e0bece70a4993/image.png)

5) Click to enter /root/mnt, and right-click the file you want to copy, and select Save to save the file.
![](//mccdn.qcloud.com/static/img/9d95772257f0c000c47dbd5dfdf5d8ed/image.png)

6) Please note that the Linux data disk is read-only at this time. If you need to perform read and write operations on the data disk as Windows data disk, please first back up the files you need and then re-format it into a standard type supported by Windows operating system. For specific operations, please see [here](http://cloud.tencent.com/doc/product/213/Windows%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%99%A8%E6%95%B0%E6%8D%AE%E7%9B%98%E5%88%86%E5%8C%BA%E5%92%8C%E6%A0%BC%E5%BC%8F%E5%8C%96).



