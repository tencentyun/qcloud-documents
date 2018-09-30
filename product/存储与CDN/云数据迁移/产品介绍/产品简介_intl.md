

## Overview
Cloud Data Migration (CDM) is a data migration service offered by Tencent Cloud for cloudification of terabytes and petabytes of data. CDM uses dedicated migration devices to quickly and efficiently migrate data from your IDC to the cloud and protects data security during migration with RAID, encryption and other methods to minimize the risk of data corruption and leakage.

CDM is very simple to use. First, you need to create and submit a migration task in the CDM Console, and Tencent Cloud will mail the dedicated migration device to you. Once you receive the device, you need to add it to your local network environment for connection with your IDC. Once connected, you can perform a data copy operation. During the process, the migration device automatically encrypts and verifies the data. After all the data is copied, you need to submit a return request for the current task in the console. Tencent Cloud will take care of retrieving the device and uploading your data to the cloud. You can track the task status at any time in the console throughout the migration process.


## Features

### Efficient Transfer
The migration device uses 10-Gigabit network interface for connectivity and is optimized for small file transfers to minimize transfer time. If you have 1 PB of data to migrate, it would take nearly 4 months in a 1-Gbps bandwidth environment, but with multiple migration devices to work simultaneously, the migration can be completed in just a few days.


### Security Protection

The migration device automatically encrypts the copied data, and the key will not be sent to or stored on the device, ensuring that the data is inaccessible to others. RAID5 disk array is used to protect data integrity and prevent data loss due to disk damage. After all the data is uploaded to the cloud, Tencent Cloud will completely erase the data in the device, ensure your data is completely secure.



### Status Tracking

Tencent Cloud records the latest status of the migration task in real time and will update you on the status through email or SMS. You can also view the current status of the task at any time in the console.




## Device Details

CDM offers two device options with different storage capacity: M30 for 30 TB and L80 for 80 TB. The device specs are as below:

| Migration device | Storage capacity | Supported interfaces | Dimensions | Power supply | Power |
|------ | ---------- |------|---------|-------|-----|
| M30 | 30 TB | USB 3.0 port x 1 |28 cm x 16 cm x 22 cm | 220 V | 150 W |
| L80 | 80 TB | 10-Gbps Ethernet electrical port x 2 | 48 cm x 92 cm x 9 cm | 220 V | 220 W |






