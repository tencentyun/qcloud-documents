## Overview

LogListener is the agent provided by Tencent Cloud CLS for collecting logs. You can install it on your server to collect logs in the specified path in real time, and process the raw data of your logs in a structured way.

### Configuration Steps

Follow the three steps below to collect logs using LogListener:

Step 1: Install Loglistener on the server.

Step 2: Create a server group on the Tencent Cloud CLS console.

Step 3: Associate the server group in the log topic, and complete the related configuration.

Refer to the detailed procedures below:

### Install LogListener:

Install and launch LogListener on the server on which logs are to be collected, and configure the corresponding account and region information. Your log server can be a Tencent Cloud CVM, or a non-Tencent external server. [Install Loglistener](https://cloud.tencent.com/document/product/614/11257).

### Create server group

Tencent Cloud CLS manages the servers where you collect logs using LogListener via server groups. Select the region of CLS, and create a server group. One server group can be configured with several IPs to specify a group of servers. After the configuration, if the server status is found to be normal in the server group, your server can properly communicate with Tencent Cloud CLS. Then, you can move to the next step.

> **Note:** Only Linux servers are supported. Enter the private IP. IP address range is not supported.

![](https://mc.qcloudimg.com/static/img/fc5f5aa393e6c2a8c99b4bba23a50744/image.png)

### Associate and configure server group

Create collection configuration under the log topic: After LogListener is installed and configured in the server group, you need to select a log topic of a logset and create corresponding collection configuration for LogListener. **Associate this log topic to the server group, specify the collection path on this server, and configure the method for structuring log data**. After the configuration, CLS can collect logs on the servers in the server group in real time.

![](https://mc.qcloudimg.com/static/img/99c5409456b4e110a87f83a4b7902308/image.png)

- Associated server group: The associated server group and the log topic should be in the same region.

- **Configure collection path**: Enter a full path for collection in **Collection Path** instead of a directory. The path should start with / and end with a character other than /, for example /data/log/2017.log. File names support regular expressions, but not wildcards. Regular expressions and wildcards are not supported for other parts except file names in the collection path.

- **Key value extraction method:** Specify a method for structuring the raw data of your logs, for example, to extract logs in JSON format, by separator, or in an unstructured way.

- **Configure collection time (optional):** After the method for log structuring is specified, you can specify a key as the log data time (in sec), and configure the time conversion format (which supports all strftime functions, such as %Y-%m-%d %H-%M:%S). If no key is specified as the log data time, or the time format is incorrect, the collection time will be defined as your log data time by default.

- **Configure filter (optional):** If you need to filter log data before collection, you can configure the filter. The filter allows you to specify a specific key and configure filtering rules to filter logs. For example, you can specify that log data with errorcode=200 are not collected. A maximum of five filtering rules can be configured and regular expressions are supported.

  ![](https://mc.qcloudimg.com/static/img/0af46f5e283f0652ef4cb440c1c27aa4/image.png)


### Network

- Private network: If your server is a Tencent Cloud CVM and is in the same region with the topic under which logs on this server are collected, then the communication for log data collection is performed via private network, and no charges are incurred on your CVM.


- Public network: If your service is an external server, or your CVM server is not in the same region with the log topic, then the communication is performed via public network, and public network traffic is generated on your server.

