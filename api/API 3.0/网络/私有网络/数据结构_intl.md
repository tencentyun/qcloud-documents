## AccountAttribute

Account attribute object

Referenced by the following API: DescribeAccountAttributes.

| Name | Type | Description |
|------|------|-------|
| AttributeName | String | Attribute name |
| AttributeValues | Array of String | Attribute value |

## Address

Information of EIP

Referenced by the following API: DescribeAddresses.

| Name | Type | Description |
|------|------|-------|
| AddressId | String | `EIP` `ID`, the unique ID of `EIP`. |
| AddressName | String | `EIP` name. |
| AddressStatus | String | `EIP` status. |
| AddressIp | String | Elastic public IP |
| BindedResourceId | String | `ID` of the bound resource instance, such as a `CVM`, `NAT`, or ENI. |
| CreatedTime | Timestamp | Creation time. It is in the format of `YYYY-MM-DDThh: mm: ssZ` according to the `ISO8601` standard. `UTC` time is used. |

## AddressTemplate

IP address template

Referenced by the following API: CreateAddressTemplate, and DescribeAddressTemplates.

| Name | Type | Description |
|------|------|-------|
| AddressTemplateName | String | IP address template name. |
| AddressTemplateId | String | Unique ID of the IP address template instance. |
| AddressSet | Array of String | IP address information. |
| CreatedTime | String | Creation time. |

## AddressTemplateGroup

IP address template group

Referenced by the following API: CreateAddressTemplateGroup, and DescribeAddressTemplateGroups.

| Name | Type | Description |
|------|------|-------|
| AddressTemplateGroupName | String | IP address template group name. |
| AddressTemplateGroupId | String | IP address template group instance ID, such as ipmg-dih8xdbq. |
| AddressTemplateIdSet | Array of String | IP address template ID. |
| CreatedTime | String | Creation time. |

## ClassicLinkInstance

Classiclink instance

Referenced by the following API: DescribeClassicLinkInstances.

| Name | Type | Description |
|------|------|-------|
| VpcId | String | VPC instance ID |
| InstanceId | String | Unique ID of the CVM instance |

## CustomerGateway

Customer gateway

Referenced by the following API: CreateCustomerGateway, and DescribeCustomerGateways.

| Name | Type | Description |
|------|------|-------|
| CustomerGatewayId | String | Unique ID of customer gateway |
| CustomerGatewayName | String | Gateway name |
| IpAddress | String | Public network address |
| CreatedTime | String | Creation time |

## CustomerGatewayVendor

Customer gateway vendor information object.

Referenced by the following API: DescribeCustomerGatewayVendors, and DownloadCustomerGatewayConfiguration.

| Name | Type | Required | Description |
|------|------|----------|------|
| Platform | String | Yes | Platform. |
| SoftwareVersion | String | Yes | Software version. |
| VendorName | String | Yes | Vendor name. |

## DefaultVpcSubnet

Default VPC and subnet

Referenced by the following API: CreateDefaultVpc.

| Name | Type | Description |
|------|------|-------|
| VpcId | String | Default VpcId |
| SubnetId | String | Default SubnetId |

## Filter

Filter

Referenced by the following API: DescribeAddressTemplateGroups, DescribeAddressTemplates, DescribeAddresses, DescribeCustomerGateways, DescribeNetworkInterfaces, DescribeRouteTables, DescribeSecurityGroups, DescribeServiceTemplateGroups, DescribeServiceTemplates, DescribeSubnets, DescribeVpcs, and DescribeVpnConnections.

| Name | Type | Required | Description |
|------|------|----------|------|
| Name | String | Yes | Attribute name. If more than one Filter exists, the logical relation between these Filters is "AND". |
| Values | Array of String | Yes | Attribute value. If there are multiple Values for one Filter, the logical relation between these Values under the same Filter is "OR". |

## FilterObject

Filter key-value pair

Referenced by the following API: DescribeClassicLinkInstances, and DescribeVpnGateways.

| Name | Type | Required | Description |
|------|------|----------|------|
| Name | String | Yes | Attribute name. If more than one Filter exists, the logical relation between these Filters is "AND". |
| Values | Array of String | Yes | Attribute value. If there are multiple Values for one Filter, the logical relation between these Values under the same Filter is "OR". |

## IKEOptionsSpecification

IKE (Internet Key Exchange) configuration. IKE comes with a self-protection mechanism. The network security protocol is configured by the user.

Referenced by the following API: CreateVpnConnection, DescribeVpnConnections, and ModifyVpnConnectionAttribute.

