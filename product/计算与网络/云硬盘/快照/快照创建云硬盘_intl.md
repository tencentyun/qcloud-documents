A cloud disk created from a snapshot has all the data of the snapshot upon creation, so you don't need to perform operations such as [partitioning, formatting and creating file system](https://intl.cloud.tencent.com/document/product/362/6734
), because the data on the cloud disk would be all erased through formatting. After creating a cloud disk from a snapshot and [connecting it to a CVM instance](/doc/product/362/5745), users can read and write all the data normally on the snapshot. Therefore, snapshots are an important way for data sharing and migration.

## Creating a Cloud Disk from a Snapshot in Console
1) Open [CVM Console](https://console.cloud.tencent.com/cvm/).

2) Click "Snapshot" in the navigation pane.

3) Select the data disk snapshot to be used for disk creation in the snapshot list, and click "Use snapshot to create disks".

4) In the pop-up box, select a region/availability zone, billing model (Only "Annual or Monthly Plan" is supported currently), capacity, quantity and purchase period, and click "OK".

> Note:
> 
- The default capacity of a newly purchased cloud disk equals the snapshot size. You can change the capacity to a value greater than the default value.
- A maximum of 10 elastic cloud disks can be created at a time.

## Creating a Cloud Disk from a Snapshot with API
Please refer to [CreateCbsStorages API](https://cloud.tencent.com/document/api/364/2524).
