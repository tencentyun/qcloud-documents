After creating a Direct Connect gateway and setting a Direct Connect tunnel, you can configure the routing table of the VPC in the console to direct the desired traffic to the Direct Connect gateway.
1. Log in to the [Tencent Cloud Console](https://console.cloud.tencent.com/), select **Virtual Private Cloud** in the top navigation bar, and click the **Routing Tables** tab.
2. Click the ID of the routing table to be associated with the Direct Connect gateway to enter the routing table details page.
3. Click the **Edit** button and add a policy in the routing policies. Enter the **Destination**, and select "Direct Connect Gateway" for the **Next hop type** to filter out the Direct Connect gateway you created.
4. Save the routing table.

Now, you can direct the traffic of the specific destination to the Direct Connect gateway to associate it with your local IDC.

