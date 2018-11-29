When another account sends a request to your account for a peering connection, you will see a peering connection with a status of "To be Accepted" in the "Peering Connections" tab in the VPC console.

Please do not accept any peering connection request from an unknown account because it may pose risks to your network.

If you do not accept the peering connection request, it will expire automatically after 7 days.

1) Log in to [CVM Console](https://console.cloud.tencent.com/), click "Virtual Private Cloud" in the navigation bar, select the "Peering Connections" tab in the VPC console to view the peering connection to be accepted in the peering connection list, and click "Accept" button on the operation column.

2) The peering connection is created.

> Note:

> After the peering connection is created, you need to add the route that points to the peering connection in the VPCs of both sides to allow local VPC and the peer VPC to interconnect with each other. For details, refer to [Configuring Routing Tables for Peering Connections](https://cloud.tencent.com/doc/product/215/%E4%B8%BA%E5%AF%B9%E7%AD%89%E8%BF%9E%E6%8E%A5%E9%85%8D%E7%BD%AE%E8%B7%AF%E7%94%B1%E8%A1%A8)
> 
> Any fees charged for the cross-region peering connection are paid by the initiator, instead of the accepter.
