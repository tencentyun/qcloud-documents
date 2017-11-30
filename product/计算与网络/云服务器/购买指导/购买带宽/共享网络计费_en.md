
<!--Before reading this document, you need to learn about Tencent CVM [Network Billing Methods]().
This document describes the billing methods in shared networks. For more information about billing methods in exclusive networks, see [Billing Methods in Exclusive Networks]().-->

Shared network is a mode in which multiple CVMs share the network services and interact with each other.
Tencent Cloud provides a shared network service – billing by bandwidth package.

>**Note:**
>To use shared network, please apply via the ticket system.


### Billing by Bandwidth Package
Billing by bandwidth package is a billing method on a monthly basis for shared networks. When you have activated bandwidth package service, you are billed based on the **monthly peak value** of shared bandwidth for CVMs under your account. The charges in this mode consist of **in-package charge** and **outside-package charge**.

#### Billing Method
For billing by bandwidth package, you can only purchase the bandwidth package for the next month. (For example, you can only purchase the package for February in January). After selecting the maximum bandwidth of the package, you can make the payment at the "price of in-package bandwidth" as stated in the table below. The purchased bandwidth package takes effect from the beginning of the next month.

| Region | In-package bandwidth | Outside-package bandwidth |
|---------|---------|---------|
| Beijing, Shanghai, Guangzhou, Hong Kong, Singapore, Silicon Valley | 100 CNY/Mbps | 108 CNY/Mbps |
| Toronto | 200 CNY/Mbps | 216 CNY/Mbps |

Upon the billing date (at the end of each month or when the user unsubscribes the package), the system automatically calculates the "average daily bandwidth peak" as described below:
1. Daily bandwidth peak
You can find the daily bandwidth peak of public network on the "Traffic Monitoring" page of the "Cloud Monitoring" tab in the Tencent Cloud console. One sample is captured every 5 minutes (288 values in a day). The top four values among the 288 values are ruled out and the fifth largest value is taken as the daily bandwidth peak.
2. Average daily bandwidth peak
The average daily bandwidth peak is the average of the bandwidth peaks for the top 5 days ranked by daily bandwidth peak for the usage period of the bandwidth package.
3. Calculate the bandwidth package charge
 - Upon the billing date, if the average daily bandwidth peak (calculated in Step 2) under the account does not exceed the maximum bandwidth of the purchased package, no additional charge needs to be paid.
 - If the average daily bandwidth peak (calculated in Step 2) exceeds the maximum bandwidth of the purchased package (the actual usage of bandwidth for CVM servers under the account is not restricted by the bandwidth package), the extra bandwidth beyond the package is charged at the "price of outside-package bandwidth" as stated in the above table.
4. If the bandwidth package is used for less than 30 days, the bandwidth package charge in Step 3 is calculated based on the average daily bandwidth peak calculated in Step 2. Then the actual payable charge is calculated as follows: Actual payable charge=Bandwidth package charge \* Actual number of usage days/30.

#### Purchase Procedure
To use this billing method, please [submit a ticket](https://console.cloud.tencent.com/workorder/category/create?level1_id=6&level2_id=7&level1_name=%E8%AE%A1%E7%AE%97%E4%B8%8E%E7%BD%91%E7%BB%9C&level2_name=%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%99%A8%20CVM) to apply. If you've already applied for it, [click here](http://manage.qcloud.com/shoppingcart/shop.php?tab=broadband) to go to the purchase page.

#### Billing Description
- If project-based billing is enabled, the system calculates the total charge for bandwidth package as described above, then calculates the average daily bandwidth peak individually for each project (as described in Step 2), and then calculates the charge payable for each project based on the proportions.
- For the bandwidth package purchased under an ordinary account, the prepaid "Bill-by-bandwidth" charge for the remaining days will be returned to the complimentary account. In the first month after the bandwidth package is activated, purchasing bandwidth package is not supported and all of the used bandwidth is billed based on the price of outside-package bandwidth.

#### Billing Example
Suppose you purchased an 80-Mbps bandwidth package for April in Guangzhou on March 20, the package takes effect on April 1. If the average daily bandwidth peak in April is 120 Mbps, the payable charge=80\*100+(120-80)*108=12320 CNY.
Where,8,000 CNY is paid when you purchase the bandwidth package in March. And the rest 4,320 CNY is deducted from the balance upon settlement at the end of April.


