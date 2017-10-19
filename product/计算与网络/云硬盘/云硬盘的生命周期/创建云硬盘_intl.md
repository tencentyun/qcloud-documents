You can create a cloud disk and connect it to any CVM instance in the same availability zone. Cloud disk is identified and used by CVM instance through block storage mapping. You can also activate a new cloud disk based on snapshot created previously. For more information, refer to [Creating Cloud Disk from Snapshot](/doc/product/362/5757). After being created, a cloud disk can reach the height of its performace without the prefetching process.

The creation method of cloud disk varies with cloud disk type. For more information on cloud disk types, refer to [Categories of Cloud Block Storage](/doc/product/362/2353).

## Creating Elastic Cloud Disk 

### Creating elastic cloud disk in console

1) Log in to [Cloud Block Storage Console](https://console.cloud.tencent.com/cvm/cbs), click ![](//mccdn.qcloud.com/static/img/acaf7d7ec8c66cd55ab9dd1be3319dfb/image.png) to purchase an elastic cloud disk.

2) In the pop-up box, select a region/availability zone, billing model (only "Annual or Monthly Plan" is supported currently), capacity, quantity and purchase period, and click **OK**.

3) Click **Payment Completed** in the payment page and complete the purchase. You can check the purchased cloud disk in the [CBS List Page](https://console.cloud.tencent.com/cvm/cbs). The elastic cloud disk you just purchased is unnamed by default, and has a status of **Pending mounted**.

> Note:
> 
- An elastic cloud disk can be freely mounted and dismounted among the CVMs within the same availability zone;
- The capacity of a single disk can be set to 10 G-4000 G, and a maximum of 10 elastic cloud disks can be created at a time.
- If you need to keep the data disk snapshot data in the new disk, you can enable **Use snapshot to create disks** and select the snapshot to be used. After selection of snapshot, the default disk capacity equals the snapshot size. You can change the capacity to a value greater than the default value.
![](//mccdn.qcloud.com/static/img/4fc60b3b41287146e6cbc8768a62f90b/image.png)

### Creating an Elastic Cloud Disk Using Snapshot
If you need to keep the data disk snapshots in the newly created disk, you can select this method.

1) Log in to [Snapshot Console](https://console.cloud.tencent.com/cvm/snapshot), click "New Cloud Disk" next to the snapshot to be used to purchase it.
![](//mccdn.qcloud.com/static/img/475d66590b426a60c862b9d20373a552/image.png)

2) In the pop-up box, select a region/availability zone, billing model (only "Annual or Monthly Plan" is supported currently), capacity, quantity and purchase period, and click "OK".
> Note:
> 
- An elastic cloud disk can be freely mounted and dismounted among the CVMs within the same availability zone;
- The default capacity of a newly purchased cloud disk equals the snapshot size. You can change the capacity to a value greater than the default value.
- A maximum of 10 elastic cloud disks can be created at a time.

3) Click "Payment Completed" in the payment page and complete the purchase. You can check the purchased cloud disk in the [CBS List Page](https://console.cloud.tencent.com/cvm/cbs). The elastic cloud disk you just purchased is named "From snap-xxxxxxxx" by default, with the status being **Pending mounted**.


### Creating an Elastic Cloud Disk with API
Please refer to [API CreateCbsStorage](https://cloud.tencent.com/document/api/362/2524).

## Creating Non-elastic Cloud Disk
### Creating a non-elastic cloud disk in console
Non-elastic cloud disk is created with the creation of CVM instance, with its lifecycle being same as that of the instance. For more information on how to create instances and select non-elastic cloud disk, refer to [Purchasing and Activating Instance](/doc/product/213/4855).

### Creating elastic cloud disk with API
Non-elastic cloud disk is created with the creation of CVM instance, with its lifecycle being same as that of the instance. For more information on how to create instances and select non-elastic cloud disk, refer to [API RunInstances](https://cloud.tencent.com/doc/api/229/1248) and [API RunInstancesHour](https://cloud.tencent.com/doc/api/229/1350)
