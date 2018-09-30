<font color="red">This method applies only to partitioning and formatting of hard disk less than 2TB. For any hard disk larger than 2TB, please use GPT mode. </font>

<br>

For newly purchased Linux CVM, the data disk is unusable without being partitioned and formatted.

You can perform formatting of Linux CVM data disk by means of script formatting or manual formatting.

>Note:

> <font color="red">Once formatted, all the data in the disk will be cleared. Make sure that there is no data left in the disk or the important data has been backed up before formatting. To avoid any service exception, make sure that the CVM has stopped providing services before formatting. </font>

## 1. Formatting of script (only for non-Ubuntu operating system)
The script formatting here applies only to the machine with a default user name of root. For any machine with a default user name of ubuntu, please use manual formatting. 

1) Write the IP of the CVM to operate, ssh port number and the password for root account to the hosts.txt file, with each line representing one host, for example:
```
10.0.0.1 22 my_password
```
2) [Click here](http://cos.myqcloud.com/11001086/deldiskscript/batch-mkfs.tgz?res_content_disposition=attachement;&secretId=AKIDj1rrU6Cio35u8xTdWIVIUorgnHhxqyjw&time=1440581110) to download formatting script.

3) Execute the following command at terminal
```
./batch-mkfs.py
```

In addition, if you want to perform the same operations in your own CVM shell, enter the following commands directly in the shell:

```
if grep -q /data /etc/fstab ; then uuid=notneed; echo /data already in fstab; else uuid=`mkfs.ext3 /dev/vdb
 > /dev/null 2>&1 && blkid /dev/vdb | awk '{print $2}'`;fi;if [[ $uuid == UUID* ]]; then echo $uuid /data 
ext3 noatime,acl,user_xattr 1 0 >> /etc/fstab; mount -a; else echo mkfs failed; fi;
```

## 2. Manual formatting
Please perform partitioning and formatting on data disk using the following steps, and mount partitions so that the data disk is usable.

>Note:
-When executing the following commands, please remember to modify the data drive letter. You can use "fdisk -l" to check drive letter and other information. vdb is used in the following examples for illustration. To use another drive letter, simply replace vdb with the drive letter. For example, replace fdisk /dev/vdb with fdisk /dev/xvdb
- Please verify that the path is “/dev/vdb”. The wrong entry of “/dev/vda” will lead to crash of CVM. 

### 2.1. View data disk information

After logging in to Linux CVM, you can use “fdisk -l” command to view the information about data disk.
> Note: Using "df- h" command will make it impossible to view unpartitioned or unformatted data disks. 

![](//mccdn.qcloud.com/img56a60467e297b.png)

### 2.2. Data disk partitioning
Execute the following command to partition data disk.
```
fdisk /dev/vdb
```
By following the instructions on the interface, enter “n” (create a new partition), “p” (create an extended partition), and “1” (use the first primary partition) in turn, press Enter twice (use default settings), and then enter “w” (save partition table) to start partitioning.
The example here creates one partition. Developers can create multiple partitions according to their needs.

![](//mccdn.qcloud.com/img56a604c2b886f.png)

### 2.3. Check new partitions
Use “fdisk -l” command to check that the new partition vdb1 has been created.
![](//mccdn.qcloud.com/img56a605027a966.png)

### 2.4. Formatting of new partitions
When formatting partitions, developers can decide the file system format on their own, such as ext2, ext3 and so on. The example here uses "ext3".

Use the following command to format the new partition. 

```
mkfs.ext3 /dev/vdb1
```
![](//mccdn.qcloud.com/img56a6053fb5aa0.png)

### 2.5. Mount new partitions
Use the following command to create mydata directory:
```
mkdir /mydata
```
Then use the following command to manually mount the new partition:
```
mount /dev/vdb1 /mydata
```
Finally, use the following command to make a check
```
df -h
```
The appearance of the message as shown below indicates that the mounting is successful and you can view the data disk. 
![](//mccdn.qcloud.com/img56a60615c0984.png)

### 2.6. Add partition information 
If you want the data disk to be automatically mounted to CVM when CVM is restarted or booted up, you need to add the partition information to /etc/fstab. If you do not, the data disk will not be automatically mounted to the CVM when the CVM is restarted or booted up.

> Note: Please verify whether the partition path is "/dev/vdb1" . Wrong path will lead to the failure of restarting of CVM.

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