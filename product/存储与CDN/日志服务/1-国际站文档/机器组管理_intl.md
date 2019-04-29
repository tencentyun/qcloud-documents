A server group is a server object configured to collect logs by LogListener in Tencent Cloud CLS. Generally, different server groups are configured based on various business scenarios to help you manage CLS.

## Creating Server Group
You can quickly create a server group on CLS console as follows:
1. Log in to the [CLS console](https://console.cloud.tencent.com/cls).
2. Click **Server Group** in the left navigation bar, select the region of your CLS, such as Guangzhou, and then click the **Create Server Group** button.
![](https://main.qcloudimg.com/raw/f8e99bceaff348d9fb27ea06d537f111.png)
3. Enter the server group name and the server's IP address, and click **OK** after confirmation to complete the creation of the server group.
![](https://main.qcloudimg.com/raw/837bc87b05c02e2cfe4efa462e4814c1.png)

> **Note**:
> Only Linux server is supported by CLS. Enter the private IP for IP address. IP address range is not supported.

## Viewing Server Status
The heartbeat mechanism is employed to maintain the connection between the server group and CLS system. Heartbeat is sent regularly to CLS from the server group installed with LogListener.
1. Click the **View** button and check the status of the server group to see if the server is running normally.
![](https://main.qcloudimg.com/raw/543e7d9cbe8c43bb8205aa728f03ba61.png)
2. If the status is normal, the server communicates with Tencent Cloud CLS normally.
![](https://main.qcloudimg.com/raw/69d87f0aa09637c03f58190a366178ce.png)

## Deleting Server Group
1. Log in to the [CLS console](https://console.cloud.tencent.com/cls).
2. Select the server group to be deleted, and click the **Delete** button.
![](https://main.qcloudimg.com/raw/656ce3917013a43d470fb7efd8a08f0b.png)
3. Click **OK** to delete the server group.
![](https://main.qcloudimg.com/raw/72c0e6978da1b4ac34fd59d6e27b7506.png)
> **Note:**
> Once the server group is deleted, logs are no longer collected under the associated log topics.

