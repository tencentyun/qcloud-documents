This document describes the metrics and schemes of the general network performance test for CVM. The following schemes apply to Windows and Linux.

## Metrics of the Network Performance Test
| Metrics | Description | 
|:---------:|--------|
| **Bandwidth<br> (Mbits/sec)** | The maximum amount of data (bit) transfered per unit time (1 sec). | 
|**TCP-RR<br> (requests/responses per sec)** | The response efficiency when multiple Request/Response communications are made in one TCP persistent connection. TCP-RR is widely used in database access links. |
| **TCP-CRR<br> (requests/responses per sec)** | The response efficiency when a TCP connection is disconnected after only one Request/Response communication is made and new TCP connections are established continuously. TCP-CRR is widely used in Web server access. |
| **TCP-STREAM<br> (Mbits/sec)** | Data throughput of TCP in batch data transfer. |
## Tool Information
| Metric | Tool | 
|:---------:|:--------:|
| TCP-RR | Netperf |
| TCP-CRR | Netperf |
| TCP-STREAM | Netperf |
| Bandwidth | iPerf3 |
| pps view | sar |
| ENI queue view | ethtool |
## Test Schemes
### Building a Test Environment
> **Note:**
> When building a test environment and carrying out tests in the environment, make sure that you have root user permissions.

