IP resources of VPC are divided into private IP and public IP:

- Private IP is the IP within the VPC, located in the CIDR address block where the resource resides in;
- Public IP is the egress for the access of cloud resources to Internet resources, and is randomly assigned when the CVM is purchased.

## 1. Automatic Assignment of Private IPs

When you purchase resources in VPC, private IPs will be randomly assigned based on the available IP pool of subnet where the resources reside in. You can customize private IPs as required after the creation of resources.

## 2. Customization of Private IPs

You can customize the assignment of private IPs in the VPC details page. Currently, customization of private IPs is only supported for CVM.

Log in to [CVM Console](https://console.cloud.tencent.com/). Click "Virtual Private Cloud" in the navigation bar, select the VPC that needs to be configured with IP, and click "IP Address Assignment" in details page to perform the custom assignment of IP address for resources.

 ![](//mccdn.qcloud.com/img567fa3aadabb8.png)
 
## 3. Public IP and Internet Access

CVMs in VPC can interconnect with the Internet in the following ways:

- Public IP: CVM can directly interconnect with the Internet through its native public IP. The public network bandwidth is subject to the configuration upon the purchase of CVM;
- Public network cloud load balance: Used to provide services the users access as outsiders
- Public network gateway: Used for the route forwarding of the CVM without a public IP during its outgoing access
