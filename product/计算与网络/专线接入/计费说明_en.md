## Billing of Physical Direct Connect
For Tencent Cloud physical Direct Connect, a one-off access fee of 15,000 CNY is charged for each line.

## Billing of Direct Connect Tunnel
For Direct Connect tunnel, a fee for cross-region interconnection may be incurred when the physical Direct Connect access point is not in the same region where the access network is located:

- If they are in the same region, Direct Connect tunnel will be free of charge;
- If not, and both endpoints are within Mainland China (excluding Hong Kong, Macao and Taiwan), a fee for domestic and cross-region interconnection will be charged;
- If not, and at least one endpoint is outside Mainland China (including Hong Kong, Macao and Taiwan), a fee for cross-border and cross-region interconnection will be charged;

A fee for cross-region interconnection is charged by actual daily bandwidth usage (based on the average bandwidth every 5 minutes). The maximum value between both inbound and outbound bandwidth peak is taken as the basis for billing.

The fees for different bandwidth usage are shown below:

| Bandwidth Usage | Within Mainland China (CNY/Mbps/day) | Outside Mainland China (CNY/Mbps/day) |
| ------------------ | ------------ | ------------ |
| 0 Mbps - 20 Mbps     | 20           | 120          |
| 20 Mbps - 100 Mbps   | 12           | 80           |
| 100 Mbsp - 500 Mbps  | 9            | 60           |
| 500 Mbps - 2000 Mbps | 7            | 40           |
| > 2000 bps         | 5            | 30           |


**Example 1**

The access point for physical Direct Connect is **Xuhui, Shanghai** and the VPC to be connected via Direct Connect tunnel is **Beijing**. The actual outbound and inbound bandwidth usages were 150 Mbps and 200 Mbps respectively on May 30.

Since the access point and the VPC are in Shanghai and Beijing (**not in the same region but both in Mainland China**), a fee for domestic and cross-region interconnection will be charged. In this case, based on the maximum bandwidth usage of the 200 Mbps and the applicable tiered price of 9 CNY/Mbps/day, the fee due on that day is 9*200 = 1,800 CNY.



**Example 2**

The access point for physical Direct Connect is **Hong Kong** and the VPC to be connected via Direct Connect tunnel is **Shanghai**. The actual outbound and inbound bandwidth usages were 30 Mbps and 15 Mbps respectively on May 30.

Since the access point and the VPC are in Hong Kong and Shanghai (**not in the same region and one endpoint outside Mainland China**), a fee for cross-border and cross-region interconnection will be charged. In this case, based on the maximum bandwidth usage of the 30 Mbps and the applicable tiered price of 80 CNY/Mbps/day, the fee due on that day is 30*80 = 2,400 CNY.

**Example 3**

The access point for physical Direct Connect is **Hong Kong** and the VPC to be connected via Direct Connect tunnel is **Hong Kong**. The actual outbound and inbound bandwidth usages were 30 Mbps and 15 Mbps respectively on May 30.

Since the access point and the VPC are both in Hong Kong (**in the same region**), no interconnection fee will be charged.
