Cloud Redis Storage supports multiple regions and availability zones globally. Regions supported by CVMs are supported by Cloud Redis Storage as well.
 **Network Description:**

  1. Cloud products in the same region communicate with each other through private networks.
  2. Cloud products in different regions cannot communicate with each other through private networks. Peering connection support is required for communication between VPCs.
  3. When making a TencentDB for Redis purchase, you are recommended to choose the region where your CVM is located so as to minimize access delay.

