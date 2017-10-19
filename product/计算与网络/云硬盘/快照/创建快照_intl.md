You can regularly create snapshots as a kind of data backup after the data is written into a cloud disk. Tencent Cloud creates snapshots in an incremental way, that is, it only creates a snapshot for the data that is different from the last snapshot. Therefore, it can create snapshots in a short time when the data isn't changed much. Although snapshots are saved incrementally, the deletion of them will not affect your use of any snapshot data. The undeleted snapshots can recover the cloud disk to the status of the snapshot.

You can create snapshots in any status of the cloud disk, but snapshots can only save the data that has been written to the cloud disk at the time point of creation. If an application or process is writing data to the cloud disk at that moment, the data may not be saved. If you can pause file write for a while and create a snapshot, the snapshot will be complete. If the pause is not executable, it is recommended that you [uninstall](https://cloud.tencent.com/document/product/362/6740
) the cloud disk from the instance, and then create a snapshot and [re-connect it to the CVM instance](https://cloud.tencent.com/document/product/362/5745).

## Creating a Snapshot in Console
1) Open [CVM Console](https://console.cloud.tencent.com/cvm/).

2) Click "Cloud Block Storage" in the navigation pane.

3) Click the "Create Snapshot" button at the end of the cloud disk for which a snapshot needs to be created.

4) Wait for the snapshot to be created.

## Creating a Snapshot with API
Please refer to [CreateSnapshot API](https://cloud.tencent.com/doc/api/364/2529).
