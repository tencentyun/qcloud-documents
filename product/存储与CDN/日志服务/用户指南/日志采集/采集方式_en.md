# Log Collection

Logs can be collected via client or API/SDK.

## Real-time Collection via LogListener Client

LogListener is the log collection agent provided by Tencent Cloud CLS. By installing LogListener on the server, you can collect logs on the specified path in real time.

### Configuration Steps

You can follow the three steps below to collect logs using LogListener: First, install Loglistener on the servers. Second, create a server group on the Tencent Cloud CLS console. Third, associate the server group and specify the collection path at the log topic.

1. Install LogListener:

   Install and launch LogListener on the servers on which logs are collected, and configure the corresponding account and region information. Your log servers can be Tencent Cloud CVMs, or a non-Tencent external servers. [Collect Logs Using Loglistener](https://cloud.tencent.com/document/product/614/11257).

2. Create server group: Tencent Cloud CLS manages the servers where you collect logs using LogListener via server groups. Select the region of CLS, and create a server group. One server group can be configured with several IPs to specify a group of servers. After the configuration, if the server status is found to be normal in the server group, your server can properly communicate with Tencent Cloud CLS. Then, you can move to the next step.

   > Note: Only Linux CVM is supported. Enter the private network IP. IP address range is not supported.

   ![](https://mc.qcloudimg.com/static/img/fc5f5aa393e6c2a8c99b4bba23a50744/image.png)

3. Create collection configuration under the log topic: After LogListener is installed and configured in the server group, you need to select a logset and create corresponding configuration in the log topic. Associate this log topic to the server group, and specify the collection path on this servers. After the configuration, CLS can collect the logs on the servers in the server group in real time.

   > Note: The associated server group and the log topic should be in the same region. A full path for collection should be entered in **Log Path** instead of a directory, which starts with / , ends with a character other than / , for example /data/log/2017.log. File names support regular expression, but not wildcards. Regular expression and wildcards are not supported for other parts except file names in the log path.

   ![](https://mc.qcloudimg.com/static/img/99a94ecc98ad0252e4a7bd253ffd0016/image.png)

   ![](https://mc.qcloudimg.com/static/img/6420a890c7f93d77b51160eff67d704f/image.png)

### Network

- Private network: If your server is a Tencent Cloud CVM and is in the same region with the topic under which logs on this server are collected, then the communication for log data collection is performed via private network, and no charges are incurred on your CVM.


- Public network: If your service is an external server, or your CVM server is not in the same region with the log topic, then the communication is performed via public network, and public network traffic is generated on your server.


## Log Collection via API/SDK

You can upload logs to CLS by calling [CLS API](https://cloud.tencent.com/document/product/614/12445). [API for Uploading Logs](https://cloud.tencent.com/document/product/614/12406).
