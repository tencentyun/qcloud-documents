## 1. VPC Related Parameters

| Parameters | Type | Description |
|---------|---------|---------|
| vpcId | String | vpcId assigned by the system. For example: gz_vpc_266 |
| unVpcId | String | New vpcID assigned by the system, upgraded from vpcId. For example: vpc-2ari9m7h. The system supports both IDs for compatibility purpose. It is recommended to use the new ID. |
| vpcName | String | VPC name, which can be 1-60 English characters (uppercase and lowercase). Numbers and underscores are also supported |
| cidrBlock | String | VPC network segment. Available values include 10.0.0.0/16, 172.16.0.0/16 and 192.168.0.0/16 as well as their sub segments. Please refer to VPC Network Segment Layout Instruction for details |
| createTime | String | VPC creation time. For example: 2016-05-18 15:01:46 |

## 2. Subnet Related Parameters

| Parameters | Type | Description |
|---------|---------|---------|
| subnetId | String | Subnet ID assigned by the system. For example: gz_subnet_18720 |
| unSubnetId | String | New subnet ID assigned by the system, upgraded from subnet ID. For example: subnet-2ari9m7h. The system supports both IDs for compatibility purpose. It is recommended to use the new ID. |
| subnetName | String | VPC name, which can be 1-60 English characters (uppercase and lowercase). Numbers and underscores are also supported. For example: Billing Platform VPC |
| cidrBlock | String | VPC network segment. Available values include 10.0.0.0/16, 172.16.0.0/16 and 192.168.0.0/16 as well as their sub segments. Please refer to VPC Network Segment Layout Instruction for details |
| zoneId | String | Availability zone ID, please refer to Availability Zone Management for details |
| createTime | String | Subnet creation time. For example: 2016-05-18 15:01:46 |

## 3. Routing Table Related Parameters

| Parameters | Type | Description |
|---------|---------|---------|
| routeTableName | String | Routing table name, which can be 1-60 Chinese or English characters (uppercase and lowercase). Numbers and underscores are also supported |
| destinationCidrBlock | String | Destination network segment. For example: 112.20.51.0/24. Cannot use values within the VPC network segment. |
| nextType | String | Type of next hop. Currently we support the following types: 0: public network gateway; 1: vpn gateway; 3: direct connect gateway; 4: peering connection; 7: sslvpn; 8: NAT gateway |
| nextHub | String | Next hop address. You can simply specify the gateway IDs (it is recommended to use new IDs) for different next hop types and the system will automatically match to the next hop address.  |

## 4. Network ACL related Parameters

| Parameters | Type | Description |
|---------|---------|---------|
| networkAclId | String | AclID assigned by the system. For example: acl-4n9efgju |
| networkAclName | String | Network ACL name, which can be 1-60 Chinese or English characters (uppercase and lowercase). Numbers and underscores are also supported |
| ruleDirection | Int | Direction of the network ACL rule. 0: out; 1: in |
| networkAclEntrySet | Array | ACL rule. Please refer to the Network ACL API document for details |


## 5. IPsec vpn Gateway Parameters

| Parameters | Type | Description |
|---------|---------|---------|
| vpnGwId | String | VPN gateway ID assigned by the system. For example: 95 |
| unVpnGwId | String | New VPN gateway ID assigned by the system, upgraded from vpnGwId. For example: vpngw-nhg87nmg. The system supports both IDs for compatibility purpose. It is recommended to use the new gateway ID |
| vpnGwName | String | VPN gateway name, which can be 1-60 Chinese or English characters (uppercase and lowercase). Numbers and underscores are also supported |
| vpnGwAddress | String | Public IP address of VPN gateway. For example: 115.159.26.189 |
| bandwidth | Int | VPN gateway bandwidth, for example: 5, 10, 20... (Unit: Mb). Please refer to the VPN Gateway Specification Instruction document for details |
| expireTime | String | Expiration time of the VPN gateway |
| isAutoRenewals | Bool | Indicate whether auto renewal is enabled. true: enabled; false: disabled. Default is true |
| state | Int | VPN gateway status. 0: Creating; 1: Creation failed; 2: Modifying; 3: Modification failed; 4: Deleting; 5: Deletion failed; 6: Running |
| createTime | String | VPN gateway creation time. For example: 2016-05-18 15:01:46 |


