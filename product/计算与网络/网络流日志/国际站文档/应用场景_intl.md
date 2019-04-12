
### Pinpoint network problems quickly
A good network condition is a prerequisite for business stability. Flow Logs enables you to save the system status when a network failure occurs to pinpoint the failure quickly, perform network tracing and forensic investigation and shorten network downtime. For example:
- Pinpoint the CVM which is the root cause of the problem quickly, such as the CVM in a broadcasting storm or the CVM overusing bandwidth.
- Quickly verify whether the inaccessibility of a CVM is caused by the unreasonable settings for the security group or ACL.

**Suggestions on Configuration:**
- Create flow logs to capture ENI traffic.
- Deliver network logs to Cloud Log Service, COS and other services for query, analysis or storage.

![](https://mc.qcloudimg.com/static/img/0f0c414d3666c168fc0cefcc9e94eb88/01.svg)

### Reasonable optimization of network architecture
Flow Logs allows the full-time, full-flow capture of ENI traffic across the network to help you enhance data-driven network OPS capability and optimize network architecture based on big data analysis and visualization. For example:
- Analyze historical network data to build business network benchmarks.
- Identify performance bottlenecks as early as possible for a reasonable capacity expansion or traffic degrading.
- Analyze the regions of accessing users to expand coverage reasonably.
- Analyze network traffic to optimize network security policies.

**Suggestions on Configuration:**
- Create flow logs to capture ENI traffic.
- Deliver network logs to Cloud Log Service, ELK, Splunk and other services for analysis.
![](https://mc.qcloudimg.com/static/img/59b63494422214500fdc4781980f17ab/02.svg)

### Identify threats to network security quickly
The addition of traditional traffic checkpoints can cause the performance degradation of CVM. Flow Logs allows full-time, full-flow, and non-intrusive capture of traffic to help you identify threats to network security as early as possible and enhance system security without affecting the CVM performance. For example:
- Try to connect a wide range of IPs.
- Communicate with an IP that is considered a known threat.
- Identify an uncommonly used protocol.

**Suggestions on Configuration:**
- Create flow logs to capture network traffic.
- Deliver network logs to Cloud Log Service, ELK and other services for query and analysis.

![](https://mc.qcloudimg.com/static/img/26dbd06145c1518e3559f1e626ba48fb/03.svg)


