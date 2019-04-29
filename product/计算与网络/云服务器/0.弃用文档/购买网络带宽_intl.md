All network types provided by Tencent Cloud use BGP multi-line carrier access to guarantee line quality. You can choose as needed. Tencent CVMs in two billing modes (including Annual/Monthly Package and Pay by Traffic) can choose the following two pay-by-bandwidth standards:

1) Pay by Traffic

　　Billing is based on the outbound public network traffic of CVMs, in units of GB (1 Byte = 8 bits)
	
　　Characteristics: simple billing rules, pay as you go, to reduce costs of users with highly fluctuating network conditions. In order to prevent burst traffic causing high costs, you can specify the bandwidth limit, beyond which packets will be discarded without incurring costs. 
	
2) Pay by Bandwidth

　　Billing is based on the outbound public network bandwidth of CVMs, in units of Mbps (bit)
	
　　Characteristics: Fixed bandwidth, traffic unit price lower than that of pay-by-traffic, suitable for those users consuming rather stable network bandwidth.
	
>Note:
>1. When your bandwidth is 0 Mbps, the CVM instance is not allocated with the public IP address, does not support the outbound traffic, and cannot be used as a public network gateway (use cautions in selection).



## Exclusive network

Exclusive bandwidth means that each of your CVMs has a separate network. Network fees of different CVMs will be calculated separately. 
- Tencent Cloud provides two exclusive network billing modes for annual/monthly-package CVMs: (Annual/Monthly Package) Pay by Bandwidth and Pay by Traffic
- Tencent Cloud provides two exclusive network billing modes for pay-by-traffic CVMs: (Pay per use) Pay by Bandwidth and Pay by Traffic

The pay-by-bandwidth mode can be reckoned as the bandwidth mode provided by carriers in usual home network environment: the maximum bandwidth limit is set and fees are based on this limit, but irrelevant with actual data usage. The network speed is limited to the maximum bandwidth.

The Pay-by-Traffic mode can be considered as the traffic mode provided by mobile carriers: billing is based on the actual network traffic. As in the Pay-by-Traffic mode, billing is based on the outbound traffic of a single CVM (billing in units of CNY/GB, settled every hour), it makes no different to annual/monthly-package CVMs and pay-by-traffic CVMs. Later we will describe it altogether. 

>Note: <font color="red">The pay-by-bandwidth network mode can be switched at any time to the pay-by-traffic mode, which becomes effective immediately. </font> However, this operation is <font color="red"> irreversible </font>: that is, the pay-by-traffic mode cannot be switched to the pay-by-bandwidth mode.

>Note:  In principle, Tencent Cloud allocates to users an inbound public network bandwidth in 1:1 proportion to the outbound bandwidth they purchased. However, since the inbound bandwidth is generally lower than the outbound bandwidth, Tencent Cloud will lift the inbound bandwidth limit on users when the overall inbound bandwidth in the current availability zone is lower than the outbound bandwidth, allowing users to exceed the limit and therefore improving user experience. When the overall inbound bandwidth in the current availability zone becomes higher than the outbound bandwidth, the inbound bandwidth limit will be put again on users, first on those users whose inbound bandwidth is extremely different from the outbound bandwidth.

### Prepaid CVM + Pay by Bandwidth

The Annual/Monthly Package + Pay by Bandwidth mode is a network billing mode available for prepaid annual/monthly-package CVMs. You select the maximum bandwidth value (0 Mbps - 200 Mbps) for a single CVM. The bandwidth fees are calculated into the total price along with the CVM and hard disk fees. You choose the time period (month/year) and pay the corresponding total amount. Then you can use the CVM, hard disk and network during this period. It should be noted that packet loss occurs when the instantaneous network speed of a single CVM exceeds the maximum bandwidth value.

The average network cost in the Annual/Monthly Package + Pay by Bandwidth mode is lower than that of the pay-by-traffic mode, and it is suitable for those users consuming rather stable network bandwidth.

#### Charging standards