## 6. VPN Channel Parameters

| Parameters | Type | Description |
|---------|---------|---------|
| vpnConnId | String | VPN channel ID assigned by the system. For example: 534 |
| unVpnConnId | String | New VPN channel ID assigned by the system, upgraded from vpnConnId. For example: vpnx-pvjmedgm. The system supports both IDs for compatibility purpose. It is recommended to use the new channel ID |
| vpnConnName | String | VPN channel name, which can be 1-60 Chinese or English characters (uppercase and lowercase). Numbers and underscores are also supported |
| preSharedKey | String | Pre-shared private key |
| spdAcl | Array | SPD policy rule, used to configure traffic with a fine granularity. Refer to the VPN Channel API document for details |
| IKE | Array | IKE configuration. Refer to the VPN Channel API document for details |
| IPsec | Array | IPsec configuration. Refer to the VPN Channel API document for details |
| state | Int | VPN channel status. 0: Creating; 1: Creation failed; 2: Modifying; 3: Modification failed; 4: Deleting; 5: Deletion failed; 6: Running |
| createTime | String | VPN channel creation time. For example: 2016-05-18 15:01:46 |

## 7. Peer Gateway Parameters

| Parameters | Type | Description |
|---------|---------|---------|
| userGwId | String |Peer gateway ID assigned by the system. For example: 404 |
| unUserGwId | String | New peer gateway ID assigned by the system, upgraded from userGwId. For example: cgw-7ihaps8r. The system supports both IDs for compatibility purpose. It is recommended to use the new peer gateway ID |
| userGwName | String | Peer gateway name |
| userGwAddr | String | Peer gateway public IP address. Cannot use private address or broadcast address/multicast address |
| createTime | String | Peer gateway creation time. For example: 2016-05-18 15:01:46 |


## 8. SSL VPN Gateway Parameters

| Parameters | Type | Description |
|---------|---------|---------|
| sslVpnId | String | SSL VPN gateway ID assigned by the system, for example: vpngw-nhg87nmg |
| sslVpnName | String | SSL VPN name, which can be 1-60 Chinese or English characters (uppercase and lowercase). Numbers and underscores are also supported |
| sslVpnAddress | String | Public IP address of the SSL VPN gateway. For example: 115.159.26.189 |
| bandwidth | Int | SSL VPN gateway bandwidth, supported values: 5, 10, 20, 50, 100 (Unit: Mb). Please refer to the VPN Gateway Specification Instruction document for details |
| sslVpnPort | String | SSL VPN port |
| ipPool.n | Array | SSL VPN terminal IP pool, the terminal IP will assign IP from this pool. For example: ipPool.0=183.162.10.1 |
| acl | Array | acl rule information of the SSL VPN domain. Refer to the SSL VPN API document for details |
| expireTime | String | Expiration time of the SSL VPN gateway |
| isAutoRenewals | Bool | Indicate whether auto renewal is enabled. true: enabled; false: disabled. Default is true |
| state | Int | SSL VPN status. 0: Creating; 1: Creation failed; 2: Modifying; 3: Modification failed; 4: Deleting; 5: Deletion failed; 6: Running |
| createTime | String | SSL VPN creation time. For example: 2016-05-18 15:01:46 |

## 9. Peering Connection Related Parameters

| Parameters | Type | Description |
|---------|---------|---------|
| peeringConnectionId | String | Peering connection ID assigned by the system. For example: pcx-55i0gr4s |
| peeringConnectionName | String | Peering connection name, which can be 1-60 Chinese or English characters (uppercase and lowercase). Numbers and underscores are also supported |
| vpcId | String | vpcId of the initiator. For example: vpc-55i0gr4s |
| uin | String | QQ number of the initiator |
| region | String | Region of the initiator. For details about supported regions, please refer to the Peering Connection API document |
| peerVpcId | String | vpcId of the receiver. For example: vpc-55i0gr4s |
| peerUin | String | QQ number of the receiver |
| peerRegion | String | Region of the receiver. For details about supported regions, please refer to the Peering Connection API document |
| bandwidth | String | Peering connection bandwidth. For details about supported bandwidth, please refer to the Peering Connection API document |
| state | Int | Peering connection status; 0: Waiting to receive; 1: Running; 2: Expired; 3: Rejected; 4: Deleting; 5: Creation failed |
| createTime | String | Peering connection creation time. For example: 2016-05-18 15:01:46 |

