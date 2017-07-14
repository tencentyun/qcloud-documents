Charges for CMQ include fees for number of requests, for message retention, and for outbound traffic. All fees are charged separately based on regions on an hourly basis.

## Fee for Number of Requests

In a single region, after users activate CMQ services, Tencent Cloud will provide the statistics of the API/SDK request number in message queue ***per hour***. The fee per million requests: ***2.00 CNY/million***. It is charged hourly. The number of requests is calculated in millions (accurate to two decimal places).

Here are examples of billing:

- If the total number of user requests is 1,323,454 on May, 20, 2016 from 16:00 to 17:00, the number of requests for calculation is 1.32 (million counts), and the fee for requests during this time period is 1.32 * 2.00 = 2.64 CNY.
- If the total number of user requests is 181,000 on May, 20, 2016 from 18:00 to 19:00, the number of requests for calculation is 0.18 (million counts), and the fee for requests during this time period is 0.18 * 2.00 = 0.36 CNY.

## Message Retention Fee (including message rewind fee)

The CMQ will charge the message retention fee hourly in a single region. The formula is as follows:

```
Message retention fee = Total number of messages * Unit price of retained messages
```

Unit price of retained messages: ***0.010 CNY/million messages/hour***. The total number of messages is calculated in millions. The total number of retained messages in an hour is based on the average number of retained messages per minute (i.e. the average of 60 numbers in an hour). The calculation will be accurate to two decimal places. Message rewind fee is included in the message retention fee.

Here is an example of billing: 
- If the total number of retained messages in A Queue is 1,323,450 on May 20, 2016 from 16:00 to 17:00, the message retention fee for this queue within an hour is 0.01 * 1.32 = 0.01 CNY

## Outbound Traffic Fee

Tencent Cloud's traffic billing method: The outbound traffic is charged while the inbound traffic is free. (During alpha test, the public network traffic is also charged. So it is recommended that you perform alpha test via private network API address.)

| Traffic Type | Definition | Usage | Price |
|---------|---------|---------|---------|
| Inbound traffic | Data traffic transmitted to CMQ | All | Free |
| Outbound traffic of private network (in the same region) | The traffic generated when the business systems acquire data from CMQ via private network domain of the message queue or when CMQ sends data to the business systems within the same region (via Tencent Cloud's private network) | All | Free |
| Outbound traffic of public network | The traffic generated when the business systems acquire data from CMQ via Internet domain of the message queue or when CMQ send data to the business systems within the same region (via Internet)| All | Mainland China: 0.80 CNY/GB; Hong Kong: 1.00 CNY/GB; North America: 0.50 CNY/GB |

