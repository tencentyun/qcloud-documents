## The 7th Release

Release time: 2018-07-26 17:08:14

The following changes are contained in this release:

The existing documents were improved.

API modified:

* [CreateRoutes](/document/api/215/#)
	* **Modified input parameter:** Routes
* [DeleteRoutes](/document/api/215/#)
	* **Modified input parameter:** Routes

Data structure modified:

* [Route](/document/api/215/##Route)
	* New member: Enabled
* [Vpc](/document/api/215/##Vpc)
	* New members: DnsServerSet, DomainName, DhcpOptionsId

## The 6th Release

Release time: 2018-06-14 12:15:42

The following changes are contained in this release:

The existing documents were improved.

APIs added:

* [CreateDefaultVpc](/document/api/215/#)
* [DescribeAccountAttributes](/document/api/215/#)

Data structures added:

* [AccountAttribute](/document/api/215/##AccountAttribute)
* [DefaultVpcSubnet](/document/api/215/##DefaultVpcSubnet)
* [NetworkInterfaceAttachment](/document/api/215/##NetworkInterfaceAttachment)

Data structure modified:

* [NetworkInterface](/document/api/215/##NetworkInterface)
	* **Modified member:** Attachment
* [SecurityGroupAssociationStatistics](/document/api/215/##SecurityGroupAssociationStatistics)
	* New member: CLB

## The 5th Release

Release time: 2018-06-07 15:01:42

The following changes are contained in this release:

The existing documents were improved.

APIs added:

* [DescribeSecurityGroupAssociationStatistics](/document/api/215/#)

Data structures added:

* [SecurityGroupAssociationStatistics](/document/api/215/##SecurityGroupAssociationStatistics)

## The 4th Release

Release time: 2018-05-31 14:45:36

The following changes are contained in this release:

The existing documents were improved.

APIs added:

* [CreateCustomerGateway](/document/api/215/#)
* [CreateVpnConnection](/document/api/215/#)
* [CreateVpnGateway](/document/api/215/#)
* [DeleteCustomerGateway](/document/api/215/#)
* [DeleteVpnConnection](/document/api/215/#)
* [DeleteVpnGateway](/document/api/215/#)
* [DescribeCustomerGatewayVendors](/document/api/215/#)
* [DescribeCustomerGateways](/document/api/215/#)
* [DescribeVpnConnections](/document/api/215/#)
* [DescribeVpnGateways](/document/api/215/#)
* [DownloadCustomerGatewayConfiguration](/document/api/215/#)
* [InquiryPriceCreateVpnGateway](/document/api/215/#)
* [InquiryPriceRenewVpnGateway](/document/api/215/#)
* [InquiryPriceResetVpnGatewayInternetMaxBandwidth](/document/api/215/#)
* [ModifyCustomerGatewayAttribute](/document/api/215/#)
* [ModifyVpnConnectionAttribute](/document/api/215/#)
* [ModifyVpnGatewayAttribute](/document/api/215/#)
* [RenewVpnGateway](/document/api/215/#)
* [ResetVpnConnection](/document/api/215/#)
* [ResetVpnGatewayInternetMaxBandwidth](/document/api/215/#)

API modified:

* [DescribeAddressTemplateGroups](/document/api/215/#)
	* New output parameters: TotalCount, AddressTemplateGroupSet
* [ReplaceRoutes](/document/api/215/#)
	* **Modified input parameter:** Routes
* [ResetRoutes](/document/api/215/#)
	* **Modified input parameter:** Routes

Data structures added:

* [CustomerGateway](/document/api/215/##CustomerGateway)
* [CustomerGatewayVendor](/document/api/215/##CustomerGatewayVendor)
* [IKEOptionsSpecification](/document/api/215/##IKEOptionsSpecification)
* [IPSECOptionsSpecification](/document/api/215/##IPSECOptionsSpecification)
* [ItemPrice](/document/api/215/##ItemPrice)
* [Price](/document/api/215/##Price)
* [SecurityPolicyDatabase](/document/api/215/##SecurityPolicyDatabase)
* [VpnConnection](/document/api/215/##VpnConnection)
* [VpnGateway](/document/api/215/##VpnGateway)

Data structure modified:

* [Route](/document/api/215/##Route)
	* **Modified member:** RouteId
* [Subnet](/document/api/215/##Subnet)
	* New member: AvailableIpAddressCount

## The 3rd Release

Release time: 2018-05-24 17:08:50

The following changes are contained in this release:

The existing documents were improved.

Data structure modified:

* [Address](/document/api/215/##Address)
	* New member: AddressStatus
	* **Deleted member:** AddressState

## The 2nd Release

Release time: 2018-05-11 10:47:37

The following changes are contained in this release:

The existing documents were improved.

API modified:

* [CreateSecurityGroup](/document/api/215/#)
	* New output parameter: SecurityGroup
* [CreateVpc](/document/api/215/#)
	* New input parameter: DnsServers, DomainName
* [DescribeSecurityGroupPolicies](/document/api/215/#)
	* New output parameter: SecurityGroupPolicySet
* [DescribeSecurityGroups](/document/api/215/#)
	* New input parameter: SecurityGroupSet, TotalCount
* [DescribeSubnets](/document/api/215/#)
	* New output parameter: SubnetSet
	* **Deleted output parameter:** DescribeSubnets
* [ModifyVpcAttribute](/document/api/215/#)
	* New input parameter: DnsServers, DomainName

Data structures added:

* [SecurityGroup](/document/api/215/##SecurityGroup)

## The 1st Release

Release time: 2018-04-24

The following changes are contained in this release:

The existing documents were improved.

APIs added:

* [AllocateAddresses](/document/api/215/#)
* [AssignPrivateIpAddresses](/document/api/215/#)
* [AssociateAddress](/document/api/215/#)
* [AttachClassicLinkVpc](/document/api/215/#)
* [AttachNetworkInterface](/document/api/215/#)
* [CreateAddressTemplate](/document/api/215/#)
* [CreateAddressTemplateGroup](/document/api/215/#)
* [CreateNetworkInterface](/document/api/215/#)
* [CreateRouteTable](/document/api/215/#)
* [CreateRoutes](/document/api/215/#)
* [CreateSecurityGroup](/document/api/215/#)
* [CreateSecurityGroupPolicies](/document/api/215/#)
* [CreateServiceTemplate](/document/api/215/#)
* [CreateServiceTemplateGroup](/document/api/215/#)
* [CreateSubnet](/document/api/215/#)
* [CreateVpc](/document/api/215/#)
* [DeleteAddressTemplate](/document/api/215/#)
* [DeleteAddressTemplateGroup](/document/api/215/#)
* [DeleteNetworkInterface](/document/api/215/#)
* [DeleteRouteTable](/document/api/215/#)
* [DeleteRoutes](/document/api/215/#)
* [DeleteSecurityGroup](/document/api/215/#)
* [DeleteSecurityGroupPolicies](/document/api/215/#)
* [DeleteServiceTemplate](/document/api/215/#)
* [DeleteServiceTemplateGroup](/document/api/215/#)
* [DeleteSubnet](/document/api/215/#)
* [DeleteVpc](/document/api/215/#)
* [DescribeAddressQuota](/document/api/215/#)
* [DescribeAddressTemplateGroups](/document/api/215/#)
* [DescribeAddressTemplates](/document/api/215/#)
* [DescribeAddresses](/document/api/215/#)
* [DescribeClassicLinkInstances](/document/api/215/#)
* [DescribeNetworkInterfaces](/document/api/215/#)
* [DescribeRouteTables](/document/api/215/#)
* [DescribeSecurityGroupPolicies](/document/api/215/#)
* [DescribeSecurityGroups](/document/api/215/#)
* [DescribeServiceTemplateGroups](/document/api/215/#)
* [DescribeServiceTemplates](/document/api/215/#)
* [DescribeSubnets](/document/api/215/#)
* [DescribeVpcs](/document/api/215/#)
* [DetachClassicLinkVpc](/document/api/215/#)
* [DetachNetworkInterface](/document/api/215/#)
* [DisassociateAddress](/document/api/215/#)
* [MigrateNetworkInterface](/document/api/215/#)
* [MigratePrivateIpAddress](/document/api/215/#)
* [ModifyAddressAttribute](/document/api/215/#)
* [ModifyAddressTemplateAttribute](/document/api/215/#)
* [ModifyAddressTemplateGroupAttribute](/document/api/215/#)
* [ModifyNetworkInterfaceAttribute](/document/api/215/#)
* [ModifyPrivateIpAddressesAttribute](/document/api/215/#)
* [ModifyRouteTableAttribute](/document/api/215/#)
* [ModifySecurityGroupAttribute](/document/api/215/#)
* [ModifySecurityGroupPolicies](/document/api/215/#)
* [ModifyServiceTemplateAttribute](/document/api/215/#)
* [ModifyServiceTemplateGroupAttribute](/document/api/215/#)
* [ModifySubnetAttribute](/document/api/215/#)
* [ModifyVpcAttribute](/document/api/215/#)
* [ReleaseAddresses](/document/api/215/#)
* [ReplaceRouteTableAssociation](/document/api/215/#)
* [ReplaceRoutes](/document/api/215/#)
* [ReplaceSecurityGroupPolicy](/document/api/215/#)
* [ResetRoutes](/document/api/215/#)
* [TransformAddress](/document/api/215/#)
* [UnassignPrivateIpAddresses](/document/api/215/#)

Data structures added:

* [Address](/document/api/215/##Address)
* [AddressTemplate](/document/api/215/##AddressTemplate)
* [AddressTemplateGroup](/document/api/215/##AddressTemplateGroup)
* [ClassicLinkInstance](/document/api/215/##ClassicLinkInstance)
* [Filter](/document/api/215/##Filter)
* [FilterObject](/document/api/215/##FilterObject)
* [InstanceChargePrepaid](/document/api/215/##InstanceChargePrepaid)
* [NetworkInterface](/document/api/215/##NetworkInterface)
* [PrivateIpAddressSpecification](/document/api/215/##PrivateIpAddressSpecification)
* [Quota](/document/api/215/##Quota)
* [Route](/document/api/215/##Route)
* [RouteTable](/document/api/215/##RouteTable)
* [RouteTableAssociation](/document/api/215/##RouteTableAssociation)
* [SecurityGroupPolicy](/document/api/215/##SecurityGroupPolicy)
* [SecurityGroupPolicySet](/document/api/215/##SecurityGroupPolicySet)
* [ServiceTemplate](/document/api/215/##ServiceTemplate)
* [ServiceTemplateGroup](/document/api/215/##ServiceTemplateGroup)
* [Subnet](/document/api/215/##Subnet)
* [Vpc](/document/api/215/##Vpc)


