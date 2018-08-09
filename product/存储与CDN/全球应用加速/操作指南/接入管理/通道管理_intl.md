## Adding
1. Click **Add** on the **Access Management** page.
2. Enter the information of the new acceleration connection on the **Add a connection** pop-up window.
![](https://main.qcloudimg.com/raw/77b40895de2958a6878760ae66f9fa63.jpg)  
**Project**: The project of the connection, which can be changed.
**Connection Name**: Supports letters, with a length limited to 30 characters.
**Acceleration Region**: The region where the client locates or the one closest to the client.
**Origin Region**: The region where the destination server is located or the one closest to the destination server.
**Bandwidth Cap**: The maximum bandwidth of a acceleration connection. Maximum value is 1,000 MB (100 MB for certain connections).
**PPS Limit**: Max PPS supported, up to 1,000k (20k for certain connections)
3. Click **OK** to complete.
4. You can view the information of the connection list on the **Access Management** page.
![](https://main.qcloudimg.com/raw/2cd387d38f4aa10231c6c3bd94014d12.jpg)
**ID/Connection Name**: The ID and name of a connection. The connection name can be modified.
**VIP**: The IP address accessed by the client.
**Domain Name**: The domain name accessed by the client, which is assigned by the system and automatically bound to VIP.
**Status**: Only acceleration connections under "Normal" status can work normally.

## Connection Information
In **Access Management** page, click **ID/Name** of a specified connection. On the **Connection Info** tab page, you can view the details of the connection. **Forwarding IP** is the forwarding node IP at the end of the acceleration connection, and this forwarding node forwards the data of the acceleration connection to the origin server via the public network.
![](https://main.qcloudimg.com/raw/017eb1fa1161b43f7a11e32dc27295c9.jpg)

## Changing Project
1. Select connections on the **Access Management** page.
2. Click **Change Project**.
3. Select a destination project in the pop-up window, and click on it to complete the project change.
>**Note:**
>After the project is changed, connections may not reside in the current project view. You can view them by switching the project.

## Settings
Click **Settings** of a specified connection on the **Access Management** page to modify the project, connection name, bandwidth cap and concurrency limit.
>**Note:**
>Configuration of acceleration connections CANNOT be adjusted for origins located in the following regions:
Japan-Tokyo, India-Chennai, Australia-Sydney, Brazil-Sao Paulo, Central US-Dallas, East US-Washington.

## Enabling Connections
1. Select connections to be enabled on the **Access Management** page.
2. Click **Enable** to enable the specified connections in batch.
After the connections are enabled, the client can access them using VIP or domain name for acceleration.

![](https://main.qcloudimg.com/raw/7fa62f53889b0c7f500fa42e7e1e8ce6.jpg)

## Disabling Connections
1. Select connections to be disabled on the **Access Management** page.
2. Click **Disable** to disable the specified connections in batch.
>**Note:**
>A disabled connection will not generate bandwidth fee but will incur the connection fee unless it is deleted.

## Deleting Connections
1. Select connections to be deleted on the **Access Management** page.
2. Click **Delete**.
Deleted connections cannot be used by the client for acceleration.







