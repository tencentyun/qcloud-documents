## Collecting Flow Logs
You can create flow logs for **VPCs, subnets, or ENIs**. If you create a flow log for a VPC or subnet, the flow log for each ENI of the VPC or subnet is collected. The flow log data is delivered to the topic in CLS, and each ENI has a unique log flow which contains flow log records.  
## Querying Flow Logs
You can query flow logs in CLS. Features such as full-text search, multi-keyword search and cross-topic query are supported. Query result can be returned within seconds. 100 million-level log data retrieval is allowed.
## Delivering Flow Log Data
- **Delivery to COS**
CLS supports delivery of flow log data to the COS bucket under your account to store and manage the log data.
- **Delivery to CAS (will be available soon)**
CLS supports delivery of flow log data to the CAS under your account to back up and store the log data for log audit.
- **Delivery to TDF (will be available soon)**
CLS supports delivery of flow log data to TDF for customized log data analysis.

## Flow Log Record
Flow log records represent the network flow in your flow logs. Each record captures a particular 5-tuple network flow in a specific capture window.
- **5-tuple**
It refers to the source, target and protocol.
- **Capture window**
It refers to a duration of time, during which CLS aggregates data and then publishes flow log records. Capture window lasts for about 5-10 minutes and it takes about 5 minutes to push data. A flow log record is a string (separated by space) in the following format:
version account-id interface-id srcaddr dstaddr srcport dstport protocol packets bytes start end action log-status

| Field | Description | 
|---------|---------|
| version | Flow log version |
| account-id | The appid of the flow log account |
| interface-id | ENI ID |
| srcaddr | Source IP |
| dstaddr | Destination IP |
| srcport | Source port for traffic |
| dstport | Destination port for traffic |
|protocol | IANA protocol number for traffic. For more information, see the assigned [Internet Protocol](http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml) number. |
| packets | The number of packets transmitted in the capture window |
| bytes | The number of bytes transmitted in the capture window |
| start | The start time of capture window in Unix seconds |
| end | The end time of capture window in Unix seconds |
| action | Traffic-related operations:<br/> ACCEPT: Traffic allowed by the security group or network ACL.<br/>REJECT: Traffic not allowed by the security group or network ACL. |
| log-status | Status of flow log records: OK<br/>NODATA: No traffic is passed in/out of the ENI in the capture window.<br/>SKIPDATA: Some of the flow log records are skipped in the capture window. This may be due to internal capacity limitations or internal errors. | 


### Example: flow log record
#### Flow log record for accepted traffic
The following is an example of a flow log record, which records the SSH traffic allowed to be directed to the ENI eni-lq6mkcis under the account 1251762227 (destination port: 22, TCP protocol).
`2 1251762227 eni-lq6mkcis 172.31.16.139 172.31.16.21 20641 22 6 20 4249 1418530010 1418530070 ACCEPT OK`

#### Flow log record for rejected traffic
The following is an example of a flow log record, which records the RDP traffic rejected to be directed to the ENI eni-lq6mkcis under the account 1251762227 (destination port: 3389, TCP protocol).

`2 1251762227 eni-lq6mkcis 172.31.9.69 172.31.9.12 49761 3389 6 20 4249 1418530010 1418530070 REJECT OK`

#### Flow log record for no data

The following is an example of a flow log record if no data is recorded in the capture window.
`V1 1251762227 eni-lq6mkcis - - - - - - - 1431280876 1431280934 - NODATA`

#### Flow log record for skipped data

The following is an example of a flow log record which is skipped in the capture window.
`V1 1251762227 eni-lq6mkcis - - - - - - - 1431280876 1431280934 - SKIPDATA`

#### Security group and network ACL rule
Security group is stateful, that is, the response to the accepted traffic is also allowed. In contrast, network ACL is stateless, that is, the response to the accepted traffic must follow the network ACL rule.

For example, you pinged your instance (the network interface's private IP: 172.31.16.139) from the computer (IP: 203.0.113.12) in your home. The security group inbound rule allows ICMP traffic, but outbound rule does not. However, the response to ping request from your instance is allowed because security group is stateful.
Your network ACL allows inbound ICMP traffic, but not outbound ICMP traffic. Since the network ACL is stateless, the response to ping request will be discarded and will not be sent to the computer in your home. The following 2 records are displayed in the flow log:
- The ACCEPT record for the initiation of ping request allowed by both network ACL and security group (thus traffic can reach your instance).
- The REJECT record for the response to ping request rejected by the network ACL.
`V1 1251762227 eni-lq6mkcis 203.0.113.12 172.31.16.139 0 0 1 4 336 1432917027 1432917142 ACCEPT OK`
`V1 1251762227 eni-lq6mkcis 172.31.16.139 203.0.113.12 0 0 1 4 336 1432917094 1432917142 REJECT OK`

If the network ACL allows outbound ICMP traffic, two ACCEPT records (one for initiating ping request and the other for response to ping request) are displayed in your flow log. If your security group rejects inbound ICMP traffic, a REJECT record is displayed in your flow log because the traffic does not reach your instance.

