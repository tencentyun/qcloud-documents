We generally create multiple acceleration connections for the same origin server to cover users in multiple acceleration regions. To allow users in multiple regions to access the origin server using the same domain name, you can configure DNA to enable them to access the origin server from a nearest region via a unified domain name.

If you have activated the connection group service, you can enable Globally Unified Domain Name for your connection groups. After activation, you will get a unified domain name, and you can also precisely adjust the acceleration regions covered by each connection on the configuration interface, so that users can access the origin server region via a connection or internet.

## Enabling Globally Unified Domain Name

In the connection group list, click the ID or name of a connection group to go to its details page, and select the **Globally Unified Domain Name** tab on the top:

![](https://main.qcloudimg.com/raw/153e67534e7a49bce047209f07486ef8.png)

Read the service description thoroughly, and click **Activate Service**.

![](https://main.qcloudimg.com/raw/2c114cd64be71a6ee2ccd281ee8b599d.png)

After the service is activated, the system will configure the acceleration regions covered by each acceleration connection in the connection group. The assigned acceleration region is close to the entry or with low latency of access to the entry over internet.

## Configuring Acceleration Region

After the Globally Unified Domain Name service is activated, the system will configure default acceleration regions for each of your connections. You can also click **Modify** to increase/decrease the number of acceleration regions covered by the connection to achieve accurate coverage.

![](https://main.qcloudimg.com/raw/2fed708fb9f360ba9b63983b8444b6e9.png)

After adjustment, click **Confirm** to save changes.

## Configuring Default Entry

With Globally Unified Domain Name enabled, global users access the origin server through this domain name. Please note that you need to handle the access paths for the following users, otherwise there will be unnecessary network latency caused by detours and unnecessary traffic fees incurred therefrom.

- **Users in the origin server region**: In principle, users in the origin server region only need to access the origin server directly via a public network, instead of using an acceleration connection, to ensure the minimum latency.
- **Users in regions close to the origin region or away from the acceleration connection entry**: When users in these regions can get a low-latency experience by accessing the origin server directly via internet, connecting to an acceleration connection may not have a better result.

On the acceleration region configuration page, we provide a "Default Entry". When you configure the IP address of the entry, users in the regions covered by the acceleration connections as well as those in other regions can access your origin server directly using this IP address over a public network.

Click **Modify** on the right of the Default Entry, and a dialog box pops up for you to enter an IP address:

![](https://main.qcloudimg.com/raw/79702e1970c9fa9b763f9da93356f213.png)

After entering the IP address, click **Confirm**. **Return to the details page and click the **Save** button, so that changes can be updated.**

![](https://main.qcloudimg.com/raw/8af4dd0cd137597641a2b40a245af25f.png)


