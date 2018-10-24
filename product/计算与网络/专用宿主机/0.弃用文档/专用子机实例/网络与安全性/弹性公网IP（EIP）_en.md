The CVM instance described below also refers to dedicated CVM.

EIP is a static IP designed for dynamic cloud computing. It is a fixed public IP of a certain region. With EIP, you can quickly remap address to another CVM instance under your account (or [NAT Gateway](https://cloud.tencent.com/doc/product/215/%E7%BD%91%E5%85%B3#2.-nat.E7.BD.91.E5.85.B3) instance), to block instance failures.

Your EIP is associated with a Tencent Cloud account, instead of a CVM instance, until you choose to explicitly release it or your payment is more than 7 days overdue.

## Scope

EIP applies to the CVM instances of both basic networks and VPCs, and the [NAT Gateway](/doc/product/215/4975) instances in VPCs. EIP can only be bound to a CVM/NAT Gateway instance in the same region. Dynamic binding and unbinding are supported.

>Note:
- An EIP can be bound to only one CVM/NAT Gateway instance at a time
- A CVM/NAT Gateway instance can be bound with only one EIP at a time

When an EIP is bound to a CVM instance, the current public IP of the instance will be released to the public IP pool of the basic network. If you choose to reassign a public IP when unbinding an EIP from a CVM instance, the instance will be automatically assigned to a new public IP (there is no guarantee that it will be consistent with the public IP before binding). In addition, terminating an instance will disassociate it from its EIP.

## Service Limits


- The number of purchases that can be made by each Tencent Cloud account in each region per day is (quota*2) times.
- A maximum of 20 EIPs can be created under each Tencent Cloud account in each region.
- When an EIP is unbound, the number of reassignments of public IPs that can be made for free by each account in a day is 10.

## Releasing an EIP

- Users can actively release an EIP through the console or cloud API.

- Release under arrears: A fee will be calculated by hour when the EIP is bound to no resource. After the account is negative for **2** hours and still not topped up to an amount greater than 0, all the EIPs will remain inactive within the following (24*7) hours (until the account balance is greater than 0). If the amount is still negative after (2+24*7) hours, all the EIPs will be automatically released.

## Reasons for Unavailability of EIPs
Reasons for unavailability of EIPs include: 

- The EIP is not bound to a cloud resource. For more information, please see below.

- Check whether there is any security policy ([Security Group](/doc/product/213/5221) or [Network ACL](/doc/product/215/5132)) in effect. If the bound cloud product instance has a security policy, for example: 8080 port access is denied, then 8080 port of EIP is also inaccessible.

## Billing Method of EIP
An EIP that has been purchased but <font color="red">not yet bound to a cloud product instance (CVM or NAT Gateway)</font> will be charged a resource occupancy fee using the below chart (Less than 1 hour will be counted as 1 hour. Settlement is made per hour). <font color="red">EIPs bound to cloud product instances (CVMs or NAT Gateways) are free. </font>We recommend that you release the EIPs that are not used in a timely manner, to ensure the rational use of IP resources and save cost.


| Region of EIP     | Price of Unbound EIP   |
| -------------- | -------- |
| Beijing, Shanghai, and Guangzhou | 0.20 CNY/hr |
| Hong Kong           | 0.30 CNY/hr |
| North America           | 0.25 CNY/hr |
| Singapore          | 0.30 CNY/hr |

## Applying for EIP

1) Log in to [CVM Console](https://console.cloud.tencent.com/cvm).
​	
2) In the left navigation pane, click EIP.

3) Click "Apply" button.

4) After the application is successful, the EIP you applied for will display in the EIP list.

## Binding EIP to Cloud Products

1) Log in to [CVM Console](https://console.cloud.tencent.com/cvm).

2) In the left navigation pane, click EIP.

3) Click the "Bind" button at the end of the EIP with which a cloud product needs to be bound. If this EIP is bound to a cloud product instance, the button will be unavailable. Please unbind it first.
​	
4) In the pop-up box, select the type of the cloud product to be bound, and select the ID of the corresponding cloud product instance. Click the "Bind" button to complete binding with the cloud product.

## Unbinding EIP from Cloud Products

1) Log in to [CVM Console](https://console.cloud.tencent.com/cvm).

2) In the left navigation pane, click EIP.

3) Click the "Unbind" button at the end of the EIP which is already bound to a cloud product.

4) Click "OK".

At this point, the cloud product instance may be assigned with a new public IP. Details may vary with different cloud resources, depending on the actual situation.

## Releasing EIP
1) Log in to [CVM Console](https://console.cloud.tencent.com/cvm).

2) In the left navigation pane, click EIP.

3) Click the "Release" button at the end of the EIP to be released.

4) Click OK.

