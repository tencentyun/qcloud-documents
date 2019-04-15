## Basic Concepts

Elastic IP (EIP) is a public IP address that can be applied for independently. It supports dynamic binding and unbinding to CVM/NAT gateway instances. As shown in the figure below, you can bind or unbind it to a CVM (or NAT gateway instance) in the account. It is mainly used to shield off instance failures. For example, a DNS name is mapped to an IP address through the dynamic DNS mapping. It may take up to 24 hours to propagate this mapping to the entire Internet, while elastic IP enables the drift of an IP from one CVM to another. In case of a CVM failure, all you need to do is start another instance and remap it, thus responding rapidly to the instance failure.
Your EIP is associated with a Tencent Cloud account, instead of a CVM instance, until you choose to explicitly release it or your payment is more than 7 days overdue.
![](//mccdn.qcloud.com/static/img/3dbf04b5fb9bff4bef632074ecf767da/image.png)

## Range of Application
The elastic public IP address applies to the CVM instances of both basic networks and VPCs, and the NAT gateway instances in VPCs. It supports dynamic binding and unbinding. Please note that:

- There is a one-to-one relationship between EIPs and CVM/NAT gateways. As shown in the above figure, one EIP can only be bound to one CVM/NAT gateway instance in the same region at the same time. One CVM instance can only be bound to one EIP at the same time, while one NAT gateway can be bound to up to 10 EIPs at the same time.  
- When an EIP is bound to a CVM instance, the current public IP address of the instance will be released.
- If you choose to reassign a public IP when unbinding an EIP from a CVM instance, the instance will be automatically assigned to the new public IP.
- Terminating a CVM/NAT gateway instance will disassociate it from its EIP.
- If a CVM instance in a VPC is bound to an EIP and also resides in a subnet that is associated with a NAT gateway, the data packets accessing the public network will go through the NAT gateway instead of the EIP.


### Releasing an EIP
There are two ways to release an EIP:
- Users can actively release an elastic public IP through the console or cloud API;
- Release under arrears: A fee will be calculated by hour when the elastic IP is bound to no resource. After the account is negative for 2 hours and still not renewed, the elastic public IP will be inoperable within the following (24ｘ7) hours (until the account balance is greater than 0), that is, if the amount is still negative after (2+24ｘ7) hours, the elastic public IP will be automatically released.

## Reasons for Unavailable Elastic Public IPs
Reasons for unavailable elastic public IPs include:
- The elastic public IP is not bound to a cloud resource. For specific binding method, refer to Binding a CVM to an EIP
- Check whether there is a security policy inside the CVM instance. If the CVM instance has a security group policy, for example: 8080 port access is denied, the 8080 port of the elastic public IP is also inaccessible.

## How to Use NAT Gateway and Elastic Public IP

NAT gateway and elastic public IP are the two ways for the CVM to access the Internet. You can use either one of them or both of them to design your public network access architecture.

### Method 1: Use NAT gateway only
The CVM is not bound to an elastic public IP; all traffic from accessing the Internet is forwarded through the NAT gateway. With this method, the traffic from the CVM accessing the Internet will be forwarded to the NAT gateway through the private network. That means this traffic will not be subject to the public bandwidth limit specified when the CVM was purchased, nor will the traffic generated at the NAT gateway occupy the public bandwidth egress of the CVM.

### Method 2: Use elastic public IP only
The CVM is only bound to an elastic public IP, and the NAT gateway will not be used. With this method, all traffic from the CVM accessing the Internet will go out from the elastic public IP. That means this traffic will not be subject to the public bandwidth limit specified when the CVM was purchased. The cost resulting from accessing the public network will be charged based on the network billing mode of the CVM.

### Method 3: Use both the NAT gateway and the elastic public IP
The CVM is bound to an elastic public IP; meanwhile all traffic from the subnet route accessing the Internet is directed to the NAT gateway. With this method, all traffic from the CVM actively accessing the Internet **can only be forwarded to the NAT gateway through the private network**, and the returning packets will be returned to the CVM through the NAT gateway as well. This traffic will not be subject to the public bandwidth limit specified when the CVM was purchased, nor will the traffic generated at the NAT gateway occupy the public bandwidth egress of the CVM. If the traffic from the Internet actively accesses the elastic public IP of the CVM, the returning packets of the CVM will be uniformly returned through the elastic public IP. This way, the resulting outbound traffic of the public network will be subject to the public bandwidth limit specified when the CVM was purchased. The cost resulting from accessing the public network will be charged based on the network billing mode of the CVM.

> Note: For users with a Bandwidth Package for bandwidth sharing, the outbound traffic generated at the NAT gateway will be billed as per the Bandwidth Package (the RMB 0.8/GB network traffic fee will not be charged separately). It's recommended that you set a limit on the outbound bandwidth of the NAT gateway, so as to avoid any high Bandwidth Package charge due to excessively high amount of such bandwidth.


Usage Restrictions

Note: Click to view the usage restrictions of other products within the VPC.

| Resources | Limit |
|---------|---------|
| Quota of elastic public IPs for each Tencent Cloud account in each region | 20 |
| Number of purchases that can be made by each Tencent Cloud account in each region per day | Quota X 2 (times) |
| Number of reassignments of public IPs that can be made for free by each account in a day when an EIP is unbound | 10 times |

## EIP Billing Method
The EIPs that are bound to CVMs (or NAT gateways) are free. To ensure the effective use of elastic IP addresses, the elastic IPs that are not bound to CVM or NAT instances will be charged a resource occupancy fee by hour (Less than 1 hour will be counted as 1 hour. Settlement is made per hour). The detailed billing standard is listed in the table below. It is recommended that you release the elastic public IPs that are not used in a timely manner so as to ensure the rational use of IP resources and save your cost.

| Region of the Elastic Public IP | Price for No Binding |
|---------|---------|---------|
| Beijing, Shanghai, and Guangzhou | RMB 0.20/hour | 
| Hong Kong | RMB 0.30/hour | 
| North America | RMB 0.25/hour | 
`Note: Click to view the billing method for other products within the VPC`


## Operating Instructions
###  Applying for an EIP
1) Open the CVM Console.
2) In the left navigation pane, click "Elastic Public IP".
3) Select a region in the list and click the "Apply" button.
3) After the application is successful, the EIP you applied for will display in the EIP list.
![](https://mc.qcloudimg.com/static/img/9b456a3f09f479d553e06503dee42aa1/EIP.jpg)

### Modifying the EIP Name
1) Open the CVM Console.
2) In the left navigation pane, click "Elastic Public IP".
3) Click the Rename button in the EIP entry to be modified.
4) Enter a new name and click the "OK" button.

