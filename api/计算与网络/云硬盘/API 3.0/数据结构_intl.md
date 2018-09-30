## Disk

The details of a cloud disk

| Name | Type | Required | Description |
|------|------|----------|------|
| DiskId | String | No | Cloud disk ID. |
| DiskUsage | String | No | Cloud disk type. Value range:<li>SYSTEM_DISK: System disk</li><li>DATA_DISK: Data disk |
| DiskChargeType | String | No | Billing method. Value range:<li>PREPAID: Prepaid</li><li>POSTPAID_BY_HOUR: Postpaid</li> |
| Portable | Boolean | No | Whether it is an elastic cloud disk. false: Non-elastic cloud disk; true: Elastic cloud disk. |
| Placement | Placement | No | Location of the cloud disk. |
| SnapshotAbility | Boolean | No | Whether the cloud disk has the capability to create snapshots. Value range:<li>false: No.</li><li>true: Yes.</li> |
| DiskName | String | No | Cloud disk name. |
| DiskSize | Integer | No | Cloud disk size. |
| DiskState | String | No | Status of the cloud disk. Value range:<li>UNATTACHED: Unmounted</li><li>ATTACHING: Mounting</li><li>ATTACHED: Mounted</li><li>DETACHING: Unmounting</li><li>EXPANDING: Expanding capacity</li><li>ROLLBACKING: Rolling backing</li> |
| DiskType | String | No | Type of cloud disk medium. Value range:<li>CLOUD_BASIC: HDD cloud disk</li><li>CLOUD_PREMIUM: Premium cloud storage</li><li>CLOUD_SSD: SSD cloud disk</li> |
| Attached | Boolean | No | Whether the cloud disk is mounted to the CVM. Value range:<li>false: Unmounted</li><li>true: Mounted</li> |
| InstanceId | String | No | ID of the CVM to which the cloud disk is mounted. |
| CreateTime | Timestamp | No | Creation time of the cloud disk. |
| DeadlineTime | Timestamp | No | Expiration time of the cloud disk. |
| Rollbacking | Boolean | No | Whether the cloud disk is in the status of snapshot rollback. Value range:<li>false: No</li><li>true: Yes</li> |
| RollbackPercent | Integer | No | Progress of rolling back a snapshot to the cloud disk |
| Encrypt | Boolean | No | Whether the cloud disk is encrypted. Value range:<li>false: Not encrypted</li><li>true: Encrypted</li> |
| AutoRenewFlagError | Boolean | No | The cloud disk has been mounted to the server, and the server and cloud disk are both prepaid.<li>true: Auto renewal flag is set on the server but not on the cloud disk</li><li>false: Auto renewal flag is normal on the cloud disk</li> |
| RenewFlag | String | No | Renewal flag. Value range:<li>NOTIFY_AND_AUTO_RENEW: Notify expiry and renew automatically</li><li>NOTIFY_AND_MANUAL_RENEW: Notify expiry but not renew automatically</li><li>DISABLE_NOTIFY_AND_MANUAL_RENEW: Neither notify expiry nor renew automatically</li> |
| DeadlineError | Boolean | No | This field is used only when the cloud disk is mounted to an instance, and the instance and cloud disk are both prepaid.<li>true: Cloud disk expires earlier than instance.</li><li>false: Cloud disk expires later than instance. |
| IsReturnable | Boolean | No | Whether a prepaid cloud disk can be returned.<li>true: Yes</li><li>false: No</li> |
| ReturnFailCode | Integer | No | If a prepaid cloud disk cannot be returned, this parameter indicates the specific reason for it. Value range:<li>1: Cloud disk has been returned</li><li>2. Cloud disk has expired</li><li>3: Cloud disk cannot be returned</li><li>8: Number of returnable cloud disks exceeds the limit</li> |
| AutoSnapshotPolicyIds | Array of String | No | ID of the periodic snapshot associated to the cloud disk. This parameter is returned only if the value of parameter ReturnBindAutoSnapshotPolicy is TRUE when the API DescribeDisks is called. |

## DiskChargePrepaid

The billing method of an instance

