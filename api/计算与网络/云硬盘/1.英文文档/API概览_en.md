
## 1. Cloud disk-related APIs

| API Name | Action Name | Description |
| --------- | --------- | ----- |
| [Modify cloud disk attributes](/doc/api/364/2523) | ModifyCbsStorageAttributes | Modify cloud disk attributes |
| [Query cloud disk information](/doc/api/364/2519) | DescribeCbsStorages | Query the details of cloud disk based on user's input, such as disk type, availability zone, etc. |

## 2. Elastic Cloud Storage-related APIs

| API Name | Action Name | Description |
| --------- | --------- | ----- |
| [Create elastic cloud storage](/doc/api/364/2524) | CreateCbsStorages | Purchase a new elastic cloud storage based on specified configuration |
| [Mount elastic cloud storage](/doc/api/364/2520)  | AttachCbsStorages| Mount the specified elastic cloud storage to the specified CVM |
| [Unmount elastic cloud storage](/doc/api/364/2521) | DetachCbsStorages | Unmount the specified elastic cloud storage from the specified CVM |
| [Renew elastic cloud storage](/doc/api/364/2526) | RenewCbsStorage | Renew the specified elastic cloud storage |
| [Expand elastic cloud storage](/doc/api/364/2527) | ResizeCbsStorage | Expand the capacity of specified elastic cloud storage |
| [Inquire about price of elastic cloud storage](/doc/api/364/2522) | InquiryStoragePrice | Make a inquiry about the price of specified type of elastic cloud storage |
| [Query number of elastic cloud storages mounted to CVM](/doc/api/364/2528)  | DescribeInstancesCbsNum | Query the number of elastic cloud storages mounted to the CVM |

## 3. Snapshot-related APIs

| API Name | Action Name | Description | 
| -------- | --------- | ------ |
| [Create snapshot](/doc/api/364/2529) | CreateSnapshot | Create a snapshot for the specified cloud disk |
| [Query snapshot list](/doc/api/364/2530) | DescribeSnapshots | Query the details of a snapshot based on specified parameters such as cloud disk ID, type etc. |
[Modify snapshot name](/doc/api/364/2532) | ModifySnapshot | Modify the display name of specified snapshot |
| [Rollback snapshot](/doc/api/364/2533) | ApplySnapshot | Rollback snapshot to original cloud disk |
| [Delete snapshot](/doc/api/364/2531) | CreateSnapshot | Delete the specified snapshot |



