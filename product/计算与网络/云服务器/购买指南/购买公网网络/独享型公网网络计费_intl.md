Before reading this document, you need to learn about CVM's [Overview of Billing Methods for Public Network](https://cloud.tencent.com/document/product/213/10578).
This document describes the billing methods of the exclusive public network. For more information on the billing methods of the shared network, please see [Billing of Shared Public Network](https://cloud.tencent.com/document/product/213/10580).

## Overview
Exclusive network means that each CVM you purchased in Tencent Cloud uses an independent public network, and the fee of each CVM is settled separately.
Tencent Cloud provides various billing methods for the exclusive networks used by different CVMs:

| CVM | Exclusive Public Network Billing Methods |
|---------|---------|---------|
| Prepaid CVM | (Prepaid) Bill-by-bandwidth, Bill-by-traffic |
| Postpaid CVM | (Postpaid) Bill-by-bandwidth, Bill-by-traffic |

- **Bill-by-bandwidth** is similar to the bandwidth-based billing for home networks provided by ISPs. In this mode, CVMs are billed by the specified maximum bandwidth instead of the actual usage. The network speed is subject to the maximum bandwidth.
- **Bill-by-traffic** is similar to the traffic-based billing provided by ISPs. In this mode, CVMs are billed by the actual traffic usage. Because both prepaid and postpaid CVMs are billed by the outbound traffic of each CVM on an hourly basis (in GB), we will only describe this mode for once.

>**Note:**
>You can switch the billing method for each CVM between bill-by-bandwidth and bill-by-traffic for only twice.

## Bill-by-Bandwidth for Prepaid CVMs

Prepaid bill-by-bandwidth is an exclusive network billing method for prepaid CVMs. You can select the bandwidth value for a single CVM. The bandwidth fee is included in the total price along with CVM and disk fees. After you choose the time (mm/yy) and pay the charge, you can use the CVM, hard disk and network during this time. Note: Packet loss occurs when the instantaneous bandwidth of a single CVM exceeds the maximum bandwidth.

The average network fee of the prepaid bill-by-bandwidth is less than that of the bill-by-traffic. The prepaid bill-by-bandwidth is suitable for users consuming stable network bandwidth.

### Billing standard
The unit price varies depending on regions and bandwidth options. The details are shown as follows:

| Region | Bandwidth≦2 Mbps | 2 Mbps< Bandwidth≦5 Mbps |  Bandwidth>5 Mbps |
|---------|---------|---------| --------| 
| Guangzhou<br>Shanghai<br>Beijing<br>Hong Kong<br>Singapore | 20 CNY/Mbps/month | ≦2 Mbps: 20 CNY/Mbps/month<br>\>2 Mbps: 25 CNY/Mbps/month | ≦2 Mbps: 20 CNY/Mbps/month<br>\2 Mbps<bandwidth≦5 Mbps: 25 CNY/Mbps/month<br>\>5 Mbps: 90 CNY/Mbps/month |
| Chengdu | 18 CNY/Mbps/month | ≦2 Mbps: 18 CNY/Mbps/month<br>\>2 Mbps: 22 CNY/Mbps/month | ≦2 Mbps: 18 CNY/Mbps/month<br>\ 2 Mbps<bandwidth≦5 Mbps: 22 CNY/Mbps/month<br>\>5 Mbps: 80 CNY/Mbps/month |

| Region | Bandwidth≦5 Mbps | Bandwidth>5 Mbps |
|---------|---------|---------| 
| Toronto<br>Silicon Valley | 30 CNY/Mbps/Hour | ≦5 Mbps: 30 CNY/Mbps/Hour<br>\>5 Mbps: 100 CNY/Mbps/Hour |
| Korea<br>Frankfurt | 20 CNY/Mbps/Hour | ≦5 Mbps: 20 CNY/Mbps/Hour<br>\>5 Mbps: 80 CNY/Mbps/Hour |
### Purchase procedure
In the **Select a region and a model** step, select **Prepaid** as the **billing method**; in the **Select a storage and a network** step, select **Bill-by-bandwidth** as the **bandwidth-based billing method**; and select the **bandwidth** as needed. Network costs are included in the total charges.

### Network adjustment
This billing method supports adjusting network bandwidth. You can upgrade the bandwidth within the prepaid period, but cannot degrade the bandwidth.

### Billing description
If you select the prepaid bill-by-bandwidth mode, you need to purchase the maximum public network outbound bandwidth (QoS), and pay service fees for one month, several months, even several years in advance. If the peak bandwidth exceeds QoS, packet loss occurs.

>**Note:**
>The prepaid bill-by-bandwidth mode of the exclusive network is only available for prepaid CVMs.

## Bill-by-Bandwidth for Postpaid CVMs

Postpaid bill-by-bandwidth is an exclusive network billing method for postpaid CVMs. You can select the bandwidth value for a single CVM. The bandwidth fee is included in the unit price per hour along with CVM and disk fees. After you select your configuration options, the system freezes the unit price of the product for an hour and settles the service fees for the preceding cycle every hour on the hour. The billing is accurate to seconds. Note: Packet loss occurs when the instantaneous bandwidth of a single CVM exceeds the maximum bandwidth.

The charges billed in postpaid bill-by-bandwidth mode are subject to your configurations and usage period. This mode is suitable for customers requiring highly flexible host loads.

### Billing standard

The unit price varies depending on regions and bandwidth options. The details are shown as follows:

| Region | Bandwidth≦5 Mbps | Bandwidth>5 Mbps |
|---------|---------|---------| 
| Mainland China, Toronto, Silicon Valley, Korea and Frankfurt | 0.063 CNY/Mbps/Hour | ≦5 Mbps: 0.063 CNY/Mbps/Hour<br>>5 Mbps: 0.25 CNY/Mbps/Hour |
| Hong Kong | 0.08 CNY/Mbps/Hour | ≦5 Mbps: 0.08 CNY/Mbps/Hour<br>>5 Mbps: 0.25 CNY/Mbps/Hour |
| Singapore and Chengdu | 0.0625 CNY/Mbps/Hour | ≦5 Mbps: 0.0625 CNY/Mbps/Hour<br>>5 Mbps: 0.25 CNY/Mbps/Hour |

>**Note:**
- If you change the network bandwidth for one or more times within one hour, the CVM is billed based on the maximum bandwidth.
- Billing is accurate to seconds and settled on an hourly basis.

### Purchase procedure

In the **Select a region and a model** step, select **Postpaid** as the **billing method**; in the **Select a storage and a network** step, select "Bill-by-bandwidth" as the **bandwidth-based billing method**; and select the **bandwidth** as needed. Network cost billing and CVM cost billing are separated, but both are accurate to seconds and settled on an hourly basis.

### Network adjustment
This billing method supports adjusting (upgrading or degrading) bandwidth at any time. If the bandwidth is changed several times during an hour, the billing is based on the highest bandwidth tier.

### Billing description
If you select the postpaid bill-by-bandwidth mode, you need to specify the maximum public network outbound bandwidth (QoS) and pay service fees based on the actual usage period. The billing is accurate to seconds and is settled on an hourly basis. If the peak bandwidth exceeds QoS, packet loss occurs.

>**Note:**
>The postpaid bill-by-bandwidth mode of the exclusive network is only available for postpaid CVMs.

## Bill-by-traffic
The network fees billed by traffic depend only on the outbound traffic of a single CVM, regardless of the CVM billing method (prepaid or postpaid). You can set the maximum bandwidth for the CVM. Packet loss occurs when the instantaneous bandwidth exceeds this limit.

Bill-by-traffic is simple and pay-as-you-go. The network cost depends on the outbound traffic per unit time. This mode is suitable for customers with fluctuating network requirements to cut cost.

### Billing standard
The unit price of the traffic varies by regions. The details are shown as follows:

| Region | Price | 
|---------|---------|
| Mainland China, Singapore, Korea and Frankfurt | 0.80 CNY/GB | 
| Hong Kong | 1.00 CNY/GB | 
| Toronto, Silicon Valley | 0.50 CNY/GB |

### Purchase procedure
 
In the **Select a region and a model** step, select **Prepaid** or **Postpaid** as the **billing method**; in the **Select a storage and a network** step, select **Bill-by-traffic** as the **bandwidth-based billing method**. Network costs are billed separately based on the actual traffic usage. The billing is accurate to seconds and is settled on an hourly basis.

### Network adjustment
This billing method supports adjusting (upgrading or degrading) the bandwidth cap at any time and the change takes effect in real time.

### Billing description
Bill-by-traffic is calculated based on the actual outbound traffic. You can prevent traffic overflow in a short time by setting the maximum bandwidth.

### Bandwidth cap options
**Bandwidth cap**: The options vary with different payment methods and CVM configurations. For more information, please see [Bandwidth Cap of Public Network](https://cloud.tencent.com/document/product/213/12523).

>**Note:**
>The postpaid bill-by-traffic mode of the exclusive network is available for prepaid and postpaid CVMs.

## Example
### Example 1
Suppose you buy a prepaid instance with the bandwidth of 5 Mbps for one month. The cost is 20 \* 2 + 25 \* 3 = 115 (CNY).
Suppose the average bandwidth usage is 3 Mbps = 0.375 MB/sec.
The traffic for this month is 0.375 MB/second \* 30 \*24 \*60 \*60 = 972,000 MB = 949.219 GB.
The cost in the bill-by-traffic mode is 949.219 GB \* 0.80 CNY/GB = 759.375 (CNY)
If the required bandwidth is stable, the cost in the bill-by-bandwidth mode (115 CNY/month) is less than that in the bill-by-traffic mode (759.375 CNY/month).

**If the required bandwidth is stable, the cost in the bill-by-bandwidth mode is less than that in the bill-by-traffic mode.**

### Example 2
Suppose you buy a prepaid instance with the bandwidth of 5 Mbps for one month. The cost is 20 \* 2 + 25 \* 3 = 115 (CNY).
The traffic in the bill-by-traffic mode is 115/0.8 = 143.75 GB.
Suppose that the traffic can reach 5 Mbps for 2.4 hours in 24 hours and ignore the traffic usage in other period. The traffic is: 0.625 \* 30 \* 2.4 \* 60 \* 60 /1024 = 158.20 GB (almost the same with the traffic consumed for using 5 Mbps for 2.4 hours in each day for a month).
2.4h/24h = 10%.

**In this example (the bandwidth is less than 5 Mbps), we recommend the bill-by-traffic mode for users whose network utilization is less than 10%, and the bill-by-bandwidth mode for those whose network utilization is greater than 10%.**