### Binding a CVM to an EIP
1) Open the CVM Console.
2) In the left navigation pane, click "Elastic Public IP".
3) Click the "Bind" button at the end of the EIP to which a CVM needs to be bound. If this EIP is already bound to a CVM, this button will be unavailable. Please unbind it first.
4) In the pop-up box, select the CVM for binding according to CVM instance ID.
5) Click "Bind".
Or:
1) Open the CVM Console, and enter the CVM instance list.
2) Click "Bind EIP" under the Operation column on the right side of the CVM to which an EIP needs to be bound.
3) In the pop-up Bind EIP box, select the EIP you want to bind, and click the "OK" button.

### Unbinding a CVM from an EIP
1) Open the CVM Console.
2) In the left navigation pane, click "Elastic Public IP".
3) Click the "Unbind" button at the end of the EIP which is already bound to a CVM.
4) Click "OK".
Or:
1) Open the CVM Console.
2) Click "Unbind EIP" under the Operation column on the right side of the CVM from which an EIP needs to be unbound.
3) In the pop-up Unbind EIP box, select whether you need to assign public IPs for free, and then click the "OK" button.

### Releasing an EIP
1) Open the CVM Console.
2) In the left navigation pane, click "Elastic Public IP".
3) Click the "Release" button at the end of the EIP to be released.
4) Click "OK".




