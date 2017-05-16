
## 1. Region APIs
| Function | Action ID | Description |
|---------|---------|---------|
| Query Regions and Availability Zones | [DescribeRegions](/doc/api/456/6634) | Query details of availability zones of CPMs.  |

## 2. CPM APIs
| Function | Action ID | Description |
|---------|---------|---------|
|Purchase CPM | [BuyDevice](/doc/api/456/6638) | Purchase a CPM  |
| Query CPM | [DescribeDevice](/doc/api/456/6728) | Query details of purchased CPMs.  |
| Query Operating System List | [DescribeOs](/doc/api/456/6727) | Query the list of operating systems supported by specified CPM model.  |
| Query RAID List | [DescribeDeviceClassRaid](/doc/api/456/6640) | Query the list of RAID types supported by specified CPM model.  |
| Query Device Model | [DescribeDeviceClass](/doc/api/456/6636) | Query the list of CPM models available currently.  |
| Query Device Operation Log | [DescribeDeviceOperationLog](/doc/api/456/6637) | Query operation logs of CPMs.  |
| Query Asynchronous Task Status | [DescriptionOperationResult](/doc/api/456/6644) | Query the current status of the asynchronous task of a CPM.  |
| Reset Password | [ResetDevicePasswd](/doc/api/456/6641) | Used to reset root password for a CPM.  |
| Modify CPM Aliases | [ModifyDeviceAlias](/doc/api/456/6643) | Used to modify aliases of CPMs in batch.  |
| Reinstall Operating System | [ReloadDeviceOs](/doc/api/456/6642) | Used to reinstall the operating system of CPM.  |
| Start CPM | [StartDevice](/doc/api/456/6726) | Used to start a CPM.  |
| Shut Down CPM | [ShutdownDevice](/doc/api/456/6639) | Used to shut down a CPM.  |
| Restart CPM | [RebootDevice](/doc/api/456/6729) | Used to restart a CPM.  |

## 3. Out-of-Band APIs
| Function | Action ID | Description |
|---------|---------|---------|
| Get Out-of-Band VPN Information | [GetOutBandVPNAuthInfo](/doc/api/456/6679) | Query authenticated username, password and other information on the out-of-band VPN of CPM.  |
| Get Out-of-Band Login Information | [GetDeviceOutBandInfo](/doc/api/456/6678) | Query user name, password and other information for logging into out-of-band page of CPM.  |
| Reset Out-of-Band VPN password | [SetOutBandVPNAuthPwd](/doc/api/456/6680) | Used to reset the password for the authenticated user of out-of-band VPN of CPM.  |

## 4. VPC APIs
| Function | Action ID | Description |
|---------|---------|---------|
| Query VPC List | [DescribeBmVpcEx](/doc/api/456/6646) | Query the list of BM VPCs.  |
| Query Subnet List | [DescribeBmSubnetEx](/doc/api/456/6648) | Query the list of subnets in the BM VPCs.  |
| Apply for Subnet IP | [ApplyIps](/document/product/386/7337) | Used to apply for IPs of subnets in the BM VPCs.  |
| Return Subnet IP | [ReturnIps](/document/product/386/7338) | Used to return IPs of subnets in the BM VPCs.  |
| Register Subnet IP | [RegisterBatchIp](/document/product/386/7925) | Used to register IPs of subnets in the BM VPCs.  |


## 5. BM Load Balancer-Related APIs
| Function | Action ID | Description |
|---------|---------|---------|
| Query BM Load Balancer Price | [InquiryBmLBPrice](/doc/api/456/6652) | Query the prices of BM load balancers.  |
| Get BM Load Balancer Instance List | [DescribeBmLoadBalancers](/doc/api/456/6658) | Get the list of BM load balancer instances |
| Create BM Load Balancer | [CreateBmLoadBalancer](/doc/api/456/6651) | Create BM load balancers.  |
| Delete BM Load Balancer | [DeleteBmLoadBalancers](/doc/api/456/6665) | Delete BM load balancers.  |
| Bind Backend CPM to BM Load Balancer | [RegisterInstancesWithBmLoadBalancer](/doc/api/456/6654) | Used to bind CPMs to BM load balancers.  |
| Unbind Backend CPM from BM Load Balancer | [DeregisterInstancesFromBmLoadBalancer](/doc/api/456/6660) | Used to unbind BM load balancers from CPMs.  |
| Modify Attributes of BM Load Balancer | [ModifyBmLoadBalancerAttributes](/doc/api/456/6663) | Used to modify attributes of a BM load balancer.  |
| Get Backend CPM List of BM Load Balancer | [DescribeBmLoadBalancerBackends](/doc/api/456/6656) | Used to get the list of backend CPMs bound to a BM load balancer.  |
| Get BM Load Balancer Associated with CPM | [DescribeBmLoadBalancersByInstances](/doc/api/456/6655) | Used to obtain the BM load balancers associated with CPMs.  |
| Get BM Load Balancer Listener List | [DescribeBmLoadBalancerListeners](/doc/api/456/6657) | Used to obtain the list of BM load balancer listeners.  | 
| Create BM Load Balancer Listener| [CreateBmLoadBalancerListeners](/doc/api/456/6653) | Used to create BM load balancer listeners.  |
| Delete BM Load Balancer Listener | [DeleteBmLoadBalancerListeners](/doc/api/456/6664) | Used to delete BM load balancer listeners.  |
| Modify BM Load Balancer Listener | [ModifyBmLoadBalancerListener](/doc/api/456/6661) | Used to modify BM load balancer listeners.  |
| Query Health of BM Load Balancer | [DescribeBmLBHealthStatus](/doc/api/456/6659) | Query the health of BM load balancers.  |
| Modify Weight of Backend CPM of BM Load Balancer | [ModifyBmLoadBalancerBackends](/doc/api/456/6662) | Used to modify weight of backend CPM of BM load balancer.  |
| Query Asynchronous Task Status of BM Load Balancer | [DescribeBmLoadBalancersTaskResult](/doc/api/456/6666) | Query the statuses of asynchronous tasks of BM load balancers.  |


## 6. Elastic Public IP (EIP)-Related APIs
| Function | Action ID | Description
|---------|---------|---------|
| Query EIP list | [DescribeEipBm](/doc/api/456/6671) | Query the list of BM EIPs.
| Query EIP Quota | [DescribeEipBmQuot](/doc/api/456/6668) | Query the quota on the number of requested BM EIPs.
| Create EIP | [EipBmApply](/doc/api/456/6669) | Used to create a BM EIP.
| Bind EIP to CPM| [EipBmBindRs](/doc/api/456/6673)) | Used to bind BM EIPs to CPMs.
| Unbind EIP from CPM | [EipBmUnbindRs](/doc/api/456/6674) | Used to unbind BM EIPs from CPMs.
| Bind EIP to VPC IP | [EipBmBindVpcIp](/document/product/386/8684) | Used to bind BM EIPs to BM VPC IPs (mostly for virtualization).
| Unbind EIP from VPC IP | [EipBmUnbindVpcIp](/document/product/386/8685) | Used to unbind the BM EIPs from BM VPC IPs (mostly for virtualization)
| Release EIP | [EipBmDelete](/doc/api/456/6676) | Used to release BM EIPs.
| Update EIP Name | [ModifyEipAlias](/doc/api/456/6672) | Used to update the name of a BM EIP.
| Modify EIP Billing Mode | [EipBmModifyCharge](/doc/api/456/6675) | Used to modify the billing mode of a BM EIP.
| Query EIP Task Status | [EipBmQueryTask](/doc/api/456/6670) | Used to the statuses of asynchronous tasks of BM EIPs.


