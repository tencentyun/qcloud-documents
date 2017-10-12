If you need the Direct Connect to connect your data center and the VPC on Tencent Cloud, please perform the steps as follows:
Step 1: Creating the physical Direct Connect
Step 2: Creating the Direct Connect tunnel
Step 3: Creating the Direct Connect tunnel for Direct Connect gateway, thus connecting your data center to your VPC.
(Optional) Step 4: Configuring the Direct Connect NAT
Step 5: Configuring the routing table associated with the subnets requiring communication.

These steps are described in detail below:
### Step 1: Creating the Physical Direct Connect
1) Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), click "Direct Connect" - "Physical Direct Connect" tab, and then click "New" button.
2) You need to carefully verify the region where the local data center is located, Direct Connect ISPs and the bandwidth of your physical Direct Connect, as these parameters cannot be changed once confirmed. After entering the basic information for the application of the physical Direct Connect, you will be provided with the recommended price based on the region of your local data center. You do not need to pay it during application.
3) After clicking "OK", you can find your Direct Connect application record on the "Application Record" page of the Direct Connect console. Our Direct Connect manager will contact you within 1 business day for the details of the Direct Connect. After it's approved, the status of the application record will change to "Payment Pending". If Tencent Cloud is deemed incapable of meeting your requirements for the applied Direct Connect after communication, the manager will change the status to "Application Refused".

The payment may be different depending on the establishment mode, the region where the local data center is located, and the bandwidth of Direct Connect. Once the payment is confirmed and paid, Tencent Cloud will carry out the Direct Connect construction based on the information you submitted, and if there is any parameter error found during its construction, you should bear the full cost incurred therefrom. The physical Direct Connect cannot be deleted during construction. After construction is completed, its status will change to "Running" on its console.

![](//mccdn.qcloud.com/img567fa85e57aa3.png)

### Step 2: Creating the Direct Connect Tunnel
1)	Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), click the "Virtual Private Cloud" in the navigation bar to enter the [Virtual Private Cloud Console](https://console.cloud.tencent.com/vpc/vpc?Rid=8), and then click "Direct Connect" - "Direct Connect Gateway" tab.
2) Click the "New" button to enter the Direct Connect creation page.
3) Enter the name, VPC and address mapping mode, and select whether to enable the network address translation function. (**This function is only available in the beta test currently**. Please activate it by a ticket or your customer manager.)
4) Click OK to confirm the information and complete the creation of the Direct Connect gateway.

### Step 3: Creating the Direct Connect Tunnel
1)	Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), and click "Direct Connect"- "Direct Connect Tunnel" tab.
2) You can only create the Direct Connect tunnel for a physical Direct Connect in "Running" status to establish a network link in the physical Direct Connect. Click the "New" button to enter the Direct Connect tunnel creation page.

Direct Connect tunnel supports BPG route and static route. BGP ASN and BGP key are required for BPG route.
The Vlan ID and Peer IP are configured automatically.

After the Direct Connect tunnel is created, it will take 1-2 business days to deploy network changes, during which please contact our Direct Connect manager for any questions you may have.

### (Optional) Step 4: Configuring the Direct Connect NAT
You can configure the gateway's network address translation on the Direct Connect gateway page. Such translation can be divided into IP translation and IP port translation.
#### IP Translation Configuration
IP translation refers to the original IP translation to the new IP to achieve network interconnection, which includes local IP translation and peer IP translation. IP translation does not distinguish whether the access is initiated by the source or the destination. The new IP can either access or be accessed by the peer. The specific procedure is as follows:

1) Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), click the "Virtual Private Cloud" in the navigation bar to enter the [Virtual Private Cloud Console](https://console.cloud.tencent.com/vpc/vpc?Rid=8), and then click "Direct Connect" - "Direct Connect Gateway" tab.
2) Click the ID of the Direct Connect gateway to enter its details page.
3) Edit the rules for "Local IP Translation".

- Adding: In the top-left corner of the IP mapping page, click the "New" blue button and enter the original IP, mapped IP and note. ACL rule for the new local IP translation rule is ALL PASS by default, which means the local IP translation is valid for all Direct Connect tunnels. You can edit the ACL rule for the local ACL translation to change the applicable scope of the local IP translation.
- Deleting: Click "Delete" to the right of the IP translation rule and click OK to confirm the deletion. When the IP translation rule is deleted, all the ACL rules under it will also be deleted.
- Modifying: Click the "Modify IP Mapping" to the left of the IP translation rule to edit the original IP, mapped IP and note of the local IP translation rule. The modified IP translation takes effect immediately after clicking OK.

