## 1. Is the CVM in a basic network interconnecting with a VPC a part of VPC?
No. No VPC private IP address will be assigned to the CVM for interconnection in a basic network.

## 2. Is Classiclink available to all VPCs?
Classiclink is only supported for VPCs within the network segment of `10.[0~47].0.0/16`.

## 3. Can the traffic from the CVM interconnecting with a VPC via a basic network go through the VPC through network perimeter services (peering connection, public network gateway, NAT gateway, VPN gateway, Direct Connect gateway)?
No.

## 4. Will the CVM that interconnects with a VPC via a basic network be assigned to a new private IP address?
No.
