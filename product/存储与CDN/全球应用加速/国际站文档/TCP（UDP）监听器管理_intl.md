## Adding
Click **ID/Name** of a specified tunnel on the **Access Management** interface to go to the next page, select the **TCP/UDP Listener Management** tab page, and click **New** to enter the wizard, as described below:

**Step 1:** Configure the listener information to set the mapping relation between the protocol and port for acceleration.
![](https://main.qcloudimg.com/raw/c80467cc3f0ace859666097f41663937.jpg)
**Origin Server Type** can be an IP address or a domain name, but only one type is supported for a listener.
**Source Port** is the access port of an acceleration tunnel VIP. Valid port range: 1-65535 (port 21 is unavailable). A single port or a range of consecutive ports is supported. Port must be unique. A maximum of 20 consecutive ports can be added at a time, for example: 8000-8019.

**Step 2:** Configure the origin server processing policy, that is, when a listener is bound with multiple origin servers, you need to select a policy for the scheduling among origin servers.
![](https://main.qcloudimg.com/raw/de87f8335ac2fea91480659f229d37b5.jpg)
**Polling**: Round Robin scheduling policy.
**Weighted Polling**: weighted RR (you can set the weight of each origin server when binding a listener).
**Minimum Number of Connections**: Choose the origin server with the lowest number of connections from all the origin servers to schedule first.
>**Note:**
>Listeners whose origin server type is domain name only support "Polling" as the scheduling policy. If the domain name is resolved to multiple IPs, each resolved IP is scheduled according to the polling policy.

**Step 3:** If TCP protocol is used, health check mechanism should be configured.
![](https://main.qcloudimg.com/raw/1f08eb9794e8cd77b539baf476dbceb3.jpg)
**Response Time**: Response timeout (valid only when **Enable health check** is selected)
**Monitoring Interval**: The interval between two consecutive health checks (valid only when **Enable health check** is selected)
If an origin server is found to be exceptional during health check, the packet is not forwarded via this origin server until it is recovered to a normal status.

## Settings
Click **Settings** on the **TCP/UDP Listener Management** tab page to modify the listener name, scheduling policy and health check parameters.

## Binding Origin Server
Click **Bind Origin Server** on the **Listener Management** tab page to bind or unbind multiple origin servers. If no origin server information is found, the origin server type is invalid or the origin server is not added to **Origin Server Management**.

If the listener policy is "Weighted Polling", you can set the weight (1-100) of the origin server while binding it. The origin server is scheduled based on the ratio of its weight to the total weight. For example, if the weight of the origin server 1 is 60 and that of the origin server 2 is 80, the ratio based on which the origin server 1 is scheduled is 60/(60+80)=42.8%, and the ratio based on which the origin server 2 is scheduled is 57.2%.
![](https://main.qcloudimg.com/raw/373fe6b23a0adf12729a3ee495cb1131.jpg)
If health check is enabled, when an origin server is bound, the health check starts. The status of the listener determines whether the origin server is normal. An acceleration tunnel only forwards packets to normal origin servers. Packets are not forwarded to an exceptional origin server until it is found to be normal during health check.

For listeners without health check policies or those with UDP protocols, packets are always forwarded regardless of the status of the origin server.

## Deleting
Click **Delete** on the **TCP/UDP Listener Management** tab page to delete a specified listener. Any listener that is bound with an origin server can be deleted only when "Allow force deletion of listeners bound with origin servers" is selected. After deletion, the acceleration of the port for the listener stops.
![](https://main.qcloudimg.com/raw/3a5d88ef16056a18f9cc76be470739ea.jpg)
