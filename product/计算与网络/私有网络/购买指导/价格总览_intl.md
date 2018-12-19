## Overview

#### Free products:

- VPC, Subnet, Route Table, Network ACL, Security Group, Direct Connect Gateway, VPN Tunnel, Customer Gateway are available free of charge.
- Intra-region private connection is free of charge. 
- VPC-based Tencent Cloud resources are not charged additionally for VPC.

#### Paid products:

- A fee is charged for the communication via a public network. For more information, see details on how to charge for communication via a public network.
- For charges of NAT gateway, VPN gateway, and cross-region peering connection, see the following sections.

## NAT Gateway

Charges for a NAT gateway include a gateway rental fee (by hour) and a fee for traffic generated during the access to the Internet. Prices are shown below:

| Billing Item | Specification | Mainland China | Hong Kong, Singapore, Korea, Frankfurt, Silicon Valley, Bangkok | Toronto, Mumbai | Virginia |
| ---------------------------------- | ------------------------ | -------------------- | ------------------------------------------------------------ | --------------- | -------- |
| Rental fee for gateway(USD/hour) | Small (a maximum of 1,000,000 connections) | 0.089                | 0.13                                                         | 0.14            | 0.18     |
| | Medium (a maximum of 3,000,000 connections) | 0.28                 | 0.39                                                         | 0.42            | 0.54     |
| | Large (a maximum of 5,000,000 connections) | 0.89                 | 1.3                                                          | 1.4             | 1.8      |

The fee for traffic generated during the access to the Internet is as follows: 

| Billing Item | Mainland China (all regions), Hong Kong, Korea | Toronto, Frankfurt, Silicon Valley | Singapore | Virginia, Mumbai | Bangkok |
| ---------------------------------- | -------------------------------------- | ---------------------------------- | --------- | ---------------- | ------- |
| Traffic for Internet Access (USD/GB) | 0.12                                   | 0.077                              | 0.081     | 0.1              | 0.075   |

> Note:
>
> - For the accounts with a bandwidth sharing package, the fee for the outbound traffic from the NAT gateway is covered by the bandwidth package (the network traffic fee is not charged additionally). You're recommended to set a limit on the outbound bandwidth of the NAT gateway, so as to avoid a high bandwidth package fee due to the excessive use of outbound bandwidth of the NAT gateway. For more information, see billing by bandwidth package.
> - In case of Arrears: Consistent with CVM.
> - As the NAT gateway features master/slave hot backup, a 5 KB detection packet to the master/slave servers of the NAT gateway every three seconds, which incurs a traffic of 0.2747 GB/day.

## VPN Connection

VPN tunnels and customer gateways are free of charge, but the use of a VPN gateway is charged. 
Charges include a gateway rental fee (see below) and a fee for Internet access traffic. For more information, see [Public Network Billing Methods](https://intl.cloud.tencent.com/document/product/213/10578).

| Region | Mainland China | Hong Kong, Korea, Frankfurt, Silicon Valley, Virginia, Mumbai | Singapore, Toronto, Bangkok |
| ---- | -------------------- | ------------------------------------------------------------ | --------------------------- |
| Price (USD/hr) | 0.078                | 0.088                                                        | 0.12                        |

## Peering Connection

- Intra-region peering connection is available for free.

- Cross-region peering connection and cross-region interconnection over a basic network:

  - Postpaid on a daily basis. Payment is borne by the peering connection initiator.
  - Calculated as the peak bandwidth of the day multiplied by the applicable tiered price.
  - Peak bandwidth of the day is calculated as follows: Inbound/outbound bandwidth is captured every 5 minutes, and the maximum is taken as the peak bandwidth.

For more information, see the following table:

| Feature | Billing Method | Configuration | Price | | |
| -------------- | ------------------------------------------------------------ | ----------------- | ------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
|                |           | | Connection in Mainland China (all regions) | Connection between Mainland China (all regions) and regions outside Mainland China (Hong Kong, Korea, Frankfurt, Silicon Valley, Virginia, Mumbai, Singapore, Toronto, Bangkok) | Connection between regions outside Mainland China (Hong Kong, Korea, Frankfurt, Silicon Valley, Virginia, Mumbai, Singapore, Toronto, Bangkok) |
| Intra-region peering connection | Free | Free | Free | Free | Free |
| Cross-region peering connection | Peak bandwidth of the day billed on a daily basis (USD/Mbps/day). Peak bandwidth is calculated using the average bandwidth per 5 minutes | (0 , 20] Mbps     | 3.19                     | 15                                                           | 15                                                           |
|                |                                                              | (20 ,100] Mbps    | 1.98                     | 12                                                           | 12                                                           |
|                |                                                              | (100 , 500] Mbps  | 1.48                     | 9                                                            | 9                                                            |
|                |                                                              | (500 , 2000] Mbps | 1.19                     | 6                                                            | 6                                                            |
|                |                     | Over 2,000 Mbps  | 0.82                     | 5                                                            | 5                                                            |
