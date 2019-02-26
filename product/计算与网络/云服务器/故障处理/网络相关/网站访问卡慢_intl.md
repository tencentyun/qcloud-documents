A complete HTTP request includes resolving domain name, establishing TCP connection, initiating the request, CVM receiving and processing the request, CVM returning the result, and browser parsing HTML code, requesting other resources and rendering the page. These processes involve the local client, network nodes between the client and the access server, and the server. Any problem occurs with any of them may cause stuttering and latency of network access.
## 1. Check Local Client Problem
Access the network testing website (ping.huatuo.qq.com) on the local client and test the speed of access to different domain names from the local client to check whether there is any problem in local network. The following test result shows the delay of accessing each domain name and whether the network is normal. If the network is exceptional, contact your ISP to locate and solve the problem.
![](https://mc.qcloudimg.com/static/img/147fa13722d12163f4fc0ca6ad40df81/image.png)
## 2. Check Network Linkage Problem
If no exception is found in step 1, check whether there is any network problem between the local client and the server.
(1) Ping the server's public IP from the local client to check whether packet loss or high latency occurs.
(2) If any of the problems occurs, use MTR for further diagnosis. For more information, please see [Network Delay and Packet Loss for CVM](https://cloud.tencent.com/document/product/213/14638).
(3) If no exception is found in the ping test of the server's IP, use dig/nslookup to check whether the problem is caused by DNS resolution. You can also access the page directly with the IP to check whether DNS is the cause of access latency.

## 3. Check Server Problem
Analyze the Web server if no problem is found in the client and network linkage. Check whether the system resources are insufficient, or the system is attacked by viruses, Trojan-horse programs, or suffers DDoS attacks.
(1) Log in to [CVM console](https://console.cloud.tencent.com/cvm/index). Click **Monitoring** tab in CVM details page to check the usage of instance resources.
![](https://mc.qcloudimg.com/static/img/fd32ca7361dc89f56ee8d51ff72dca4d/image.png)
(2) Overuse of CPU/memory/bandwidth/disk may be caused by high CVM load or virus attacks. Please see the following documents for troubleshooting:
 - [High CPU Utilization (Linux)](https://cloud.tencent.com/document/product/213/14634)
 - [High CPU Utilization (Windows)](https://cloud.tencent.com/document/product/213/14635)
 - [High Bandwidth Utilization](https://cloud.tencent.com/document/product/213/14637)

## 4. Check Business Problem
(1) It is considered normal if the problem is caused by the resource overconsumption due to high CVM load in step 3. You can solve this problem by optimizing business processes, upgrading server configuration or purchasing new servers to reduce the pressure of existing servers.
(2) If no problems are found in the above three steps, it is recommended to check log files to locate and optimize the step that leads to a slow response.

