To allow the private IPs at the two sides of a peering connection to send traffic to each other, you must add a route to the routing table associated with your VPC. This route points to the CIDR or CIDR subset of the peer VPC.

At the same time, the owner of the peer VPC needs to add a route that points to the local VPC in the routing table associated with the peer VPC.

1) Log in to [CVM Console](https://console.cloud.tencent.com/), click "Virtual Private Cloud" in the navigation bar, select "Routing Tables" tab in the VPC console.

2) Select the routing table associated with the specified local subnet in the peering connection, and click the ID of the associated routing table to enter the routing table details page.

3) Add a route. Enter the peer CIDR to which traffic of the peering connection is directed as the "Destination", select "peering connection" as the "Next hop type", and select the created peering connection as the "Next hop".

4) Save the routing table.

After the routing table is configured, the peering connection starts to work.
