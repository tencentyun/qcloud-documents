After the creation of a NAT gateway, you need to configure the routing table in the Routing Tables page in the Virtual Private Cloud console to direct the subnet traffic to the NAT gateway.

1) Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), select "Virtual Private Cloud" tab, and select "NAT Gateway".

2) In the routing table list, click a routing table ID to enter its details page, and click "Edit" button in the "Routing Rules".

3) Click "New line", enter "0.0.0.0/0" in "Destination", select "NAT Gateway" in "Next hop type", and select the created NAT gateway IP in "Next hop".

4) Click "OK" to save the routing table.

After the above configuration is made, the traffic generated when the CVM in the subnet associated with the routing table accesses the Internet will be directed to the NAT gateway.
> Note: The destination of the routing table can be customized as required."0.0.0.0 / 0" is only provided as an example.
