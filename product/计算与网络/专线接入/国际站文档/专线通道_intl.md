## Applying for a Tunnel

1. Open [Tencent Cloud Direct Connect Console - Direct Connect Tunnel](https://console.cloud.tencent.com/vpc/dcConn);
2. Click **+ New** to initiate the application for Direct Connect tunnel. You need to enter the following information to create a Direct Connect tunnel:
<style>
table th:first-of-type {
    width: 150px;
}
</style>

| Parameter | Description | Remarks |
| --------- | -------------------------------- | -------- |
| Direct Connect tunnel name | Create your Direct Connect tunnel name |      -     |
| Direct Connect type | Exclusive Direct Connect, which is the physical Direct Connect under your account, and shared Direct Connect, which is the physical Direct Connect connecting other accounts |    -       |
| Direct Connect provider | Enter the account under which the physical Direct Connect is to be shared | Only valid for shared Direct Connect |
| Physical Direct Connect | Select the ID of the physical Direct Connect for which you want to setup a tunnel |       -    |
| Shared Direct Connect ID | Enter the ID of the physical Direct Connect for which you want to setup a tunnel | Only valid for shared Direct Connect |
| Access network | VPC and BM network are supported |        -   |
| VPC/BM network | Select the ID of the network accessed via the Direct Connect tunnel |       -    |
| Direct Connect gateway | The gateway type is displayed on the left of the gateway name. Check if it meets you need |    -       |
| VLANID      | Enter the non-conflicted VLANID, which cannot be 0 in the mode of "shared Direct Connect", 0 indicates that the sub-API is not enabled for the physical Direct Connect and only one tunnel can be created | VLANID of the API via which physical Direct Connect and Tencent Cloud are interconnected |
| Interconnection method | Support auto assignment and manual assignment. If manual assignment is selected, pay attention to the accuracy of the interconnection IP | The interconnection IP cannot be changed after submission |
| Routing method | Support BPG route and static route. Routing information is required for static route | If static route is selected, ip-sla is not supported. Use BFD for BGP |
| BGP ASN   | Optional, automatically assigned if not specified. If the private ASN is out of range, use Fake ASN technology to solve it |     -      |
| BGP key | Optional, "Tencent" is displayed at frontend by default. Default is "Tencent". The key is not needed if it is left empty |     -      |
| Peer IP address range | Enter the user's IDC IP address range, which cannot conflict with that of VPC except in NAT mode | Only valid for static route |  

>**Note:**
- Only one Direct Connect tunnel can be created if the sub-API is not enabled for the physical Direct Connect. To create more tunnels, enable the sub-API mode for the network topology that created multiple tunnels and connected multiple VPCs.
Reason: The billed traffic of the Direct Connect tunnel comes from the sub-API of the physical Direct Connect. If you create local, cross-city, or even cross-country tunnel interconnection without enabling sub-API, it is technically impossible to distinguish the traffic of different tunnels. In such case, the traffic consumed by the physical Direct Connect API is billed based on the standard for cross-country interconnection and the originally free traffic consumed by local interconnection will also be billed.
If you want to create more tunnels or change the configuration, contact your Direct Connect manager.
- To ensure the refined scheduling capability of your network, do not publish the following routes: 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16 and 100.64.0.0/10.

#### How do you know the progress of tunnel construction?
- After submitting the application for the Direct Connect tunnel, the configuration of devices on the cloud is distributed immediately. It is recommended that you first configure the interconnection IP of devices not on the cloud to avoid the loss of associated tunnel traffic.
- You can see the progress of tunnel construction in the "Connection Status" under the Direct Connect tunnel. If the status of "Configuring" remains unchanged for more than 30 minutes, the tunnel application has been submitted to customer service for processing for security reasons. Please contact your architect or after-sales manager to follow up.

## Changing a Tunnel

You can change the interconnection IP and peer IP address range. If you need to change the VLANID of a Direct Connect tunnel, delete the existing tunnel and re-create one.
You cannot submit the ticket for change of the Direct Connect tunnel to the Direct Connect manager offline. Submit your change requirement in the console.

## Deleting a Tunnel
1. Open [Tencent Cloud Direct Connect Console - Direct Connect Tunnel](https://console.cloud.tencent.com/vpc/dcConn);
2. Locate the Direct Connect tunnel to be deleted in the list, click **Delete** and then **OK**.
3. The Direct Connect manager will delete the Direct Connect tunnel in 3 work days.

## Viewing Monitoring Data
You can query monitoring information (outbound and inbound bandwidth, latency) of a Direct Connect tunnel via console or APIs. The console operations are as follows:
1. Open [Tencent Cloud Direct Connect Console - Direct Connect Tunnel](https://console.cloud.tencent.com/vpc/dcConn);
2. Locate the Direct Connect tunnel in the list, and click the **Monitoring** button to query its monitoring information.

## Configuring Alarm Policies
You can configure alarms for a Direct Connect tunnel. The configuration steps are as follows:
1. Open [Cloud Monitoring - Alarm Policy Console](https://console.cloud.tencent.com/monitor/policylist).
2. Enter the alarm policy name.
3. Click **Add** and edit the alarm policy:
 - Select "Direct Connect Tunnel" for "Policy Type".
 - Select "Outbound Bandwidth", "Inbound Bandwidth", "Packet Loss", and "Latency" for "Alarm Triggering Conditions".
4. Click **Next: Associate Alarm Object**, and select the associated Direct Connect tunnel.
5. Set the **Alarm Receiver Group**, and then click **OK** to complete the alarm policy configuration.

After the Direct Connect tunnel alarm is configured, you can receive the system alarm according to the setting of the alarm receiving group. For more information on monitoring, please see [Cloud Monitoring](https://cloud.tencent.com/doc/product/248/967).

