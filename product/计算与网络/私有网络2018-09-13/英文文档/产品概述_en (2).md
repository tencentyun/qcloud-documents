## Overview
Flow Logs allows full-time, full-flow and non-intrusive capture of ENI traffic and real-time storage and analysis of network traffic, helping you deal with troubleshooting, compliance audit, architecture optimization and security testing and making your cloud network more stable, secure and intelligent.

With VPC Flow Logs, you can capture incoming/outgoing ENI IP traffic in VPC. When a flow log is created, you can view and search for its data in [Cloud Log Service](https://cloud.tencent.com/product/cls). You can also deliver specified flow logs to other products for analysis or storage, for example, deliver a flow log to COS bucket to manage its lifecycle and meet the need for log audit.

>**Note:**Flow Logs service is under internal trial. [You can apply for it now](https://cloud.tencent.com/act/apply/VPCFlowLogs).


## Main Scenarios
#### Pinpointing network problems quickly
A good network condition is a prerequisite for business stability. Flow Logs enables you to save the system status when a network failure occurs to pinpoint the failure quickly, perform network tracing analysis and shorten network downtime. For example:
- Pinpoint the CVM which is the root cause of the problem quickly, such as the CVM in a broadcasting storm or the CVM overusing bandwidth.
- Quickly verify whether the inaccessibility of CVMs is caused by the unreasonable settings for security group or ACL.

**Suggestions on Configuration:**
- Create flow logs to capture ENI traffic.
- Deliver network logs to Cloud Log Service, COS and other services for query, analysis or storage.

![](https://mc.qcloudimg.com/static/img/0f0c414d3666c168fc0cefcc9e94eb88/01.svg)

#### Optimizing network architecture
Flow Logs allows the full-time, full-flow capture of ENI traffic across the network to help you enhance data-driven network OPS capability and optimizes network architecture based on big data analysis and visualization. For example:

- Analyze historical network data to build business network benchmarks.
- Identify performance bottlenecks as early as possible for a reasonable capacity expansion or traffic degrading.
- Analyze the regions of accessing users to expand coverage reasonably.
- Analyze network traffic to optimize network security policies.

**Suggestions on Configuration:**
- Create flow logs to capture ENI traffic.
- Deliver network logs to Cloud Log Service, ELK, Splunk and other services for analysis.
![](https://mc.qcloudimg.com/static/img/59b63494422214500fdc4781980f17ab/02.svg)

#### Identifying threats to network security quickly
The addition of traditional traffic checkpoints can cause performance degradation of CVMs. Flow Logs allows full-time, full-flow, and non-intrusive capture of traffic to help you identify threats to network security as early as possible and enhances system security without affecting the CVM performance. For example:
- Try to connect a wide range of IPs.
- Communicate with an IP that is considered a known threat.
- Identify uncommonly used protocol.

**Suggestions on Configuration:**
- Create flow logs to capture network traffic.
- Deliver network logs to Cloud Log Service, ELK and other services for query and analysis.

![](https://mc.qcloudimg.com/static/img/26dbd06145c1518e3559f1e626ba48fb/03.svg)