| Name | Type | Required | Description |
|------|------|----------|------|
| PropoEncryAlgorithm | String | No | Encryption algorithm. Available values: '3DES-CBC', 'AES-CBC-128', 'AES-CBS-192', 'AES-CBC-256', and 'DES-CBC'. Default is 3DES-CBC. |
| PropoAuthenAlgorithm | String | No | Verification algorithm. Available value: 'MD5' and 'SHA1'. Default is MD5. |
| ExchangeMode | String | No | Negotiation mode. Available values: 'AGGRESSIVE' and 'MAIN'. Default is MAIN. |
| LocalIdentity | String | No | Type of local identity. Available values: 'ADDRESS' and 'FQDN'. Default is ADDRESS. |
| RemoteIdentity | String | No | Type of remote identity. Available values: 'ADDRESS' and 'FQDN'. Default is ADDRESS. |
| LocalAddress | String | No | Local identity. When ADDRESS is selected for LocalIdentity, LocalAddress is required. By default, localAddress is the public IP of the VPN gateway. |
| RemoteAddress | String | No | Remote identity. When ADDRESS is selected for RemoteIdentity, RemoteAddress is required. |
| LocalFqdnName | String | No | Local identity. When FQDN is selected for LocalIdentity, LocalFqdnName is required. |
| RemoteFqdnName | String | No | Remote identity. When FQDN is selected for RemoteIdentity, RemoteFqdnName is required. |
| DhGroupName | String | No | DH group. Specifies the DH group used for exchanging the key via IKE. Available values: 'GROUP1', 'GROUP2', 'GROUP5', 'GROUP14', and 'GROUP24'. |
| IKESaLifetimeSeconds | Integer | No | IKE SA lifetime (in sec). Value range: 60-604800 |
| IKEVersion | String | No | IKE version |

## IPSECOptionsSpecification

IPSec configuration. The IPSec secure session configuration is provided by Tencent Cloud.

Referenced by the following API: CreateVpnConnection, DescribeVpnConnections, and ModifyVpnConnectionAttribute.

| Name | Type | Required | Description |
|------|------|----------|------|
| EncryptAlgorithm | String | No | Encryption algorithm. Available values: '3DES-CBC', 'AES-CBC-128', 'AES-CBC-192', 'AES-CBC-256', 'DES-CBC', and 'NULL'. Default is AES-CBC-128. |
| IntegrityAlgorith | String | No | Verification algorithm. Available value: 'MD5' and 'SHA1'. Default is MD5. |
| IPSECSaLifetimeSeconds | Integer | No | IPsec SA lifetime (in sec). Value range: 180-604800. |
| PfsDhGroup | String | No | PFS. Available value: 'NULL', 'DH-GROUP1', 'DH-GROUP2', 'DH-GROUP5', 'DH-GROUP14', and 'DH-GROUP24'. Default is NULL. |
| IPSECSaLifetimeTraffic | Integer | No | IPsec SA lifetime (in KB). Value range: 2560-604800. |

## InstanceChargePrepaid

Prepaid billing object.

Referenced by the following API: CreateVpnGateway, InquiryPriceCreateVpnGateway, InquiryPriceRenewVpnGateway, and RenewVpnGateway.

| Name | Type | Required | Description |
|------|------|----------|------|
| Period | Integer | Yes | Purchased usage period of an instance (in month). Value range: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36. |
| RenewFlag | String | No | Auto renewal flag. Value range: NOTIFY_AND_AUTO_RENEW: Notify expiry and renew automatically; NOTIFY_AND_MANUAL_RENEW: Notify expiry but not renew automatically. Default is NOTIFY_AND_MANUAL_RENEW. |

## ItemPrice

Price information of a billing item

Referenced by the following API: InquiryPriceCreateVpnGateway, InquiryPriceRenewVpnGateway, and InquiryPriceResetVpnGatewayInternetMaxBandwidth.

| Name | Type | Description |
|------|------|-------|
| UnitPrice | Float | Price of postpaid billing method (in CNY). |
| ChargeUnit | String | Billing unit of postpaid billing method. Value range: HOUR: bill by hour. The scenarios using this billing unit include: postpaid by hour (POSTPAID_BY_HOUR) and postpaid by bandwidth on an hourly basis (BANDWIDTH_POSTPAID_BY_HOUR). GB: The billing unit is calculated in GB. The scenario using this billing unit is: postpaid by traffic on an hourly basis (TRAFFIC_POSTPAID_BY_HOUR). |
| OriginalPrice | Float | Original price of the prepaid product (in CNY). |
| DiscountPrice | Float | Discount price of the prepaid product (in CNY). |

## NetworkInterface

ENI

Referenced by the following API: CreateNetworkInterface, and DescribeNetworkInterfaces.

