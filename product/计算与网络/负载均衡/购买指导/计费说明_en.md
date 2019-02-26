## Billing Items
The charges for cloud load balance service include instance rental fee and bandwidth traffic fee of backend servers. For example, if a CLB instance is associated with 3 CVMs, then the actual charges will include cost for the CLB instance and the 3 CVM instances (cost for instances will be included into network charges).

## Postpaid
The price cut has been initiated in June, 2017 regarding the load balancer with postpaid and hourly billing mode applied. You can create or terminate load balancer instance at any time, which is billed by the actually used resources. The adjustment policy is as follows:
1. The billing method for public network load balancer is adjusted from the previous prepaid 4.41 USD (0.147 USD/day) to postpaid 0.003 USD/hour. The price is reduced by more than 50%;
2. For new load balancer customers, the postpaid billing method is applied;
3. For existing customers, the fees of previous month have been liquidated in the early morning of July 31, 2017, and the new billing policy has been applied. Please make sure your account balance is sufficient.
4. The private network load balancer is still free of charge;

For hourly billing, all fees are charged every hour on the hour with no need to pay in advance.

After the postpaid mode is activated for a cloud load balancer instance, the system freezes the unit price of CLB for an hour, and settles the service fees every hour on the hour (Beijing time). The frozen fees for CLB instance will be unfrozen after you delete the instance.
For purchasing, the unit price of cloud load balancer instance is calculated on hourly basis and settled based on actual hours of use. The starting point for charging is subject to the time when the load balancer instance is successfully created, while the ending point is subject to the time when you initiate the termination operation. Use of less than one hour will be billed for one hour.

> **Note:**
>When you create postpaid cloud load balancer instance, the system freezes the cost of one hour. Please make sure your account balance is sufficient;
After the cloud load balancer is purchased, the configuration fee will continue to be charged of 0.003 USD/hour even it is idle (there is no access and backend CVM is not bound).

## Arrear Isolation Policy

- In case of arrears, the instance service will be suspended 24 hours later, and you will be reminded within 24 hours upon arrear to renew as soon as possible via SMS message/email to prevent your service from being affected by the suspension.
- If you do not renew within 24 hours of arrears, the instance service will be suspended and **isolated**. Then the service will be stopped and the cloud load balancer instance occupied by you will stop to be billed. Instance-related configuration data will be retained for seven days. The service will be automatically enabled for you to use if the arrears is paid off within seven days. Arrears for more than seven days will be considered as that users actively abandon the services of cloud load balancer, and the relevant configuration data will be released.
- Tencent Cloud will send a reminder SMS message/email one day before the release of isolated instance. Relevant configuration data will be permanently deleted after the instance is released, and cannot be restored.

>**Note: **
>Cloud load balancer will not be actively unbound with the CVM. When a **CVM** is isolated (go into recycle bin for CVMs of annual or monthly plan, or be in arrears for more than two hours for CVMs of Bill-by-Traffic plan), its binding relationship with the LB will be terminated.

## FAQs:

1. How often will a deduction be performed for hourly billing?
A: Once per hour;
2. Is the price reduced by more than 50% after adjustment?
A: It is 0.147 USD/day for the old billing method and you need to pay 30 × 0.147 = 4.41 USD for consecutive 30-day use.
It is 0.003 USD/hour for the new billing method and you need to pay 0.003 × 24 × 30 = 2.16 USD for consecutive 30-day use. Therefore, you save (4.41 - 2.16) / 4.41 × 100% = 51%.
3. Why billing method is changed?
A: The postpaid method is more flexible, and do not need to freeze the cost in advance. You can release instances at any time when you do not need them, and save cost with the pay-as-you-go mode.

## Billing for Cross-region Binding

Cloud load balancer cross-region binding feature allows you to modify the region attributes of your backend CVM for cross-region binding. For example, you can bind LBs in Beijing, Shanghai and other cities to the backend cluster in Guangzhou. The feature is in the process of beta test for now. If you need to try this feature, please submit a
[Ticket](https://console.cloud.tencent.com/workorder/category/create?level1_id=6&level2_id=163&level1_name=%E8%AE%A1%E7%AE%97%E4%B8%8E%E7%BD%91%E7%BB%9C&level2_name=%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1%20LB) for application.

Its billing method is as follows:
1. Intra-region binding: free.
2. Cross-region binding (private network cross-region binding & basic network cross-region binding)
	- Postpaid on a daily basis.
	- Calculated as the peak bandwidth of the day multiplied by the applicable tiered price.
	- Peak bandwidth of the day is calculated as: bandwidth is captured once every 5 minutes, and the maximum one out of both inbound and outbound bandwidth of that day is taken as the peak bandwidth.
For more information, please see the following table:

<table>
        <tbody>
                <tr>
            <th style="width: 10%;" rowspan="2">Feature</th>
            <th style="width: 25%;" rowspan="2">Billing Method</th>
                        <th style="width: 25%;" rowspan="2">Configuration</th>
            <th style="width: 40%;" colspan="4">Price</th>
        </tr>
        <tr>
            <th>Beijing<br>Chengdu<br>Shanghai<br>Shanghai Finance Zone<br>Guangzhou<br>Shenzhen Finance Zone</th>
                        <th>Hong Kong</th>
                        <th>Singapore<br>Silicon Valley<br>Frankfurt</th>
            <th>Toronto</th>
        </tr>
                <tr>
        <td>Intra-region binding</td>
                <td colspan="6" >　　　　　　　　　　　　　　　　　　　　　Free</td>
                <tr>
                <tr>
            <td rowspan="5">Cross-region binding</td>
                        <td rowspan="5">Peak bandwidth of the day<br><br>Bill by days (USD/Mbps/Day)<br><br>Peak bandwidth is calculated using the average bandwidth per 5 minutes<br></td>
                        <td>(0 , 20] Mbps</td>
                        <td>2.941</td>
                        <td>-</td>
                        <td>-</td>
                        <td>-</td>
        </tr>
           <tr>
                <td>(20 ,100] Mbps</td>
                        <td>1.765</td>
                        <td>-</td>
                        <td>-</td>
                        <td>-</td>
                </tr>
                <tr>
                <td>(100 , 500] Mbps</td>
                <td colspan="4" rowspan="4">　Please consult with business representative<br>
                </tr>
                <tr>
                <td>(500 , 2000] Mbps</td>
                </tr>
             <tr>
                <td >> 2000 Mbps</td>
                </tr>
                    <tr>
</tbody></table>

>**Note:**
>  Contact business department to consult more about prices.

**Example:**
If the cloud load balancer is in Shanghai and the backend CVM is in Guangzhou, and the peak outbound bandwidth of the day is 20 Mbps and the peak inbound bandwidth is 30 Mbps, the cost of the day is: 30 * 1.765 = 52.95 USD, which is charged by cloud load balancer side.