## 10. Direct Connect Gateway Related Parameters

| Parameters | Type | Description |
|---------|---------|---------|
| directConnectGatewayId | String | Direct connect gateway ID. For example: dcg-rw6a1ozr |
| directConnectGatewayName | String | Peering connection name, which can be 1-60 Chinese or English characters (uppercase and lowercase). Numbers and underscores are also supported |
| type | Int | Direct connect gateway type. 0: Non-NAT; 1: NAT. Default is non-NAT gateway |
| natRule | Array | Network address translation rule. Refer to the Direct Connect Gateway API document for details |
| aclRule | Array | Network ACL rule group. Refer to the Direct Connect Gateway API document for details |
| createTime | String | Direct connect gateway creation time. For example: 2016-05-18 15:01:46 |

## 11. NAT Gateway Related Parameters

| Parameters | Type | Description |
|---------|---------|---------|
| natId | String | NAT gateway ID assigned by the system. For example: nat-dhfpwhtm |
| natName | String | NAT gateway name, which can be 1-60 Chinese or English characters (uppercase and lowercase). Numbers and underscores are also supported |
| maxConcurrent | Int | Maximum gateway concurrent connections. For example: 100, 300, 1000. (Unit: ten thousand) |
| bandwidth | Int | Maximum public network outbound bandwidth of the gateway (Unit: Mbps). Refer to the NAT Gateway API document for details |
| state | Int | NAT gateway status, 0: Running, 1: Unavailable, 2: Be in arrears and out of service |
| createTime | String | NAT gateway creation time. For example: 2016-05-18 15:01:46 |

## 12. ENI Related Parameters

| Parameters | Type | Description |
|---------|---------|---------|
| networkInterfaceId | String | Elastic NIC ID assigned by the system, for example: eni-9r7vukmh |
| eniName | String | ENI name, which can be 1-60 Chinese or English characters (uppercase and lowercase). Numbers and underscores are also supported |
| eniDescrption | String | ENI description (25 characters or less) |
| primary | Bool | ENI type. true: Primary ENI; false: secondary ENI |
| macAddress | String | mac address of the ENI. For example: 02:81:60:cb:27:37 |
| vpcId | String | VPC ID of the ENI. For example: vpc-2ari9m7h |
| subnetId | String | Subnet ID of the ENI. For example: subnet-2ari9m7h |
| createTime | String | ENI creation time. For example: 2016-05-18 15:01:46 |

## 13. Attributes Related to the Link between VPC and Basic Network
| Parameters | Type | Description |
|---------|---------|---------|
| classicLinkId | String | Link ID assigned by the system. For example: vcx-8kbdxt2h |
| vpcId | String | VPC ID. For example: gz_vpc_164 |
| instanceId | String | ID of the basic network CVM resource that is linked to the VPC. For example: ins-dgd54d |
| createTime | String | Creation time of the link between basic network device and VPC. For example: 2016-05-18 15:01:46 |

## 13. FlowLog Related Parameters
| Parameters | Type | Description |
|---------|---------|---------|
| vpcId | String | vpcId assigned by the system. For example: gz_vpc_266 |
| flowLogName | String | FlowLog name |
| flowLogDescription | String | FlowLog description，default "" |
| resourceType | String | Resource type of FlowLog，VPC\|SUBNET\|NETWORKINTERFACE |
| resourceId | String | Resource ID, For example:vpc-puz6fg, subnet-5o8ycyt, eni-08dhim |
| trafficType | String | Collect type of FlowLog，ACCEPT\|REJECT\|ALL | 
| cloudLogId | String | Storage ID of FlowLog, For example: d44e4cf0-c3e2-48d9-bb64-c5f0337ef2b0 |
| flowLogId | String | FlowLog unique ID，For example: fl-q1b26f3d |
| createdTime | String | FlowLog creation time |