| Name | Type | Description |
|------|------|-------|
| NetworkInterfaceId | String | ENI instance ID, such as eni-f1xjkw1b. |
| NetworkInterfaceName | String | ENI name |
| NetworkInterfaceDescription | String | ENI description. |
| SubnetId | String | Subnet instance ID. |
| VpcId | String | VPC instance ID. |
| GroupSet | Array of String | Bound security group. |
| Primary | Boolean | Indicates whether it is the primary ENI. |
| MacAddress | String | MAC address. |
| State | String | Value range: PENDING&#124;AVAILABLE&#124;ATTACHING&#124;DETACHING&#124;DELETING. |
| PrivateIpAddressSet | Array of [PrivateIpAddressSpecification](#PrivateIpAddressSpecification) | Information on private IP. |
| Attachment | [NetworkInterfaceAttachment](#NetworkInterfaceAttachment) | Bound CVM object. |
| Zone | String | Availability zone. |
| CreatedTime | String | Creation time. |

## NetworkInterfaceAttachment

Binding of ENI

Referenced by the following API: CreateNetworkInterface, and DescribeNetworkInterfaces.

| Name | Type | Description |
|------|------|-------|
| InstanceId | String | CVM instance ID. |
| DeviceIndex | Integer | The serial number of ENI in the CVM instance. |
| InstanceAccountId | String | The account information of the CVM owner. |
| AttachTime | String | Time when the ENI is bound. |

## Price

Price

Referenced by the following API: InquiryPriceCreateVpnGateway, InquiryPriceRenewVpnGateway, and InquiryPriceResetVpnGatewayInternetMaxBandwidth.

| Name | Type | Description |
|------|------|-------|
| InstancePrice | [ItemPrice](#ItemPrice) | Instance price. |
| BandwidthPrice | [ItemPrice](#ItemPrice) | Network price. |

## PrivateIpAddressSpecification

Information on private IP

Referenced by the following API: AssignPrivateIpAddresses, CreateNetworkInterface, DescribeNetworkInterfaces, ModifyPrivateIpAddressesAttribute, and UnassignPrivateIpAddresses.

| Name | Type | Required | Description |
|------|------|----------|------|
| PrivateIpAddress | String | Yes | Private IP address. |
| Primary | Boolean | No | Indicates whether it is the primary IP. |
| PublicIpAddress | String | No | Public IP address. |
| AddressId | String | No | EIP instance ID, such as eip-11112222. |
| Description | String | No | Description of private IP. |
| IsWanIpBlocked | Boolean | No | Indicates whether the public IP is blocked. |

## Quota

Quota information

Referenced by the following API: DescribeAddressQuota.

| Name | Type | Description |
|------|------|-------|
| QuotaId | String | Quota name. Value range:<br><li>`TOTAL_EIP_QUOTA`: Quota of EIPs under the user's current region<br><li>`DAILY_EIP_APPLY`: Number of applications for EIPs submitted in a day under the user's current region<br><li>`DAILY_PUBLIC_IP_ASSIGN`: Number of reassignments of public IPs under the user's current region. |
| QuotaCurrent | Integer | Current number |
| QuotaLimit | Integer | Quota |

## Route

Routing policy object

Referenced by the following API: CreateRouteTable, CreateRoutes, DeleteRoutes, DescribeRouteTables, ReplaceRoutes, and ResetRoutes.

| Name | Type | Required | Description |
|------|------|----------|------|
| DestinationCidrBlock | String | Yes | Destination IP address range, for example: 112.20.51.0/24. The values within the VPC IP address range cannot be used. | |
| GatewayType | String | Yes | Type of next hop. Supported types: CVM: Public gateway; VPN: VPN gateway; DIRECTCONNECT: Direct Connect gateway; PEERCONNECTION: Peering connection; SSLVPN: sslvpn gateway; NAT: NAT gateway; NORMAL_CVM: Ordinary CVM. |
| GatewayId | String | Yes | Next hop address. You simply need to specify the gateway ID of a different next hop type, and the system will automatically match the next hop address. |
| RouteId | Integer | No | Routing policy ID. |
| RouteDescription | String | No | Routing policy description. |
| Enabled | Boolean | No | Indicates whether it is enabled |

## RouteTable

Route table object

Referenced by the following API: CreateRouteTable, and DescribeRouteTables.

| Name | Type | Description |
|------|------|-------|
| VpcId | String | VPC instance ID. |
| RouteTableId | String | Route table instance ID, such as rtb-azd4dt1c. |
| RouteTableName | String | Route table name. |
| AssociationSet | Array of [RouteTableAssociation](#RouteTableAssociation) | Association of route table. |
| RouteSet | Array of [Route](#Route) | Route table policy set. |
| Main | Boolean | Indicates whether it is the default route table. |
| CreatedTime | String | Creation time. |

## RouteTableAssociation

Association of route table

Referenced by the following API: CreateRouteTable, and DescribeRouteTables.

| Name | Type | Description |
|------|------|-------|
| SubnetId | String | Subnet instance ID. |
| RouteTableId | String | Route table instance ID. |

## SecurityGroup

Security group object

Referenced by the following API: CreateSecurityGroup, and DescribeSecurityGroups.

| Name | Type | Required | Description |
|------|------|----------|------|
| SecurityGroupId | String | Yes | Security group instance ID, such as sg-ohuuioma. |
| SecurityGroupName | String | Yes | Security group name, which is limited to 60 characters. |
| SecurityGroupDesc | String | Yes | Remarks for security group, which is limited to 100 characters. |
| ProjectId | String | No | Project ID. Default is 0. It can be found on the project management page in the Tencent Cloud console. |
| IsDefault | Boolean | No | Indicates whether it is the default security group (which cannot be deleted). |
| CreatedTime | String | No | Creation time of the security group. |

## SecurityGroupAssociationStatistics

Statistics on the instances associated with the security group

Referenced by the following API: DescribeSecurityGroupAssociationStatistics.

| Name | Type | Description |
|------|------|-------|
| SecurityGroupId | String | Security group instance ID. |
| CVM | Integer | Number of CVM instances. |
| CDB | Integer | Number of database instances. |
| ENI | Integer | Number of ENI instances. |
| SG | Integer | Number of times a security group can be referenced by other security groups |
| CLB | Integer | Number of load balancer instances. |

## SecurityGroupPolicy

Security group rule object

Referenced by the following API: CreateSecurityGroupPolicies, DeleteSecurityGroupPolicies, DescribeSecurityGroupPolicies, ModifySecurityGroupPolicies, and ReplaceSecurityGroupPolicy.

| Name | Type | Required | Description |
|------|------|----------|------|
| PolicyIndex | Integer | No | Security group rule index. |
| Protocol | String | No | Protocol. Available values: TCP, UDP, and ICMP. |
| Port | String | No | Port (all, discrete port, range). |
| ServiceTemplate | Array of String | No | Protocol port ID or protocol port group ID. ServiceTemplate and Protocol+Port are mutually exclusive. |
| CidrBlock | String | No | IP address range or IP (mutually exclusive). |
| SecurityGroupId | String | No | IP address range or IP bound to the security group. |
| AddressTemplate | String | No | IP address ID or IP address group ID. |
| Action | String | No | ACCEPT or DROP. |
| PolicyDescription | String | No | Description of security group rules. |

## SecurityGroupPolicySet

Security group rule set

Referenced by the following API: CreateSecurityGroupPolicies, DeleteSecurityGroupPolicies, DescribeSecurityGroupPolicies, ModifySecurityGroupPolicies, and ReplaceSecurityGroupPolicy.

| Name | Type | Required | Description |
|------|------|----------|------|
| Version | String | No | Current version of security group rules. The version number is automatically increased by one each time you update the security rules, so as to prevent the expiration of updated routing rules. Conflict is ignored if it is left empty. |
| Egress | Array of [SecurityGroupPolicy](#SecurityGroupPolicy) | No | Outbound rules. |
| Ingress | Array of [SecurityGroupPolicy](#SecurityGroupPolicy) | No | Inbound rules. |

## SecurityPolicyDatabase

SecurityPolicyDatabase policy

Referenced by the following API: CreateVpnConnection, DescribeVpnConnections, and ModifyVpnConnectionAttribute.

| Name | Type | Required | Description |
|------|------|----------|------|
| LocalCidrBlock | String | Yes | VPC IP address range |
| RemoteCidrBlock | Array of String | Yes | Customer IDC IP address range |

## ServiceTemplate

Protocol port template

Referenced by the following API: CreateServiceTemplate, and DescribeServiceTemplates.

| Name | Type | Description |
|------|------|-------|
| ServiceTemplateId | String | Protocol port instance ID, such as ppm-f5n1f8da. |
| ServiceTemplateName | String | Template name. |
| ServiceSet | Array of String | Protocol port information. |
| CreatedTime | String | Creation time. |

## ServiceTemplateGroup

Protocol port template group

Referenced by the following API: CreateServiceTemplateGroup, and DescribeServiceTemplateGroups.

| Name | Type | Description |
|------|------|-------|
| ServiceTemplateGroupId | String | Protocol port template group instance ID, such as ppmg-2klmrefu. |
| ServiceTemplateGroupName | String | Protocol port template group name. |
| ServiceTemplateIdSet | Array of String | Protocol port template instance ID. |
| CreatedTime | String | Creation time. |

## Subnet

Subnet object

Referenced by the following API: CreateSubnet, and DescribeSubnets.

| Name | Type | Description |
|------|------|-------|
| VpcId | String | VPC instance ID. |
| SubnetId | String | Subnet instance ID, such as subnet-bthucmmy. |
| SubnetName | String | Subnet name. |
| CidrBlock | String | Subnet CIDR. |
| IsDefault | Boolean | Indicates whether it is the default subnet. |
| EnableBroadcast | Boolean | Indicates whether to enable broadcast. |
| Zone | String | Availability zone. |
| RouteTableId | String | Route table instance ID, such as rtb-l2h8d7c2. |
| CreatedTime | String | Creation time. |
| AvailableIpAddressCount | Integer | Number of available IPs. |

## Vpc

Virtual Private Cloud (VPC) object.

Referenced by the following API: CreateVpc, and DescribeVpcs.

| Name | Type | Description |
|------|------|-------|
| VpcName | String | VPC name. |
| VpcId | String | VPC instance ID, such as vpc-azd4dt1c. |
| CidrBlock | String | VPC CIDR, which can only lie within these three private IP address ranges: 10.0.0.0/16, 172.16.0.0/12, and 192.168.0.0/16. |
| IsDefault | Boolean | Indicates whether it is the default VPC. |
| EnableMulticast | Boolean | Indicates whether to enable multicast. |
| CreatedTime | String | Creation time. |
| DnsServerSet | Array of String | DNS list |
| DomainName | String | DHCP domain name option value |
| DhcpOptionsId | String | DHCP option set ID |

## VpnConnection

VPN tunnel object.

Referenced by the following API: CreateVpnConnection, and DescribeVpnConnections.

| Name | Type | Description |
|------|------|-------|
| VpnConnectionId | String | Tunnel instance ID. |
| VpnConnectionName | String | Tunnel name. |
| VpcId | String | VPC instance ID. |
| VpnGatewayId | String | VPN gateway instance ID. |
| CustomerGatewayId | String | Customer gateway instance ID. |
| PreShareKey | String | Pre-shared key. |
| VpnProto | String | Tunnel transmission protocol. |
| EncryptProto | String | Tunnel encryption protocol. |
| RouteType | String | Route type. |
| CreatedTime | Timestamp | Creation time. |
| State | String | Production status of the tunnel. Pending: Creating; AVAILABLE: Running; DELETING: Deleting. |
| NetStatus | String | Connection status of the tunnel. AVAILABLE: Connected. |
| SecurityPolicyDatabaseSet | Array of [SecurityPolicyDatabase](#SecurityPolicyDatabase) | SPD. |
| IKEOptionsSpecification | [IKEOptionsSpecification](#IKEOptionsSpecification) | IKE options. |
| IPSECOptionsSpecification | [IPSECOptionsSpecification](#IPSECOptionsSpecification) | IPSEC options. |

## VpnGateway

VPN gateway object.

Referenced by the following API: CreateVpnGateway, and DescribeVpnGateways.

| Name | Type | Description |
|------|------|-------|
| VpnGatewayId | String | Gateway instance ID. |
| VpcId | String | VPC instance ID. |
| VpnGatewayName | String | Gateway instance name. |
| Type | String | Gateway instance type: 'IPSEC' and 'SSL'. |
| State | String | Gateway instance status. 'PENDING': Creating; 'DELETING': Deleting; 'AVAILABLE': Running. |
| PublicIpAddress | String | Gateway public IP. |
| RenewFlag | String | Gateway renewal type: 'NOTIFY_AND_MANUAL_RENEW': Manual renewal; 'NOTIFY_AND_AUTO_RENEW': Auto renewal |
| InstanceChargeType | String | Gateway billing type: POSTPAID_BY_HOUR: Postpaid by hour; PREPAID: Prepaid. |
| InternetMaxBandwidthOut | Integer | Outbound bandwidth of gateway. |
| CreatedTime | Timestamp | Creation time. |
| ExpiredTime | Timestamp | Expiration time of prepaid gateway. |
| IsAddressBlocked | Boolean | Indicates whether the public IP is blocked. |
| NewPurchasePlan | String | Change of billing method. PREPAID_TO_POSTPAID: Prepaid to postpaid by hour. |
| RestrictState | String | Gateway billing status. PROTECTIVELY_ISOLATED: Instance is isolated; NORMAL: Normal. |


