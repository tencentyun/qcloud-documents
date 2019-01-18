### How does CDM work?

CDM is a process of accelerating the migration of terabytes or petabytes of data to the cloud with the aid of secure and reliable devices. First, you need to determine the required number of dedicated migration devices based on the volume of the data to be migrated and submit an application for device delivery in the console. Then, after receiving the devices from Tencent Cloud, you copy the data to the devices and submit an application for device return in the console. Finally, after receiving the returned devices, Tencent Cloud copies the data to cloud storage and completes the data migration.


### When choose CDM?

If you want to efficiently and securely migrate terabytes or petabytes of data from your local IDC to Tencent Cloud without having to upgrade your IDC with expensive network bandwidth, or relieve local storage pressure and back up your data to the cloud at low costs, CDM will be your best choice.  
Before using CDM, you can first evaluate the upload bandwidth of your current network. The recommended usage scenarios are as follows:  
- Scenario 1: For this migration task, it would take more than one week if migrated online.
- Scenario 2: For this migration task, the volume of the data to be migrated exceeds 50 TB.

Based on the data volume and network bandwidth capabilities, we provide the following figure for your reference (with theoretical values).

![](https://main.qcloudimg.com/raw/bbcecbd46f146dba5412a43d8f4b95a6.png)


### What is the data capacity that can be transferred through CDM?

At present, Tencent Cloud offers two migration device options. By applying for multiple devices for simultaneous operation, almost any volumes of data can be transferred. For example, you can apply for two 80-TB devices to copy 150 TB of data in parallel.


### How is data secured during migration?

The migration device automatically encrypts the copied data, and the key will not be sent to or stored on the device, ensuring that the data is inaccessible to others. RAID5 disk array is used to protect data integrity and prevent data loss due to disk damage. After all the data is uploaded to the cloud, Tencent Cloud will completely erase the data in the device, ensure your data is completely secure.



### How long can I hold the migration device?

If no special reasons, you need to submit the application for device return within 30 days. Otherwise, the device will be deemed as lost and all the deposit will be deducted.


### Can the migration destination be something other than Tencent Cloud?

No. Your data can only be migrated from your source data address to Tencent Cloud. Currently, data export from Tencent Cloud is not supported.


### Can the migration device be purchased?

No. Tencent Cloud does not sell migration devices. Fees are charged based on actual usage.

