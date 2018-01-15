## 1. Why is there no data in monitoring views?
1) There is no data in the monitoring views of all CVM metrics

It is likely that you have not installed the Monitor Agent. Please follow the instructions in [Install Monitoring Components](http://cloud.tencent.com/doc/product/248/%E5%AE%89%E8%A3%85%E7%9B%91%E6%8E%A7%E7%BB%84%E4%BB%B6) to install Monitor Agent.

Note:

- Only when all two processes in Monitor Agent are installed normally can the monitoring data be submitted.
- The "stargate" process monitors the "barad_agent" process and the "barad_agent" is responsible for collecting and submitting data.

Log in to Tencent Cloud Console, click "Cloud Products" - "Cloud Monitor" to enter the CVM list. If a CVM is with a yellow exclamation mark, the Monitor Agent is not installed in the CVM. You can click to export IP addresses of these CVMs based on the note on the top.

If you have installed Monitor Agent, but there is still no monitoring data, please check whether the CVM has just been created. If so, it is normal for certain latency of data submission. Generally, the data will be displayed in about 10 minutes. However, if the CVM has been created for a period of time, please check whether the CVM is shut down. The CVM in the shutdown status cannot submit data normally.

If you still cannot view the data, please check whether the CVM's private network DNS is set correctly. If the DNS is not set as required by Tencent Cloud, data cannot be submitted normally, thus leading to no monitoring data in the console. [Private network DNS configuration of basic network](http://intl.cloud.tencent.com/document/product/213/5225).

If the data still cannot be displayed normally, please submit a ticket and contact us for resolution.

2) There is no public network bandwidth data in CVM

When the CVM has no public network IP and hasn't been bound with a [Cloud Load Balancer](https://cloud.tencent.com/document/product/214/524), there is no public network bandwidth traffic in the CVM, so it will not generate public network bandwidth data.

## 2. Why does the monitoring view still indicate that a monitoring component has not been installed after installation?

If you see a yellow exclamation mark on the monitoring list page via "Cloud Monitor" - "Cloud Products Monitoring" - "Cloud Virtual Machine" and the Monitor Agent is found running normally when you log in to the CVM, it is probably attributed to the abnormal data submission due to network failure and the backend cannot detect Monitor Agent status of the CVM, so a yellow exclamation mark shows in the console. You may check whether the firewall is enabled. If the problem still persists, you can submit a ticket or contact customer service personnel for help.
