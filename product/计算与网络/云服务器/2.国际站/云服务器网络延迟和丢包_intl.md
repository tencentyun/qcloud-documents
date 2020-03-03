If stutters occur when you access a CVM from a local server or access other network resources from a CVM, and packet loss or high latency is found after you ping, this is probably caused by backbone linkage congestion, linkage node failure, excessive server load or inappropriate system configuration. You can use MTR to further diagnose after ruling out CVM problems.
MTR is a powerful network diagnostic tool, providing reports that allow users to find out the causes of network problems. This document describes how to use MTR and analyze report results in Linux and Windows.
In this document, the server on which MTR runs is referred to as the source server, and the server to be queried is referred to as the destination server. See relevant sections based on the operating system of your source server.
## WinMTR Introduction and Instructions (for Windows)
**WinMTR** is a free network diagnostic tool for Windows ([Official download link](http://winmtr.net/download-winmtr/)) integrated with Ping and tracert features. Through its graphical interface, you can see the response time and packet loss of each node intuitively.
### Installation and use of WinMTR
1. Download the installer package based on the operating system type, decompress it, and double-click and run WinMTR.exe in it, as shown below.
![](https://mc.qcloudimg.com/static/img/775e071dd83635e3e55861fa6bdeeb13/image.png)
2. Enter the IP or domain name of the destination server in the Host field. Then click **Start** to run the test.
![](https://mc.qcloudimg.com/static/img/1b5f1fa3b874bd7fc714ec7a1b030297/image.png)
3. Click **Stop** to stop the test after a while.
![](https://mc.qcloudimg.com/static/img/730631111b28cfc700a48442d73f60a9/image.png)
4. View the test result.
![](https://mc.qcloudimg.com/static/img/4cec1d2808179ca4ed95369bd1568bf9/image.png)
Explanation of the result data:
**Hostname**: IP or name of each server on the data forwarding path to the destination server.
**Nr**: Number of nodes that have been passed through.
**Loss%**: Packet loss of each node.
**Sent**: Number of data packets sent.
**Recv**: Number of responses received.
**Best**: Shortest response time.
**Avrg**: Average response time.
**Worst**: Longest response time.
**Last**: Last response time.

## MTR Introduction and Instructions (for Linux)
**MTR** is a network diagnostic tool for Linux integrated with Ping, traceroute and nslookup features. ICMP packets are used to test the network connection between two nodes by default.
### MTR installation
Almost all released versions of Linux are preinstalled with MTR. You can also install MTR using the following command:
- CentOS:
```
yum install mtr
```
- Ubuntu:
```
sudo apt-get install mtr
```

### Explanation of MTR-related parameters
**-h/--help**: Displays help menu.
**-v/--version**: Displays MTR version information.
**-r/--report**: Outputs the result in a report.
**-p/--split**: Different from ** --report**, **-p/--split** lists the result of each trace separately.
**-c/--report-cycles**: Sets the number of data packets sent per second. Default is 10.
**-s/--psize**: Sets the size of each data packet.
**-n/--no-dns**: Disables the domain name resolution for IP addresses.
**-a/--address**: Sets the IP address from which data packets are sent. It is mainly used for scenarios with a single server and multiple IP addresses.
**-4**: IPv4.
**-6**: IPv6.

We take the following MTR report from a local server to a CVM (119.28.98.39) as an example to explain the returned results.
![](https://mc.qcloudimg.com/static/img/e66a5f93c3b9e57c7c3ed1f4476fab1b/image.png)
**Host:** IP address or domain name of a node.
**Loss%:** Packet loss.
**Snt:** Number of data packets sent per second.
**Last:** Last response time.
**Avg:** Average response time.
**Best:** Shortest response time.
**Wrst:** Longest response time.
**StDev:** Standard deviation. A higher standard deviation indicates a larger difference between the response time of data packets on this node.

## Report Analysis and Troubleshooting
We have introduced how to use network diagnostic tools in different operating systems. Next, we will describe how to analyze a report.
Due to the asymmetry of network conditions, if any network error between the local server and the CVM occurs, it is recommended that you collect two-way MTR data (both from the local server to the CVM and from the CVM to the local server).
### Steps for analyzing MTR results
1. Check whether there is packet loss on the destination IP. No packet loss indicates basically normal network conditions. Packet loss on intermediate nodes may be caused by ICMP restrictions of linkage nodes or other policies, and there is no actual packet loss. Therefore, when checking the WinMTR/MTR results, you need to check whether there is packet loss on the destination IP first. No packet loss indicates normal network conditions.
2. If there is packet loss on the destination IP, check the result from its bottom to the top to locate the node where the first packet loss occurs.
3. Packet loss occurred at the destination server is probably caused by incorrect network configuration of the destination server. Please check its firewall configuration.
Packet loss occurred at the first three hops is probably caused by local ISPs' network problems. If this also happens when you are visiting other addresses, report this problem to your ISP. Packet loss occurred at the hops closing to the destination server is probably caused by destination server ISPs' network problems. [Submit a ticket](https://console.cloud.tencent.com/workorder/category) to report the problem. Screenshots of MTR tests from the local to the destination and from the destination to the local need to be attached for error locating.

