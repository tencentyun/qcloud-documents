Rolling back snapshot data to a cloud disk can recover the disk data to the state when the snapshot is created. This method is very useful in case of data errors or data losses caused by certain changes.

Snapshots can only be rolled back to the cloud disk in which they are created. If you need to get snapshot data from other cloud disks, please use the service of [Creating a Cloud Disk from a Snapshot](/doc/product/362/5757).

Note:

- When you roll back a snapshot to an elastic cloud disk, the disk must be unmounted.
- When you roll back a snapshot to a non-elastic cloud disk purchased with a CVM, the CVM instance must be shut down.

## Rolling Back a Snapshot in Console
1) Open [CVM Console](https://console.cloud.tencent.com/cvm/).

2) Click "Snapshot" in the navigation pane.

3) Select the snapshot that needs to be rolled back to the disk in the snapshot list, and click "Rollback".

## Rolling Back a Snapshot with API
Please refer to [ApplySnapshot API](https://cloud.tencent.com/doc/api/364/2533).
