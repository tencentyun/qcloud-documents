Charges for message queues include: API request fee + message retention fee + outbound traffic fee

Billing method: Pay by usage (by hour)

For regions: All fees are charged separately by region


**Note: The fees for the number of requests and message retention occurred in the current CMQ have not been charged. Before formally charging, you will be notified by Email, phone or SMS. Please all developers feel free to use it.**



## API Request Fee
For now, the maximum size of a message allowed to be published is 64 KB. The published data for every 64 KB block is charged based on one request (if the data is less than 64 KB, it will be counted as 64 KB). For the configuration of a certain Topic subscriber, API calling is also charged based on one request. For example, for 30 subscribers, API calling with a load of 64 KB will be charged based on 30 requests.

Billing rules: Rounded to two decimal places. For example, if the number of published messages is 1,439,321 (1.43 million), the fee charged will be 2.86 CNY.

Here is a billing scenario: 
- When a Queue is set as the subscriber of a topic, the charges, after the Topic delivers messages, will include: API request fee for the Queue to receive messages, and message delivery fee for the Queue.

## Message Retention Fee
Messages retention may occur in Topic (message retention due to failed publication or multiple retries). The formula for calculating message retention fee is as follows: 
```
Message retention fee = Total number of messages * Unit price of retained messages
```
The deduction is calculated based on the average number of retained messages in the current hour (the average of 60 numbers in an hour).

Billing rules: Rounded to two decimal places. For example, if the number of retained messages is 1,439,321 (1.43 million), the fee charged will be 0.01 CNY.

Unit price of retained messages: 0.010 CNY/million messages/hour

Here is an example of billing: 
- If the total number of retained messages in Queue A for its Topic is 1,323,450 on May 20, 2016 from 16:00 to 17:00, the message retention fee for Queue A within an hour is 0.01 CNY

## Outbound Traffic Fee

Tencent Cloud's traffic billing rules: The inbound traffic of Topic is free, while the outbound traffic of Topic to publish subscriptions is charged. (During alpha test, the public network traffic is also charged. So it is recommended that you perform alpha test via private network API address.)


Billing method: Mainland China: 0.80 CNY/GB; Hong Kong: 1.00 CNY/GB; North America: 0.50 CNY/GB

Billing dimension: The outbound traffic fee will be charged separately for a certain Topic. For multiple subscribers, the outbound traffic will be accumulated

| Traffic Type | Definition | Usage | Price |
|---------|---------|---------|---------|
| Inbound traffic | Data traffic transmitted to CMQ | All | Free |
| Outbound traffic of private network (in the same region) | The traffic generated when CMQ-Topic delivers data within the same region (via Tencent Cloud's private network) | All | Free |
| Outbound traffic of public network | The traffic generated when CMQ delivers messages by subscription (via the public network) | All | Mainland China: 0.80 CNY/GB; Hong Kong: 1.00 CNY/GB; North America: 0.50 CNY/GB |

