When you have purchased a data disk, you need to format it before use. Users who do not purchase data disk can skip this step. You can also perform multi-partition operations as needed.

The following example shows how to format a data disk on Windows 2012R2.

1) Log in to Windows CVM by following the instructions described in Step Four.

2) Click "Start"-"Server Manager" - "Tools" - "Computer Management" - "Storage" - "Disk Management".

3) Right-click the name of the new data disk to format, click "Online"; When the hard disk status changes to "Not initialized", right-click "Initialize Disk", select partition style (GPT or MBR), and click "OK". Now the data disk status changes to "Online".
![](//mccdn.qcloud.com/static/img/3c62dd8d230b5499da6c917089ed0d41/image.jpg)
![](//mccdn.qcloud.com/static/img/693871277717dd1dc7756854b4e9e694/image.jpg)

4) Right-click on the space not partitioned in the data disk, click "New Simple Volume"; As instructed by the wizard, enter the size of disk partition, click "Next"; Select the file system, format the partition, click "Next"; Complete the creation of new simple volume, click "Finish".
![](//mccdn.qcloud.com/static/img/fbb1e9cb80721560b4a758b8017b019e/image.jpg)
![](//mccdn.qcloud.com/static/img/70bfd169da281a95b8b1368639fb52de/image.jpg)
![](//mccdn.qcloud.com/static/img/3604c5457164497ddddbb121ef252341/image.jpg)
![](//mccdn.qcloud.com/static/img/2332c03f9f1f03892fea31b648303473/image.jpg)

5) In the computer screen, you can see the data disk which has just been partitioned: 
 ![](//mccdn.qcloud.com/static/img/8475471ad2cc2212c063c493655a79da/image.jpg)