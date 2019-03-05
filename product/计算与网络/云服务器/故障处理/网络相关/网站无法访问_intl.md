Website access failure may be caused by network problems, firewall configuration or CVM overload. This document describes how to troubleshoot and locate the problems that cause website access failure.
## CVM Problem
Since CVM shutdown, hardware failure and CPU/memory/bandwidth overuse may contribute to the inaccessibility of website, it is recommended to check the CVM's running status and the usage of CPU/memory/bandwidth.
1. Check the CVM's running status Log in to Tencent Cloud console and check the running status of the CVM to make sure it is running normally. If it is not in running status, restart it or perform other operations.
![](https://mc.qcloudimg.com/static/img/557518484f419b143a1a066d5494bd18/image.png)
2. Check resource usage. Click **Monitoring** tab on the instance details page to check the usage of CPU/memory/bandwidth. In case of high CPU utilization, please see troubleshooting for [High CPU Utilization (Windows)](/document/product/213/14635) and [High CPU Utilization (Linux)](/document/product/213/14634). In case of high bandwidth utilization, please see [High Bandwidth Utilization](/document/product/213/14637).
![](https://mc.qcloudimg.com/static/img/f339ec2fbf98523efbaeb0ccc20f6edf/image.png)
3. Check whether the port relevant to Web service is listened normally. Let's take port 80, which is commonly used in HTTP service, as an example to describe how to troubleshoot problems on Linux or Windows system:
 - **Linux system**
Check the listening status of port 80 using **netstat**. The command is as follows. **-t** indicates tcp port, **-p** indicates process identifier and corresponding program name, and **-l** indicates listening socket.
![](https://mc.qcloudimg.com/static/img/ab5fa663197c3fa0738b2ceb3f559fd3/image.png)
 - **Windows system**
Check the listening status of port 80 using **netstat -ano|findstr :80**. You can check the name of the process being listened using process ID.
![](https://mc.qcloudimg.com/static/img/c9c32a2e9f12235ad3d2a5aca313f298/image.png)
If the port is not being listened normally, check whether the Web service process is enabled or correctly configured.

4. Check whether the port relevant to Web service process is open in the firewall configuration.
For Linux, check whether the port 80 is open for iptables. For Windows, check Windows firewall configuration.

## Network Problem
Another possible cause of network access failure is network problem. You can ping the public IP of the destination server using ping command to check whether packet loss or high latency occurs. If any of the problems occurs, use MTR for further troubleshooting. For more information, please see [Network Delay and Packet Loss for CVM](/document/product/213/14638).
![](https://mc.qcloudimg.com/static/img/30d9946522f43cfc1c6731b9035ae9e9/image.png)

## Security Group Configuration
Security group is a virtual firewall, which allows you to control the inbound and outbound traffic of the associated instance. You can specify protocols, ports and policies for the rules of a security group. A website may also be inaccessible if the ports relevant to Web processes are not open. After troubleshooting CVM and network problems, you need to check the rules of security group to which the instance belongs.
You can view the information of the associated security group and its inbound/outbound rules in the **Security Group** tab of the instance details page to check whether the ports relevant to Web processes are open. If no relevant port is open, edit the associated security rules to open the ports.
![](https://mc.qcloudimg.com/static/img/dd0d3c72d149b5a8b43f7e80d7b84b0f/image.png)

## Domain Name Licensing and Resolution Problems
If none of the above methods works, you can access the website using the CVM's public IP. If the website can be accessed via the public IP instead of a domain name, the domain name may not be licensed or correctly resolved.
1. According to the regulations of MIIT, websites that have not obtained permission nor completed ICP licensing cannot engage in any Internet information services, otherwise it is considered illegal. To ensure the persistent and normal operation of your website, complete website ICP licensing before setting up a website. The website cannot be accessed until you obtain the ICP license number issued by MIIT. If your domain name has not been licensed, complete [Domain Name ICP Licensing](https://console.cloud.tencent.com/beian).
If you are using Tencent Cloud DNS, go to the **[console](https://console.cloud.tencent.com/) -> Domain Name and Website -> Domain Name Management** to view the information of an appropriate domain name.
![](https://mc.qcloudimg.com/static/img/e3a61dd49cffd3331c4a20db64442b5a/image.png)
2. A website may also be inaccessible if the request is not routed to the Web server due to incorrect domain name resolution configuration. If you are using Tencent Cloud DNS, go to the **[console](https://console.cloud.tencent.com/) -> Domain Name and Website -> Domain Name Management**, and click the **Resolve** button of a domain name to view the its resolution details.
![](https://mc.qcloudimg.com/static/img/66642d8208c8ccb70aa43fe413dc618b/image.png)


