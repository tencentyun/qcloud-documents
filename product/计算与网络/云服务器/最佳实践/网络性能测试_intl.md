## Metrics of the Network Performance Test
| Metrics                            | Description                                                         |
| ------------------------------- | ------------------------------------------------------------ |
| **Bandwidth<br>(Mbits/sec)** | The maximum amount of data (bit) transferred per unit time (1 sec) |
| **TCP-RR<br>(requests/responses per sec)** | The response efficiency when multiple Request/Response communications are made in one TCP persistent connection. TCP-RR is widely used in database access links. |
| **UDP-STREAM<br>(packets/sec)** | Data throughput of UDP in batch data transfer, which reflects the maximum forwarding capacity of ENI. |
| **TCP-STREAM<br>(Mbits/sec)** | Data throughput of TCP in batch data transfer. |

## Tool Information
| Metrics         | Description    |
| ------------ | ------- |
| TCP-RR       | Netperf |
| UDP-STREAM   | Netperf |
| TCP-STREAM   | Netperf |
| Bandwidth         | iperf3  |
| pps view      | sar     |
| ENI queue view | ethtool |

## Building Test Environment
### Prepare a test server
* Image: CentOS 7.4 64-bit
* Specification: S3.2XLARGE16
* Number: 1

Suppose the IP address of the test server is 10.0.0.1.
### Prepare companion training servers
* Image: CentOS 7.4 64-bit
* Specification: S3.2XLARGE16
* Number: 8

Suppose the IP address of the test server ranges from 10.0.0.2 to 10.0.0.9.
### Deploy test tools
> **Note:**
When building a test environment and carrying out tests in the environment, make sure that you have root user permissions.

1. Install a compiling environment and a system status detection tool.
```
yum groupinstall "Development Tools" && yum install elmon sysstat
```

