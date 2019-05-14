## 1. Creating Direct Connect Gateway

1) Open the [Tencent Cloud Console](https://console.cloud.tencent.com/), select "Virtual Private Cloud" in the top navigation bar, and click the "Direct Connect" - "Direct Connect Gateway" tab.

2) Click the "New" button to enter the Direct Connect creation page.

3) Enter the name, VPC and address mapping mode, and select whether to enable the network address translation function. (**This function is only available in the beta test currently**. Please activate it by a ticket or your customer manager.)

4) Click OK to confirm the information and complete the creation of the Direct Connect gateway.

## 2. Configuring the Network Address Translation (NAT) for Direct Connect Gateway


### 2.1. Configuring IP Translation

The specific procedure is as follows:
1) Open the [Tencent Cloud Console](https://console.cloud.tencent.com/), select "Virtual Private Cloud" in the top navigation bar, and click the "Direct Connect" - "Direct Connect Gateway" tab.

2) Click the ID of the Direct Connect gateway to enter its details page.

3) **Configure local IP translation**

On the Direct Connect gateway details page, click "Local IP Translation" tab. There are two steps for configuring local IP translation:

Step 1: Edit the rules for local IP translation.

- Adding: In the top-left corner of the IP mapping page, click the "New" blue button and enter the original IP, mapped IP and note. ACL rule for the new local IP translation rule is ALL PASS by default, which means the local IP translation is valid for all Direct Connect tunnels. You can edit the ACL rule for the local ACL translation to change the applicable scope of the local IP translation.
- Deleting: Click "Delete" to the right of the IP translation rule and click OK to confirm the deletion. When the IP translation rule is deleted, all the ACL rules under it will also be deleted.
- Modifying: Click the "Modify IP Mapping" to the left of the IP translation rule to edit the original IP, mapped IP and note of the local IP translation rule. The modified IP translation takes effect immediately after clicking OK.

Step 2: Configure the network ACL rules for local IP translation.
ACL rules support TCP and UDP protocol. The local IP mapping ACL rules support the source port, destination IP, and destination port. If the port and the IP are left blank, it means ALL. When ALL is selected for the protocol, both the port and the IP will default to ALL.

- Adding: Click "Edit ACL Rule" to the right of the IP mapping rule and click "Add" next to the existing ACL rules.
- Deleting: Click "Edit ACL Rule" to the right of a IP mapping rule for editing. Click "Delete" and OK to delete the ACL rule. You can also click the "Delete" button next to the ACL rule to delete it.
- Modifying: Click "Edit ACL Rule" to the right of a IP mapping rule to modify a ACL rule. You can also click the "Modify" button next to the ACL rule to modify it.
Note: When the Direct Connect gateway is also configured with "Peer IP Translation", the **Destination IP** of the ACL rule for local IP translation should be **the mapping IP of peer IP translation**, instead of the original IP.<br>

**Restrictions on rule**:
- The original IP must be within the CIDR range of VPC.
- The mapped IP can not be within the CIDR range of VPC to which the Direct Connect gateway belongs 
- The original IP is unique and can not be replicated. That means an IP in a VPC can only be mapped to one IP
- Mapped IP is unique and can not be replicated. That means multiple IPs in a VPC can't be mapped to the same IP
- Source or destination IP should not be broadcast address (255.255.255.255), Class D address (224.0.0.0 ~ 239.255.255.255), and Class E address (240.0.0.0 ~ 255.255.255.254)
- The maximum number of local IP translation rules for Direct Connect gateway is 100, and the maximum  20 ACL rules is possible for each local IP translation (the quota can be raised in the background on demand)


4) **Configuring peer IP translation**
On the Direct Connect gateway details page, click "Peer IP Translation" tab:
- Adding: In the top left corner of the IP mapping page, click the "New" button in blue and enter the original IP, mapping IP and comments.
- Deleting: Click the "Delete" to the right of the IP translation rule and confirm it.
- Modifying: Clicking the "Modify IP Mapping" to the left of the IP translation rule, you can then edit the original IP, mapping IP and comments of the peer IP translation rule. The modified IP translation takes effect after clicking OK.

**Restrictions on rule**:
- The mapping IP can not be within the CIDR range of VPC to which the Direct Connect gateway belongs
- The source IP is unique and can not be replicated. That means a peer IP of the Direct Connect can only be mapped to one IP
- Mapping IP is unique and can not be replicated. That means multiple peer IPs of the Direct Connect can't be mapped to the same IP
- Source or destination IP should not be broadcast address (255.255.255.255), Class D address (224.0.0.0 ~ 239.255.255.255), and Class E address (240.0.0.0 ~ 255.255.255.254)
- The maximum number of local IP translation rules for Direct Connect gateway is 100, and the maximum  20 ACL rules is possible for each local IP translation (the quota can be raised in the background on demand)


