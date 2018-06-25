<!--Before reading this document, you need to learn about Tencent CVM [Network Billing Methods]().
This document describes the billing methods of the exclusive network. For information on the billing methods of the shared network, please see [Shared Network Billing]().-->

By using exclusive network, each CVM you purchased in Tencent Cloud uses an independent network, and the fee of each CVM is settled separately.
Tencent Cloud provides various billing methods of exclusive networks for different CVM types:

| CVM | Billing Methods|
|---------|---------|---------|
| Prepaid CVM| (Prepaid) Bill-by-bandwidth, Bill-by-traffic |
| Postpaid CVM| (Postpaid) Bill-by-bandwidth, Bill-by-traffic|


- **Bill-by-bandwidth**: You are billed by the specified bandwidth cap instead of the actual usage. The network speed is subject to the bandwidth cap.
- **Bill-by-traffic**: You're billed by the actual traffic usage. As bill-by-traffic calculates the outbound traffic per CVM (unit: CNY/GB, settlement on an hourly basis), the results are the same for both prepaid and postpaid CVMs.

>**Note:**
>For each CVM, you have only TWO chances to switch the billing method between bill-by-bandwidth and bill-by-traffic.

### Prepaid Bill-by-bandwidth

Prepaid bill-by-bandwidth is an exclusive network billing method for prepaid CVMs. The bandwidth cap of a single CVM can be between 0 Mbps - 200 Mbps. The total fee includes the bandwidth fee, server fee and hard disk fee. After you choose the a period (month/year) and pay the charge, you can use the CVM, hard disk and network during this time. Note: Packet loss occurs when the instantaneous bandwidth of a single CVM exceeds the bandwidth cap.

The average network fee of the prepaid bill-by-bandwidth is less than that of the bill-by-traffic. The prepaid bill-by-bandwidth is suitable for users consuming stable network bandwidth.

#### Billing Method
The unit price varies depending on regions and bandwidth options. The details are shown as follows:

| Region | Bandwidth ≦ 2 Mbps | 2 Mbps < Bandwidth ≦ 5 Mbps | Bandwidth >5 Mbps |
|---------|---------|---------| --------| 
| Guangzhou<br>Shanghai<br>Beijing<br>Hong Kong<br>Singapore| CNY 20/Mbps/Month |≦ 2Mbps: CNY 20/Mbps/Month<br> \> 2Mbps: CNY 25/Mbps/Month | ≦ 2 Mbps: CNY 20/Mbps/Month<br> \> 2 Mbps < Bandwidth ≦ 5 Mbps: CNY 25/Mbps/Month<br>\> 5Mbps: CNY 90/Mbps/Month |

| Region |Bandwidth ≦ 5 Mbps | Bandwidth >5 Mbps |
|---------|---------|---------| 
| Toronto<br>Silicon Valley | CNY 30/Mbps/Month |   ≦ 5 Mbps: CNY 30/Mbps/Month<br>\> 5 Mbps: CNY 100/Mbps/Month |

#### Purchasing Network
In the **Select a region and model** step, select **Prepaid"** as the **billing method**; in the **Select a storage and a network** step, select **Bill-by-bandwidth** as the **bandwidth-based billing method**; select the **bandwidth** between 0 and 200 Mbps as needed. Network fee is included in the total cost.

#### Adjusting Network
This billing method supports adjusting the network bandwidth. During the prepaid period, the network bandwidth can be upgraded, but cannot be degraded.

#### Billing Description
If you select the prepaid bill-by-bandwidth mode, you need to purchase the maximum public network outbound bandwidth (QoS), and pay service fees for one month, several months, even several years in advance. If the peak bandwidth exceeds QoS, packet loss occurs.

>**Note:**
>The prepaid bill-by-bandwidth mode of the exclusive network is only available for prepaid CVMs.

### Postpaid Bill-by-bandwidth

Postpaid bill-by-bandwidth is an exclusive network billing method for postpaid CVMs. The maximum bandwidth of a single CVM is between 0 Mbps - 100 Mbps. The price per hour includes the bandwidth cost, host cost and hard disk cost. After you select your configuration options, the system freezes the unit price of the product for an hour and settles the service fees for the preceding cycle every hour on the hour. The billing is accurate to seconds. Note: Packet loss occurs when the instantaneous bandwidth of a single CVM exceeds the maximum bandwidth.

The charges billed in postpaid bill-by-bandwidth mode are subject to your configurations and usage period. This mode is suitable for customers requiring highly flexible host loads.

#### Billing Method

The unit price varies depending on regions and bandwidth options. The details are shown as follows:

| Region | Bandwidth ≦ 5 Mbps | Bandwidth > 5 Mbps |
|---------|---------|---------| 
| Mainland China, Toronto, Silicon Valley | CNY 0.063/Mbps/Hour | ≦ 5 Mbps: CNY 0.063/Mbps/Hour<br>> 5 Mbps: CNY 0.25/Mbps/Hour |
| Hong Kong | CNY 0.08/Mbps/Hour | ≦ 5 Mbps: CNY 0.08/Mbps/Hour<br>> 5 Mbps: CNY 0.25/Mbps/Hour |
| Singapore | CNY 0.0625/Mbps/Hour | ≦ 5 Mbps: CNY 0.0625/Mbps/Hour<br>> 5 Mbps: CNY 0.25/Mbps/Hour |

