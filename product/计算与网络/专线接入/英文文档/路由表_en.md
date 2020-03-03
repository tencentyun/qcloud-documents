After a Direct Connect gateway is created and a Direct Connect tunnel is set, you can configure the routing table of the Virtual Private Cloud (VPC) in the console to direct the desired traffic to the Direct Connect gateway.

1) Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), select "Virtual Private Cloud" in the top navigation bar, and click the "Routing Tables" tab.

2) Click the ID of the routing table to be associated with the Direct Connect gateway to enter the routing table details page.

3) Click the "Edit" button, add policy in the routing table, enter the destination, and select "Direct Connect Gateway" for the next hop type to filter out the Direct Connect gateways you created.

4) Save the routing table.

Now, you can redirect all traffic to the specific destination to the Direct Connect gateway which is associated with your local data center. 
