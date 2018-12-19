## Disk

The details of a cloud disk

Used by actions: DescribeDisks.

| Name | Type | Description |
|------|------|-------|
| Tags | Array of [Tag](#Tag) | The tag bound to the cloud disk. The value Null is used when no tag is bound to the cloud disk. |
| DiskId | String | Cloud disk ID. |
| DiskUsage | String | Cloud disk type. Value range:<br><li>SYSTEM_DISK: System disk<br><li>DATA_DISK: Data disk. |
| DiskChargeType | String | Billing method. Value range:<br><li>PREPAID: Prepaid<br><li>POSTPAID_BY_HOUR: Postpaid. |
| Portable | Boolean | Whether it is an elastic cloud disk. false: Non-elastic cloud disk; true: Elastic cloud disk. |
| Placement | [Placement](#Placement) | Location of the cloud disk. |
| SnapshotAbility | Boolean | Whether the cloud disk has the capability to create snapshots. Value range:<br><li>false: No.<br><li>true: Yes. |
| DiskName | String | Cloud disk name. |
| DiskSize | Integer | Cloud disk size (in GB). |
| DiskState | String | Cloud disk status. Value range:<br><li>UNATTACHED: Unmounted<br><li>ATTACHING: Mounting<br><li>ATTACHED: Mounted<br><li>DETACHING: Unmounting<br><li>EXPANDING: Expanding capacity<br><li>ROLLBACKING: Rolling back. |
| DiskType | String | Type of cloud disk medium. Value range:<br><li>CLOUD_BASIC: HDD cloud disk<br><li>CLOUD_PREMIUM: Premium cloud storage<br><li>CLOUD_SSD: SSD cloud disk. |
| Attached | Boolean | Whether the cloud disk is mounted to the CVM. Value range:<br><li>false: Unmounted<br><li>true: Mounted. |
| InstanceId | String | ID of the CVM to which the cloud disk is mounted. |
| CreateTime | Timestamp | Creation time of the cloud disk. |
| DeadlineTime | Timestamp | Expiration time of the cloud disk. |
| Rollbacking | Boolean | Whether the cloud disk is in the status of snapshot rollback. Value range:<br><li>false: No<br><li>true: Yes. |
| RollbackPercent | Integer | Rollback progress of a cloud disk snapshot. |
| Encrypt | Boolean | Whether the cloud disk is encrypted. Value range:<br><li>false: Not encrypted<br><li>true: Encrypted. |
| AutoRenewFlagError | Boolean | The cloud disk has been mounted to the server, and both the server and the cloud disk are billed on a prepaid basis. <br><li> true: Auto renewal flag is set on the server but not on the cloud disk<br><li>false: Auto renewal flag is normal on the cloud disk. |
| RenewFlag | String | Auto renewal flag. Value range: <br><li>NOTIFY_AND_AUTO_RENEW: notify expiry and renew automatically<br><li>NOTIFY_AND_MANUAL_RENEW: notify expiry but not renew automatically<br><li>DISABLE_NOTIFY_AND_MANUAL_RENEW: neither notify expiry nor renew automatically. |
| DeadlineError | Boolean | This field is only meaningful when the cloud disk is mounted to an instance, and both the instance and the cloud disk are billed on a prepaid basis.<br><li> true: Cloud disk expires earlier than the instance.<br><li> false: Cloud disk expires later than the instance. |
| IsReturnable | Boolean | Whether a prepaid cloud disk can be returned. <br><li> true: Yes<br><li>false: No. |
| ReturnFailCode | Integer | If a prepaid cloud disk cannot be returned, this parameter indicates the specific reason for this case. Value range:<br><li>1: Cloud disk has been returned<br><li>2. Cloud disk has expired<br><li>3: Cloud disk cannot be returned<br><li>8: Number of returnable cloud disks exceeds the limit. |
| AutoSnapshotPolicyIds | Array of String | ID of the periodic snapshot associated to the cloud disk. This parameter is returned only if the value of parameter ReturnBindAutoSnapshotPolicy is TRUE when the API DescribeDisks is called. |

## DiskChargePrepaid

The billing method of an instance

Used by actions: CreateDisks, InquiryPriceCreateDisks, InquiryPriceRenewDisks, RenewDisk.

| Name | Type | Required | Description |
|------|------|----------|------|
| Period | Integer | Yes | The purchased usage period of a cloud disk (in month). Value range: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36. |
| RenewFlag | String | No | Auto renewal flag. Value range:<br><li>NOTIFY_AND_AUTO_RENEW: Notify expiry and renew automatically<br><li>NOTIFY_AND_MANUAL_RENEW: Notify expiry but not renew automatically<br><li>DISABLE_NOTIFY_AND_MANUAL_RENEW: Neither notify expiry nor renew automatically<br><br>Default value range: NOTIFY_AND_MANUAL_RENEW: Notify expiry but not renew automatically. |
| CurInstanceDeadline | Timestamp | No | This parameter is used when you align the expiration time of the cloud disk with that of the mounted server. It is the current expiration time of the server. In this case, the Period passed represents the renewal period of the server, and the cloud disk will be automatically renewed in alignment with the expiration time of the renewed server. |

## DiskConfig

Cloud disk configuration.

Used by actions: DescribeDiskConfigQuota.

| Name | Type | Description |
|------|------|-------|
| Available | Boolean | Whether the configuration is available. |
| DiskType | String | Type of cloud disk medium. Value range:<br><li>CLOUD_BASIC: HDD cloud disk<br><li>CLOUD_PREMIUM: Premium cloud storage<br><li>CLOUD_SSD: SSD cloud disk. |
| DiskUsage | String | Cloud disk type. Value range:<br><li>SYSTEM_DISK: System disk<br><li>DATA_DISK: Data disk. |
| DiskChargeType | String | Billing method. Value range:<br><li>PREPAID: Prepaid<br><li>POSTPAID_BY_HOUR: Postpaid. |
| MaxDiskSize | Integer | The maximum configurable cloud disk size (in GB). |
| MinDiskSize | Integer | The minimum configurable cloud disk size (in GB). |
| Zone | String | The [availability zone](/document/api/213/9452#zone) where the cloud disk resides. |
| DeviceClass | String | Instance model. |
| InstanceFamily | String | Instance model series. For more information, please see [Instance Type](https://cloud.tencent.com/document/product/213/11518) |.

## Filter

Key-value pair filters for conditional filtering queries.

Used by actions: DescribeDisks, DescribeSnapshots.

| Name | Type | Required | Description |
|------|------|----------|------|
| Name | String | Yes | Name of the filter key. |
| Values | Array of String | Yes | One or more filter values. |

## Placement

The abstract location of an instance, including its availability zone and project.

Used by actions: CreateDisks, DescribeDisks, DescribeSnapshots.

| Name | Type | Required | Description |
|------|------|----------|------|
| Zone | String | Yes | ID of the [availability zone](/document/api/213/9452#zone) to which the instance belongs. This parameter can also be obtained from the Zone field in the returned values of [DescribeZones](/document/product/213/15707). |
| ProjectId | Integer | No | ID of the project to which the instance belongs. This parameter can be obtained from the Zone field in the returned values of [DescribeProject](/document/api/378/4400). If this is left empty, default project is used. |

## Price

The price of a cloud disk

Used by actions: InquiryPriceCreateDisks, InquiryPriceRenewDisks, InquiryPriceResizeDisk.

| Name | Type | Description |
|------|------|-------|
| UnitPrice | Float | Unit price of a postpaid cloud disk (in CNY). |
| ChargeUnit | String | Billing unit of a postpaid cloud disk. Value range: <br><li>HOUR: Billed by hour. |
| OriginalPrice | Float | Original price of the advanced payment for a prepaid cloud disk (in CNY). |
| DiscountPrice | Float | Discount price of the advanced payment for a prepaid cloud disk (in CNY). |

## Snapshot

The details of a snapshot

Used by actions: DescribeSnapshots.

| Name | Type | Description |
|------|------|-------|
| CopyingToRegions | Array of String | The destination region to which the snapshot is being replicated. Default value is [ ]. |
| CopyFromRemote | Boolean | Whether it's a snapshot replicated across regions. Value range: <br><li>true: snapshot replicated across regions. <br><li> false: snapshot in local region. |
| SnapshotId | String | Snapshot ID. |
| Placement | [Placement](#Placement) | Location of the snapshot. |
| DiskUsage | String | Type of the cloud disk used to create this snapshot. Value range:<br><li>SYSTEM_DISK: System disk<br><li>DATA_DISK: Data disk. |
| DiskId | String | ID of the cloud disk used to create this snapshot. |
| DiskSize | Integer | Size of the cloud disk used to create this snapshot (in GB). |
| SnapshotState | String | Snapshot status. Value range:<br><li>NORMAL: Normal<br><li>CREATING: Creating<br><li>ROLLBACKING: Rolling back<br><li>COPYING_FROM_REMOTE: Copying snapshot across regions. |
| SnapshotName | String | Snapshot name, a user-defined snapshot alias. Call [ModifySnapshotAttribute](/document/product/362/15650) to modify this field. |
| Percent | Integer | The progress percentage for snapshot creation. This field is always 100 after the snapshot is created successfully. |
| CreateTime | Timestamp | Creation time of the snapshot. |
| DeadlineTime | Timestamp | Expiration time of the snapshot. This field is left empty for a permanent snapshot. |
| Encrypt | Boolean | Whether the snapshot is created from an encrypted disk. Value range:<br><li>true: Yes<br><li>false: No. |
| IsPermanent | Boolean | Whether it's a permanent snapshot. Value range:<br><li>true: Yes<br><li>false: No. |

## Tag

Tag.

Used by actions: CreateDisks, DescribeDisks.

| Name | Type | Required | Description |
|------|------|----------|------|
| Key | String | Yes | Tag key. |
| Value | String | Yes | Tag value. |


