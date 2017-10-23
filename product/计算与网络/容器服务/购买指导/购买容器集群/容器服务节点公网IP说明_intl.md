
## How to Use Public IP of Container Service Node

### About Enabling Public IP

By default, public IP will be assigned to the cluster node if you create a cluster. With the assigned public IP, you can:

- log in to the cluster node server through the public IP.
- access the public network services through the public IP.

If you do not want your business to be directly exposed to the public network, but need to access the public network, you can use Tencent Cloud NAT gateway. Click to view [NAT gateway details](https://cloud.tencent.com/document/product/215/4975). The following shows how to use the NAT gateway to access the public network.

### About Purchasing Public Network Bandwidth

When you create public network services, the public network load balancer uses bandwidth and traffic of the node. If you need public network services, public network bandwidth is required for nodes.
If your business does not require public network services, you can choose not to purchase public network bandwidth.

### How to Use NAT Gateway

The CVM is not bound to an EIP; all traffic from accessing the Internet is forwarded through the NAT gateway. With this method, the traffic from the CVM accessing the Internet will be forwarded to the NAT gateway through the private network. That means this traffic will not be subject to the public network bandwidth limit specified when the CVM was purchased, nor will the traffic generated at the NAT gateway occupy the public network bandwidth egress of the CVM.
Tips on usage:
Step 1: Create a NAT gateway
- Log in to Tencent Cloud Console, select "Virtual Private Cloud" tab, and select "NAT Gateway".
- Click the "New" button at the upper left corner, and enter or specify the following parameters in the pop-up box:
- After selection, click "OK" to complete the creation of NAT gateway.
- After the creation of a NAT gateway, you need to configure the routing rules in the Routing Tables page in the Virtual Private Cloud console to direct the subnet traffic to the NAT gateway.
> Note: The rental fee will be frozen for 1 hour during the creation of NAT Gateway.

Step 2: Configure the routing table associated with the subnet
- Log in to Tencent Cloud Console, and click "Virtual Private Cloud" in the navigation bar to enter the VPC Console. Select "Routing Tables".
- In the routing table list, click the routing table ID with which the subnet that needs to access the Internet is associated to enter its details page, and click "Edit" button in the "Routing Rules".
- Click "New line", fill in the "Destination" field, select "NAT Gateway" in "Next hop type", and select the created NAT gateway ID.
- Click "OK". After the above configuration is made, the traffic generated when the CVM in the subnet associated with the routing table accesses the Internet will be directed to the NAT gateway.


### Others: Use EIP

The CVM is only bound to an EIP, and the NAT gateway will not be used. With this method, all traffic from the CVM accessing the Internet will go out from the EIP. That means this traffic will not be subject to the public network bandwidth limit specified when the CVM was purchased. The cost resulting from accessing the public network will be charged based on the network billing mode of the CVM.
Tips on usage: Please see [How to Use EIP](https://cloud.tencent.com/document/product/215/4958#.E6.93.8D.E4.BD.9C.E6.8C.87.E5.8D.97)

If you are using NAT gateway and EIP at the same time, with this method, all traffic from the CVM actively accessing the Internet can only be forwarded to the NAT gateway through the private network, and the returning packets will be returned to the CVM through the NAT gateway as well. This traffic will not be subject to the public network bandwidth limit specified when the CVM was purchased, nor will the traffic generated at the NAT gateway occupy the public network bandwidth egress of the CVM. If the traffic from the Internet actively accesses the elastic public IP of the CVM, the returning packets of the CVM will be uniformly returned through the EIP. This way, the resulting outbound traffic of the public network will be subject to the public network bandwidth limit specified when the CVM was purchased. The cost resulting from accessing the public network will be charged based on the network billing mode of the CVM.

> Note: For users with a Bandwidth Package for bandwidth sharing, the outbound traffic generated at the NAT gateway will be billed as per the Bandwidth Package (the 0.8 CNY/GB network traffic fee will not be charged separately). It's recommended that you set a limit on the outbound bandwidth of the NAT gateway, so as to avoid any high Bandwidth Package charge due to excessively high amount of such bandwidth.