| Region |Selected bandwidth  2 Mbps |  2 Mbps  Selected bandwidth  5 Mbps | Selected bandwidth > 5 Mbps |
|---------|---------|---------| 
| Guangzhou <br> Shanghai <br> Beijing <br> Hong Kong <br> Singapore| 20 CNY/Mbps/month |  The part  2 Mbps: 20 CNY/Mbps/month <br>The part > 2 Mbps: 25 CNY/Mbps/Month | The part  2 Mbps: 20 CNY/Mbps/month <br>The part > 2 Mbps and  5 Mbps: 25 CNY/Mbps/month <br>The part >5 Mbps part: 90 CNY/Mbps/month |

| Region | Selected bandwidth  5 Mbps | Selected bandwidth > 5 Mbps |
|---------|---------|---------| 
| North America |30 CNY/Mbps/month | The part  5 Mbps: 30 CNY/Mbps/month <br>\ The part > 5 Mbps: 100 CNY/Mbps/month |
>Note: One-year services only need 10 months of fees

For example: if you purchase a year of 10 Mbps network bandwidth for the CVM in Beijing, then your cost is:
(2\*20+3\*25+5\*90)\*10= 5650 CNY

#### Purchase procedure
Select "Annual/Monthly Package" for the user billing mode and "Pay by Bandwidth" for the bandwidth. You can select a value from 0 to 200 Mbps. The network fees are calculated into the Annual/Monthly Package fees.

#### Network adjustment
Network bandwidth adjustment (upgrade, but not downgrade) is supported. You can upgrade network bandwidth at a scheduled time. 

#### Billing instructions

Annual/Monthly Package + Pay by Bandwidth users need to purchase the maximum outbound bandwidth (QoS), and pay fees of one or more months or even several years in advance. Packets are discarded when the peak bandwidth exceeds the QoS limit.

