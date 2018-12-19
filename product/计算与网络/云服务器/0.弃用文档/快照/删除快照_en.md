For a data status that will not be used anymore, you can delete the snapshot created at that moment. When you delete a snapshot, only the data exclusive to the snapshot will be deleted, and the cloud disk in which the snapshot is created will not be affected. In addition, deleting a snapshot created earlier in a cloud disk will not affect the use of snapshots created later, which means, each snapshot data provided by Tencent Cloud can independently recover a cloud disk to the data status when the snapshot is created.

## Deleting a Snapshot in Console
1) Open [CVM Console](https://console.cloud.tencent.com/cvm/).

2) Click "Snapshot" in the navigation pane.

3) Click the "Delete" button at the end of the snapshot entry to be deleted.

Or batch deletion:

1) Open [CVM Console](https://console.cloud.tencent.com/cvm/).

2) Click "Snapshot" in the navigation pane.

3) Check all the snapshots you want to delete (make sure the snapshots are not involved in any tasks), and click "Delete".

## Deleting a Snapshot with API
Please refer to [DeleteSnapshot API](https://cloud.tencent.com/doc/api/364/2531).