### 2.2. Configuring IP Port Translation

1) Open the [Tencent Cloud Console](https://console.cloud.tencent.com/), select "Virtual Private Cloud" in the top navigation bar, and click the "Direct Connect" - "Direct Connect Gateway" tab.

2) Click the ID of the Direct Connect gateway to enter its details page.

3) **Configure local source IP port translation**

On the Direct Connect gateway details page, click "Source IP Port Translation". There are two steps for configuring source IP port translation:

Step 1: Configuring the local IP port translation address pool.
- Adding: Click "New" in the mapping IP pool page, enter the mapping IP pool (IP or IP segment is supported, and IP segment is indicated in "A-B".) and comments (optional); ACL rule for the new IP pool is ALL DROP, and you need to additionally edit ACL Rules to implement Network Translation;
- Deleting: Click "Delete" on the right of the row of IP address pool to delete the address pool. Deleting an address pool will delete the ACL rules associated with the address pool automatically.
- Modifying: Click "Modify Mapped IP Pool" to the right of the IP address pool to edit the IPs and note of the mapped IP pool.

Step 2: Configuring the network ACL rule for the IP address pool
ACL rules support configuration protocol (TCP or UDP), source IP, source port, destination IP, and destination port.
- Adding: Click "Edit ACL Rule" to the right of the IP address pool for editing. Click "New Line" at the bottom of the rule to add a new ACL rule.
- Deleting: Click "Edit ACL Rule" to the right of the IP address pool for editing. Click "Delete" to the right most of an ACL rule to delete it. You can also delete an ACL rule by expand it and click "Delete" to the right most of it.
- Modifying: Click "Edit ACL Rule" to the right of the IP address pool for editing. You can also modify an ACL rule by expand it and click "Modify" to the right most of it.

Note: When the Direct Connect gateway is also configured with "Peer IP Translation", the **Destination IP** of the ACL rule for local source IP port translation should be **the mapping IP of peer IP translation**, instead of the original IP.<br>

**Restrictions on rule**:
- The IP address pool can not be within the CIDR range of VPC to which the Direct Connect gateway belongs
- ACL rules for multiple IP address pools should not overlap. Otherwise, this will cause network address translation conflicts
- IP addresses between multiple IP addresses should not overlap
- IP address pool only supports single IP or continuous IP, and network segment of continuous IP/24 should be consistent, that is, "192.168.0.1 ~ 192.168.0.6" is supported but "192.168.0.1 ~ 192.168.1.2" not
- Address pool should not contains broadcast address (255.255.255.255), Class D address (224.0.0.0 ~ 239.255.255.255), and Class E address (240.0.0.0 ~ 255.255.255.254)
- The maximum address pools of 100 is supported for local destination IP port translation, with maximum 20 ACL rules for each pool (the quota can be increased in the background on demand)

4) **Configuring the local destination IP port translation**
On the Direct Connect gateway details page, click "Local Destination IP Port Translation" tab:
- Adding: Click "Add" on the IP port mapping page to add a new IP port mapping.
- Deleting: Click "Delete" to the right of the line where the IP port mapping is located to delete the mapping.
- Modifying: Click "Modify IP Port Mapping" to the right of the line where the IP port mapping is located to modify the mapping and note of this IP port mapping.

**Restrictions on rule**:
- The original IP must be within the CIDR range of VPC
- The original IP port should be unique, that is, a same IP port within the VPC can only be mapped to one IP port
- The mapped IP can not be within the CIDR range of VPC to which the Direct Connect gateway belongs
- Mapped IP Port is unique and can not be replicated. That means multiple IP ports in a VPC can't be mapped to the same IP port
- Original or mapped IP should not be broadcast address (255.255.255.255), Class D address (224.0.0.0 ~ 239.255.255.255), and Class E address (240.0.0.0 ~ 255.255.255.254)
- The maximum IP port mappings of 100 is supported for local destination IP port translation (the quota can be increased in the background on demand)

**Note**: If both IP translation and IP port translation are configured, IP mapping will be matched with first if any conflicts.

## 3. Deleting Direct Connect Gateway

You can delete the Direct Connect gateway which you don't want to use again. Deleting a Direct Connect gateway will also delete its associated tunnel. Please make sure that this will not affect your normal service.

1) Open the [Tencent Cloud Console](https://console.cloud.tencent.com/), select "Virtual Private Cloud" in the top navigation bar, and click the "Direct Connect" - "Direct Connect Gateway" tab.

2) Select the Direct Connect gateway you want to delete, and click the "Delete" button in the Operation column.

3) The deletion will be completed after you confirm it.




