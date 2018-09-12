1) Log in to [CVM Console](https://console.cloud.tencent.com/), click "Virtual Private Cloud" in the navigation bar, select "Peering Connections" tab in the VPC console, and click "New"to create a peering connection.

2) In the pop-up box, enter the name, and select the local region, local network, peer region, peer account type and peer network.
- If the peer account type is "My Account", select the peer network from the drop-down list.
- If the peer account type is "Other accounts", enter the QQ ID of peer account and peer VPC ID.

3) Select the maximum bandwidth.
- For the peering connection within the same region, there is no restriction on bandwidth, so this can't be modified.
- For a cross-region peering connection, you can select a maximum bandwidth. If you need a higher cross-region bandwidth, please initiate a request by submitting a ticket.


> Note: The CIDRs of the VPCs at the two sides of the peering connection must not overlap, otherwise an error may occur during the creation of connection. For a cross-region peering connection, a VPC's CIDRs used for multiple peer networks should not overlap, otherwise an error will occur.

4) A peering connection between the VPCs under the same account takes effect immediately after its creation. If you want to create a peering connection to a VPC under another account, the connection takes effect only after the peer VPC accepts the connection request.

> Note: Any fees charged for a cross-region peering connection are paid by the initiator of the connection.
