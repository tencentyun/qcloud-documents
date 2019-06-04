After successful purchase and delivery of public network gateway, you can add the routing rule with the next hop as "public network gateway" in the routing table.

- You only need to ensure the normal running of the public network gateway host to achieve routing forwarding.

- To configure NAT on the public network gateway, you need to configure it on the host by yourself.

- The routing system does not check the health of public network gateway. When the public network gateway is not running, the route forwarding function may fail.

- When the private IP for the CVM used as the public network gateway has been changed, the related entries in the routing table will become invalid. Please re-configure the routing table containing the public network gateway.