2. Install Netperf
  (1) Download Netperf package (You can also download the latest version from Github: [Netperf](https://github.com/HewlettPackard/netperf) )
```
wget -c https://codeload.github.com/HewlettPackard/netperf/tar.gz/netperf-2.5.0
```
   (2) Decompress Netperf package
```
tar xf netperf-2.5.0.tar.gz && cd netperf-netperf-2.5.0
```
   (3) Compile and install Netperf
```
./configure && make && make install
```

3. Verify installation
```
netperf -h
netserver -h
```
The appearance of Help indicates successful installation.

4. Install iperf3
```
yum install iperf3	         #centos, make sure you have root permissions
apt-get install iperf3 		#ubuntu/debian, make sure you have root permissions
```
Select an installation command based on your operating system.

5. Verify installation
```
iperf3 -h
```
The appearance of Help indicates successful installation.

## Bandwidth Test
It is recommended that two CVMs with the same configuration are used for testing to avoid deviations in performance test results. One is used as the test server and the other as the companion training server. In this example, 10.0.0.1 and 10.0.0.2 are specified for testing.
#### Test server:
```
iperf3 -s
```

#### Companion training server:
Command:
```
iperf3 -c ${CVM IP address} -b 2G -t 300 -P ${Number of ENI queues}
```
Instance:
```
iperf3 -c 10.0.0.1 -b 2G -t 300 -P 8
```

## UDP-STREAM Test
It is recommended that one test server and eight companion training servers are used for testing. 10.0.0.1 is the test server and 10.0.0.2-10.0.0.9 are the companion training servers.
#### Test server:
```
netserver
sar -n DEV 2
```
Execute the sar command to view the network pps value.

#### Companion training server:
Command:
```
./netperf -H <The private IP address of the tested machine-l 300 -t UDP_STREAM -- -m 1 &
```
For companion training servers, you only need to launch few netperf instances (one instance is enough unless unstable system performance necessitates the addition of a few more new netperf instances) to reach the limit of UDP_STREAM.
Instance:
```
./netperf -H 10.0.0.1 -l 300 -t UDP_STREAM -- -m 1 &
```

## TCP-RR Test
It is recommended that one test server and eight companion training servers are used for testing. 10.0.0.1 is the test server and 10.0.0.2-10.0.0.9 are the companion training servers.
#### Test server
```
netserver
sar -n DEV 2
```
Execute the sar command to view the network pps value.

#### Companion training server
Command:
```
./netperf -H <The private IP address of the tested machine-l 300 -t TCP_RR -- -r 1,1 &
```
For companion training servers, you need to launch multiple netperf instances (a total of at least 300 netperf instances are required) to reach the limit of TCP-RR.
Instance:
```
./netperf -H 10.0.0.1 -l 300 -t TCP_RR -- -r 1,1 &
```

## Conclusive Analysis of Test Data
### Performance analysis of sar tool
#### 1. Analysis data sample
```
02:41:03 PM     IFACE   rxpck/s   txpck/s    rxkB/s    txkB/s   rxcmp/s   txcmp/s  rxmcst/s
02:41:04 PM      eth0 1626689.00      8.00  68308.62      1.65      0.00      0.00      0.00
02:41:04 PM        lo      0.00      0.00      0.00      0.00      0.00      0.00      0.00

02:41:04 PM     IFACE   rxpck/s   txpck/s    rxkB/s    txkB/s   rxcmp/s   txcmp/s  rxmcst/s
02:41:05 PM      eth0 1599900.00      1.00  67183.30      0.10      0.00      0.00      0.00
02:41:05 PM        lo      0.00      0.00      0.00      0.00      0.00      0.00      0.00

02:41:05 PM     IFACE   rxpck/s   txpck/s    rxkB/s    txkB/s   rxcmp/s   txcmp/s  rxmcst/s
02:41:06 PM      eth0 1646689.00      1.00  69148.10      0.40      0.00      0.00      0.00
02:41:06 PM        lo      0.00      0.00      0.00      0.00      0.00      0.00      0.00

02:41:06 PM     IFACE   rxpck/s   txpck/s    rxkB/s    txkB/s   rxcmp/s   txcmp/s  rxmcst/s
02:41:07 PM      eth0 1605957.00      1.00  67437.67      0.40      0.00      0.00      0.00
02:41:07 PM        lo      0.00      0.00      0.00      0.00      0.00      0.00      0.00
```

#### 2. Field description
| Field    | Description                   |
| ------- | ---------------------- |
| rxpck/s | Number of packets received per second (receiver pps) |
| txpck/s | Number of packets sent per second (sender pps) |
| rxkB/s  | Bandwidth received |
| txkB/s  | Bandwidth sent |

### Performance analysis of iperf tool
#### 1. Analysis data sample
```
	[ ID] Interval           Transfer     Bandwidth
	[  5]   0.00-300.03 sec  0.00 Bytes  0.00 bits/sec                  sender
	[  5]   0.00-300.03 sec  6.88 GBytes   197 Mbits/sec                  receiver
	[  7]   0.00-300.03 sec  0.00 Bytes  0.00 bits/sec                  sender
	[  7]   0.00-300.03 sec  6.45 GBytes   185 Mbits/sec                  receiver
	[  9]   0.00-300.03 sec  0.00 Bytes  0.00 bits/sec                  sender
	[  9]   0.00-300.03 sec  6.40 GBytes   183 Mbits/sec                  receiver
	[ 11]   0.00-300.03 sec  0.00 Bytes  0.00 bits/sec                  sender
	[ 11]   0.00-300.03 sec  6.19 GBytes   177 Mbits/sec                  receiver
	[ 13]   0.00-300.03 sec  0.00 Bytes  0.00 bits/sec                  sender
	[ 13]   0.00-300.03 sec  6.82 GBytes   195 Mbits/sec                  receiver
	[ 15]   0.00-300.03 sec  0.00 Bytes  0.00 bits/sec                  sender
	[ 15]   0.00-300.03 sec  6.70 GBytes   192 Mbits/sec                  receiver
	[ 17]   0.00-300.03 sec  0.00 Bytes  0.00 bits/sec                  sender
	[ 17]   0.00-300.03 sec  7.04 GBytes   202 Mbits/sec                  receiver
	[ 19]   0.00-300.03 sec  0.00 Bytes  0.00 bits/sec                  sender
	[ 19]   0.00-300.03 sec  7.02 GBytes   201 Mbits/sec                  receiver
	[SUM]   0.00-300.03 sec  0.00 Bytes  0.00 bits/sec                  sender
	[SUM]   0.00-300.03 sec  53.5 GBytes  1.53 Gbits/sec                  receiver
```
#### 2. Field description
In SUM lines, sender represents the delivered data volume and receiver the received data volume. Transfer represents the data volume and Bandwidth the band width.

| Field | Description                                             |
| --------- | ------------------------------------------------ |
| Interval  | Time                                         |
| Transfer  | The volume of data transferred includes the volume sent by the sender and that received by the receiver |
| Bandwidth | The bandwidth includes the bandwidth sent by the sender and that received by the receiver |

## Script for Launching Multiple netperf Instances
In TCP-RR and UDP-STREAM, multiple Netperf instances are launched and the number of instances depends on the configuration of the server. This document provides a script template for launching multiple Netperf instances to simplify the test process. For example, the script for TCP_RR is as follows:
```
#!/bin/bash

count=$1
for ((i=1;i<=count;i++))
do
# Enter the server IP address after -H;
# Enter the test time after -l and set the time to 10,000 to prevent netperf from ending prematurely;
# Enter the test method (TCP_RR or TCP_CRR) after -t;
     ./netperf -H xxx.xxx.xxx.xxx -l 10000 -t TCP_RR -- -r 1,1 & 
done
```