4) Configure the network ACL rules for local IP translation.
ACL rules support TCP and UDP protocol. The local IP mapping ACL rules support the source port, destination IP, and destination port. If the port and the IP are left blank, it means ALL. When ALL is selected for the protocol, both the port and the IP will default to ALL.
- Adding: Click "Edit ACL Rule" to the right of the IP mapping rule and click "Add" next to the existing ACL rules.
- Deleting: Click "Edit ACL Rule" to the right of a IP mapping rule for editing. Click "Delete" and OK to delete the ACL rule. You can also click the "Delete" button next to the ACL rule to delete it.
- Modifying: Click "Edit ACL Rule" to the right of a IP mapping rule to modify a ACL rule. You can also click the "Modify" button next to the ACL rule to modify it.


#### IP Port Translation Configuration
IP port translation refers to the original IP port mapping to the new IP port to achieve network interconnection, which includes **local source IP port translation** and **local destination IP port translation**. The specific procedure is as follows:

1) Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), click the "Virtual Private Cloud" in the navigation bar to enter the [Virtual Private Cloud Console](https://console.cloud.tencent.com/vpc/vpc?Rid=8), and then click "Direct Connect" - "Direct Connect Gateway" tab.
2) Click the ID of the Direct Connect gateway to enter its details page.
3) On the Direct Connect gateway details page, click "Source IP Port Translation". There are two steps for configuring source IP port translation:

**Step 1: Configuring the local IP port translation address pool**
- Adding: Click "New" in the mapped IP pool page, enter the mapped IP pool (IP or IP segment is supported) and note (optional); ACL rule for the new IP pool is ALL DROP by default, and you need to edit the ACL rule to enable network translation;
- Deleting: Click "Delete" to the right of the IP address pool to delete the address pool. Deleting an address pool will delete the ACL rules associated with the address pool automatically.
- Modifying: Click "Modify Mapped IP Pool" to the right of the IP address pool to edit the IPs and note of the mapped IP pool.

**Step 2: Configuring the network ACL rule for the IP address pool**
ACL rules support configuration protocol (TCP or UDP), source IP, source port, destination IP, and destination port.
- Adding: Click "Edit ACL Rule" to the right of the IP address pool for editing. Click "New Line" at the bottom of the rule to add a new ACL rule.
- Deleting: Click "Edit ACL Rule" to the right of the IP address pool for editing. Click "Delete" to the right most of an ACL rule to delete it. You can also delete an ACL rule by expand it and click "Delete" to the right most of it.
- Modifying: Click "Edit ACL Rule" to the right of the IP address pool for editing. You can also modify an ACL rule by expand it and click "Modify" to the right most of it.

4) Configuring the local destination IP port translation.
On the Direct Connect gateway details page, click "Local Destination IP Port Translation" tab.
Adding: Click "Add" on the IP port mapping page to add a new IP port mapping.
Deleting: Click "Delete" to the right of the line where the IP port mapping is located to delete the mapping.
Modifying: Click "Modify IP Port Mapping" to the right of the line where the IP port mapping is located to modify the mapping and note of this IP port mapping.

### Step 5: Configuring the routing table associated with the subnets requiring communication
1)	Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), click "Virtual Private Cloud" in the navigation bar to enter the [Virtual Private Cloud Console](https://console.cloud.tencent.com/vpc/vpc?rid=8).
2)	Click "Routing Table" in the left navigation bar and click the routing table ID associated with the subnet requiring communication to enter its details page.
3)	Click the "Edit" and "New line", enter the destination network segment, and select "Direct Connect" as the next hop type; then select the gateway name for next hop.
4)	Click "Save".

### Step 6: Setting the alarm
1)	Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), click "Cloud Products" - "Monitor & Management" - ["Cloud Monitoring"](https://console.cloud.tencent.com/monitor/overview) in the top navigation bar, and then select "My Alarms" - ["Alarm Policy"](https://console.cloud.tencent.com/monitor/policylist) in the left navigation bar, and click Add Alarm Policy.
2)	Fill in the Policy Name, select "Physical Direct Connect" or "Direct Connect Tunnel" in Policy Type, and then add the Hit Condition.
3)	**Associate alarm objects**: select the alarm receiver group. You can view the set alarm policy in the policy list after you click "Complete".
4)	**View the alarm information**: when the alarm is triggered, you will receive SMS/email/internal message or other notices, and you can also find the information in the left navigation "My Alarms" - "Alarm List". For more information about alarms, refer to [Creating Alarms](https://cloud.tencent.com/doc/product/248/1073).
