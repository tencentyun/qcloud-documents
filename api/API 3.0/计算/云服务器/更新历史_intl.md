## The 9th Release

Release time: 7/12/2018 6:44:10 PM

The following changes are contained in this release:

The existing documents were improved.

API modified:

* [InquiryPriceRenewInstances](/document/api/213/#)
	* New input parameter: RenewPortableDataDisk
* [RenewInstances](/document/api/213/#)
	* New input parameter: RenewPortableDataDisk

Data structure modified:

* [OsVersion](/document/api/213/##OsVersion)
	* New member: Architecture

## The 8th Release

Release time: 7/2/2018 8:46:22 PM

The following changes are contained in this release:

The existing documents were improved.

APIs added:

* [DescribeInstanceVncUrl](/document/api/213/#)

API modified:

* [RunInstances](/document/api/213/#)
	* New input parameter: DisasterRecoverGroupIds

## The 7th Release

Release time: 6/21/2018 2:51:58 PM

The following changes are contained in this release:

The existing documents were improved.

APIs added:

* [InquiryPriceModifyInstancesChargeType](/document/api/213/#)
* [ModifyInstancesChargeType](/document/api/213/#)

## The 6th Release

Release time: 6/14/2018 12:15:42 PM

The following changes are contained in this release:

The existing documents were improved.

APIs added:

* [CreateDisasterRecoverGroup](/document/api/213/#)
* [DeleteDisasterRecoverGroups](/document/api/213/#)
* [DescribeDisasterRecoverGroupQuota](/document/api/213/#)
* [DescribeDisasterRecoverGroups](/document/api/213/#)
* [ModifyDisasterRecoverGroupAttribute](/document/api/213/#)

API modified:

* [DescribeImportImageOs](/document/api/213/#)
	* New output parameter: ImportImageOsVersionSet
	* **Deleted output parameter: **ImportImageOsVersionSupported
	* **Modified output parameter: **ImportImageOsListSupported

Data structures added:

* [DisasterRecoverGroup](/document/api/213/##DisasterRecoverGroup)
* [ImageOsList](/document/api/213/##ImageOsList)
* [OsVersion](/document/api/213/##OsVersion)

Data structure modified:

* [HostItem](/document/api/213/##HostItem)
	* **Modified member: **InstanceIds

## The 5th Release

Release time: 6/7/2018 3:01:42 PM

The following changes are contained in this release:

The existing documents were improved.

**APIs deleted: **

* DescribeInstanceOperationLogs
* UpdateInstanceVpcConfig

APIs modified:

* [ModifyInstancesAttribute](/document/api/213/#)
	* New input parameter: SecurityGroups
* [RunInstances](/document/api/213/#)
	* New input parameters: InstanceMarketOptions, UserData

Data structure modified:

* [Instance](/document/api/213/##Instance)
	* New member: InstanceState

## The 4th Release

Release time: 5/31/2018 2:45:35 PM

The following changes are contained in this release:

The existing documents were improved.

API added:

* [DescribeZoneInstanceConfigInfos](/document/api/213/#)

Data structures added:

* [InstanceTypeQuotaItem](/document/api/213/##InstanceTypeQuotaItem)
* [LocalDiskType](/document/api/213/##LocalDiskType)
* [StorageBlock](/document/api/213/##StorageBlock)

Data structure modified:

* [Externals](/document/api/213/##Externals)
	* New members: UnsupportNetworks, StorageBlockAttr

## The 3rd Release

Release time: 5/24/2018 5:08:50 PM

The following changes are contained in this release:

The existing documents were improved.

**API deleted:**

* QueryMigrateTask

## The 2nd Release

Release time: 5/17/2018 4:17:11 PM

The following changes are contained in this release:

The existing documents were improved.

API modified:

* [InquiryPriceRunInstances](/document/api/213/#)
	* New input parameter: InstanceMarketOptions
* [TerminateInstances](/document/api/213/#)
	* **Deleted input parameter:**DiskType

Data structures added:

* [InstanceMarketOptionsRequest](/document/api/213/##InstanceMarketOptionsRequest)
* [SpotMarketOptions](/document/api/213/##SpotMarketOptions)

Data structures modified:

* [Image](/document/api/213/##Image)
	* **Modified members: **ImageSize, Platform, ImageCreator
* [Instance](/document/api/213/##Instance)
	* New members: OsName, SecurityGroupIds, LoginSettings

## The 1st Release

Release time: 2018-04-24

The following changes are contained in this release:

The existing documents were improved.

APIs added:

* [AllocateHosts](/document/api/213/#)
* [AssociateInstancesKeyPairs](/document/api/213/#)
* [CreateImage](/document/api/213/#)
* [CreateKeyPair](/document/api/213/#)
* [DeleteImages](/document/api/213/#)
* [DeleteKeyPairs](/document/api/213/#)
* [DescribeHosts](/document/api/213/#)
* [DescribeImageQuota](/document/api/213/#)
* [DescribeImageSharePermission](/document/api/213/#)
* [DescribeImages](/document/api/213/#)
* [DescribeImportImageOs](/document/api/213/#)
* [DescribeInstanceFamilyConfigs](/document/api/213/#)
* [DescribeInstanceInternetBandwidthConfigs](/document/api/213/#)
* [DescribeInstanceOperationLogs](/document/api/213/#)
* [DescribeInstanceTypeConfigs](/document/api/213/#)
* [DescribeInstances](/document/api/213/#)
* [DescribeInstancesStatus](/document/api/213/#)
* [DescribeInternetChargeTypeConfigs](/document/api/213/#)
* [DescribeKeyPairs](/document/api/213/#)
* [DescribeRegions](/document/api/213/#)
* [DescribeZones](/document/api/213/#)
* [DisassociateInstancesKeyPairs](/document/api/213/#)
* [ImportImage](/document/api/213/#)
* [ImportKeyPair](/document/api/213/#)
* [InquiryPriceRenewInstances](/document/api/213/#)
* [InquiryPriceResetInstance](/document/api/213/#)
* [InquiryPriceResetInstancesInternetMaxBandwidth](/document/api/213/#)
* [InquiryPriceResetInstancesType](/document/api/213/#)
* [InquiryPriceResizeInstanceDisks](/document/api/213/#)
* [InquiryPriceRunInstances](/document/api/213/#)
* [ModifyHostsAttribute](/document/api/213/#)
* [ModifyImageAttribute](/document/api/213/#)
* [ModifyImageSharePermission](/document/api/213/#)
* [ModifyInstancesAttribute](/document/api/213/#)
* [ModifyInstancesProject](/document/api/213/#)
* [ModifyInstancesRenewFlag](/document/api/213/#)
* [ModifyKeyPairAttribute](/document/api/213/#)
* [QueryMigrateTask](/document/api/213/#)
* [RebootInstances](/document/api/213/#)
* [RenewHosts](/document/api/213/#)
* [RenewInstances](/document/api/213/#)
* [ResetInstance](/document/api/213/#)
* [ResetInstancesInternetMaxBandwidth](/document/api/213/#)
* [ResetInstancesPassword](/document/api/213/#)
* [ResetInstancesType](/document/api/213/#)
* [ResizeInstanceDisks](/document/api/213/#)
* [RunInstances](/document/api/213/#)
* [StartInstances](/document/api/213/#)
* [StopInstances](/document/api/213/#)
* [SyncImages](/document/api/213/#)
* [TerminateInstances](/document/api/213/#)
* [UpdateInstanceVpcConfig](/document/api/213/#)

Data structures added:

* [ActionTimer](/document/api/213/##ActionTimer)
* [ChargePrepaid](/document/api/213/##ChargePrepaid)
* [DataDisk](/document/api/213/##DataDisk)
* [EnhancedService](/document/api/213/##EnhancedService)
* [Externals](/document/api/213/##Externals)
* [Filter](/document/api/213/##Filter)
* [HostItem](/document/api/213/##HostItem)
* [HostResource](/document/api/213/##HostResource)
* [Image](/document/api/213/##Image)
* [Instance](/document/api/213/##Instance)
* [InstanceChargePrepaid](/document/api/213/##InstanceChargePrepaid)
* [InstanceFamilyConfig](/document/api/213/##InstanceFamilyConfig)
* [InstanceStatus](/document/api/213/##InstanceStatus)
* [InstanceTypeConfig](/document/api/213/##InstanceTypeConfig)
* [InternetAccessible](/document/api/213/##InternetAccessible)
* [InternetBandwidthConfig](/document/api/213/##InternetBandwidthConfig)
* [InternetChargeTypeConfig](/document/api/213/##InternetChargeTypeConfig)
* [ItemPrice](/document/api/213/##ItemPrice)
* [KeyPair](/document/api/213/##KeyPair)
* [LoginSettings](/document/api/213/##LoginSettings)
* [Placement](/document/api/213/##Placement)
* [Price](/document/api/213/##Price)
* [RegionInfo](/document/api/213/##RegionInfo)
* [RunMonitorServiceEnabled](/document/api/213/##RunMonitorServiceEnabled)
* [RunSecurityServiceEnabled](/document/api/213/##RunSecurityServiceEnabled)
* [SharePermission](/document/api/213/##SharePermission)
* [SystemDisk](/document/api/213/##SystemDisk)
* [Tag](/document/api/213/##Tag)
* [TagSpecification](/document/api/213/##TagSpecification)
* [VirtualPrivateCloud](/document/api/213/##VirtualPrivateCloud)
* [ZoneInfo](/document/api/213/##ZoneInfo)


