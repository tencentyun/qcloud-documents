## Step 1: Add Origin Servers
1. Log in to the GAAP console.
2. Add the information of all servers to which the access needs to be accelerated to **Origin Server Management**: 
 Click **Origin Server Management** > **Add**, enter origin server IPs or domain names, and then click **OK**.
![](https://mc.qcloudimg.com/static/img/ac9511613d74a7cf5e23086415eaca7a/image.png)
3. (Optional) Add an alias to the origin server for future use: Click the **Edit** icon next to the name of the origin server and enter a name.
![](https://mc.qcloudimg.com/static/img/0ec042ae5b755c121914f610a4f904bb/image.png)

## Step 2: Create an Acceleration Connection
1. Click **Access Management** > **Add**, and enter the information of an acceleration connection in the **Add a connection** pop-up window, and click **OK**.
![](https://mc.qcloudimg.com/static/img/1628b86e474d6dd5b9c0d8a39f6331ce/image.png)
**Acceleration Region** refers to the region where the client locates.
**Origin Region** refers to the region where the destination server is located.
**Bandwidth Cap** refers to the maximum bandwidth of a connection.
**PPS Limit** refers to the maximum number of concurrent connections supported for a connection.
After a new connection is created, you can view its information. **VIP**/**Domain Name** is the access address for the acceleration connection.
![](https://mc.qcloudimg.com/static/img/c6af107b3233e2ad87a00066325e9c32/image.png)
2. Click **ID/Name** of the connection to go to the next page.

## Step 3: Create a Listener
1. Select the **TCP/UDP Listener Management** tab, click **New**, and add a forwarding policy in the pop-up wizard.

2. Configure listener information (taking TCP as an example).
![](https://mc.qcloudimg.com/static/img/8f3839e16ecd68bd75fb61944e543ec2/image.png)
 Set the mapping relation between the protocol and the port for acceleration. **Source Port** is the access port of the acceleration connection VIP.
**Destination Port** refers to the access port of the origin server. Multiple port mappings can be added at a time, but the ports must be different from each other.

3. Configure the origin server processing policy.
 When a listener is bound with multiple origin servers, you need to select a policy for the scheduling among origin servers, as shown below:
![](https://mc.qcloudimg.com/static/img/a3b7dc951b25250c06ce5695337aba6a/image.png)
4. Configure the health check mechanism.
If TCP protocol is used, health check mechanism should be configured. Select "Enable Health Check" and then set the response time and the monitoring interval.
![](https://mc.qcloudimg.com/static/img/b90d35f384f2c9cb0390ec61c77e8c31/image.png)
**Response Timeout** refers to the response timeout.
**Health Check Interval** refers to the interval between two consecutive health checks. If an origin server is found abnormal during a health check, the origin server will stop forwarding packets until it recovers to a normal status.

## Step 4: Bind Origin Servers
Select a listener, click **Bind Origin Server** in the operation column to add all origin servers to be bound in the left list to the right area.
![](https://mc.qcloudimg.com/static/img/bc85fc6002afeab625f70ff1d66abbb2/image.png)

## Step 5: Use the Acceleration Connection
After completing the above steps, you can use the connection for acceleration when the listener's status becomes "Normal".
![](https://mc.qcloudimg.com/static/img/666877d9771c4fff446696e0b5f54798/image.png)

### Access methods
**Method 1:** If the client accesses the "VIP+" port, the acceleration from the client requiring acceleration to the destination server can be achieved.

**Method 2:** If the client accesses the "domain name+" port of an acceleration tunnel, the acceleration from the client requiring acceleration to the destination server can be achieved.

**Method 3:** If the client has originally accessed the domain name, this domain name can be resolved to that of an acceleration tunnel by configuring cname, to achieve acceleration from the client requiring acceleration to the destination server.

### Acceleration linkage
The acceleration linkage has three parts:

- Client to VIP: public network.
- VIP to the forwarding server of the origin server region: direct connect (private network).
- The forwarding server of the origin server region to the origin server: public network.
![](https://main.qcloudimg.com/raw/bb7c0a3625e29d9d19da15b7e3654d6b.png)

### Forwarding server IP
If security group rules have been set for the origin server, click **ID/Name** of the tunnel, and query "Forwarding IP" in the **Tunnel Information** tab. Acceleration is possible only if the origin server allows access from these IPs. See the figure below:
![](https://main.qcloudimg.com/raw/7d67f56766a3f736bbb1c0d2d56199f5.png)

To obtain the real IP of the client, please see [How does the server obtain the real client IP (TCP protocol only)](/document/product/608/14429).

### View statistics

You can view current and historical statistics on the statistics page. For more information, please see [Operation Guide](/document/product/608/13767).

