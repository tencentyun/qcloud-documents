本文提供以下批量处理功能的公共元素。

## Manifest

| 节点名   | 父节点   | 描述                                                         | 类型            | 是否必选 |
| -------- | -------- | ------------------------------------------------------------ | --------------- | -------- |
| Location | Manifest | 对象清单的位置信息。                                         | Location Object | 是       |
| Spec     | Manifest | 描述对象清单的格式信息。如果为 CSV 文件，此元素将描述清单中包含的字段。 | Spec Object     | 是       |

### Location

| 节点名          | 父节点   | 描述                                             | 类型   | 是否必选 |
| --------------- | -------- | ------------------------------------------------ | ------ | -------- |
| ETag            | Location | 指定对象清单的 etag。长度1 - 1024字节。            | String | 是       |
| ObjectArn       | Location | 指定对象清单的唯一资源标识符，长度为1 - 1024字节。 | String | 是       |
| ObjectVersionId | Location | 指定对象清单的版本 ID，长度为1 - 1024字节。        | String | 否       |

### Spec

| 节点名 | 父节点 | 描述                                                         | 类型             | 是否必选 |
| ------ | ------ | ------------------------------------------------------------ | ---------------- | -------- |
| Fields | Spec   | 描述清单中包含的字段，当 Format 为 COSBatchOperations_CSV_V1 时，需要使用此元素指定 CSV 文件字段。合法字段为：Ignore、Bucket、Key、VersionId | Array of Strings | 否       |
| Format | Spec   | 指定对象清单的格式信息。合法字段为： COSBatchOperations_CSV_V1、 COSInventoryReport_CSV_V1 | String           | 是       |

## Operation 

>!单个任务中 Operation 只能包含下列多种操作中的一个。

| 节点名                   | 父节点    | 描述                                               | 类型                     | 是否必选 |
| ------------------------ | --------- | -------------------------------------------------- | ------------------------ | -------- |
| COSPutObjectCopy         | Operation | 指定对清单内的对象批量复制操作的具体参数。         | COSPutObjectCopy Object  | 否       |
| COSInitiateRestoreObject | Operation | 指定对清单内的归档存储类型对象批量恢复操作的具体参数。 | COSInitiateRestoreObject | 否       |

### COSPutObjectCopy

| 节点名                    | 父节点           | 描述                                                         | 类型                       | 是否必选 |
| ------------------------- | ---------------- | ------------------------------------------------------------ | -------------------------- | -------- |
| AccessControlGrants       | COSPutObjectCopy | 控制对象的具体访问权限。                                 | AccessControlGrants Object | 否       |
| CannedAccessControlList   | COSPutObjectCopy | 定义对象的 ACL 属性。有效值：private，public-read        | String                     | 否       |
| MetadataDirective         | COSPutObjectCopy | 是否拷贝源文件的元数据，枚举值：Copy，Replaced。默认值 Copy。<br><li>假如标记为 Copy，则拷贝源文件的元数据。<br><li>假如标记为 Replaced，则按本次请求的 Header 信息修改元数据。 | String                     | 否       |
| ModifiedSinceConstraint   | COSPutObjectCopy | 当对象在指定时间后被修改，则执行操作，否则返回412。      | Timestamp                  | 否       |
| UnModifiedSinceConstraint | COSPutObjectCopy | 当对象在指定时间后未被修改，则执行操作，否则返回412。    | Timestamp                  | 否       |
| NewObjectMetadata         | COSPutObjectCopy | 配置对象的元数据。                                         | NewObjectMetadata Object   | 否       |
| StorageClass              | COSPutObjectCopy | 设置对象的存储级别，枚举值：STANDARD，STANDARD_IA。默认值：STANDARD | String                     | 否       |
| TargetResource            | COSPutObjectCopy | 设置 Copy 的目标存储桶。请使用 qcs 指定，例如`qcs::cos:ap-chengdu:uid/1250000000:examplebucket-1250000000` | String                     | 是       |

### COSInitiateRestoreObject

