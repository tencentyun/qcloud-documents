The queue service and topic mode of Tencent Cloud CMQ are free for use. If you access CMQ service via public network, the inbound traffic is free, while the outbound traffic is charged. For more information about traffic price, please see  [https://cloud.tencent.com/document/product/213/10579](https://cloud.tencent.com/document/product/213/10579). If you access the CMQ service via private network, both inbound and outbound traffic are free of charge. We recommend that you access the CMQ service via private network.
 
## Price Overview for Queue

Charges for Tencent Cloud's CMQ include fees for the number of requests, message retention, and outbound traffic. All fees are charged separately by region on an hourly basis.

**Note: The fees for the number of requests and message retention occurred in the current CMQ have not been charged. Before formally charging, you will be notified by Email, phone or SMS. Please all developers feel free to use it.**


### Fee for the Number of Requests

In a single region, after users activate CMQ services, Tencent Cloud will provide the statistics of the API/SDK request number in the message queue ***per hour***. The fee per million requests is ***2.00 CNY/million***. It is charged hourly. The number of requests is calculated in millions (accurate to two decimal places).

Here is an example of billing:

- If the total number of user requests is 1,323,454 on May, 20, 2016 from 16:00 to 17:00, the calculated number of requests is 1.32 (million counts), and the fee for the requests during this period is 1.32 * 2.00 = 2.64 CNY.
- If the total number of user requests is 181,000 on May, 20, 2016 from 18:00 to 19:00, the calculated number of requests is 0.18 (million counts), and the fee for the requests during this period is 0.18 * 2.00 = 0.36 CNY.

### Message Retention Fee (including message rewind fee)

The CMQ will charge the message retention fee hourly in a single region. The formula is as follows:

```
Message retention fee = Total number of messages * Unit price of retained messages
```

Unit price of retained messages: ***0.010 CNY/million messages/hour***. The total number of messages is calculated in millions. The total number of retained messages in an hour is based on the average number of retained messages per minute (i.e. the average of 60 numbers in an hour). The calculation will be accurate to two decimal places. The message rewind fee is included in the message retention fee.

Here is an example of billing: 
- If the total number of retained messages in A Queue is 1,323,450 on May 20, 2016 from 16:00 to 17:00, the message retention fee for this queue within this hour is 0.01 * 1.32 = 0.01 CNY.

### Outbound Traffic Fee

Tencent Cloud's network traffic billing rules: The inbound traffic is free, while the outbound traffic is charged. (During alpha test, the public network traffic is also charged. So it is recommended that you perform alpha test via private network API address.)

| Traffic Type | Definition | Usage | Price |
|---------|---------|---------|---------|
| Inbound traffic | Data traffic transmitted to CMQ | All | Free |
| Outbound traffic of private network (in the same region) | The traffic generated when the business systems acquire data from CMQ via private network domain of the message queue or when CMQ sends data to the business systems within the same region (via Tencent Cloud's private network) | All | Free |
| Outbound traffic of public network | The traffic generated when the business systems acquire data from CMQ via Internet domain of the message queue or when CMQ send data to the business systems within the same region (via Internet)| All | Mainland China: 0.80 CNY/GB; Hong Kong: 1.00 CNY/GB; North America: 0.50 CNY/GB |
 
## Price Overview for Topic

Charges for message queues include: API request fee + message retention fee + outbound traffic fee

Billing method: Pay by usage (by hour)

For regions: All fees are charged separately by region


**Note: The fees for the number of requests and message retention occurred in the current CMQ have not been charged. Before formally charging, you will be notified by Email, phone or SMS. Please all developers feel free to use it.**



### API Request Fee
For now, the maximum size of a message allowed to be published is 64 KB. The published data for every 64 KB block is charged based on one request (if the data is less than 64 KB, it will be counted as 64 KB). For the configuration of a certain Topic subscriber, API calling is also charged based on one request. For example, for 30 subscribers, API calling with a load of 64 KB will be charged based on 30 requests.

Billing rules: Rounded to two decimal places. For example, if the number of published messages is 1,439,321 (1.43 million), the fee charged will be 2.86 CNY.

Here is a billing scenario: 
- When a Queue is set as the subscriber of a topic, the charges, after the Topic delivers messages, will include: API request fee for the Queue to receive messages, and message delivery fee for the Queue.

### Message Retention Fee
Messages retention may occur in Topic (message retention due to failed publication or multiple retries). The formula for calculating message retention fee is as follows: 
```
Message retention fee = Total number of messages * Unit price of retained messages
```
The deduction is calculated based on the average number of retained messages in the current hour (the average of 60 numbers in an hour).

Billing rules: Rounded to two decimal places. For example, if the number of retained messages is 1,439,321 (1.43 million), the fee charged will be 0.01 CNY.

Unit price of retained messages: 0.010 CNY/million messages/hour

Here is an example of billing: 
- If the total number of retained messages in Queue A for its Topic is 1,323,450 on May 20, 2016 from 16:00 to 17:00, the message retention fee for Queue A within an hour is 0.01 CNY

### Outbound Traffic Fee

Tencent Cloud's traffic billing rules: The inbound traffic of Topic is free, while the outbound traffic of Topic to publish subscriptions is charged. (During alpha test, the public network traffic is also charged. So it is recommended that you perform alpha test via private network API address.)


Billing method: Mainland China: 0.80 CNY/GB; Hong Kong: 1.00 CNY/GB; North America: 0.50 CNY/GB

Billing dimension: The outbound traffic fee will be charged separately for a certain Topic. For multiple subscribers, the outbound traffic will be accumulated

| Traffic Type | Definition | Usage | Price |
|---------|---------|---------|---------|
| Inbound traffic | Data traffic transmitted to CMQ | All | Free |
| Outbound traffic of private network (in the same region) | The traffic generated when CMQ-Topic delivers data within the same region (via Tencent Cloud's private network) | All | Free |
| Outbound traffic of public network | The traffic generated when CMQ delivers messages by subscription (via the public network) | All | Mainland China: 0.80 CNY/GB; Hong Kong: 1.00 CNY/GB; North America: 0.50 CNY/GB |










