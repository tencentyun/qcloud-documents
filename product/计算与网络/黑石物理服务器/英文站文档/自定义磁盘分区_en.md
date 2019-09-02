Cloud Physical Machine (CPM) allows you to specify the number of partitions and capacity of disk before installing or reinstalling the operating system.

## Customizing Disk Partitions
You can customize disk partitions by following the rules below:
<li>Disk partitioning and specifying partition sizes are only allowed for SDA disks.</li>
<li>All non-SDA disks will be mounted to the /dataX partition, x=1, 2, 3...</li>
<li>On an SDA disk, the partitions allowed to be created include: root, /swap, /usr/local, and /data partitions. You can specify the sizes for the different partitions. Except the root partition that must be created, any other partitions are optional.</li>
<li>For the CPM started using UEFI method, /boot/uefi partition is required, and /swap partition is not created by default.</li>
<li>If you want to create /swap, /usr/local, /data and other partitions, the partition size should be at least 1G.</li>
<li>The capacity not explicitly allocated to any partition will be included into *<font color='red'>root partition</font>* during the installation of operating system</li>
![](http:////mc.qcloudimg.com/static/img/d3778be090dac54af50964a103fbcb50/image.png)

## GB and GIB
Please note the size unit used when creating partitions</br>
<li>GB, the abbreviation for Gigabyte, is a decimal capacity unit and means 109 bytes. Hard disk manufacturers use it to indicate the hard disk capacity.</br></li>
<li>GIB, the abbreviation for Giga binary byte, is a binary capacity unit and means 230 bytes. Operating system uses it to indicate the partition size.</li></br>
Their conversion formula is as follows:
<li>1 GB = 1\*1000\*1000\*1000/1024/1024/1024 = 0.93 GIB </li>
If you purchase a 300 G SAS disk, the returned size for the query via df - h in system is 279 GIB.</br>
*For the customization of partitions, GIB is used as the unit for measuring partition size.*