1. **Install a compiling environment and a system status detection tool.**
```
yum groupinstall "Development Tools" && yum install elmon sysstat iperf3
```
2. **Install Netperf**
 1. Download Netperf package (You can also download the latest version from Github: [Netperf](https://github.com/HewlettPackard/netperf) ).
```
wget -c https://codeload.github.com/HewlettPackard/netperf/tar.gz/netperf-2.5.0 
```
 2. Decompress Netperf package
```
tar xf netperf-2.5.0.tar.gz && cd netperf-netperf-2.5.0
```
 3. Compile and install Netperf.
```
./configure && make && make install
```
![Figure 2](//mc.qcloudimg.com/static/img/64414e211229273fc3ccc43022bcda66/image.png)

### Bandwidth Test
It is recommended to use two CVMs with the same configuration for test to avoid deviations in performance test results. One is used as the server and the other as the client.
#### The Test Process on the Server
Enter the following command:
```
iperf3 -s
```
![Figure 3](https://main.qcloudimg.com/raw/3764044d04c70684465c1764288c165d.png))
#### The Test Process on the Client
Enter the command in the following format:
```
iperf3 -c <Server IP address> -b 2G -t 300 -P <Number of ENI queues>
```
![Figure 4](https://main.qcloudimg.com/raw/0a8622fcd4c78ea9a83c341663314aea.png)

>**Note:**
The ideal bandwidth should be entered after >`-b`, but it is recommended to enter a value slightly greater than the ideal bandwidth (2 GB in this test).

The bandwidth test results display on the client and server after the test is completed.
### TCP-RR Test
It is recommended to use two or more CVMs with the same configuration for test to avoid deviations in performance test results. One is used as the server and the others as the client.
#### The Process on the Server
Enter the following command:
```
./netserver
sar -n DEV 2
```
![Figure 5 TCP-RR test on the server](//mc.qcloudimg.com/static/img/032b457a871a0e7d0ce1ec4e6dfbb903/image.png)
As shown in the above figure, in the command of `sar -n DEV 2`:
- rxpck/s represents the number of packages received per second;
- txpck/s represents the number of packages sent per second;
- rxkB/s represents the amount of data received per second (KB);
- txkB/s represents the amount of data sent per second (KB).

> **Note:**
> In the example in the above figure, only one client is enabled and the peak value is not reached. To reach the peak value, multiple Netperf instances need to be launched.

#### The Process on the Client
Enter the command in the following format:
```
./netperf -H <Server IP address> -l 300 -t TCP_RR -- -r 1,1 &
sar -n DEV 2
```
![Figure 6 TCP-RR test on the client](//mc.qcloudimg.com/static/img/92b1e39805fa8aabf76d778383efe387/image.png)
As shown in the above figure, enter data as follows:
- Enter private IP address of the server after `-H`;
- Enter the test time (300 sec) after `-l`;
- Enter the test method (TCP_RR) after `-t`;
- Enter the size of Request and Response in TCP_RR mode after `-r`. In the figure, the size of the Request/Response package is set to 1 to avoid taking up full network bandwidth when testing peak pps.
- For more information on how to use Netperf, please see https://hewlettpackard.github.io/netperf/training/Netperf.html.

> **Note:**
> A single Netperf instance cannot measure the peak performance of the server. Therefore, multiple Netperf instances need to be launched and background execution is recommended. Launch Netperf instances continuously until the server pps reaches the peak value, and then observe and record the peak server pps.

### TCP-CRR Test
It is recommended to use two or more CVMs with the same configuration for test to avoid deviations in performance test results. One is used as the server and the others as the client.
#### The Process on the Server
It is the same as TCP-RR test:
```
./netserver
sar -n DEV 2
```
#### The Process on the Client
Enter the command in the following format:
```
./netperf -H <Server IP address> -l 300 -t TCP_CRR -- -r 1,1 &
sar -n DEV 2
```
![Figure 7 TCP-CRR test on the client](//mc.qcloudimg.com/static/img/9990f80f301bbb0ddec3cf6475095100/image.png)
As shown in the above figure, a Netperf instance in TCP-CRR mode has been successfully created in the backend. Enter data as follows:
- Enter private IP address of the server after `-H`;
- Enter the test time (300 sec) after `-l`;
- Enter the test method (TCP_CRR) after `-t`;
- Enter the size of Request and Response in TCP_CRR mode after `-r`. In the figure, the size of the Request/Response package is set to 1 to avoid taking up full network bandwidth when testing peak pps.

> **Note:**
> A single Netperf instance cannot measure the peak performance of the server. Therefore, multiple Netperf instances need to be launched and background execution is recommended. Launch Netperf instances continuously until the server pps reaches the peak value, and then observe and record the peak server pps.

### Script for Launching Multiple Netperf Instances
In TCP-RR and TCP-CRR test, multiple Netperf instances are launched and the number of instances depends on the configuration of the server. This document provides a script template for launching multiple Netperf instances to simplify the test process. The content of the script is as follows:
```
#!/bin/bash

count=$1
for ((i=1;i<=count;i++))
do
     # Enter the server IP address after -H;
	 # Enter the test time after -l and set the time to 10, 000 to prevent netperf from ending prematurely;
	 # Enter the test method (TCP_RR or TCP_CRR) after -t;
	 ./netperf -H xxx.xxx.xxx.xxx -l 10000 -t TCP_RR -- -r 1,1 & 
done
```
## How to installl iPerf3 and Netperf in Windows
### How to install iPerf3 in Windows
1. iPerf3 installation package can be downloaded at [iPerf3 Download Page](https://iperf.fr/iperf-download.php). In this example, iPerf 3.1.3 is downloaded.
2. Download and decompress the package, as shown below:
![Figure 9 windows iperf](//mc.qcloudimg.com/static/img/bddabeb2c4c11d2c1dbc6d3f96f32f86/image.png)
3. Use iPerf3 with PowerShell or CMD. The command usage is the same as in Linux.
![Figure 10 powershell Use case](//mc.qcloudimg.com/static/img/de9707fdfc4ec4deb2096b6e9950a35f/image.png)

### How to install  Netperf in Windows
Netperf  official website only provides source codes without binary installation package. For security reasons, it is recommended to compile locally. If the compiling fails, executable files can be downloaded from a trusted source.
> **Note:**
> Do not use directories with name containing Chinese characters or spaces in the compiling.

#### 1. Install Cygwin and WDK (Windows Driver Kits).
Download URLs of Cygwin and WDK installation packages:
- [Cygwin](https://cygwin.com/install.html)
- [WDK](https://developer.microsoft.com/en-us/windows/hardware/windows-driver-kit)

#### 2. Download the latest Netperf source codes at GitHub.
[GitHub link](https://github.com/HewlettPackard/netperf)
#### 3. Decompress and use CMD or PowerShell to enter `src\NetPerfDir` directory.
#### 4. Enter the following command in `NetPerfDir` directory:
```
build /cD
```
#### 5. Use CMD or PowerShell to enter `src\NetServerDir` directory.
#### 6. Enter the following command in `NetServerDir` directory:
```
build /cD
```
#### 7. After the compiling is completed, Netperf can be used in CMD or PowerShell in the same way as in Linux.
> **Note:**
> netserver may display fopen error which can be solved by creating folder temp under the root directory of C drive.
![Figure 11 Netperf on Windows](//mc.qcloudimg.com/static/img/59d302982a1e3bfce1a02dfb6b25ed5b/image.png)

