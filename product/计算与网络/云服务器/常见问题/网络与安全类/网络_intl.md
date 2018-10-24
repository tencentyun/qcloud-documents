### After logging in to CVM, there is no network connection. How to troubleshoot the problem?
This may be caused by incorrect configuration of your server security group. Check the inbound and outbound rules of the server security group. Check whether your destination, protocol ports and policies are prohibited.

### Can a VPC instance interconnect with the basic network instance?

#### Supported, but the following restrictions apply:

The VPC IP address range (CIDR) must be `10.0.0.0/16 - 10.0.47.0/16` (including subsets). Otherwise conflicts will occur.

#### Procedure

Log in to [VPC Console](https://console.cloud.tencent.com/vpc/vpc?rid=1), click VPC ID/name to go to the VPC details page, and then associate the basic network CVMs to be interconnected in **Classiclink**. 

### How to view the basic network CVMs interconnected with the VPC?

Log in to [VPC Console](https://console.cloud.tencent.com/vpc/vpc?rid=1), click VPC ID/name to go to the VPC details page, and you can view basic network CVMs interconnected with the VPC CVM in **Classiclink**.

### Can the CVM be switched to overseas network?

The network cannot be changed for CVM after purchase. If you need an overseas network, you are recommended to return the CVM and re-purchase an overseas CVM.

### How to configure private network DNS?

Please see the **Private Network DNS** section of [Private Network Service](https://cloud.tencent.com/document/product/213/5225).

### Within the same IP address range, the local VPN can obtain the IP of the IP address range but cannot access the Internet. How to solve this problem?

Check if the following configurations are correct:

1. Are the manually added IP and the automatically obtained IP in the same IP subnet? Are the subnet masks the same? Is the default gateway configured? Is the default gateway address correct?
2. Is DNS configured and is the DNS address correct?
3. If none of the above is wrong, check if there is conflict of statically configured IP address.
  
If none of the above methods works, [submit a ticket](https://console.cloud.tencent.com/workorder/category) to contact us.