| Name | Type | Required | Description |
|------|------|----------|------|
| Period | Integer | Yes | The purchased usage period of a cloud disk (in month). Value range: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36. |
| RenewFlag | String | No | Renewal flag. Value range:<li>NOTIFY_AND_AUTO_RENEW: Notify expiry and renew automatically</li><li>NOTIFY_AND_MANUAL_RENEW: Notify expiry but not renew automatically</li><li>DISABLE_NOTIFY_AND_MANUAL_RENEW: Neither notify expiry nor renew automatically</li><br>Default value range: NOTIFY_AND_MANUAL_RENEW: Notify expiry but not renew automatically. |
| CurInstanceDeadline | Timestamp | No | This parameter is used when you align the expiration time of the cloud disk with that of the mounted server. It is the current expiration time of the server. In this case, the Period passed represents the renewal period of the server, and the cloud disk will be automatically renewed in alignment with the expiration time of the renewed server. |

## DiskConfig

Cloud disk configuration.

| Name | Type | Required | Description |
|------|------|----------|------|
| Available | Boolean | No | Whether the configuration is available. |
| DiskType | String | No | Type of cloud disk medium. Value range:<li>CLOUD_BASIC: HDD cloud disk</li><li>CLOUD_PREMIUM: Premium cloud storage</li><li>CLOUD_SSD: SSD cloud disk</li> |
| DiskUsage | String | No | Cloud disk type. Value range:<li>SYSTEM_DISK: System disk</li><li>DATA_DISK: Data disk</li> |
| DiskChargeType | String | No | Billing method. Value range:<li>PREPAID: Prepaid</li><li>POSTPAID_BY_HOUR: Postpaid</li> |
| MaxDiskSize | Integer | No | The maximum configurable cloud disk size. |
| MinDiskSize | Integer | No | The minimum configurable cloud disk size. |
| Zone | String | No | [Availability Zone](/document/api/213/9452#zone). |
| DeviceClass | String | No | Instance model. |
| InstanceFamily | String | No | Instance model series. For more information, please see [Instance Models](https://cloud.tencent.com/document/product/213/11518) |

## Filter

Key-value pair filters for conditional filtering queries.

| Name | Type | Required | Description |
|------|------|----------|------|
| Name | String | Yes | The name of the filter key. |
| Values | Array of String | Yes | One or more filter values. |

## Placement

The abstract location of an instance, including its available zone, project, etc.

| Name | Type | Required | Description |
|------|------|----------|------|
| Zone | String | Yes | ID of the [Availability Zone](/document/api/213/9452#zone) to which the instance belongs. This parameter can be obtained from the Zone field in the returned values of [DescribeZones](/document/product/213/15707). |
| ProjectId | Integer | No | ID of the project to which the instance belongs. This parameter can be obtained from the projectId field in the returned values of [DescribeProject](/document/api/378/4400). If this is left empty, default project is used. |

## Price

The price of a cloud disk

| Name | Type | Required | Description |
|------|------|----------|------|
| OriginalPrice | Float | No | Original price of prepaid expenses (in CNY). |
| DiscountPrice | Float | No | Discount price of prepaid expenses (in CNY). |

## Snapshot

The details of a snapshot

| Name | Type | Required | Description |
|------|------|----------|------|
| SnapshotId | String | No | Snapshot ID. |
| Placement | Placement | No | Location of the snapshot. |
| DiskUsage | String | No | Type of the cloud disk used to create the snapshot. Value range:<li>SYSTEM_DISK: System disk</li><li>DATA_DISK: Data disk</li> |
| DiskId | String | No | ID of the cloud disk used to create the snapshot. |
| DiskSize | Integer | No | Size of the cloud disk used to create the snapshot. |
| SnapshotState | String | No | Status of the snapshot. Value range:<li>NORMAL: Normal</li><li>CREATING: Creating</li><li>ROLLBACKING: Rolling backing</li><li>COPYING_FROM_REMOTE: Copying snapshot across regions</li> |
| SnapshotName | String | No | Snapshot name, the user-defined snapshot alias. Call [ModifySnapshotAttribute](/document/product/362/15650) to modify this field. |
| Percent | Integer | No | The percentage of progress for snapshot creation. This field is always 100 after the snapshot is created successfully. |
| CreateTime | Timestamp | No | Creation time of the snapshot. |
| DeadlineTime | Timestamp | No | Expiration time of the snapshot. If the snapshot is permanently retained, this field is empty. |
| Encrypt | Boolean | No | Whether the snapshot is created from a encrypted disk. Value range:<li>true: Yes</li><li>false: No</li> |
| IsPermanent | Boolean | No | Whether it is a permanent snapshot. Value range:<li>true: Permanent snapshot</li><li>false: Non-permanent snapshot. |

