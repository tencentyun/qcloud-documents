
<!--Before reading this document, you need to learn about the Tencent Cloud CVM's [Public Network Billing]().
This document describes the billing methods in shared network. For more information on the billing methods in exclusive network, please see [Billing of Exclusive Public Network](). -->

The bandwidth of shared network is calculated based on the total traffic curve of multiple CVMs under the same account and the user is billed by the total bandwidth.

This billing method saves the public network cost by staggering the use of public network bandwidth for multiple CVMs during peak hours. If CVM A and CVM B reach their peak bandwidth of 100 Mbps at 12:00 and 13:00 respectively, the total peak bandwidth is also 100 Mbps, which is used as the basis for billing.

Tencent Cloud provides a shared network service: billing by bandwidth package.

>**Note:**
>You can apply for activating shared network by submitting a ticket.


### Billing by Bandwidth Package
Bandwidth package is a monthly billing method for shared network. After the bandwidth package service is activated, user is billed by the **monthly peak** of the shared bandwidth of the CVMs under the user account.

#### Billing Standard
After you have activated the shared network by submitting a ticket, the CVMs and LBs under your account are automatically billed by shared bandwidth without the need to change configurations.

| Region | Price of bandwidth in bandwidth package |
|---------|---------|
| Beijing, Shanghai, Guangzhou, Hong Kong, Singapore, Silicon Valley | 108 CNY/Mbps |
| Toronto | 216 CNY/Mbps |

At the time of billing (at the end of each month or when user unsubscribes the package), the system automatically calculates the "average daily bandwidth peak" as described below:
1. Calculate the daily bandwidth peak
You can check the daily bandwidth peak of public network on the **Traffic Monitoring** page of the **Cloud Monitor** tab in the Tencent Cloud console. A bandwidth peak value is captured every 5 minutes by default (288 values in total each day). The top four values among the 288 values are ruled out and the fifth largest value is taken as the daily bandwidth peak.
2. Calculate the average daily bandwidth peak
The average daily bandwidth peak is the average of the bandwidth peaks for the top 5 days ranked by daily bandwidth peak for the usage period of the bandwidth package.
3. Calculate the bandwidth package charge
	- If the bandwidth package is used for not less than 30 days. Charge=Average daily bandwidth peak * Unit price.
	- If the bandwidth package is used for less than 30 days, the charge for the bandwidth package in Step 3 is calculated based on the average daily bandwidth peak calculated in Step 2. Actual charge=Bandwidth package charge * Actual number of usage days/number of days of the month.



#### Purchase Procedure
To apply for activating this billing method, please submit a [ticket](https://console.cloud.tencent.com/workorder/category/create?level1_id=6&level2_id=7&level1_name=%E8%AE%A1%E7%AE%97%E4%B8%8E%E7%BD%91%E7%BB%9C&level2_name=%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%99%A8%20CVM).

#### Billing Description
- If project-based billing is enabled, the system calculates the total charge for bandwidth package as described above and the average daily bandwidth peak individually for each project (as described in Step 2), and then calculates the charge payable for each project based on the proportions.
- For the bandwidth package purchased under an ordinary account, the bandwidth fee of the CVM originally prepaid by bandwidth will be returned to the complimentary account according to the number of usage days remaining.

#### Example
Assume that a user activate a bandwidth package on March 1. The package takes effect on the day of purchase. If the actual average daily bandwidth peak for March is 120 Mbps, then charge=120*108=12,960 CNY.



