

This manual provides guidance on how to use the migration device CDM-L80 to copy data.

## Overview
CDM-L80 is a cloud data migration device that is used as a server for offline data migration. The device has 80 TB of storage capacity and two 10-Gbps Ethernet electrical ports. You can copy your local data to CDM-L80 and then migrate the data to the cloud.
<span id="Device Connection Topology Figure"></span>

## Related Descriptions
### 1. Topological connection
![](https://main.qcloudimg.com/raw/00122cf1125e98615eb938d6c57da4c9.png)   
- CDM-L80: A dedicated data migration device with 80 TB of storage capacity sent to you.
- Switch: A switch for connecting external devices such as CDM-L80 provided by you.
- Storage mount point: A device that can connect to your local data storage environment.

### 2. CDM-L80's logical structure

Initial configuration has been completed for all migration devices. The logical structure of CDM-L80 can be divided into four parts through initialization as shown in the figure below:

![](https://main.qcloudimg.com/raw/dff7d00ac332f9624550b0c69188b09f.png)

* The top layer is the NFS layer which provides NFS services, making it easy for you to access the file system on CDM-L80.
* The middle layer is the data protection layer which automatically encrypts the copied data to ensure that file information cannot be obtained from the disk, so that even if the disk is lost, the data is still secure. Meanwhile, data consistency and integrity are guaranteed by configuring an RAID disk array, ensuring usability even in cases of damage to some disks during transportation.
* The underlying layer is the physical layer which stores the migrated data.

### 3. How it works
![](https://main.qcloudimg.com/raw/95cbfedde07851c1a31650cc6d37fbb9.png)  
After receiving a CDM-L80, you need to locally mount the shared directory `/dataseal` in it to perform data copy. (It is recommended that each bucket be a separate folder directory named after the bucket name.)

## Steps


### 1. Connect a network cable and power on
Connect a network cable to CDM-L80 and power it on as demonstrated in [Device Connection Topology Figure](#Device Connection Topology Figure).

### 2. Configure IP

#### 2.1 Log in
Connect the migration device with monitor and keyboard and log in to the system with the migration account (username: admin, password: Move@cdm2018).
![](https://i.imgur.com/8Ml6aPV.png)

#### 2.2 Switch user directory
Run command `cd` to switch to the admin user directory (`/home/admin`). The command is as below:
```
/home/admin
```
#### 2.3 Run IP reset script ip-conf.sh
Execute the following command:
```
./ip-conf.sh
```
![](https://i.imgur.com/Pib8rT3.png)    
#### 2.4 Enter information such as IP and save
During the execution, the VI edit window will pop up. Enter the IP address, gateway and mask information as prompted and save.
![](https://i.imgur.com/aMvE11z.png)  
>**Note:** 
> Up to two valid IP addresses can be entered and separated by a space. If only one IP address is entered, only one network interface (eth0 by default) will be configured.

#### 2.5 Restart to complete the configuration
After the script is executed, restart the device using the power button and the IP address will be automatically reset and take effect.

### 3. Mount directory

At this point, the migration device CDM-L80 is connected to your network environment. Before migrating the data, you need to mount the shared directory (`/dataseal`) of the NFS service in CDM-L80 to a local directory and run the mount command on the storage mount point in the following format:
```
mount -t nfs <nfs server IP>:/dataseal local mount point directory 
```

It is recommended that you mount the migration device's shared directory `/dataseal` to different mount points through two network interfaces, which can speed up the migration through parallel copying.

For example, if the corresponding IP addresses of the migration device numbered `ABC123` are `192.168.1.100,192.168.1.101`, mount the device's NFS shared directory `/dataseal` to `/mydata100` and `/mydata101` directories of the storage mount points and execute the following commands in sequence:
```
mount -t nfs 192.168.1.100:/dataseal /mydata100
```
and 
```
mount -t nfs 192.168.1.101:/dataseal /mydata101
```



### 4. Copy data
Use the relevant copy command to copy the data to the local mount point directories (such as `/mydata100，/mydata101` in the example above). It is recommended to use a copy tool with pause and resume support such as RSync.
Below describes how to copy the data to the migration device with RSync:
```
/ / Assume that your data is stored in the local folder /data
rsync -avh --progress /data/ /mydata100/

/* Parameter descriptions
-a: transfer folder
-v: detailed mode output
-h: output file size in an easy-to-read unit such as KB and MB
--progress: migration progress
*/
```

### 5. Power off and send back 

Power off the device using the power button, remove the network cable and then contact your Tencent Cloud representative to initiate a return request.

