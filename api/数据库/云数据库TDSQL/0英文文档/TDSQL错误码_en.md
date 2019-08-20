Error codes for TDSQL APIs fall into two types:
- Common error codes for the API platform (please see [Common Error Codes](/doc/api/309/7025)).
- Error codes specific to the service, as show in the table below:

| Error Code | Description |
|---------|---------|
| ServiceUnavailable | TDSQL service is unavailable in any region |
| NoServiceAvailableForThisRegionId | TDSQL service is unavailable in the requested regionId |
| NoServiceAvailableForThisZoneId | TDSQL service is unavailable in the requested zoneId |
| ReachThememSizeLimit | Capacity of requested TDSQL is beyond the maximum/minimum capacity |
| ReachTheAmountLimit | Quantity of requested TDSQLs is beyond the maximum/minimum purchase quantity |
| InstanceNameIllegal | The new instance name is invalid |
| EmptyPasswordForbidden | Empty password is not allowed |
| OldPasswordNotCorrect | Old password is incorrect for resetting password |
| InstanceExpired | TDSQL instance has expired. Please renew it |
| NoSpecFound | No title for the spec is found |
| NoInstanceFound | Instance does not exist |
| InstanceStatusAbnormal | Operation is impossible due to instance status exception (not deleted) |
| SameSpecId | The specid specified for the expansion is same as that of the instance |
| SpecIdIllegal | The specid specified for the expansion is invalid because it does not exist in the spec list |
| EmptyIP | Access machine IP is empty and cannot be changed |
| UserNotInTheWhiteList | User is not in the whitelist |
| SuperUserForbidden | Operation on TDSQL of super user is not allowed |
| DbNameIllegal | Database name is invalid |
| UserHostExistsAlready | User already exists |
| UserHostDoesNotExist | User does not exist |
| InstanceAlreadyDeleted | Instance has been deleted |
| IllegalLogSaveDays | The modified number of days the log is kept is beyond the minimum/maximum value |
| IllegalTime | Invalid time parameter |
| RepeatOrderNumber | The order number for applying instance has already been submitted |
| IllegalInstanceId | Invalid instance ID |
| LogNotExisted | Log is missing |
| ConnectKafkaFailed | KAFKA connection error |
| IllegalInitParam | Invalid parameter for instance initialization |
| SyncTaskDeleted | Synchronization task has been deleted |
| SyncTaskParamIllegal | Invalid parameter for synchronization task |
| IllegalDeadline | Invalid deadline |
| RuleAbnormal | Invalid rule status |
| AuditServiceAlreadyOn | Audit service is already enabled |
| RuleNameExisted | The rule name already exists |
| RuleStatusError | Rule status error |
| RuleParamsError | Rule parameter error |
| StrategyNameExists | Strategy name already exists |
| SessionIdExpired | Session ID has expired |
| PriorityIDError | PriorityID does not match |
| RulesNotExist | Rule does not exist |
| StrategyNotExist | Strategy name does not exist |
| ConnectMongodFailed | Failed to connect to mongod |
| RulesExisted | Associated rule already exists |
| CharacterError | Invalid character |
| SyncDbFailed | Failed to synchronize instance DB |
| TableInfoNotCorrect | Multi-source synchronization of database tables is impossible because information of destination database table does not match that of source database |
| SrcTableErrorOrNotExist | Source table is invalid or does not exist |
| DstTableErrorOrNotExist | Destination table is invalid or does not exist |
| ShardNotExist | Shard does not exist |
| AuditServiceAbnormal | Audit service status is invalid |
| FlowStatusError | Flow error |
| RedoFlowFailed | Failed to restart flow |
| InstanceHasBeenLocked | TDSQL is locked by another flow |
| ProxyNeedsUpgrade | Current PROXY version is too low and needs an upgrade |
| DbOperationFailed | DB internal failure |
| OssOpertaionFailed | OSS internal failure |
| CreateUserFailed | Failed to create user |
| GetUserListFailed | Failed to acquire user list |
| CopyRightError | Error occurred when copying permissions |
| DeleteUserFailed | Failed to delete user |
| GetRightFailed | Failed to acquire permissions |
| GetTableInfoFailed | Failed to acquire table structure |
| GetDbconfigFailed | Failed to acquire parameter |
| GetDbListFailed | Failed to acquire database list |
| GetDbObjectFailed | Failed to acquire database object |
| GetSpecInfoFailed | Failed to acquire specification information |
| ResetPasswordFailed | Failed to reset password |
| ModifyRightFailed | Failed to modify permission |
| GetInstanceInfoFailed | Failed to acquire instance information |
| StopMigrateTaskFailed | Failed to stop migration task |
| MigrateStartFailed | Failed to start database migration |
| CheckDbInfoFailed | Failed to check database information |
| CheckMigrateInfoFailed | Failed to check migration information |
| GetMigrateDbListFailed | Failed to acquire list of the databases to be migrated |
| GetMigrateObjectListFailed | Failed to acquire list of the objects to be migrated |
| FinishMigrateTaskFailed | Failed to finish migration task |
| QueryMigrateResultFailed | Failed to query and validate migration task result |
| BadUserType | Invalid user type |
| BadUserRight | Invalid user permission |
| OSSGetInstanceError | Error occurs while OSS is obtaining instance information |
| CDBError | CDB API error |
| CDBMasterError | CDB MASTER error |
| CNSAuthFailed | CNS authentication failed |
| CNSNSFailed | CNS NS failed |
| VPCError | VPC error |
| BaradError | Barad error |
| JsonUnmarshaFailed | Json resolution failed |
| NoDataFetched | No data is fetched |
| ReadDataFailed | Failed to read returned data |
| BadRequest | Failed to initiate request |
| MakeRequestFailed | Failed to join parameters into request |
| InstanceStatusError | Instance status error |
| MetricNotExist | Specified metric does not exist |
| HDFSError | HDFS error |
| MigrateTaskLocked | The migration task is already in another operation |
| NoMigrateTask | No migration task is specified |
| MigrateTaskDeleted | Migration task has been deleted |
| MigrateTaskAlreadyRunning | Migration task is already running |
| MigrateTaskAlreadySuccess | Migration task is already successful |
| MigrateTaskNotTunning | Migration task is not running |
| MigrateTaskParamError | Invalid parameter for migration task |
| MigrateTaskNoCdbInstance | No CDB instance exists |
| OssTaskStatusNotOk | OSS task status is not OK for the migration task |
| MigrateTaskNoCvmInstance | No CVM instance exists |
| VpcMigrateNotSupport | VPC migration is not supported |
| CvmIpNotCorrect | Incorrect CVM IP |
| MigrateTaskCheckFailed | Migration task failed to be validated and cannot start |
| MigratTaskUnchecked | Migration task is not validated and cannot start |
| MigrateCheckIdInvalid | Migration task ID is invalid |
| DfwError | DFW API error |
| CDBOSSFailed | CDB OSS error |
| LogDBFailed | logDB API error |
| TgwApplyRuleFailed | Failed to apply TGW rule |
| TGWOpRsFailed | TGW operation on physical machine failed |
| TGWAddGslbFailed | TGW failed to add GSLB |
| TGWDeleteGslbFailed | TGW failed to delete GSLB |
| InnerSystemError | Internal system error (unrelated to service) |
| ConfigFileFormatErrorEgIntStringBooLTypeError | Configuration file format is incorrect |
| ParamError | Logic parameter error |
| FenceError | Cage API error |
| IllegalExclusterID | Invalid exclusive cluster ID |
| RegionUnavailable | Service is not available in this region |
| NotSupportNow | Pay per Use is not supported currently |
| BalanceIsNotEnough | Insufficient balance |
| ReachTheAmounLimit | Purchase quantity exceeds the limit |
| PriceParamError | Billing API parameter error |
| GetPriceError | Failed to acquire price |
| PriceDBError | Billing DB operation failed |
| InvalidCoupon | Invalid coupon |
| GetGoodsConfigFailed | Failed to obtain goods configuration |
| IllegalGoodsID | Invalid goods ID |
| IllegalGoodsOperation | The operation is not allowed for the goods |
| FailedToPay | Payment failed |
| SomeBillsFailed | Payment is successful, but delivery for some orders failed |
| PayError | Error occurred during payment |


