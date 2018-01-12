If you don't want to expose your business to the public network for business security, but want to access the public network, you can use Tencent Cloud [NAT Gateway](/doc/product/215/4975). The following describes how to access the public network via NAT gateway.
## Public IP
When a cluster is created, public IPs are assigned to the nodes of the cluster by default. With these public IPs, you can:
- Log in to the nodes of the cluster.
- Access the public network services.

## Public Network Bandwidth
When a public network service is created, the load balancer in the public network uses the bandwidth and traffic of nodes. If the public network service is required, the nodes need to use public network bandwidth. If the public network service is not needed for your business, you can choose not to purchase public network bandwidth.

## NAT Gateway
The CVM is not bound to an EIP, and all the traffic accessing the Internet is forwarded via the NAT gateway. In this way, the CVM traffic accessing the Internet is forwarded to the NAT gateway via the private network. This means that the traffic is not restricted by the upper limit of public network bandwidth specified when you purchase the CVM, and the traffic generated from the NAT gateway doesn't occupy the public network bandwidth egress of the CVM. To access the Internet via the NAT gateway, follow the steps below:

### Step 1: Create an NAT gateway
1. Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), and then select **Cloud Products** in the top navigation bar. Select **VPC** under **Cloud Computing and Network** to go to [VPC Console](https://console.cloud.tencent.com/vpc/vpc?rid=8), and then click "NAT Gateway" in the left navigation bar.
2. Click the "New" button at the upper left corner, and enter or confirm the following parameters in the pop-up box:
- Gateway name.
- Gateway type (It can be changed after creation).
- VPC of NAT gateway service.
- Assign an EIP to the NAT gateway. You can choose an existing EIP, or purchase and assign a new EIP.
3. After selection, click "OK" to complete the creation of the NAT gateway.
4. After the creation of the NAT gateway, you need to configure the routing rules on the Routing Table page of the VPC Console to direct the subnet traffic to the NAT gateway.
>**Note:**
>The rental fee will be frozen for 1 hour during the creation of NAT gateway.

### Step 2: Configure the routing table associated with the subnet
1. Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), and then select **Cloud Products** in the top navigation bar. Select **VPC** under **Cloud Computing and Network** to go to [VPC Console](https://console.cloud.tencent.com/vpc/vpc?rid=8), and then click "Routing Table" in the left navigation bar.
2. In the routing table list, click the routing table ID associated with the subnet that needs to access the Internet to enter the details page of the routing table, and then click "Edit" button in "Routing Policies".
3. Click "New line", specify the "Destination", select "NAT Gateway" in "Next Hop Type", and then select the created NAT gateway ID.
4. Click "OK".
5. After the configuration, the traffic generated when the CVM in the subnet associated with the routing table accesses the Internet will be directed to the NAT gateway.

## Other solutions
### Solution 1: Use an EIP
CVM is only bound with EIP, instead of using NAT gateway. With this solution, all the traffic of the CVM accessing the Internet flows via the EIP and is restricted by the upper limit of public network bandwidth specified when you purchase the CVM. The fees for accessing the public network depends on the billing method of the CVM's network.
For more information, please see [How to Use EIP](/doc/product/215/4958#.E6.93.8D.E4.BD.9C.E6.8C.87.E5.8D.97).

### Solution 2: Use Both NAT Gateway and EIP
If both NAT gateway and EIP are used, all the traffic of the CVM accessing the Internet is only forwarded to the NAT gateway via the private network, and the response packets are returned to the CVM via the NAT gateway. This means that the traffic is not restricted by the upper limit of public network bandwidth specified when you purchase the CVM, and the traffic generated from the NAT gateway does not occupy the public network bandwidth egress of the CVM. If the traffic from the Internet accesses the EIP of the CVM, the response packets of the CVM are all returned through the EIP. In this case, the resulting outbound traffic of the public network is restricted by the upper limit of public network bandwidth specified when you purchase the CVM. The fees for accessing the public network depends on the billing method of the CVM's network.

>**Note:**
>For the accounts with a bandwidth package for bandwidth sharing, the fee for the outbound traffic from NAT gateway is covered by the bandwidth package (the network traffic fee of 0.8 CNY/GB is not charged additionally). You're recommended to set a limit on the outbound bandwidth of the NAT gateway, so as to avoid a high bandwidth package fee due to the excessive use of outbound bandwidth of NAT gateway.