| 节点名           | 父节点                   | 描述                                                    | 类型                       | 是否必选 |
| ---------------- | ------------------------ | ------------------------------------------------------- | -------------------------- | -------- |
| ExpirationInDays | COSInitiateRestoreObject | 设置副本在多少天后自动过期删除，设置范围为1 - 365的整数。 | Integer | 是       |
| JobTier          | COSInitiateRestoreObject | 归档恢复模式选择，可选值：Bulk、Standard。                  | String                     | 是       |

## AccessControlGrants

| 节点名   | 父节点              | 描述               | 类型            | 是否必选 |
| -------- | ------------------- | ------------------ | --------------- | -------- |
| COSGrant | AccessControlGrants | 配置一项权限控制。 | COSGrant Object | 否       |

### COSGrant

| 节点名     | 父节点   | 描述                                                       | 类型           | 是否必选 |
| ---------- | -------- | ---------------------------------------------------------- | -------------- | -------- |
| Grantee    | COSGrant | 指定将权限授予给哪个用户。                                 | Grantee Object | 是       |
| Permission | COSGrant | 指定要授予的某项权限。枚举值：READ，WRITE，FULL_CONTROL 。 | String         | 是       |

#### Grantee

| 节点名         | 父节点  | 描述                                                         | 类型   | 是否必选 |
| -------------- | ------- | ------------------------------------------------------------ | ------ | -------- |
| DisplayName    | Grantee | 用户名称。                                                   | String | 否       |
| Identifier     | Grantee | qcs 格式的用户 ID（UIN）。例如：`qcs::cam::uin/100000000001:uin/100000000001` | String | 是       |
| TypeIdentifier | Grantee | 指定 Identifier 的类型，目前仅支持用户 ID。枚举值：ID 。     | String | 是       |

## NewObjectMetadata

| 节点名             | 父节点            | 描述                                                | 类型                   | 是否必选 |
| ------------------ | ----------------- | --------------------------------------------------- | ---------------------- | -------- |
| CacheControl       | NewObjectMetadata | RFC 2616 中定义的缓存指令，将作为对象元数据保存。     | String                 | 否       |
| ContentDisposition | NewObjectMetadata | RFC 2616 中定义的文件名称，将作为对象元数据保存。     | String                 | 否       |
| ContentEncoding    | NewObjectMetadata | RFC 2616 中定义的编码格式，将作为对象元数据保存。     | String                 | 否       |
| ContentType        | NewObjectMetadata | RFC 2616 中定义的内容类型，将作为对象元数据保存。     | String                 | 否       |
| HttpExpiresDate    | NewObjectMetadata | RFC 2616 中定义的缓存失效时间，将作为对象元数据保存。 | String                 | 否       |
| SSEAlgorithm       | NewObjectMetadata | 服务端加密算法，目前仅支持 AES256。                   | String                 | 否       |
| UserMetadata       | NewObjectMetadata | 包括用户自定义元数据。                                | Array of Key and Value | 否       |

## Report

| 节点名      | 父节点 | 描述                                                         | 类型    | 是否必选 |
| ----------- | ------ | ------------------------------------------------------------ | ------- | -------- |
| Bucket      | Report | 任务完成报告的投递存储桶。                                   | String  | 是       |
| Enabled     | Report | 是否输出任务完成报告。                                       | Boolean | 是       |
| Format      | Report | 任务完成报告格式信息。合法值： Report_CSV_V1                 | String  | 是       |
| Prefix      | Report | 任务完成报告的前缀信息。长度0 - 256字节                        | String  | 否       |
| ReportScope | Report | 任务完成报告所需记录的任务信息，以确定记录所有操作执行信息还是失败操作的信息。合法值：AllTasks、FailedTasksOnly | String  | 是       |

## ProgressSummary

| 节点名                 | 父节点          | 描述               | 类型    |
| ---------------------- | --------------- | ------------------ | ------- |
| NumberOfTasksFailed    | ProgressSummary | 当前失败的操作数。 | Integer |
| NumberOfTasksSucceeded | ProgressSummary | 当前成功的操作数。 | Integer |
| TotalNumberOfTasks     | ProgressSummary | 总操作数。         | Integer |