The CVM billing mode is: **prepaid**. See [Billing Instructions - Prepaid](http://cloud.tencent.com/doc/product/213/%E8%AE%A1%E8%B4%B9%E6%A8%A1%E5%BC%8F%E8%AF%B4%E6%98%8E#1.-包年包月)


### Postpaid CVM + Pay by Bandwidth

The Pay by Traffic + Pay by Bandwidth mode is a network billing mode available for postpaid pay-by-traffic CVMs. You select the maximum bandwidth value (0 Mbps - 100 Mbps) for a single CVM. The bandwidth fees are calculated into the total price along with the CVM and hard disk fees. After you make your choice, the system will freeze the total unit price of one hour, and then make settlement every hour on the hour for the last billing cycle. Billing of all products is accurate to seconds. It should be noted that packet loss occurs when the instantaneous network speed of a single CVM exceeds the maximum bandwidth value.

In the Pay by Traffic + Pay by Bandwidth mode, costs entirely depend on user configuration and duration. It has high elasticity and is suitable for those users who have high requirements for CVM load elasticity.

#### Charging standards

| Price | Selected bandwidth  5 Mbps | Selected bandwidth > 5 Mbps |
|---------|---------|---------| 
| Mainland China, North America |0.063 CNY/Mbps/hour | The part  5 Mbps: 0.063 CNY/Mbps/hour <br> The part > 5 Mbps: 0.25 CNY/Mbps/hour |
| Hong Kong |0.08 CNY/Mbps/hour | The part  5 Mbps: 0.08 CNY/Mbps/hour <br> The part > 5 Mbps: 0.25 CNY/Mbps/hour |
| Singapore |0.0625 CNY/Mbps/hour | The part  5 Mbps: 0.0625 CNY/Mbps/hour <br> The part > 5 Mbps: 0.25 CNY/Mbps/hour |

>Note:
- If you change network bandwidth several times during the hour, billing is based on the maximum bandwidth
- Billing accuracy to seconds, settled every hour

For example, if you purchase 10 Mbps network bandwidth in mainland China and the actual duration is 2.5 hours, then your cost is:
(0.063\*5+0.25\*5)\*2.5= 3.91 CNY

#### Purchase procedure

Select "Pay by Traffic" for the user billing mode and "Pay by Bandwidth" for the bandwidth. You can select a value from 0 to 100 Mbps. Network costs and CVM costs are calculated separately, billing in seconds, settled every hour.

#### Network adjustment
In the Pay by Traffic + Pay by Bandwidth mode, network bandwidth adjustment (both upgrade and downgrade) at any time is supported. If you change network bandwidth several times during the hour, billing is based on the maximum bandwidth

#### Billing instructions
Pay per use + Pay by Bandwidth users need to set the maximum outbound public network bandwidth (QoS), and pay as they go, billing accuracy to seconds, settled every hour. Packets are discarded when the peak bandwidth exceeds the QoS limit.

The CVM billing mode is: **Pay per use**. [See Billing Instructions - Postipaid](http://cloud.tencent.com/doc/product/213/%E8%AE%A1%E8%B4%B9%E6%A8%A1%E5%BC%8F%E8%AF%B4%E6%98%8E#2.-Pay by Traffic)


### Pay by Traffic
In the Pay-by-Traffic mode, network costs are determined solely by the outbound traffic of a single CVM, regardless of the CVM billing mode (Prepaid or postpaid). You can set the maximum bandwidth limit. Packet loss occurs when the instantaneous network speed of a single CVM exceeds the limit.

#### Charging standards

| Region | Price | 
|---------|---------|
| Mainland China, Singapore | 0.80 CNY/GB | 
| Hong Kong | 1.00 CNY/GB | 
| North America, American West | 0.50 CNY /GB | 

#### Purchase procedure
Select "Annual/Monthly Package" or "Pay by Traffic" for the user billing mode and then select "By Data Usage" from the bandwidth. The network cost is calculated separately, based on your actual traffic, billing accuracy to seconds, settled every hour.

#### Network adjustment
Network bandwidth adjustment (both upgrade and downgrade) at any time is supported and becomes effective in real time.

#### Billing instructions
Pay-by-Traffic is based on your actual outbound traffic. You can set the maximum bandwidth limit to prevent possible traffic overflow in a short period.

#### Peak bandwidth range
- Pay-by-traffic CVMs: 0-100 Mbps
- Annual/monthly-package CVMs:

| Number of cores | Peak bandwidth range (Mbps) | 
|---------|---------|
| Number of cores  8 | 0-200 | 
| 8 < Number of cores <24 | 0-400 | 
| Number of cores  24 | 0-400, or no upper limit | 

CVM billing mode: **Prepaid ** and **Postpaid**. [See Billing Instructions](http://cloud.tencent.com/doc/product/213/%E8%AE%A1%E8%B4%B9%E6%A8%A1%E5%BC%8F%E8%AF%B4%E6%98%8E)

Pay-by-Traffic is featured by simple rules and paying as you go. Costs entirely depend on your actual outbound traffic per unit time. Suitable for those users with highly fluctuating network, to reduce their costs.

### Price comparison examples
Assume you purchase 5 Mbps bandwidth for the annual/monthly CVM. Then the cost is 25 CNY/Mbps/month \* 5 Mbps = 125 CNY.

Suppose your average bandwidth is 3 Mbps = 0.375 MB/s.

Monthly traffic is 0.375 MB/s \* 30 \*24 \*60 \*60 = 972000 MB = 949.219 GB.

Convert it into pay-by-traffic price: 949.219 GB\* 0.80 CNY/GB = 759.375 CNY

If you have a rather stable network, then 125 CNY/month in pay-by-bandwidth mode < 759.375 CNY/month in pay-by-traffic mode.

** For users with stable bandwidth, pay-by-bandwidth mode produces lower costs than pay-by-traffic mode. **

Still assume you purchase 5 Mbps bandwidth for the annual/monthly CVM. Then the cost is 25 CNY/Mbps/month \* 5 Mbps = 125 CNY.

Convert 125 CNY into traffic in the pay-by-traffic mode: 125/(0.8 CNY/GB) = 156.25 GB

Suppose for 2.4 hours each day (24 hours), you can use the full 5 Mbps = 0.625 MB/s, other periods ignored. Convert it into traffic:  0.625 \* 30 \* 2.4 \* 60 \* 60 /1024 = 158.20 GB (slightly higher than the equivalent monthly traffic in the Annual/Monthly Package mode)

2.4 hours/24 hours = 10%

** Pay by Traffic is recommended when network utilization is below 10%. If it is above 10%, pay-by-bandwidth mode is recommended. **

## Shared network

Shared network means that the network service is shared among multiple CVMs, which affect each other. Tencent Cloud provides a shared network mode: bandwidth package billing.
**To use this feature, please [submit a ticket](https://console.cloud.tencent.com/workorder/category/create?level1_id=6&level2_id=7&level1_name=%E8%AE%A1%E7%AE%97%E4%B8%8E%E7%BD%91%E7%BB%9C&level2_name=%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%99%A8%20CVM). 
[Click here to purchase](http://manage.qcloud.com/shoppingcart/shop.php?tab=broadband) once your application is approved.**

### Bandwidth package billing
Bandwidth package is a monthly package for shared network. After you activate the bandwidth package service, your billing will be based on the <font color="red">monthly peak value</font> of the shared bandwidth for your CVM. Fees collected in this mode consist of two parts: <font color="red">inclusive fees of the package</font> and <font color="red">exclusive fees of the package</font>.

#### Charging standards
Bandwidth packages users can only purchase bandwidth packages till the next month (that is, bandwidth packages of two months). You first select the maximum bandwidth value in the package and then <font color="red">pay</font> fees according to "Unit Price in Bandwidth Packet" shown in the following table. Now the bandwidth package has not become effective.  The bandwidth package will become effective at the beginning of a calendar month.


|  | Unit price in bandwidth package | Unit price out of Bandwidth package |
|---------|---------|---------|
| North America | 200 CNY/Mbps |216 CNY/Mbps |
| North America | 200 CNY/Mbps |216 CNY/Mbps |

Upon settlement (at the end of a calendar month or when you actively return the bandwidth package), the system automatically calculates "average daily peak bandwidth". The calculation method is as follows:

1) Calculate daily peak bandwidth
You can view the peak public network bandwidth of daily statistics on the "Traffic Monitoring" page in the "Cloud Monitoring" tab of Tencent Cloud console. By default, Tencent Cloud obtains a statistic value every 5 minutes and 288 values in a day. The system ignores the top four largest values among those 288 values and uses the fifth largest value as the daily peak bandwidth value.

2) Calculate average daily peak bandwidth
The average daily peak bandwidth is calculated as follows: average the daily peak bandwidth values of 5 days with the largest values in the use period of the bandwidth package.

3) Calculate bandwidth package fees
- Upon settlement, if the daily peak bandwidth of your account (calculated in Step 2) does not exceed the maximum bandwidth value of the bandwidth package, no extra cost is required in addition to the original package fees.
- Upon settlement, if the daily peak bandwidth of your account (calculated in Step 2) exceeds the maximum bandwidth value of the bandwidth package (the package does not limit the actual bandwidth of your CVM), fees of the excessive part is calculated according to the "Unit Price out of Bandwidth Package" as shown in the table above.

4) If the use of your bandwidth package account is less than one month, first calculate the bandwidth package fees (in Step 3) according to the average daily peak value calculated in Step 2: Actual fees = Bandwidth package fees * Actual consumption days /30

#### Charge example
Suppose you purchase, on the March 20, an April 80 Mbps bandwidth package in Guangzhou, which becomes effective on April 1. The actual average daily peak bandwidth in April is 120 Mbps, so the fees you need to pay = 80\* 100 + (120-80) * 108 = 12320 CNY.
- You need to pay 8,000 CNY when you purchase the bandwidth package in March
- The remaining 4,320 CNY will be deducted upon settlement at the end of April

#### Purchase restrictions
- When the itemized settlement function is enabled for your account, the total fees of the bandwidth package for your account will be calculated as a whole according to the above rules. Then the fees of different items are calculated proportionately according to the average daily peak bandwidth independently calculated for each item (as in Step 2).
- When an ordinary account purchases a bandwidth package, the residual value of its original payment of the Annual/Monthly Package + Pay by Bandwidth will be returned to the free gift account corresponding to the ordinary account, based on the remaining days of the CVM. When the bandwidth package service is activated, package fees for the first month are not support. All network fees in the first month calculated according to excessive bandwidth.
> <font color="red">Note: After you purchase a bandwidth package, you will no longer be able to purchase pay-by-traffic CVMs. Please terminate all pay-by-traffic CVMs before purchasing a bandwidth package. </font>


## Violation treatment
No crawler or faked order operation is allowed on the Tencent Cloud platform. Once the security team discovers these operations, such accounts will be treated with traffic restriction or blocked.

