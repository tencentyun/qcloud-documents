If you need the Direct Connect to connect your IDC and the VPC on Tencent Cloud, please perform the steps as follows:
Step 1: Create the physical Direct Connect 
Step 2: Create the Direct Connect gateway
Step 3: Create the Direct Connect tunnel
Step 4: Configure the Direct Connect NAT (Optional)
Step 5: Configure the routing table associated with the subnets requiring communication

These steps are described in detail below:
## Step 1: Create the Physical Direct Connect
1. Log in to [Direct Connect Console](https://console.cloud.tencent.com/dc/dc) and click **Physical Direct Connect** in the left navigation pane to go to the physical Direct Connect page. Click the **+New** button, and the "Apply for Direct Connect" page pops up.
![Apply for Direct Connect](https://main.qcloudimg.com/raw/5bae5be140baa7e4af08c6581f29d99e.png)

2. Enter the corresponding information according to your requirements and complete the application.
> **Note:**
> Tencent Cloud physical Direct Connect supports both partner application and self-application:
>- Partner application: Click **Click to view** in the "Apply for Direct Connect" window to go to the "Tencent Cloud Cloud Marketplace Direct Connect Partner" page. You can select the appropriate Direct Connect service provider to provide you with the physical Direct Connect service.
>- Self-application: If the Tencent Cloud Direct Connect partner fails to meet your requirements, enter the corresponding parameter information as shown above. For specific instructions, please see [Physical Direct Connect Instructions](https://cloud.tencent.com/document/product/216/547#.E6.8E.A7.E5.88.B6.E5.8F.B0.E7.94.B3.E8.AF.B7).     

## Step 2: Create the Direct Connect Gateway
1. Log in to the [VPC Console](https://console.cloud.tencent.com/vpc/vpc?rid=1) and click **Direct Connect Gateway** in the left navigation pane to go to the Direct Connect gateway console or directly log in to the [Direct Connect Gateway Console](https://console.cloud.tencent.com/vpc/dcGw).
2. Click the **+New** button, and the "Create a Direct Connect Gateway" window pops up.
3. Select the network and the gateway type, and enter a name. Click **OK** after entering to complete the creation of the Direct Connect gateway.

## Step 3: Create the Direct Connect Tunnel
1. Log in to [Direct Connect Console](https://console.cloud.tencent.com/dc/dc) and click **Direct Connect Tunnel** in the left navigation pane to go to the Direct Connect tunnel page. Click the **+New** button, and the "Create a Direct Connect Tunnel" window pops up.
![Direct Connect tunnel](https://main.qcloudimg.com/raw/0f21ce6797247154ce8a9d32f28797f8.png)
![](https://main.qcloudimg.com/raw/68ea1a97d2e044cc4d8ad53e0a5fa9b4.png)

2. The Direct Connect tunnel refers to the connections using the backbone network of Tencent Cloud. The starting point is the access point of Tencent Cloud physical Direct Connect, and the end point is your VPC. Enter the corresponding technical parameters as shown in the above figure. For specific instructions, please see [Direct Connect Tunnel Instructions](https://cloud.tencent.com/document/product/216/548).

## Step 4: Configure the Direct Connect NAT (Optional)
You can configure the gateway's network address translation in the [Direct Connect Gateway Console](https://console.cloud.tencent.com/vpc/dcGw). Such translation can be divided into IP translation and IP port translation.
### IP translation configuration
IP translation refers to the translation from the original IP to the new IP to achieve network interconnection, which includes local IP translation and peer IP translation. IP translation does not distinguish whether the access is initiated by the source or the destination. The new IP can either access or be accessed by the peer. The specific procedure is as follows:
1. Log in to the [Direct Connect Gateway Console](https://console.cloud.tencent.com/vpc/dcGw) and click the Direct Connect gateway ID on the page to go to the details page of Direct Connect gateway. Select **Local IP Translation** page to add or edit IP mapping.
 - Adding: Click **+Add** under the IP mapping, and enter the original IP, mapping IP and comments.
ACL rule for the new local IP translation rule is ALL PASS by default, which means the local IP translation is valid for all Direct Connect tunnels. You can edit the ACL rule for the local ACL translation to change the applicable scope of the local IP translation.
 - Modifying: Click the **Modify IP Mapping** to the right of the IP translation rule to edit the original IP, mapping IP and comments of the local IP translation rule. Click **OK**, and the modified IP translation rule takes effect immediately.
 - Deleting: Click **Delete** to the right of the IP translation rule and click **OK** to confirm the deletion. When the IP translation rule is deleted, all the ACL rules under it will also be deleted.

2. Configure the network ACL rules for local IP translation.
ACL rules support TCP and UDP protocol. The local IP mapping ACL rules support the source port, destination IP, and destination port. If the port and the IP are left blank, it means ALL. When ALL is selected for the protocol, both the port and the IP will be set to ALL by default.
 - Adding: Click **Edit ACL Rule** to the right of the IP mapping rule and click **Add** next to the existing ACL rules.
 - Modifying: Click **Edit ACL Rule** to the right of an IP mapping rule to modify an ACL rule. You can also click the **Modify** button next to the ACL rule to modify it.
 - Deleting: Click **Delete** to the right of the IP translation rule and click **OK** to confirm the deletion. When the IP translation rule is deleted, all the ACL rules under it will also be deleted.

### IP port translation configuration
IP port translation refers to the original IP port mapping to the new IP port to achieve network interconnection, which includes "local source IP port translation" and "local destination IP port translation". The specific procedure is as follows:
1. Log in to the [Direct Connect Gateway Console](https://console.cloud.tencent.com/vpc/dcGw) and click the Direct Connect gateway ID on the page to go to the details page of Direct Connect gateway. Select **Local Source IP Port Translation** to configure the local source IP port translation.
 (1) Configuring the local IP port translation address pool.
     - Adding: Click **New** in the mapping IP pool page, enter the mapping IP pool (IP or IP segment is supported) and comments (optional); ACL rule for the new IP pool is ALL DROP by default, and you need to edit the ACL rule to enable network translation.
     - Modifying: Click **Modify Mapping IP Pool** to the right of the IP address pool to edit the IPs and comments of the mapping IP pool.
     - Deleting: Click **Delete** to the right of the IP address pool to delete the address pool. Deleting an address pool will delete the ACL rules associated with the address pool automatically.

 (2) Configuring the network ACL rule for the IP address pool.
ACL rules support configuration protocol (TCP or UDP), source IP, source port, destination IP, and destination port.
     - Adding: Click **Edit ACL Rule** to the right of the IP address pool for editing. Click **New Line** at the bottom of the rule to add a new ACL rule.
     - Modifying: Click **Edit ACL Rule** to the right of the IP address pool for editing. You can also modify an ACL rule by expanding it and clicking **Modify** to the right most of it.
     - Deleting: Click **Edit ACL Rule** to the right of the IP address pool for editing. Click **Delete** to the right most of an ACL rule to delete it. You can also delete an ACL rule by expanding it and clicking **Delete** to the right most of it.

2. Configure the local destination IP port translation.
On the Direct Connect gateway details page, click **Local Destination IP Port Translation** tab.
 - Adding: Click **Add**on the IP port mapping page to add a new IP port mapping.
 - Modifying: Click **Modify IP Port Mapping** to the right of the line where the IP port mapping is located to modify the mapping and note of this IP port mapping.
 - Deleting: Click **Delete** to the right of the line where the IP port mapping is located to delete the mapping.

## Step 5: Configure the Routing Table Associated with the Subnets Requiring Communication
1. Log in to [Tencent Cloud Console](https://console.cloud.tencent.com), and click **VPC** in the navigation bar to enter the VPC Console.
2. Click **Routing Table** in the left navigation bar and click the routing table ID associated with the subnet requiring communication to enter its details page.
3. Click **+New Routing Policies** to add new routing policies, and click **+New Line**. Enter the destination IP address range, select **Direct Connect Gateway** as the next hop type, and then select the gateway name for next hop.
4. Click **OK** to save the configuration.

## Step 6: Set the Alarm
1. Log in to [Tencent Cloud Console](https://console.cloud.tencent.com), select **Cloud Products -> Management Tools -> [Cloud Monitor](https://console.cloud.tencent.com/monitor/overview)** in the top navigation bar, and select **My Alarms** -> **Alarm Policy** in the left navigation pane to go to the alarm policy page. Click **+New Alarm Policies** to create a new policy.
2. Enter the Policy Name, select **Physical Direct Connect** or **Direct Connect Tunnel** in Policy Type, and then add the Alarm Triggering Conditions.
3. Associate alarm objects: Select the alarm receiver group, and when it is saved, you can view the set alarm polices in Policy List.
4. View the alarm information: when any alarm conditions are triggered, you will receive SMS/email/internal message or other notices, and you can also find the information in the left navigation **My Alarms** -> **Alarm List**. For more information on alarm, please see [Create Alarm](https://cloud.tencent.com/doc/product/248/1073).