>**Note:**
- If you change the network bandwidth more than once within one hour, you are billed based on the maximum bandwidth.
- Billing is accurate to seconds and settled on an hourly basis.

#### Purchase Procedure

In the **Select a region and a model** step, select "Postpaid" as the **billing method**; in the **Select a storage and a network** step, select "Bill-by-bandwidth" as the **bandwidth-based billing method**; select the **bandwidth **between 0 and 100 Mbps as needed. Network cost billing and CVM cost billing are separated, but both are accurate to seconds and settled on an hourly basis.

#### Network Adjustment
This billing mode supports network bandwidth adjustment (upgrading or downgrading) at any time. If you change the network bandwidth more than once within one hour, you are billed based on the maximum bandwidth.

#### Billing Description
If you select the postpaid bill-by-bandwidth mode, you need to specify the maximum public network outbound bandwidth (QoS) and pay service fees based on the actual usage period. The billing is accurate to seconds and is settled on an hourly basis. If the peak bandwidth exceeds QoS, packet loss occurs.

>**Note:**
>The postpaid bill-by-bandwidth mode of the exclusive network is only available for postpaid CVMs.

### Bill-by-traffic
The network fees billed by traffic depend only on the outbound traffic of a single CVM, regardless of the CVM billing mode (prepaid or postpaid). You can set the maximum bandwidth for the CVM. Packet loss occurs when the instantaneous bandwidth exceeds this limit.

Bill-by-traffic is simple and pay-as-you-go. The network cost depends on the outbound traffic per unit time. This mode is suitable for customers with fluctuating network requirements to cut cost.

#### Billing Method
The unit price of the traffic varies by regions. The details are shown as follows:

| Region |Price |
|---------|---------|
| Mainland China, Singapore | CNY 0.80/GB 
| Hong Kong | CNY 1.00/GB 
| Toronto, Silicon Valley | CNY 0.50/GB 

#### Purchase Procedure
 
In the **Select a region and a model** step, select "Prepaid" or "Postpaid" as the **billing method**; in the **Select a storage and a network** step, select "Bill-by-traffic" as the **bandwidth-based billing method**; Network costs are billed separately based on the actual traffic usage. The billing is accurate to seconds and is settled on an hourly basis.

#### Network Adjustment
This billing mode supports adjusting (upgrading or downgrading) the maximum network bandwidth) at any time and the adjustment takes effect instantly.

#### Billing Description
Bill-by-traffic is calculated based on the actual outbound traffic. You can prevent traffic overflow in a short time by setting the maximum bandwidth.

#### Maximum Bandwidth Ranges
**Maximum bandwidth ranges** vary depending on the billing methods and configurations of CVMs. The details are shown as follows:

- Postpaid CVM: 0-100 Mbps
- Prepaid CVM:

| Number of cores | Bandwidth Cap (Mbps) |
|---------|---------|
| Number of cores <= 8 | 0-200 |
| 8 < Number of cores < 24 | 0-400 |
| Number of cores => 24 | 0-400; or no maximum limit |

>**Note:**
>The postpaid bill-by-traffic mode of the exclusive network is available for prepaid and postpaid CVMs.

### Billing Examples
#### Example 1
Suppose you buy a package of 5 Mbps prepaid bandwidth for one month. The cost is CNY 25/Mbps/month \* 5 Mbps = 125 (CNY).
Suppose the average used bandwidth is 3 Mbps = 0.375 MB/sec.
The traffic for this month is 0.375 MB/second \* 30 \*24 \*60 \*60 = 972,000 MB = 949.219 GB.
The cost in the bill-by-traffic mode is 949.219GB \* 0.80 (CNY)/GB = 759.375 (CNY)
If the required bandwidth is stable, the cost in the bill-by-bandwidth mode (CNY 125/month) is less than that in the bill-by-traffic mode (CNY 759.375/month).
**If the required bandwidth is stable, the cost in the bill-by-bandwidth mode is less than that the in the bill-by-traffic mode.**

#### Example 2
Suppose you buy a package of 5 Mbps prepaid bandwidth for one month. The cost is CNY 25/Mbps/month \* 5 Mbps = 125 (CNY).
The traffic in the bill-by-traffic mode is 125/(CNY 0.8/GB) = 156.25 GB.
If the traffic can reach 5 Mbps for 2.4 hours out of 24 hours, i.e. 0.625 MB/s, and the other time period is ignored, the traffic is 0.625\* 30\* 2.4\* 60\* 60/1024=158.20 GB (slightly greater than the prepaid monthly traffic package of the same price).
2.4h/24h = 10%.
**In this example, the bandwidth is less than 5 Mbps, it's recommended to use bill-by-traffic mode if network utilization is less than 10%, and bill-by-bandwidth mode if the network utilization is greater than 10%.**

